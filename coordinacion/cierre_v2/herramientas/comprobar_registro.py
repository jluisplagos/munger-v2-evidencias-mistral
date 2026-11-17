"""Comprueba el registro de un lanzador (formato «== nombre hora» / «   código N» / «fin …»). Solo biblioteca estándar.

Uso: python3 -I comprobar_registro.py REGISTRO [--esperados N] [--json]
Códigos de salida, cada uno con su causa en la salida:
  0  todos los pasos con código 0 y, si se da --esperados, tantos pasos como los esperados
  1  algún paso con código distinto de 0 (se listan)
  2  error de lectura o registro mal formado: no existe, no se puede leer, está vacío, un paso sin su código, una línea
     que no se entiende o falta la línea «fin» (registro truncado o lanzador interrumpido)
  3  registro bien formado y sin fallos, pero con un número de pasos distinto del esperado
Así «no hay fallos» (0) no se confunde con «no se ha podido leer» (2), como ocurre con grep (1 frente a 2).
"""
import argparse
import json
import re
import sys

PASO = re.compile(r"^== (\S+) (\d\d:\d\d:\d\d)\s*$")
CODIGO = re.compile(r"^\s+código (-?\d+)\s*$")
FIN = re.compile(r"^fin \d\d:\d\d:\d\d\b")


def analizar(ruta):
    try:
        lineas = open(ruta, encoding="utf-8").read().splitlines()
    except (OSError, UnicodeDecodeError) as e:
        return {"resultado": 2, "causa": f"no se puede leer el registro: {e}"}
    pasos, pendiente, fin, malas = [], None, False, []
    for i, l in enumerate(lineas, 1):
        if not l.strip() or l.startswith("#"):
            continue
        if m := PASO.match(l):
            if pendiente:
                malas.append(f"l.{i}: el paso «{pendiente}» no tiene código")
            pendiente = m.group(1)
        elif m := CODIGO.match(l):
            if not pendiente:
                malas.append(f"l.{i}: código sin paso")
            else:
                pasos.append((pendiente, int(m.group(1)))); pendiente = None
        elif FIN.match(l):
            fin = True
        else:
            malas.append(f"l.{i}: línea no reconocida: {l[:80]!r}")
    if pendiente:
        malas.append(f"el paso «{pendiente}» no tiene código (registro truncado)")
    if not pasos and not malas:
        malas.append("el registro no contiene ningún paso")
    if not fin:
        malas.append("falta la línea «fin»: lanzador interrumpido o registro truncado")
    return {"resultado": None, "pasos": pasos, "malas": malas}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("registro"); ap.add_argument("--esperados", type=int); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    d = analizar(a.registro)
    if d["resultado"] is None:
        fallidos = [(n, c) for n, c in d["pasos"] if c != 0]
        if d["malas"]:
            d.update(resultado=2, causa="registro mal formado: " + "; ".join(d["malas"]))
        elif fallidos:
            d.update(resultado=1, causa="pasos con código distinto de 0: " + ", ".join(f"{n}={c}" for n, c in fallidos))
        elif a.esperados is not None and len(d["pasos"]) != a.esperados:
            d.update(resultado=3, causa=f"{len(d['pasos'])} pasos en el registro, {a.esperados} esperados")
        else:
            d.update(resultado=0, causa=f"{len(d['pasos'])} pasos, todos con código 0")
    print(json.dumps(d, ensure_ascii=False) if a.json else f"RESULTADO {d['resultado']} · {d['causa']}")
    return d["resultado"]


if __name__ == "__main__":
    sys.exit(main())
