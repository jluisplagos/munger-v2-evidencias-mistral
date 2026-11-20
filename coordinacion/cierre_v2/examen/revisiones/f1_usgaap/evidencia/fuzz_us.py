#!/usr/bin/env python3
"""Revisión R1 · F1 US GAAP · declaraciones mal formadas al azar: evaluar() no debe lanzar excepciones distintas de ErrorDeclaracion ni dar «utilizable»
con el bloque de arrendamientos incompleto. Uso: python3 -B fuzz_us.py [N]"""
import copy, os, random, shutil, sys, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ayudas
A = ayudas.cargar()
M, libro, decl, fuentes = A["M"], A["libro"], A["decl"], A["fuentes"]
rnd = random.Random(842)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
RAROS = [None, "", 0, 1, -1, 1.5, True, False, [], {}, "fila_8", "fila_14", "no_publicada", "fuera_de_las_filas_8_y_14", "x", {"ubicacion": "fila_14"}, [1, 2], "2025", {"valor": 3}]
def mutar(x, prob=0.15):
    if isinstance(x, dict):
        out = {}
        for k, v in x.items():
            r = rnd.random()
            if r < prob * 0.4:
                continue
            out[k] = rnd.choice(RAROS) if r < prob else mutar(v, prob)
        if rnd.random() < prob * 0.3:
            out[rnd.choice(["ubicacion", "existen", "pagina", "cita", "2025", "valor_fuente", "signo", "literal", "fila", "operativos", "registro"])] = rnd.choice(RAROS)
        return out
    return x
exc = collections.Counter(); util_incompleto = []; n_util = 0
tmp = []
try:
    for i in range(N):
        base = decl(rnd.choice(["A0_total", "A2_propio", "A1_sin_ROU"]), fin=rnd.choice([True, False]), ub_am=rnd.choice(["fila_8", "fila_14", "fuera_de_las_filas_8_y_14", "no_publicada"]),
                    ub_pas=rnd.choice(["fila_14", "fuera_de_las_filas_8_y_14", "no_publicada"]), a8=rnd.choice([None, 10]), ajuste=rnd.choice([None, 10, -10]),
                    rou_fin=rnd.choice([None, 5]), fin_princ=rnd.choice([None, 5]), pasivo=rnd.choice([None, 0, 50]))
        d = mutar(base, prob=rnd.choice([0.03, 0.1, 0.25]))
        L = libro(da=rnd.choice([20.0, 25.0, 30.0]), dwc=rnd.choice([0.0, 10.0, -10.0]), C49=rnd.choice([0.0, 5.0]), princ=rnd.choice([0.0, 5.0]), fila23=rnd.choice([0.0, 50.0]),
                  motor=rnd.choice(["A", "A", "B"]), l4=rnd.choice(["US GAAP", "US GAAP", "IFRS"]))
        try:
            c = fuentes(copy.deepcopy(d) if not isinstance(d.get("series"), dict) or not all(isinstance(v, dict) for v in d["series"].values()) else d)
            tmp.append(c)
        except Exception:
            c = None
        try:
            r = M.evaluar(L, d, carpeta=c)
            json.dumps(r, default=str)
            if r.get("utilizable_para_conclusion"):
                n_util += 1
                b = d.get("arrendamientos_us_gaap")
                ok = isinstance(b, dict) and isinstance((b.get("operativos") or {}).get("existen") if isinstance(b.get("operativos"), dict) else None, bool) \
                    and isinstance((b.get("financieros") or {}).get("existen") if isinstance(b.get("financieros"), dict) else None, bool)
                if not ok:
                    util_incompleto.append((i, json.dumps(d.get("arrendamientos_us_gaap"), default=str)[:200]))
        except M.ErrorDeclaracion:
            exc["ErrorDeclaracion (controlada)"] += 1
        except Exception as ex:
            import traceback
            tb = traceback.extract_tb(ex.__traceback__)[-1]
            exc[f"{type(ex).__name__}: {str(ex)[:60]} @ {os.path.basename(tb.filename)}:{tb.lineno} {tb.name} · {tb.line[:110]}"] += 1
        if len(tmp) > 200:
            for t in tmp: shutil.rmtree(t, ignore_errors=True)
            tmp = []
finally:
    for t in tmp: shutil.rmtree(t, ignore_errors=True)
print(f"{N} declaraciones mal formadas · utilizables: {n_util} · utilizables con el bloque de arrendamientos incompleto: {len(util_incompleto)}")
for k, v in exc.most_common(): print(f"  excepción · {v} veces · {k}")
for x in util_incompleto[:5]: print("  ", x)
