"""Bloque 2 de E-ELIS + correccion E1 (E-R1..E-R5, E-R7, E-R9): lectura verificada de los documentos descargados.

Idempotente (E-R9): reescribe LECTURA_FUENTES.jsonl desde cero en cada ejecucion y
recalcula (sin duplicar) las columnas de bloque 2 y de revision E1 en
PREGUNTAS_Y_RESULTADOS.csv; filtra las filas DESCARGADO_*/FALLO_*/CANDIDATO_* de
FUENTES_Y_BUSQUEDA.csv antes de re-anhadirlas desde .trabajo/elis_fuentes/INDICE_DESCARGAS.csv.

Cada cita curada indica documento (id de descarga), pagina PDF y patron; el patron debe
estar dentro de esa pagina del texto extraido ([PDF PAGE n], PyMuPDF) y falla loudly si no.
Reglas del revisor aplicadas (E-R5): ningun .* codicioso ni alternativas; cada afirmacion
del hallazgo queda cubierta por su cita registrada. tipo_evidencia distingue
'corroboracion_base' (documento ya conservado en base-4.14: urd2025) de 'nueva' (E-R3/E-R4).

Correcciones de interpretacion (E-R1 N2, E-R2/E-R3 M6, E-R4 M1) en los textos hallazgo:
- N2: retirada la afirmacion falsa de 'concepto monetario / seccion operativa'; dos medidas
  separadas (+23,1 EFE p.327 vs +25,7 nota 4.6 p.350) y 16,9 a cobrar (p.349).
- M6: Bodensee reclasificada como adquisicion importante (p.306/p.312/p.341); 117,6 (M&A
  total 2025) separado de 37,3 ('Other acquisitions' 2025); perimetro p.313 = corroboracion
  de F1 V1, no confirma el 31,5 M EUR/ano.
- M1: capex p.311-312 y taxonomia p.215-217 declarados corroboracion de la base; perimetro
  de la taxonomia anadido (p.217); no es importe del plan climatico.
- E-R7: nada de 'no publicado' absoluto; siempre 'no localizado en esta busqueda' + alcance.

Genera LECTURA_FUENTES.jsonl (registros documento + cita con patron, linea, sha256 y
tipo_evidencia) y actualiza PREGUNTAS_Y_RESULTADOS.csv y FUENTES_Y_BUSQUEDA.csv.
"""
import csv
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
TRABAJO = RAIZ / ".trabajo/elis_fuentes"
SALIDA = RAIZ / "resultados_cierre/elis_fuentes"

# Documentos ya conservados en la Release base-4.14 (su lectura es corroboracion, no evidencia nueva)
DOCS_BASE = {"urd2025"}
SHA_URD2025 = "04bfd08724e768804e7110093d3ec2cf017a7e7fe2983bacd75656d3a95cd62e"

# (pregunta, doc_id, pagina_pdf, patron, hallazgo, no_demuestra, salida_afecta)
CITAS = [
    # ---------------- M1 ----------------
    ("M1", "cgmbrochure2026", 15, r"covers investments for both growth \(new plants or to increase capacity\) and maintenance \(equipment replacement\)",
     "El capex industrial se declara que cubre crecimiento (plantas nuevas o mas capacidad) y mantenimiento (reemplazo de equipos)",
     "No da el reparto mantenimiento/crecimiento en importes por bloque ni por ano; no localizado en esta busqueda",
     "M1: flujo de partida 339,8-477,8 (45% del FCF base); nivel del motor A; ancla S2C"),
    ("M1", "cgmbrochure2026", 15, r"gross capital expenditure \(before grants\) for the financial years ended December 31, 2023, 2024 and 2025 \(excluding acquisitions\) totaled \S*€823\.9 million, \S*€887\.4 million and \S*€890\.2 million, respectively",
     "Capex bruto (antes de subvenciones, sin adquisiciones) 2023/2024/2025 = 823,9 / 887,4 / 890,2 M EUR",
     "Es bruto y agregado; no separa mantenimiento de crecimiento ni lino de industrial",
     "M1: ancla el nivel de capex bruto por ano"),
    ("M1", "fy2025_comunicado_en", 6, r"net capex were stable compared to 2024 and stood at 18\.2% as a percentage of revenue, compared to 19\.2% in 2024",
     "Net capex 2025 = 18,2% de ventas (19,2% en 2024); mejora por mejor gestion de la inversion en lino",
     "Sigue sin localizarse en esta busqueda el desglose mantenimiento/crecimiento",
     "M1"),
    ("M1", "fy2025_presentacion_en", 29, r"Net capex \(874\.7\) \(876\.0\)",
     "Net capex 2025 = 874,7 M EUR (2024: 876,0); 18,2% / 19,2% de ventas; FCF 358,6",
     "Idem: nivel, no reparto",
     "M1"),
    ("M1", "h1_2026_comunicado_en", 6, r"ratio stood at 19\.5% in H1 2026 \(versus 18\.4% in H1 2025\), reflecting the ramp up of major industrial investment projects during the half\. The ratio is expected to be around 18% by year-end",
     "H1 2026 net capex = 19,5% de ventas (18,4% H1 2025) por 'ramp up of major industrial investment projects'; esperado ~18% a cierre 2026",
     "Confirma proyectos industriales grandes en curso, sin importe ni reparto mantenimiento/crecimiento",
     "M1: capex 2026 esperado ~18%"),
    ("M1", "urd2025", 137, r"two-thirds of which ensures the maintenance of the stock in circulation",
     "URD 2025 p.137 (ya en base-4.14): 'two-thirds' del lino plano mantienen el stock en circulacion (texto fijo desde URD 2020)",
     "Proporcion parcial de un bloque (lino plano = 46,2% de ventas 2025); no es proporcion de capex total ni importe",
     "M1"),
    ("M1", "urd2025", 215, r"Capex 1,160\.0 86\.0% 842\.0 72\.6% 1\.9% 0\.0% 0\.0% 70\.7%",
     "Taxonomia UE 2025 (ya en base-4.14, corroboracion): CapEx 1.160,0 M EUR; 86,0% elegible; 842,0 M EUR (72,6%) alineado; de los alineados, 1,9 pp objetivo climatico y 70,7 pp economia circular",
     "Es un reparto por objetivo taxonomico, no mantenimiento vs crecimiento; no es el importe del plan climatico",
     "M1"),
    ("M1", "urd2025", 215, r"Taxonomy-aligned CapEx \(Circular economy goal\) 72\.6%",
     "El 72,6% de CapEx alineado corresponde al objetivo 'Circular economy goal'",
     "Casi todo el alineado es economia circular; no mide el plan climatico",
     "M1"),
    ("M1", "urd2025", 217, r"IAS 38 – €26\.2 million",
     "Perimetro de la taxonomia (p.217, corroboracion de base): incluye altas de intangibles IAS 38 = 26,2 M EUR",
     "Perimetro de la taxonomia, distinto del capex propio 890,2 (p.312); no mide plan climatico ni mantenimiento/crecimiento",
     "M1: perimetro taxonomico"),
    ("M1", "urd2025", 217, r"IFRS 16 – €183\.9 million",
     "Perimetro de la taxonomia (p.217): incluye derechos de uso IFRS 16 = 183,9 M EUR",
     "Idem: 26,2 + 183,9 + 887,1 + 62,7 = 1.159,9 ~ CapEx taxonomico 1.160,0, no el capex propio 890,2",
     "M1: perimetro taxonomico"),
    ("M1", "urd2025", 217, r"IAS 16 – €887\.1 million",
     "Perimetro de la taxonomia (p.217): incluye PP&E IAS 16 = 887,1 M EUR",
     "Idem",
     "M1: perimetro taxonomico"),
    ("M1", "urd2025", 217, r"business combinations are also included \(€62\.7 million",
     "Perimetro de la taxonomia (p.217): incluye altas por combinaciones de negocio = 62,7 M EUR (Note 2.4); goodwill excluido",
     "Idem",
     "M1: perimetro taxonomico"),
    ("M1", "urd2025", 311, r"Asset disposals 15\.3 7\.3 Investment grants 0\.2 4\.1 OUTFLOWS/INFLOWS RELATING TO PROPERTY, PLANT AND EQUIPMENT AND INTANGIBLE ASSETS \(874\.7\) \(876\.0\)",
     "Identidad capex 2025 (ya en base, corroboracion): cesiones de activos 15,3 + subvenciones 0,2; neto (874,7) frente a bruto 890,2 (p.312)",
     "Nivel, no reparto mantenimiento/crecimiento",
     "M1"),
    ("M1", "urd2025", 311, r"They represented 18\.2% of revenue in 2025 \(compared with 19\.2% in 2024\)",
     "Capex neto 2025 = 18,2% de ventas (19,2% en 2024), corroboracion de base",
     "Idem",
     "M1"),
    ("M1", "urd2025", 312, r"\(excluding acquisitions\) totaled \S*€823\.9 million, \S*€887\.4 million and \S*€890\.2 million, respectively",
     "URD 2025 p.312 (ya en base): capex bruto 2023/2024/2025 = 823,9 / 887,4 / 890,2 M EUR, sin adquisiciones",
     "Bruto y agregado",
     "M1"),
    ("M1", "cgmbrochure2026", 60, r"capex contained despite new workwear contracts and expenditure under the Climate plan",
     "Se confirma gasto bajo el Climate plan en 2025 ('expenditure under the Climate plan'), sin importe",
     "Sin importe, horizonte ni finalidad cuantificada del plan climatico en esta pagina; no localizado en esta busqueda",
     "M1: plan climatico sigue pendiente"),
    ("M1", "cgmbrochure2026", 4, r"presentation of the Group\S*s 2030 CSR roadmap \(including the Climate Strategy\)",
     "La CGM del 21-may-2026 incluye como punto de agenda (sin resolucion) la presentacion de la roadmap CSR 2030 incl. Climate Strategy",
     "La agenda anuncia la presentacion; el contenido con importes no esta en este documento",
     "M1: plan climatico"),
    # ---------------- M2 ----------------
    ("M2", "urd2025", 141, r"customer attrition rates are monitored at the Executive Committee level across all operating regions",
     "URD 2025 p.141 (corroboracion de base): las tasas de bajas de clientes se siguen a nivel de Comite Ejecutivo en todas las regiones; sin cifra publicada",
     "No publica la tasa de bajas ni por segmento ni total; no localizado en esta busqueda",
     "M2: PPA 85,7/a (28% FCF base); A1 vs A2 89,9"),
    ("M2", "fy2024_presentacion_en", 5, r"Customer retention rate back to its normative level",
     "Presentacion FY2024 p.5: 'customer retention rate back to its normative level' (2024); cualitativo, nivel normativo no cuantificado",
     "No cuantifica la tasa ni el nivel normativo",
     "M2"),
    ("M2", "factsheet2026", 1, r"4-year contracts: Monthly fixed fee",
     "Factsheet 2026: contratos de 4 anos con tarifa fija mensual (workwear = 37% de ventas)",
     "Estructura contractual, no tasa de bajas ni desembolso inicial por cliente nuevo",
     "M2"),
    ("M2", "cgmbrochure2026", 15, r"Growth investments thus make up a large percentage of this expenditure because of the initial outlay required to set up a new customer",
     "Brochure CGM p.15: el gasto de lino incluye 'the initial outlay required to set up a new customer'; la inversion de crecimiento es 'a large percentage' de ese gasto por esa dotacion inicial",
     "Cualitativo ('large percentage'), sin importe del desembolso inicial por cliente nuevo; no localizado en esta busqueda",
     "M2: dotacion a clientes nuevos que repone perdidos (enlaza M1)"),
    ("M2", "fy2025_presentacion_en", 12, r"streamlining customer onboarding and reducing implementation lead times",
     "Presentacion FY2025 p.12: plataforma CRM para acortar lead times de implementacion/onboarding de clientes",
     "Sin importe ni tasa; no identifica el desembolso inicial por cliente nuevo",
     "M2"),
    ("M2", "q3_2026_revenue", 3, r"takes a selective approach to acquiring new customers",
     "Q3 2026 p.3: 'selective approach to acquiring new customers' (disciplina de precios); cualitativo",
     "Sin tasa de bajas ni importe por cliente nuevo",
     "M2"),
    # ---------------- M6 ----------------
    ("M6", "urd2025", 313, r"revenue of more than €5\.0 million in France and €3\.0 million in other countries",
     "URD 2025 p.313 (corroboracion: F1 V1 ya lo tenia, informe 716cbd6 l550 [P: URD2025 p.313; DEU2024 p.259; URD2023 p.267]): 'major acquisitions/disposals' = empresas con ingresos anuales en la adquisicion > 5,0 M EUR en Francia y > 3,0 M EUR en otros paises (Note 2.4); el crecimiento organico solo excluye esas y el efecto divisa",
     "Define el umbral del perimetro; NO confirma el 31,5 M EUR/ano (esa media sale de los flujos de las compras pequenas, URD2025 p.341-342 y DEU2024 p.288, ya citada por F1 V1); no es finalidad de las compras",
     "M6: las compras < umbral permanecen DENTRO del organico publicado"),
    ("M6", "fy2025_comunicado_en", 11, r"calculated excluding \(i\) the impacts of changes in the scope of consolidation of “major acquisitions” and “major disposals”",
     "Comunicado FY2025 p.11 repite la misma definicion de crecimiento organico (solo excluye 'major acquisitions' y 'major disposals' segun el URD + divisa)",
     "Igual: umbral de perimetro, no finalidad",
     "M6"),
    ("M6", "fy2024_comunicado_en", 7, r"bolt-on acquisitions, with an envelope between 50 million euros and 150 million euros per year",
     "Comunicado FY2024 p.7: politica de asignacion de capital (6-mar-2025): adquisiciones bolt-on con sobre de 50-150 M EUR/ano",
     "Es un presupuesto, no un desglose de finalidad ni importes por operacion",
     "M6"),
    ("M6", "fy2025_comunicado_en", 7, r"bolt-on acquisitions, with an annual budget of between 50 million euros and 150 million euros",
     "Comunicado FY2025 p.7: ratifica el sobre bolt-on de 50-150 M EUR/ano para 2026",
     "Idem",
     "M6"),
    ("M6", "q1_2025_revenue", 1, r"3 acquisitions contributing to the consolidated revenue since January 1, 2025: Carsan in Spain, Ernst in Germany and Bodensee in Switzerland; their combined revenue was c\. 55 million euros in 2024",
     "Q1 2025 p.1: Carsan (Espana), Ernst (Alemania) y Bodensee (Suiza) consolidadas desde 1-ene-2025, ingresos combinados 2024 c. 55 M EUR. Clasificacion por pagina: en esta pagina Bodensee aparece en el grupo de 3 operaciones del trimestre; el URD 2025 la clasifica entre las SEIS adquisiciones importantes de 2025 (citas p.306/p.312/p.341)",
     "No dice que parte repone cartera perdida ni cuanto es crecimiento",
     "M6"),
    ("M6", "q1_2025_revenue", 1, r"external growth was \+2\.1% in Q1, driven by the contribution of 3 acquisitions in Spain, in Germany and in Switzerland, with annual combined revenue of c\. 55 million euros in 2024",
     "Q1 2025 p.1: esas 3 adquisiciones explican el crecimiento externo +2,1% del trimestre",
     "Sin importes por operacion ni finalidad reposicion/crecimiento",
     "M6"),
    ("M6", "q3_2026_revenue", 1, r"Recent acquisitions contributed 1\.5 percentage points to revenue growth; the pipeline remains strong",
     "Q3 2026 p.1: las adquisiciones recientes contribuyeron +1,5 pp al crecimiento del trimestre; pipeline 'remains strong'",
     "Sin importes por operacion ni finalidad",
     "M6"),
    ("M6", "q3_2026_revenue", 2, r"the acquisition of Muller contributed 0\.5 percentage points to reported quarterly revenue growth",
     "Q3 2026 p.2: la adquisicion de Muller contribuyo +0,5 pp al crecimiento del trimestre",
     "Sin importe ni finalidad",
     "M6"),
    ("M6", "q3_2026_revenue", 3, r"the acquisition of RS10 in Spain, whose revenue has been consolidated since 1 June 2026, contributed 1\.3 percentage points to reported quarterly revenue growth",
     "Q3 2026 p.3: RS10 (Espana), consolidada desde 1-jun-2026, contribuyo +1,3 pp al crecimiento del trimestre",
     "Sin importe ni finalidad",
     "M6"),
    ("M6", "fy2025_presentacion_en", 29, r"Acquisitions of subsidiaries, net of cash acquired \(117\.6\) \(183\.3\)",
     "Presentacion FY2025 p.29: M&A TOTAL 2025 en caja (filiales, neta de caja adquirida) = 117,6 M EUR (2024: 183,3). Precision registrada (adenda del coordinador): en la pagina impresa hay un marcador de nota '5' entre el rotulo y la cifra; la cita registrada lo omite. Es el total de M&A, no desglose por operacion ni por finalidad",
     "No separa adquisiciones importantes de 'Other acquisitions' (esa separacion esta en URD p.341)",
     "M6"),
    ("M6", "urd2025", 306, r"The major acquisitions the Group completed during the financial year were",
     "URD 2025 p.306, seccion 4.1.2 'Major acquisitions' (corroboracion de base): lista de las adquisiciones IMPORTANTES completadas en 2025",
     "Lista de sociedades, no importes por operacion en esta pagina (los importes estan en Note 2.4, p.341)",
     "M6: clasificacion por sociedad"),
    ("M6", "urd2025", 306, r"W\S*scherei Bodensee in Switzerland;",
     "URD 2025 p.306: Warts cherei Bodensee (Suiza) esta en la lista de adquisiciones IMPORTANTES de 2025; NO es una compra pequena",
     "La clasificacion no da su importe (columna propia en p.341) ni su finalidad",
     "M6: clasificacion Bodensee"),
    ("M6", "urd2025", 312, r"six major acquisitions in different countries where the Group is present in 2025, including the laundries W\S*scherei Bodensee in Switzerland, Bugaderia Neutral in Spain, Laros\S+ and Adrett in Germany",
     "URD 2025 p.312 (corroboracion de base): SEIS adquisiciones importantes en 2025, incl. Warts cherei Bodensee (Suiza), Bugaderia Neutral (Espana), Larose y Adrett (Alemania)",
     "Lista parcial ('including'); los importes por operacion estan en Note 2.4 p.341",
     "M6: clasificacion por sociedad"),
    ("M6", "urd2025", 341, r"2025 W\S*scherei Bodensee Bugaderia Neutral Laros\S+ Acqua\S+ash JP Muller Adrett Lavartex Other acquisitions",
     "URD 2025 p.341, Note 2.4 (corroboracion de base): cada adquisicion importante de 2025 tiene COLUMNA PROPIA (Bodensee, Bugaderia Neutral, Larose, JP Muller, Adrett, Lavartex) y 'Other acquisitions' es una columna aparte, fuera de las importantes",
     "Cabecera de tabla; los valores por columna estan en la fila NET CASH FLOW de la misma pagina",
     "M6: 117,6 frente a 37,3"),
    ("M6", "urd2025", 341, r"NET CASH FLOW \(117\.6\) \(8\.9\) \(13\.2\) \(10\.2\) \(7\.0\) \(11\.8\) \(9\.7\) \(19\.7\) \(37\.3\)",
     "URD 2025 p.341, fila NET CASH FLOW 2025 (corroboracion de base): total (117,6) = suma de las columnas propias de las adquisiciones importantes + 'Other acquisitions' (37,3, ultima columna). 117,6 = M&A TOTAL 2025; 37,3 = compras pequenas ('Other acquisitions') 2025. F1 V1 ya citaba 35,3 / 22,0 / 37,3 en 2023-25 (media 31,5) [informe 716cbd6 l550; URD2025 p.341-342; DEU2024 p.288]",
     "Importes en caja, no finalidad reposicion/crecimiento; no localizado en esta busqueda",
     "M6: separar 117,6 de 37,3"),
    ("M6", "urd2025", 327, r"Acquisition of subsidiaries, net of cash acquired[\s\S]{0,6}\(117\.6\) \(183\.3\)",
     "EFE p.327 (corroboracion de base): 'Acquisition of subsidiaries, net of cash acquired' (117,6) en la seccion de INVERSION = el mismo total 117,6 de la Note 2.4 (p.341) y de la presentacion (p.29)",
     "Total agregado, no desglose",
     "M6"),
    ("M6", "fy2025_comunicado_en", 2, r"2025 was also an active year for M&A, with many small and mid-sized acquisitions that strengthen Elis\S* network density in Europe and Latin America",
     "Comunicado FY2025 p.2: 2025 'active year for M&A, with many small and mid-sized acquisitions'; cualitativo",
     "Sin lista completa ni importes en esta pagina (Note 2.4 del URD los lista)",
     "M6"),
    # ---------------- N2 ----------------
    ("N2", "urd2025", 350, r"Net gain \(loss\) related to retirement of fixed assets 25\.7 \(1\.5\)",
     "URD 2025 nota 4.6 p.350 (corroboracion de base): dentro de OOIE 2025 figura su PROPIA linea 'Net gain (loss) related to retirement of fixed assets' +25,7 M EUR (2024: -1,5)",
     "La nota no dice que ese +25,7 sea la compensacion del seguro; no se igualan dos magnitudes parecidas sin mas evidencia",
     "N2: m0 +0,54 pp (diagnostico F1)"),
    ("N2", "urd2025", 350, r"of which monetary items \(28\.2\) \(22\.2\)",
     "URD 2025 p.350: la sublinea 'of which monetary items' es (28,2), SEPARADA de la linea de bajas +25,7: el +25,7 NO es un 'concepto monetario' en esa nota (correccion E-R1 de la afirmacion anterior)",
     "No identifica fiscalidad ni cobro en caja de la partida",
     "N2"),
    ("N2", "urd2025", 350, r"of which net gain \(loss\) on disposal of non-current assets 25\.7 \(1\.5\)",
     "URD 2025 p.350: el +25,7 figura ademas como sublinea 'of which net gain (loss) on disposal of non-current assets'",
     "Idem",
     "N2"),
    ("N2", "urd2025", 350, r"OTHER OPERATING INCOME AND EXPENSES \(3\.1\) \(18\.5\)",
     "OOIE 2025 = -3,1 M EUR (2024: -18,5); la mejora incluye menos earnouts y la partida de bajas +25,7",
     "No desagrega el cobro del seguro en caja",
     "N2"),
    ("N2", "urd2025", 327, r"Net gains and losses on disposal of property, plant and equipment and intangible assets \(23\.1\)",
     "EFE p.327 (corroboracion de base): 'Net gains and losses on disposal of PP&E and intangible assets' (23,1) aparece en la seccion OPERATIVA de la misma pagina (antes del subtotal 'NET CASH FROM OPERATING ACTIVITIES', l. registrada) y se RESTA como partida no monetaria: es una medida de RESULTADO, distinta de los +25,7 de la nota 4.6; F1 usa +23,1 para f (informe 716cbd6 l317/l328)",
     "Medida agregada de todas las bajas de PP&E e intangibles; no separa seguro de venta de activos",
     "N2: dos medidas separadas (+23,1 resultado vs +25,7 nota)"),
    ("N2", "urd2025", 327, r"Proceeds from disposal of property, plant and equipment 15\.3 7\.3",
     "EFE p.327: 'Proceeds from disposal of property, plant and equipment' 15,3 (2024: 7,3) en la seccion de INVERSION (antes del subtotal 'NET CASH FLOWS FROM INVESTING ACTIVITIES'): medida de CAJA por venta de activos",
     "No separa cobro de seguro de producto de la venta; no localized en esta busqueda el desglose",
     "N2: caja por bajas"),
    ("N2", "urd2025", 327, r"NET CASH FROM OPERATING ACTIVITIES 1,510\.6 1,452\.1",
     "EFE p.327: subtotal de la seccion operativa (ancla de posicion de la linea (23,1) en la misma pagina)",
     "Idem",
     "N2"),
    ("N2", "urd2025", 327, r"NET CASH FLOWS FROM INVESTING ACTIVITIES \(991\.5\) \(1,060\.3\)",
     "EFE p.327: subtotal de la seccion de inversion (ancla de posicion de los cobros 15,3 en la misma pagina)",
     "Idem",
     "N2"),
    ("N2", "urd2025", 349, r"Change in receivables on disposal of fixed assets 16\.9 \(0\.1\)",
     "URD 2025 nota 4.4 p.349 (corroboracion de base): a cierre 2025 quedan 16,9 M EUR por cobrar por bajas de inmovilizado (2024: (0,1)) - parte del producto de las bajas aun no cobrada en caja a cierre",
     "No identifica cuanto corresponde a seguro frente a venta de activos",
     "N2: cobro pendiente a cierre"),
    ("N2", "urd2025", 309, r"offset by a high level of insurance benefits in 2025",
     "URD 2025 p.309 (corroboracion de base): la caida de OOIE se vincula a menos earnouts, 'offset by a high level of insurance benefits in 2025'",
     "Narrativa cualitativa; no importe ni evento asegurado identificado en esta pagina; NO se iguala con el +25,7",
     "N2"),
    ("N2", "fy2025_comunicado_en", 4, r"higher level of insurance compensations in 2025",
     "Comunicado FY2025 p.4: las perdidas operativas no corrientes bajaron mucho, 'offset by a higher level of insurance compensations in 2025'",
     "Sin importe ni fiscalidad",
     "N2"),
    ("N2", "fy2025_presentacion_en", 25, r"Positive one[\s\S]{0,3}offs linked to insurance compensation",
     "Presentacion FY2025 p.25: 'Positive one-offs linked to insurance compensation' en el puente a net income 2025",
     "Sin importe en la pagina (el +25,7 esta en la nota 4.6 del URD); no se iguala con la nota",
     "N2"),
]

ESTADOS_E1 = {
    "M1": "ABIERTO - nivel de capex corroborado (bruto 823,9/887,4/890,2 y neto 874,7 = 18,2% ya en URD2025 de la base, p.311-312; H1-2026 19,5% nuevo) pero SIN reparto mantenimiento/crecimiento ni importe/horizonte del plan climatico (taxonomia 1.160,0 incluye ROU 183,9 y combinaciones 62,7, p.217; alineado 842,0 es sobre todo economia circular 70,7 pp, clima 1,9 pp, p.215); no localizado en esta busqueda (alcance: 12 docs oficiales nuevos + base ya examinada)",
    "M2": "ABIERTO - solo cualitativo (attrition 'monitored' URD p.141; retencion 'back to normative' FY2024; contratos 4 anos; 'initial outlay' por cliente nuevo sin importe, CGM p.15); no localizado en esta busqueda (mismo alcance)",
    "M6": "ABIERTO - perimetro corroborado (ya en F1 V1: informe 716cbd6 l550; URD2025 p.313): umbral 'major' >5,0 M EUR Francia / >3,0 M EUR otros paises; clasificacion 2025 con pagina: seis adquisiciones importantes con columna propia incl. Bodensee (p.306/p.312/p.341) y 'Other acquisitions' 37,3 M EUR (p.341); M&A TOTAL 2025 en caja 117,6 M EUR (p.341/p.327/presentacion p.29), separado de 37,3; sobre bolt-on 50-150 M EUR/ano; finalidad reposicion vs crecimiento no localizado en esta busqueda",
    "N2": "ABIERTO - dos medidas separadas: +23,1 M EUR EFE p.327 (bajas PP&E+intangibles; resta en seccion operativa; cobros 15,3 en inversion) y +25,7 M EUR nota 4.6 p.350 (linea propia, separada de 'of which monetary items' (28,2)); 16,9 M EUR a cobrar por bajas a cierre (p.349); narrativa de seguros sin importe (p.309, comunicado p.4, presentacion p.25) NO igualada con el +25,7; cobro/fiscalidad/reposicion no localizados en esta busqueda",
}

CORRECCION_E1 = {
    "M1": "E-R4: capex p.311-312 y taxonomia p.215-217 declarados corroboracion de la base (URD2025 ya en base-4.14); perimetro taxonomico anadido (p.217: 26,2+183,9+887,1+62,7 = 1.159,9 ~ 1.160,0); no presentado como importe del plan climatico",
    "M2": "Sin cambio material respecto a 93a9780 (solo redaccion E-R7)",
    "M6": "E-R2: Bodensee reclasificada como adquisicion IMPORTANTE (p.306/p.312, columna propia p.341); 117,6 (M&A total 2025) separado de 37,3 ('Other acquisitions' 2025, p.341). E-R3: perimetro p.313 ya conocido por F1 V1 (informe 716cbd6 l550) -> corroboracion; el umbral no confirma el 31,5 M EUR/ano (sale de p.341-342/DEU2024 p.288)",
    "N2": "E-R1: retirada la afirmacion falsa de 'concepto monetario / seccion operativa'; +25,7 va en linea propia de la nota 4.6 (p.350), separada de 'monetary items' (28,2); EFE p.327 resta (23,1) en operativo y lleva cobros 15,3 a inversion; 16,9 a cobrar (p.349); dos medidas separadas (+23,1 resultado vs +25,7 nota); seguro no igualado; N2 queda ABIERTO en cobro/fiscalidad/reposicion",
}

PAGINAS_E1 = {
    "M1": "urd2025 p215, p217, p311, p312 (corroboracion base anadida)",
    "M2": "sin paginas nuevas",
    "M6": "urd2025 p306, p312, p341, p327; q1_2025_revenue p1 y q3_2026_revenue p1-p3 reescritas sin .* ni alternativas (E-R5)",
    "N2": "urd2025 p327, p349, p350 (tres paginas exigidas por E-R1)",
}


def pagina_texto(fid, page):
    lines = (TRABAJO / "texto" / f"{fid}.txt").read_text(encoding="utf-8").splitlines()
    out, cur, found = [], None, None
    for i, ln in enumerate(lines):
        m = re.match(r"\[PDF PAGE (\d+)\]", ln)
        if m:
            if cur == page:
                break
            cur = int(m.group(1))
            if cur == page:
                out = [ln]
                found = i + 1
                continue
        if cur == page:
            out.append(ln)
    if found is None:
        raise AssertionError(f"{fid}: no existe [PDF PAGE {page}]")
    return "\n".join(out), found


def main():
    indice = {r["id"]: r for r in csv.DictReader((TRABAJO / "INDICE_DESCARGAS.csv").open(encoding="utf-8"))}
    if indice["urd2025"]["sha256"] != SHA_URD2025:
        raise AssertionError("urd2025 descargado no coincide con base-4.14 (sha256 esperado " + SHA_URD2025[:16] + "...)")
    registros = []
    for fid, meta in indice.items():
        registros.append({
            "tipo": "documento",
            "id": fid,
            "titulo": meta["titulo"],
            "url_solicitada": meta["url_solicitada"],
            "url_final": meta["url_final"],
            "http": meta["http"],
            "content_type": meta["content_type"],
            "bytes": meta["bytes"],
            "sha256": meta["sha256"],
            "paginas_pdf": meta["paginas_pdf"],
            "fecha": meta["fecha"],
            "fecha_descarga": meta["fecha_descarga"],
            "ejercicio": meta["ejercicio"],
            "idioma": meta["idioma"],
            "preguntas": meta["preguntas"],
            "estado_preservacion": meta["estado"],
            "tipo_evidencia": "corroboracion_base" if fid in DOCS_BASE else "nueva",
            "nota": "URD2025 descargado coincide byte a byte (sha256 04bfd087...) con el URD2025 ya conservado en base-4.14: verificacion de conservacion, no fuente nueva" if fid == "urd2025" else "",
        })
    citas_ok = []
    for pregunta, fid, page, patron, hallazgo, no_demuestra, salida in CITAS:
        texto_pag, linea_base = pagina_texto(fid, page)
        p = patron.replace(" ", r"\s+")
        m = re.search(p, texto_pag, re.IGNORECASE | re.DOTALL)
        if not m:
            raise AssertionError(f"cita no verificada: {fid} p{page} /{patron}/")
        if re.search(r"\.\*|\|", patron):
            raise AssertionError(f"patron prohibido (.* codicioso o alternativa): {fid} p{page} /{patron}/")
        cita = " ".join(m.group(0).split())[:400]
        pos = texto_pag.find(m.group(0)[:40])
        registro = {
            "tipo": "cita",
            "pregunta": pregunta,
            "documento": fid,
            "titulo": indice[fid]["titulo"],
            "pagina_pdf": page,
            "patron": patron,
            "linea_txt": linea_base + (texto_pag[:pos].count("\n") if pos >= 0 else 0),
            "cita": cita,
            "sha256_doc": indice[fid]["sha256"],
            "tipo_evidencia": "corroboracion_base" if fid in DOCS_BASE else "nueva",
            "hallazgo": hallazgo,
            "no_demuestra": no_demuestra,
            "salida_afecta": salida,
        }
        registros.append(registro)
        citas_ok.append(registro)
    ruta = SALIDA / "LECTURA_FUENTES.jsonl"
    with ruta.open("w", encoding="utf-8") as fh:
        for r in registros:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("escrito", ruta.relative_to(RAIZ), "-", len(registros), "registros,", len(citas_ok), "citas verificadas (idempotente: reescrito desde cero)")

    # PREGUNTAS_Y_RESULTADOS.csv (idempotente: anade columnas solo si faltan y recalcula valores)
    por_preg = {}
    for c in citas_ok:
        por_preg.setdefault(c["pregunta"], []).append(c)
    ruta_p = SALIDA / "PREGUNTAS_Y_RESULTADOS.csv"
    with ruta_p.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
        campos = list(rows[0].keys())
    for c in ["hallazgo_bloque2", "documentos_paginas_bloque2", "estado_tras_bloque2",
              "hallazgo_revision_e1", "documentos_paginas_revision_e1", "estado_tras_revision_e1"]:
        if c not in campos:
            campos.append(c)
    with ruta_p.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=campos)
        w.writeheader()
        for r in rows:
            pid = r["id"]
            cs = por_preg.get(pid, [])
            r["hallazgo_bloque2"] = " | ".join(c["hallazgo"] for c in cs)
            r["documentos_paginas_bloque2"] = "; ".join(f"{c['documento']} p{c['pagina_pdf']}" for c in cs)
            r["estado_tras_bloque2"] = ESTADOS_E1[pid]
            r["hallazgo_revision_e1"] = CORRECCION_E1[pid]
            r["documentos_paginas_revision_e1"] = PAGINAS_E1[pid]
            r["estado_tras_revision_e1"] = ESTADOS_E1[pid]
            w.writerow(r)
    print("actualizado", ruta_p.relative_to(RAIZ), "(columnas anadidas solo si faltaban; valores recalculados)")

    # FUENTES_Y_BUSQUEDA.csv (idempotente: filtra filas de descarga/candidato y las re-anade)
    ruta_f = SALIDA / "FUENTES_Y_BUSQUEDA.csv"
    with ruta_f.open(encoding="utf-8") as fh:
        fr = list(csv.DictReader(fh))
        campos_f = list(fr[0].keys())
    for c in ["url_solicitada", "url_final", "http", "content_type", "fecha_descarga", "version"]:
        if c not in campos_f:
            campos_f.append(c)
    fr = [r for r in fr if not (r["estado"].startswith("DESCARGADO") or r["estado"].startswith("FALLO_DESCARGA")
                                or r["estado"].startswith("CANDIDATO_NUEVO"))]
    with ruta_f.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=campos_f)
        w.writeheader()
        for r in fr:
            w.writerow(r)
        for fid, meta in indice.items():
            w.writerow({
                "estado": "DESCARGADO_PROVISIONAL_BLOQUE2" if meta["http"] == "200" else "FALLO_DESCARGA",
                "categoria": "documento oficial nuevo (fr.elis.com, TLS verificado)" + (" [hash coincide con base-4.14: ya conservado]" if fid == "urd2025" else ""),
                "nombre": fid,
                "ruta_o_recurso": meta["url_final"],
                "sha256": meta["sha256"],
                "bytes": meta["bytes"],
                "ejercicio": meta["ejercicio"],
                "idioma": meta["idioma"],
                "examinado_en": f"bloque 2 E-ELIS + correccion E1 ({meta['fecha']})",
                "notas": f"{meta['titulo']}; {meta['paginas_pdf']} pags; {meta['estado']}; preguntas {meta['preguntas']}",
                "url_solicitada": meta["url_solicitada"],
                "url_final": meta["url_final"],
                "http": meta["http"],
                "content_type": meta["content_type"],
                "fecha_descarga": meta["fecha_descarga"],
                "version": meta["version"],
            })
    print("ampliado", ruta_f.relative_to(RAIZ), "(filas de descarga re-anadidas sin duplicar)")


if __name__ == "__main__":
    main()
