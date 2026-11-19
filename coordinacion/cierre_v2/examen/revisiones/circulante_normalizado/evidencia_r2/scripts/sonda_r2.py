"""Sondas del revisor, ronda 2 (corrección C1). Usa los datos y ayudas de test_circulante_f1.py y su expediente sintético tipo VINCI; sin LibreOffice.
  S1 · la sonda de la ronda 1 (caja base que cuenta el circulante + dos partidas C46 que se compensan, documento «x»), con un libro V6.3.1 y con uno V6.3.2;
  S2 · la misma con el cálculo de C46 amañado para que cuadre con el libro: + un componente «casi circulante» con fuente verdadera
       (la variación de clientes y de provisiones corrientes de la nota de circulante, que suman la línea del estado de flujos menos 1 en 2023),
       el C46 del libro escrito igual que ese cálculo (11.417,000) y una partida C46 de «redondeo» para que K3a cuadre;
  S3 · control: VINCI genuino (caja base sin el circulante) con el expediente sintético: utilizable."""
import contextlib, copy, io, os, sys, tempfile
PV = sys.argv[1]
os.chdir(PV)
ruta = os.path.join(PV, "pruebas", "test_circulante_f1.py")
g = {"__name__": "sonda", "__file__": ruta}
with contextlib.redirect_stdout(io.StringIO()):
    try:
        exec(compile(open(ruta, encoding="utf-8").read(), ruta, "exec"), g)
    except SystemExit:
        pass
EXP, FIX, CONC, NORM = g["EXP"], g["FIX"], g["CONC"], g["NORM"]
ev, decl, bloquean, libro_vinci, L0 = g["ev"], g["decl"], g["bloquean"], g["libro_vinci"], g["L0"]
# la prueba borra al terminar su carpeta de fuentes: se recrea igual (el expediente sintético y la fuente de las series)
os.makedirs(g["CARPETA"], exist_ok=True)
EXP.escribir(g["CARPETA"], FIX["valores"])
open(os.path.join(g["CARPETA"], g["FUENTE_TXT"]), "w", encoding="utf-8").write(g["FUENTE"])
def resumen(r, et):
    cd = r.get("calculo_perimetro_declarado") or {}
    print(f"{et}\n    bloquean {bloquean(r)} · utilizable {r.get('utilizable_para_conclusion')} · f {cd.get('f')} · flujo sin crecimiento {cd.get('flujo_sin_crecimiento')}")
    for x in r["guardas"]:
        if x["id"] in ("F1-CIRC", "F1-K3a", "F1-K3c", "F1-LIBRO") and (x["salta"] or x["id"] == "F1-CIRC"):
            print(f"    {x['id']}: salta {x['salta']} · {x['severidad']} · {x.get('efecto')} · {(x['detalle'] or '')[:230]}")
COMPENSA = [{"componente": "C46", "importe": -2090.0, "partida": "circulante excluido (falso)", "fuente": {"documento": "x", "pagina": 1}},
            {"componente": "C46", "importe": 2090.0, "partida": "compensación (falsa)", "fuente": {"documento": "x", "pagina": 1}}]
sin_wc = [e for e in CONC if e["importe"] != -2090.0]
otras = L0["Análisis!C47"] + L0["Análisis!C48"] + L0["Análisis!C49"] + L0["Análisis!C50"]
cfo_m = sum(L0[f"Historia!{g['COL'][y]}11"] for y in (2023, 2024, 2025)) / 3
# S1
c46_con = round(cfo_m + 37.333333, 3); c52_con = round(c46_con - otras, 3)
conc_s1 = sin_wc + [{"componente": "C70", "importe": c52_con - (c46_con - otras), "partida": "redondeo", "fuente": {"documento": "prueba", "pagina": 1}}] + COMPENSA
for v632 in (False, True):
    kw = dict(v632=True, regla="circulante_a_cero", anios_norm=NORM["anios"]) if v632 else {}
    L = libro_vinci(**kw, **{"Análisis!C46": c46_con, "Análisis!C52": c52_con, "Historia!C70": c52_con})
    resumen(ev(L, decl(NORM, conc=conc_s1)), f"S1 · sonda de la ronda 1, libro {'V6.3.2' if v632 else 'V6.3.1'} (C46 = {c46_con})")
# S2: componentes «casi circulante» con fuente verdadera en una página nueva del texto conservado
c = tempfile.mkdtemp(prefix="sonda_r2_", dir=os.environ.get("TMPDIR"))
pag = len(EXP.PAGINAS) + 1
EXP.PAGINAS.append("Note 5 Working capital (detail)\nChange in trade receivables 1311 1000\nChange in current provisions 1000 462")
cli = {"2023": {"valor": 1000, "fuente": EXP.TEXTO, "pagina": pag, "cita": "Change in trade receivables 1311 1000"},
       "2024": {"valor": 1311, "fuente": EXP.TEXTO, "pagina": pag, "cita": "Change in trade receivables 1311 1000"},
       "2025": {"valor": 1496, "fuente": EXP.TEXTO, "pagina": 7, "cita": "Change in trade receivables 1496 1311"}}
pro = {"2023": {"valor": 462, "fuente": EXP.TEXTO, "pagina": pag, "cita": "Change in current provisions 1000 462"},
       "2024": {"valor": 1000, "fuente": EXP.TEXTO, "pagina": pag, "cita": "Change in current provisions 1000 462"},
       "2025": {"valor": 1000, "fuente": EXP.TEXTO, "pagina": 7, "cita": "Change in current provisions 1000 1000"}}
f1 = EXP.fase1(FIX["valores"])
cal = f1["analisis"]["C46"]["calculo"]
cal["terminos"] = cal["terminos"] + [{"componente": "variacion_clientes", "signo": 1}, {"componente": "variacion_provisiones", "signo": 1}]
cal["componentes"].update({"variacion_clientes": cli, "variacion_provisiones": pro})
from fractions import Fraction as Fr
val = Fr(round(cfo_m * 3)) / 3 - 2090 + Fr(112, 3) + Fr(1000 + 1311 + 1496, 3) + Fr(462 + 1000 + 1000, 3)
f1["analisis"]["C46"]["valor"] = round(float(val), 3)
EXP.escribir(c, None, f1=f1)
open(os.path.join(c, g["FUENTE_TXT"]), "w", encoding="utf-8").write(g["FUENTE"])   # la fuente de las series, como en la carpeta de la prueba
c46_s2 = round(float(val), 3); c52_s2 = round(c46_s2 - otras, 3)
conc_s2 = [dict(e, importe=round(37.333333 - (c46_con - c46_s2), 6)) if e["componente"] == "C46" else e for e in sin_wc] + COMPENSA
conc_s2 += [{"componente": "C70", "importe": c52_s2 - (c46_s2 - otras), "partida": "redondeo", "fuente": {"documento": "prueba", "pagina": 1}}]
L2 = libro_vinci(v632=True, regla="circulante_a_cero", anios_norm=NORM["anios"], **{"Análisis!C46": c46_s2, "Análisis!C52": c52_s2, "Historia!C70": c52_s2})
print(f"S2 · cálculo de C46 del expediente = {float(val):.3f} (cfo + fila 14 + dividendos + clientes + provisiones; clientes + provisiones de media "
      f"{(1000 + 1311 + 1496 + 462 + 1000 + 1000) / 3:.3f} frente a −media de la fila 14 = 2.090)")
resumen(ev(L2, decl(NORM, conc=conc_s2), carpeta=c), "S2 · caja base que cuenta el circulante salvo 0,333, libro V6.3.2, cálculo de C46 con fuentes verdaderas")
# S3: control
resumen(ev(libro_vinci(v632=True, regla="circulante_a_cero", anios_norm=NORM["anios"]), decl(NORM)), "S3 · control: VINCI genuino, libro V6.3.2")
r2 = ev(L2, decl(NORM, conc=conc_s2), carpeta=c)
print("S2 · texto completo de F1-CIRC:", [x["detalle"] for x in r2["guardas"] if x["id"] == "F1-CIRC"][0])
