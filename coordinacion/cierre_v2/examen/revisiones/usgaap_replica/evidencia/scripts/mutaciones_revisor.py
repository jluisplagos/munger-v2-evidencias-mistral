"""Mutaciones de la corrección del margen de partida, con un criterio de detección por recuento (no por el texto de las pruebas):
una mutación se detecta si en alguna de las dos baterías bajan las pruebas que pasan, cambia el total o la batería se interrumpe.
Trabaja en copias temporales bajo /dev/shm/rev_m0/mut (scripts, esquema, prompts y las dos baterías)."""
import os, re, shutil, subprocess, sys, tempfile, json
from concurrent.futures import ThreadPoolExecutor
PV = "/dev/shm/rev_m0/nuevo/munger_v2_r1/personaje_v2"
BAT = ("test_motor_a_f1.py", "test_motor_a_f1_usgaap.py")
sys.path.insert(0, os.path.join(PV, "empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/f1_impl/scripts"))
src_aut = open(os.path.join(PV, "empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/f1_impl/scripts/mutaciones_margen_de_partida.py"), encoding="utf-8").read()
# la lista M del autor, sin ejecutar su script
ns = {}
exec(src_aut[src_aut.index("M = ["):src_aut.index("SRC = ")], ns)
M = list(ns["M"])
M += [
    ("r13 · leer_libro no lee Palancas C8 (solo lo ven las pruebas con libro real)", '("Palancas", "C8:C8"), ', ""),
    ("r18 · media del ciclo con los años disponibles aunque falte alguno (no para)",
     "    return media(margenes) if con_ventas and len(margenes) == len(con_ventas) else None", "    return media(margenes) if margenes else None"),
    ("r22 · la réplica contrasta siempre con C48 (aunque C8 diga «Media del ciclo»)",
     '    celda_m0 = "Historia!C49" if ciclo else "Historia!C48"', '    celda_m0 = "Historia!C48"'),
    ("r23 · la réplica no contrasta Diagnóstico V6 C10 (solo la celda de la Historia y el Motor)",
     'for ref in (celda, "Diagnóstico V6!C10", "Motor!D6", "Motor!D7", "Motor!D8"):', 'for ref in (celda, "Motor!D6", "Motor!D7", "Motor!D8"):'),
]
SRC = open(os.path.join(PV, "scripts", "motor_a_f1.py"), encoding="utf-8").read()
RAIZ = "/dev/shm/rev_m0/mut"; os.makedirs(RAIZ, exist_ok=True)
pat = re.compile(r"^(\d+)/(\d+) pruebas")

def correr(codigo):
    tmp = tempfile.mkdtemp(prefix="m_", dir=RAIZ)
    try:
        pv = os.path.join(tmp, "personaje_v2")
        for d in ("scripts", "esquema", "prompts"):
            shutil.copytree(os.path.join(PV, d), os.path.join(pv, d), ignore=shutil.ignore_patterns("__pycache__"))
        os.makedirs(os.path.join(pv, "pruebas"))
        for b in BAT:
            shutil.copy(os.path.join(PV, "pruebas", b), os.path.join(pv, "pruebas"))
        open(os.path.join(pv, "scripts", "motor_a_f1.py"), "w", encoding="utf-8").write(codigo)
        td = os.path.join(tmp, "tmp"); os.makedirs(td)
        out = {}
        for b in BAT:
            r = subprocess.run([sys.executable, "-B", os.path.join("pruebas", b)], cwd=pv, capture_output=True, text=True,
                               env=dict(os.environ, TMPDIR=td, PYTHONDONTWRITEBYTECODE="1"))
            lin = [l for l in r.stdout.splitlines() if l.startswith("PASA ") or l.startswith("FALLA")]
            tot = [pat.match(l) for l in r.stdout.splitlines() if pat.match(l)]
            ok, n = (int(tot[-1].group(1)), int(tot[-1].group(2))) if tot else (None, None)
            out[b] = {"ok": ok, "n": n, "estados": ["P" if l.startswith("PASA") else "F" for l in lin],
                      "falla": [l[:150] for l in lin if l.startswith("FALLA")], "interrumpida": "Traceback" in r.stderr}
        return out
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

BASE = correr(SRC)
def una(m):
    nombre, viejo, nuevo = m
    if SRC.count(viejo) != 1:
        return nombre, None, f"el texto aparece {SRC.count(viejo)} veces"
    r = correr(SRC.replace(viejo, nuevo))
    det, motivo = False, []
    for b in BAT:
        a, z = BASE[b], r[b]
        if z["interrumpida"] or z["ok"] is None:
            det = True; motivo.append(f"{b}: se interrumpe"); continue
        if z["n"] != a["n"]:
            det = True; motivo.append(f"{b}: total {a['n']} → {z['n']}")
        nuevas = [i for i, (x, y) in enumerate(zip(a["estados"], z["estados"])) if x == "P" and y == "F"]
        if z["ok"] < a["ok"] or nuevas:
            det = True; motivo.append(f"{b}: pasan {a['ok']} → {z['ok']}; primera nueva FALLA: {(z['falla'] or [''])[0][:110]}")
    return nombre, det, "; ".join(motivo) or "ninguna prueba deja de pasar"

with ThreadPoolExecutor(max_workers=3) as ex:
    res = list(ex.map(una, M))
print("sin mutar:", {b: (BASE[b]["ok"], BASE[b]["n"], BASE[b]["falla"]) for b in BAT})
for n, d, mo in res:
    print(("DETECTADA    " if d else ("ERROR        " if d is None else "NO DETECTADA ")) + "· " + n + " · " + mo)
print(f"\n{sum(1 for _, d, _ in res if d)} de {len(res)} mutaciones detectadas por las baterías sintéticas")
