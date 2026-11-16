"""Bloque 2 de E-ELIS: lectura acotada verificada de los documentos nuevos descargados.

Cada cita curada indica documento (id de descarga), pagina PDF y patron; el script exige que
el patron este dentro de esa pagina del texto extraido ([PDF PAGE n]) y registra linea y cita.
Genera:
- LECTURA_FUENTES.jsonl: un registro por documento (metadatos de descarga) y uno por cita
  (pregunta, hallazgo, lo que no demuestra, salida afectada).
- PREGUNTAS_Y_RESULTADOS.csv actualizado (hallazgo_bloque2, documentos_paginas_bloque2,
  estado_tras_bloque2).
- FUENTES_Y_BUSQUEDA.csv ampliado con las fuentes nuevas descargadas (estado real).
Falla loudly si una cita no esta en su pagina.
"""
import csv
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
TRABAJO = RAIZ / ".trabajo/elis_fuentes"
SALIDA = RAIZ / "resultados_cierre/elis_fuentes"

# (pregunta, doc_id, pagina_pdf, patron, hallazgo, no_demuestra, salida_afecta)
CITAS = [
    ("M1", "cgmbrochure2026", 15, r"covers investments for both growth .* and maintenance \(equipment replacement\)",
     "El capex industrial se declara que cubre crecimiento (nuevas plantas/capacidad) y mantenimiento (reemplazo de equipos); categorias: intangibles TI, PP&E (proyectos grandes + instalaciones), aparatos de higiene y gasto de lino",
     "No da el reparto mantenimiento/crecimiento en importes por bloque ni por ano",
     "M1: flujo de partida 339,8-477,8 (45% del FCF base); nivel motor A; ancla S2C"),
    ("M1", "cgmbrochure2026", 15, r"gross capital expenditure .* totaled .*823\.9 million, .*887\.4 million and .*890\.2 million",
     "Capex bruto (antes de subvenciones, sin adquisiciones) 2023/2024/2025 = 823,9 / 887,4 / 890,2 millones de euros",
     "Es bruto y agregado; no separa mantenimiento de crecimiento ni lino de industrial",
     "M1: ancla el nivel de capex bruto por ano"),
    ("M1", "fy2025_comunicado_en", 6, r"net capex were stable compared to 2024 and stood at 18\.2% as a percentage of revenue, compared to 19\.2% in 2024",
     "Net capex 2025 = 18,2% de ventas (19,2% en 2024); mejora por mejor gestion de la inversion en lino",
     "Sigue sin publicar el desglose mantenimiento/crecimiento",
     "M1"),
    ("M1", "fy2025_presentacion_en", 29, r"Net capex \(874\.7\) \(876\.0\)",
     "Net capex 2025 = 874,7 millones de euros (2024: 876,0); 18,2% / 19,2% de ventas; FCF 358,6",
     "Idem: nivel, no reparto",
     "M1"),
    ("M1", "h1_2026_comunicado_en", 6, r"ratio stood at 19\.5% in H1 2026 .* ramp up of major industrial investment projects .* around 18% by year-end",
     "H1 2026 net capex = 19,5% de ventas (18,4% H1 2025) por 'ramp up of major industrial investment projects'; esperado ~18% a cierre 2026",
     "Confirma proyectos industriales grandes en curso, sin importe ni reparto mantenimiento/crecimiento",
     "M1: capex 2026 esperado ~18%"),
    ("M1", "urd2025", 137, r"two-thirds of which ensures the maintenance of the stock in circulation",
     "URD 2025 p.137: 'two-thirds' del lino plano mantienen el stock en circulacion (texto fijo desde URD 2020); en bajada el capex de plantas 'becomes irrelevant'",
     "Proporcion parcial de un bloque (lino plano = 46,2% de ventas 2025); no es proporcion de capex total ni importe",
     "M1"),
    ("M1", "urd2025", 215, r"Capex 1,160\.0 86\.0% 842\.0 72\.6%",
     "Taxonomia UE 2025: CapEx total 1.160,0 M EUR; 86,0% elegible; 842,0 M EUR (72,6%) alineado (economia circular 70,7%)",
     "Es un reparto por objetivo taxonomico (economia circular/clima), no mantenimiento vs crecimiento",
     "M1: importe de capex alineado con clima/economia circular publicado (842,0 M EUR)"),
    ("M1", "cgmbrochure2026", 60, r"capex contained despite new workwear contracts and expenditure under the Climate plan",
     "Se confirma gasto bajo el Climate plan en 2025 ('expenditure under the Climate plan'), sin importe",
     "Sin importe, horizonte ni finalidad cuantificada del plan climatico en esta pagina",
     "M1: plan climatico (importe/horizonte/finalidad) sigue pendiente"),
    ("M1", "cgmbrochure2026", 4, r"2030 CSR roadmap \(including the Climate Strategy\)",
     "La CGM del 21-may-2026 incluye como punto de agenda (sin resolucion) la presentacion de la roadmap CSR 2030 incl. Climate Strategy",
     "La agenda anuncia la presentacion; el contenido con importes no esta en este documento",
     "M1: plan climatico"),
    ("M2", "urd2025", 141, r"customer attrition rates are monitored at the Executive Committee level",
     "URD 2025 p.141: las tasas de bajas de clientes se siguen a nivel de Comite Ejecutivo en todas las regiones; sin cifra publicada",
     "No publica la tasa de bajas ni por segmento ni total",
     "M2: PPA 85,7/a (28% FCF base); A1 vs A2 89,9"),
    ("M2", "fy2024_presentacion_en", 5, r"Customer retention rate back to its normative level",
     "Presentacion FY2024 p.5: 'customer retention rate back to its normative level' (2024); cualitativo, nivel normativo no cuantificado",
     "No cuantifica la tasa ni el nivel normativo",
     "M2"),
    ("M2", "factsheet2026", 1, r"4-year contracts: Monthly fixed fee",
     "Factsheet 2026: contratos de 4 anos con tarifa fija mensual (workwear = 37% de ventas)",
     "Estructura contractual, no tasa de bajas ni desembolso inicial por cliente nuevo",
     "M2"),
    ("M2", "cgmbrochure2026", 15, r"initial outlay required to set up a new customer",
     "Brochure CGM p.15: el gasto de lino incluye 'the initial outlay required to set up a new customer'; la inversion de crecimiento es 'a large percentage' de ese gasto por esa dotacion inicial",
     "Cualitativo ('large percentage'), sin importe del desembolso inicial por cliente nuevo",
     "M2: dotacion a clientes nuevos que repone perdidos (enlaza M1)"),
    ("M2", "fy2025_presentacion_en", 12, r"streamlining customer onboarding and reducing implementation lead times",
     "Presentacion FY2025 p.12: plataforma CRM para acortar lead times de implementacion/onboarding de clientes",
     "Sin importe ni tasa; no identifica el desembolso inicial por cliente nuevo",
     "M2"),
    ("M2", "q3_2026_revenue", 3, r"selective approach to acquiring new customers",
     "Q3 2026: 'selective approach to acquiring new customers' (disciplina de precios); cualitativo",
     "Sin tasa de bajas ni importe por cliente nuevo",
     "M2"),
    ("M6", "urd2025", 313, r"annual revenue of more than .5\.0. million in France and .3\.0. million in other countries",
     "URD 2025 p.313 (def. APM): 'major acquisitions/disposals' = empresas con ingresos anuales en la adquisicion > 5,0 M EUR en Francia y > 3,0 M EUR en otros paises (Note 2.4); el crecimiento organico solo excluye esas y el efecto divisa",
     "Define el umbral del perimetro, no la finalidad de las compras pequenas (reposicion vs crecimiento)",
     "M6: las compras < umbral permanecen DENTRO del organico publicado; cada M EUR de compras como reposicion baja 1 M EUR el flujo sostenible"),
    ("M6", "fy2025_comunicado_en", 11, r"calculated excluding \(i\) the impacts of changes in the scope of consolidation of .major acquisitions",
     "Comunicado FY2025 p.11 repite la misma definicion de crecimiento organico (solo excluye 'major acquisitions' y 'major disposals' segun el URD + divisa)",
     "Igual: umbral de perimetro, no finalidad",
     "M6"),
    ("M6", "fy2024_comunicado_en", 7, r"bolt-on acquisitions, with an envelope between 50 million euros and 150",
     "Comunicado FY2024 p.7: politica de asignacion de capital (6-mar-2025): adquisiciones bolt-on con sobre de 50-150 M EUR/anuales",
     "Es un presupuesto, no un desglose de finalidad ni importes por operacion",
     "M6"),
    ("M6", "fy2025_comunicado_en", 7, r"annual budget of between 50 million euros and 150 million euros",
     "Comunicado FY2025 p.7: ratifica el sobre bolt-on de 50-150 M EUR/anuales para 2026",
     "Idem",
     "M6"),
    ("M6", "q1_2025_revenue", 1, r"Carsan in Spain, Ernst in .* with annual combined revenue of c\. 55 million euros in 2024",
     "Q1 2025 p.1: 3 bolt-ons consolidadas desde 1-ene-2025 (Carsan Espagne, Ernst Alemania, Bodensee Suiza), ingresos combinados 2024 c. 55 M EUR; contribuyeron al crecimiento externo +2,1%",
     "No dice que parte repone cartera perdida ni cuanto es crecimiento; son ejemplo de compras pequenas dentro del perimetro organico/externo publicado",
     "M6"),
    ("M6", "q3_2026_revenue", 1, r"RS10 in Spain|acquisitions contributed 1\.5 percentage points",
     "Q3 2026 p.1: adquisiciones contribuyeron +1,5 pp en Q3 2026 (RS10 en Espana consolidada desde 1-jun-2026; Muller +0,5 pp); pipeline 'remains strong'",
     "Sin importes por operacion ni finalidad reposicion/crecimiento",
     "M6"),
    ("M6", "fy2025_presentacion_en", 29, r"Acquisitions of subsidiaries, net of cash acquired \(117\.6\) \(183\.3\)",
     "Presentacion FY2025 p.29: caja de adquisiciones de filiales (neta de caja adquirida) 2025 = 117,6 M EUR (2024: 183,3)",
     "Importe total de M&A, no desglose por operacion ni por finalidad",
     "M6"),
    ("M6", "fy2025_comunicado_en", 2, r"active year for M&A, with many small and mid-sized acquisitions",
     "Comunicado FY2025 p.2: 2025 'active year for M&A, with many small and mid-sized acquisitions' que refuerzan la densidad de red en Europa y Latinoamerica; cualitativo",
     "Sin lista completa ni importes en esta pagina (Note 2.4 del URD los lista)",
     "M6"),
    ("N2", "urd2025", 350, r"Net gain \(loss\) related to retirement of fixed assets 25\.7 \(1\.5\)",
     "URD 2025 nota 4.6 p.350: dentro de otros ingresos y gastos operativos 2025 figura 'Net gain related to retirement of fixed assets' +25,7 M EUR (2024: -1,5); es un concepto monetario (el detalle separa los de impacto no monetario 0,3)",
     "La nota no dice que ese +25,7 sea la compensacion del seguro; no se igualan dos magnitudes parecidas sin mas evidencia",
     "N2: bajas de 2025 con seguros; m0 +0,54 pp"),
    ("N2", "urd2025", 350, r"OTHER OPERATING INCOME AND EXPENSES \(3\.1\) \(18\.5\)",
     "OOIE 2025 = -3,1 M EUR (2024: -18,5); la mejora incluye menos earnouts y la partida de bajas +25,7",
     "No desagrega el cobro del seguro en caja",
     "N2"),
    ("N2", "urd2025", 309, r"offset by a high level of insurance benefits in 2025",
     "URD 2025 p.309 (analisis de resultados): la caida de OOIE se vincula a menos earnouts, 'offset by a high level of insurance benefits in 2025'",
     "Narrativa cualitativa; no importe ni evento asegurado identificado en esta pagina",
     "N2"),
    ("N2", "fy2025_comunicado_en", 4, r"higher level of insurance compensations in 2025",
     "Comunicado FY2025 p.4: las perdidas operativas no corrientes bajaron mucho, 'offset by a higher level of insurance compensations in 2025'",
     "Sin importe ni fiscalidad",
     "N2"),
    ("N2", "fy2025_presentacion_en", 25, r"Positive one -offs linked to insurance compensation",
     "Presentacion FY2025 p.25: 'Positive one-offs linked to insurance compensation' en el puente a net income 2025",
     "Sin importe en la pagina (el +25,7 esta en la nota 4.6 del URD)",
     "N2"),
]


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
    registros = []
    # registro por documento descargado
    for fid, meta in indice.items():
        registros.append({
            "tipo": "documento",
            "id": fid,
            "titulo": meta["titulo"],
            "url_final": meta["url_final"],
            "http": meta["http"],
            "bytes": meta["bytes"],
            "sha256": meta["sha256"],
            "paginas_pdf": meta["paginas_pdf"],
            "fecha": meta["fecha"],
            "ejercicio": meta["ejercicio"],
            "idioma": meta["idioma"],
            "preguntas": meta["preguntas"],
            "estado_preservacion": meta["estado"],
            "nota": "URD2025 descargado coincide byte a byte (sha256 04bfd087...) con el URD2025 ya conservado en base-4.14: verificacion de conservacion, no fuente nueva" if fid == "urd2025" else "",
        })
    # registros por cita verificada
    citas_ok = []
    for pregunta, fid, page, patron, hallazgo, no_demuestra, salida in CITAS:
        texto_pag, linea_base = pagina_texto(fid, page)
        p = patron.replace(" ", r"\s+")
        m = re.search(p, texto_pag, re.IGNORECASE | re.DOTALL)
        if not m:
            raise AssertionError(f"cita no verificada: {fid} p{page} /{patron}/")
        cita = " ".join(m.group(0).split())[:400]
        # linea dentro del archivo: buscar la primera linea del match
        pos = texto_pag.find(m.group(0)[:40])
        registro = {
            "tipo": "cita",
            "pregunta": pregunta,
            "documento": fid,
            "titulo": indice[fid]["titulo"],
            "pagina_pdf": page,
            "linea_txt": linea_base + (texto_pag[:pos].count("\n") if pos >= 0 else 0),
            "cita": cita,
            "sha256_doc": indice[fid]["sha256"],
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
    print("escrito", ruta.relative_to(RAIZ), "-", len(registros), "registros,", len(citas_ok), "citas verificadas")

    # actualizar PREGUNTAS_Y_RESULTADOS.csv
    por_preg = {}
    for c in citas_ok:
        por_preg.setdefault(c["pregunta"], []).append(c)
    ruta_p = SALIDA / "PREGUNTAS_Y_RESULTADOS.csv"
    with ruta_p.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
        campos = list(rows[0].keys())
    campos += ["hallazgo_bloque2", "documentos_paginas_bloque2", "estado_tras_bloque2"]
    estados = {
        "M1": "ABIERTO - nuevos datos de nivel (capex bruto 823,9/887,4/890,2; neto 874,7 = 18,2%; taxonomía 842,0 alineado) pero SIN reparto mantenimiento/crecimiento ni importe del plan climático; no localizado en esta búsqueda",
        "M2": "ABIERTO - solo cualitativo (attrition 'monitored', retención 'back to normative', 4-year contracts, initial outlay por cliente nuevo sin importe); no localizado en esta búsqueda",
        "M6": "PERIMETRO ACLARADO - umbral 'major acquisition' publicado (>5,0 M€ Francia / >3,0 M€ otros países; el orgánico solo excluye esas) y sobre bolt-on 50-150 M€/año; FINALIDAD (reposición vs crecimiento) no publicada; no localizado en esta búsqueda",
        "N2": "PARCIAL - publicado +25,7 M€ de ganancia neta por bajas de inmovilizado en OOIE 2025 (nota 4.6) y narrativa de 'insurance benefits/compensations 2025'; NO se afirma que sean la misma partida, ni fiscalidad ni cobro detallado; no localizado en esta búsqueda",
    }
    with ruta_p.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=campos)
        w.writeheader()
        for r in rows:
            pid = r["id"]
            cs = por_preg.get(pid, [])
            r["hallazgo_bloque2"] = " | ".join(c["hallazgo"] for c in cs)
            r["documentos_paginas_bloque2"] = "; ".join(f"{c['documento']} p{c['pagina_pdf']}" for c in cs)
            r["estado_tras_bloque2"] = estados[pid]
            w.writerow(r)
    print("actualizado", ruta_p.relative_to(RAIZ))

    # ampliar FUENTES_Y_BUSQUEDA.csv con las fuentes nuevas
    ruta_f = SALIDA / "FUENTES_Y_BUSQUEDA.csv"
    with ruta_f.open(encoding="utf-8") as fh:
        fr = list(csv.DictReader(fh))
        campos_f = list(fr[0].keys())
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
                "examinado_en": f"bloque 2 E-ELIS ({meta['fecha']})",
                "notas": f"{meta['titulo']}; {meta['paginas_pdf']} pags; {meta['estado']}; preguntas {meta['preguntas']}",
            })
    print("ampliado", ruta_f.relative_to(RAIZ))


if __name__ == "__main__":
    main()
