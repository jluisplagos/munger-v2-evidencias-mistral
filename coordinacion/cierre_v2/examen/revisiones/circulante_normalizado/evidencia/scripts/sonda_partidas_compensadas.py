"""Sonda del revisor: ¿puede la normalización del circulante silenciar K3c en una empresa cuya caja base SÍ cuenta el circulante, declarando dos
partidas C46 que se compensan (una igual a la media de la fila 14 y otra de signo contrario)? Usa los datos y ayudas de test_circulante_f1.py."""
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
L_con, conc_sin, decl, NORM, ev, bloquean, g_ = g["L_con"], g["conc_sin"], g["decl"], g["NORM"], g["ev"], g["bloquean"], g["g"]
def resumen(r, et):
    k3 = {x["id"]: (x["salta"], x["severidad"], (x["detalle"] or "")[:120]) for x in r["guardas"] if x["id"] in ("F1-CIRC", "F1-K3a", "F1-K3c")}
    cd = r.get("calculo_perimetro_declarado") or {}
    print(f"{et}: bloquean {bloquean(r)} · utilizable {r.get('utilizable_para_conclusion')} · f {cd.get('f')} · reinversión {cd.get('reinversion_media')}")
    for k, v in k3.items(): print(f"    {k}: salta {v[0]} · {v[1]} · {v[2]}")
resumen(ev(L_con, decl(NORM, conc=conc_sin)), "caja base CON circulante + normalización (prueba del autor)")
falsas = [{"componente": "C46", "importe": -2090.0, "partida": "circulante excluido de C46 (falso)", "fuente": {"documento": "x", "pagina": 1}},
          {"componente": "C46", "importe": 2090.0, "partida": "compensación (falsa)", "fuente": {"documento": "x", "pagina": 1}}]
resumen(ev(L_con, decl(NORM, conc=conc_sin + falsas)), "caja base CON circulante + normalización + dos partidas C46 que se compensan")
