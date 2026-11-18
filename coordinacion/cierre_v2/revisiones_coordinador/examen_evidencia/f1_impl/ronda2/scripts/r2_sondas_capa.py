#!/usr/bin/env python3
"""Segunda ronda · sondas del revisor sobre motor_a_f1.py @ 340d78c (sin LibreOffice). Uso: r2_sondas_capa.py RUTA_personaje_v2
Reutiliza los constructores de la batería del autor (libro, decl, estacionario…): se ejecuta solo la cabecera de test_motor_a_f1.py."""
import copy, json, os, shutil, sys, tempfile
sys.dont_write_bytecode = True
PV = os.path.abspath(sys.argv[1])
src = open(os.path.join(PV, "pruebas", "test_motor_a_f1.py"), encoding="utf-8").read().split("# ================================================================== SIN")[0]
src = src.replace("AQUI = os.path.dirname(os.path.abspath(__file__))", f"AQUI = {os.path.join(PV, 'pruebas')!r}")
exec(src)
import cierre_v2 as CIE

def bl(r): return sorted({x["id"] for x in r["guardas"] if x["salta"] and x["severidad"] == "BLOQUEA"})
def av(r): return sorted({x["id"] for x in r["guardas"] if x["salta"] and x["severidad"] == "AVISO"})
def t(x): print("\n=== " + x)

# ------------------------------------------------------------------ L1–L3: las sondas de la primera ronda, repetidas
t("L1 · (S1) NIIF 16 con el principal fuera del FCF base y perímetro A1/A2")
for c49 in (0.0, None):
    L = libro([1000.0] * 10, [70.0] * 10, [30.0] * 10, [0.0] * 10, [20.0] * 10, [0.0] * 10, [0.0] * 10, [10.0] * 10, 78.0, 0.0 if c49 is None else c49)
    if c49 is None: L["Análisis!C49"] = None
    for per in ("A0_total", "A1_sin_ROU", "A2_propio"):
        r = M.evaluar(L, decl(per, rou=todos(10), ppa=todos(0)))
        print(f"  C49={c49!r:5} · {per:11}: bloquean {bl(r)} · K3b «{r['K3']['K3b_alquiler_contado']}»")
t("L2 · (S2) A0 con ROU declarada a cero, C49 vacío y filas 17/23 con arrendamientos")
L = libro([1000.0] * 10, [70.0] * 10, [30.0] * 10, [0.0] * 10, [20.0] * 10, [0.0] * 10, [0.0] * 10, [10.0] * 10, 78.0, 0.0); L["Análisis!C49"] = None
for c in COLS: L[f"Historia!{c}23"] = 50.0
r = M.evaluar(L, decl("A0_total", rou=todos(0), ppa=todos(0)))
print("  utilizable:", r["utilizable_para_conclusion"], "· bloquean", bl(r))
t("L3 · (S14) A0 sin arrendamientos con términos explícitos")
L7_, _ = estacionario(0, 0, C49=0)
d = decl("A0_total", rou=todos(0), ppa=todos(0), trans=True)
d["transicion"].update({"tratamiento": "termino_explicito", "importes": {str(k): 7 for k in range(1, 6)}, "horizonte": 5, "naturaleza": "temporal",
                        "finalidad_documentada": "plan", "ancla_s2c_excluye_terminos": True})
r = M.evaluar(L7_, d); print("  transición término: utilizable", r["utilizable_para_conclusion"], "· bloquean", bl(r))
d = decl("A0_total", rou=todos(0), ppa=todos(0), compras="reposicion_con_importe"); d["clasificacion_compras"].update({"proporcion_ventas": 0.009, "ancla_s2c_excluye_terminos": True})
La = dict(L7_); La["Historia!L13"] = 9.0
r = M.evaluar(La, d); print("  compras término:    utilizable", r["utilizable_para_conclusion"], "· bloquean", bl(r))

# ------------------------------------------------------------------ L4: A3 con C49 = 0, arrendamientos en la Historia y ROU sin declarar
t("L4 · A3_estimado (R = D&A propia 20), C49 = 0, principal (fila 17) 10 y pasivo (fila 23) 50 en la Historia, D&A ROU SIN declarar")
L = libro([1000.0] * 10, [70.0] * 10, [30.0] * 10, [0.0] * 10, [20.0] * 10, [0.0] * 10, [0.0] * 10, [10.0] * 10, 78.0, 0.0)
for c in COLS: L[f"Historia!{c}23"] = 50.0
d = decl("A3_estimado")   # sin series
d["reinversion_estimada"] = {"por_anio": {str(y): {"R_propia": 20, "R_compras": 0, "transicion": 0} for y in ANIOS[-5:]}, "fuente": "f", "metodo": "m", "rango": "±2",
                             "responsable": "r", "reposicion_clientes": "en R_propia", "transicion": "sin transición", "incluye_gasto_comercial": False}
r = M.evaluar(L, d)
print("  flujo sin crecimiento A3:", r["calculo_perimetro_declarado"]["flujo_sin_crecimiento"], "(caja verdadera 68) · bloquean", bl(r), "· K3b «%s»" % r["K3"]["K3b_alquiler_contado"])

# ------------------------------------------------------------------ L5: K3a con casos legítimos
t("L5 · K3a con casos legítimos de la plantilla V6.3")
base, _ = estacionario(0, 0, C49=0)      # sin arrendamientos, A0 admisible
def k3a(L, **kw):
    r = M.evaluar(L, decl("A0_total", rou=todos(0), ppa=todos(0), **kw))
    gk = [x for x in r["guardas"] if x["id"] == "F1-K3a"][0]
    return r["utilizable_para_conclusion"], gk["salta"], gk["detalle"][:170]
print("  (a) base coherente:", k3a(base))
Lx = copy.deepcopy(base); Lx["Análisis!C48"] = None
print("  (b) C48 VACÍO (intereses dentro del CFO; la plantilla dice «déjalo vacío»):", k3a(Lx))
Lx = copy.deepcopy(base)
for c in COLS: Lx[f"Historia!{c}16"] = None
print("  (c) fila 16 vacía (sin intereses en financiación):", k3a(Lx))
Lx = copy.deepcopy(base); Lx["Análisis!C51"] = "No"
for c in COLS:
    Lx[f"Historia!{c}18"] = 4.0; Lx[f"Historia!{c}35"] = Lx[f"Historia!{c}35"] - 4.0
Lx["Análisis!C50"] = 4.0
print("  (d) SBC 4 que el expediente decide NO restar (C51 = No):", k3a(Lx))
print("      … con la partida declarada:", k3a(Lx, conc=[{"componente": "C50", "importe": 4.0, "partida": "SBC no restada (C51 = No)", "fuente": "Análisis C51"}]))

# ------------------------------------------------------------------ L6: K3a se satisface con cualquier partida declarada igual al residuo
t("L6 · K3a: alquiler restado dos veces en el FCF base (C49 = 12 con el interés; fila 17 = 10; C48 = 2) y una partida declarada que iguala el residuo")
L56b = libro([1000.0] * 10, [70.0] * 10, [30.0] * 10, [0.0] * 10, [20.0] * 10, [0.0] * 10, [0.0] * 10, [10.0] * 10, 56.0, 12.0, c48=2.0)
conc = [{"componente": "C48", "importe": -2, "partida": "interés de arrendamientos en C48", "fuente": "x"}]
r = M.evaluar(L56b, decl("A1_sin_ROU", rou=todos(10), ppa=todos(0), conc=conc)); print("  sin declarar el −2 de C49: F1-K3a salta", salta(r, "F1-K3a"))
conc2 = conc + [{"componente": "C49", "importe": -2, "partida": "cualquier texto", "fuente": "cualquier fuente"}]
r = M.evaluar(L56b, decl("A1_sin_ROU", rou=todos(10), ppa=todos(0), conc=conc2)); print("  declarando {C49: −2, «cualquier texto»}: F1-K3a salta", salta(r, "F1-K3a"), "· K3 conforme:", r["K3"]["conforme"], "· bloquean", bl(r))

# ------------------------------------------------------------------ L7: el mismo error en las dos vías
t("L7 · el interés de arrendamientos restado dos veces de forma COHERENTE (C48 = 2 y fila 16 = 2; C49 = 12 y fila 17 = 12): FCF base 66 frente a 68")
L = libro([1000.0] * 10, [70.0] * 10, [30.0] * 10, [0.0] * 10, [20.0] * 10, [0.0] * 10, [0.0] * 10, [12.0] * 10, 66.0, 12.0, c48=2.0, int16=2.0)
r = M.evaluar(L, decl("A1_sin_ROU", rou=todos(10), ppa=todos(0)))
print("  F1-K3a salta:", salta(r, "F1-K3a"), "· K3b «%s»" % r["K3"]["K3b_alquiler_contado"], "· K3c salta:", salta(r, "F1-K3c"), "· bloquean", bl(r), "· flujo A1", F0(r, "A1_sin_ROU"))

# ------------------------------------------------------------------ L8: K3c con un caso legítimo (circulante negativo que crece con las ventas)
t("L8 · K3c: distribuidor que crece un 5 % con capex = D&A propia y circulante que APORTA caja (−0,6 % de las ventas): sin arrendamientos ni PPA, A0")
V = [1000 * 1.05 ** i for i in range(10)]
dao = [0.02 * v for v in V]; dwc = [-0.006 * v for v in V]; ebit = [0.05 * v for v in V]
C70 = sum(ebit[i] * 0.75 + dao[i] - dao[i] - dwc[i] for i in range(7, 10)) / 3
L = libro(V, ebit, dao, [0.25] * 10, dao, [0.0] * 10, dwc, [0.0] * 10, C70, 0.0)
r = M.evaluar(L, decl("A0_total", rou=todos(0), ppa=todos(0)))
gk = [x for x in r["guardas"] if x["id"] == "F1-K3c"][0]
print("  utilizable:", r["utilizable_para_conclusion"], "· F1-K3c:", gk["severidad"], "·", gk["detalle"][:150])
r = M.evaluar(L, decl("A0_total", rou=todos(0), ppa=todos(0), justificacion_reinversion_negativa="x"))
print("  con justificacion_reinversion_negativa = «x» (sin registro): utilizable:", r["utilizable_para_conclusion"], "· avisos", av(r))

# ------------------------------------------------------------------ L9: exenciones y vigencia
t("L9 · exenciones: ¿puede quedar exento un expediente nuevo?")
tmp = tempfile.mkdtemp(prefix="r2_ex_")
try:
    Larr = libro([1000.0] * 10, [70.0] * 10, [30.0] * 10, [0.0] * 10, [20.0] * 10, [0.0] * 10, [0.0] * 10, [10.0] * 10, 68.0, 10.0)
    c = os.path.join(tmp, "Nueva"); os.makedirs(c)
    print("  (a) carpeta nueva con arrendamientos en el libro, sin archivos: exigido =", M.exigido(c, L=Larr), "· exención:", M.exencion(c))
    json.dump({"empresa": "Empresa real S.A. (inventada)"}, open(os.path.join(c, "fase1_v63.json"), "w"))
    print("  (b) fase1_v63.json con «(inventada)» en el nombre: exigido =", M.exigido(c, L=Larr), "· exención:", M.exencion(c))
    os.remove(os.path.join(c, "fase1_v63.json"))
    ex = os.path.join(PV, "empresas_v2_correcciones", "2026-11_Vidrala_ensayo_4_14", "elis_decisiones", "Elis", "cierre_vigente.json")
    shutil.copy(ex, os.path.join(c, "cierre_vigente.json"))
    print("  (c) cierre_vigente.json de OTRO expediente (Elis, registrado) copiado a la carpeta: exigido =", M.exigido(c, L=Larr), "· exención:", str(M.exencion(c))[:90])
    json.dump({"modo": "estricta"}, open(os.path.join(c, "entrada_efectiva.json"), "w"))
    print("  (d) lo mismo con entrada_efectiva.json (expediente de la 4.15): exigido =", M.exigido(c, L=Larr))
finally:
    shutil.rmtree(tmp, ignore_errors=True)

t("L10 · vigencia y cierre cuando el estado del pipeline no dice el motor (p. ej. tras --reiniciar) y no hay evaluación F1")
tmp = tempfile.mkdtemp(prefix="r2_vig_")
try:
    import openpyxl
    c = os.path.join(tmp, "EmpresaR"); os.makedirs(os.path.join(c, "recalc"))
    wb = openpyxl.Workbook()
    for h in ("Historia", "Análisis", "Palancas", "Motor", "Diagnóstico V6", "Control maestro"): wb.create_sheet(h)
    for k, v in Larr.items():
        if "!" in k and v is not None:
            h, cc = k.split("!"); wb[h][cc] = v
    wb.save(os.path.join(c, "EmpresaR_v63_evaluada.xlsx"))
    json.dump({"celdas": {"C62": "Sí"}}, open(os.path.join(c, "fase_a.json"), "w"))
    for st in ({"motor": "A", "estado_pendiente": None, "estado_analisis_fase_c": "concluido"}, {"motor": None, "paso": 13}, {}):
        json.dump(st, open(os.path.join(c, "estado_pipeline.json"), "w"))
        v = M.vigencia(c, motor=st.get("motor"))
        print(f"  estado {st}: vigencia exigido={v['exigido']} motivo={v['motivo']!r} · motivo_f1 = {str(CIE.motivo_f1(c, st))[:80]!r}")
finally:
    shutil.rmtree(tmp, ignore_errors=True)
