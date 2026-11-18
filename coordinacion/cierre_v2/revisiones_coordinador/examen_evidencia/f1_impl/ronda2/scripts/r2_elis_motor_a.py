#!/usr/bin/env python3
"""Segunda ronda · el expediente real anterior a F1 `2026-11_Vidrala_ensayo_4_14/elis_motor_A/Elis` (motor A, NIIF, C49 = 128,1; en el paso 13,
esperando la auditoría; la fase C propone pendiente_de_datos), sobre COPIAS y con el código nuevo. La auditoría la escribe el agente simulado
de la batería (APROBADO). LibreOffice: ejecutar con flock (el paso 12 recalcula). Uso (desde personaje_v2/ de la copia NUEVA): r2_elis_motor_a.py DIR SALIDA.json"""
import json, os, shutil, subprocess, sys
PV = os.getcwd()
sys.path.insert(0, os.path.join(PV, "pruebas")); sys.path.insert(0, os.path.join(PV, "scripts")); sys.dont_write_bytecode = True
import agentes_sinteticos as AG
import motor_a_f1 as F1
ORIG = os.path.join(PV, "empresas_v2_correcciones", "2026-11_Vidrala_ensayo_4_14", "elis_motor_A", "Elis")
BASE, SALIDA = os.path.abspath(sys.argv[1]), sys.argv[2]
PIPE = os.path.join(PV, "scripts", "pipeline.py")
SAL = {}

def lanzar(c, *extra, max_vueltas=8):
    args = list(extra); log = []
    for _ in range(max_vueltas):
        r = subprocess.run([sys.executable, PIPE, c] + args, capture_output=True, text=True)
        args = []
        log.append((r.stdout + r.stderr).strip().splitlines()[-1][:300] if (r.stdout + r.stderr).strip() else "")
        if r.returncode != 10:
            return r.returncode, log
        nombre = open(os.path.join(c, "ESPERANDO.md"), encoding="utf-8").read().split("**")[1]
        if nombre != "verificacion":
            return 10, log + [f"espera a {nombre}: la sonda solo simula la auditoría"]
        AG.auditoria(c, "APROBADO")
    return 10, log + ["demasiadas vueltas"]

def foto(c, etiqueta, rc, log):
    st = json.load(open(os.path.join(c, "estado_pipeline.json"), encoding="utf-8"))
    fi = json.load(open(os.path.join(c, "ficha.json"), encoding="utf-8")) if os.path.exists(os.path.join(c, "ficha.json")) else None
    inf = open(os.path.join(c, "informe.md"), encoding="utf-8").read() if os.path.exists(os.path.join(c, "informe.md")) else ""
    d = {"codigo": rc, "ultimas_lineas": log[-3:], "estado": st.get("estado_analisis"), "paso": st.get("paso"), "auditoria": st.get("auditoria"), "motor_en_estado": st.get("motor"),
         "ficha_oficial": None if fi is None else {"estado": fi.get("estado_analisis"), "cubo": fi.get("cubo"), "accion": (fi.get("decision") or {}).get("accion"), "cierre": fi.get("cierre"),
                                                  "escalera": {k: (fi.get("escalera") or {}).get(k) for k in ("zona", "precio_si", "ponderado")} if fi.get("escalera") else None,
                                                  "bloque_f1": None if not isinstance(fi.get("motor_a_f1"), dict) else {k: fi["motor_a_f1"].get(k) for k in ("utilizable_para_conclusion", "vigencia")}},
         "informe_estado": next((l for l in inf.splitlines() if l.startswith("**Estado")), "")[:170],
         "vigencia_f1": F1.vigencia(c), "historial": [h[-220:] for h in st.get("historial", []) if ("F1" in h or "FIN" in h or "CIERRE" in h)][-3:]}
    SAL[etiqueta] = d
    print("--- " + etiqueta + "\n" + json.dumps(d, ensure_ascii=False, indent=1))

for nombre, extra in (("E1 · elis_motor_A reanudado sin opciones", ()), ("E2 · elis_motor_A con --reiniciar --desde 13", ("--reiniciar", "--desde", "13"))):
    d = os.path.join(BASE, nombre[:2]); shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    c = os.path.join(d, "Elis"); shutil.copytree(ORIG, c, symlinks=True)
    print(nombre, "· exención:", F1.exencion(c), "· exigido:", F1.exigido(c))
    if not extra:
        AG.auditoria(c, "APROBADO")   # la respuesta que el expediente esperaba
    rc, log = lanzar(c, *extra)
    foto(c, nombre, rc, log)
json.dump(SAL, open(SALIDA, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
