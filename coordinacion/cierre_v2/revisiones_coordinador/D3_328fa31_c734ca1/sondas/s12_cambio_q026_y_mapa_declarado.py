"""Sondas del revisor (stubs; no ejecutan el producto) sobre c734ca1:

a) D3-R3 · validación del CAMBIO de Q1-026 contra el banco (ejecutar_caso.py:206-233): cada
   alteración de las cifras debe dar ERROR_ESPECIFICACION (exit 2) ANTES de llamar al producto.
b) D3-R5 · el MAPA cuenta «con aserción» lo que declara adaptaciones.json, sin comprobar que la
   aserción exista en la especificación, que haya resultado, ni que no sea no_discriminante.

Uso: python3 -I -B s12_cambio_q026_y_mapa_declarado.py <ejecucion_d @c734ca1> <banco_revisado> <salida.json>
"""
import copy, csv, json, os, shutil, subprocess, sys, tempfile

D, BANCO, OUT = [os.path.abspath(x) for x in sys.argv[1:4]]
PY = sys.executable
res = {"alcance": "stubs; no son resultados del producto", "objeto": "c734ca1"}


def git(c, *a):
    return subprocess.run(["git", "-C", c, *a], check=True, capture_output=True, text=True)


os.makedirs(os.environ.get("TMPDIR", tempfile.gettempdir()), exist_ok=True)
with tempfile.TemporaryDirectory() as tmp:
    cand = os.path.join(tmp, "cand")
    sc = os.path.join(cand, "munger_v2_r1", "personaje_v2", "scripts")
    os.makedirs(sc)
    open(os.path.join(sc, "verificacion_entradas.py"), "w").write("import sys\nsys.exit(0)\n")
    open(os.path.join(sc, "cambiar_base.py"), "w").write("import sys\nsys.stderr.write('PRODUCTO DE JUGUETE LLAMADO\\n'); sys.exit(1)\n")
    git(cand, "init", "-q"); git(cand, "add", "-A"); git(cand, "-c", "user.email=r@r", "-c", "user.name=r", "commit", "-qm", "stub")
    sha = git(cand, "rev-parse", "HEAD").stdout.strip()
    pl = os.path.join(tmp, "pl"); os.makedirs(pl); open(os.path.join(pl, "fase1_v63.json"), "w").write("{}")
    base = json.load(open(os.path.join(D, "scripts", "especificaciones", "bloque2", "Q1-026.json"), encoding="utf-8"))

    def variante(nombre, mut):
        s = copy.deepcopy(base); mut(s["pasos"][0]["cambio"])
        sp = os.path.join(tmp, nombre + ".json"); json.dump(s, open(sp, "w"), ensure_ascii=False)
        ev = os.path.join(tmp, "ev_" + nombre)
        r = subprocess.run([PY, "-I", "-B", os.path.join(D, "scripts", "ejecutar_caso.py"), sp], capture_output=True, text=True,
                           env=dict(os.environ, BANCO_DIR=BANCO, CANDIDATA_DIR=cand, SHA_CANDIDATA_ESPERADO=sha, PLANTILLA_EXP=pl,
                                    EVIDENCIAS_DIR=ev, RUN_DIR=os.path.join(tmp, "run_" + nombre)))
        rp = os.path.join(ev, "Q1-026", "resultado_ejecucion.json")
        rr = json.load(open(rp)) if os.path.isfile(rp) else {}
        llamado = os.path.isfile(os.path.join(ev, "Q1-026", "cambiar_base_preparar.txt"))
        return {"exit": r.returncode, "estado": rr.get("estado_caso"), "errores": [e[:150] for e in rr.get("errores", [])][:2],
                "producto_llamado": llamado}

    a = {}
    a["a0_control_CAMBIO_publicado"] = variante("a0", lambda c: None)
    a["a1_C24_valor_85"] = variante("a1", lambda c: c["analisis"]["C24"].__setitem__("valor", 85.0))
    a["a2_deuda_neta_resultado_215"] = variante("a2", lambda c: c["derivados_esperados"]["deuda_neta"].__setitem__("resultado", 215))
    a["a3_operandos_250_90"] = variante("a3", lambda c: c["derivados_esperados"]["deuda_neta"].__setitem__("operandos", [250, 90]))
    a["a4_cita_sin_la_linea_del_fixture"] = variante("a4", lambda c: c["analisis"]["C24"].__setitem__("fuente", "Nota 4: Caja 90"))
    a["a5_sin_bloque_evidencia"] = variante("a5", lambda c: c.pop("evidencia"))
    a["a6_sin_derivados_esperados"] = variante("a6", lambda c: c.pop("derivados_esperados"))
    # lo que la validación NO mira: la deuda 300 y el original 95 solo existen como texto o como operando declarado
    a["a7_texto_dice_deuda_999_pero_operandos_300_90"] = variante("a7", lambda c: c["evidencia"]["Análisis!C24"].__setitem__("E", "Caja 90; Deuda financiera 999"))
    a["nota"] = ("a1-a6 deben dar exit 2 sin llamar al producto; a7 (texto de evidencia con otra deuda) pasa: la deuda 300 solo se valida "
                 "como operando declarado en derivados_esperados, bloque que el producto no lee (cambiar_base.py no lo usa)")
    res["a_validacion_del_CAMBIO"] = a

    # b) MAPA declarado
    t = os.path.join(tmp, "mapa", "resultados_qwen", "ejecucion_d")
    shutil.copytree(D, t, ignore=shutil.ignore_patterns("__pycache__"))
    adp = os.path.join(t, "scripts", "especificaciones", "adaptaciones.json")
    ad = json.load(open(adp, encoding="utf-8"))
    ad["casos"]["Q1-028"]["cobertura_banco"][0] = {"indice": 0, "asercion": "C9", "cobertura": "asercion", "razon": ""}   # caso SIN spec ni evidencia
    ad["casos"]["Q1-027"]["cobertura_banco"][2] = {"indice": 2, "asercion": "C4", "cobertura": "asercion", "razon": ""}   # C4 es no_discriminante
    json.dump(ad, open(adp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    r = subprocess.run([PY, "-I", "-B", os.path.join(t, "scripts", "generar_correspondencia.py")], capture_output=True, text=True,
                       env=dict(os.environ, BANCO_DIR=BANCO))
    filas = [x for x in csv.DictReader(open(os.path.join(t, "MAPA_CRITERIOS_BANCO.csv"), encoding="utf-8"))]
    res["b_MAPA_declarado"] = {
        "exit": r.returncode, "salida": r.stdout.strip().replace(tmp, "<tmp>")[-110:],
        "Q1-028#0 (caso sin especificación ni evidencia)": next((x["asercion_arnes"], x["cobertura"], x["estado_ejecucion"]) for x in filas if x["caso"] == "Q1-028" and x["criterio_indice"] == "0"),
        "Q1-027#2 (C4 es no_discriminante)": next((x["asercion_arnes"], x["cobertura"]) for x in filas if x["caso"] == "Q1-027" and x["criterio_indice"] == "2"),
        "con_asercion_publicado": 54,
        "con_asercion_tras_declarar_dos_filas": sum(1 for x in filas if x["cobertura"] == "asercion" and x["asercion_arnes"] != "sin aserción"),
        "veredicto": "el recuento «con aserción» es un dato declarado en adaptaciones.json; el generador no lo contrasta con especificaciones ni resultados"}
    txt = json.dumps(res, ensure_ascii=False, indent=1).replace(tmp, "<tmp>")
open(OUT, "w").write(txt)
print(txt)
