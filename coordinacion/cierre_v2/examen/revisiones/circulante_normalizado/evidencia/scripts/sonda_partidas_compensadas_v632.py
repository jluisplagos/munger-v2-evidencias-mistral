"""Sonda del revisor (2): las dos partidas C46 que se compensan con un libro V6.3.2 F1 sintético (recalculado por el oráculo de la prueba, que es
independiente de motor_a_f1) cuya caja base SÍ cuenta el circulante. Usa los datos y ayudas de test_circulante_f1.py; no usa LibreOffice."""
import contextlib, io, os, sys
PV = sys.argv[1]
os.chdir(PV)
ruta = os.path.join(PV, "pruebas", "test_circulante_f1.py")
g = {"__name__": "sonda", "__file__": ruta}
with contextlib.redirect_stdout(io.StringIO()):
    try:
        exec(compile(open(ruta, encoding="utf-8").read(), ruta, "exec"), g)
    except SystemExit:
        pass
# la prueba borra su carpeta de fuentes al terminar: se recrea igual (mismo archivo y contenido) para evaluar aquí
os.makedirs(g["CARPETA"], exist_ok=True)
open(os.path.join(g["CARPETA"], g["FUENTE_TXT"]), "w", encoding="utf-8").write(g["FUENTE"])
ev, bloquean, decl, NORM, conc_sin, libro_vinci = g["ev"], g["bloquean"], g["decl"], g["NORM"], g["conc_sin"], g["libro_vinci"]
c46_con, c52_con, r_v = g["c46_con"], g["c52_con"], g["r_v"]
def resumen(r, et):
    k3 = {x["id"]: (x["salta"], x["severidad"], (x["detalle"] or "")[:110]) for x in r["guardas"] if x["id"] in ("F1-CIRC", "F1-K3a", "F1-K3c", "F1-LIBRO")}
    cd = r.get("calculo_perimetro_declarado") or {}
    print(f"{et}: bloquean {bloquean(r)} · utilizable {r.get('utilizable_para_conclusion')} · f {cd.get('f')} · reinversión {cd.get('reinversion_media')} · F0 {cd.get('flujo_sin_crecimiento')}")
    for k, v in k3.items(): print(f"    {k}: salta {v[0]} · {v[1]} · {v[2]}")
r_v = ev(g["libro_vinci"](v632=True, regla="circulante_a_cero", anios_norm=NORM["anios"]), decl(NORM))
resumen(r_v, "referencia: Vinci genuino, libro V6.3.2 con la normalización (caja base SIN circulante, partida C46 −2.090 real)")
L632_con = libro_vinci(v632=True, regla="circulante_a_cero", anios_norm=NORM["anios"],
                       **{"Análisis!C46": c46_con, "Análisis!C52": c52_con, "Historia!C70": c52_con})
resumen(ev(L632_con, decl(NORM, conc=conc_sin)), "libro V6.3.2, caja base CON circulante + normalización (sin partida C46)")
falsas = [{"componente": "C46", "importe": -2090.0, "partida": "circulante excluido de C46 (falso)", "fuente": {"documento": "x", "pagina": 1}},
          {"componente": "C46", "importe": 2090.0, "partida": "compensación (falsa)", "fuente": {"documento": "x", "pagina": 1}}]
resumen(ev(L632_con, decl(NORM, conc=conc_sin + falsas)), "libro V6.3.2, caja base CON circulante + normalización + dos partidas C46 que se compensan")
r_x = ev(L632_con, decl(NORM, conc=conc_sin + falsas))
print("detalle de las guardas que saltan con las partidas falsas de fuente «x»:")
for x in r_x["guardas"]:
    if x["salta"]: print("   ", x["id"], x["severidad"], (x["detalle"] or "")[:300])
falsas_p = [dict(e, fuente={"documento": "prueba", "pagina": 1}) for e in falsas]
resumen(ev(L632_con, decl(NORM, conc=conc_sin + falsas_p)), "libro V6.3.2, caja base CON circulante + normalización + dos partidas C46 que se compensan (fuente «prueba», la misma que la partida de redondeo de la prueba del autor)")
r_p = ev(L632_con, decl(NORM, conc=conc_sin + falsas_p))
for x in r_p["guardas"]:
    if x["salta"]: print("   ", x["id"], x["severidad"], (x["detalle"] or "")[:300])
