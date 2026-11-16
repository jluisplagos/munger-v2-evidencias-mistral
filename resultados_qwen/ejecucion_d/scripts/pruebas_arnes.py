#!/usr/bin/env python3
"""Pruebas del propio arnés (CORRECCION_D): el arnés debe detectar sus fallos.

1. positivo real (Q1-001 -> COMPONENTE_OK, rc 0)
2. negativo esperado real (Q1-006: sellar rechazado exit 1 declarado en `esperado` -> rc 0)
3. candidata incompleta (CANDIDATA_DIR vacío -> rc != 0, estado ERROR_ENTORNO)
4. artefacto heredado tras fallo de generación (config con plantilla ausente -> ficha exit 2
   inesperado -> caso ERROR y NO se copia el artefacto heredado)
5. carpeta de evidencias ausente (matriz sobre evidencias vacías -> 0 ejecuciones propias,
   ningún veredicto positivo de componente)
6. resultado mutado que incumple un predicado (aserción FALLA detectada)
7. recuentos desde fuente única (recuentos.json == CSV; Q1-035 coherente), observaciones
   compartidas declaradas y precondiciones simuladas registradas

Uso: python3 pruebas_arnes.py   (exit 0 solo si todas PASA; log en evidencias/pruebas_arnes.log)
"""
import csv
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

    # 1. positivo real
    r = run_caso(spec_001, base_env)
    res = json.load(open(os.path.join(ev, "Q1-001", "resultado_ejecucion.json")))
    paso("positivo real Q1-001 (COMPONENTE_OK, aserciones CUMPLE)",
         r.returncode == 0 and res["estado_caso"] == "COMPONENTE_OK"
         and all(c["estado"] == "CUMPLE_COMPONENTE" for c in res["criterios"]),
         f"rc={r.returncode} estado={res['estado_caso']}")

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
    paso("candidata incompleta -> error propagado (rc!=0, ERROR_ENTORNO, errores registrados)",
         r.returncode != 0 and res3.get("estado_caso") == "ERROR_ENTORNO" and bool(res3.get("errores")),
         f"rc={r.returncode} estado={res3.get('estado_caso')}")

    # 4. artefacto heredado tras fallo de generación: candidata aislada con la plantilla
    # V6.4.1 ausente (symlinks a los scripts reales; config rota; git init propio).
    # No se toca ningún binario oficial: la ausencia vive solo en la copia de prueba.
    fake = os.path.join(tmp, "candidata_fake")
    fpj = os.path.join(fake, "munger_v2_r1", "personaje_v2")
    os.makedirs(fpj)
    for d in ("scripts", "esquema", "prompts", "corpus"):
        src = os.path.join(L.PERSONAJE, d)
        if os.path.isdir(src):
            os.symlink(src, os.path.join(fpj, d))
    for cfgname in ("config_v2.json",):
        shutil.copy(os.path.join(L.PERSONAJE, cfgname), os.path.join(fpj, cfgname))
    cfg = json.load(open(os.path.join(L.PERSONAJE, "config_v2_v641_experimental.json"), encoding="utf-8"))
    cfg["plantilla"]["archivo"] = "../v6/v641_experimental/entregables/NO_EXISTE.xlsx"
    json.dump(cfg, open(os.path.join(fpj, "config_v2_v641_experimental.json"), "w", encoding="utf-8"))
    subprocess.run(["git", "-C", fake, "init", "-q"], check=True)
    subprocess.run(["git", "-C", fake, "add", "-A"], check=True)
    subprocess.run(["git", "-C", fake, "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "fake"], check=True)
    sha_fake = subprocess.run(["git", "-C", fake, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    spec_obsoleto = {
        "id": "SONDA_OBSOLETO", "harness_version": "2.0",
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
         f"rc={r.returncode} estado={res4['estado_caso']} copiado={copiado} criterios={[c['estado'] for c in res4['criterios']]}")

    # 5. carpeta de evidencias ausente -> matriz sin veredictos positivos
    aux_tmp = os.path.join(tmp, "aux")
    os.makedirs(os.path.join(aux_tmp, "scripts", "especificaciones"))
    os.makedirs(os.path.join(aux_tmp, "evidencias"))
    shutil.copy(os.path.join(AQUI, "generar_matriz.py"), os.path.join(aux_tmp, "scripts", "generar_matriz.py"))
    shutil.copy(os.path.join(AQUI, "especificaciones", "adaptaciones.json"),
                os.path.join(aux_tmp, "scripts", "especificaciones", "adaptaciones.json"))
    r5 = subprocess.run([sys.executable, "-B", os.path.join(aux_tmp, "scripts", "generar_matriz.py")],
                        capture_output=True, text=True,
                        env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", BANCO_DIR=L.BANCO))
    csv5 = os.path.join(aux_tmp, "MATRIZ_EJECUCION.csv")
    rec5 = json.load(open(os.path.join(aux_tmp, "evidencias", "recuentos.json")))
    filas = list(csv.DictReader(open(csv5, encoding="utf-8")))
    paso("carpeta de evidencias ausente -> 36 filas, 0 ejecuciones propias, ningún CUMPLE de componente",
         r5.returncode == 0 and len(filas) == 36 and rec5.get("con_ejecucion_propia") == 0
         and all(rr["veredicto_componente"] == "" for rr in filas),
         f"rc={r5.returncode} filas={len(filas)} propias={rec5.get('con_ejecucion_propia')}")

    # 6. resultado mutado que incumple un predicado
    run_caso(spec_001, base_env)
    import ejecutar_caso as EC
    p6 = os.path.join(ev, "Q1-001", "03_comprobar_sellado.json")
    obj = json.load(open(p6, encoding="utf-8"))
    obj["comprobadas"] = [x for x in obj["comprobadas"] if x != "Historia!C23"]
    json.dump(obj, open(p6, "w", encoding="utf-8"))
    spec = json.load(open(spec_001, encoding="utf-8"))
    caso_fake = L.Caso.__new__(L.Caso)
    caso_fake.id = "Q1-001"
    caso_fake.ev_dir = os.path.join(ev, "Q1-001")
    ok, detalle = EC.evaluar_afirmacion(caso_fake, spec["criterios"][0]["afirma"][0])
    paso("resultado mutado que incumple el predicado -> aserción FALLA detectada", ok is False, detalle)

    # 7. recuentos desde fuente única + compartidos + simuladas
    subprocess.run([sys.executable, "-B", os.path.join(AQUI, "generar_matriz.py")],
                   capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    rec = json.load(open(os.path.join(L.EVIDENCIAS, "recuentos.json")))
    filas = list(csv.DictReader(open(os.path.join(L.AUX, "MATRIZ_EJECUCION.csv"), encoding="utf-8")))
    q35 = next(rr for rr in filas if rr["id"] == "Q1-035")
    q28 = next(rr for rr in filas if rr["id"] == "Q1-028")
    res001 = json.load(open(os.path.join(L.EVIDENCIAS, "Q1-001", "resultado_ejecucion.json")))
    paso("recuentos desde fuente única (recuentos.json == CSV) y Q1-035 coherente matriz/recuentos",
         rec["veredicto_caso"].get("DECISION_PENDIENTE", 0) == 2
         and q35["veredicto_caso"].startswith("DECISION_PENDIENTE"), f"recuentos={rec['veredicto_caso']}")
    paso("observación compartida declarada (Q1-028) y precondiciones simuladas registradas (D-R4)",
         q28["observacion_compartida"] != "-" and "SIMULADA" in res001.get("precondiciones_simuladas", ""),
         f"obs={q28['observacion_compartida'][:50]}")

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
