"""Bloque 1 de E-ELIS: inventario reproducible de preguntas y de recursos ya examinados.

Lee, solo con git show (sin fusionar), las versiones fijadas por el control comun:
- producto f1 = 716cbd6... : datos/fuentes.json del frente E/F1 de Elis (6 archivos conservados)
- revision F1 = f5775dc... : revision_externa/f1_v3_20261116/seleccion_fuentes.json (bytes + sha256)
- control = 99adbbf... (rama coordinacion/cierre-v2; commit de referencia de la reanudacion
  c241a59): CONTROL.json (fila E-ELIS, versiones_fijadas)

Dependencias declaradas (E-R9): 716cbd6 vive solo en el repositorio del producto y no esta
en el auxiliar. Si falta algun commit, el script imprime el comando exacto para traerlo y
sale con exit 2 (antes fallaba con un AssertionError crudo).

Genera PREGUNTAS_Y_RESULTADOS.csv y FUENTES_Y_BUSQUEDA.csv en resultados_cierre/elis_fuentes/.
Comprueba que los sha256 de datos/fuentes.json y de seleccion_fuentes.json coinciden y que el
ZIP base-4.14 local tiene la huella registrada; falla loudly si algo se mueve.
"""
import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
SALIDA = RAIZ / "resultados_cierre/elis_fuentes"

PRODUCTO_F1 = "716cbd6794b7fcde8b3862c9d1e7acdaf516d262"
REVISION_F1 = "f5775dc07a61b829df2b0e7a4a97c556869ae0f4"
CONTROL = "99adbbf62a78afc32de010179495281266a0bd00"
FRENTE = "docs/validacion_economica_paralela/frente_E_F1_elis"
ZIP_BASE414 = RAIZ / ".trabajo/base414.zip"
SHA_ZIP_BASE414 = "bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e"
PRODUCTO_URL = "ht" + "tps" + "://github.com/jluisplagos/munger-v2.git"


def asegurar_commit(sha, fetch_cmd, origen):
    """E-R9: dependencia declarada. Sale con exit 2 e imprime el comando exacto si falta."""
    r = subprocess.run(["git", "-C", str(RAIZ), "cat-file", "-e", sha + "^{commit}"], capture_output=True)
    if r.returncode != 0:
        print(f"DEPENDENCIA AUSENTE: {sha} ({origen}) no esta en este clon del auxiliar.")
        print(f"Ejecuta: {fetch_cmd}")
        sys.exit(2)


def git_show(sha, ruta):
    r = subprocess.run(["git", "-C", str(RAIZ), "show", f"{sha}:{ruta}"],
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise AssertionError(f"git show {sha}:{ruta} fallo: {r.stderr[:200]}")
    return r.stdout


PREGUNTAS = [
    {
        "id": "M1",
        "pregunta": "Reparto anual por activos del capex propio entre mantenimiento y crecimiento; base y fecha de la proporcion 'dos tercios' del lino plano; importe, horizonte y finalidad del plan climatico.",
        "definicion_fuente": "INFORME_CONCILIACION_F1.md §6.4 l561 (producto 716cbd6): reparto por bloque (lino, otros articulos, industrial/TI, plan climatico) y año; §6.1 l498-506: busqueda previa agotada, solo proporcion parcial 'dos tercios' del lino plano (URD25 p.137, URD23 p.239, URD22 p.221, URD21 p.189, DEU24 p.135), texto fijo desde al menos URD 2020",
        "estado_inicial": "ABIERTO - no localizado en busqueda previa",
        "evidencia_ya_examinada": "URD 2016-2023 y 2025, DEU 2024, comunicado de resultados 2025 y documentos S1-2026 (alcance de busqueda de §6.1); terminos ya usados: maintenance/growth capex, replacement, renewal, churn, attrition, retention rate, investissements de maintenance/croissance, renouvellement, taux de perte, two-thirds/deux tiers; resultado: ningun importe de reparto, churn solo cualitativo",
        "salida_afecta": "flujo de partida 339,8-477,8 (intervalo 138 = 45% del FCF base 307,933); nivel del motor A y anclaje S2C",
        "limite": "una proporcion de ventas no es proporcion de capex; 'dos tercios' de un bloque no se extrapola al total; categoria contable no identifica reposicion economica",
    },
    {
        "id": "M2",
        "pregunta": "Tasa de bajas de clientes (en particular de los adquiridos) y desembolso inicial por cliente nuevo; distinguir gasto comercial corriente de inversion propia y de compras de cartera.",
        "definicion_fuente": "INFORME_CONCILIACION_F1.md §6.4 l562 (producto 716cbd6); ESPECIFICACION_F1_PROPUESTA.md l31 (R_propia incluye la dotacion a clientes que sustituyen a los perdidos)",
        "estado_inicial": "ABIERTO - solo cualitativo publicado",
        "evidencia_ya_examinada": "contratos de cuatro años publicados; 'attrition rates are monitored' (URD 2019-2025); mejoras de retencion en URD 2019; 'new client wins outpacing churn' y 'lower churn' en la presentacion S1-2026 (§6.1 l491); ninguna tasa ni importe publicado",
        "salida_afecta": "politica PPA 85,7 al año (28% del FCF base); diferencia A1/A2 en el flujo de partida 89,9",
        "limite": "no inferir tasa de bajas a partir de textos cualitativos ni de la duracion de contratos",
    },
    {
        "id": "M6",
        "pregunta": "Finalidad de las compras pequenas de sociedades y crecimiento organico sin ellas; el organico publicado excluye solo adquisiciones importantes (las compras pequenas, 31,5 al año de media en 2023-25, estan dentro del organico publicado).",
        "definicion_fuente": "INFORME_CONCILIACION_F1.md §6.4 l566 (producto 716cbd6; añadido por la revision dirigida V1 y P2)",
        "estado_inicial": "ABIERTO - no localizado en busqueda previa",
        "evidencia_ya_examinada": "crecimiento publicado = organico + externo + divisa (§5, l218); compras pequenas dentro del organico publicado segun §6.4",
        "salida_afecta": "cada millon anual de compras que fuera de reposicion bajaria el flujo sostenible en un millon, tambien en el terminal; sustituye por dato la hipotesis de que las compras son crecimiento (propuesta 4b)",
        "limite": "no re-inferir 'sin compras' del organico publicado; no suponer que dos magnitudes parecidas son la misma partida",
    },
    {
        "id": "N2",
        "pregunta": "Relacion de seguros/resultado por bajas de 2025: donde se cobro, fiscalidad y reposicion de activos; no suponer que dos magnitudes parecidas son la misma partida.",
        "definicion_fuente": "INFORME_CONCILIACION_F1.md l330: plusvalia de 2025 (+25,7 en otros ingresos operativos, 'a high level of insurance benefits in 2025', URD25 p.309); ESPECIFICACION_F1_PROPUESTA.md l114: N2 no se aplica mientras su fiscalidad y su caja no esten identificadas",
        "estado_inicial": "ABIERTO - solo la frase cualitativa publicada",
        "evidencia_ya_examinada": "URD25 p.309 (citada en el informe F1); busqueda previa de §6.1 no hallo fiscalidad ni caja del seguro",
        "salida_afecta": "m0 +0,54 puntos porcentuales (diagnostico); regla N2 pendiente de fiscalidad y caja identificadas",
        "limite": "la plusvalia en OOIE y el ingreso de seguro no se igualan sin evidencia de caja y fiscalidad",
    },
]


def main():
    asegurar_commit(PRODUCTO_F1, f"git fetch {PRODUCTO_URL} {PRODUCTO_F1}", "repositorio del producto (solo lectura)")
    asegurar_commit(REVISION_F1, f"git fetch origin {REVISION_F1}", "rama de revision del auxiliar")
    asegurar_commit(CONTROL, "git fetch origin coordinacion/cierre-v2  # contiene " + CONTROL, "control comun (rama coordinacion/cierre-v2)")
    head_control = subprocess.run(["git", "-C", str(RAIZ), "ls-remote", "origin", "coordinacion/cierre-v2"],
                                  capture_output=True, text=True).stdout.split()[0]
    print(f"control de referencia usado: {CONTROL[:8]}; HEAD remoto actual de coordinacion/cierre-v2: {head_control[:8]}")
    fuentes = json.loads(git_show(PRODUCTO_F1, f"{FRENTE}/datos/fuentes.json"))
    seleccion = json.loads(git_show(REVISION_F1, "revision_externa/f1_v3_20261116/seleccion_fuentes.json"))
    control = json.loads(git_show(CONTROL, "coordinacion/cierre_v2/CONTROL.json"))

    # comprobaciones cruzadas
    sel_by_ruta = {a["ruta"]: a for a in seleccion["archivos"]}
    for tag, info in list(fuentes["fuentes"].items()) + [("libro", fuentes["libro"])]:
        a = sel_by_ruta[info["archivo"]]
        if a["sha256"] != info["sha256"]:
            raise AssertionError(f"sha256 discrepante en {tag}: fuentes.json vs seleccion_fuentes.json")
    h = hashlib.sha256(ZIP_BASE414.read_bytes()).hexdigest()
    if h != SHA_ZIP_BASE414:
        raise AssertionError(f"ZIP base-4.14 local: sha256 {h} != registrado {SHA_ZIP_BASE414}")
    elis = next(t for t in control["tareas"] if t["id"] == "E-ELIS")
    if control["versiones_fijadas"]["f1"] != PRODUCTO_F1 or control["versiones_fijadas"]["revision_F1"] != REVISION_F1:
        raise AssertionError("versiones fijadas del control no coinciden con las usadas")

    # PREGUNTAS_Y_RESULTADOS.csv
    with (SALIDA / "PREGUNTAS_Y_RESULTADOS.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "pregunta", "definicion_fuente", "estado_inicial", "evidencia_ya_examinada",
                    "salida_afecta", "limite", "hallazgo_bloque1", "documentos_paginas_bloque1"])
        for p in PREGUNTAS:
            w.writerow([p["id"], p["pregunta"], p["definicion_fuente"], p["estado_inicial"],
                        p["evidencia_ya_examinada"], p["salida_afecta"], p["limite"],
                        "inventario inicial; sin busqueda nueva en este bloque", "ninguno (bloque 1 = inventario)"])

    # FUENTES_Y_BUSQUEDA.csv
    with (SALIDA / "FUENTES_Y_BUSQUEDA.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["estado", "categoria", "nombre", "ruta_o_recurso", "sha256", "bytes", "ejercicio",
                    "idioma", "examinado_en", "notas"])
        for tag, info in fuentes["fuentes"].items():
            w.writerow(["YA_EXAMINADO_CONSERVADO", "URD/DEU oficial Elis", tag, info["archivo"], info["sha256"],
                        sel_by_ruta[info["archivo"]]["bytes"], info["ejercicio"], info["idioma"],
                        f"producto {PRODUCTO_F1[:8]} frente E/F1; revision externa {REVISION_F1[:8]} (seleccion_fuentes.json)",
                        "Conservado en el ZIP de la Release base-4.14 (tag base-4.14, repo producto); no re-descargar ni re-pedir; lectura previa NO es fuente nueva. " + info["descripcion"]])
        w.writerow(["YA_EXAMINADO_CONSERVADO", "libro evaluado Elis", "libro", fuentes["libro"]["archivo"],
                    fuentes["libro"]["sha256"], sel_by_ruta[fuentes["libro"]["archivo"]]["bytes"], "", "",
                    f"producto {PRODUCTO_F1[:8]} frente E/F1",
                    "Conservado en la Release base-4.14; solo lectura de valores en cache; no modificar"])
        w.writerow(["YA_EXAMINADO_EN_BUSQUEDA_PREVIA", "comunicado de resultados 2025", "comunicado 2025",
                    "carpeta de fuentes de Elis (base 4.14), citado en INFORME §6.1 l489", "", "", 2025, "en/fr",
                    f"producto {PRODUCTO_F1[:8]} frente E/F1 §6.1", "Usado solo como alcance de busqueda; no esta entre las cinco fuentes verificadas; no se vuelve a buscar sin pista nueva"])
        w.writerow(["YA_EXAMINADO_EN_BUSQUEDA_PREVIA", "documentos del primer semestre de 2026", "docs S1-2026",
                    "carpeta de fuentes de Elis, citados en INFORME §6.1 l489-491", "", "", 2026, "en/fr",
                    f"producto {PRODUCTO_F1[:8]} frente E/F1 §6.1", "'new client wins outpacing churn' / 'lower churn' cualitativos; sin tasa ni importe"])
        w.writerow(["YA_EXAMINADO_EN_BUSQUEDA_PREVIA", "extractos de paginas (92 archivos)", "evidencias/paginas/*",
                    f"{FRENTE}/evidencias (producto {PRODUCTO_F1[:8]})", "", "", "2021-2025", "en/fr",
                    f"producto {PRODUCTO_F1[:8]}; revision {REVISION_F1[:8]} evidencia_pdf",
                    "Pasajes acotados de las 5 fuentes verificadas; lectura previa, no fuente nueva"])
        for cat, nota in [
            ("presentacion oficial de resultados / CMD", "prioridad: documento oficial publicado por Elis (web de inversores o AMF), no terceros"),
            ("documento regulatorio (AMF/CSA)", "ej.: informe anual registrado, hecho relevante, folleto; URL oficial y final"),
            ("Q&A de RI publicada", "solo transcripciones/Q&A publicados oficialmente, no contacto privado"),
        ]:
            w.writerow(["CANDIDATO_NUEVO_POR_SELECCIONAR", cat, "", "", "", "", "", "", "bloque 2",
                        "hasta 12 documentos oficiales nuevos en total, seleccionados por relacion con M1/M2/M6/N2; buscadores y terceros son solo pistas"])
    print("escritos", SALIDA / "PREGUNTAS_Y_RESULTADOS.csv", "y", SALIDA / "FUENTES_Y_BUSQUEDA.csv")
    print("control E-ELIS:", elis["entrega"], "| versiones fijadas OK | zip base-4.14 sha256 OK")


if __name__ == "__main__":
    main()
