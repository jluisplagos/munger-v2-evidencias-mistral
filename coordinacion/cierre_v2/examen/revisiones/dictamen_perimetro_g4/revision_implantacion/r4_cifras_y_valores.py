"""Revisión de la implantación de P-FOSO · R4: (a) las cifras del módulo perimetro_f1.py frente a la réplica del dictamen (replica/motor.py y
02_perimetro_ahold.py: 13,03 %, 14,82 %, 8,78 % y neutro 9,04 %); (b) las filas «V-F1g (valores)» y «V-F1k (valores)» con cada juego de
palancas del dictamen (las palancas se cambian en memoria sobre los valores leídos del libro recalculado; nada se escribe).
Uso: r4_cifras_y_valores.py RAIZ_PERSONAJE_V2 COPIA_EXPEDIENTE_CON_LA_SERIE"""
import json, os, sys

PV, EXP = sys.argv[1], sys.argv[2]
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), "replica"))
sys.path.insert(0, os.path.join(PV, "scripts"))
sys.dont_write_bytecode = True
import motor as R                   # réplica del dictamen  # noqa: E402
import perimetro_f1 as PF           # noqa: E402
import motor_a_f1 as M              # noqa: E402

libro = os.path.join(EXP, "recalc", "Ahold_v63_evaluada.xlsx")
decl = json.load(open(os.path.join(EXP, "motor_a_f1.json"), encoding="utf-8"))
T = json.load(open(os.path.join(EXP, "datos_v63.json"), encoding="utf-8"))
pf = PF.desde_datos(T, decl, EXP)

# --- (a) réplica independiente de las tres medias (filas de la Historia leídas del libro por la réplica) y del neutro
Lr = R.leer(libro, R.RANGOS)
anios = [int(Lr[f"Historia!{c}5"]) for c in R.COLS_HIST]
H = lambda n: dict(zip(anios, [Lr.get(f"Historia!{c}{n}") for c in R.COLS_HIST]))
EBIT, t, arr, cap = H(7), H(10), H(23), H(32)
INT = {2021: 337, 2022: 356, 2023: 382, 2024: 422, 2025: 465}
u = anios[-5:]
rep = {"roic_propio_pagado_el_alquiler_medio": sum((EBIT[y] - INT[y]) * (1 - t[y]) / (cap[y] - arr[y]) for y in u) / 5,
       "roic_sin_arrendamientos_medio": sum(EBIT[y] * (1 - t[y]) / (cap[y] - arr[y]) for y in u) / 5,
       "roic_todo_el_capital_medio": sum(EBIT[y] * (1 - t[y]) / cap[y] for y in u) / 5}
base, pal = R.base_del_libro(Lr), R.palancas_del_libro(Lr)
ok = True
for k, v in rep.items():
    d = abs(pf[k] - v)
    ok &= d < 1e-12
    print(f"{k:<40} módulo {pf[k]:.10f} · réplica {v:.10f} · dif {d:.1e}")
N0 = base["m0"] * (1 - base["tau"])
neu0 = base["r"] * N0 / (N0 - base["f"])
print(f"{'roic_neutro_con_m0':<40} módulo {pf['roic_neutro_con_m0']:.10f} · réplica {neu0:.10f} · dif {abs(pf['roic_neutro_con_m0'] - neu0):.1e}")
ok &= abs(pf["roic_neutro_con_m0"] - neu0) < 1e-12
for e in R.ESC:
    N = pal[e]["mobj"] * (1 - base["tau"])
    print(f"   neutro {e}: réplica {base['r'] * N / (N - base['f']):.6%} · módulo PF.neutro {PF.neutro(base['r'], pal[e]['mobj'], base['tau'], base['f']):.6%}")
print("C55 del libro:", Lr["Historia!C55"], "· por año (módulo):", {y: round(v["roic_propio_pagado_el_alquiler"], 4) for y, v in pf["por_anio"].items()})
print("CIFRAS:", "CONFORMES con la réplica del dictamen" if ok else "DISTINTAS")

# --- (b) filas por valores con cada juego de palancas
L0 = M.leer_libro(libro)
JUEGOS = [("libro recalculado (1.ª pasada)", (2.5, 3.2, 3.5), (0.08, 0.09, 0.09)),
          ("S2C en A2 y ROIC = r", (3.9, 5.4, 5.9), (0.09, 0.09, 0.09)),
          ("S2C en A2 y tope sin foso", (3.9, 5.4, 5.9), (0.09, 0.12, 0.12)),
          ("vigente (vuelta C→B)", (3.9, 5.4, 5.9), (0.13, 0.15, 0.15)),
          ("NORMAL 4,0: justo bajo la media geométrica de las dos anclas (4,03)", (3.0, 4.0, 4.5), (0.09, 0.09, 0.09)),
          ("NORMAL 4,1: justo encima", (3.0, 4.1, 4.5), (0.09, 0.09, 0.09))]
for nombre, s2c, roic in JUEGOS:
    L = dict(L0)
    for c, s, ro in zip("BCD", s2c, roic):
        L[f"Palancas!{c}16"], L[f"Palancas!{c}18"] = s, ro
    r = M.evaluar(L, decl, carpeta=EXP)
    g = {x["id"]: x for x in r["guardas"]}
    vg, vk = g["V-F1g (valores)"], g["V-F1k (valores)"]
    pv = r["perimetro_f1_valores"]["palancas"]
    print(f"\n{nombre}: S2C {s2c} · ROIC {roic}")
    print(f"   V-F1g (valores): salta {vg['salta']} · {vg['severidad']} · " + "; ".join(f"{e} más cerca de {pv[e]['mas_cerca_de']}" for e in R.ESC))
    print(f"   V-F1k (valores): salta {vk['salta']} · {vk['severidad']} · exceso sobre el neutro: " + " / ".join(f"{100 * pv[e]['exceso_sobre_neutro']:+.2f}" for e in R.ESC)
          + " puntos · bloquean: " + (", ".join(sorted({x['id'] for x in r['guardas'] if x['salta'] and x['severidad'] == 'BLOQUEA'})) or "ninguna"))
