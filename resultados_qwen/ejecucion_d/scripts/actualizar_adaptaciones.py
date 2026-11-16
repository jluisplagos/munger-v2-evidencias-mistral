#!/usr/bin/env python3
"""Actualiza adaptaciones.json con los resultados del bloque 2 (estados, veredictos, evidencias).

Uso: python3 actualizar_adaptaciones.py
"""
import json
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(AQUI, "especificaciones", "adaptaciones.json")
EV = os.path.join(os.path.dirname(os.path.dirname(AQUI)), "evidencias")

BLOQUE2 = {
    "Q1-005": ("CUMPLE", "evidencias/Q1-005/01_comprobar_derivado_origen_pendiente.json (aux:D pendiente: origen sin comprobar); 04_comprobar_formula_trivial_origenes_comprobados.json (error U4: origen no influye)"),
    "Q1-007": ("CUMPLE", "evidencias/Q1-007/01 (escala no declarada -> discrepancia, no se asume); 03 (unidad declarada miles -> comprobada)"),
    "Q1-008": ("CUMPLE", "evidencias/Q1-008/02 (cita '(1110)' -> comprobada); 03 (control signo -1 -> rechazada)"),
    "Q1-009": ("CUMPLE", "evidencias/Q1-009/01 (cita 480 de otra columna -> discrepancia 0.48 != modelo); 03 (corregido 730833 -> comprobada)"),
    "Q1-010": ("CUMPLE", "evidencias/Q1-010/02 (45054 miles escala 0.001 -> comprobada); 03 (45054 declarados millones -> discrepancia)"),
    "Q1-011": ("CUMPLE", "evidencias/Q1-011/02 (signo -1 con tratamiento declarado -> comprobada); 03 (doble negacion -> discrepancia -49.699 != 49.699)"),
    "Q1-012": ("CUMPLE", "evidencias/Q1-012/01 (perimetro segmento A sin justificacion -> error); 02 (con justificacion pasa el control)"),
    "Q1-013": ("CUMPLE", "evidencias/Q1-013/02_comprobar_trazabilidad_completa.json (comprobada con documento, version, pagina, periodo, unidad, perimetro)"),
    "Q1-014": ("CUMPLE", "evidencias/Q1-014/02 (reexpresado declarado -> comprobada); 03 (aux 2024 original conservado como historico, no vigente)"),
    "Q1-015": ("CUMPLE", "evidencias/Q1-015/01 (conflicto 120000 vs 45054 -> discrepancia con ambas fuentes, sin elegir por favorabilidad); 03 (resuelto con evidencia -> comprobada)"),
    "Q1-016": ("CUMPLE", "evidencias/Q1-016/01 (unidad 'dolares' -> pendiente U7, sin conversion inventada)"),
    "Q1-017": ("CUMPLE", "evidencias/Q1-017/01 y 02 (verificado declarado sin bytes -> no comprobada, apto_por_entradas=false)"),
    "Q1-018": ("CUMPLE", "evidencias/Q1-018/02 (aux:inv_v2 vigente comprobada; aux:inv_v1 historica pendiente; aux:reexpresion 210-190=20 declarada)"),
    "Q1-020": ("CUMPLE", "evidencias/Q1-020/02 (hipotesis sellada -> comprobada An\u0301lisis!C62); 03 (tras cambiar fundamento -> ya no comprobada)"),
    "Q1-021": ("CUMPLE", "evidencias/Q1-021/01 (cita en pagina de la instruccion embebida -> no contiene la cifra, rechazada); 03 (tabla normal -> comprobada)"),
    "Q1-023": ("CUMPLE", "evidencias/Q1-023/01 (periodo 2017 en columna 2016 -> error del contrato); 03 (periodo correcto -> comprobada)"),
    "Q1-024": ("CUMPLE", "evidencias/Q1-024/01 (dato como hipotesis sin justificacion_clase -> error N2); 02 (con justificacion -> listado en datos_como_hipotesis, no publicado)"),
    "Q1-029": ("CUMPLE", "evidencias/Q1-029/02 (3 fuentes presentes -> comprobadas; 2 ausentes -> pendientes R2; recuentos visibles)"),
}


def main():
    data = json.load(open(PATH, encoding="utf-8"))
    for cid, (veredicto, evidencia) in BLOQUE2.items():
        c = data["casos"][cid]
        c["estado"] = "PARCIAL_COMPONENTE"
        c["veredicto"] = veredicto
        c["evidencia"] = evidencia
        spec = os.path.join(AQUI, "especificaciones", "bloque2", cid + ".json")
        c["comandos"] = f"python3 scripts/ejecutar_caso.py scripts/especificaciones/bloque2/{cid}.json"
    json.dump(data, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("actualizados", len(BLOQUE2), "casos")


if __name__ == "__main__":
    main()
