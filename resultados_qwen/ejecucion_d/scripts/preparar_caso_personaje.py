#!/usr/bin/env python3
"""Prepara el ESTADO INICIAL de un caso del banco para el recorrido del personaje (D4-R4).

NO lanza agentes ni ejecuta el pipeline: materializa el expediente de trabajo bajo
RUN_DIR/<caso>/ a partir del expediente base declarado en relevos_casos.json (ruta
relativa a la candidata), archiva las salidas heredadas, carga cada fixture del banco
en su archivo del producto (fuentes_sinteticas/<nombre> con marcas [PDF PAGE n]) y
genera el registro con `verificacion_entradas.py plantilla` (comando documentado del
producto). Escribe ESTADO_INICIAL.md y imprime el comando_relevo.

El runtime del coordinador ejecuta después `comando_relevo` (pipeline.py con flock +
subagentes según config_v2.json). En Q1-028 la aprobación de partida la crea el
runtime como aprobación AUTÉNTICA de prueba antes del cambio (PLAN §2); este script
solo materializa el fixture como fuente de prueba.

Uso: python3 -I scripts/preparar_caso_personaje.py Q1-028
Exit 0 si el estado inicial queda preparado. Sin editar nada.
"""
import json
import os
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib_arnes as L  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def main():
    if len(sys.argv) != 2 or not L.ID_RE.fullmatch(sys.argv[1]):
        print("uso: preparar_caso_personaje.py Q1-nnn")
        return 2
    cid = sys.argv[1]
    casos = [json.loads(l) for l in open(os.path.join(L.BANCO, "casos_aceptacion.jsonl"), encoding="utf-8") if l.strip()]
    ids_banco = {c["id"] for c in casos}
    if cid not in ids_banco:
        print(f"ERROR_ID {cid!r}: no está en el banco")
        return 2
    caso = next(c for c in casos if c["id"] == cid)
    rel = json.load(open(os.path.join(AQUI, "especificaciones", "relevos_casos.json"), encoding="utf-8"))["casos"][cid]

    problemas, info = L.verificar_entorno()
    if problemas:
        print(f"ERROR entorno: {problemas}")
        return 2

    exp_base_rel = rel["estado_inicial"]["expediente_base"]
    if os.path.isabs(exp_base_rel):
        print(f"ERROR: expediente_base debe ser relativo a la candidata: {exp_base_rel!r}")
        return 2
    exp_base = os.path.join(L.CANDIDATA, exp_base_rel)
    if not os.path.isdir(exp_base):
        print(f"ERROR: no existe el expediente base en la candidata: {exp_base_rel}")
        return 2

    destino = os.path.join(L.RUN_DIR, cid, "Viscofan")
    shutil.rmtree(os.path.join(L.RUN_DIR, cid), ignore_errors=True)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    shutil.copytree(exp_base, destino, ignore=L.IGNORAR_COPIA)
    # archivar salidas heredadas (D-R2)
    arch = os.path.join(L.RUN_DIR, cid, "_heredados")
    os.makedirs(arch, exist_ok=True)
    for nombre in L.ARTEFACTOS_HEREDADOS:
        p = os.path.join(destino, nombre)
        if os.path.exists(p):
            shutil.move(p, os.path.join(arch, nombre))

    ev_prep = os.path.join(L.RUN_DIR, cid, "_preparacion")
    os.makedirs(ev_prep, exist_ok=True)

    def log(t):
        with open(os.path.join(ev_prep, "preparacion.log"), "a", encoding="utf-8") as f:
            f.write(t + "\n")

    log(f"# preparación estado inicial {cid} · candidata {info.get('candidata_sha_observado')} · banco sha256 {info.get('banco_casos_sha256')}")
    log(f"# expediente base (relativo a la candidata): {exp_base_rel}")
    # registro inicial: comando documentado del producto
    r = subprocess.run([sys.executable, "-B", os.path.join(L.SCRIPTS, "verificacion_entradas.py"), "plantilla", destino],
                       capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    log(f"plantilla exit={r.returncode} stdout={r.stdout.strip()[:120]}")
    if r.returncode != 0:
        print(f"ERROR: verificacion_entradas.py plantilla exit={r.returncode}: {r.stderr.strip()[:200]}")
        return 1
    # fixtures del banco -> archivos del producto (fuentes_sinteticas/)
    for fx in rel["estado_inicial"]["fixtures"]:
        src = os.path.join(L.BANCO, fx["fixture_banco"])
        if not os.path.isfile(src):
            print(f"ERROR: falta el fixture del banco {fx['fixture_banco']}")
            return 1
        texto = open(src, encoding="utf-8").read()
        dst_rel = fx["archivo_producto"]
        if L.ruta_dentro(os.path.join(destino, "fuentes_sinteticas"), os.path.basename(dst_rel)) is None:
            print(f"ERROR: archivo_producto fuera de fuentes_sinteticas/: {dst_rel!r}")
            return 2
        p = L.materializar_fuente(None, destino, os.path.basename(dst_rel), texto)
        log(f"fixture {fx['fixture_banco']} -> {dst_rel} sha256={L.sha256_archivo(p)}")
    # estado inicial documentado
    with open(os.path.join(L.RUN_DIR, cid, "ESTADO_INICIAL.md"), "w", encoding="utf-8") as f:
        f.write(f"# Estado inicial preparado · {cid}\n\n")
        f.write(f"- expediente base (relativo a la candidata): `{exp_base_rel}`\n")
        f.write(f"- expediente de trabajo: `{destino}` (heredados archivados en `_heredados/`)\n")
        f.write(f"- registro: `verificacion_entradas.py plantilla` exit {r.returncode} (salida en verificacion_entradas.plantilla.json)\n")
        f.write(f"- fixtures cargados en el producto: {[fx['archivo_producto'] for fx in rel['estado_inicial']['fixtures']]}\n")
        if rel["estado_inicial"].get("aprobacion_de_partida"):
            f.write(f"- aprobación de partida: {rel['estado_inicial']['aprobacion_de_partida']}\n")
        f.write(f"- entrada_usuario (del banco, texto íntegro): {caso['entrada_usuario']}\n")
        f.write("- fases del personaje:\n")
        for fa in rel["fases"]:
            f.write(f"  {fa['orden']}. paso {fa['paso']} — {fa['fase']} · agente: {fa['agente']} · {fa['modelo']}/{fa['esfuerzo']} · código esperado {fa['codigo_esperado']} · salida: {fa['salida']}\n")
        f.write(f"- comando_relevo: `{rel['comando_relevo']}`\n")
        f.write("- artefacto por criterio: ver relevos_casos.json y PAQUETES_RELEVO.json (este caso)\n")
    print(f"OK estado inicial {cid}: {destino}")
    print(f"comando_relevo: {rel['comando_relevo']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
