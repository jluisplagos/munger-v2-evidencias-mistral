#!/usr/bin/env python3
"""Pruebas del propio arnés v3 (D2-R1/R2/R7): el arnés debe detectar sus fallos.

1. positivo real (Q1-001 -> COMPONENTE_OK, rc 0)
2. negativo esperado real (Q1-006: sellar rechazado exit 1 declarado -> rc 0)
3. candidata incompleta (CANDIDATA_DIR vacío -> rc 2, ERROR_ENTORNO)
4. artefacto heredado tras fallo de generación (plantilla ausente -> caso ERROR, NO copiado)
5. matriz SIN carpeta de evidencias (no se crea) -> rc 0, 36 filas, 0 CUMPLE (control explícito)
6. resultado mutado que incumple un predicado -> aserción FALLA detectada
7. recuentos desde fuente única: recuentos.json == MATRIZ_EJECUCION.csv (estados y veredictos)
8. D2-R1a P1: especificación vacía (pasos/criterios vacíos) -> rc 2, ERROR_ESPECIFICACION
9. D2-R1b P2: criterio sin aserciones -> rc 2, ERROR_ESPECIFICACION
10. D2-R1c P3: aserción con ruta fuera del caso (../Q1-036/…) -> rc != 0 y error registrado
11. D2-R1e P5: json_lista_no_contiene sobre salida sin universo positivo -> FALLA
12. D2-R1d P4: resultado forjado (dos campos, sin criterios ni huella de spec) -> la matriz no da CUMPLE
13. D2-R7c P8: candidata con cambio sin commit (archivo rastreado modificado) -> rc 2, ERROR_ENTORNO
14. D2-R7b P9: un log por ejecución (Q1-001 dos veces -> 1 «# Caso» en el log)
15. D2-R2: control negativo por aserción: TODAS las aserciones de TODAS las specs fallan
    sobre un estado previo vacío
16. D2-R7a: marcas SIMULADA en todo registro escrito por el arnés (dict y "verificada"),
    incluido el --revisor del sellar

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


def main():
    tmp = tempfile.mkdtemp(prefix="pruebas_arnes_")
    ev = os.path.join(tmp, "evidencias")
    run_dir = os.path.join(tmp, "run")
    os.makedirs(ev)
    base_env = {"EVIDENCIAS_DIR": ev, "RUN_DIR": run_dir}
    spec_001 = os.path.join(AQUI, "especificaciones", "piloto", "Q1-001.json")
    spec_006 = os.path.join(AQUI, "especificaciones", "piloto", "Q1-006.json")
    spec_002 = os.path.join(AQUI, "especificaciones", "bloque2", "Q1-002.json")

    # 1. positivo real
    r = run_caso(spec_001, base_env)
    res = json.load(open(os.path.join(ev, "Q1-001", "resultado_ejecucion.json")))
    paso("positivo real Q1-001 (COMPONENTE_OK, aserciones CUMPLE, sha observado registrado)",
         r.returncode == 0 and res["estado_caso"] == "COMPONENTE_OK"
         and all(c["estado"] == "CUMPLE_COMPONENTE" for c in res["criterios"])
         and res.get("candidata_sha") == L.SHA_CANDIDATA_ESPERADO and res.get("spec_sha256"),
         f"rc={r.returncode} estado={res['estado_caso']} sha={str(res.get('candidata_sha'))[:8]}")

    # 2. negativo esperado real
    r = run_caso(spec_006, base_env)
    res6 = json.load(open(os.path.join(ev, "Q1-006", "resultado_ejecucion.json")))
    sellar = [p for p in res6["pasos"] if "sellar" in p.get("descripcion", "")]
    paso("negativo esperado real Q1-006 (sellar exit 1 está en esperado; aserciones pasan)",
         r.returncode == 0 and res6["estado_caso"] == "COMPONENTE_OK"
         and any(p.get("exit") == 1 and not p.get("error_inesperado") for p in sellar), f"rc={r.returncode}")

    # 3. candidata incompleta
    empty = os.path.join(tmp, "candidata_vacia")
    os.makedirs(empty)
    r = run_caso(spec_001, {**base_env, "CANDIDATA_DIR": empty})
    p = os.path.join(ev, "Q1-001", "resultado_ejecucion.json")
    res3 = json.load(open(p)) if os.path.isfile(p) else {}
    paso("candidata incompleta -> error propagado (rc=2, ERROR_ENTORNO, errores registrados)",
         r.returncode == 2 and res3.get("estado_caso") == "ERROR_ENTORNO" and bool(res3.get("errores")),
         f"rc={r.returncode} estado={res3.get('estado_caso')}")

    # 4. artefacto heredado tras fallo de generación (candidata aislada, plantilla ausente)
    fake = os.path.join(tmp, "candidata_fake")
    fpj = os.path.join(fake, "munger_v2_r1", "personaje_v2")
    os.makedirs(fpj)
    shutil.copytree(os.path.join(L.PERSONAJE, "scripts"), os.path.join(fpj, "scripts"))
    for cfgname in ("config_v2.json", "config_v2_v641_experimental.json"):
        src = os.path.join(L.PERSONAJE, cfgname)
        if os.path.isfile(src):
            shutil.copy(src, os.path.join(fpj, cfgname))
    cfgp = os.path.join(fpj, "config_v2_v641_experimental.json")
    if os.path.isfile(cfgp):
        cfg = json.load(open(cfgp, encoding="utf-8"))
        cfg["plantilla"]["archivo"] = "../v6/v641_experimental/entregables/NO_EXISTE.xlsx"
        json.dump(cfg, open(cfgp, "w", encoding="utf-8"))
    subprocess.run(["git", "-C", fake, "init", "-q"], check=True)
    subprocess.run(["git", "-C", fake, "add", "-A"], check=True)
    subprocess.run(["git", "-C", fake, "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "fake"], check=True)
    sha_fake = subprocess.run(["git", "-C", fake, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    spec_obsoleto = {
        "id": "SONDA_OBSOLETO", "harness_version": "3.0",
        "pasos": [
            {"op": "nuevo_expediente"},
            {"op": "ficha", "args": ["--estado", "concluido", "--provisional"], "guardar": "ficha.txt", "esperado": [0]},
            {"op": "copiar_artefacto", "archivo": "ficha_provisional.json", "guardar": "ficha_copia.json"},
        ],
        "criterios": [{"id": "C1", "texto": "el artefacto copiado es nuevo y del paso productor con exit esperado",
                      "afirma": [{"tipo": "archivo_existe", "archivo": "ficha_copia.json"}]}],
    }
    sp = os.path.join(tmp, "sonda_obsoleto.json")
    json.dump(spec_obsoleto, open(sp, "w", encoding="utf-8"))
    r = run_caso(sp, {**base_env, "CANDIDATA_DIR": fake, "SHA_CANDIDATA_ESPERADO": sha_fake,
                      "PLANTILLA_EXP": L.PLANTILLA_EXP})
    res4 = json.load(open(os.path.join(ev, "SONDA_OBSOLETO", "resultado_ejecucion.json")))
    copiado = os.path.isfile(os.path.join(ev, "SONDA_OBSOLETO", "ficha_copia.json"))
    paso("artefacto heredado tras fallo de generación -> detectado, NO copiado, rc!=0",
         r.returncode != 0 and res4["estado_caso"] == "ERROR" and not copiado
         and (bool(res4["afirmaciones_fallidas"]) or any(c["estado"] == "FALLA_COMPONENTE" for c in res4["criterios"])),
         f"rc={r.returncode} estado={res4['estado_caso']} copiado={copiado}")

    # 5. matriz SIN carpeta de evidencias (no se crea): control explícito, 0 CUMPLE
    aux_tmp = os.path.join(tmp, "aux")
    os.makedirs(os.path.join(aux_tmp, "scripts", "especificaciones"))
    shutil.copy(os.path.join(AQUI, "generar_matriz.py"), os.path.join(aux_tmp, "scripts", "generar_matriz.py"))
    shutil.copy(os.path.join(AQUI, "especificaciones", "adaptaciones.json"),
                os.path.join(aux_tmp, "scripts", "especificaciones", "adaptaciones.json"))
    r5 = subprocess.run([sys.executable, "-B", os.path.join(aux_tmp, "scripts", "generar_matriz.py")],
                        capture_output=True, text=True,
                        env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", BANCO_DIR=L.BANCO))
    csv5 = os.path.join(aux_tmp, "MATRIZ_EJECUCION.csv")
    rec5 = json.load(open(os.path.join(aux_tmp, "evidencias", "recuentos.json")))
    filas = list(csv.DictReader(open(csv5, encoding="utf-8")))
    paso("matriz sin carpeta de evidencias (no creada a mano) -> rc 0, 36 filas, 0 propias, ningún CUMPLE",
         r5.returncode == 0 and len(filas) == 36 and rec5.get("con_ejecucion_propia") == 0
         and all(rr["veredicto_componente"] == "" for rr in filas),
         f"rc={r5.returncode} filas={len(filas)} propias={rec5.get('con_ejecucion_propia')}")

    # 6. resultado mutado que incumple un predicado
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
    ok, detalle = EC.evaluar_afirmacion(caso_fake, spec["criterios"][0]["afirma"][0])
    paso("resultado mutado que incumple el predicado -> aserción FALLA detectada", ok is False, detalle)

    # 7. recuentos desde fuente única: recuentos.json == CSV (estados y veredictos)
    subprocess.run([sys.executable, "-B", os.path.join(AQUI, "generar_matriz.py")],
                   capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    rec = json.load(open(os.path.join(L.EVIDENCIAS, "recuentos.json")))
    filas = list(csv.DictReader(open(os.path.join(L.AUX, "MATRIZ_EJECUCION.csv"), encoding="utf-8")))
    import collections
    est_csv = dict(collections.Counter(r["estado_ejecucion"] for r in filas))
    vc_csv = dict(collections.Counter(r["veredicto_caso"].split(" (")[0] for r in filas))
    paso("recuentos desde fuente única (recuentos.json == CSV en estados y veredicto_caso)",
         rec["estado_ejecucion"] == est_csv and rec["veredicto_caso"] == vc_csv,
         f"estados={est_csv} veredicto_caso={vc_csv}")

    # 8-10. sondas D2-R1: P1 spec vacía, P2 criterio sin afirma, P3 ruta cruzada
    sp = os.path.join(tmp, "p1.json")
    json.dump({"id": "Q1-031", "harness_version": "3.0", "pasos": [], "criterios": []}, open(sp, "w"))
    r = run_caso(sp, base_env)
    res_p1 = json.load(open(os.path.join(ev, "Q1-031", "resultado_ejecucion.json")))
    paso("D2-R1a P1: especificación vacía -> rc 2, ERROR_ESPECIFICACION (no COMPONENTE_OK)",
         r.returncode == 2 and res_p1["estado_caso"] == "ERROR_ESPECIFICACION", f"rc={r.returncode} estado={res_p1['estado_caso']}")
    sp = os.path.join(tmp, "p2.json")
    json.dump({"id": "Q1-033", "harness_version": "3.0", "pasos": [{"op": "nuevo_expediente"}],
               "criterios": [{"id": "C1", "texto": "x", "afirma": []}]}, open(sp, "w"))
    r = run_caso(sp, base_env)
    res_p2 = json.load(open(os.path.join(ev, "Q1-033", "resultado_ejecucion.json")))
    paso("D2-R1b P2: criterio sin aserciones -> rc 2, ERROR_ESPECIFICACION",
         r.returncode == 2 and res_p2["estado_caso"] == "ERROR_ESPECIFICACION", f"rc={r.returncode} estado={res_p2['estado_caso']}")
    sp = os.path.join(tmp, "p3.json")
    os.makedirs(os.path.join(ev, "Q1-036"), exist_ok=True)
    open(os.path.join(ev, "Q1-036", "07_informe_provisional.md"), "w").write("apta por entradas: no\n")
    json.dump({"id": "Q1-032", "harness_version": "3.0", "pasos": [{"op": "nuevo_expediente"}],
               "criterios": [{"id": "C1", "texto": "x", "afirma": [
                   {"tipo": "texto_contiene", "archivo": "../Q1-036/07_informe_provisional.md", "contiene": "apta"}]}]},
              open(sp, "w"))
    r = run_caso(sp, base_env)
    res_p3 = json.load(open(os.path.join(ev, "Q1-032", "resultado_ejecucion.json")))
    paso("D2-R1c P3: aserción que lee evidencia de otro caso (../) -> rc!=0 y error de ruta registrado",
         r.returncode != 0 and any("FUERA DEL CASO" in e or "fuera del RUN_DIR" in e for e in res_p3["errores"]),
         f"rc={r.returncode} errores={res_p3['errores']}")

    # 11. D2-R1e P5: negativo sin universo positivo no acredita
    caso11 = L.Caso.__new__(L.Caso)
    caso11.id = "P5"
    caso11.ev_dir = os.path.join(tmp, "ev_p5")
    caso11.errores = []
    os.makedirs(caso11.ev_dir, exist_ok=True)
    json.dump({"comprobadas": [], "pendientes": ["aux:litigio: sin rango"]},
              open(os.path.join(caso11.ev_dir, "salida.json"), "w"))
    ok, detalle = EC.evaluar_afirmacion(caso11, {"tipo": "json_lista_no_contiene", "archivo": "salida.json",
                                                 "lista": "comprobadas", "prefijo": "aux:litigio"})
    paso("D2-R1e P5: json_lista_no_contiene sobre salida vacía (sin universo) -> FALLA", ok is False, detalle)

    # 12. D2-R1d P4: resultado forjado en la matriz -> sin CUMPLE
    t4 = os.path.join(tmp, "p4")
    os.makedirs(os.path.join(t4, "scripts", "especificaciones"))
    os.makedirs(os.path.join(t4, "evidencias", "Q1-031"))
    shutil.copy(os.path.join(AQUI, "generar_matriz.py"), os.path.join(t4, "scripts", "generar_matriz.py"))
    shutil.copy(os.path.join(AQUI, "especificaciones", "adaptaciones.json"),
                os.path.join(t4, "scripts", "especificaciones", "adaptaciones.json"))
    json.dump({"harness_version": "3.0", "estado_caso": "COMPONENTE_OK"},
              open(os.path.join(t4, "evidencias", "Q1-031", "resultado_ejecucion.json"), "w"))
    r = subprocess.run([sys.executable, "-B", os.path.join(t4, "scripts", "generar_matriz.py")],
                       env=dict(os.environ, BANCO_DIR=L.BANCO), capture_output=True, text=True)
    fila = next(x for x in csv.DictReader(open(os.path.join(t4, "MATRIZ_EJECUCION.csv"))) if x["id"] == "Q1-031")
    rec4 = json.load(open(os.path.join(t4, "evidencias", "recuentos.json")))
    paso("D2-R1d P4: resultado forjado (dos campos) -> la matriz NO da CUMPLE (recalcula desde criterios+aserción+huella)",
         r.returncode == 0 and fila["veredicto_componente"] == "" and rec4["con_ejecucion_propia"] == 0,
         f"Q1-031 veredicto={fila['veredicto_componente']!r} estado={fila['estado_ejecucion']!r}")

    # 13. D2-R7c P8: candidata con cambio sin commit -> detectado
    fake8 = os.path.join(tmp, "cand_sucia")
    os.makedirs(os.path.join(fake8, "munger_v2_r1", "personaje_v2"))
    shutil.copytree(os.path.join(L.PERSONAJE, "scripts"), os.path.join(fake8, "munger_v2_r1", "personaje_v2", "scripts"))
    subprocess.run(["git", "-C", fake8, "init", "-q"], check=True)
    subprocess.run(["git", "-C", fake8, "add", "-A"], check=True)
    subprocess.run(["git", "-C", fake8, "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "x"], check=True)
    sha8 = subprocess.run(["git", "-C", fake8, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    with open(os.path.join(fake8, "munger_v2_r1", "personaje_v2", "scripts", "verificacion_entradas.py"), "a") as f:
        f.write("\n# modificado sin commit\n")
    sp = os.path.join(tmp, "p8.json")
    json.dump({"id": "P8", "harness_version": "3.0", "pasos": [{"op": "nuevo_expediente"}],
               "criterios": [{"id": "C1", "texto": "x", "afirma": [{"tipo": "texto_contiene", "archivo": "ejecucion.log", "contiene": "x"}]}]},
              open(sp, "w"))
    r = run_caso(sp, {**base_env, "CANDIDATA_DIR": fake8, "SHA_CANDIDATA_ESPERADO": sha8, "PLANTILLA_EXP": L.PLANTILLA_EXP})
    res8 = json.load(open(os.path.join(ev, "P8", "resultado_ejecucion.json")))
    paso("D2-R7c P8: candidata con cambio sin commit (árbol sucio) -> rc 2, ERROR_ENTORNO",
         r.returncode == 2 and res8["estado_caso"] == "ERROR_ENTORNO"
         and any("sin commit" in e for e in res8["errores"]), f"rc={r.returncode} errores={res8['errores']}")

    # 14. D2-R7b P9: un log por ejecución
    run_caso(spec_001, base_env)
    run_caso(spec_001, base_env)
    n = open(os.path.join(ev, "Q1-001", "ejecucion.log")).read().count("# Caso Q1-001")
    paso("D2-R7b P9: una ejecución = evidencias limpias (Q1-001 dos veces -> 1 '# Caso' en el log)",
         n == 1, f"ejecuciones_en_un_log={n}")

    # 15. D2-R2: control negativo por aserción sobre estado previo vacío
    import glob as _glob
    run_dir_real = L.RUN_DIR
    L.RUN_DIR = os.path.join(tmp, "run_vacio")
    mal = []
    for spath in sorted(_glob.glob(os.path.join(AQUI, "especificaciones", "*", "Q1-*.json"))):
        s = json.load(open(spath, encoding="utf-8"))
        c = L.Caso.__new__(L.Caso)
        c.id = s["id"]
        c.ev_dir = os.path.join(tmp, "ev_vacio", s["id"])
        c.errores = []
        os.makedirs(c.ev_dir, exist_ok=True)
        os.makedirs(os.path.join(L.RUN_DIR, s["id"]), exist_ok=True)
        for crit in s.get("criterios", []):
            for a in crit.get("afirma", []):
                ok, _ = EC.evaluar_afirmacion(c, a)
                if ok:
                    mal.append(f"{s['id']} {crit['id']} {a}")
    L.RUN_DIR = run_dir_real
    paso("D2-R2: control negativo por aserción: todas las aserciones de todas las specs fallan sobre estado previo vacío",
         not mal, f"aserciones que pasaron en vacío: {mal[:3]}")

    # 16. D2-R7a: marcas SIMULADA en registros escritos por el arnés (Q1-001 verificada, Q1-002 dict)
    run_caso(spec_002, base_env)
    regs = []
    for cid in ("Q1-001", "Q1-002"):
        p = os.path.join(run_dir, cid, "Viscofan", "verificacion_entradas.json")
        regs.append(json.load(open(p, encoding="utf-8")) if os.path.isfile(p) else None)
    marcadas = all(r and all((e.get("comprobacion") or {}).get("_simulada") is True
                             for e in r["entradas"] if (e.get("comprobacion") or {}).get("extractor") or (e.get("comprobacion") or {}).get("revisor"))
                   for r in regs if r)
    revisor_sim = any(r and any("[SIMULADO]" in str((e.get("comprobacion") or {}).get("revisor") or "")
                                for e in r["entradas"]) for r in regs if r)
    paso("D2-R7a: toda comprobación escrita por el arnés lleva _simulada/[SIMULADO] (dict y 'verificada', incl. --revisor del sellar)",
         marcadas and revisor_sim, f"marcadas={marcadas} revisor_sim={revisor_sim}")

    log = os.path.join(L.EVIDENCIAS, "pruebas_arnes.log")
    with open(log, "w", encoding="utf-8") as f:
        json.dump({"pruebas": RESULTADOS, "todo_ok": all(x["ok"] for x in RESULTADOS)}, f, ensure_ascii=False, indent=1)
        for x in RESULTADOS:
            f.write(("PASA " if x["ok"] else "FALLA ") + x["prueba"] + " · " + x["detalle"] + "\n")
    shutil.rmtree(tmp, ignore_errors=True)
    n_ok = sum(1 for x in RESULTADOS if x["ok"])
    print(f"pruebas del arnés: {n_ok}/{len(RESULTADOS)} PASA · log en {log}")
    return 0 if n_ok == len(RESULTADOS) else 1


if __name__ == "__main__":
    sys.exit(main())
