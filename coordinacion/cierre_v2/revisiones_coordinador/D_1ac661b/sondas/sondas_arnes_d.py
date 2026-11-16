"""Sondas del revisor contra el arnés D @1ac661b (no del producto).

Uso: python3 -I sondas_arnes_d.py <dir ejecucion_d (copia)> <dir banco_revisado> <salida.json>

Todas las sondas usan una CANDIDATA FALSA con scripts de juguete (stubs) que imitan la
interfaz de línea de órdenes del producto; NO se ejecuta código de Munger, ni LibreOffice,
ni agentes, ni red. Lo que se mide es la lógica del arnés (aserciones, propagación de
errores, artefactos, recuentos), no el comportamiento del producto. Incluye las dos sondas
D de sondas_revision.py (d375d80) adaptadas al arnés nuevo.
"""
import csv, json, os, shutil, subprocess, sys, tempfile, collections

D, BANCO, OUT = [os.path.abspath(x) for x in sys.argv[1:4]]
PY = sys.executable
res = {"alcance": "sondas del arnés con candidata falsa (stubs); no son resultados del producto"}

STUB_VE = r'''
import json, os, sys
modo = os.environ.get("STUB_MODO", "")
cmd = sys.argv[1]
if cmd == "plantilla":
    exp = sys.argv[2]
    json.dump({"entradas": [{"celda": "Historia!C23"}, {"celda": "Historia!C24"}], "perimetro_del_expediente": ""},
              open(os.path.join(exp, "verificacion_entradas.plantilla.json"), "w"))
    print("plantilla con 2 entradas"); sys.exit(0)
if cmd == "comprobar":
    if modo == "q034_sin_rango":
        # salida que NO conserva ningún rango 0-200 ni hipótesis: solo un pendiente genérico
        print(json.dumps({"comprobadas": [], "pendientes": ["aux:litigio: no está acreditado (sin mención de rango)"]}))
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
    # vía oficial: se niega como en la evidencia publicada (exit 3)
    print("no se confirma: falta aprobación; no hay ficha.json oficial"); sys.exit(3)
if os.environ.get("STUB_MODO") == "plantilla_ausente":
    # vía provisional con plantilla ausente: exit 2 sin escribir salida (escenario D_SALIDA_OBSOLETA)
    sys.stderr.write("STUB: plantilla ausente: no se escribe ninguna ficha\n"); sys.exit(2)
sys.exit(0)
'''
STUB_INFORME = STUB_FICHA.replace("ficha", "informe")
STUB_CAMBIAR = r'''
import sys
# Falla por un motivo cualquiera, pero su mensaje contiene la subcadena que afirma Q1-026 C1
sys.stderr.write("ERROR ajeno a pdftotext: CAMBIO inválido; «archivo» ausente o inexistente en texto/: 'X.txt'\n"); sys.exit(1)
'''


def candidata_falsa(tmp, con_scripts=True):
    cand = os.path.join(tmp, "cand")
    sc = os.path.join(cand, "munger_v2_r1", "personaje_v2", "scripts")
    os.makedirs(sc)
    if con_scripts:
        for n, t in (("verificacion_entradas.py", STUB_VE), ("ficha.py", STUB_FICHA),
                     ("informe.py", STUB_INFORME), ("cambiar_base.py", STUB_CAMBIAR)):
            open(os.path.join(sc, n), "w").write(t)
    else:
        open(os.path.join(cand, "LEEME"), "w").write("sin scripts")
    g = lambda *a: subprocess.run(["git", "-C", cand, *a], check=True, capture_output=True, text=True)
    g("init", "-q"); g("add", "-A"); g("-c", "user.email=r@r", "-c", "user.name=revisor", "commit", "-qm", "stub")
    sha = g("rev-parse", "HEAD").stdout.strip()
    plantilla = os.path.join(tmp, "plantilla_exp")
    os.makedirs(plantilla)
    # salidas heredadas del histórico (para la sonda de artefacto obsoleto)
    open(os.path.join(plantilla, "ficha_provisional.json"), "w").write('{"heredado": true}')
    open(os.path.join(plantilla, "informe_provisional.md"), "w").write("heredado\napta por entradas: no\n")
    open(os.path.join(plantilla, "fase1_v63.json"), "w").write('{"origen": "plantilla"}')
    return cand, sha, plantilla


def correr(spec_path, env_extra):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", BANCO_DIR=BANCO, **env_extra)
    r = subprocess.run([PY, "-I", "-B", os.path.join(D, "scripts", "ejecutar_caso.py"), spec_path],
                       capture_output=True, text=True, env=env)
    return r


def resultado(ev, cid):
    p = os.path.join(ev, cid, "resultado_ejecucion.json")
    return json.load(open(p)) if os.path.isfile(p) else None


with tempfile.TemporaryDirectory() as tmp:
    # --- R1: sonda del revisor 'D_arnes_sin_scripts_producto' adaptada (scripts vacíos)
    t1 = os.path.join(tmp, "r1"); os.makedirs(t1)
    cand, sha, plantilla = candidata_falsa(t1, con_scripts=False)
    ev = os.path.join(t1, "ev")
    r = correr(os.path.join(D, "scripts/especificaciones/piloto/Q1-001.json"),
               {"CANDIDATA_DIR": cand, "SHA_CANDIDATA_ESPERADO": sha, "PLANTILLA_EXP": plantilla,
                "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(t1, "run")})
    rr = resultado(ev, "Q1-001")
    res["R1_sin_scripts_producto"] = {"exit_arnes": r.returncode, "stdout": r.stdout.strip()[:200],
                                      "estado_caso": rr and rr["estado_caso"],
                                      "esperado_revisor": "exit != 0 y estado no positivo",
                                      "veredicto": "DETECTA" if r.returncode != 0 and rr and rr["estado_caso"] != "COMPONENTE_OK" else "NO DETECTA"}

    # --- R2: sonda del revisor 'D_matriz_sin_evidencias' adaptada (scripts sin carpeta evidencias)
    t2 = os.path.join(tmp, "r2", "d"); os.makedirs(os.path.dirname(t2))
    shutil.copytree(os.path.join(D, "scripts"), os.path.join(t2, "scripts"), ignore=shutil.ignore_patterns("__pycache__"))
    r = subprocess.run([PY, "-I", "-B", os.path.join(t2, "scripts/generar_matriz.py")],
                       env=dict(os.environ, BANCO_DIR=BANCO), capture_output=True, text=True)
    m = os.path.join(t2, "MATRIZ_EJECUCION.csv")
    filas = list(csv.DictReader(open(m))) if os.path.isfile(m) else []
    res["R2_matriz_sin_evidencias"] = {"exit": r.returncode, "carpeta_evidencias_existe": os.path.isdir(os.path.join(t2, "evidencias")),
                                       "filas": len(filas), "veredicto_componente": dict(collections.Counter(x["veredicto_componente"] or "(vacío)" for x in filas)),
                                       "stderr_ultima_linea": (r.stderr.strip().splitlines() or [""])[-1][:200],
                                       "veredicto": "DETECTA (sin CUMPLE)" if not any(x["veredicto_componente"] == "CUMPLE" for x in filas) else "NO DETECTA"}

    # Candidata falsa con stubs para el resto
    t3 = os.path.join(tmp, "r3"); os.makedirs(t3)
    cand, sha, plantilla = candidata_falsa(t3)
    base = {"CANDIDATA_DIR": cand, "SHA_CANDIDATA_ESPERADO": sha, "PLANTILLA_EXP": plantilla}

    # --- P1: especificación sin criterios ni pasos -> ¿COMPONENTE_OK?
    ev = os.path.join(t3, "ev_p1")
    sp = os.path.join(t3, "vacia.json")
    json.dump({"id": "Q1-031", "harness_version": "2.0", "pasos": [], "criterios": []}, open(sp, "w"))
    r = correr(sp, {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(t3, "run_p1")})
    rr = resultado(ev, "Q1-031")
    res["P1_especificacion_vacia"] = {"exit_arnes": r.returncode, "estado_caso": rr["estado_caso"], "criterios": rr["criterios"],
                                      "esperado_revisor": "un resultado vacío debe fallar",
                                      "veredicto": "FALSO POSITIVO" if r.returncode == 0 and rr["estado_caso"] == "COMPONENTE_OK" else "DETECTA"}

    # --- P2: criterio sin aserciones -> NO_EVALUADO pero caso COMPONENTE_OK
    ev = os.path.join(t3, "ev_p2")
    sp = os.path.join(t3, "sin_afirma.json")
    json.dump({"id": "Q1-033", "harness_version": "2.0", "pasos": [{"op": "nuevo_expediente"}],
               "criterios": [{"id": "C1", "texto": "precio actual frente a histórico", "afirma": []}]}, open(sp, "w"))
    r = correr(sp, {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(t3, "run_p2")})
    rr = resultado(ev, "Q1-033")
    res["P2_criterio_sin_aserciones"] = {"exit_arnes": r.returncode, "estado_caso": rr["estado_caso"],
                                         "criterios": [(c["id"], c["estado"]) for c in rr["criterios"]],
                                         "veredicto": "FALSO POSITIVO" if r.returncode == 0 and rr["estado_caso"] == "COMPONENTE_OK" else "DETECTA"}

    # --- P3: aserción que lee evidencia de OTRO caso (../Q1-036/...) -> observación compartida convertida en CUMPLE
    ev = os.path.join(t3, "ev_p3")
    os.makedirs(os.path.join(ev, "Q1-036"))
    open(os.path.join(ev, "Q1-036", "07_informe_provisional.md"), "w").write("apta por entradas: no\n")
    sp = os.path.join(t3, "cruzada.json")
    json.dump({"id": "Q1-032", "harness_version": "2.0", "pasos": [],
               "criterios": [{"id": "C1", "texto": "recuentos visibles", "afirma": [
                   {"tipo": "texto_contiene", "archivo": "../Q1-036/07_informe_provisional.md", "contiene": "apta por entradas: no"}]}]},
              open(sp, "w"))
    r = correr(sp, {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(t3, "run_p3")})
    rr = resultado(ev, "Q1-032")
    res["P3_evidencia_de_otro_caso"] = {"exit_arnes": r.returncode, "estado_caso": rr["estado_caso"],
                                        "criterios": [(c["id"], c["estado"], c["detalle"]) for c in rr["criterios"]],
                                        "veredicto": "FALSO POSITIVO (sin aislamiento por caso)" if rr["estado_caso"] == "COMPONENTE_OK" else "DETECTA"}

    # --- P4: generar_matriz acepta un resultado_ejecucion.json mínimo/forjado sin criterios ni especificación
    t4 = os.path.join(tmp, "p4", "d"); os.makedirs(os.path.dirname(t4))
    shutil.copytree(D, t4, ignore=shutil.ignore_patterns("__pycache__"))
    os.makedirs(os.path.join(t4, "evidencias", "Q1-031"), exist_ok=True)
    json.dump({"harness_version": "2.0", "estado_caso": "COMPONENTE_OK"}, open(os.path.join(t4, "evidencias", "Q1-031", "resultado_ejecucion.json"), "w"))
    r = subprocess.run([PY, "-I", "-B", os.path.join(t4, "scripts/generar_matriz.py")], env=dict(os.environ, BANCO_DIR=BANCO), capture_output=True, text=True)
    fila = next(x for x in csv.DictReader(open(os.path.join(t4, "MATRIZ_EJECUCION.csv"))) if x["id"] == "Q1-031")
    rec = json.load(open(os.path.join(t4, "evidencias", "recuentos.json")))
    res["P4_resultado_forjado_en_matriz"] = {"exit": r.returncode, "Q1-031": {k: fila[k] for k in ("estado_ejecucion", "veredicto_componente", "criterios_evaluados", "comandos_reproducibles")},
                                            "recuentos_veredicto_componente": rec["veredicto_componente"],
                                            "veredicto": "FALSO POSITIVO" if fila["veredicto_componente"] == "CUMPLE" else "DETECTA"}

    # --- P5: Q1-034 real con una salida que no conserva ningún rango -> C1 'rango 0-200 se conserva'
    ev = os.path.join(t3, "ev_p5")
    r = correr(os.path.join(D, "scripts/especificaciones/bloque2/Q1-034.json"),
               {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(t3, "run_p5"), "STUB_MODO": "q034_sin_rango"})
    rr = resultado(ev, "Q1-034")
    salida = open(os.path.join(ev, "Q1-034", "01_comprobar_rango_acotado.json")).read()
    res["P5_Q1-034_sin_rango"] = {"exit_arnes": r.returncode, "estado_caso": rr["estado_caso"],
                                  "salida_01": salida.strip(), "menciona_0_200": ("200" in salida),
                                  "criterios": [(c["id"], c["estado"]) for c in rr["criterios"]],
                                  "veredicto": "FALSO POSITIVO en C1" if dict((c["id"], c["estado"]) for c in rr["criterios"]).get("C1") == "CUMPLE_COMPONENTE" and "200" not in salida else "DETECTA"}

    # --- P6: sonda D_SALIDA_OBSOLETA con la especificación real Q1-036 (ficha/informe provisional exit 2)
    ev = os.path.join(t3, "ev_p6")
    r = correr(os.path.join(D, "scripts/especificaciones/piloto/Q1-036.json"),
               {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(t3, "run_p6"), "STUB_MODO": "plantilla_ausente"})
    rr = resultado(ev, "Q1-036")
    copiados = [f for f in ("05_ficha_provisional.json", "07_informe_provisional.md") if os.path.isfile(os.path.join(ev, "Q1-036", f))]
    res["P6_salida_obsoleta_Q1-036"] = {"exit_arnes": r.returncode, "estado_caso": rr["estado_caso"], "copiados": copiados,
                                        "exits": [p["exit"] for p in rr["pasos"]],
                                        "veredicto": "DETECTA" if r.returncode != 0 and not copiados and rr["estado_caso"] != "COMPONENTE_OK" else "NO DETECTA"}

    # --- P7: Q1-026 real: cambiar_base falla por motivo ajeno (stub) y el origen preexistente se reutiliza
    pd = os.path.join(cand, "munger_v2_r1", "pruebas_d", "Q1-026_origen")
    os.makedirs(pd)
    open(os.path.join(pd, "fase1_v63.json"), "w").write('{"origen": "PREEXISTENTE Y MUTADO"}')
    ev = os.path.join(t3, "ev_p7")
    r = correr(os.path.join(D, "scripts/especificaciones/bloque2/Q1-026.json"),
               {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(t3, "run_p7")})
    rr = resultado(ev, "Q1-026")
    st = subprocess.run(["git", "-C", cand, "status", "--porcelain"], capture_output=True, text=True).stdout
    res["P7_Q1-026"] = {"exit_arnes": r.returncode, "estado_caso": rr["estado_caso"],
                        "criterios": [(c["id"], c["estado"]) for c in rr["criterios"]],
                        "origen_reutilizado": open(os.path.join(pd, "fase1_v63.json")).read(),
                        "escribe_en_candidata (git status)": st.strip().splitlines(),
                        "veredicto": "FALSO POSITIVO (C1 acepta cualquier fallo con la subcadena; origen preexistente reutilizado; escribe en la candidata)" if rr["estado_caso"] == "COMPONENTE_OK" else "DETECTA"}

    # --- P8: candidata modificada sin commit al mismo HEAD -> el control de SHA no lo detecta
    open(os.path.join(cand, "munger_v2_r1", "personaje_v2", "scripts", "verificacion_entradas.py"), "a").write("\n# modificado sin commit\n")
    ev = os.path.join(t3, "ev_p8")
    sp = os.path.join(t3, "p8.json")
    json.dump({"id": "Q1-031", "harness_version": "2.0", "pasos": [{"op": "nuevo_expediente"}],
               "criterios": [{"id": "C1", "texto": "x", "afirma": [{"tipo": "texto_contiene", "archivo": "ejecucion.log", "contiene": "plantilla con 2 entradas"}]}]}, open(sp, "w"))
    r = correr(sp, {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(t3, "run_p8")})
    rr = resultado(ev, "Q1-031")
    res["P8_candidata_sucia"] = {"exit_arnes": r.returncode, "estado_caso": rr["estado_caso"], "candidata_sha_registrado": rr["candidata_sha"],
                                 "git_status": subprocess.run(["git", "-C", cand, "status", "--porcelain"], capture_output=True, text=True).stdout.strip().splitlines(),
                                 "veredicto": "NO DETECTA (árbol modificado aceptado)" if rr["estado_caso"] == "COMPONENTE_OK" else "DETECTA"}

    # --- P9: el log se acumula entre ejecuciones (no se reinicia la carpeta de evidencias)
    r = correr(sp, {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(t3, "run_p8")})
    n = open(os.path.join(ev, "Q1-031", "ejecucion.log")).read().count("# Caso Q1-031")
    res["P9_log_acumulado"] = {"ejecuciones_en_un_log": n, "veredicto": "ACUMULA (procedencia del log mezclada)" if n > 1 else "OK"}

json.dump(res, open(OUT, "w"), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))
