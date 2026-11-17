"""Sondas del revisor contra el arnés D en 3934bc9 (bloque 1) y 5f4b2a2 (bloque 2).

Uso: python3 -I sondas_arnes_d2.py <ejecucion_d bloque1> <ejecucion_d bloque2> <banco_revisado> <salida.json>

Todo con CANDIDATA FALSA y scripts de juguete (stubs) que imitan la interfaz del producto:
no se ejecuta Munger, ni LibreOffice, ni agentes, ni red. Mide la lógica del arnés y de los
generadores (matriz, correspondencia, relevo), no el producto. Repite las sondas P1-P5, P7,
P8 y P9 de la revisión de 1ac661b y añade una variante no literal por defecto.
"""
import csv, hashlib, json, os, shutil, subprocess, sys, tempfile, collections

D1, D2, BANCO, OUT = [os.path.abspath(x) for x in sys.argv[1:5]]
PY = sys.executable
res = {"alcance": "sondas con candidata falsa (stubs); no son resultados del producto Munger"}

STUB_VE = r'''
import json, os, sys
modo = os.environ.get("STUB_MODO", "")
cmd = sys.argv[1]
aqui = os.path.dirname(os.path.abspath(__file__))
if cmd == "plantilla":
    exp = sys.argv[2]
    json.dump({"entradas": [{"celda": "Historia!C23"}, {"celda": "Historia!C24"}], "perimetro_del_expediente": ""},
              open(os.path.join(exp, "verificacion_entradas.plantilla.json"), "w"))
    extra = os.path.join(aqui, "override.txt")
    if os.path.isfile(extra):
        print("INYECTADO DESDE ARCHIVO NO RASTREADO: " + open(extra).read().strip())
    print("plantilla con 2 entradas"); sys.exit(0)
if cmd == "comprobar":
    if modo == "q034_sin_rango":
        print(json.dumps({"comprobadas": [], "pendientes": ["aux:litigio: no está acreditado (sin mención de rango)"]}))
    elif modo == "q034_universo_sin_rango":
        print(json.dumps({"universo": 321, "comprobadas": [], "datos_como_hipotesis": [],
                          "pendientes": ["aux:litigio: no está acreditado (sin mención de rango)"]}))
    elif modo == "q034_eco_nota":
        # el producto de juguete NO lee el registro: solo devuelve la nota que escribió el arnés
        print(json.dumps({"universo": 321, "comprobadas": [], "datos_como_hipotesis": [],
                          "pendientes": ["aux:litigio: no está acreditado; rango acotado preservado como hipótesis; sin punto"]}))
    else:
        print(json.dumps({}))
    sys.exit(1)
if cmd == "sellar":
    print("selladas 0 · rechazadas 1"); sys.exit(1)
sys.exit(9)
'''
STUB_FICHA = r'''
import os, sys
if "--provisional" not in sys.argv:
    print("no se confirma: falta aprobación"); sys.exit(3)
if os.environ.get("STUB_MODO") == "plantilla_ausente":
    sys.stderr.write("STUB: plantilla ausente\n"); sys.exit(2)
sys.exit(0)
'''
STUB_INFORME = STUB_FICHA.replace("ficha", "informe")
STUB_CAMBIAR = r'''
import os, sys
m = os.environ.get("STUB_CAMBIAR", "ajeno_subcadena")
if m == "ajeno_subcadena":
    sys.stderr.write("ERROR ajeno a pdftotext: CAMBIO inválido; «archivo» ausente o inexistente en texto/: 'X.txt'\n")
elif m == "replay_real":
    # stderr literal de evidencias/Q1-026/cambiar_base_preparar.txt (publicado)
    sys.stderr.write("fase1_historia.py construir falló: ipal: «cero» sin «cita» literal de la página 12\n"
                     "AR_2019: sbc: «cero» sin «cita» literal de la página 13\n"
                     "AR_2019: arrendamientos: «cero» sin «cita» literal de la página 62\n"
                     "AR_2019: minoritarios: «cero» sin «cita» literal de la página 11\n"
                     "AR_2020: minoritarios: «cero» sin «cita» literal de la página 4\n"
                     + "".join(f"AR_{a}: AR_{a}: «archivo» ausente o inexistente en texto/: 'AR_{a}.txt'\n" for a in (2021, 2022, 2023, 2024)))
elif m == "ajeno_con_lineas":
    # fallo por un motivo ajeno (CAMBIO mal formado) que además imprime líneas con los prefijos esperados
    sys.stderr.write("ERROR: CAMBIO mal formado: clave 'version_formato' no admitida\n"
                     "ipal: aviso: la cita no se ha podido revisar\n"
                     + "".join(f"AR_{a}: (diagnóstico previo) «archivo» ausente o inexistente en texto/\n" for a in (2021, 2022, 2023, 2024)))
sys.exit(1)
'''


def git(cand, *a):
    return subprocess.run(["git", "-C", cand, *a], check=True, capture_output=True, text=True)


def candidata(tmp, nombre="cand"):
    cand = os.path.join(tmp, nombre)
    sc = os.path.join(cand, "munger_v2_r1", "personaje_v2", "scripts")
    os.makedirs(sc)
    for n, t in (("verificacion_entradas.py", STUB_VE), ("ficha.py", STUB_FICHA),
                 ("informe.py", STUB_INFORME), ("cambiar_base.py", STUB_CAMBIAR)):
        open(os.path.join(sc, n), "w").write(t)
    git(cand, "init", "-q"); git(cand, "add", "-A")
    git(cand, "-c", "user.email=r@r", "-c", "user.name=revisor", "commit", "-qm", "stub")
    sha = git(cand, "rev-parse", "HEAD").stdout.strip()
    plantilla = os.path.join(tmp, nombre + "_plantilla_exp")
    os.makedirs(plantilla)
    open(os.path.join(plantilla, "ficha_provisional.json"), "w").write('{"heredado": true}')
    open(os.path.join(plantilla, "informe_provisional.md"), "w").write("heredado\n")
    open(os.path.join(plantilla, "fase1_v63.json"), "w").write('{"origen": "plantilla"}')
    return cand, sha, plantilla


def correr(D, spec_path, env_extra):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", BANCO_DIR=BANCO, **env_extra)
    return subprocess.run([PY, "-I", "-B", os.path.join(D, "scripts", "ejecutar_caso.py"), spec_path],
                          capture_output=True, text=True, env=env)


def resultado(ev, cid):
    p = os.path.join(ev, cid, "resultado_ejecucion.json")
    return json.load(open(p)) if os.path.isfile(p) else None


def crit(rr):
    return [(c["id"], c["estado"]) for c in rr["criterios"]] if rr else None


def spec_tmp(tmp, nombre, obj):
    p = os.path.join(tmp, nombre)
    json.dump(obj, open(p, "w"), ensure_ascii=False)
    return p


def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def sondas_arnes(D, etiqueta, tmp):
    out = {}
    cand, sha, plantilla = candidata(tmp)
    base = {"CANDIDATA_DIR": cand, "SHA_CANDIDATA_ESPERADO": sha, "PLANTILLA_EXP": plantilla}

    def run(nombre, spec, extra=None, cid=None):
        ev = os.path.join(tmp, "ev_" + nombre)
        rd = os.path.join(tmp, "run_" + nombre)
        r = correr(D, spec, {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": rd, **(extra or {})})
        cid = cid or json.load(open(spec))["id"]
        return r, resultado(ev, cid), ev, rd

    # P1 original
    sp = spec_tmp(tmp, "p1.json", {"id": "Q1-031", "harness_version": "3.0", "pasos": [], "criterios": []})
    r, rr, _, _ = run("p1", sp)
    out["P1_spec_vacia"] = {"exit": r.returncode, "estado": rr and rr["estado_caso"],
                            "veredicto": "DETECTA" if r.returncode != 0 and rr and rr["estado_caso"] != "COMPONENTE_OK" else "FALSO POSITIVO"}
    # P1/P2 variante: aserción tautológica sobre un archivo que escribe el propio arnés
    sp = spec_tmp(tmp, "p1v.json", {"id": "Q1-031", "harness_version": "3.0", "pasos": [{"op": "nuevo_expediente"}],
                                     "criterios": [{"id": "C1", "texto": "precio actual frente a histórico",
                                                    "afirma": [{"tipo": "archivo_existe", "archivo": "ejecucion.log"}]},
                                                   {"id": "C2", "texto": "objetivo calculado",
                                                    "afirma": [{"tipo": "texto_contiene", "archivo": "ejecucion.log", "contiene": "# Caso"}]}]})
    r, rr, _, _ = run("p1v", sp)
    out["P1v_P2v_asercion_sobre_log_del_arnes"] = {"exit": r.returncode, "estado": rr and rr["estado_caso"], "criterios": crit(rr),
                                                   "veredicto": "FALSO POSITIVO (no examina ninguna salida del producto)" if rr and rr["estado_caso"] == "COMPONENTE_OK" else "DETECTA"}
    # P2 original
    sp = spec_tmp(tmp, "p2.json", {"id": "Q1-033", "harness_version": "3.0", "pasos": [{"op": "nuevo_expediente"}],
                                    "criterios": [{"id": "C1", "texto": "x", "afirma": []}]})
    r, rr, _, _ = run("p2", sp)
    out["P2_criterio_sin_aserciones"] = {"exit": r.returncode, "estado": rr and rr["estado_caso"],
                                         "veredicto": "DETECTA" if r.returncode != 0 and rr and rr["estado_caso"] != "COMPONENTE_OK" else "FALSO POSITIVO"}
    # P3 original
    ev3 = os.path.join(tmp, "ev_p3")
    os.makedirs(os.path.join(ev3, "Q1-036"))
    open(os.path.join(ev3, "Q1-036", "07_informe_provisional.md"), "w").write("apta por entradas: no\n")
    sp = spec_tmp(tmp, "p3.json", {"id": "Q1-032", "harness_version": "3.0", "pasos": [{"op": "nuevo_expediente"}],
                                    "criterios": [{"id": "C1", "texto": "recuentos", "afirma": [
                                        {"tipo": "texto_contiene", "archivo": "../Q1-036/07_informe_provisional.md", "contiene": "apta por entradas: no"}]}]})
    r = correr(D, sp, {**base, "EVIDENCIAS_DIR": ev3, "RUN_DIR": os.path.join(tmp, "run_p3")})
    rr = resultado(ev3, "Q1-032")
    out["P3_lectura_otro_caso"] = {"exit": r.returncode, "estado": rr["estado_caso"], "errores": rr["errores"],
                                   "veredicto": "DETECTA" if rr["estado_caso"] != "COMPONENTE_OK" else "FALSO POSITIVO"}
    # P3 variante a: copiar_artefacto con ruta relativa que sale del expediente hacia el RUN_DIR de Q1-036
    rd = os.path.join(tmp, "run_p3va")
    os.makedirs(os.path.join(rd, "Q1-036", "Viscofan"))
    open(os.path.join(rd, "Q1-036", "Viscofan", "informe_provisional.md"), "w").write("SALIDA DE Q1-036\napta por entradas: no\n4 verificadas / 1 pendiente / 5\n")
    ev = os.path.join(tmp, "ev_p3va")
    sp = spec_tmp(tmp, "p3va.json", {"id": "Q1-032", "harness_version": "3.0", "pasos": [
        {"op": "nuevo_expediente"},
        {"op": "copiar_artefacto", "archivo": "../../Q1-036/Viscofan/informe_provisional.md", "guardar": "informe_propio.md"}],
        "criterios": [{"id": "C1", "texto": "la matriz parcial muestra 4/1/5", "afirma": [
            {"tipo": "texto_contiene", "archivo": "informe_propio.md", "contiene": "4 verificadas / 1 pendiente / 5"}]}]})
    r = correr(D, sp, {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": rd})
    rr = resultado(ev, "Q1-032")
    out["P3va_copiar_artefacto_de_otro_caso"] = {"exit": r.returncode, "estado": rr["estado_caso"], "criterios": crit(rr),
                                                 "artefactos": rr["artefactos"],
                                                 "veredicto": "FALSO POSITIVO (la contención solo cubre la lectura de aserciones)" if rr["estado_caso"] == "COMPONENTE_OK" else "DETECTA"}
    # P3 variante b: 'guardar' con ruta relativa escribe en la evidencia de otro caso
    ev = os.path.join(tmp, "ev_p3vb")
    os.makedirs(os.path.join(ev, "Q1-036"))
    victima = os.path.join(ev, "Q1-036", "07_informe_provisional.md")
    open(victima, "w").write("EVIDENCIA ORIGINAL DE Q1-036\n")
    sp = spec_tmp(tmp, "p3vb.json", {"id": "Q1-033", "harness_version": "3.0", "pasos": [
        {"op": "nuevo_expediente"},
        {"op": "comprobar", "guardar": "../Q1-036/07_informe_provisional.md", "esperado": [0, 1]}],
        "criterios": [{"id": "C1", "texto": "x", "afirma": [{"tipo": "texto_contiene", "archivo": "ejecucion.log", "contiene": "plantilla con 2 entradas"}]}]})
    r = correr(D, sp, {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(tmp, "run_p3vb")})
    rr = resultado(ev, "Q1-033")
    nuevo = open(victima).read()
    out["P3vb_guardar_escribe_en_otro_caso"] = {"exit": r.returncode, "estado": rr["estado_caso"],
                                                "contenido_Q1-036_tras_la_ejecucion": nuevo.strip()[:80],
                                                "veredicto": "DEFECTO (sobrescribe evidencia ajena)" if "ORIGINAL" not in nuevo else "OK"}
    # P5 original (spec Q1-034 de este bloque)
    q034 = os.path.join(D, "scripts/especificaciones/bloque2/Q1-034.json")
    for nombre, modo in (("P5_Q1-034_sin_universo", "q034_sin_rango"), ("P5v_Q1-034_universo_sin_rango", "q034_universo_sin_rango"),
                         ("P5w_Q1-034_eco_de_la_nota_del_arnes", "q034_eco_nota")):
        r, rr, ev, rd = run(nombre, q034, {"STUB_MODO": modo})
        det = {c["id"]: c["detalle"] for c in rr["criterios"]}
        out[nombre] = {"exit": r.returncode, "estado": rr["estado_caso"], "criterios": crit(rr), "detalle_C1": det.get("C1"),
                       "veredicto": ("FALSO POSITIVO en C1" if dict(crit(rr)).get("C1") == "CUMPLE_COMPONENTE" else "C1 FALLA")}
    # P7 original a: residuo pruebas_d dentro de la candidata
    cand7, sha7, pl7 = candidata(tmp, "cand7")
    os.makedirs(os.path.join(cand7, "munger_v2_r1", "pruebas_d", "Q1-026_origen"))
    open(os.path.join(cand7, "munger_v2_r1", "pruebas_d", "Q1-026_origen", "fase1_v63.json"), "w").write('{"origen": "PREEXISTENTE Y MUTADO"}')
    q026 = os.path.join(D, "scripts/especificaciones/bloque2/Q1-026.json")
    ev = os.path.join(tmp, "ev_p7a")
    r = correr(D, q026, {"CANDIDATA_DIR": cand7, "SHA_CANDIDATA_ESPERADO": sha7, "PLANTILLA_EXP": pl7,
                         "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(tmp, "run_p7a"), "STUB_CAMBIAR": "ajeno_subcadena"})
    rr = resultado(ev, "Q1-026")
    out["P7a_residuo_en_candidata"] = {"exit": r.returncode, "estado": rr["estado_caso"], "errores": rr["errores"][:2],
                                       "veredicto": "DETECTA" if rr["estado_caso"] != "COMPONENTE_OK" else "NO DETECTA"}
    # P7 original b: origen preexistente mutado bajo RUN_DIR + fallo ajeno con la subcadena
    rd = os.path.join(tmp, "run_p7b")
    os.makedirs(os.path.join(rd, "Q1-026", "pruebas_d", "Q1-026_origen"))
    open(os.path.join(rd, "Q1-026", "pruebas_d", "Q1-026_origen", "fase1_v63.json"), "w").write('{"origen": "PREEXISTENTE Y MUTADO"}')
    for nombre, modo in (("P7b_fallo_ajeno_subcadena", "ajeno_subcadena"), ("P7c_replay_stderr_real", "replay_real"),
                         ("P7v_fallo_ajeno_con_lineas_esperadas", "ajeno_con_lineas")):
        ev = os.path.join(tmp, "ev_" + nombre)
        rdn = rd if nombre.startswith("P7b") else os.path.join(tmp, "run_" + nombre)
        r = correr(D, q026, {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": rdn, "STUB_CAMBIAR": modo})
        rr = resultado(ev, "Q1-026")
        eb = os.path.join(ev, "Q1-026", "errores_bloqueo.json")
        st = subprocess.run(["git", "-C", cand, "status", "--porcelain"], capture_output=True, text=True).stdout.strip()
        orig = os.path.join(rdn, "Q1-026", "pruebas_d", "Q1-026_origen", "fase1_v63.json")
        out[nombre] = {"exit": r.returncode, "estado": rr["estado_caso"], "criterios": crit(rr),
                       "detalle_fallos": rr["afirmaciones_fallidas"][:3],
                       "errores_bloqueo": json.load(open(eb)) if os.path.isfile(eb) else None,
                       "origen_tras_ejecucion": open(orig).read() if os.path.isfile(orig) else None,
                       "git_status_candidata": st.splitlines()}
    # P8 original: archivo rastreado modificado sin commit
    cand8, sha8, pl8 = candidata(tmp, "cand8")
    open(os.path.join(cand8, "munger_v2_r1/personaje_v2/scripts/verificacion_entradas.py"), "a").write("\n# modificado sin commit\n")
    sp8 = spec_tmp(tmp, "p8.json", {"id": "Q1-031", "harness_version": "3.0", "pasos": [{"op": "nuevo_expediente"}],
                                     "criterios": [{"id": "C1", "texto": "x", "afirma": [{"tipo": "texto_contiene", "archivo": "ejecucion.log", "contiene": "plantilla con 2 entradas"}]}]})
    ev = os.path.join(tmp, "ev_p8")
    r = correr(D, sp8, {"CANDIDATA_DIR": cand8, "SHA_CANDIDATA_ESPERADO": sha8, "PLANTILLA_EXP": pl8, "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(tmp, "run_p8")})
    rr = resultado(ev, "Q1-031")
    out["P8_rastreado_modificado"] = {"exit": r.returncode, "estado": rr["estado_caso"], "errores": rr["errores"][:1],
                                      "veredicto": "DETECTA" if rr["estado_caso"] != "COMPONENTE_OK" else "NO DETECTA"}
    # P8 variante a: modificación oculta con skip-worktree
    cand8a, sha8a, pl8a = candidata(tmp, "cand8a")
    git(cand8a, "update-index", "--skip-worktree", "munger_v2_r1/personaje_v2/scripts/verificacion_entradas.py")
    p = os.path.join(cand8a, "munger_v2_r1/personaje_v2/scripts/verificacion_entradas.py")
    texto = open(p).read()  # leer antes de truncar
    open(p, "w").write(texto.replace('print("plantilla con 2 entradas")', 'print("plantilla con 2 entradas (SCRIPT ALTERADO)")'))
    ev = os.path.join(tmp, "ev_p8a")
    r = correr(D, sp8, {"CANDIDATA_DIR": cand8a, "SHA_CANDIDATA_ESPERADO": sha8a, "PLANTILLA_EXP": pl8a, "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(tmp, "run_p8a")})
    rr = resultado(ev, "Q1-031")
    log = open(os.path.join(ev, "Q1-031", "ejecucion.log")).read()
    out["P8va_skip_worktree"] = {"exit": r.returncode, "estado": rr["estado_caso"], "candidata_sha": rr["candidata_sha"] == sha8a,
                                 "git_status": subprocess.run(["git", "-C", cand8a, "status", "--porcelain"], capture_output=True, text=True).stdout.strip(),
                                 "script_alterado_ejecutado": "SCRIPT ALTERADO" in log,
                                 "veredicto": "NO DETECTA" if rr["estado_caso"] == "COMPONENTE_OK" else "DETECTA"}
    # P8 variante b: archivo NO rastreado en scripts/ que cambia el comportamiento
    cand8b, sha8b, pl8b = candidata(tmp, "cand8b")
    open(os.path.join(cand8b, "munger_v2_r1/personaje_v2/scripts/override.txt"), "w").write("comportamiento alterado")
    ev = os.path.join(tmp, "ev_p8b")
    r = correr(D, sp8, {"CANDIDATA_DIR": cand8b, "SHA_CANDIDATA_ESPERADO": sha8b, "PLANTILLA_EXP": pl8b, "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(tmp, "run_p8b")})
    rr = resultado(ev, "Q1-031")
    log = open(os.path.join(ev, "Q1-031", "ejecucion.log")).read()
    out["P8vb_no_rastreado_en_scripts"] = {"exit": r.returncode, "estado": rr["estado_caso"], "candidata_no_rastreadas": rr.get("candidata_no_rastreadas"),
                                           "salida_alterada": "INYECTADO" in log,
                                           "veredicto": "NO DETECTA" if rr["estado_caso"] == "COMPONENTE_OK" else "DETECTA"}
    # P9 original y variantes
    ev = os.path.join(tmp, "ev_p9"); rd = os.path.join(tmp, "run_p9")
    for _ in range(2):
        correr(D, sp8, {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": rd})
    n = open(os.path.join(ev, "Q1-031", "ejecucion.log")).read().count("# Caso Q1-031")
    out["P9_un_log_por_ejecucion"] = {"cabeceras_en_log": n, "veredicto": "OK" if n == 1 else "ACUMULA"}
    ev = os.path.join(tmp, "ev_p9v")
    for _ in range(2):
        correr(D, sp8, {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": rd, "ARNES_EVIDENCIAS_LIMPIAS": "0"})
    n = open(os.path.join(ev, "Q1-031", "ejecucion.log")).read().count("# Caso Q1-031")
    rr = resultado(ev, "Q1-031")
    out["P9v_opcion_ARNES_EVIDENCIAS_LIMPIAS_0"] = {"cabeceras_en_log": n,
                                                    "resultado_registra_la_opcion": any("LIMPIAS" in k.upper() for k in rr),
                                                    "veredicto": "ACUMULA sin registrarlo" if n > 1 else "OK"}
    ev = os.path.join(tmp, "ev_p9w")
    os.makedirs(os.path.join(ev, "Q1-001")); open(os.path.join(ev, "Q1-001", "evidencia.txt"), "w").write("de otro caso")
    sp = spec_tmp(tmp, "p9w.json", {"id": ".", "pasos": [], "criterios": []})
    r = correr(D, sp, {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(tmp, "run_p9w")})
    out["P9w_id_punto_borra_evidencias"] = {"exit": r.returncode, "Q1-001_sobrevive": os.path.isfile(os.path.join(ev, "Q1-001", "evidencia.txt")),
                                            "stderr_ultima": (r.stderr.strip().splitlines() or [""])[-1][:160],
                                            "veredicto": "DEFECTO (borra la evidencia de los demás casos)" if not os.path.isfile(os.path.join(ev, "Q1-001", "evidencia.txt")) else "OK"}
    # R7a: --revisor dado por la spec y auxiliar sin comprobación
    sp = spec_tmp(tmp, "r7a.json", {"id": "Q1-020", "harness_version": "3.0", "pasos": [
        {"op": "nuevo_expediente"},
        {"op": "entrada", "celda": "aux:prueba", "clase": "hipotesis", "hipotesis": {"fundamento": "x", "alternativas": [], "limites": "y"}},
        {"op": "sellar", "celdas": ["Historia!C24"], "revisor": "revisora independiente (nombre de persona)", "esperado": [0, 1]}],
        "criterios": [{"id": "C1", "texto": "x", "afirma": [{"tipo": "texto_contiene", "archivo": "ejecucion.log", "contiene": "rechazadas 1"}]}]})
    r, rr, ev, rd = run("r7a", sp)
    sellar = next(p for p in rr["pasos"] if "sellar" in " ".join(p["comando"]))
    reg = json.load(open(os.path.join(rd, "Q1-020", "Viscofan", "verificacion_entradas.json")))
    aux = next(e for e in reg["entradas"] if e["celda"] == "aux:prueba")
    out["R7a_marcas"] = {"revisor_en_comando_sellar": sellar["comando"][sellar["comando"].index("--revisor") + 1],
                         "aux_comprobacion_escrita_por_el_arnes": aux["comprobacion"],
                         "veredicto": "LÍMITE: registros del arnés sin marca" if "[SIMULADO]" not in sellar["comando"][sellar["comando"].index("--revisor") + 1] or not aux["comprobacion"].get("_simulada") else "OK"}
    # R7c: SHA observado (con una candidata limpia)
    r, rr, _, _ = run("r7c", sp8)
    out["R7c_sha_observado"] = {"candidata_sha": rr["candidata_sha"], "esperado": sha, "spec_sha256": bool(rr.get("spec_sha256")),
                                "banco_casos_sha256": bool(rr.get("banco_casos_sha256")), "harness_version": rr["harness_version"]}
    return out


def sondas_matriz(D, etiqueta, tmp):
    t = os.path.join(tmp, "m_" + etiqueta, "d")
    shutil.copytree(D, t, ignore=shutil.ignore_patterns("__pycache__"))
    ev = os.path.join(t, "evidencias")
    spec001 = os.path.join(t, "scripts/especificaciones/piloto/Q1-001.json")
    spec002 = os.path.join(t, "scripts/especificaciones/bloque2/Q1-002.json")
    # M1 (P4 original): Q1-031 con dos campos
    os.makedirs(os.path.join(ev, "Q1-031"), exist_ok=True)
    json.dump({"harness_version": "2.0", "estado_caso": "COMPONENTE_OK"}, open(os.path.join(ev, "Q1-031", "resultado_ejecucion.json"), "w"))
    # M2 (P4 variante): Q1-001 forjado con 5 campos, huella de la spec calculada y UN criterio; sin ninguna otra evidencia
    shutil.rmtree(os.path.join(ev, "Q1-001"))
    os.makedirs(os.path.join(ev, "Q1-001"))
    json.dump({"harness_version": "3.0", "estado_caso": "COMPONENTE_OK", "spec_sha256": sha256(spec001),
               "criterios": [{"id": "C1", "estado": "CUMPLE_COMPONENTE"}]}, open(os.path.join(ev, "Q1-001", "resultado_ejecucion.json"), "w"))
    # M3: Q1-026 con resultado ERROR_ENTORNO (o cualquiera)
    json.dump({"harness_version": "3.0", "estado_caso": "ERROR_ENTORNO", "criterios": []}, open(os.path.join(ev, "Q1-026", "resultado_ejecucion.json"), "w"))
    # M4: Q1-002 publicado reetiquetado como v3 con la huella de la spec actual (como lo dejaría una ejecución v3 real)
    p2 = os.path.join(ev, "Q1-002", "resultado_ejecucion.json")
    o = json.load(open(p2)); o["harness_version"] = "3.0"; o["spec_sha256"] = sha256(spec002)
    json.dump(o, open(p2, "w"))
    r = subprocess.run([PY, "-I", "-B", os.path.join(t, "scripts/generar_matriz.py")], env=dict(os.environ, BANCO_DIR=BANCO), capture_output=True, text=True)
    filas = {x["id"]: x for x in csv.DictReader(open(os.path.join(t, "MATRIZ_EJECUCION.csv")))}
    rec = json.load(open(os.path.join(ev, "recuentos.json")))
    g = lambda cid: {k: filas[cid][k] for k in ("estado_ejecucion", "veredicto_componente")}
    return {"exit": r.returncode,
            "M1_P4_dos_campos_Q1-031": g("Q1-031"),
            "M2_P4v_forjado_5_campos_Q1-001_sin_evidencia": g("Q1-001"),
            "M3_Q1-026_ERROR_ENTORNO": g("Q1-026"),
            "M4_Q1-002_resultado_v3_legitimo": g("Q1-002"),
            "Q1-003_publicado_v2_sin_tocar": g("Q1-003"),
            "recuentos_estado": rec["estado_ejecucion"], "recuentos_veredicto_componente": rec["veredicto_componente"]}


def sondas_r2(D, tmp):
    """Q1-027: ¿discrimina cada aserción frente al estado previo? y ¿lo detectaría la prueba 15?"""
    code = r'''
import json, os, shutil, sys
D, EVPUB, T = sys.argv[1:4]
sys.path.insert(0, os.path.join(D, "scripts"))
os.environ["RUN_DIR"] = os.path.join(T, "run")
import lib_arnes as L, ejecutar_caso as EC
spec = json.load(open(os.path.join(D, "scripts/especificaciones/piloto/Q1-027.json")))
def caso(nombre):
    c = L.Caso.__new__(L.Caso); c.id = "Q1-027"; c.ev_dir = os.path.join(T, nombre); c.errores = []
    os.makedirs(c.ev_dir, exist_ok=True); return c
vacio = caso("vacio")
previo = caso("previo")   # el estado ANTES de mutar: 02 copiado como 03
shutil.copy(os.path.join(EVPUB, "02_comprobar_antes_mutacion.json"), os.path.join(previo.ev_dir, "02_comprobar_antes_mutacion.json"))
shutil.copy(os.path.join(EVPUB, "02_comprobar_antes_mutacion.json"), os.path.join(previo.ev_dir, "03_comprobar_tras_mutacion.json"))
shutil.copy(os.path.join(EVPUB, "01_sellar.txt"), os.path.join(previo.ev_dir, "04_sellar_tras_mutacion.txt"))
publicado = caso("pub")
for f in os.listdir(EVPUB):
    shutil.copy(os.path.join(EVPUB, f), os.path.join(publicado.ev_dir, f))
out = {}
for cr in spec["criterios"]:
    for i, a in enumerate(cr["afirma"]):
        out[f"{cr['id']}.{i}"] = {"vacio": EC.evaluar_afirmacion(vacio, a)[0], "estado_previo": EC.evaluar_afirmacion(previo, a)[0],
                                  "evidencia_publicada": EC.evaluar_afirmacion(publicado, a)[0]}
print(json.dumps(out))
'''
    hp = os.path.join(tmp, "r2_helper.py"); open(hp, "w").write(code)
    r = subprocess.run([PY, "-I", "-B", hp, D, os.path.join(D, "evidencias", "Q1-027"), os.path.join(tmp, "r2")], capture_output=True, text=True)
    if r.returncode:
        return {"error": r.stderr[-600:]}
    tabla = json.loads(r.stdout)
    return {"tabla": tabla,
            "no_discriminan_frente_al_estado_previo": [k for k, v in tabla.items() if v["estado_previo"]],
            "pasan_en_vacio_(lo_que_mide_la_prueba_15)": [k for k, v in tabla.items() if v["vacio"]]}


def sondas_regeneracion(D, tmp):
    t = os.path.join(tmp, "regen", "d")
    shutil.copytree(D, t, ignore=shutil.ignore_patterns("__pycache__"))
    env = dict(os.environ, BANCO_DIR=BANCO)
    ex = {}
    for s in ("generar_matriz.py", "generar_correspondencia.py", "generar_relevo.py"):
        ex[s] = subprocess.run([PY, "-I", "-B", os.path.join(t, "scripts", s)], env=env, capture_output=True, text=True).returncode
    filas = list(csv.DictReader(open(os.path.join(t, "MATRIZ_EJECUCION.csv"))))
    mapa = list(csv.DictReader(open(os.path.join(t, "MAPA_CRITERIOS_BANCO.csv"))))
    rel = json.load(open(os.path.join(t, "relevo/PAQUETES_RELEVO.json")))
    sin_agente = [p["caso"] for p in rel["paquetes"] if p["caso"] not in ("Q1-030", "Q1-035")
                  and not any("agente" in (f["qué"] + f["quién"]) for f in p["falta_para_caso_completo"])]
    publicado = {x["id"]: x for x in csv.DictReader(open(os.path.join(D, "MATRIZ_EJECUCION.csv")))}
    return {"exits": ex,
            "matriz_regenerada_estados": dict(collections.Counter(x["estado_ejecucion"] for x in filas)),
            "matriz_regenerada_CUMPLE": sum(1 for x in filas if x["veredicto_componente"] == "CUMPLE"),
            "matriz_publicada_CUMPLE": sum(1 for x in publicado.values() if x["veredicto_componente"] == "CUMPLE"),
            "matriz_publicada_igual_a_regenerada": open(os.path.join(t, "MATRIZ_EJECUCION.csv")).read() == open(os.path.join(D, "MATRIZ_EJECUCION.csv")).read(),
            "mapa_filas": len(mapa), "mapa_con_asercion": sum(1 for x in mapa if x["cobertura"] == "asercion"),
            "mapa_publicado_existe": os.path.isfile(os.path.join(D, "MAPA_CRITERIOS_BANCO.csv")),
            "relevos_sin_ningun_paso_de_agente": sin_agente,
            "relevos_Q1-028_Q1-032": {p["caso"]: {"comando_relevo": p["comando_relevo"], "falta": p["falta_para_caso_completo"]}
                                      for p in rel["paquetes"] if p["caso"] in ("Q1-028", "Q1-032")},
            "relevo_Q1-001_falta": next(p["falta_para_caso_completo"] for p in rel["paquetes"] if p["caso"] == "Q1-001")}


with tempfile.TemporaryDirectory() as tmp:
    for et, D in (("bloque1_3934bc9", D1), ("bloque2_5f4b2a2", D2)):
        os.makedirs(os.path.join(tmp, et))
        res[et] = {"arnes": sondas_arnes(D, et, os.path.join(tmp, et)), "matriz": sondas_matriz(D, et, os.path.join(tmp, et))}
    res["bloque2_5f4b2a2"]["R2_Q1-027"] = sondas_r2(D2, os.path.join(tmp, "bloque2_5f4b2a2"))
    res["bloque2_5f4b2a2"]["regeneracion_con_evidencia_publicada"] = sondas_regeneracion(D2, os.path.join(tmp, "bloque2_5f4b2a2"))

txt = json.dumps(res, ensure_ascii=False, indent=1)
for a, b in ((os.path.dirname(os.path.dirname(OUT)), "<rev_D2>"), (tempfile.gettempdir(), "<tmp>")):
    txt = txt.replace(a, b)
open(OUT, "w").write(txt)
print(txt)
