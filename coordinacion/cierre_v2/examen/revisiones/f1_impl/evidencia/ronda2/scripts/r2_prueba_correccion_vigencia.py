#!/usr/bin/env python3
"""Segunda ronda · PROPUESTA del revisor, probada solo en una copia: en motor_a_f1.vigencia(), si el estado del pipeline no dice el motor, se toma
de fase_a.json (C62). Se aplica el cambio a la copia, se repiten A3, PC2-4 y E2 y la batería F1, y se restaura el archivo.
LibreOffice: ejecutar con flock. Uso (desde personaje_v2/ de la copia NUEVA): r2_prueba_correccion_vigencia.py DIR_R2"""
import json, os, shutil, subprocess, sys
PV = os.getcwd(); R2 = os.path.abspath(sys.argv[1])
M = os.path.join(PV, "scripts", "motor_a_f1.py")
orig = open(M, encoding="utf-8").read()
viejo = '''    out = {"motor": motor, "exento": exencion(carpeta)}
    if motor != "A":
'''
nuevo = '''    if motor is None:
        fa = _json(os.path.join(carpeta, "fase_a.json"))
        c62 = ((fa.get("celdas") or {}) if isinstance(fa, dict) else {}).get("C62")
        motor = {"Sí": "A", "No · financiación cambia mucho": "B", "No · banco o aseguradora": "C"}.get(c62)
    out = {"motor": motor, "exento": exencion(carpeta)}
    if motor != "A":
'''
assert orig.count(viejo) == 1
sys.path.insert(0, os.path.join(PV, "pruebas")); sys.dont_write_bytecode = True
import agentes_sinteticos as AG
import test_pipeline_sintetico as TS
PIPE = os.path.join(PV, "scripts", "pipeline.py")
reac = TS.reaccion_normal()
def lanzar(c, *extra, solo_auditoria=False):
    args = list(extra); log = []
    for _ in range(30):
        r = subprocess.run([sys.executable, PIPE, c] + args, capture_output=True, text=True); args = []
        log.append((r.stdout + r.stderr).strip().splitlines()[-1][:230] if (r.stdout + r.stderr).strip() else "")
        if r.returncode != 10:
            return r.returncode, log
        nombre = open(os.path.join(c, "ESPERANDO.md"), encoding="utf-8").read().split("**")[1]
        if solo_auditoria:
            if nombre != "verificacion":
                return 10, log + [f"espera a {nombre}"]
            AG.auditoria(c, "APROBADO")
        else:
            reac(c, nombre)
    return 10, log
def foto(c, etiqueta, rc, log):
    st = json.load(open(os.path.join(c, "estado_pipeline.json"), encoding="utf-8"))
    fi = json.load(open(os.path.join(c, "ficha.json"), encoding="utf-8")) if os.path.exists(os.path.join(c, "ficha.json")) else {}
    print(f"{etiqueta}: código {rc} · estado {st.get('estado_analisis')} · paso {st.get('paso')} · ficha oficial: {fi.get('estado_analisis')} / cubo {fi.get('cubo')} / acción {(fi.get('decision') or {}).get('accion')} / cierre {bool(fi.get('cierre'))} · {log[-1][:170]}")
open(M, "w", encoding="utf-8").write(orig.replace(viejo, nuevo))
try:
    r = subprocess.run([sys.executable, "-B", os.path.join(PV, "pruebas", "test_motor_a_f1.py")], capture_output=True, text=True, cwd=PV)
    print("batería F1 con la propuesta:", r.stdout.strip().splitlines()[-1])
    base = os.path.join(R2, "ataques_correccion"); shutil.rmtree(base, ignore_errors=True)
    # A3
    c = os.path.join(base, "a3", "EmpresaY"); os.makedirs(os.path.dirname(c)); shutil.copytree(os.path.join(R2, "sint_antiguo", "EmpresaY"), c, symlinks=True)
    rc, log = lanzar(c, "--reiniciar", "--desde", "13"); foto(c, "A3 con la propuesta (--reiniciar --desde 13, expediente anterior a F1 con arrendamientos)", rc, log)
    # PC2-4
    c = os.path.join(base, "pc", "EmpresaX_PC"); os.makedirs(os.path.dirname(c)); shutil.copytree(os.path.join(R2, "ataques_pc", "_respaldo_PC"), c, symlinks=True)
    os.remove(os.path.join(c, "motor_a_f1_resultado.json"))
    rc, log = lanzar(c, "--reiniciar", "--desde", "13"); foto(c, "PC2-4 con la propuesta (resultado F1 borrado, declaración que bloquea)", rc, log)
    # E2
    c = os.path.join(base, "e2", "Elis"); os.makedirs(os.path.dirname(c))
    shutil.copytree(os.path.join(PV, "empresas_v2_correcciones", "2026-11_Vidrala_ensayo_4_14", "elis_motor_A", "Elis"), c, symlinks=True)
    rc, log = lanzar(c, "--reiniciar", "--desde", "13", solo_auditoria=True); foto(c, "E2 con la propuesta (elis_motor_A, --reiniciar --desde 13)", rc, log)
    # caso legítimo: la pasada normal del expediente sintético exento sigue cerrando
    TS.BASE = os.path.join(base, "base")
    c = TS.preparar("EmpresaX_ok", precio=8)
    rc, log = lanzar(c); foto(c, "línea de base sintética (exenta) con la propuesta", rc, log)
finally:
    open(M, "w", encoding="utf-8").write(orig)
    print("archivo restaurado:", open(M, encoding="utf-8").read() == orig)
