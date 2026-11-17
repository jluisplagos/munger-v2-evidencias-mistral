"""Comprueba el registro de un lanzador (formato «== nombre hora» / «   código N» / «fin …»). Solo biblioteca estándar.

Uso: python3 -I comprobar_registro.py REGISTRO [--esperados N] [--json]
Códigos de salida, cada uno con su causa en la salida:
  0  todos los pasos con código 0 y, si se da --esperados, tantos pasos como los esperados
  1  algún paso con código distinto de 0 (se listan)
  2  error de lectura o registro mal formado o inconsistente: no existe, no se puede leer, está vacío, un paso sin su
     código, una línea que no se entiende, falta la línea «fin» (registro truncado o lanzador interrumpido), hay más de
     una o hay pasos o códigos después de ella, o el resumen ampliado contradice los pasos leídos
  3  registro bien formado y sin fallos, pero con un número de pasos distinto del esperado (el de --esperados o el que
     declara el propio resumen ampliado)

Cierre del registro. Debe haber exactamente una línea «fin», la última. Se aceptan dos formatos:
  histórico  «fin HH:MM:SS» (lanzadores anteriores, p. ej. C18)
  ampliado   «fin HH:MM:SS · ejecutados N · esperados M · fallidos K · resultado R» (lanzador_comun.sh)
En el ampliado se exige N = pasos leídos, K = pasos con código ≠ 0 y R = 1 si K > 0, si no 3 si N ≠ M, si no 0 (las
reglas de terminar). La cabecera «# lanzador · inicio … · esperados M», si existe, debe declarar el mismo M.
Así «no hay fallos» (0) no se confunde con «no se ha podido leer» (2), como ocurre con grep (1 frente a 2).
"""
import argparse
import json
import re
import sys

PASO = re.compile(r"^== (\S+) (\d\d:\d\d:\d\d)\s*$")
CODIGO = re.compile(r"^\s+código (-?\d+)\s*$")
FIN_HIST = re.compile(r"^fin \d\d:\d\d:\d\d\s*$")
FIN_AMPL = re.compile(r"^fin \d\d:\d\d:\d\d · ejecutados (\d+) · esperados (\d+) · fallidos (\d+) · resultado (\d+)\s*$")
CABECERA = re.compile(r"^# lanzador · inicio \S+ · esperados (\d+)\s*$")


def analizar(ruta):
    try:
        lineas = open(ruta, encoding="utf-8").read().splitlines()
    except (OSError, UnicodeDecodeError) as e:
        return {"resultado": 2, "causa": f"no se puede leer el registro: {e}"}
    pasos, pendiente, fin, malas, resumen, cabecera = [], None, False, [], None, None
    for i, l in enumerate(lineas, 1):
        if not l.strip():
            continue
        if l.startswith("#"):
            if m := CABECERA.match(l):
                cabecera = int(m.group(1))
            continue
        if fin and not l.startswith("fin"):
            malas.append(f"l.{i}: contenido después de la línea «fin»: {l[:60]!r}")
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
        elif l.startswith("fin"):
            if fin:
                malas.append(f"l.{i}: segunda línea «fin»")
                continue
            if pendiente:
                malas.append(f"l.{i}: «fin» antes del código del paso «{pendiente}»")
                pendiente = None
            if m := FIN_AMPL.match(l):
                resumen = tuple(int(x) for x in m.groups())
            elif not FIN_HIST.match(l):
                malas.append(f"l.{i}: línea «fin» con formato no reconocido: {l[:80]!r}")
            fin = True
        else:
            malas.append(f"l.{i}: línea no reconocida: {l[:80]!r}")
    if pendiente:
        malas.append(f"el paso «{pendiente}» no tiene código (registro truncado)")
    if not pasos and not malas:
        malas.append("el registro no contiene ningún paso")
    if not fin:
        malas.append("falta la línea «fin»: lanzador interrumpido o registro truncado")
    declarados = None
    if resumen:
        n, m, k, r = resumen
        leidos, fallidos = len(pasos), sum(1 for _, c in pasos if c != 0)
        r_ok = 1 if fallidos else (3 if leidos != m else 0)
        if n != leidos:
            malas.append(f"el resumen declara {n} ejecutados y hay {leidos} pasos")
        if k != fallidos:
            malas.append(f"el resumen declara {k} fallidos y hay {fallidos} pasos con código ≠ 0")
        if r != r_ok:
            malas.append(f"el resumen declara resultado {r} y los pasos dan {r_ok}")
        if cabecera is not None and cabecera != m:
            malas.append(f"la cabecera declara {cabecera} esperados y el resumen {m}")
        declarados = m
    return {"resultado": None, "pasos": pasos, "malas": malas, "esperados_declarados": declarados}


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
        elif d["esperados_declarados"] is not None and len(d["pasos"]) != d["esperados_declarados"]:
            d.update(resultado=3, causa=f"{len(d['pasos'])} pasos en el registro, {d['esperados_declarados']} esperados según su resumen")
        else:
            d.update(resultado=0, causa=f"{len(d['pasos'])} pasos, todos con código 0")
    print(json.dumps(d, ensure_ascii=False) if a.json else f"RESULTADO {d['resultado']} · {d['causa']}")
    return d["resultado"]


if __name__ == "__main__":
    sys.exit(main())
