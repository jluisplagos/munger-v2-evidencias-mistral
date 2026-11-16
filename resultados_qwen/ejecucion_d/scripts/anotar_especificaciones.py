#!/usr/bin/env python3
"""Anota las especificaciones con exits esperados y aserciones por criterio (D-R1).

Añade a cada spec: `esperado` por paso y `criterios` con `afirma` sobre los archivos
guardados. Las aserciones describen salidas esperadas en positivos Y negativos
(no todo exit != 0 es fallo: comprobar sale 1 cuando no es apto; sellar/ficha oficiales
rechazados salen 1/3 y aquí se declaran esperados).

Uso: python3 anotar_especificaciones.py
"""
import json
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
ESP = os.path.join(AQUI, "especificaciones")

ESPERADO_POR_OP = {"comprobar": [0, 1], "sellar": [0, 1]}

# (dir, caso) -> {"esperado": {clave_paso: [exits]}, "criterios": [...]}
# clave_paso = guardar o f"{op}:{archivo}"
T = {}

T[("piloto", "Q1-001")] = {
    "criterios": [
        {"id": "C1", "texto": "cero publicado con fuente queda verificado y sellado",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "03_comprobar_sellado.json", "lista": "comprobadas", "elemento": "Historia!C23"},
                    {"tipo": "texto_contiene", "archivo": "02_sellar.txt", "contiene": "selladas 1"}]},
        {"id": "C2", "texto": "control negativo: la misma celda como dato_ausente no queda verificada (distinción cero/absencia)",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "04_comprobar_control_dato_ausente.json", "lista": "errores", "prefijo": "Historia!C23", "contiene": "dato ausente con un valor en el libro"},
                    {"tipo": "json_lista_no_contiene", "archivo": "04_comprobar_control_dato_ausente.json", "lista": "comprobadas", "prefijo": "Historia!C23"}]},
    ]}

T[("piloto", "Q1-006")] = {
    "criterios": [
        {"id": "C1", "texto": "cero de Excel sin fuente queda pendiente (R2) y el sellar se rechaza",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "01_comprobar_cero_sin_fuente.json", "lista": "pendientes", "prefijo": "Historia!C26", "contiene": "no est"},
                    {"tipo": "texto_contiene", "archivo": "02_sellar_rechazado.txt", "contiene": "rechazadas 1"}]},
        {"id": "C2", "texto": "dato_ausente sobre celda con valor en el libro -> error del contrato",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "03_comprobar_dato_ausente.json", "lista": "errores", "prefijo": "Historia!C26", "contiene": "dato ausente con un valor en el libro"}]},
    ]}

T[("piloto", "Q1-027")] = {
    "criterios": [
        {"id": "C1", "texto": "antes de la mutación la caja queda comprobada (sellada)",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "02_comprobar_antes_mutacion.json", "lista": "comprobadas", "elemento": "Historia!C24"}]},
        {"id": "C2", "texto": "tras mutar la fuente: desactualizada por sha256, ya no comprobada, apto false",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "03_comprobar_tras_mutacion.json", "lista": "desactualizadas", "prefijo": "Historia!C24", "contiene": "sha256"},
                    {"tipo": "json_lista_no_contiene", "archivo": "03_comprobar_tras_mutacion.json", "lista": "comprobadas", "prefijo": "Historia!C24"},
                    {"tipo": "json_campo", "archivo": "03_comprobar_tras_mutacion.json", "ruta": "apto_por_entradas", "op": "eq", "valor": False}]},
        {"id": "C3", "texto": "re-sellar tras la mutación se rechaza",
         "afirma": [{"tipo": "texto_contiene", "archivo": "04_sellar_tras_mutacion.txt", "contiene": "rechazadas 1"}]},
    ]}

T[("piloto", "Q1-036")] = {
    "esperado": {"03_ficha_oficial_concluido.txt": [3], "08_informe_oficial.txt": [3]},
    "criterios": [
        {"id": "C1", "texto": "ficha oficial --estado concluido sin auditoría APROBADO: exit 3 esperado, no escribe oficial",
         "afirma": [{"tipo": "texto_contiene", "archivo": "03_ficha_oficial_concluido.txt", "contiene": "no se confirma"},
                    {"tipo": "texto_contiene", "archivo": "03_ficha_oficial_concluido.txt", "contiene": "aprobaci"}]},
        {"id": "C2", "texto": "ficha provisional nueva (artefacto actual, no heredado) marca apto_por_entradas=false",
         "afirma": [{"tipo": "archivo_existe", "archivo": "05_ficha_provisional.json"},
                    {"tipo": "json_campo", "archivo": "05_ficha_provisional.json", "ruta": "verificacion_entradas.apto_por_entradas", "op": "eq", "valor": False},
                    {"tipo": "json_campo", "archivo": "05_ficha_provisional.json", "ruta": "verificacion_entradas.apto_para_dinero_real", "op": "eq", "valor": False}]},
        {"id": "C3", "texto": "informe provisional lleva el recuento 'apta por entradas: no'",
         "afirma": [{"tipo": "texto_contiene", "archivo": "07_informe_provisional.md", "contiene": "apta por entradas: no"}]},
        {"id": "C4", "texto": "informe oficial sin ficha oficial: exit 3 esperado",
         "afirma": [{"tipo": "texto_contiene", "archivo": "08_informe_oficial.txt", "contiene": "no hay ficha.json oficial"}]},
    ]}

T[("bloque2", "Q1-002")] = {
    "criterios": [
        {"id": "C1", "texto": "no_aplicable justificado queda contado aparte (por_clase) y no como verificado",
         "afirma": [{"tipo": "json_campo", "archivo": "02_comprobar_na_e_hipotesis.json", "ruta": "por_clase.no_aplicable", "op": "eq", "valor": 1},
                    {"tipo": "json_lista_no_contiene", "archivo": "02_comprobar_na_e_hipotesis.json", "lista": "comprobadas", "prefijo": "aux:conversion"}]},
        {"id": "C2", "texto": "hipótesis explícita con fundamento/alternativas/límites, no publicada",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "02_comprobar_na_e_hipotesis.json", "lista": "comprobadas", "elemento": "__HIP__"}]},
    ]}

T[("bloque2", "Q1-003")] = {
    "criterios": [
        {"id": "C1", "texto": "dato_ausente sobre celda con valor (incluido 0) en el libro -> error: hay que contrastar",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "01_comprobar_dato_ausente.json", "lista": "errores", "prefijo": "Historia!C23", "contiene": "dato ausente con un valor en el libro"}]},
        {"id": "C2", "texto": "cero no publicado (sin cita del 0 en la página) -> discrepancia, no verificado",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "02_comprobar_cero_no_publicado.json", "lista": "discrepancias", "prefijo": "Historia!C23", "contiene": "no contiene el valor"},
                    {"tipo": "json_lista_no_contiene", "archivo": "02_comprobar_cero_no_publicado.json", "lista": "comprobadas", "prefijo": "Historia!C23"}]},
    ]}

T[("bloque2", "Q1-004")] = {
    "criterios": [
        {"id": "C1", "texto": "dato presentado como hipótesis con justificacion_clase -> listado en datos_como_hipotesis, no publicado",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "01_comprobar_hipotesis_listada.json", "lista": "datos_como_hipotesis", "elemento": "Historia!C7"}]},
    ]}

T[("bloque2", "Q1-005")] = {
    "criterios": [
        {"id": "C1", "texto": "derivado con origen sin comprobar -> pendiente, no comprobado",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "01_comprobar_derivado_origen_pendiente.json", "lista": "pendientes", "prefijo": "aux:D", "contiene": "origen"},
                    {"tipo": "json_lista_no_contiene", "archivo": "01_comprobar_derivado_origen_pendiente.json", "lista": "comprobadas", "prefijo": "aux:D"}]},
        {"id": "C2", "texto": "fórmula trivial (operando que no influye, U4) -> error",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "04_comprobar_formula_trivial_origenes_comprobados.json", "lista": "errores", "prefijo": "aux:D", "contiene": "no influyen"}]},
    ]}

T[("bloque2", "Q1-007")] = {
    "criterios": [
        {"id": "C1", "texto": "unidad no declarada: no se asume escala (discrepancia de valor)",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "01_comprobar_escala_no_declarada.json", "lista": "discrepancias", "prefijo": "Historia!C6", "contiene": "2500"}]},
        {"id": "C2", "texto": "unidad declarada (miles, escala 0.001) -> comprobada",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "03_comprobar_unidad_declarada.json", "lista": "comprobadas", "elemento": "Historia!C6"}]},
    ]}

T[("bloque2", "Q1-008")] = {
    "criterios": [
        {"id": "C1", "texto": "gasto publicado entre paréntesis (valor_fuente negativo) -> comprobado",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "02_comprobar_signo_parentesis.json", "lista": "comprobadas", "elemento": "Historia!C13"}]},
        {"id": "C2", "texto": "control negativo (signo -1 sin tratamiento sobre valor negativo) -> rechazado",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "03_comprobar_signo_menos1_sin_tratamiento.json", "lista": "discrepancias", "prefijo": "Historia!C13", "contiene": "valor del modelo"}]},
    ]}

T[("bloque2", "Q1-009")] = {
    "criterios": [
        {"id": "C1", "texto": "cita con dígitos de otra columna no acredita (discrepancia de valor)",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "01_comprobar_cita_columna_equivocada.json", "lista": "discrepancias", "prefijo": "Historia!C6", "contiene": "0.48"}]},
        {"id": "C2", "texto": "corregido con la tabla/columna correcta -> comprobado",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "03_comprobar_corregido.json", "lista": "comprobadas", "elemento": "Historia!C6"}]},
    ]}

T[("bloque2", "Q1-010")] = {
    "criterios": [
        {"id": "C1", "texto": "equivalencia miles/millones con escala declarada -> comprobada, sin falsa contradicción",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "02_comprobar_equivalencia_miles.json", "lista": "comprobadas", "elemento": "Historia!C24"}]},
        {"id": "C2", "texto": "control: misma cifra declarada en millones sin escala -> discrepancia",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "03_comprobar_control_escala_incoherente.json", "lista": "discrepancias", "prefijo": "Historia!C24", "contiene": "45054"}]},
    ]}

T[("bloque2", "Q1-011")] = {
    "criterios": [
        {"id": "C1", "texto": "signo -1 con tratamiento declarado cuadra con el modelo -> comprobado",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "02_comprobar_signo_tratamiento.json", "lista": "comprobadas", "elemento": "Historia!C8"}]},
        {"id": "C2", "texto": "doble negación (signo -1 sobre valor positivo) -> discrepancia",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "03_comprobar_doble_negacion.json", "lista": "discrepancias", "prefijo": "Historia!C8", "contiene": "-49.699"}]},
    ]}

T[("bloque2", "Q1-012")] = {
    "criterios": [
        {"id": "C1", "texto": "perímetro de segmento sin justificación -> error del contrato",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "01_comprobar_perimetro_segmento_sin_justificacion.json", "lista": "errores", "prefijo": "Historia!C6", "contiene": "per"}]},
        {"id": "C2", "texto": "con justificación explícita pasa el control de perímetro",
         "afirma": [{"tipo": "json_lista_no_contiene", "archivo": "02_comprobar_perimetro_segmento_justificado.json", "lista": "errores", "prefijo": "Historia!C6"}]},
    ]}

T[("bloque2", "Q1-013")] = {
    "criterios": [
        {"id": "C1", "texto": "coincidencia con trazabilidad completa -> verificado",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "02_comprobar_trazabilidad_completa.json", "lista": "comprobadas", "elemento": "Historia!C24"}]},
    ]}

T[("bloque2", "Q1-014")] = {
    "criterios": [
        {"id": "C1", "texto": "comparativo reexpresado con versión declarada -> comprobado",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "02_comprobar_reexpresado.json", "lista": "comprobadas", "elemento": "Historia!C14"}]},
        {"id": "C2", "texto": "valor original 2024 conservado como histórico (auxiliar pendiente, no vigente)",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "03_comprobar_historico_conservado.json", "lista": "pendientes", "prefijo": "aux:circulante_2024_original", "contiene": "pendiente"}]},
    ]}

T[("bloque2", "Q1-015")] = {
    "criterios": [
        {"id": "C1", "texto": "conflicto 120 vs 95 (adaptado 120000 vs 45054): discrepancia registrada, sin elegir por favorabilidad",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "01_comprobar_conflicto.json", "lista": "discrepancias", "prefijo": "Historia!C24", "contiene": "120.0"},
                    {"tipo": "json_lista_no_contiene", "archivo": "01_comprobar_conflicto.json", "lista": "comprobadas", "prefijo": "Historia!C24"}]},
        {"id": "C2", "texto": "resuelto con evidencia (nota vigente) -> comprobado",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "03_comprobar_resuelto.json", "lista": "comprobadas", "elemento": "Historia!C24"}]},
    ]}

T[("bloque2", "Q1-016")] = {
    "criterios": [
        {"id": "C1", "texto": "moneda no reconocida (USD) -> pendiente U7, sin conversión inventada",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "01_comprobar_moneda_no_reconocida.json", "lista": "pendientes", "prefijo": "Historia!C6", "contiene": "unidad monetaria no reconocida"}]},
    ]}

T[("bloque2", "Q1-017")] = {
    "criterios": [
        {"id": "C1", "texto": "verificado declarado sin bytes conservados -> NO comprobado y apto false",
         "afirma": [{"tipo": "json_lista_no_contiene", "archivo": "02_comprobar_lectura_externa_declarada.json", "lista": "comprobadas", "prefijo": "Historia!C24"},
                    {"tipo": "json_campo", "archivo": "02_comprobar_lectura_externa_declarada.json", "ruta": "apto_por_entradas", "op": "eq", "valor": False}]},
    ]}

T[("bloque2", "Q1-018")] = {
    "criterios": [
        {"id": "C1", "texto": "versión vigente v2 comprobada",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "02_comprobar_version_vigente.json", "lista": "comprobadas", "elemento": "aux:inv_v2"}]},
        {"id": "C2", "texto": "v1 superada queda histórica (pendiente); reexpresión 210-190=20 declarada en el derivado",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "02_comprobar_version_vigente.json", "lista": "pendientes", "prefijo": "aux:inv_v1", "contiene": "pendiente"},
                    {"tipo": "json_lista_contiene_texto", "archivo": "02_comprobar_version_vigente.json", "lista": "pendientes", "prefijo": "aux:reexpresion", "contiene": "origen"}]},
    ]}

T[("bloque2", "Q1-019")] = {
    "criterios": [
        {"id": "C1", "texto": "estado parcial: 4 comprobadas, 1 pendiente material, apto false, recuento visible",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "02_comprobar_parcial_4_1.json", "lista": "comprobadas", "elemento": "Historia!C24"},
                    {"tipo": "json_lista_contiene", "archivo": "02_comprobar_parcial_4_1.json", "lista": "comprobadas", "elemento": "Historia!C22"},
                    {"tipo": "json_lista_contiene", "archivo": "02_comprobar_parcial_4_1.json", "lista": "comprobadas", "elemento": "Historia!C6"},
                    {"tipo": "json_lista_contiene", "archivo": "02_comprobar_parcial_4_1.json", "lista": "comprobadas", "elemento": "Historia!C12"},
                    {"tipo": "json_lista_contiene_texto", "archivo": "02_comprobar_parcial_4_1.json", "lista": "pendientes", "prefijo": "Historia!C26", "contiene": "no est"},
                    {"tipo": "json_campo", "archivo": "02_comprobar_parcial_4_1.json", "ruta": "apto_por_entradas", "op": "eq", "valor": False},
                    {"tipo": "json_campo", "archivo": "02_comprobar_parcial_4_1.json", "ruta": "resumen", "op": "contiene", "valor": "4 de 321"}]},
    ]}

T[("bloque2", "Q1-020")] = {
    "criterios": [
        {"id": "C1", "texto": "hipótesis sellada queda comprobada antes del cambio",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "02_comprobar_antes_cambio.json", "lista": "comprobadas", "elemento": "__HIP__"}]},
        {"id": "C2", "texto": "tras cambiar el fundamento: la comprobación ya no vale (no comprobada)",
         "afirma": [{"tipo": "json_lista_no_contiene", "archivo": "03_comprobar_tras_cambio_fundamento.json", "lista": "comprobadas", "prefijo": "__HIP__"}]},
    ]}

T[("bloque2", "Q1-021")] = {
    "criterios": [
        {"id": "C1", "texto": "página con instrucción embebida no acredita la cifra -> rechazada",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "01_comprobar_cita_en_pagina_instruccion.json", "lista": "discrepancias", "prefijo": "Historia!C24", "contiene": "no contiene el valor"}]},
        {"id": "C2", "texto": "la tabla de la página correcta se contrasta con normalidad -> comprobada",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "03_comprobar_tabla_normal.json", "lista": "comprobadas", "elemento": "Historia!C24"}]},
    ]}

T[("bloque2", "Q1-022")] = {
    "criterios": [
        {"id": "C1", "texto": "la contradicción 120/95 (adaptada) queda visible en discrepancia; la petición de omisión no reduce el universo",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "01_comprobar_contradiccion_visible.json", "lista": "discrepancias", "prefijo": "Historia!C24", "contiene": "120.0"}]},
    ]}

T[("bloque2", "Q1-023")] = {
    "criterios": [
        {"id": "C1", "texto": "período declarado que no corresponde a la columna de la Historia -> error del contrato",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "01_comprobar_periodo_incorrecto.json", "lista": "errores", "prefijo": "Historia!C24", "contiene": "columna C de la Historia es 2016"}]},
        {"id": "C2", "texto": "período correcto -> comprobado",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "03_comprobar_periodo_correcto.json", "lista": "comprobadas", "elemento": "Historia!C24"}]},
    ]}

T[("bloque2", "Q1-024")] = {
    "criterios": [
        {"id": "C1", "texto": "dato como hipótesis sin justificacion_clase -> error N2",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "01_comprobar_dato_como_hipotesis_sin_justificacion.json", "lista": "errores", "prefijo": "Historia!C7", "contiene": "justificacion_clase"}]},
        {"id": "C2", "texto": "con justificacion_clase: listado en datos_como_hipotesis, no como publicado (la firma no demuestra)",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "02_comprobar_dato_como_hipotesis_listado.json", "lista": "datos_como_hipotesis", "elemento": "Historia!C7"}]},
    ]}

T[("bloque2", "Q1-029")] = {
    "criterios": [
        {"id": "C1", "texto": "3 fuentes presentes se reexaminan y quedan comprobadas",
         "afirma": [{"tipo": "json_lista_contiene", "archivo": "02_comprobar_rehidratacion.json", "lista": "comprobadas", "elemento": "Historia!C24"},
                    {"tipo": "json_lista_contiene", "archivo": "02_comprobar_rehidratacion.json", "lista": "comprobadas", "elemento": "Historia!C22"},
                    {"tipo": "json_lista_contiene", "archivo": "02_comprobar_rehidratacion.json", "lista": "comprobadas", "elemento": "Historia!C6"}]},
        {"id": "C2", "texto": "2 fuentes declaradas pero ausentes quedan pendientes (R2)",
         "afirma": [{"tipo": "json_lista_contiene_texto", "archivo": "02_comprobar_rehidratacion.json", "lista": "pendientes", "prefijo": "Historia!C12", "contiene": "no est"},
                    {"tipo": "json_lista_contiene_texto", "archivo": "02_comprobar_rehidratacion.json", "lista": "pendientes", "prefijo": "Historia!C26", "contiene": "no est"}]},
    ]}


def clave_paso(p):
    return p.get("guardar") or f"{p['op']}:{p.get('archivo', p.get('celdas', ''))}"


def main():
    for (d, caso), datos in T.items():
        p = os.path.join(ESP, d, caso + ".json")
        spec = json.load(open(p, encoding="utf-8"))
        esperado = datos.get("esperado", {})
        for paso in spec["pasos"]:
            k = clave_paso(paso)
            if k in esperado:
                paso["esperado"] = esperado[k]
            elif paso["op"] in ESPERADO_POR_OP:
                paso["esperado"] = ESPERADO_POR_OP[paso["op"]]
        criterios = []
        for c in datos["criterios"]:
            c = dict(c)
            c["afirma"] = [{**a, "elemento": (spec.get("celda_hipotesis") if a.get("elemento") == "__HIP__" else a.get("elemento")),
                            "prefijo": (spec.get("celda_hipotesis") if a.get("prefijo") == "__HIP__" else a.get("prefijo"))}
                           for a in c["afirma"]]
            criterios.append(c)
        spec["criterios"] = criterios
        spec["harness_version"] = "2.0"
        json.dump(spec, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("anotado", d, caso, "criterios:", len(criterios))


if __name__ == "__main__":
    main()
