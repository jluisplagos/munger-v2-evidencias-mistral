"""Mutaciones de la corrección C2 (perimetro_f1.py, margen de partida según Palancas C8) frente a test_perimetro_foso.py, por recuento.
Cada mutación se aplica a perimetro_f1.py de la copia limpia, se corre la batería y se repone el original (comprobado con su huella)."""
import hashlib, re, subprocess, sys
L = sys.argv[1]
P = f"{L}/scripts/perimetro_f1.py"
SRC = open(P, encoding="utf-8").read(); H = hashlib.sha256(SRC.encode()).hexdigest()
M = [
    ("p1 · «Media del ciclo» toma C48", '        return c49, "Historia!C49"', '        return c48, "Historia!C48"'),
    ("p2 · un valor fuera de la lista se toma como «Último año»", "    return None, None\n\n\ndef desde_datos", '    return c48, "Historia!C48"\n\n\ndef desde_datos'),
    ("p3 · desde_datos no lee C8", '    base = (t.get("palancas") or {}).get("C8")', "    base = None"),
    ("p4 · desde_libro no lee C8", '    m0, celda = margen_de_partida(g("Palancas!C8"), g("Historia!C48"), g("Historia!C49"))',
     '    m0, celda = margen_de_partida(None, g("Historia!C48"), g("Historia!C49"))'),
    ("p5 · el texto rotula siempre Historia!C48", '    return f"Con el margen de partida del Motor ({celda} = {_f(m0)}; "',
     '    return f"Con el margen de partida del Motor (Historia!C48 = {_f(m0)}; "'),
    ("p6 · con C49 vacía se cae en C48", '        return c49, "Historia!C49"', '        return (c49 if c49 is not None else c48), "Historia!C49"'),
]
def correr():
    r = subprocess.run([sys.executable, "-B", "pruebas/test_perimetro_foso.py"], cwd=L, capture_output=True, text=True)
    m = re.search(r"^(\d+)/(\d+) pruebas del perímetro", r.stdout, re.M)
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)
base = correr(); print("sin mutar:", base)
det = 0
try:
    for n, a, b in M:
        assert SRC.count(a) == 1, n
        open(P, "w", encoding="utf-8").write(SRC.replace(a, b))
        ok, tot = correr()
        d = ok is None or ok < base[0] or tot != base[1]; det += d
        print(("DETECTADA    " if d else "NO DETECTADA ") + f"· {n} · pasan {ok} de {tot}")
finally:
    open(P, "w", encoding="utf-8").write(SRC)
assert hashlib.sha256(open(P, encoding="utf-8").read().encode()).hexdigest() == H
print(f"{det} de {len(M)} detectadas; perimetro_f1.py repuesto (huella comprobada)")
