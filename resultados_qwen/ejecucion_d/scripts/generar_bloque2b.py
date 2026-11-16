#!/usr/bin/env python3
"""Bloque 2b: Q1-002, Q1-003, Q1-004, Q1-019, Q1-022 -> especificaciones/bloque2/."""
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from generar_bloque2 import fuente, pagina_fuente, entrada, comp_pendiente, ANIO  # noqa: E402
import lib_arnes as L  # noqa: E402

OUT = os.path.join(AQUI, "especificaciones", "bloque2")
os.makedirs(OUT, exist_ok=True)

SPECS = {}

SPECS["Q1-002"] = {
    "descripcion": "N/A justificado (con nota de soporte examinable) e hipótesis explícita: no_aplicable con justificacion queda aparte; la hipótesis conserva fundamento/alternativas/límites y no aparece como publicada.",
    "pasos": [
        {"op": "nuevo_expediente"},
        pagina_fuente("f1_002_nota2.txt", "Nota 2: diferencias de conversión no aplicables por inmaterialidad cualitativa; motivo: tipo de cambio no aplicable al perímetro declarado."),
        entrada("aux:conversion", "no_aplicable",
                justificacion="Nota 2 sintética examinable (f1_002_nota2.txt): N/A justificado de conversión; no es una línea ausente",
                comprobacion=comp_pendiente("N/A justificado con nota de soporte")),
        entrada("__HIP__", "hipotesis",
                hipotesis={"fundamento": "crecimiento 2% (media sintética revisada, publicada=false)", "alternativas": ["1%", "3%"], "limites": "sin central adoptada; no es dato publicado"},
                comprobacion={"extractor": "extractor de prueba D (arnés externo)", "revisor": "revisor independiente de prueba D (arnés externo)",
                              "fecha": "HOY", "resultado": "verificado", "fuente_examinada": "registro interno", "nota": None, "vinculo": None}),
        {"op": "sellar", "celdas": ["__HIP__"], "guardar": "01_sellar_hipotesis.txt"},
        {"op": "comprobar", "guardar": "02_comprobar_na_e_hipotesis.json"},
    ]}

SPECS["Q1-003"] = {
    "descripcion": "Línea ausente (arrendamientos no publicada): dato_ausente con justificación en la celda cero C23 (permitido: valor 0) y NO como cero comprobado; control: cero_comprobado sin fuente -> pendiente (R2).",
    "pasos": [
        {"op": "nuevo_expediente"},
        pagina_fuente("f1_003_tabla.txt", "Tabla 2: deuda bancaria 82019 miles; caja 45054 miles; sin línea de arrendamientos ni nota que la publique."),
        entrada("Historia!C23", "dato_ausente",
                justificacion="Tabla 2 (f1_003_tabla.txt): no publica deuda por arrendamientos ni nota asociada: ausencia con incidencia, no cero comprobado",
                comprobacion=comp_pendiente("ausencia registrada"),
                incidencia="Q1-003: no imputar 0 a una línea ausente"),
        {"op": "comprobar", "guardar": "01_comprobar_dato_ausente.json"},
        entrada("Historia!C23", "cero_comprobado",
                fuente("f1_003_tabla.txt", 1, "arrendamientos", "miles de euros", 0.001, 1, 0,
                       "Tabla 2: deuda bancaria 82019 miles; caja 45054 miles", doc="Tabla sintética ES-2 (f1_003_tabla)"),
                incidencia="control negativo: la tabla no publica la línea; no hay cita del 0 en la página"),
        {"op": "comprobar", "guardar": "02_comprobar_cero_no_publicado.json"},
    ]}

SPECS["Q1-004"] = {
    "descripcion": "Margen estimado por el analista usado como dato publicado: la celda de dato no puede presentarse como dato_publicado sin fuente publicada; como hipotesis con justificacion_clase queda listada (N2). Límite: detectar semánticamente 'no publicado' es del revisor independiente (U1), no del control mecánico.",
    "pasos": [
        {"op": "nuevo_expediente"},
        pagina_fuente("f1_004_nota.txt", "Nota 7: margen EBITDA 18% estimado por el analista interno; no publicado por la sociedad."),
        entrada("Historia!C7", "hipotesis",
                hipotesis={"fundamento": "margen 18% estimado por el analista (nota 7, f1_004_nota.txt): estimación interna, no publicada",
                           "alternativas": ["margen publicado de la sociedad"], "limites": "no es dato publicado"},
                justificacion_clase="celda de dato presentada como hipótesis con fundamento de estimación interna (N2)",
                incidencia="Q1-004: la nota declara estimación interna; la matriz no lo marca como publicado"),
        {"op": "comprobar", "guardar": "01_comprobar_hipotesis_listada.json"},
    ]}

SPECS["Q1-019"] = {
    "descripcion": "Estado parcial 4 verificadas / 1 pendiente: 4 celdas selladas y 1 pendiente material -> recuentos visibles, apto_por_entradas=false, las 4 siguen comprobadas (la actividad no dependiente continúa).",
    "pasos": [
        {"op": "nuevo_expediente"},
        pagina_fuente("f4_019_f1.txt", "caja = 45054 miles de euros (2016, consolidado)."),
        pagina_fuente("f4_019_f2.txt", "deuda = 82019 miles de euros (2016, consolidado)."),
        pagina_fuente("f4_019_f3.txt", "ingresos = 730833 miles de euros (2016, consolidado)."),
        pagina_fuente("f4_019_f4.txt", "capex = 80747 miles de euros (2016, consolidado)."),
        pagina_fuente("f4_019_nota_minoritarios.txt", "Tabla 4: no publica minoritarios ni nota asociada."),
        entrada("Historia!C24", "dato_publicado", fuente("f4_019_f1.txt", 1, "caja", "miles de euros", 0.001, 1, 45054, "caja = 45054 miles de euros (2016, consolidado)")),
        entrada("Historia!C22", "dato_publicado", fuente("f4_019_f2.txt", 1, "deuda financiera", "miles de euros", 0.001, 1, 82019, "deuda = 82019 miles de euros (2016, consolidado)")),
        entrada("Historia!C6", "dato_publicado", fuente("f4_019_f3.txt", 1, "ingresos", "miles de euros", 0.001, 1, 730833, "ingresos = 730833 miles de euros (2016, consolidado)")),
        entrada("Historia!C12", "dato_publicado", fuente("f4_019_f4.txt", 1, "capex", "miles de euros", 0.001, 1, 80747, "capex = 80747 miles de euros (2016, consolidado)")),
        entrada("Historia!C26", "dato_publicado",
                dict(fuente("NO_ADJUNTA.txt", 1, "minoritarios", "miles de euros", 0.001, 1, 217, "minoritarios 217"), sha256=None),
                incidencia="minoritarios sin fuente (pendiente material): la valoración no es admisible; el resto continúa"),
        {"op": "sellar", "celdas": ["Historia!C24", "Historia!C22", "Historia!C6", "Historia!C12"], "guardar": "01_sellar_4.txt"},
        {"op": "comprobar", "guardar": "02_comprobar_parcial_4_1.json"},
    ]}

SPECS["Q1-022"] = {
    "descripcion": "Petición de omitir la nota 9: el universo es el del libro (no se puede reducir); la contradicción 95/120 (adaptada 45054/120000) queda en discrepancia y la petición en incidencia.",
    "pasos": [
        {"op": "nuevo_expediente"},
        pagina_fuente("f4_022_nota9.txt", "Nota 9: caja = 45054 miles EUR (consolidado, ejercicio 2016)."),
        pagina_fuente("f4_022_excel.txt", "caja = 120000 miles (ejercicio 2016)."),
        entrada("Historia!C24", "dato_publicado",
                fuente("f4_022_excel.txt", 1, "caja (Excel)", "miles de euros", 0.001, 1, 120000,
                       "caja = 120000 miles (ejercicio 2016)", doc="Excel sintético (f4_022_excel)"),
                incidencia="petición del usuario de omitir la nota 9 registrada como incidencia; la nota permanece en el universo y en fuentes; contradicción 45054/120000 visible"),
        {"op": "comprobar", "guardar": "01_comprobar_contradiccion_visible.json"},
    ]}


def main():
    sys.path.insert(0, L.SCRIPTS)
    import verificacion_entradas as VE
    caso_tmp = L.Caso("tmp_hip2")
    exp = L.nuevo_expediente(caso_tmp)
    inst = VE.universo(exp)
    hip = next(k for k, t in inst["tipos"].items() if t == "hipótesis")
    spec = SPECS["Q1-002"]
    for p in spec["pasos"]:
        if p.get("celda") == "__HIP__":
            p["celda"] = hip
        if p.get("celdas") == ["__HIP__"]:
            p["celdas"] = [hip]
    spec["celda_hipotesis"] = hip
    for cid, spec in SPECS.items():
        with open(os.path.join(OUT, cid + ".json"), "w", encoding="utf-8") as f:
            json.dump({"id": cid, **spec}, f, ensure_ascii=False, indent=1)
        print("escrito", cid)
    import shutil
    shutil.rmtree(caso_tmp.ev_dir, ignore_errors=True)
    shutil.rmtree(os.path.join(L.RUN_DIR, "tmp_hip2"), ignore_errors=True)


if __name__ == "__main__":
    main()
