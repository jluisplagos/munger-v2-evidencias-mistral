#!/usr/bin/env python3
"""Comprobador estructural del banco Q1 v2 (Munger V2).
NO ejecuta ni simula el producto: solo valida el banco de casos propuesto.
Uso:
  python comprobar_banco.py [--autocontroles] [--resultado] [--generar-manifiesto]
Codigos de salida: 0 banco valido (y controles negativos detectados si se piden);
1 banco invalido; 2 control negativo no detectado.
"""
import argparse
import ast
import hashlib
import json
import math
import os
import re
import sys
from datetime import datetime, timezone

CAMPOS_TEXTO = ["precondiciones", "entrada_usuario", "riesgo_que_detecta",
                "actividad_que_puede_continuar", "conclusion_afectada",
                "referencia_requisito"]
CAMPOS_LISTA = ["criterios_observables", "conductas_inaceptables"]
CONTROLES = {"POSITIVO", "CONFLICTO_CARENCIA"}
NATURALEZAS = {"CONTRATO_REFERENCIADO", "PROPUESTA_ACEPTACION", "DECISION_PENDIENTE"}
FORMATOS = {"TXT", "CSV", "JSON", "XLSX"}
IDS_ESPERADOS = {f"Q1-{i:03d}" for i in range(1, 37)}


def cargar(ruta):
    casos, errores = [], []
    with open(ruta, encoding="utf-8") as f:
        for n, linea in enumerate(f, 1):
            linea = linea.strip()
            if not linea:
                continue
            try:
                casos.append(json.loads(linea))
            except json.JSONDecodeError as e:
                errores.append(f"linea {n}: JSON invalido ({e})")
    return casos, errores


def es_numero(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def evaluar(operacion, operandos):
    """Evalua solo +,-,*,/ y nombres op0..opN. Devuelve (valor, indices_usados)."""
    arbol = ast.parse(operacion, mode="eval")
    usados = set()
    ops = {ast.Add: lambda a, b: a + b, ast.Sub: lambda a, b: a - b,
           ast.Mult: lambda a, b: a * b, ast.Div: lambda a, b: a / b}

    def nodo(n):
        if isinstance(n, ast.Expression):
            return nodo(n.body)
        if isinstance(n, ast.Constant) and es_numero(n.value):
            return n.value
        if isinstance(n, ast.Name):
            m = re.fullmatch(r"op(\d+)", n.id)
            if not m or int(m.group(1)) >= len(operandos):
                raise ValueError(f"nombre no permitido: {n.id}")
            usados.add(int(m.group(1)))
            return operandos[int(m.group(1))]
        if isinstance(n, ast.BinOp) and type(n.op) in ops:
            return ops[type(n.op)](nodo(n.left), nodo(n.right))
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
            return -nodo(n.operand)
        raise ValueError(f"expresion no permitida: {ast.dump(n)}")

    return nodo(arbol), usados


def validar(casos, base):
    e = []
    ids = [c.get("id") for c in casos]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        e.append(f"ids duplicados: {sorted(dup)}")
    faltan = IDS_ESPERADOS - set(ids)
    sobran = set(ids) - IDS_ESPERADOS
    if faltan:
        e.append(f"faltan ids (cobertura incompleta): {sorted(faltan)}")
    if sobran:
        e.append(f"ids fuera de rango: {sorted(sobran)}")
    for fam in range(1, 7):
        del_fam = [c for c in casos if c.get("familia") == fam]
        if len(del_fam) != 6:
            e.append(f"cobertura incompleta: familia {fam} tiene {len(del_fam)} casos (se esperan 6)")
        pos = sum(1 for c in del_fam if c.get("control") == "POSITIVO")
        if pos != 2:
            e.append(f"positivos familia {fam}: {pos} (se esperan 2)")
    for c in casos:
        cid = c.get("id", "?")
        if not isinstance(c.get("familia"), int) or isinstance(c.get("familia"), bool) or c.get("familia") not in range(1, 7):
            e.append(f"{cid}: familia invalida")
        if c.get("control") not in CONTROLES:
            e.append(f"{cid}: control invalido")
        if c.get("naturaleza") not in NATURALEZAS:
            e.append(f"{cid}: naturaleza invalida")
        if c.get("estado_ejecucion_producto") != "NO_EJECUTADO":
            e.append(f"{cid}: estado_ejecucion_producto debe ser NO_EJECUTADO")
        for campo in CAMPOS_TEXTO:
            if not isinstance(c.get(campo), str) or not c.get(campo).strip():
                e.append(f"{cid}: campo {campo} vacio o ausente")
        for campo in CAMPOS_LISTA:
            v = c.get(campo)
            if not isinstance(v, list) or not v or not all(isinstance(x, str) and x.strip() for x in v):
                e.append(f"{cid}: campo {campo} debe ser lista no vacia de textos")
        arch = c.get("archivos_sinteticos")
        if not isinstance(arch, list):
            e.append(f"{cid}: archivos_sinteticos debe ser lista")
            arch = []
        for a in arch:
            if not isinstance(a, dict) or not all(k in a for k in ("ruta", "formato", "contenido_breve")):
                e.append(f"{cid}: archivo sintetico mal formado")
                continue
            if a["formato"] not in FORMATOS:
                e.append(f"{cid}: formato no permitido {a['formato']}")
            ruta = os.path.join(base, a["ruta"])
            if not os.path.isfile(ruta):
                e.append(f"{cid}: referencia de archivo inexistente {a['ruta']}")
            if a["formato"] == "XLSX" and not os.path.isfile(ruta[:-5] + ".csv"):
                e.append(f"{cid}: XLSX sin CSV companion {a['ruta']}")
        en = c.get("esperado_numerico")
        if en is not None:
            if not isinstance(en, dict) or not all(k in en for k in ("unidad", "operandos", "operacion", "resultado")):
                e.append(f"{cid}: esperado_numerico mal formado")
                continue
            ops = en["operandos"]
            if not isinstance(ops, list) or not ops or not all(es_numero(x) and math.isfinite(x) for x in ops):
                e.append(f"{cid}: operandos invalidos (vacio/booleano/no finito)")
                continue
            res = en["resultado"]
            if not es_numero(res) or not math.isfinite(res):
                e.append(f"{cid}: resultado booleano o no finito")
                continue
            if not isinstance(en["operacion"], str) or not en["operacion"].strip():
                e.append(f"{cid}: operacion vacia")
                continue
            try:
                calc, usados = evaluar(en["operacion"], ops)
            except Exception as ex:
                e.append(f"{cid}: operacion no evaluable ({ex})")
                continue
            if usados != set(range(len(ops))):
                e.append(f"{cid}: operandos ignorados por la operacion (usados {sorted(usados)} de {len(ops)})")
                continue
            if not math.isfinite(calc):
                e.append(f"{cid}: calculo no finito")
                continue
            if not math.isclose(calc, res, rel_tol=1e-9, abs_tol=1e-6):
                e.append(f"{cid}: esperado_numerico incorrecto: recalculado {calc} != declarado {res}")
    return e


def autocontroles(casos, base):
    """Controles negativos sobre copias en memoria; el banco valido no se toca."""
    res = []
    e1 = validar(casos[:-1], base)
    res.append({"control": "ausencia_de_caso", "detectado": any("faltan ids" in x or "cobertura" in x for x in e1)})
    mut = json.loads(json.dumps(casos))
    idx = next(i for i, c in enumerate(mut) if c.get("esperado_numerico"))
    mut[idx]["esperado_numerico"]["resultado"] += 1
    e2 = validar(mut, base)
    res.append({"control": "esperado_numerico_erroneo", "detectado": any("esperado_numerico incorrecto" in x for x in e2)})
    e3 = validar(casos + [casos[0]], base)
    res.append({"control": "id_duplicado", "detectado": any("duplicados" in x for x in e3)})
    # operacion constante que ignora operandos
    mut = json.loads(json.dumps(casos))
    mut[idx]["esperado_numerico"]["operacion"] = str(mut[idx]["esperado_numerico"]["resultado"])
    e4 = validar(mut, base)
    res.append({"control": "operacion_constante_ignora_operandos", "detectado": any("operandos ignorados" in x for x in e4)})
    # resultado booleano aunque el calculo de 1
    mut = json.loads(json.dumps(casos))
    mut[idx]["esperado_numerico"].update({"operandos": [1, 1], "operacion": "op0 * op1", "resultado": True})
    e5 = validar(mut, base)
    res.append({"control": "resultado_booleano", "detectado": any("resultado booleano" in x for x in e5)})
    # calculo no finito (overflow) con operandos finitos
    mut = json.loads(json.dumps(casos))
    mut[idx]["esperado_numerico"].update({"operandos": [1e308, 10.0], "operacion": "op0 * op1", "resultado": 0})
    e6 = validar(mut, base)
    res.append({"control": "calculo_no_finito", "detectado": any("calculo no finito" in x for x in e6)})
    # operando booleano
    mut = json.loads(json.dumps(casos))
    mut[idx]["esperado_numerico"]["operandos"] = [True, 1]
    e7 = validar(mut, base)
    res.append({"control": "operando_booleano", "detectado": any("operandos invalidos" in x for x in e7)})
    return res


def generar_manifiesto(base):
    lineas = []
    for root, dirs, files in os.walk(base):
        dirs[:] = [d for d in dirs if d not in ("__pycache__", ".git")]
        for f in sorted(files):
            if f == "MANIFIESTO_SHA256.txt":
                continue
            ruta = os.path.join(root, f)
            rel = os.path.relpath(ruta, base).replace(os.sep, "/")
            with open(ruta, "rb") as fh:
                huella = hashlib.sha256(fh.read()).hexdigest()
            lineas.append(f"{huella}  {rel}")
    with open(os.path.join(base, "MANIFIESTO_SHA256.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(sorted(lineas)) + "\n")
    return len(lineas)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--autocontroles", action="store_true")
    ap.add_argument("--resultado", action="store_true")
    ap.add_argument("--generar-manifiesto", action="store_true")
    args = ap.parse_args()
    base = os.path.dirname(os.path.abspath(__file__))
    ruta_banco = os.path.join(base, "casos_aceptacion.jsonl")
    print("AVISO: este comprobador valida el banco propuesto, NO el producto Munger V2.")
    if not os.path.isfile(ruta_banco):
        errores, casos, controles = ["casos_aceptacion.jsonl ausente"], [], []
        codigo = 1
    else:
        casos, errores = cargar(ruta_banco)
        errores += validar(casos, base)
        controles = autocontroles(casos, base) if (args.autocontroles and not errores) else []
        if errores:
            codigo = 1
        elif controles and any(not c["detectado"] for c in controles):
            codigo = 2
        else:
            codigo = 0
    resumen = {"casos": len(casos),
               "por_familia": {f: sum(1 for c in casos if c.get("familia") == f) for f in range(1, 7)},
               "positivos_por_familia": {f: sum(1 for c in casos if c.get("familia") == f and c.get("control") == "POSITIVO") for f in range(1, 7)},
               "esperados_numericos": sum(1 for c in casos if c.get("esperado_numerico") is not None),
               "errores": errores, "autocontroles": controles, "codigo_salida": codigo}
    print(json.dumps(resumen, ensure_ascii=False, indent=2))
    if args.resultado:
        with open(os.path.join(base, "resultado_comprobacion.json"), "w", encoding="utf-8", newline="\n") as fh:
            json.dump({"ejecutado": True, "comando": sys.argv, "codigo_salida": codigo,
                       "fecha_utc": datetime.now(timezone.utc).isoformat(),
                       "aviso": "Validacion estructural del banco; no es evidencia sobre el producto.",
                       **resumen}, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
    if args.generar_manifiesto and codigo == 0:
        n = generar_manifiesto(base)
        print(f"MANIFIESTO_SHA256.txt generado con {n} huellas.")
    sys.exit(codigo)


if __name__ == "__main__":
    main()