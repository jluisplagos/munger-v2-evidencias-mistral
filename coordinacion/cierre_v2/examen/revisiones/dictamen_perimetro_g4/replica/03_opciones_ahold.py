"""3 · Ahold: escalera y gramática (G4, G7, G8 como en comprobar_gramatica.py) con cada juego de palancas S2C / ROIC terminal.
Uso: 03_opciones_ahold.py CARPETA_EXPEDIENTE"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from motor import *

EXP = sys.argv[1]
L = leer(os.path.join(EXP, "recalc", "Ahold_v63_evaluada.xlsx"), RANGOS)
base, pal = base_del_libro(L), palancas_del_libro(L)
pj = json.load(open(os.path.join(EXP, "precio.json"), encoding="utf-8"))
p, precio, k = pj["p"], pj["precio"], pj["k"]
C55 = float(L["Historia!C55"]); C18 = L.get("Análisis!C18")
fb = json.load(open(os.path.join(EXP, "fase_b.json"), encoding="utf-8"))
v2 = {q: tuple(fb["palancas"][q][e]["valor"] for e in ESC) for q in ("s2c", "roic_lp")}
print(f"Base: f = {base['f']:.9f} · acciones {base['acciones']} · r {base['r']} · p {p} · k {k} · precio {precio} · C55 {C55:.4f} · C18 del libro {C18!r}")
print(f"fase_b.json vigente (vuelta C→B): S2C {v2['s2c']} · ROIC LP {v2['roic_lp']}")
ROIC_PROPIO = 0.148181   # media 2021–2025 de NOPAT NIIF 16 ÷ (capital invertido − arrendamientos): 02_perimetro_ahold.py
S2C_A2 = v2["s2c"]


def caso(nombre, s2c, roic, c18="No", c55_g7=None, umbral_g4=0.03, **kw):
    pl = {e: dict(pal[e], s2c=s2c[i], roic=roic[i]) for i, e in enumerate(ESC)}
    b = dict(base); b.update(kw)
    V = [motor(**b, **pl[e])["por_accion"] for e in ESC]
    esc = escalera(V, p, precio, k)
    g = gramatica(b, pl, C55, c18, umbral_g4=umbral_g4, c55_g7=c55_g7)
    sin = [x for x in g if x[3].startswith("SIN")]
    cod = 1 if sin else 0
    res = "; ".join(f"{i} {e}" + ("✗" if j.startswith("SIN") else "") for i, e, _, j in g) or "—"
    print(f"{nombre:<58} S2C {'/'.join(f'{x:g}' for x in s2c):<12} ROIC {'/'.join(f'{x:g}' for x in roic):<15} "
          f"V {V[0]:6.2f} {V[1]:6.2f} {V[2]:6.2f} · Sí {esc['precio_si']:6.2f} · pond {esc['ponderado']:6.2f} · {esc['zona']:<14} · gram. cód. {cod}: {res}")
    return V, esc, g


print("\n— Con las reglas del producto (G7 contra 2 × Historia!C55; G4 sin justificación posible si C18 ≠ Sí) —")
ref = caso("0 · libro recalculado (1.ª pasada de la fase B)", (2.5, 3.2, 3.5), (0.08, 0.09, 0.09))
caso("1 · fase_b.json vigente (vuelta C→B)", S2C_A2, v2["roic_lp"])
caso("2 · S2C en A2; ROIC LP como en la 1.ª pasada", S2C_A2, (0.08, 0.09, 0.09))
caso("3 · S2C en A2; ROIC LP = r (referencia mecánica)", S2C_A2, (0.09, 0.09, 0.09))
caso("4 · S2C en A2; ROIC LP en el tope sin foso (r + 3)", S2C_A2, (0.09, 0.12, 0.12))
caso("4b · ídem con MALO 0,12", S2C_A2, (0.12, 0.12, 0.12))
caso("4c · referencias B.2 con el ROIC histórico en A2 (BUENO 0,12)", S2C_A2, (0.09, 0.09, 0.12))
caso("5 · como 1, pero con C18 = Sí (G4 justificable)", S2C_A2, v2["roic_lp"], c18="Sí")
caso("6 · solo ROIC LP de la vuelta, S2C de la 1.ª pasada", (2.5, 3.2, 3.5), v2["roic_lp"])
caso("7 · lo que midió la fase C: S2C 3,9/5,4/5,7", (3.9, 5.4, 5.7), (0.08, 0.09, 0.09))
caso("7b · fase C: S2C 3,9/5,4/5,7 y ROIC 0,13/0,15/0,15", (3.9, 5.4, 5.7), (0.13, 0.15, 0.15))

print("\n— Con G7 medido en el perímetro del S2C (2 × ROIC propio 2021–2025 = 2 × 14,82 %) —")
caso("1' · fase_b.json vigente", S2C_A2, v2["roic_lp"], c55_g7=ROIC_PROPIO)
caso("3' · S2C en A2; ROIC LP = r", S2C_A2, (0.09, 0.09, 0.09), c55_g7=ROIC_PROPIO)
caso("4' · S2C en A2; ROIC LP 0,09/0,12/0,12", S2C_A2, (0.09, 0.12, 0.12), c55_g7=ROIC_PROPIO)

print("\n— Si la persona escalara la tolerancia de G4 por el apalancamiento del arrendamiento (r + 3 × capital total ÷ propio = r + 5,1) —")
caso("8 · umbral 0,141: 0,13/0,14/0,14 (sin foso)", S2C_A2, (0.13, 0.14, 0.14), c55_g7=ROIC_PROPIO, umbral_g4=0.03 * 1.688)
caso("8b · umbral 0,141: fase_b.json vigente", S2C_A2, v2["roic_lp"], c55_g7=ROIC_PROPIO, umbral_g4=0.03 * 1.688)

print("\n— Cuánto vale cada pieza (precio de Sí frente al libro) —")
for nombre, s2c, roic in (("solo S2C a A2", S2C_A2, (0.08, 0.09, 0.09)), ("S2C a A2 y MALO de 0,08 a 0,09", S2C_A2, (0.09, 0.09, 0.09)),
                          ("S2C a A2 y ROIC 0,09/0,12/0,12", S2C_A2, (0.09, 0.12, 0.12)), ("S2C a A2 y ROIC 0,13/0,15/0,15", S2C_A2, v2["roic_lp"])):
    pl = {e: dict(pal[e], s2c=s2c[i], roic=roic[i]) for i, e in enumerate(ESC)}
    V = [motor(**base, **pl[e])["por_accion"] for e in ESC]
    esc = escalera(V, p, precio, k)
    print(f"   {nombre:<34} precio de Sí {esc['precio_si']:.2f} ({esc['precio_si'] - ref[1]['precio_si']:+.2f} €; {esc['precio_si'] / ref[1]['precio_si'] - 1:+.1%}) · ponderado {esc['ponderado']:.2f} ({esc['ponderado'] - ref[1]['ponderado']:+.2f}) · {esc['zona']}")

print("\n— Sensibilidad que NO resuelve este dictamen: la f (conciliación propia del modelo A; K3 «+381») —")
S = 90147.3333333
for nombre, extra in (("f del libro (0,00014)", 0.0), ("sin la devolución fiscal belga de 2023 (367/3 al año)", 367 / 3), ("f solo con 2025 (0,00235)", None)):
    f = base["f"] + extra / S if extra is not None else (3542 * (1 - 0.2242) - 85 - (2150 + 130 + 138 + 28)) / 92352
    for etiqueta, s2c, roic in (("palancas de la opción 3", S2C_A2, (0.09, 0.09, 0.09)), ("palancas de la vuelta C→B", S2C_A2, v2["roic_lp"])):
        pl = {e: dict(pal[e], s2c=s2c[i], roic=roic[i]) for i, e in enumerate(ESC)}
        V = [motor(**dict(base, f=f), **pl[e])["por_accion"] for e in ESC]
        esc = escalera(V, p, precio, k)
        print(f"   {nombre:<52} f = {f:.5f} · {etiqueta:<26} Sí {esc['precio_si']:.2f} · pond {esc['ponderado']:.2f} · {esc['zona']}")
