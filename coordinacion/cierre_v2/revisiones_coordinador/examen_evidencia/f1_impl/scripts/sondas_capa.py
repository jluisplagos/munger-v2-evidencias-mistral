#!/usr/bin/env python3
"""Sondas del revisor sobre motor_a_f1.py (sin LibreOffice). Uso: sondas_capa.py RUTA_personaje_v2"""
import copy, json, os, sys
from fractions import Fraction as Fr
PV = sys.argv[1]
sys.path.insert(0, os.path.join(PV, "scripts"))
sys.dont_write_bytecode = True
import motor_a_f1 as M

COLS = "CDEFGHIJKL"; ANIOS = list(range(2016, 2026))
REG = {"fecha": "2026-11-17", "persona": "sonda del revisor", "motivo": "sonda"}

def libro(ventas, ebit, da, tau, capex, adq, dwc, princ, C70, C49, n=3, pal=None, l4="IFRS (adoptadas por la Unión Europea)", c179=0.05, pasivo=None, anios=ANIOS, motor="A"):
    L = {"sha256": "sintetico", "Diagnóstico V6!C5": motor, "Control maestro!L4": l4, "Diagnóstico V6!C179": c179}
    for i, (c, y) in enumerate(zip(COLS, anios)):
        for fila, serie in ((5, anios), (6, ventas), (7, ebit), (8, da), (10, tau), (12, capex), (13, adq), (14, dwc), (17, princ)):
            if serie[i] is not None:
                L[f"Historia!{c}{fila}"] = serie[i]
        if pasivo is not None:
            L[f"Historia!{c}23"] = pasivo[i]
    w = range(10 - n, 10)
    S = sum(ventas[i] for i in w) / n
    nop = sum(ebit[i] * (1 - tau[i]) for i in w) / n
    rei = sum(capex[i] - da[i] + dwc[i] for i in w) / n
    L["Historia!C58"] = ((nop - rei) - C70) / S
    L["Historia!C57"] = n; L["Historia!C70"] = C70; L["Historia!C44"] = ventas[-1]; L["Historia!C48"] = ebit[-1] / ventas[-1]
    L["Historia!C52"] = sum(tau[5:]) / 5
    den = sum(capex[i] - da[i] + dwc[i] + adq[i] for i in range(5, 10))
    L["Historia!C53"] = (ventas[-1] - ventas[4]) / den if den > 0 else ""
    L["Análisis!C48"], L["Análisis!C52"] = 0, C70
    if C49 is not None:
        L["Análisis!C49"] = C49
    pal = pal or {"B": (0.02, 0.10, 1.0, 0.01, 0.08), "C": (0.03, 0.10, 1.2, 0.02, 0.10), "D": (0.04, 0.11, 1.5, 0.025, 0.12)}
    for c, (g15, mo, s2c, gi, roic) in pal.items():
        L[f"Palancas!{c}14"], L[f"Palancas!{c}15"], L[f"Palancas!{c}16"], L[f"Palancas!{c}18"], L[f"Análisis!{c}68"] = g15, mo, s2c, roic, gi
    for c, s in zip("BCD", (0.0047, 0.0068, 0.0241)):
        L[f"Diagnóstico V6!{c}178"] = s; L[f"Diagnóstico V6!{c}176"] = s + 0.1; L[f"Diagnóstico V6!{c}177"] = 0.1
    return L

def serie(vals, signo=-1, trat="publicado entre paréntesis"):
    return {str(y): {"valor_fuente": -v if signo == -1 else v, "signo": signo, "tratamiento": trat if signo == -1 else "ninguno", "documento": "sintético", "pagina": 1} for y, v in vals.items()}

def decl(per="A0_total", rou=None, ppa=None, norma="NIIF", margen="EBIT_NIIF16_PPA_constante", pal=None, roic=None, compras="sin_compras", trans=False, **extra):
    d = {"norma_contable": {"valor": norma, "registro": REG}, "perimetro_reinversion": {"valor": per, "registro": REG},
         "perimetro_margen": {"valor": margen, "registro": REG}, "perimetro_palancas_s2c": {"valor": pal or per, "registro": REG},
         "perimetro_roic": {"valor": roic or pal or per, "registro": REG}, "clasificacion_compras": {"valor": compras, "registro": REG},
         "transicion": {"conocida": trans, "tratamiento": None, "registro": REG}, "series": {}}
    if rou is not None: d["series"]["da_rou"] = serie(rou)
    if ppa is not None: d["series"]["da_ppa"] = serie(ppa)
    d.update(extra); return d

def todos(v): return {y: v for y in ANIOS}
def bloq(r): return sorted({g["id"] for g in r["guardas"] if g["salta"] and g["severidad"] == "BLOQUEA"})
def F0(r, p): return r["diagnostico_por_perimetro"][p]["flujo_sin_crecimiento"]
def titulo(t): print("\n=== " + t)

# ---------------------------------------------------------------- S1: omisión del alquiler con A1/A2 cuando C49 = 0 (o vacío)
titulo("S1 · NIIF 16 con los pagos de principal FUERA del FCF base (C49 = 0 o vacío) y perímetro A1/A2: ¿bloquea algo?")
# EBITDA 100; capex propio = D&A propia 20; ROU 10; pagos 12 (10 principal + 2 interés). FCF verdadero 68.
# El FCF base del libro NO resta el principal (C49 vacío): C70 = 100 − 20 − 2 = 78.
for c49 in (0.0, None):
    L = libro([1000.0] * 10, [70.0] * 10, [30.0] * 10, [0.0] * 10, [20.0] * 10, [0.0] * 10, [0.0] * 10, [10.0] * 10, 78.0, c49, pasivo=[50.0] * 10)
    for per in ("A0_total", "A1_sin_ROU", "A2_propio"):
        r = M.evaluar(L, decl(per, rou=todos(10), ppa=todos(0)))
        print(f"  C49={c49!r:5} · declarado {per:11}: F0 A0 {F0(r,'A0_total'):.1f} · A1 {F0(r,'A1_sin_ROU'):.1f} (verdadero 68) · bloquean {bloq(r)}")

# ---------------------------------------------------------------- S2: A0 admitido con C49 vacío y ROU declarada 0 aunque las filas 17 y 23 del libro muestran arrendamientos
titulo("S2 · A0 con ROU declarada a cero y C49 vacío, mientras Historia filas 17 (principal) y 23 (pasivo) dicen que hay arrendamientos")
L = libro([1000.0] * 10, [70.0] * 10, [30.0] * 10, [0.0] * 10, [20.0] * 10, [0.0] * 10, [0.0] * 10, [10.0] * 10, 78.0, None, pasivo=[50.0] * 10)
r = M.evaluar(L, decl("A0_total", rou=todos(0), ppa=todos(0)))
print("  utilizable_para_conclusion:", r["utilizable_para_conclusion"], "· bloquean", bloq(r), "· rótulo:", r["rotulo"][:90])

# ---------------------------------------------------------------- S3: menos de 10 años de historia
titulo("S3 · empresa con 8 años de historia (C5:D5 vacías; la V6.3 lo admite con ≥ 5 años)")
an8 = [None, None] + list(range(2018, 2026))
L = libro([1000.0] * 10, [65.0] * 10, [35.0] * 10, [0.0] * 10, [20.0] * 10, [0.0] * 10, [0.0] * 10, [10.0] * 10, 68.0, 10.0, anios=an8)
try:
    r = M.evaluar(L, decl("A2_propio", rou={y: 10 for y in range(2018, 2026)}, ppa={y: 5 for y in range(2018, 2026)}))
    print("  evaluó:", bloq(r))
except M.ErrorDeclaracion as ex:
    print("  ErrorDeclaracion →", ex, "(el CLI devuelve 2 y el pipeline lo convierte en no_entregable · fallo_de_implementacion)")

# ---------------------------------------------------------------- S4: N1 · alcance elegido por omisión y partida cualquiera
titulo("S4 · N1: ¿se puede elegir «solo la ventana» por omisión y normalizar una partida que no es un earnout?")
L6 = libro([1000.0] * 10, [65.0] * 10, [35.0] * 10, [0.0] * 10, [20.0] * 10, [0.0] * 10, [0.0] * 10, [10.0] * 10, 68.0, 10.0)
n1 = {"ajustes": [{"regla": "N1", "anio": 2025, "partida": "gastos de reestructuración (NO es un earnout)", "importe": -5, "fuente": {"documento": "s", "pagina": 1},
                   "regla_fiscal": "no_deducible", "ubicacion_caja": "en el FCF base"}],
      "bai": {"2025": {"valor": 50, "documento": "s"}}, "gasto_impuesto": {"2025": {"valor": 0, "documento": "s"}},
      "margen_objetivo_sin_ajustes": True, "actualizacion_financiera_earnout_declarada": False}
r = M.evaluar(L6, decl("A2_propio", rou=todos(10), ppa=todos(5), normalizacion=n1))
print("  V-F1l salta:", any(g["id"] == "V-F1l" and g["salta"] for g in r["guardas"]), "· F1-PARAM salta:", any(g["id"] == "F1-PARAM" and g["salta"] for g in r["guardas"]),
      "· F1-REGISTRO salta:", any(g["id"] == "F1-REGISTRO" and g["salta"] for g in r["guardas"]), "· bloquean", bloq(r))
print("  (sin registro de la normalización; partida de reestructuración con su caja EN el FCF base; nada lo señala salvo F1-LIBRO)")

# ---------------------------------------------------------------- S5: compras de reposición con importes por año: año 11 y años sin importe
titulo("S5 · compras de reposición «con importes por año» (sin proporción): ¿qué cobra el año 11 y los años sin importe?")
d = decl("A2_propio", rou=todos(10), ppa=todos(5), compras="reposicion_con_importe")
d["clasificacion_compras"].update({"importes": {"1": 9, "2": 9, "3": "nueve"}, "ancla_s2c_excluye_terminos": True})
r = M.evaluar(L6, d)
base = M.evaluar(L6, decl("A2_propio", rou=todos(10), ppa=todos(5)))
a = r["calculo_perimetro_declarado"]["escenarios"]["NORMAL"]; b = base["calculo_perimetro_declarado"]["escenarios"]["NORMAL"]
print("  V-F1j salta:", any(g["id"] == "V-F1j" and g["salta"] for g in r["guardas"]), "· cargo por año 1–10:", [round(y - x, 3) for x, y in zip(a["anios_1_10"], b["anios_1_10"])],
      "· cargo año 11:", round(b["anio_11"] - a["anio_11"], 3))
print("  ancla E4 con compras-término:", r["calculo_perimetro_declarado"]["ancla_s2c_E4"], "· sin ellas:", base["calculo_perimetro_declarado"]["ancla_s2c_E4"])

# ---------------------------------------------------------------- S6: transición término explícito: el ancla «excluye» solo de palabra
titulo("S6 · transición como término explícito con «ancla_s2c_excluye_terminos: true» y sin importes históricos: ¿cambia el ancla calculada?")
V = [1000 * 1.05 ** i for i in range(10)]
dao = [0.02 * v for v in V]; capex = [dao[i] + 0.5 * (V[i] - (V[i - 1] if i else V[0] / 1.05)) + 7 for i in range(10)]   # 7 de transición dentro del capex
ebit = [0.10 * v for v in V]
C70 = sum(ebit[i] * 0.75 + dao[i] - capex[i] for i in range(7, 10)) / 3
Lt = libro(V, ebit, dao, [0.25] * 10, capex, [0.0] * 10, [0.0] * 10, [0.0] * 10, C70, 0.0)
dt_ = decl("A2_propio", rou=todos(0), ppa=todos(0), trans=True)
dt_["transicion"].update({"tratamiento": "termino_explicito", "importes": {str(t): 7 for t in range(1, 6)}, "horizonte": 5, "naturaleza": "temporal",
                          "finalidad_documentada": "plan sintético", "ancla_s2c_excluye_terminos": True})
r1 = M.evaluar(Lt, dt_)
r0 = M.evaluar(Lt, decl("A2_propio", rou=todos(0), ppa=todos(0)))
print("  V-F1i salta:", any(g["id"] == "V-F1i" and g["salta"] for g in r1["guardas"]), "· ancla con término declarado fuera del ancla:", round(r1["calculo_perimetro_declarado"]["ancla_s2c_E4"], 6),
      "· ancla sin transición declarada:", round(r0["calculo_perimetro_declarado"]["ancla_s2c_E4"], 6), "· ancla correcta sin los 7 de transición: 2.0")

# ---------------------------------------------------------------- S7: registro: «no hay transición conocida» y normalización sin registro
titulo("S7 · «transicion.conocida: false» sin registro (fecha, persona, motivo)")
d = decl("A0_total", rou=todos(0), ppa=todos(0))
L7 = libro([1000.0] * 10, [80.0] * 10, [20.0] * 10, [0.0] * 10, [20.0] * 10, [0.0] * 10, [0.0] * 10, [0.0] * 10, 80.0, 0.0)
d["transicion"] = {"conocida": False}
r = M.evaluar(L7, d)
print("  utilizable:", r["utilizable_para_conclusion"], "· bloquean", bloq(r))

# ---------------------------------------------------------------- S8: norma: L4 con texto mixto
titulo("S8 · F1-NORMA: declaración «NIIF» frente a textos de Control maestro L4")
for l4 in ("US GAAP", "US GAAP (no IFRS)", "PCGA de EE. UU.; concilia con IFRS en la nota 3", "Swiss GAAP FER", "NIIF-UE"):
    Lx = copy.deepcopy(L7); Lx["Control maestro!L4"] = l4
    r = M.evaluar(Lx, d)
    print(f"  L4={l4!r:50} → F1-NORMA bloquea: {any(g['id']=='F1-NORMA' and g['salta'] for g in r['guardas'])}")

# ---------------------------------------------------------------- S9: el libro no dice «A» (caché vacía) y el pipeline sí
titulo("S9 · Diagnóstico V6!C5 sin valor en caché (None) con un expediente de motor A")
Lx = copy.deepcopy(L6); del Lx["Diagnóstico V6!C5"]
r = M.evaluar(Lx, decl("A0_total", rou=todos(10), ppa=todos(5)))
print("  aplica:", r["aplica"], "· bloquea:", r["bloquea"], "· motivo:", r.get("motivo"), "→ el CLI devuelve 0 y el gancho del pipeline sigue")

# ---------------------------------------------------------------- S10: K3 es una identidad: cuadra con cualquier dato, también con un FCF base mal construido
titulo("S10 · K3 con datos arbitrarios y con un FCF base que resta el alquiler DOS veces")
import random
random.seed(7)
n_ok = 0
for k in range(500):
    Vv = [random.uniform(500, 5000) for _ in range(10)]; eb = [random.uniform(-200, 800) for _ in range(10)]; da = [random.uniform(50, 900) for _ in range(10)]
    ta = [round(random.uniform(0, 0.5), 4) for _ in range(10)]; cx = [random.uniform(0, 1500) for _ in range(10)]; dw = [random.uniform(-100, 100) for _ in range(10)]
    Lr = libro(Vv, eb, da, ta, cx, [0.0] * 10, dw, [0.0] * 10, random.uniform(-500, 2000), random.choice([0.0, 50.0]))
    rr = M.evaluar(Lr, decl("A0_total", rou={y: da[i] * 0.3 for i, y in enumerate(ANIOS)}, ppa={y: da[i] * 0.1 for i, y in enumerate(ANIOS)}))
    n_ok += all(v["K3"]["cuadra"] for v in rr["diagnostico_por_perimetro"].values())
print(f"  500 libros aleatorios (FCF base, EBIT, D&A, capex sin relación entre sí): K3 «cuadra» en los cuatro perímetros en {n_ok} de 500")
# caso económico: sin arrendamientos ni PPA declarados (ROU = 0, C49 = 0), pero el FCF base registrado resta 12 de alquiler que YA estaba en el EBIT (gasto de alquiler operativo)
Ld = libro([1000.0] * 10, [68.0] * 10, [20.0] * 10, [0.0] * 10, [20.0] * 10, [0.0] * 10, [0.0] * 10, [0.0] * 10, 68.0 - 12.0, 0.0)
rd = M.evaluar(Ld, decl("A0_total", rou=todos(0), ppa=todos(0)))
k3 = rd["calculo_perimetro_declarado"]["K3"]
print("  FCF verdadero 68; FCF base registrado 56 (alquiler restado dos veces): flujo sin crecimiento", k3["flujo_sin_crecimiento"], "· K3 cuadra:", k3["cuadra"],
      "· partidas sin explicar:", k3["partidas_sin_explicar"], "· utilizable:", rd["utilizable_para_conclusion"])

# ---------------------------------------------------------------- S11: exigencia
titulo("S11 · exigencia F1 con el modo declarado en alcance_v2.json (forma del hito 1) y sin declaración")
import tempfile, shutil
t = tempfile.mkdtemp()
try:
    json.dump({"entrada_efectiva": "estricta"}, open(os.path.join(t, "alcance_v2.json"), "w"))
    print("  alcance_v2.json {entrada_efectiva: estricta} (expediente 4.15, hito 1) → exigido:", M.exigido(t))
    json.dump({"entrada_efectiva": "estricta"}, open(os.path.join(t, "fase1_metadatos.json"), "w"))
    print("  + fase1_metadatos.json con el modo → exigido:", M.exigido(t))
    print("  carpeta nueva sin nada → exigido:", M.exigido(tempfile.mkdtemp()))
finally:
    shutil.rmtree(t, ignore_errors=True)

# ---------------------------------------------------------------- S12: T9 · magnitud positiva de una cifra publicada entre paréntesis
titulo("S12 · T9: «(149.5)» declarado como +149,5 con signo 1 y tratamiento «ninguno» (la magnitud positiva sin la declaración del signo)")
d = decl("A2_propio", rou=todos(10), ppa=todos(5))
d["series"]["da_rou"]["2025"] = {"valor_fuente": 10, "signo": 1, "tratamiento": "ninguno", "documento": "s", "pagina": 1}
r = M.evaluar(L6, d)
print("  V-F1e salta:", any(g["id"] == "V-F1e" and g["salta"] for g in r["guardas"]), "(la capa no lee la fuente: no puede saber cómo está publicada la cifra)")

# ---------------------------------------------------------------- S13: series con página inexistente / documento inventado
titulo("S13 · serie con documento y página inventados")
d = decl("A2_propio", rou=todos(10), ppa=todos(5))
for y in d["series"]["da_rou"]:
    d["series"]["da_rou"][y].update({"documento": "informe que no existe.pdf", "pagina": 99999})
r = M.evaluar(L6, d)
print("  V-F1e salta:", any(g["id"] == "V-F1e" and g["salta"] for g in r["guardas"]), "· bloquean", bloq(r))
