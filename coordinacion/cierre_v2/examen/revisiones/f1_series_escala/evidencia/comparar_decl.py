"""Compara F1-SERIES (código viejo frente al nuevo) en todas las declaraciones motor_a_f1*.json del paquete. Uso: python3 -B comparar_decl.py <scripts> <viejo_dir> <raiz>"""
import importlib.util, json, os, sys, glob
sys.path.insert(0, sys.argv[1])
import motor_a_f1 as N
spec = importlib.util.spec_from_file_location("viejo", os.path.join(sys.argv[2], "motor_a_f1.py")); V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)
n = dif = 0
for p in sorted(glob.glob(os.path.join(sys.argv[3], "**", "*.json"), recursive=True)):
    try: d = json.load(open(p, encoding="utf-8"))
    except Exception: continue
    if not isinstance(d, dict) or "series" not in d or not isinstance(d.get("series"), dict): continue
    out = []
    for Mod in (V, N):
        G, r = Mod.Guardas(), {}
        Mod._guarda_fuentes_series(G, d, os.path.dirname(p), list(range(2005, 2031)), r)
        x = [y for y in G.lista if y["id"] == "F1-SERIES"][0]
        ls = []
        for nm in Mod.SERIES:
            ls.append(Mod.leer_serie(d, nm, list(range(2005, 2031))))
        out.append((x["salta"], x["severidad"], x["efecto"], x["detalle"], json.dumps(r["F1_SERIES"], sort_keys=True, default=str), repr(ls)))
    n += 1
    if out[0] != out[1]:
        dif += 1; print("DISTINTO", p); print("  viejo", out[0][:4]); print("  nuevo", out[1][:4])
print(f"{n} declaraciones con series; {dif} con F1-SERIES o leer_serie distintos")
