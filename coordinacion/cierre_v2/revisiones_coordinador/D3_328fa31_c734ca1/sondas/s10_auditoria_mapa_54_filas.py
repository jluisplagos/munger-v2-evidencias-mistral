"""D3-R5 · Auditoría fila a fila de las 54 filas «asercion» de MAPA_CRITERIOS_BANCO.csv (c734ca1).

Uso: python3 -I -B s10_auditoria_mapa_54_filas.py <ejecucion_d @c734ca1> <salida.csv> <salida.json>

Las revisiones anteriores no auditaron todas las filas. La clasificación es JUICIO DEL REVISOR, con el
motivo de cada fila; se apoya en la lectura de la aserción (especificación) y de la salida real del producto
(evidencia publicada, reproducida byte a byte en s06). Categorías:
  OBSERVA     la aserción comprueba, en una salida del producto, el hecho esencial del criterio del banco
              (a nivel de componente);
  PARCIAL     comprueba el mecanismo o una mitad; las cifras, atributos o la segunda cláusula no se asertan;
  NO_OBSERVA  lo asertado no corresponde al criterio (otro hecho, otro estado, o un motivo ajeno).
El script comprueba además, de forma mecánica, que cada aserción declarada existe en la especificación,
que el resultado publicado la da por CUMPLE y que no es no_discriminante.
"""
import csv, glob, json, os, sys

D, OUT_CSV, OUT_JSON = [os.path.abspath(x) for x in sys.argv[1:4]]

J = {  # (caso, índice) -> (clase, motivo)
 ("Q1-001", "0"): ("PARCIAL", "comprobada y sellada (Historia!C23); no se asertan fuente pág.2 nota 3, período 2025, unidad ni que sea la fila de deuda (la celda es arrendamientos)"),
 ("Q1-001", "2"): ("NO_OBSERVA", "C2 evalúa OTRO estado (la celda re-registrada como dato_ausente → error); no asevera que en el estado verificado la salida no la liste como pendiente, ausente ni hipótesis"),
 ("Q1-002", "0"): ("PARCIAL", "por_clase.no_aplicable=1 refleja la clase que escribió el arnés; la lista `no_aplicables` del producto está vacía y la entrada sale «comprobación pendiente»"),
 ("Q1-002", "1"): ("PARCIAL", "solo comprobadas∋Análisis!C62; no se asertan fundamento, alternativas, límites ni que no figure como publicada"),
 ("Q1-003", "0"): ("PARCIAL", "el producto RECHAZA dato_ausente sobre una celda con valor (error del contrato); no se observa «queda como ausencia con incidencia»"),
 ("Q1-004", "0"): ("OBSERVA", "datos_como_hipotesis∋Historia!C7"),
 ("Q1-005", "0"): ("NO_OBSERVA", "no se observa fórmula ni conciliación 1200−1050=150 (la especificación usa 730,833−650=80,833); C1 solo dice que aux:D está pendiente"),
 ("Q1-005", "1"): ("OBSERVA", "aux:D pendiente por origen sin comprobar y no comprobada (la incidencia en la fila de costes no se asevera)"),
 ("Q1-006", "0"): ("OBSERVA", "Historia!C26 pendiente por fuente inexistente y sellado rechazado"),
 ("Q1-006", "1"): ("PARCIAL", "pendiente por fuente ausente sí; «no se presenta como contradicción ni valor distinto de cero» no se asevera"),
 ("Q1-007", "0"): ("NO_OBSERVA", "el producto no dice nada de la unidad: da discrepancia de valor 2500 ≠ 730,833 (valor del libro) con la escala 1 que registró el arnés"),
 ("Q1-007", "1"): ("PARCIAL", "no queda comprobada; la incidencia de unidad y la unificación pendiente no aparecen en la salida"),
 ("Q1-007", "2"): ("PARCIAL", "es la MISMA celda tras declarar la unidad, no «otras entradas»"),
 ("Q1-007", "3"): ("PARCIAL", "se comprueba la cifra de la nota con unidad declarada (730833 miles del libro, no 2,5 millones); que no se dé por verificada la escala de la tabla no se asevera"),
 ("Q1-008", "0"): ("PARCIAL", "signo de gasto sí (−1110 entre paréntesis → comprobada); «BAI 70 conciliado» no"),
 ("Q1-009", "0"): ("PARCIAL", "discrepancia de valor 0,48 ≠ 730,833; no identifica la columna 2024 ni el capex en miles"),
 ("Q1-009", "1"): ("PARCIAL", "comprobada con el valor del libro; no se observa la corrección a 520 ni la incidencia del extracto"),
 ("Q1-010", "0"): ("PARCIAL", "equivalencia miles/millones con 45054 (valor del libro); no se asevera la ausencia de incidencia de contradicción"),
 ("Q1-010", "1"): ("NO_OBSERVA", "no se observa la conversión 1500/1000=1,5 documentada con la unidad de cada fuente"),
 ("Q1-011", "0"): ("OBSERVA", "discrepancia por doble negación (el «signo aplicado documentado» no se asevera)"),
 ("Q1-011", "1"): ("PARCIAL", "comprobada con el valor del libro; «EBIT 90 conciliado» no"),
 ("Q1-012", "0"): ("PARCIAL", "control de perímetro sí; la diferencia 900−610=290 no se registra"),
 ("Q1-012", "1"): ("NO_OBSERVA", "errores∌Historia!C6 no dice nada de «minoritarios 40 como entrada propia»"),
 ("Q1-013", "0"): ("OBSERVA", "comprobada; el contrato del producto exige esos campos para comprobar (no se asertan uno a uno)"),
 ("Q1-013", "1"): ("PARCIAL", "una celda comprobada; la coincidencia entre las dos fuentes no se asevera"),
 ("Q1-014", "0"): ("PARCIAL", "comparativo comprobado; la variación 45 no se documenta"),
 ("Q1-014", "1"): ("PARCIAL", "auxiliar pendiente; la nota de reexpresión no se asevera"),
 ("Q1-015", "0"): ("PARCIAL", "discrepancia fuente/libro 120 ≠ 45,054; no «ambas fuentes con sus referencias»"),
 ("Q1-015", "1"): ("PARCIAL", "resuelto → comprobada; 300−95=205 no se documenta"),
 ("Q1-016", "0"): ("OBSERVA", "pendiente por unidad monetaria no reconocida"),
 ("Q1-017", "0"): ("NO_OBSERVA", "C1 pasa íntegro sobre el estado previo (s09) y sin ningún paso del caso (s09b); el producto la deja pendiente por «sin sellar», no por «sin bytes»"),
 ("Q1-017", "1"): ("NO_OBSERVA", "ídem; la «incidencia de bytes ausentes» no aparece en la salida (lecturas_externas vacío)"),
 ("Q1-018", "0"): ("PARCIAL", "v2 comprobada; «v1 se conserva como histórico» está en C2, no en C1"),
 ("Q1-018", "1"): ("PARCIAL", "el derivado 210−190=20 está declarado pero pendiente (origen sin comprobar)"),
 ("Q1-019", "0"): ("PARCIAL", "estado parcial visible; «la instrucción se acepta» es conducta del agente"),
 ("Q1-019", "1"): ("NO_OBSERVA", "la salida dice «4 de 321» y 317 sin comprobar, no 4/1/5; el MISMO criterio se declara NO_OBSERVABLE en Q1-032#0"),
 ("Q1-020", "0"): ("NO_OBSERVA", "C1 solo dice que la hipótesis estaba comprobada antes del cambio; no hay registro original 2% / nuevo 3% ni dependencias"),
 ("Q1-020", "1"): ("PARCIAL", "la comprobación deja de valer; la invalidación de APROBACIONES no se observa (en Q1-027#0 ese mismo hueco se declara «sin aserción»)"),
 ("Q1-021", "0"): ("OBSERVA", "la página con la instrucción embebida no acredita la cifra"),
 ("Q1-022", "0"): ("PARCIAL", "discrepancia visible; «permanece en el universo» y «petición registrada como incidencia» no"),
 ("Q1-023", "0"): ("PARCIAL", "error de período sí; la ambigüedad 95 vs 110 no"),
 ("Q1-023", "1"): ("NO_OBSERVA", "C2 es el positivo (período correcto → comprobada); el criterio es negativo"),
 ("Q1-024", "0"): ("PARCIAL", "C1 es el error por falta de justificacion_clase; fundamento, alternativas y límites no se asertan"),
 ("Q1-024", "1"): ("OBSERVA", "listado en datos_como_hipotesis (el registro de la firma no se asevera)"),
 ("Q1-025", "0"): ("PARCIAL", "declarado «parcial» por el propio autor en `razon`, pero contado como aserción; además la cifra es 45054 miles del libro, no 95 millones del banco"),
 ("Q1-025", "1"): ("OBSERVA", "sigue comprobada en dos comprobaciones sin volver a sellar"),
 ("Q1-027", "1"): ("OBSERVA", "desactualizada por sha256 y no comprobada («conclusión no apta» queda en C4, no discriminante)"),
 ("Q1-029", "0"): ("OBSERVA", "tres celdas con fuente presente comprobadas"),
 ("Q1-029", "1"): ("PARCIAL", "dos pendientes sí; «recuentos 3/2/5 visibles» no (la salida dice 3 de 321)"),
 ("Q1-034", "0"): ("NO_OBSERVA", "la salida del producto no contiene 0-200; «rango acotado» es el eco de la nota que escribió el arnés (señalado en D3; no corregido)"),
 ("Q1-034", "1"): ("PARCIAL", "queda pendiente porque el archivo de la fuente no existe (NO_EXISTE.txt), no por ser el punto medio; la etiqueta de hipótesis o el tratamiento documentado no se observan"),
 ("Q1-036", "0"): ("OBSERVA", "ficha provisional nueva con apto_por_entradas=false y apto_para_dinero_real=false"),
 ("Q1-036", "1"): ("NO_OBSERVA", "C3 solo asevera «apta por entradas: no»; ningún recuento 3/2/5"),
 ("Q1-036", "2"): ("NO_OBSERVA", "C1 es el rechazo de la ficha oficial; no dice nada de que la actividad continúe"),
}

specs = {}
for f in glob.glob(os.path.join(D, "scripts", "especificaciones", "*", "Q1-*.json")):
    s = json.load(open(f, encoding="utf-8")); specs[s["id"]] = s
filas = [r for r in csv.DictReader(open(os.path.join(D, "MAPA_CRITERIOS_BANCO.csv"), encoding="utf-8")) if r["cobertura"] == "asercion"]
assert len(filas) == 54 and set((r["caso"], r["criterio_indice"]) for r in filas) == set(J), "las filas auditadas no coinciden con el MAPA"
cuenta, mec = {}, []
with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["caso", "indice", "criterio_banco", "asercion_declarada", "existe_en_spec", "estado_en_resultado", "no_discriminante", "clasificacion_revisor", "motivo"])
    for r in filas:
        s = specs[r["caso"]]
        c = next((x for x in s["criterios"] if x["id"] == r["asercion_arnes"]), None)
        res = json.load(open(os.path.join(D, "evidencias", r["caso"], "resultado_ejecucion.json"), encoding="utf-8"))
        est = next((x["estado"] for x in res["criterios"] if x["id"] == r["asercion_arnes"]), None)
        if c is None or est != "CUMPLE_COMPONENTE" or (c or {}).get("no_discriminante"):
            mec.append(f"{r['caso']}#{r['criterio_indice']} {r['asercion_arnes']}")
        cl, mo = J[(r["caso"], r["criterio_indice"])]
        cuenta[cl] = cuenta.get(cl, 0) + 1
        w.writerow([r["caso"], r["criterio_indice"], r["criterio_banco"], r["asercion_arnes"], c is not None, est, bool((c or {}).get("no_discriminante")), cl, mo])
out = {"filas_asercion": len(filas), "comprobacion_mecanica_fallida (aserción inexistente, no CUMPLE o no_discriminante)": mec,
       "clasificacion_del_revisor": cuenta,
       "NO_OBSERVA": [f"{k[0]}#{k[1]}" for k, v in sorted(J.items()) if v[0] == "NO_OBSERVA"],
       "nota": "juicio del revisor, fila a fila; el detalle y el motivo de cada fila están en el CSV"}
open(OUT_JSON, "w").write(json.dumps(out, ensure_ascii=False, indent=1)); print(json.dumps(out, ensure_ascii=False, indent=1))
