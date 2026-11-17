"""Sondas del revisor contra el arnés D en d032691 (bloque 3), frente a CORRECCION_D3.

Uso: python3 -I -B sondas_arnes_d3.py <ejecucion_d de d032691> <banco_revisado @4745f38> <salida.json>

Todo con CANDIDATA FALSA y scripts de juguete (stubs) que imitan la interfaz del producto:
no se ejecuta Munger, ni LibreOffice, ni agentes, ni red. Mide la lógica del arnés y de los
generadores (matriz, correspondencia, relevo), no el producto.

- R1: repite las variantes de la revisión D2 (P1v, P3va, P3vb, M2, P8va, P8vb, P9w) y añade
  una variante nueva por invariante (N1..N5). Comprueba además si ejecutar_todo.sh cierra M2.
- R2: controles negativos frente al estado previo (Q1-027, Q1-034, Q1-026) y la lógica de la
  prueba 15 de pruebas_arnes.py.
- R3: reevaluación independiente de las aserciones sobre la evidencia publicada.
- R4: dependencia del relevo respecto de PARCIAL_COMPONENTE.
"""
import csv, hashlib, json, os, shutil, subprocess, sys, tempfile, collections

D, BANCO, OUT = [os.path.abspath(x) for x in sys.argv[1:4]]
PY = sys.executable
res = {"alcance": "sondas con candidata falsa (stubs); no son resultados del producto Munger",
       "objeto": "d032691 (resultados_qwen/ejecucion_d)"}

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
    if modo == "q034_eco_nota":
        # el producto de juguete NO lee el registro: devuelve siempre lo mismo
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
import sys
if "--provisional" not in sys.argv:
    print("no se confirma: falta aprobación"); sys.exit(3)
sys.exit(0)
'''
REAL_026 = ("fase1_historia.py construir falló: ipal: «cero» sin «cita» literal de la página 12\n"
            "AR_2019: sbc: «cero» sin «cita» literal de la página 13\n"
            "AR_2019: arrendamientos: «cero» sin «cita» literal de la página 62\n"
            "AR_2019: minoritarios: «cero» sin «cita» literal de la página 11\n"
            "AR_2020: minoritarios: «cero» sin «cita» literal de la página 4\n"
            + "".join(f"AR_{a}: AR_{a}: «archivo» ausente o inexistente en texto/: 'AR_{a}.txt'\n" for a in (2021, 2022, 2023, 2024)))
STUB_CAMBIAR = r'''
import os, sys
m = os.environ.get("STUB_CAMBIAR", "replay_real")
REAL = %r
if m == "replay_real":
    sys.stderr.write(REAL)
elif m == "ajeno_con_lineas":
    # P7v de la revisión D2: fallo ajeno que imprime líneas con los prefijos antiguos
    sys.stderr.write("ERROR: CAMBIO mal formado: clave 'version_formato' no admitida\n"
                     "ipal: aviso: la cita no se ha podido revisar\n"
                     + "".join(f"AR_{a}: (diagnóstico previo) «archivo» ausente o inexistente en texto/\n" for a in (2021, 2022, 2023, 2024)))
elif m == "ajeno_mas_real":
    # NUEVA: el CAMBIO es inválido (motivo ajeno al entorno) y además salen las líneas reales
    sys.stderr.write("ERROR: CAMBIO inválido: analisis.C24.valor no coincide con la evidencia declarada\n" + REAL)
sys.exit(1)
''' % REAL_026


def git(cand, *a):
    return subprocess.run(["git", "-C", cand, *a], check=True, capture_output=True, text=True)


def candidata(tmp, nombre="cand"):
    cand = os.path.join(tmp, nombre)
    sc = os.path.join(cand, "munger_v2_r1", "personaje_v2", "scripts")
    os.makedirs(sc)
    for n, t in (("verificacion_entradas.py", STUB_VE), ("ficha.py", STUB_FICHA),
                 ("informe.py", STUB_FICHA), ("cambiar_base.py", STUB_CAMBIAR)):
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


def correr(D_, spec_path, env_extra):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", BANCO_DIR=BANCO, **env_extra)
    return subprocess.run([PY, "-I", "-B", os.path.join(D_, "scripts", "ejecutar_caso.py"), spec_path],
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


def generar(t, *scripts):
    env = dict(os.environ, BANCO_DIR=BANCO, PYTHONDONTWRITEBYTECODE="1")
    return {s: subprocess.run([PY, "-I", "-B", os.path.join(t, "scripts", s)], env=env, capture_output=True, text=True).returncode
            for s in scripts}


def fila_matriz(t, cid):
    for x in csv.DictReader(open(os.path.join(t, "MATRIZ_EJECUCION.csv"), encoding="utf-8")):
        if x["id"] == cid:
            return {k: x[k] for k in ("estado_ejecucion", "veredicto_componente")}


LOG_OK = [{"tipo": "texto_contiene", "archivo": "ejecucion.log", "contiene": "plantilla con 2 entradas"}]


def r1(tmp):
    out = {}
    cand, sha, plantilla = candidata(tmp)
    base = {"CANDIDATA_DIR": cand, "SHA_CANDIDATA_ESPERADO": sha, "PLANTILLA_EXP": plantilla}

    def run(nombre, spec, extra=None, ev=None, rd=None):
        ev = ev or os.path.join(tmp, "ev_" + nombre)
        rd = rd or os.path.join(tmp, "run_" + nombre)
        r = correr(D, spec, {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": rd, **(extra or {})})
        return r, ev, rd

    # ---- invariante 1: rutas (lectura y escritura) dentro del RUN_DIR del caso ----
    rd = os.path.join(tmp, "run_p3va")
    os.makedirs(os.path.join(rd, "Q1-036", "Viscofan"))
    open(os.path.join(rd, "Q1-036", "Viscofan", "informe_provisional.md"), "w").write("SALIDA DE Q1-036\n4 verificadas / 1 pendiente / 5\n")
    sp = spec_tmp(tmp, "p3va.json", {"id": "Q1-032", "harness_version": "3.0", "pasos": [
        {"op": "nuevo_expediente"},
        {"op": "copiar_artefacto", "archivo": "../../Q1-036/Viscofan/informe_provisional.md", "guardar": "informe_propio.md"}],
        "criterios": [{"id": "C1", "texto": "matriz 4/1/5", "afirma": [
            {"tipo": "texto_contiene", "archivo": "informe_propio.md", "contiene": "4 verificadas / 1 pendiente / 5"}]}]})
    r, ev, _ = run("p3va", sp, rd=rd)
    rr = resultado(ev, "Q1-032")
    out["P3va_copiar_artefacto_../../Q1-036"] = {"exit": r.returncode, "estado": rr["estado_caso"], "criterios": crit(rr),
                                                 "veredicto": "ABIERTO (lee fuera del caso y da COMPONENTE_OK)" if rr["estado_caso"] == "COMPONENTE_OK" else "CERRADO"}

    ev = os.path.join(tmp, "ev_p3vb")
    os.makedirs(os.path.join(ev, "Q1-036"))
    victima = os.path.join(ev, "Q1-036", "07_informe_provisional.md")
    open(victima, "w").write("EVIDENCIA ORIGINAL DE Q1-036\n")
    sp = spec_tmp(tmp, "p3vb.json", {"id": "Q1-033", "harness_version": "3.0", "pasos": [
        {"op": "nuevo_expediente"}, {"op": "comprobar", "guardar": "../Q1-036/07_informe_provisional.md", "esperado": [0, 1]}],
        "criterios": [{"id": "C1", "texto": "x", "afirma": LOG_OK}]})
    r, _, _ = run("p3vb", sp, ev=ev)
    nuevo = open(victima).read()
    out["P3vb_guardar_../Q1-036"] = {"exit": r.returncode, "estado": resultado(ev, "Q1-033")["estado_caso"],
                                     "contenido_Q1-036_tras_la_ejecucion": nuevo.strip()[:60],
                                     "veredicto": "ABIERTO (sobrescribe evidencia ajena)" if "ORIGINAL" not in nuevo else "CERRADO"}

    # N1a (nueva, escritura): escribir_fuente con nombre relativo escribe en el RUN_DIR de otro caso
    rd = os.path.join(tmp, "run_n1a")
    os.makedirs(os.path.join(rd, "Q1-036", "Viscofan"))
    vict = os.path.join(rd, "Q1-036", "Viscofan", "verificacion_entradas.json")
    open(vict, "w").write('{"original": "Q1-036"}')
    sp = spec_tmp(tmp, "n1a.json", {"id": "Q1-031", "harness_version": "3.0", "pasos": [
        {"op": "nuevo_expediente"},
        {"op": "escribir_fuente", "nombre": "../../../Q1-036/Viscofan/verificacion_entradas.json", "paginas": ["PISADO POR Q1-031"]}],
        "criterios": [{"id": "C1", "texto": "x", "afirma": LOG_OK}]})
    r, ev, _ = run("n1a", sp, rd=rd)
    out["N1a_escribir_fuente_nombre_../../../Q1-036 (nueva)"] = {
        "exit": r.returncode, "estado": resultado(ev, "Q1-031")["estado_caso"],
        "registro_de_Q1-036_tras_la_ejecucion": open(vict).read().strip()[:60],
        "veredicto": "ABIERTO (escribe en el RUN_DIR de otro caso)" if "PISADO" in open(vict).read() else "CERRADO"}
    # N1b (nueva, lectura): copiar_artefacto con ruta ABSOLUTA a la evidencia de otro caso
    ajeno = os.path.join(tmp, "ev_ajena", "Q1-036")
    os.makedirs(ajeno)
    open(os.path.join(ajeno, "07_informe_provisional.md"), "w").write("apta por entradas: no\n")
    sp = spec_tmp(tmp, "n1b.json", {"id": "Q1-032", "harness_version": "3.0", "pasos": [
        {"op": "nuevo_expediente"},
        {"op": "copiar_artefacto", "archivo": os.path.join(ajeno, "07_informe_provisional.md"), "guardar": "informe.md"}],
        "criterios": [{"id": "C1", "texto": "x", "afirma": [{"tipo": "texto_contiene", "archivo": "informe.md", "contiene": "apta por entradas: no"}]}]})
    r, ev, _ = run("n1b", sp)
    rr = resultado(ev, "Q1-032")
    out["N1b_copiar_artefacto_ruta_absoluta (nueva)"] = {"exit": r.returncode, "estado": rr["estado_caso"], "criterios": crit(rr),
                                                         "veredicto": "ABIERTO" if rr["estado_caso"] == "COMPONENTE_OK" else "CERRADO"}

    # ---- invariante 3: aserciones que no leen archivos escritos por el propio arnés ----
    sp = spec_tmp(tmp, "p1v.json", {"id": "Q1-031", "harness_version": "3.0", "pasos": [{"op": "nuevo_expediente"}],
                                     "criterios": [{"id": "C1", "texto": "precio histórico", "afirma": [{"tipo": "archivo_existe", "archivo": "ejecucion.log"}]},
                                                   {"id": "C2", "texto": "objetivo", "afirma": [{"tipo": "texto_contiene", "archivo": "ejecucion.log", "contiene": "# Caso"}]}]})
    r, ev, _ = run("p1v", sp)
    rr = resultado(ev, "Q1-031")
    out["P1v_asercion_sobre_ejecucion.log"] = {"exit": r.returncode, "estado": rr["estado_caso"], "criterios": crit(rr),
                                               "veredicto": "ABIERTO" if rr["estado_caso"] == "COMPONENTE_OK" else "CERRADO"}
    # N3 (nueva): aserción run: sobre la fuente sintética que escribe el propio arnés
    sp = spec_tmp(tmp, "n3.json", {"id": "Q1-031", "harness_version": "3.0", "pasos": [
        {"op": "nuevo_expediente"},
        {"op": "escribir_fuente", "nombre": "f6_031_precio.txt", "paginas": ["precio histórico 14,20 EUR (31/12/2025); capitalización 710"]}],
        "criterios": [{"id": "C1", "texto": "la salida etiqueta el precio como histórico", "afirma": [
            {"tipo": "texto_contiene", "archivo": "run:Viscofan/fuentes_sinteticas/f6_031_precio.txt", "contiene": "precio histórico 14,20"}]},
            {"id": "C2", "texto": "capitalización 710 documentada", "afirma": [
            {"tipo": "texto_contiene", "archivo": "run:Viscofan/fuentes_sinteticas/f6_031_precio.txt", "contiene": "710"}]}]})
    r, ev, _ = run("n3", sp)
    rr = resultado(ev, "Q1-031")
    out["N3_asercion_run:_sobre_fuente_escrita_por_el_arnes (nueva)"] = {"exit": r.returncode, "estado": rr["estado_caso"], "criterios": crit(rr),
                                                                        "veredicto": "ABIERTO" if rr["estado_caso"] == "COMPONENTE_OK" else "CERRADO"}

    # ---- invariante 4: el id se valida antes de tocar el disco ----
    ev = os.path.join(tmp, "ev_p9w")
    os.makedirs(os.path.join(ev, "Q1-001")); open(os.path.join(ev, "Q1-001", "evidencia.txt"), "w").write("de otro caso")
    sp = spec_tmp(tmp, "p9w.json", {"id": ".", "pasos": [], "criterios": []})
    r, _, _ = run("p9w", sp, ev=ev)
    viva = os.path.isfile(os.path.join(ev, "Q1-001", "evidencia.txt"))
    out["P9w_id_punto"] = {"exit": r.returncode, "Q1-001_sobrevive": viva, "veredicto": "CERRADO" if viva else "ABIERTO (borra la evidencia de todos los casos)"}
    # N4 (nueva): id "../fuera" borra una carpeta hermana de EVIDENCIAS (fuera del árbol de evidencias)
    raiz = os.path.join(tmp, "n4")
    ev = os.path.join(raiz, "evidencias")
    os.makedirs(ev); os.makedirs(os.path.join(raiz, "fuera"))
    open(os.path.join(raiz, "fuera", "ajeno.txt"), "w").write("archivo ajeno a las evidencias")
    sp = spec_tmp(tmp, "n4.json", {"id": "../fuera", "pasos": [], "criterios": []})
    r, _, _ = run("n4", sp, ev=ev)
    viva = os.path.isfile(os.path.join(raiz, "fuera", "ajeno.txt"))
    out["N4_id_../fuera (nueva)"] = {"exit": r.returncode, "ajeno_sobrevive": viva,
                                     "veredicto": "CERRADO" if viva else "ABIERTO (borra fuera de EVIDENCIAS antes de validar)"}
    # N4b: id vacío
    ev = os.path.join(tmp, "ev_n4b")
    os.makedirs(os.path.join(ev, "Q1-002")); open(os.path.join(ev, "Q1-002", "evidencia.txt"), "w").write("x")
    sp = spec_tmp(tmp, "n4b.json", {"id": "", "pasos": [], "criterios": []})
    r, _, _ = run("n4b", sp, ev=ev)
    viva = os.path.isfile(os.path.join(ev, "Q1-002", "evidencia.txt"))
    out["N4b_id_vacio (nueva)"] = {"exit": r.returncode, "Q1-002_sobrevive": viva, "veredicto": "CERRADO" if viva else "ABIERTO"}

    # ---- invariante 5: candidata limpia ----
    def cand_alterada(nombre, prepara):
        c, s, pl = candidata(tmp, nombre)
        prepara(c)
        ev = os.path.join(tmp, "ev_" + nombre)
        r = correr(D, sp8, {"CANDIDATA_DIR": c, "SHA_CANDIDATA_ESPERADO": s, "PLANTILLA_EXP": pl,
                            "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(tmp, "run_" + nombre)})
        rr = resultado(ev, "Q1-031")
        log = open(os.path.join(ev, "Q1-031", "ejecucion.log")).read()
        return {"exit": r.returncode, "estado": rr["estado_caso"], "candidata_no_rastreadas": rr.get("candidata_no_rastreadas"),
                "git_status": subprocess.run(["git", "-C", c, "status", "--porcelain"], capture_output=True, text=True).stdout.strip(),
                "salida_alterada_en_log": ("ALTERADO" in log) or ("INYECTADO" in log),
                "veredicto": "ABIERTO (pasa como candidata limpia)" if rr["estado_caso"] == "COMPONENTE_OK" else "CERRADO"}
    sp8 = spec_tmp(tmp, "p8.json", {"id": "Q1-031", "harness_version": "3.0", "pasos": [{"op": "nuevo_expediente"}],
                                     "criterios": [{"id": "C1", "texto": "x", "afirma": [{"tipo": "texto_contiene", "archivo": "ejecucion.log", "contiene": "plantilla con 2 entradas"}]}]})
    rel = "munger_v2_r1/personaje_v2/scripts/verificacion_entradas.py"

    def alterar(c, flag):
        git(c, "update-index", flag, rel)
        p = os.path.join(c, rel)
        t = open(p).read()
        open(p, "w").write(t.replace('print("plantilla con 2 entradas")', 'print("plantilla con 2 entradas (SCRIPT ALTERADO)")'))
    out["P8va_skip_worktree"] = cand_alterada("c8a", lambda c: alterar(c, "--skip-worktree"))
    out["P8vb_no_rastreado_en_scripts"] = cand_alterada("c8b", lambda c: open(os.path.join(c, "munger_v2_r1/personaje_v2/scripts/override.txt"), "w").write("comportamiento alterado"))
    out["N5a_assume_unchanged (nueva)"] = cand_alterada("c8c", lambda c: alterar(c, "--assume-unchanged"))

    def excluido(c):
        open(os.path.join(c, ".git", "info", "exclude"), "a").write("\noverride.txt\n")
        open(os.path.join(c, "munger_v2_r1/personaje_v2/scripts/override.txt"), "w").write("comportamiento alterado y oculto")
    out["N5b_no_rastreado_oculto_por_.git/info/exclude (nueva)"] = cand_alterada("c8d", excluido)
    return out


def r1_matriz(tmp):
    """Invariante 2: la matriz reevalúa las aserciones."""
    t = os.path.join(tmp, "m", "d")
    shutil.copytree(D, t, ignore=shutil.ignore_patterns("__pycache__"))
    ev = os.path.join(t, "evidencias")
    spec001 = os.path.join(t, "scripts/especificaciones/piloto/Q1-001.json")
    # M2: Q1-001 sustituido por un resultado de 4 campos con la huella de la spec y UN criterio
    shutil.rmtree(os.path.join(ev, "Q1-001")); os.makedirs(os.path.join(ev, "Q1-001"))
    json.dump({"harness_version": "3.0", "estado_caso": "COMPONENTE_OK", "spec_sha256": sha256(spec001),
               "criterios": [{"id": "C1", "estado": "CUMPLE_COMPONENTE"}]}, open(os.path.join(ev, "Q1-001", "resultado_ejecucion.json"), "w"))
    # N2a (nueva): Q1-003 con la salida del producto alterada (comprobadas vacía) y resultado intacto
    p3 = os.path.join(ev, "Q1-003")
    alterados = []
    for f in sorted(os.listdir(p3)):
        if f.endswith(".json") and f != "resultado_ejecucion.json":
            o = json.load(open(os.path.join(p3, f)))
            for k in ("comprobadas", "pendientes", "desactualizadas"):
                if isinstance(o.get(k), list):
                    o[k] = []
            o["universo"] = 0
            json.dump(o, open(os.path.join(p3, f), "w")); alterados.append(f)
    # N2b (nueva): Q1-004 de otra candidata y otro banco, harness 2.0
    p4 = os.path.join(ev, "Q1-004", "resultado_ejecucion.json")
    o = json.load(open(p4)); o["candidata_sha"] = "0" * 40; o["banco_casos_sha256"] = "f" * 64; o["harness_version"] = "2.0"
    json.dump(o, open(p4, "w"))
    # M3: Q1-026 con resultado ERROR_ENTORNO y sin criterios
    json.dump({"harness_version": "3.0", "estado_caso": "ERROR_ENTORNO", "criterios": []},
              open(os.path.join(ev, "Q1-026", "resultado_ejecucion.json"), "w"))
    ex = generar(t, "generar_matriz.py")
    return {"exit": ex,
            "M2_resultado_de_4_campos_Q1-001": fila_matriz(t, "Q1-001"),
            "N2a_salida_del_producto_vaciada_Q1-003 (nueva)": {"archivos_alterados": alterados, **fila_matriz(t, "Q1-003")},
            "N2b_otra_candidata_otro_banco_harness_2.0_Q1-004 (nueva)": fila_matriz(t, "Q1-004"),
            "M3_Q1-026_ERROR_ENTORNO": fila_matriz(t, "Q1-026")}


def r1_ejecutar_todo_cierra_M2(tmp):
    """¿Cierra ejecutar_todo.sh la variante M2 por otra vía? Reejecuta la spec: Caso.__init__
    borra la carpeta del caso antes de escribir el resultado. Se reproduce con UNA spec."""
    t = os.path.join(tmp, "et", "d")
    shutil.copytree(D, t, ignore=shutil.ignore_patterns("__pycache__"))
    ev = os.path.join(t, "evidencias")
    spec001 = os.path.join(t, "scripts/especificaciones/piloto/Q1-001.json")
    shutil.rmtree(os.path.join(ev, "Q1-001")); os.makedirs(os.path.join(ev, "Q1-001"))
    json.dump({"harness_version": "3.0", "estado_caso": "COMPONENTE_OK", "spec_sha256": sha256(spec001),
               "criterios": [{"id": "C1", "estado": "CUMPLE_COMPONENTE"}]}, open(os.path.join(ev, "Q1-001", "resultado_ejecucion.json"), "w"))
    cand, sha, pl = candidata(tmp, "cand_et")
    r = correr(t, spec001, {"CANDIDATA_DIR": cand, "SHA_CANDIDATA_ESPERADO": sha, "PLANTILLA_EXP": pl, "RUN_DIR": os.path.join(tmp, "run_et")})
    generar(t, "generar_matriz.py")
    rr = resultado(ev, "Q1-001")
    return {"ejecutar_caso_exit": r.returncode, "resultado_tras_reejecutar": rr and rr.get("estado_caso"),
            "fila_Q1-001": fila_matriz(t, "Q1-001"),
            "conclusion": "dentro del flujo ejecutar_todo.sh el resultado forjado se sustituye; generar_matriz.py por separado lo sigue aceptando (M2)"}


def r2(tmp):
    code = r'''
import json, os, shutil, sys
D, EVP, T, MODO = sys.argv[1:5]
sys.path.insert(0, os.path.join(D, "scripts"))
os.environ["RUN_DIR"] = os.path.join(T, "run")
import lib_arnes as L, ejecutar_caso as EC
L.RUN_DIR = os.environ["RUN_DIR"]
def caso(cid, nombre):
    c = L.Caso.__new__(L.Caso); c.id = cid; c.ev_dir = os.path.join(T, nombre, cid); c.errores = []
    os.makedirs(c.ev_dir, exist_ok=True); os.makedirs(os.path.join(L.RUN_DIR, cid), exist_ok=True); return c
out = {}
if MODO == "q027":
    spec = json.load(open(os.path.join(D, "scripts/especificaciones/piloto/Q1-027.json")))
    ev = os.path.join(EVP, "Q1-027")
    vacio = caso("Q1-027", "vacio"); previo = caso("Q1-027", "previo"); pub = caso("Q1-027", "pub")
    # estado previo = el estado ANTES de mutar: 02 copiado como 03 y el primer sellado como 04
    shutil.copy(os.path.join(ev, "02_comprobar_antes_mutacion.json"), os.path.join(previo.ev_dir, "02_comprobar_antes_mutacion.json"))
    shutil.copy(os.path.join(ev, "02_comprobar_antes_mutacion.json"), os.path.join(previo.ev_dir, "03_comprobar_tras_mutacion.json"))
    shutil.copy(os.path.join(ev, "01_sellar.txt"), os.path.join(previo.ev_dir, "04_sellar_tras_mutacion.txt"))
    for f in os.listdir(ev):
        shutil.copy(os.path.join(ev, f), os.path.join(pub.ev_dir, f))
    for cr in spec["criterios"]:
        for i, a in enumerate(cr["afirma"]):
            out[f"{cr['id']}.{i}"] = {"vacio": EC.evaluar_afirmacion(vacio, a)[0], "estado_previo": EC.evaluar_afirmacion(previo, a)[0],
                                      "evidencia_publicada": EC.evaluar_afirmacion(pub, a)[0]}
elif MODO == "q034":
    spec = json.load(open(os.path.join(D, "scripts/especificaciones/bloque2/Q1-034.json")))
    # estado previo = solo lo que escribe el arnés (paso 3, poner_entrada) y NINGUNA salida del producto
    previo = caso("Q1-034", "previo")
    exp = os.path.join(L.RUN_DIR, "Q1-034", "Viscofan"); os.makedirs(exp, exist_ok=True)
    json.dump({"entradas": [], "perimetro_del_expediente": "consolidado"}, open(os.path.join(exp, "verificacion_entradas.plantilla.json"), "w"))
    p3 = spec["pasos"][2]
    L.poner_entrada(exp, p3["celda"], clase=p3["clase"], hipotesis=p3["hipotesis"], comprobacion=p3["comprobacion"])
    for cr in spec["criterios"]:
        for i, a in enumerate(cr["afirma"]):
            out[f"{cr['id']}.{i}"] = {"estado_previo_solo_registro_del_arnes": EC.evaluar_afirmacion(previo, a)[0]}
print(json.dumps(out))
'''
    hp = os.path.join(tmp, "r2_helper.py"); open(hp, "w").write(code)
    out = {}
    for modo in ("q027", "q034"):
        r = subprocess.run([PY, "-I", "-B", hp, D, os.path.join(D, "evidencias"), os.path.join(tmp, "r2_" + modo), modo], capture_output=True, text=True)
        out[modo] = json.loads(r.stdout) if r.returncode == 0 else {"error": r.stderr[-800:]}
    t27 = out["q027"]
    out["Q1-027_no_discriminan_frente_al_estado_previo"] = [k for k, v in t27.items() if isinstance(v, dict) and v.get("estado_previo")]
    out["Q1-034_pasan_sin_ninguna_salida_del_producto"] = [k for k, v in out["q034"].items() if isinstance(v, dict) and v.get("estado_previo_solo_registro_del_arnes")]

    # Prueba 15 de pruebas_arnes.py, reproducida tal cual (estado previo VACÍO) sobre las specs de d032691
    code15 = r'''
import glob, json, os, sys
D, T = sys.argv[1:3]
sys.path.insert(0, os.path.join(D, "scripts"))
import lib_arnes as L, ejecutar_caso as EC
L.RUN_DIR = os.path.join(T, "run_vacio")
mal = []; n = 0
for sp in sorted(glob.glob(os.path.join(D, "scripts", "especificaciones", "*", "Q1-*.json"))):
    s = json.load(open(sp)); c = L.Caso.__new__(L.Caso); c.id = s["id"]; c.ev_dir = os.path.join(T, "ev_vacio", s["id"]); c.errores = []
    os.makedirs(c.ev_dir, exist_ok=True); os.makedirs(os.path.join(L.RUN_DIR, s["id"]), exist_ok=True)
    for cr in s["criterios"]:
        for a in cr["afirma"]:
            n += 1
            if EC.evaluar_afirmacion(c, a)[0]: mal.append(f"{s['id']} {cr['id']}")
print(json.dumps({"aserciones": n, "pasan_en_vacio": mal}))
'''
    hp15 = os.path.join(tmp, "p15.py"); open(hp15, "w").write(code15)
    r = subprocess.run([PY, "-I", "-B", hp15, D, os.path.join(tmp, "p15")], capture_output=True, text=True)
    out["prueba15_reproducida"] = json.loads(r.stdout) if r.returncode == 0 else {"error": r.stderr[-600:]}
    out["prueba15_detecta_Q1-027_C4"] = False if out["Q1-027_no_discriminan_frente_al_estado_previo"] and not out["prueba15_reproducida"].get("pasan_en_vacio") else None

    # Q1-034 ejecutada con un producto de juguete que NO lee el registro (eco constante)
    cand, sha, pl = candidata(tmp, "cand34")
    ev = os.path.join(tmp, "ev_q034"); rd = os.path.join(tmp, "run_q034")
    rr_ = correr(D, os.path.join(D, "scripts/especificaciones/bloque2/Q1-034.json"),
                 {"CANDIDATA_DIR": cand, "SHA_CANDIDATA_ESPERADO": sha, "PLANTILLA_EXP": pl, "EVIDENCIAS_DIR": ev, "RUN_DIR": rd, "STUB_MODO": "q034_eco_nota"})
    rr = resultado(ev, "Q1-034")
    reg = json.load(open(os.path.join(rd, "Q1-034", "Viscofan", "verificacion_entradas.json")))
    aux = next(e for e in reg["entradas"] if e["celda"] == "aux:litigio")
    out["Q1-034_con_producto_de_eco"] = {"exit": rr_.returncode, "estado": rr["estado_caso"], "criterios": crit(rr),
                                         "clase_final_de_aux:litigio_cuando_se_evalua_C1": aux["clase"],
                                         "texto_de_C1": json.load(open(os.path.join(D, "scripts/especificaciones/bloque2/Q1-034.json")))["criterios"][0]["texto"]}

    # Q1-026 C1 con tres stderr
    q026 = os.path.join(D, "scripts/especificaciones/bloque2/Q1-026.json")
    for nombre, modo in (("P7c_stderr_real", "replay_real"), ("P7v_ajeno_con_lineas_antiguas", "ajeno_con_lineas"),
                         ("P7v2_CAMBIO_invalido_mas_lineas_reales (nueva)", "ajeno_mas_real")):
        c, s, pl = candidata(tmp, "c26_" + modo)
        ev = os.path.join(tmp, "ev26_" + modo)
        r = correr(D, q026, {"CANDIDATA_DIR": c, "SHA_CANDIDATA_ESPERADO": s, "PLANTILLA_EXP": pl, "EVIDENCIAS_DIR": ev,
                             "RUN_DIR": os.path.join(tmp, "run26_" + modo), "STUB_CAMBIAR": modo})
        rr = resultado(ev, "Q1-026")
        eb = json.load(open(os.path.join(ev, "Q1-026", "errores_bloqueo.json")))
        out[nombre] = {"exit": r.returncode, "estado": rr["estado_caso"], "criterios": crit(rr),
                       "otros_errores_primera_linea": (eb["otros_errores"] or [""])[0][:100]}
    return out


def r3_reevaluar(tmp):
    """Reevalúa con el evaluar_afirmacion de d032691 cada aserción no run: sobre la evidencia publicada."""
    code = r'''
import glob, json, os, sys
D, T = sys.argv[1:3]
sys.path.insert(0, os.path.join(D, "scripts"))
import lib_arnes as L, ejecutar_caso as EC
out = {"coinciden": [], "difieren": [], "no_reevaluables_run:": []}
for rp in sorted(glob.glob(os.path.join(D, "evidencias", "Q1-*", "resultado_ejecucion.json"))):
    r = json.load(open(rp)); cid = r["caso"]
    s = json.load(open(os.path.join(os.path.dirname(os.path.dirname(D)), r["spec"])))
    c = L.Caso.__new__(L.Caso); c.id = cid; c.ev_dir = os.path.dirname(rp); c.errores = []
    decl = {x["id"]: x["estado"] for x in r["criterios"]}
    for cr in s["criterios"]:
        oks = []
        for a in cr["afirma"]:
            if a["archivo"].startswith("run:"):
                out["no_reevaluables_run:"].append(f"{cid} {cr['id']}"); continue
            oks.append(EC.evaluar_afirmacion(c, a)[0])
        mio = "CUMPLE_COMPONENTE" if all(oks) else "FALLA_COMPONENTE"
        (out["coinciden"] if mio == decl.get(cr["id"]) else out["difieren"]).append(f"{cid} {cr['id']}")
out["n_coinciden"] = len(out.pop("coinciden"))
print(json.dumps(out))
'''
    hp = os.path.join(tmp, "r3.py"); open(hp, "w").write(code)
    r = subprocess.run([PY, "-I", "-B", hp, D, tmp], capture_output=True, text=True)
    return json.loads(r.stdout) if r.returncode == 0 else {"error": r.stderr[-800:]}


def r4(tmp):
    """¿El paso de agente del relevo depende de PARCIAL_COMPONENTE?"""
    t = os.path.join(tmp, "r4", "d")
    shutil.copytree(D, t, ignore=shutil.ignore_patterns("__pycache__"))
    p = os.path.join(t, "evidencias", "Q1-005", "resultado_ejecucion.json")
    o = json.load(open(p)); o["estado_caso"] = "COMPONENTE_FALLA"; o["criterios"][0]["estado"] = "FALLA_COMPONENTE"
    json.dump(o, open(p, "w"))
    ex = generar(t, "generar_matriz.py", "generar_correspondencia.py", "generar_relevo.py")
    rel = json.load(open(os.path.join(t, "relevo", "PAQUETES_RELEVO.json")))
    q5 = next(x for x in rel["paquetes"] if x["caso"] == "Q1-005")
    pub = json.load(open(os.path.join(D, "relevo", "PAQUETES_RELEVO.json")))
    falta_txt = collections.Counter(f["qué"] for x in pub["paquetes"] for f in x["falta_para_caso_completo"])
    claves = sorted(set(k for x in pub["paquetes"] for k in x))
    return {"exits": ex, "Q1-005_tras_pasar_a_COMPONENTE_FALLA": {"estado": q5["estado_ejecucion"], "falta": q5["falta_para_caso_completo"]},
            "publicado_textos_de_falta_mas_repetidos": [(n, k[:90]) for k, n in falta_txt.most_common(3)],
            "publicado_claves_de_paquete": claves,
            "publicado_Q1-028_Q1-032": {x["caso"]: {"comando_relevo": x["comando_relevo"],
                                                   "paso_de_agente": any("agente" in (f["qué"] + f["quién"]) for f in x["falta_para_caso_completo"])}
                                       for x in pub["paquetes"] if x["caso"] in ("Q1-028", "Q1-032")}}


with tempfile.TemporaryDirectory() as tmp:
    for nombre, fn in (("R1_arnes", r1), ("R1_matriz", r1_matriz), ("R1_ejecutar_todo_y_M2", r1_ejecutar_todo_cierra_M2),
                       ("R2", r2), ("R3_reevaluacion_publicada", r3_reevaluar), ("R4_relevo", r4)):
        d = os.path.join(tmp, nombre); os.makedirs(d)
        try:
            res[nombre] = fn(d)
        except Exception as e:  # una sonda rota no debe ocultar las demás
            import traceback
            res[nombre] = {"excepcion": traceback.format_exc()[-1500:]}
    txt = json.dumps(res, ensure_ascii=False, indent=1)
    for a, b in ((tmp, "<tmp>"), (os.path.dirname(os.path.dirname(OUT)), "<rev_D3>"), (tempfile.gettempdir(), "<tmp>")):
        txt = txt.replace(a, b)
open(OUT, "w").write(txt)
print(txt)
