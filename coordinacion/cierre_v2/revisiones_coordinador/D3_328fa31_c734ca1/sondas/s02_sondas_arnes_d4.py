"""Sondas NUEVAS del revisor contra el arnés D v4 en c734ca1 (bloques A 328fa31 y B c734ca1).

Uso: python3 -I -B s02_sondas_arnes_d4.py <ejecucion_d @c734ca1> <banco_revisado @4745f38> <salida.json>

Todo con CANDIDATA FALSA y scripts de juguete (stubs) que imitan la interfaz del producto:
no se ejecuta Munger, ni LibreOffice, ni agentes, ni red. Mide la lógica del arnés y de la
matriz, no el producto. Las variantes de la revisión anterior (P3va, P3vb, N1a, N1b, P1v, N3,
P9w, N4, N4b, P8va, P8vb, N5a, N5b, M2, N2a, N2b, M3, P7v, P7v2) se repiten sin cambios con
sondas_arnes_d3.py (s01). Aquí va UNA variante nueva por invariante de D3-R1 y por punto.

El producto de juguete NO lee el registro de entradas y su salida de `comprobar` es constante
({"marca": "limpio"}). Por tanto, cualquier COMPONENTE_OK obtenido aquí con aserciones sobre
cifras o textos del caso se ha obtenido SIN que ninguna salida del producto los contenga.

Invariante 3 (las aserciones no leen archivos que escribe el propio arnés):
  A1 N3b  copiar_artefacto de la fuente sintética que escribe escribir_fuente
  A2 N3c  copiar_artefacto del registro que escribe poner_entrada (tautología de Q1-034)
  A3 N3d  mutar_fuente sobre un artefacto del expediente y copiar_artefacto después
  A4 P1v2 `guardar` con el nombre del log del arnés (ejecucion.log)
  A5 P7v3 preparar_cambio con guardar="origen_estado.txt" (diagnóstico del arnés)
  y si la MATRIZ v4 los certifica (CUMPLE / BLOQUEO_ENTORNO).
Invariante 1 (toda ruta dentro del caso):
  B1 N1c  entrada.fuente.archivo relativo con ../ y absoluto: el arnés lee (huella) fuera del caso
Invariante 4 (id):
  C1 id "Q1-001\\n" · C2 id "Q1-999" (no existe en el banco) · C3 spec con el id de OTRO caso
Invariante 5 (candidata limpia):
  D0 controles: P8va, P8vb, N5a, N5b con una aserción sobre salida del producto
  D1 N5c  script rastreado alterado con assume-unchanged Y skip-worktree a la vez
  D2 N5g  directorio enlazado no rastreado en scripts/ (oculto por .git/info/exclude) que suplanta un módulo
Invariante 2 / D3-R3 (matriz):
  E1 M3b  Q1-026 con un resultado de UN campo {"estado_caso": "ERROR_ENTORNO"}
  E2 M3c  Q1-026 ejecutado con la candidata SUCIA -> ERROR_ENTORNO -> ¿BLOQUEO_ENTORNO?
  E3 M7   generar_matriz ignora EVIDENCIAS_DIR
"""
import csv, hashlib, json, os, shutil, subprocess, sys, tempfile

D, BANCO, OUT = [os.path.abspath(x) for x in sys.argv[1:4]]
PY = sys.executable
res = {"alcance": "sondas con candidata falsa (stubs); no son resultados del producto Munger",
       "objeto": "c734ca1 (resultados_qwen/ejecucion_d), arnés v4"}

STUB_VE = r'''
import ast  # el producto real también lo importa (verificacion_entradas.py:86)
import json, os, sys
cmd = sys.argv[1]
if cmd == "plantilla":
    exp = sys.argv[2]
    json.dump({"entradas": [{"celda": "Historia!C23"}, {"celda": "Historia!C24"}], "perimetro_del_expediente": ""},
              open(os.path.join(exp, "verificacion_entradas.plantilla.json"), "w"))
    print("plantilla con 2 entradas"); sys.exit(0)
if cmd == "comprobar":
    # producto de juguete: NO lee el registro; su salida es constante
    print(json.dumps({"universo": 2, "comprobadas": [], "pendientes": ["Historia!C23: pendiente"], "marca": "limpio"}))
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
elif m == "ajeno":
    # el CAMBIO es inválido por un motivo AJENO al entorno; no sale ninguna de las 9 líneas reales
    sys.stderr.write("ERROR: CAMBIO inválido: analisis.C24.valor no coincide con la evidencia declarada\n")
sys.exit(1)
''' % REAL_026
AST_FALSO = r'''
# paquete "ast" falso: se importa antes que el de la biblioteca estándar porque scripts/ es sys.path[0]
import json as _j
_o = _j.dumps
def _d(o, *a, **k):
    if isinstance(o, dict) and "marca" in o:
        o = dict(o, marca="ALTERADO")
    return _o(o, *a, **k)
_j.dumps = _d
'''


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


def fila_matriz(t, cid):
    for x in csv.DictReader(open(os.path.join(t, "MATRIZ_EJECUCION.csv"), encoding="utf-8")):
        if x["id"] == cid:
            return {k: x[k] for k in ("estado_ejecucion", "veredicto_componente", "veredicto_caso", "evidencia")}


def copia_entrega(tmp, nombre):
    t = os.path.join(tmp, nombre, "resultados_qwen", "ejecucion_d")
    shutil.copytree(D, t, ignore=shutil.ignore_patterns("__pycache__"))
    return t


def matriz(t, sha_esperado=None):
    env = dict(os.environ, BANCO_DIR=BANCO, PYTHONDONTWRITEBYTECODE="1")
    if sha_esperado:
        env["SHA_CANDIDATA_ESPERADO"] = sha_esperado
    return subprocess.run([PY, "-I", "-B", os.path.join(t, "scripts", "generar_matriz.py")], env=env, capture_output=True, text=True).returncode


SPECS_INV3 = {
    "A1_N3b_copiar_artefacto_de_fuente_escrita_por_el_arnes": ("Q1-031", {"id": "Q1-031", "harness_version": "4.0", "pasos": [
        {"op": "nuevo_expediente"},
        {"op": "escribir_fuente", "nombre": "f6_031_precio.txt", "paginas": ["precio histórico 14,20 EUR (31/12/2025); capitalización 710"]},
        {"op": "copiar_artefacto", "archivo": "fuentes_sinteticas/f6_031_precio.txt", "guardar": "salida_precio.txt"}],
        "criterios": [{"id": "C1", "texto": "la salida etiqueta el precio como histórico", "afirma": [
            {"tipo": "texto_contiene", "archivo": "salida_precio.txt", "contiene": "precio histórico 14,20"}]},
            {"id": "C2", "texto": "capitalización 710 documentada", "afirma": [
            {"tipo": "texto_contiene", "archivo": "salida_precio.txt", "contiene": "710"}]}]}),
    "A2_N3c_copiar_artefacto_del_registro_escrito_por_el_arnes": ("Q1-033", {"id": "Q1-033", "harness_version": "4.0", "pasos": [
        {"op": "nuevo_expediente"},
        {"op": "entrada", "celda": "aux:litigio", "clase": "hipotesis",
         "hipotesis": {"fundamento": "Nota 12: rango acotado 0-200 millones EUR", "alternativas": [], "limites": "0-200"}},
        {"op": "copiar_artefacto", "archivo": "verificacion_entradas.json", "guardar": "registro.json"}],
        "criterios": [{"id": "C1", "texto": "el rango 0-200 queda registrado como hipótesis", "afirma": [
            {"tipo": "json_entrada_campo", "archivo": "registro.json", "celda": "aux:litigio", "ruta": "clase", "op": "eq", "valor": "hipotesis"},
            {"tipo": "json_entrada_campo", "archivo": "registro.json", "celda": "aux:litigio", "ruta": "hipotesis.fundamento", "op": "contiene", "valor": "0-200"}]}]}),
    "A3_N3d_mutar_fuente_sobre_artefacto_y_copiar_artefacto": ("Q1-032", {"id": "Q1-032", "harness_version": "4.0", "pasos": [
        {"op": "nuevo_expediente"},
        {"op": "informe", "args": ["--provisional"], "guardar": "06_informe.txt", "esperado": [0]},
        {"op": "mutar_fuente", "archivo": "informe_provisional.md", "paginas": ["Matriz parcial: 4 verificadas / 1 pendiente / 5 total. Valoración NO admisible."]},
        {"op": "copiar_artefacto", "archivo": "informe_provisional.md", "guardar": "07_informe_provisional.md"}],
        "criterios": [{"id": "C1", "texto": "la matriz parcial muestra 4/1/5", "afirma": [
            {"tipo": "texto_contiene", "archivo": "07_informe_provisional.md", "contiene": "4 verificadas / 1 pendiente / 5 total"}]}]}),
    "A4_P1v2_guardar_con_el_nombre_del_log_del_arnes": ("Q1-028", {"id": "Q1-028", "harness_version": "4.0", "pasos": [
        {"op": "nuevo_expediente"},
        {"op": "comprobar", "guardar": "ejecucion.log", "esperado": [0, 1]},
        {"op": "escribir_fuente", "nombre": "deuda neta vigente 300+40-95=245 pendiente de verificar.txt", "paginas": ["x"]}],
        "criterios": [{"id": "C1", "texto": "la deuda neta vigente 245 queda documentada", "afirma": [
            {"tipo": "texto_contiene", "archivo": "ejecucion.log", "contiene": "300+40-95=245 pendiente de verificar"}]}]}),
}


def inv3(tmp):
    """Invariante 3 + matriz: se instalan como especificaciones de casos SIN spec publicada
    (Q1-028/031/032/033), se ejecutan con el arnés v4 y se genera la MATRIZ v4."""
    out = {}
    cand, sha, plantilla = candidata(tmp)
    t = copia_entrega(tmp, "inv3")
    base = {"CANDIDATA_DIR": cand, "SHA_CANDIDATA_ESPERADO": sha, "PLANTILLA_EXP": plantilla, "RUN_DIR": os.path.join(tmp, "run_inv3")}
    for nombre, (cid, spec) in SPECS_INV3.items():
        sp = os.path.join(t, "scripts", "especificaciones", "bloque2", cid + ".json")
        json.dump(spec, open(sp, "w"), ensure_ascii=False)
        r = correr(t, sp, base)
        rr = resultado(os.path.join(t, "evidencias"), cid)
        out[nombre] = {"caso": cid, "exit": r.returncode, "estado": rr and rr["estado_caso"], "criterios": crit(rr),
                       "errores": rr and rr["errores"], "archivos_producto_segun_el_arnes": rr and rr.get("archivos_producto")}
    # A5: Q1-026 con el diagnóstico del arnés (origen_estado.txt) como "salida del producto" y un fallo AJENO al entorno
    q026 = json.load(open(os.path.join(t, "scripts", "especificaciones", "bloque2", "Q1-026.json"), encoding="utf-8"))
    q026["pasos"][0]["guardar"] = "origen_estado.txt"
    q026["criterios"] = [{"id": "C1", "texto": "bloqueo de entorno: el origen queda intacto", "afirma": [
        {"tipo": "texto_contiene", "archivo": "origen_estado.txt", "contiene": "intacto=true"}]}]
    sp = os.path.join(t, "scripts", "especificaciones", "bloque2", "Q1-026.json")
    json.dump(q026, open(sp, "w"), ensure_ascii=False)
    r = correr(t, sp, {**base, "STUB_CAMBIAR": "ajeno"})
    rr = resultado(os.path.join(t, "evidencias"), "Q1-026")
    eb = json.load(open(os.path.join(t, "evidencias", "Q1-026", "errores_bloqueo.json")))
    out["A5_P7v3_preparar_cambio_guardar=origen_estado.txt_con_fallo_ajeno"] = {
        "caso": "Q1-026", "exit": r.returncode, "estado": rr and rr["estado_caso"], "criterios": crit(rr),
        "stderr_del_producto_de_juguete": eb["otros_errores"], "lineas_de_texto_PDF_ausente": eb["texto_pdf_faltante_pdftotext"],
        "archivos_producto_segun_el_arnes": rr and rr.get("archivos_producto")}
    ex = matriz(t, sha)
    out["MATRIZ_v4_sobre_estas_especificaciones"] = {"exit": ex, **{cid: fila_matriz(t, cid) for cid in ("Q1-031", "Q1-033", "Q1-032", "Q1-028", "Q1-026")}}
    for k, v in out.items():
        if k.startswith("A") and isinstance(v, dict):
            fm = out["MATRIZ_v4_sobre_estas_especificaciones"].get(v["caso"]) or {}
            abierto = v["estado"] == "COMPONENTE_OK"
            v["matriz"] = fm.get("estado_ejecucion"), fm.get("veredicto_componente")
            v["veredicto"] = ("ABIERTO: COMPONENTE_OK sin que ninguna salida del producto contenga lo asertado; matriz = "
                              + str(v["matriz"])) if abierto else "CERRADO"
    return out


def inv1(tmp):
    out = {}
    cand, sha, plantilla = candidata(tmp)
    rd = os.path.join(tmp, "run_n1c")
    ajena = os.path.join(rd, "Q1-036", "Viscofan", "fuentes_sinteticas")
    os.makedirs(ajena)
    open(os.path.join(ajena, "ajena.txt"), "w").write("[PDF PAGE 1]\nfuente del caso Q1-036: capitalización 710\n")
    absoluta = os.path.join(tmp, "fuera_de_todo.txt")
    open(absoluta, "w").write("[PDF PAGE 1]\narchivo fuera de RUN_DIR: 710\n")
    for nombre, ruta in (("B1a_N1c_entrada_fuente_archivo_../../Q1-036", "../../Q1-036/Viscofan/fuentes_sinteticas/ajena.txt"),
                         ("B1b_N1c_entrada_fuente_archivo_absoluto", absoluta)):
        sp = spec_tmp(tmp, nombre[:3] + ".json", {"id": "Q1-031", "harness_version": "4.0", "pasos": [
            {"op": "nuevo_expediente"},
            {"op": "entrada", "celda": "aux:capitalizacion", "clase": "dato_publicado", "valor_modelo": 710,
             "fuente": {"documento": "fuente de otro caso", "archivo": ruta, "pagina": 1, "valor_fuente": 710, "cita": "710"},
             "comprobacion": "verificada"},
            {"op": "comprobar", "guardar": "01.json", "esperado": [0, 1]}],
            "criterios": [{"id": "C1", "texto": "x", "afirma": [{"tipo": "archivo_existe", "archivo": "01.json"}]}]})
        ev = os.path.join(tmp, "ev_" + nombre[:3])
        r = correr(D, sp, {"CANDIDATA_DIR": cand, "SHA_CANDIDATA_ESPERADO": sha, "PLANTILLA_EXP": plantilla, "EVIDENCIAS_DIR": ev, "RUN_DIR": rd})
        rr = resultado(ev, "Q1-031")
        reg = json.load(open(os.path.join(rd, "Q1-031", "Viscofan", "verificacion_entradas.json")))
        e = next(x for x in reg["entradas"] if x["celda"] == "aux:capitalizacion")
        ajeno = os.path.join(ajena, "ajena.txt") if "../" in ruta else absoluta
        leido = e["fuente"].get("sha256") == sha256(ajeno)
        out[nombre] = {"exit": r.returncode, "estado": rr["estado_caso"], "errores": rr["errores"],
                       "huella_del_archivo_ajeno_escrita_en_el_registro": leido,
                       "fuente_examinada_en_el_registro": e["comprobacion"]["fuente_examinada"].replace(tmp, "<tmp>"),
                       "veredicto": "ABIERTO (el arnés lee fuera del caso sin ERROR)" if leido and not rr["errores"] else "CERRADO"}
    return out


def inv4(tmp):
    out = {}
    cand, sha, plantilla = candidata(tmp)
    base = {"CANDIDATA_DIR": cand, "SHA_CANDIDATA_ESPERADO": sha, "PLANTILLA_EXP": plantilla}
    minimo = {"harness_version": "4.0", "pasos": [{"op": "nuevo_expediente"}, {"op": "comprobar", "guardar": "01.json", "esperado": [0, 1]}],
              "criterios": [{"id": "C1", "texto": "x", "afirma": [{"tipo": "archivo_existe", "archivo": "01.json"}]}]}
    for nombre, cid in (("C1_id_con_salto_de_linea_final", "Q1-001\n"), ("C2_id_Q1-999_inexistente_en_el_banco", "Q1-999"),
                        ("C2b_id_con_digitos_no_ASCII", "Q1-٠٠١")):
        ev = os.path.join(tmp, "ev_" + nombre[:3])
        os.makedirs(ev)
        r = correr(D, spec_tmp(tmp, nombre[:3] + ".json", {"id": cid, **minimo}), {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(tmp, "run_" + nombre[:3])})
        out[nombre] = {"id": cid, "exit": r.returncode, "carpetas_creadas_en_EVIDENCIAS": sorted(os.listdir(ev)),
                       "hay_resultado_ejecucion": any(os.path.isfile(os.path.join(ev, d, "resultado_ejecucion.json")) for d in os.listdir(ev)),
                       "ultima_linea_stderr": (r.stderr.strip().splitlines() or [""])[-1][:120],
                       "veredicto": "id aceptado por la validación; el caso termina con traza y sin resultado" if r.returncode not in (0, 2) else
                                    ("id rechazado antes de tocar el disco" if r.returncode == 2 and not os.listdir(ev) else "id aceptado")}
    # C3: una especificación con el id de OTRO caso borra la evidencia de ese caso
    ev = os.path.join(tmp, "ev_c3")
    os.makedirs(os.path.join(ev, "Q1-001"))
    open(os.path.join(ev, "Q1-001", "03_comprobar_sellado.json"), "w").write('{"evidencia": "de Q1-001"}')
    sp = spec_tmp(tmp, "Q1-031.json", {"id": "Q1-001", **minimo})
    r = correr(D, sp, {**base, "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(tmp, "run_c3")})
    out["C3_archivo_Q1-031.json_con_id_Q1-001"] = {"exit": r.returncode, "evidencia_previa_de_Q1-001_sobrevive": os.path.isfile(os.path.join(ev, "Q1-001", "03_comprobar_sellado.json")),
                                                 "veredicto": "límite: no se comprueba que el id coincida con el nombre de la especificación"}
    return out


def inv5(tmp):
    out = {}
    rel = "munger_v2_r1/personaje_v2/scripts/verificacion_entradas.py"
    sp = spec_tmp(tmp, "cand.json", {"id": "Q1-031", "harness_version": "4.0", "pasos": [
        {"op": "nuevo_expediente"}, {"op": "comprobar", "guardar": "01.json", "esperado": [0, 1]}],
        "criterios": [{"id": "C1", "texto": "solo se cumple si la salida del producto está ALTERADA", "afirma": [
            {"tipo": "json_campo", "archivo": "01.json", "ruta": "marca", "op": "eq", "valor": "ALTERADO"}]}]})

    def cand_alterada(nombre, prepara):
        c, s, pl = candidata(tmp, nombre)
        prepara(c)
        ev = os.path.join(tmp, "ev_" + nombre)
        r = correr(D, sp, {"CANDIDATA_DIR": c, "SHA_CANDIDATA_ESPERADO": s, "PLANTILLA_EXP": pl,
                           "EVIDENCIAS_DIR": ev, "RUN_DIR": os.path.join(tmp, "run_" + nombre)})
        rr = resultado(ev, "Q1-031")
        salida = os.path.join(ev, "Q1-031", "01.json")
        return {"exit": r.returncode, "estado": rr["estado_caso"], "criterios": crit(rr), "errores": [e[:110] for e in rr["errores"]],
                "candidata_no_rastreadas": rr.get("candidata_no_rastreadas"),
                "git_status": subprocess.run(["git", "-C", c, "status", "--porcelain"], capture_output=True, text=True).stdout.strip(),
                "git_ls_files_v": subprocess.run(["git", "-C", c, "ls-files", "-v", "--", rel], capture_output=True, text=True).stdout.strip(),
                "marca_en_la_salida_del_producto": json.load(open(salida)).get("marca") if os.path.isfile(salida) else None,
                "veredicto": "ABIERTO (candidata alterada pasa como limpia y la alteración decide el CUMPLE)" if rr["estado_caso"] == "COMPONENTE_OK"
                             else ("CERRADO (ERROR_ENTORNO)" if rr["estado_caso"] == "ERROR_ENTORNO" else "sin alteración efectiva: " + rr["estado_caso"])}

    def alterar(c, *flags):
        for fl in flags:
            git(c, "update-index", fl, rel)
        p = os.path.join(c, rel)
        t = open(p).read()
        open(p, "w").write(t.replace('"marca": "limpio"', '"marca": "ALTERADO"'))

    def no_rastreado(c, excluir):
        if excluir:
            open(os.path.join(c, ".git", "info", "exclude"), "a").write("\nast_local.py\n")
        # archivo suelto no rastreado: no altera nada por sí mismo; mide solo la detección
        open(os.path.join(c, "munger_v2_r1/personaje_v2/scripts/ast_local.py"), "w").write("# no rastreado\n")

    def enlace_a_directorio(c):
        falso = os.path.join(tmp, "ast_falso_" + os.path.basename(c))
        os.makedirs(falso)
        open(os.path.join(falso, "__init__.py"), "w").write(AST_FALSO)
        os.symlink(falso, os.path.join(c, "munger_v2_r1/personaje_v2/scripts/ast"))
        open(os.path.join(c, ".git", "info", "exclude"), "a").write("\nast\n")

    out["D0_control_candidata_intacta"] = cand_alterada("d0", lambda c: None)
    out["D0a_P8va_skip_worktree"] = cand_alterada("d0a", lambda c: alterar(c, "--skip-worktree"))
    out["D0b_N5a_assume_unchanged"] = cand_alterada("d0b", lambda c: alterar(c, "--assume-unchanged"))
    out["D0c_P8vb_archivo_no_rastreado"] = cand_alterada("d0c", lambda c: no_rastreado(c, False))
    out["D0d_N5b_archivo_no_rastreado_oculto_por_exclude"] = cand_alterada("d0d", lambda c: no_rastreado(c, True))
    out["D1_N5c_assume_unchanged_Y_skip_worktree (nueva)"] = cand_alterada("d1", lambda c: alterar(c, "--assume-unchanged", "--skip-worktree"))
    out["D2_N5g_directorio_enlazado_no_rastreado_oculto_por_exclude (nueva)"] = cand_alterada("d2", enlace_a_directorio)
    return out


def matriz_q026(tmp):
    out = {}
    cand, sha, plantilla = candidata(tmp)
    # E1: resultado de UN campo
    t = copia_entrega(tmp, "e1")
    json.dump({"estado_caso": "ERROR_ENTORNO"}, open(os.path.join(t, "evidencias", "Q1-026", "resultado_ejecucion.json"), "w"))
    ex = matriz(t)
    out["E1_M3b_Q1-026_resultado_de_un_campo_ERROR_ENTORNO"] = {"exit": ex, **fila_matriz(t, "Q1-026")}
    # E2: Q1-026 publicado, ejecutado con una candidata SUCIA (archivo no rastreado en scripts/)
    t = copia_entrega(tmp, "e2")
    c2, s2, pl2 = candidata(tmp, "cand_sucia")
    open(os.path.join(c2, "munger_v2_r1/personaje_v2/scripts/override.txt"), "w").write("candidata sucia")
    r = correr(t, os.path.join(t, "scripts", "especificaciones", "bloque2", "Q1-026.json"),
               {"CANDIDATA_DIR": c2, "SHA_CANDIDATA_ESPERADO": s2, "PLANTILLA_EXP": pl2, "RUN_DIR": os.path.join(tmp, "run_e2")})
    rr = resultado(os.path.join(t, "evidencias"), "Q1-026")
    ex = matriz(t, s2)
    out["E2_M3c_Q1-026_ejecutado_con_candidata_sucia"] = {"ejecutar_caso_exit": r.returncode, "estado": rr["estado_caso"],
                                                          "errores": [e[:140] for e in rr["errores"]], "matriz": fila_matriz(t, "Q1-026")}
    # E3: generar_matriz ignora EVIDENCIAS_DIR
    t = copia_entrega(tmp, "e3")
    ev_otro = os.path.join(tmp, "ev_del_coordinador")
    r = correr(t, os.path.join(t, "scripts", "especificaciones", "piloto", "Q1-001.json"),
               {"CANDIDATA_DIR": cand, "SHA_CANDIDATA_ESPERADO": sha, "PLANTILLA_EXP": plantilla, "RUN_DIR": os.path.join(tmp, "run_e3"), "EVIDENCIAS_DIR": ev_otro})
    rr = resultado(ev_otro, "Q1-001")
    env = dict(os.environ, BANCO_DIR=BANCO, PYTHONDONTWRITEBYTECODE="1", EVIDENCIAS_DIR=ev_otro)
    ex = subprocess.run([PY, "-I", "-B", os.path.join(t, "scripts", "generar_matriz.py")], env=env, capture_output=True, text=True).returncode
    out["E3_M7_generar_matriz_ignora_EVIDENCIAS_DIR"] = {
        "ejecutar_caso_con_EVIDENCIAS_DIR_propio": {"exit": r.returncode, "estado": rr["estado_caso"] if rr else "sin resultado (traza): " + (r.stderr.strip().splitlines() or [""])[-1][:100]},
        "generar_matriz_con_el_mismo_EVIDENCIAS_DIR": {"exit": ex, **{k: v for k, v in fila_matriz(t, "Q1-001").items() if k != "veredicto_caso"}},
        "veredicto": "la matriz lee siempre <ejecucion_d>/evidencias: tras reejecutar con EVIDENCIAS_DIR propio muestra el CUMPLE publicado, no el resultado nuevo"}
    return out


os.makedirs(os.environ.get("TMPDIR", tempfile.gettempdir()), exist_ok=True)
with tempfile.TemporaryDirectory() as tmp:
    for nombre, fn in (("INV3_aserciones_sobre_archivos_del_arnes", inv3), ("INV1_rutas", inv1), ("INV4_id", inv4),
                       ("INV5_candidata_limpia", inv5), ("INV2_R3_matriz", matriz_q026)):
        d = os.path.join(tmp, nombre); os.makedirs(d)
        try:
            res[nombre] = fn(d)
        except Exception:  # una sonda rota no debe ocultar las demás
            import traceback
            res[nombre] = {"excepcion": traceback.format_exc()[-1800:]}
    txt = json.dumps(res, ensure_ascii=False, indent=1)
    for a, b in ((tmp, "<tmp>"), (os.path.dirname(os.path.dirname(OUT)), "<rev_D3>"), (tempfile.gettempdir(), "<tmp>")):
        txt = txt.replace(a, b)
open(OUT, "w").write(txt)
print(txt)
