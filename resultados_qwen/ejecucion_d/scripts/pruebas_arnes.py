#!/usr/bin/env python3
"""Pruebas del propio arnés v4 (D3-R1/R2/R7): el arnés debe detectar sus fallos.

1-2. positivo/negativo reales (Q1-001, Q1-006)
3. candidata incompleta -> rc 2 ERROR_ENTORNO
4. artefacto heredado tras fallo -> detectado, NO copiado
5. matriz sin carpeta de evidencias -> rc 0, 36 filas, 0 CUMPLE
6. resultado mutado -> aserción FALLA
7. recuentos == CSV (fuente única)
8-9. D2-R1: spec vacía / criterio sin afirma -> rc 2
10. D2/D3-R1: ruta ../ en aserción -> rc!=0
11. D2-R1e: negativo sin universo -> FALLA
12. D2-R1d: resultado forjado de 2 campos -> sin CUMPLE
13. D3-R1 inv.5: rastreado modificado -> rc 2
14. D2-R7b: un log por ejecución
15. D2-R2: control negativo en vacío (todas las aserciones fallan)
16. D2-R7a: marcas SIMULADA en registros del arnés
17. P3va: copiar_artefacto ../../Q1-036 -> rc!=0, no copia
18. P3vb: guardar ../Q1-036/... -> víctima intacta, rc!=0
19. N1a: escribir_fuente ../../../Q1-036 -> registro ajeno intacto
20. N1b: copiar_artefacto con ruta absoluta -> rc!=0
21. P1v: aserción sobre ejecucion.log (archivo del arnés) -> rc!=0
22. N3: aserción run: -> rc!=0 (no soportado)
23. P9w: id "." -> rc 2 SIN borrar la evidencia de otros casos
24. N4: id "../fuera" -> rc 2 SIN borrar fuera de EVIDENCIAS
25. N4b: id "" -> rc 2 SIN borrar EVIDENCIAS
26. P8va: skip-worktree -> rc 2
27. P8vb: no rastreado en scripts/ -> rc 2
28. N5a: assume-unchanged -> rc 2
29. N5b: oculto por .git/info/exclude -> rc 2
30. M2: resultado de 4 campos con spec_sha256 -> generar_matriz sola: sin CUMPLE
31. N2a: salidas del producto vaciadas -> sin CUMPLE
32. N2b: candidata/banco ajenos + harness 2.0 -> sin CUMPLE
33. M3: Q1-026 con ERROR_ENTORNO -> BLOQUEO_ENTORNO desde el resultado
34. D3-R2: control negativo contra el ESTADO PREVIO (quitando los archivos del paso
    que produce el archivo leído y posteriores): toda aserción falla salvo las
    marcadas no_discriminante
35. D3-R7: sellar con --revisor propio sin marca -> queda [SIMULADO]; ARNES_EVIDENCIAS_LIMPIAS=0 -> flag registrado
36. D3-R4: cada paquete de relevo tiene estado_inicial, fases, entrada, artefacto por
    criterio y comando_relevo ejecutable (o motivo explícito)

Uso: python3 pruebas_arnes.py   (exit 0 solo si todas PASA; log en evidencias/pruebas_arnes.log)
"""
import csv
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import lib_arnes as L  # noqa: E402

RESULTADOS = []


def paso(nombre, ok, detalle=""):
    RESULTADOS.append({"prueba": nombre, "ok": bool(ok), "detalle": str(detalle)[:400]})
    print(("PASA " if ok else "FALLA ") + "· " + nombre + (f" · {str(detalle)[:240]}" if detalle else ""))


def run_caso(spec, env_extra):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", **env_extra)
    return subprocess.run([sys.executable, "-B", os.path.join(AQUI, "ejecutar_caso.py"), spec],
                          capture_output=True, text=True, env=env)


def spec_tmp(tmp, nombre, obj):
    p = os.path.join(tmp, nombre)
    json.dump(obj, open(p, "w", encoding="utf-8"), ensure_ascii=False)
    return p


def resultado(ev, cid):
    p = os.path.join(ev, cid, "resultado_ejecucion.json")
    return json.load(open(p, encoding="utf-8")) if os.path.isfile(p) else None


def candidata_falsa(tmp, nombre="cand"):
    cand = os.path.join(tmp, nombre)
    sc = os.path.join(cand, "munger_v2_r1", "personaje_v2", "scripts")
    os.makedirs(sc)
    shutil.copytree(os.path.join(L.PERSONAJE, "scripts"), sc)
    subprocess.run(["git", "-C", cand, "init", "-q"], check=True)
    subprocess.run(["git", "-C", cand, "add", "-A"], check=True)
    subprocess.run(["git", "-C", cand, "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "x"], check=True)
    sha = subprocess.run(["git", "-C", cand, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    pl = os.path.join(tmp, nombre + "_pl")
    os.makedirs(pl)
    open(os.path.join(pl, "fase1_v63.json"), "w").write('{"origen": "plantilla"}')
    return cand, sha, pl


def main():
    tmp = tempfile.mkdtemp(prefix="pruebas_arnes_v4_")
    ev = os.path.join(tmp, "evidencias")
    run_dir = os.path.join(tmp, "run")
    os.makedirs(ev)
    base_env = {"EVIDENCIAS_DIR": ev, "RUN_DIR": run_dir}
    spec_001 = os.path.join(AQUI, "especificaciones", "piloto", "Q1-001.json")
    spec_006 = os.path.join(AQUI, "especificaciones", "piloto", "Q1-006.json")
    spec_002 = os.path.join(AQUI, "especificaciones", "bloque2", "Q1-002.json")

    r = run_caso(spec_001, base_env)
    res = resultado(ev, "Q1-001")
    paso("1 positivo real Q1-001 (COMPONENTE_OK, sha observado, spec_sha256)",
         r.returncode == 0 and res["estado_caso"] == "COMPONENTE_OK"
         and all(c["estado"] == "CUMPLE_COMPONENTE" for c in res["criterios"])
         and res.get("candidata_sha") == L.SHA_CANDIDATA_ESPERADO and res.get("spec_sha256"),
         f"rc={r.returncode}")

    r = run_caso(spec_006, base_env)
    res6 = resultado(ev, "Q1-006")
    sellar = [p for p in res6["pasos"] if "sellar" in p.get("descripcion", "")]
    paso("2 negativo esperado real Q1-006 (sellar exit 1 en esperado)",
         r.returncode == 0 and res6["estado_caso"] == "COMPONENTE_OK"
         and any(p.get("exit") == 1 and not p.get("error_inesperado") for p in sellar), f"rc={r.returncode}")

    empty = os.path.join(tmp, "cand_vacia")
    os.makedirs(empty)
    r = run_caso(spec_001, {**base_env, "CANDIDATA_DIR": empty})
    res3 = resultado(ev, "Q1-001") or {}
    paso("3 candidata incompleta -> rc 2 ERROR_ENTORNO",
         r.returncode == 2 and res3.get("estado_caso") == "ERROR_ENTORNO", f"rc={r.returncode} estado={res3.get('estado_caso')}")

    fake, sha_fake, pl_fake = candidata_falsa(tmp, "cand_fake")
    cfgp = os.path.join(fake, "munger_v2_r1", "personaje_v2", "config_v2_v641_experimental.json")
    if os.path.isfile(cfgp):
        cfg = json.load(open(cfgp, encoding="utf-8"))
        cfg["plantilla"]["archivo"] = "../v6/v641_experimental/entregables/NO_EXISTE.xlsx"
        json.dump(cfg, open(cfgp, "w", encoding="utf-8"))
        subprocess.run(["git", "-C", fake, "add", "-A"], check=True)
        subprocess.run(["git", "-C", fake, "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "cfg rota"], check=True)
        sha_fake = subprocess.run(["git", "-C", fake, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    spec_obs = spec_tmp(tmp, "obsoleto.json", {"id": "Q1-036", "harness_version": "4.0", "pasos": [
        {"op": "nuevo_expediente"},
        {"op": "ficha", "args": ["--estado", "concluido", "--provisional"], "guardar": "ficha.txt", "esperado": [0]},
        {"op": "copiar_artefacto", "archivo": "ficha_provisional.json", "guardar": "ficha_copia.json"}],
        "criterios": [{"id": "C1", "texto": "x", "afirma": [{"tipo": "archivo_existe", "archivo": "ficha_copia.json"}]}]})
    r = run_caso(spec_obs, {**base_env, "CANDIDATA_DIR": fake, "SHA_CANDIDATA_ESPERADO": sha_fake, "PLANTILLA_EXP": pl_fake})
    res4 = resultado(ev, "Q1-036")
    copiado = os.path.isfile(os.path.join(ev, "Q1-036", "ficha_copia.json"))
    paso("4 artefacto heredado tras fallo -> detectado, NO copiado",
         r.returncode != 0 and res4["estado_caso"] == "ERROR" and not copiado,
         f"rc={r.returncode} estado={res4['estado_caso']} copiado={copiado}")

    aux_tmp = os.path.join(tmp, "aux")
    os.makedirs(os.path.join(aux_tmp, "scripts", "especificaciones"))
    shutil.copy(os.path.join(AQUI, "generar_matriz.py"), os.path.join(aux_tmp, "scripts", "generar_matriz.py"))
    shutil.copy(os.path.join(AQUI, "especificaciones", "adaptaciones.json"),
                os.path.join(aux_tmp, "scripts", "especificaciones", "adaptaciones.json"))
    r5 = subprocess.run([sys.executable, "-B", os.path.join(aux_tmp, "scripts", "generar_matriz.py")],
                        capture_output=True, text=True,
                        env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", BANCO_DIR=L.BANCO))
    filas = list(csv.DictReader(open(os.path.join(aux_tmp, "MATRIZ_EJECUCION.csv"), encoding="utf-8")))
    rec5 = json.load(open(os.path.join(aux_tmp, "evidencias", "recuentos.json")))
    paso("5 matriz sin carpeta de evidencias -> rc 0, 36 filas, 0 CUMPLE",
         r5.returncode == 0 and len(filas) == 36 and rec5.get("con_ejecucion_propia") == 0
         and all(rr["veredicto_componente"] == "" for rr in filas), f"rc={r5.returncode} filas={len(filas)}")

    import ejecutar_caso as EC
    run_caso(spec_001, base_env)
    p6 = os.path.join(ev, "Q1-001", "03_comprobar_sellado.json")
    obj = json.load(open(p6, encoding="utf-8"))
    obj["comprobadas"] = [x for x in obj["comprobadas"] if x != "Historia!C23"]
    json.dump(obj, open(p6, "w", encoding="utf-8"))
    spec = json.load(open(spec_001, encoding="utf-8"))
    caso_fake = L.Caso.__new__(L.Caso)
    caso_fake.id = "Q1-001"
    caso_fake.ev_dir = os.path.join(ev, "Q1-001")
    caso_fake.errores = []
    caso_fake.archivos_producto = set(resultado(ev, "Q1-001").get("archivos_producto") or [])
    ok, detalle = EC.evaluar_afirmacion(caso_fake, spec["criterios"][0]["afirma"][0])
    paso("6 resultado mutado -> aserción FALLA detectada", ok is False, detalle)

    subprocess.run([sys.executable, "-B", os.path.join(AQUI, "generar_matriz.py")],
                   capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    rec = json.load(open(os.path.join(L.EVIDENCIAS, "recuentos.json")))
    filas = list(csv.DictReader(open(os.path.join(L.AUX, "MATRIZ_EJECUCION.csv"), encoding="utf-8")))
    import collections
    est_csv = dict(collections.Counter(r["estado_ejecucion"] for r in filas))
    vc_csv = dict(collections.Counter(r["veredicto_caso"].split(" (")[0] for r in filas))
    paso("7 recuentos == CSV (fuente única)", rec["estado_ejecucion"] == est_csv and rec["veredicto_caso"] == vc_csv,
         f"estados={est_csv}")

    # 8-11 D2-R1 literales
    r = run_caso(spec_tmp(tmp, "p1.json", {"id": "Q1-031", "harness_version": "4.0", "pasos": [], "criterios": []}), base_env)
    paso("8 spec vacía -> rc 2 ERROR_ESPECIFICACION",
         r.returncode == 2 and resultado(ev, "Q1-031")["estado_caso"] == "ERROR_ESPECIFICACION", f"rc={r.returncode}")
    r = run_caso(spec_tmp(tmp, "p2.json", {"id": "Q1-033", "harness_version": "4.0", "pasos": [{"op": "nuevo_expediente"}],
                                           "criterios": [{"id": "C1", "texto": "x", "afirma": []}]}), base_env)
    paso("9 criterio sin afirma -> rc 2", r.returncode == 2, f"rc={r.returncode}")
    sp = spec_tmp(tmp, "p3.json", {"id": "Q1-032", "harness_version": "4.0", "pasos": [{"op": "nuevo_expediente"}],
                                   "criterios": [{"id": "C1", "texto": "x", "afirma": [
                                       {"tipo": "texto_contiene", "archivo": "../Q1-036/07_informe_provisional.md", "contiene": "x"}]}]})
    r = run_caso(sp, base_env)
    res_p3 = resultado(ev, "Q1-032")
    paso("10 aserción con ruta ../ -> rc!=0 y error registrado",
         r.returncode != 0 and any("fuera" in e for e in res_p3["errores"]), f"rc={r.returncode} errores={res_p3['errores']}")
    caso11 = L.Caso.__new__(L.Caso)
    caso11.id = "P5"; caso11.ev_dir = os.path.join(tmp, "ev_p5"); caso11.errores = []
    caso11.archivos_producto = {"salida.json"}
    os.makedirs(caso11.ev_dir, exist_ok=True)
    json.dump({"comprobadas": [], "pendientes": ["x"]}, open(os.path.join(caso11.ev_dir, "salida.json"), "w"))
    ok, detalle = EC.evaluar_afirmacion(caso11, {"tipo": "json_lista_no_contiene", "archivo": "salida.json", "lista": "comprobadas", "prefijo": "aux:litigio"})
    paso("11 negativo sin universo -> FALLA", ok is False, detalle)

    # 12 forjado de 2 campos
    t = os.path.join(tmp, "p4")
    os.makedirs(os.path.join(t, "scripts", "especificaciones"))
    os.makedirs(os.path.join(t, "evidencias", "Q1-031"))
    for s in ("generar_matriz.py",):
        shutil.copy(os.path.join(AQUI, s), os.path.join(t, "scripts", s))
    shutil.copytree(os.path.join(AQUI, "especificaciones"), os.path.join(t, "scripts", "especificaciones"))
    json.dump({"harness_version": "4.0", "estado_caso": "COMPONENTE_OK"},
              open(os.path.join(t, "evidencias", "Q1-031", "resultado_ejecucion.json"), "w"))
    subprocess.run([sys.executable, "-B", os.path.join(t, "scripts", "generar_matriz.py")],
                   env=dict(os.environ, BANCO_DIR=L.BANCO), capture_output=True, text=True)
    fila = next(x for x in csv.DictReader(open(os.path.join(t, "MATRIZ_EJECUCION.csv"))) if x["id"] == "Q1-031")
    paso("12 resultado forjado de 2 campos -> sin CUMPLE", fila["veredicto_componente"] == "", f"veredicto={fila['veredicto_componente']!r}")

    # 13 rastreado modificado
    cand13, sha13, pl13 = candidata_falsa(tmp, "cand13")
    with open(os.path.join(cand13, "munger_v2_r1/personaje_v2/scripts/verificacion_entradas.py"), "a") as f:
        f.write("\n# sin commit\n")
    sp8 = spec_tmp(tmp, "p8.json", {"id": "Q1-031", "harness_version": "4.0", "pasos": [{"op": "nuevo_expediente"}],
                                    "criterios": [{"id": "C1", "texto": "x", "afirma": [{"tipo": "texto_contiene", "archivo": "ejecucion.log", "contiene": "x"}]}]})
    r = run_caso(sp8, {**base_env, "CANDIDATA_DIR": cand13, "SHA_CANDIDATA_ESPERADO": sha13, "PLANTILLA_EXP": pl13})
    res8 = resultado(ev, "Q1-031")
    paso("13 rastreado modificado -> rc 2 ERROR_ENTORNO",
         r.returncode == 2 and res8["estado_caso"] == "ERROR_ENTORNO", f"rc={r.returncode}")

    run_caso(spec_001, base_env)
    run_caso(spec_001, base_env)
    n = open(os.path.join(ev, "Q1-001", "ejecucion.log")).read().count("# Caso Q1-001")
    paso("14 una ejecución = un log (Q1-001 dos veces -> 1 '# Caso')", n == 1, f"n={n}")

    # 15 control negativo en vacío
    run_dir_real = L.RUN_DIR
    L.RUN_DIR = os.path.join(tmp, "run_vacio")
    mal = []
    for spath in sorted(glob.glob(os.path.join(AQUI, "especificaciones", "*", "Q1-*.json"))):
        s = json.load(open(spath, encoding="utf-8"))
        c = L.Caso.__new__(L.Caso)
        c.id = s["id"]; c.ev_dir = os.path.join(tmp, "ev_vacio", s["id"]); c.errores = []
        c.archivos_producto = {"x.json"}
        os.makedirs(c.ev_dir, exist_ok=True)
        os.makedirs(os.path.join(L.RUN_DIR, s["id"]), exist_ok=True)
        for crit in s.get("criterios", []):
            for a in crit.get("afirma", []):
                if EC.evaluar_afirmacion(c, a)[0]:
                    mal.append(f"{s['id']} {crit['id']} {a['archivo']}")
    L.RUN_DIR = run_dir_real
    paso("15 control negativo en vacío: todas las aserciones fallan", not mal, f"pasan={mal[:3]}")

    # 16 marcas SIMULADA
    run_caso(spec_002, base_env)
    regs = []
    for cid in ("Q1-001", "Q1-002"):
        p = os.path.join(run_dir, cid, "Viscofan", "verificacion_entradas.json")
        regs.append(json.load(open(p, encoding="utf-8")) if os.path.isfile(p) else None)
    marcadas = all(r and all((e.get("comprobacion") or {}).get("_simulada") is True
                             for e in r["entradas"] if isinstance(e.get("comprobacion"), dict))
                       for r in regs if r) if any(regs) else False
    revisor_sim = any(r and any("[SIMULADO]" in str((e.get("comprobacion") or {}).get("revisor") or "")
                                for e in r["entradas"]) for r in regs if r)
    paso("16 toda comprobación del arnés marcada _simulada/[SIMULADO] (incl. --revisor)",
         bool(marcadas) and revisor_sim, f"marcadas={marcadas} revisor_sim={revisor_sim}")

    # 17-22 variantes D3-R1 de rutas eLectura
    cand, sha, pl = candidata_falsa(tmp, "cand_r1")
    b = {"CANDIDATA_DIR": cand, "SHA_CANDIDATA_ESPERADO": sha, "PLANTILLA_EXP": pl}
    rd = os.path.join(tmp, "run_p3va")
    os.makedirs(os.path.join(rd, "Q1-036", "Viscofan"))
    open(os.path.join(rd, "Q1-036", "Viscofan", "informe_provisional.md"), "w").write("SALIDA Q1-036\n4/1/5\n")
    sp = spec_tmp(tmp, "p3va.json", {"id": "Q1-032", "harness_version": "4.0", "pasos": [
        {"op": "nuevo_expediente"},
        {"op": "copiar_artefacto", "archivo": "../../Q1-036/Viscofan/informe_provisional.md", "guardar": "informe_propio.md"}],
        "criterios": [{"id": "C1", "texto": "x", "afirma": [{"tipo": "texto_contiene", "archivo": "informe_propio.md", "contiene": "4/1/5"}]}]})
    r = run_caso(sp, {**base_env, **b, "RUN_DIR": rd})
    res17 = resultado(ev, "Q1-032")
    copiado17 = os.path.isfile(os.path.join(ev, "Q1-032", "informe_propio.md"))
    paso("17 P3va copiar_artefacto ../../Q1-036 -> rc!=0, no copiado",
         r.returncode != 0 and res17["estado_caso"] != "COMPONENTE_OK" and not copiado17,
         f"rc={r.returncode} estado={res17['estado_caso']} copiado={copiado17}")

    ev18 = os.path.join(tmp, "ev_p3vb")
    os.makedirs(os.path.join(ev18, "Q1-036"))
    vict = os.path.join(ev18, "Q1-036", "07.md")
    open(vict, "w").write("ORIGINAL Q1-036")
    sp = spec_tmp(tmp, "p3vb.json", {"id": "Q1-033", "harness_version": "4.0", "pasos": [
        {"op": "nuevo_expediente"}, {"op": "comprobar", "guardar": "../Q1-036/07.md", "esperado": [0, 1]}],
        "criterios": [{"id": "C1", "texto": "x", "afirma": [{"tipo": "texto_contiene", "archivo": "02.json", "contiene": "x"}]}]})
    r = run_caso(sp, {**base_env, **b, "EVIDENCIAS_DIR": ev18})
    paso("18 P3vb guardar ../Q1-036 -> víctima intacta, rc!=0",
         r.returncode != 0 and open(vict).read() == "ORIGINAL Q1-036", f"rc={r.returncode} victima={open(vict).read()[:20]!r}")

    rd19 = os.path.join(tmp, "run_n1a")
    os.makedirs(os.path.join(rd19, "Q1-036", "Viscofan"))
    vict19 = os.path.join(rd19, "Q1-036", "Viscofan", "verificacion_entradas.json")
    open(vict19, "w").write('{"original": "Q1-036"}')
    sp = spec_tmp(tmp, "n1a.json", {"id": "Q1-031", "harness_version": "4.0", "pasos": [
        {"op": "nuevo_expediente"},
        {"op": "escribir_fuente", "nombre": "../../../Q1-036/Viscofan/verificacion_entradas.json", "paginas": ["PISADO"]}],
        "criterios": [{"id": "C1", "texto": "x", "afirma": [{"tipo": "texto_contiene", "archivo": "x.txt", "contiene": "x"}]}]})
    r = run_caso(sp, {**base_env, **b, "RUN_DIR": rd19})
    paso("19 N1a escribir_fuente ../../../Q1-036 -> registro ajeno intacto",
         open(vict19).read() == '{"original": "Q1-036"}', f"registro={open(vict19).read()[:30]!r} rc={r.returncode}")

    ajeno = os.path.join(tmp, "ev_ajena", "Q1-036")
    os.makedirs(ajeno)
    open(os.path.join(ajeno, "07.md"), "w").write("ajeno\n")
    sp = spec_tmp(tmp, "n1b.json", {"id": "Q1-032", "harness_version": "4.0", "pasos": [
        {"op": "nuevo_expediente"},
        {"op": "copiar_artefacto", "archivo": os.path.join(ajeno, "07.md"), "guardar": "copia.md"}],
        "criterios": [{"id": "C1", "texto": "x", "afirma": [{"tipo": "texto_contiene", "archivo": "copia.md", "contiene": "ajeno"}]}]})
    r = run_caso(sp, {**base_env, **b})
    res20 = resultado(ev, "Q1-032")
    paso("20 N1b copiar_artefacto ruta absoluta -> rc!=0",
         r.returncode != 0 and res20["estado_caso"] != "COMPONENTE_OK", f"rc={r.returncode} estado={res20['estado_caso']}")

    sp = spec_tmp(tmp, "p1v.json", {"id": "Q1-031", "harness_version": "4.0", "pasos": [{"op": "nuevo_expediente"}],
                                    "criterios": [{"id": "C1", "texto": "x", "afirma": [
                                        {"tipo": "texto_contiene", "archivo": "ejecucion.log", "contiene": "# Caso"}]}]})
    r = run_caso(sp, {**base_env, **b})
    res21 = resultado(ev, "Q1-031")
    paso("21 P1v aserción sobre ejecucion.log (archivo del arnés) -> rc!=0",
         r.returncode != 0 and res21["estado_caso"] != "COMPONENTE_OK"
         and any("no producido por el producto" in e for e in res21["errores"]), f"rc={r.returncode}")

    sp = spec_tmp(tmp, "n3.json", {"id": "Q1-031", "harness_version": "4.0", "pasos": [
        {"op": "nuevo_expediente"},
        {"op": "escribir_fuente", "nombre": "f.txt", "paginas": ["710"]}],
        "criterios": [{"id": "C1", "texto": "x", "afirma": [
            {"tipo": "texto_contiene", "archivo": "run:Viscofan/fuentes_sinteticas/f.txt", "contiene": "710"}]}]})
    r = run_caso(sp, {**base_env, **b})
    res22 = resultado(ev, "Q1-031")
    paso("22 N3 aserción run: -> rc!=0 (no soportado)",
         r.returncode != 0 and any("run:" in e for e in res22["errores"]), f"rc={r.returncode} errores={res22['errores']}")

    # 23-25 ids
    ev23 = os.path.join(tmp, "ev_p9w")
    os.makedirs(os.path.join(ev23, "Q1-001"))
    open(os.path.join(ev23, "Q1-001", "evidencia.txt"), "w").write("de otro caso")
    r = run_caso(spec_tmp(tmp, "p9w.json", {"id": ".", "pasos": [], "criterios": []}), {**base_env, "EVIDENCIAS_DIR": ev23})
    paso("23 P9w id '.' -> rc 2 SIN borrar evidencia ajena",
         r.returncode == 2 and os.path.isfile(os.path.join(ev23, "Q1-001", "evidencia.txt")), f"rc={r.returncode}")
    raiz = os.path.join(tmp, "n4")
    os.makedirs(os.path.join(raiz, "evidencias")); os.makedirs(os.path.join(raiz, "fuera"))
    open(os.path.join(raiz, "fuera", "ajeno.txt"), "w").write("ajeno")
    r = run_caso(spec_tmp(tmp, "n4.json", {"id": "../fuera", "pasos": [], "criterios": []}), {**base_env, "EVIDENCIAS_DIR": os.path.join(raiz, "evidencias")})
    paso("24 N4 id '../fuera' -> rc 2 SIN borrar fuera de EVIDENCIAS",
         r.returncode == 2 and os.path.isfile(os.path.join(raiz, "fuera", "ajeno.txt")), f"rc={r.returncode}")
    ev25 = os.path.join(tmp, "ev_n4b")
    os.makedirs(os.path.join(ev25, "Q1-002"))
    open(os.path.join(ev25, "Q1-002", "evidencia.txt"), "w").write("x")
    r = run_caso(spec_tmp(tmp, "n4b.json", {"id": "", "pasos": [], "criterios": []}), {**base_env, "EVIDENCIAS_DIR": ev25})
    paso("25 N4b id '' -> rc 2 SIN borrar EVIDENCIAS",
         r.returncode == 2 and os.path.isfile(os.path.join(ev25, "Q1-002", "evidencia.txt")), f"rc={r.returncode}")

    # 26-29 candidata con alteraciones ocultas
    rel = "munger_v2_r1/personaje_v2/scripts/verificacion_entradas.py"

    def cand_alt(nombre, prepara):
        c, s, pl = candidata_falsa(tmp, nombre)
        prepara(c)
        r = run_caso(sp8, {**base_env, "CANDIDATA_DIR": c, "SHA_CANDIDATA_ESPERADO": s, "PLANTILLA_EXP": pl,
                           "EVIDENCIAS_DIR": os.path.join(tmp, "ev_" + nombre)})
        return r.returncode

    def alterar(c, flag):
        subprocess.run(["git", "-C", c, "update-index", flag, rel], check=True)
        p = os.path.join(c, rel)
        open(p, "w").write(open(p).read().replace("def ", "def x_", 1))

    paso("26 P8va skip-worktree -> rc 2", cand_alt("c8a", lambda c: alterar(c, "--skip-worktree")) == 2)
    paso("27 P8vb no rastreado en scripts/ -> rc 2",
         cand_alt("c8b", lambda c: open(os.path.join(c, "munger_v2_r1/personaje_v2/scripts/override.txt"), "w").write("x")) == 2)
    paso("28 N5a assume-unchanged -> rc 2", cand_alt("c8c", lambda c: alterar(c, "--assume-unchanged")) == 2)

    def excluido(c):
        open(os.path.join(c, ".git", "info", "exclude"), "a").write("\noverride.txt\n")
        open(os.path.join(c, "munger_v2_r1/personaje_v2/scripts/override.txt"), "w").write("x")
    paso("29 N5b oculto por .git/info/exclude -> rc 2", cand_alt("c8d", excluido) == 2)

    # 30-33 matriz: reevaluación (M2, N2a, N2b, M3)
    t = os.path.join(tmp, "mat")
    shutil.copytree(os.path.join(L.AUX), t, ignore=shutil.ignore_patterns("__pycache__"))
    evt = os.path.join(t, "evidencias")
    spec001 = os.path.join(t, "scripts/especificaciones/piloto/Q1-001.json")
    import hashlib
    sha001 = hashlib.sha256(open(spec001, "rb").read()).hexdigest()
    os.makedirs(os.path.join(evt, "Q1-001"), exist_ok=True)
    json.dump({"harness_version": "4.0", "estado_caso": "COMPONENTE_OK", "spec_sha256": sha001, "errores": [],
               "afirmaciones_fallidas": [], "criterios": [{"id": "C1", "estado": "CUMPLE_COMPONENTE"}]},
              open(os.path.join(evt, "Q1-001", "resultado_ejecucion.json"), "w"))
    p3 = os.path.join(evt, "Q1-003")
    for f in os.listdir(p3):
        if f.endswith(".json") and f != "resultado_ejecucion.json":
            o = json.load(open(os.path.join(p3, f)))
            for k in ("comprobadas", "pendientes", "desactualizadas"):
                if isinstance(o.get(k), list):
                    o[k] = []
            o["universo"] = 0
            json.dump(o, open(os.path.join(p3, f), "w"))
    o = json.load(open(os.path.join(evt, "Q1-004", "resultado_ejecucion.json")))
    o["candidata_sha"] = "0" * 40; o["banco_casos_sha256"] = "f" * 64; o["harness_version"] = "2.0"
    json.dump(o, open(os.path.join(evt, "Q1-004", "resultado_ejecucion.json"), "w"))
    json.dump({"harness_version": "4.0", "estado_caso": "ERROR_ENTORNO", "criterios": [], "errores": ["x"],
               "afirmaciones_fallidas": []}, open(os.path.join(evt, "Q1-026", "resultado_ejecucion.json"), "w"))
    subprocess.run([sys.executable, "-B", os.path.join(t, "scripts", "generar_matriz.py")],
                   env=dict(os.environ, BANCO_DIR=L.BANCO), capture_output=True, text=True)
    filas = {r["id"]: r for r in csv.DictReader(open(os.path.join(t, "MATRIZ_EJECUCION.csv"), encoding="utf-8"))}
    paso("30 M2 resultado de 4 campos con spec_sha256 -> generar_matriz sola: sin CUMPLE",
         filas["Q1-001"]["veredicto_componente"] == "", f"Q1-001={filas['Q1-001']['veredicto_componente']!r} {filas['Q1-001']['estado_ejecucion']!r}")
    paso("31 N2a salidas vaciadas (universo 0) -> sin CUMPLE",
         filas["Q1-003"]["veredicto_componente"] == "", f"Q1-003={filas['Q1-003']['veredicto_componente']!r}")
    paso("32 N2b otra candidata/otro banco/harness 2.0 -> sin CUMPLE",
         filas["Q1-004"]["veredicto_componente"] == "", f"Q1-004={filas['Q1-004']['veredicto_componente']!r}")
    paso("33 M3 Q1-026 ERROR_ENTORNO -> BLOQUEO_ENTORNO desde el resultado",
         filas["Q1-026"]["estado_ejecucion"] == "BLOQUEO_ENTORNO", f"Q1-026={filas['Q1-026']['estado_ejecucion']!r}")

    # 34 D3-R2: control negativo contra el estado previo (quitando los archivos del paso que produce el leído y posteriores)
    mal = []
    for spath in sorted(glob.glob(os.path.join(AQUI, "especificaciones", "*", "Q1-*.json"))):
        s = json.load(open(spath, encoding="utf-8"))
        evc = os.path.join(L.EVIDENCIAS, s["id"])
        if not os.path.isdir(evc):
            continue
        prod_paso = {}
        for i, p in enumerate(s["pasos"]):
            if p.get("guardar"):
                prod_paso[os.path.basename(p["guardar"])] = i
            if p.get("op") == "copiar_artefacto" and p.get("guardar"):
                prod_paso[os.path.basename(p["guardar"])] = i
        max_paso = len(s["pasos"])
        for cr in s.get("criterios", []):
            for a in cr.get("afirma", []):
                if a["archivo"].startswith("run:"):
                    continue
                k = prod_paso.get(a["archivo"], 0)
                prev = os.path.join(tmp, "prev", s["id"], cr["id"] + "_" + a["archivo"].replace("/", "_"))
                shutil.rmtree(os.path.dirname(prev), ignore_errors=True)
                os.makedirs(prev, exist_ok=True)
                for f in os.listdir(evc):
                    if f in ("ejecucion.log", "resultado_ejecucion.json"):
                        continue
                    if prod_paso.get(f, max_paso) >= k and f != a["archivo"]:
                        continue
                    if prod_paso.get(f, max_paso) >= k:
                        continue
                    shutil.copy(os.path.join(evc, f), os.path.join(prev, f))
                c = L.Caso.__new__(L.Caso)
                c.id = s["id"]; c.ev_dir = prev; c.errores = []
                c.archivos_producto = {f for f in os.listdir(prev)}
                ok, _ = EC.evaluar_afirmacion(c, a)
                if ok and not cr.get("no_discriminante") and not a.get("no_discriminante"):
                    mal.append(f"{s['id']} {cr['id']} {a['archivo']} pasa en estado previo sin marca no_discriminante")
    paso("34 D3-R2 control contra el ESTADO PREVIO: toda aserción falla salvo las marcadas no_discriminante",
         not mal, f"mal={mal[:3]}")

    # 35 D3-R7: sellar con revisor propio sin marca; ARNES_EVIDENCIAS_LIMPIAS=0 registrado
    sp = spec_tmp(tmp, "rev.json", {"id": "Q1-001", "harness_version": "4.0", "pasos": [
        {"op": "nuevo_expediente"},
        {"op": "entrada", "celda": "aux:x", "clase": "hipotesis",
         "hipotesis": {"fundamento": "f", "alternativas": [], "limites": "l"},
         "comprobacion": {"extractor": "ext propio", "revisor": "rev propio", "fecha": "HOY", "resultado": "verificado", "fuente_examinada": "f", "nota": None, "vinculo": None}},
        {"op": "sellar", "celdas": ["aux:x"], "revisor": "revisor propio sin marca", "guardar": "s.txt", "esperado": [0, 1]}],
        "criterios": [{"id": "C1", "texto": "x", "afirma": [{"tipo": "texto_contiene", "archivo": "s.txt", "contiene": "sellar"}]}]})
    r = run_caso(sp, {**base_env, **{"CANDIDATA_DIR": cand, "SHA_CANDIDATA_ESPERADO": sha, "PLANTILLA_EXP": pl},
                      "RUN_DIR": os.path.join(tmp, "run_rev")})
    reg = json.load(open(os.path.join(tmp, "run_rev", "Q1-001", "Viscofan", "verificacion_entradas.json")))
    aux = next(e for e in reg["entradas"] if e["celda"] == "aux:x")
    comp = aux["comprobacion"]
    r35a = comp.get("_simulada") is True and "[SIMULADO]" in str(comp.get("revisor")) and "[SIMULADO]" in str(comp.get("extractor"))
    ev35 = os.path.join(tmp, "ev_lim0")
    os.makedirs(ev35)
    r = run_caso(spec_001, {**base_env, "EVIDENCIAS_DIR": ev35, "ARNES_EVIDENCIAS_LIMPIAS": "0"})
    res35 = resultado(ev35, "Q1-001")
    r35b = res35.get("evidencias_limpiadas") is False and "AVISO" in open(os.path.join(ev35, "Q1-001", "ejecucion.log")).read()
    paso("35 D3-R7 sellar con revisor propio queda [SIMULADO]; ARNES_EVIDENCIAS_LIMPIAS=0 registrado con aviso",
         r35a and r35b, f"comp={comp} limpiadas={res35.get('evidencias_limpiadas')}")

    # 36 D3-R4: paquetes de relevo completos
    rel_p = os.path.join(L.AUX, "relevo", "PAQUETES_RELEVO.json")
    if os.path.isfile(rel_p):
        doc = json.load(open(rel_p, encoding="utf-8"))
        mal = []
        for p in doc["paquetes"]:
            for clave in ("estado_inicial", "fases", "entrada", "artefacto_por_criterio"):
                if not p.get(clave):
                    mal.append(f"{p['caso']} sin {clave}")
            if not p.get("comando_relevo") and not p.get("motivo_sin_comando"):
                mal.append(f"{p['caso']} sin comando_relevo ni motivo")
            for cb in p.get("criterios_banco", []):
                if not cb.get("artefacto"):
                    mal.append(f"{p['caso']} criterio {cb.get('indice')} sin artefacto")
        paso("36 D3-R4 cada paquete: estado_inicial+fases+entrada+artefacto por criterio+comando/motivo",
             not mal, f"mal={mal[:4]} paquetes={len(doc['paquetes'])}")
    else:
        paso("36 D3-R4 paquetes presentes", False, "falta PAQUETES_RELEVO.json")

    log = os.path.join(L.EVIDENCIAS, "pruebas_arnes.log")
    with open(log, "w", encoding="utf-8") as f:
        json.dump({"pruebas": RESULTADOS, "todo_ok": all(x["ok"] for x in RESULTADOS)}, f, ensure_ascii=False, indent=1)
        for x in RESULTADOS:
            f.write(("PASA " if x["ok"] else "FALLA ") + x["prueba"] + " · " + x["detalle"] + "\n")
    shutil.rmtree(tmp, ignore_errors=True)
    n_ok = sum(1 for x in RESULTADOS if x["ok"])
    print(f"pruebas del arnés v4: {n_ok}/{len(RESULTADOS)} PASA · log en {log}")
    return 0 if n_ok == len(RESULTADOS) else 1


if __name__ == "__main__":
    sys.exit(main())
