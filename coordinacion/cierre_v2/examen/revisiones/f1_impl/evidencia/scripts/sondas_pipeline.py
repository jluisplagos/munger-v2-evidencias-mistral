#!/usr/bin/env python3
"""Sondas del revisor sobre el gancho F1 del pipeline, con la empresa sintética (NIIF, motor A, C49 = 3,71 > 0, pasivo por arrendamientos 50)
y los agentes simulados de la batería. LibreOffice: ejecutar con flock /home/user/e_work/libreoffice.lock.
Uso (desde personaje_v2/ de la COPIA): python3 -B sondas_pipeline.py DIR_TRABAJO SALIDA.json"""
import json, os, shutil, subprocess, sys
PV = os.getcwd()
sys.path.insert(0, os.path.join(PV, "pruebas"))
sys.dont_write_bytecode = True
import test_pipeline_sintetico as TS

TS.BASE = os.path.abspath(sys.argv[1])
os.makedirs(TS.BASE, exist_ok=True)
SAL = {}

def resumen(c, etiqueta):
    st = TS.estado(c)
    fi = json.load(open(os.path.join(c, "ficha.json"), encoding="utf-8")) if os.path.exists(os.path.join(c, "ficha.json")) else {}
    inf = open(os.path.join(c, "informe.md"), encoding="utf-8").read() if os.path.exists(os.path.join(c, "informe.md")) else ""
    linea = next((l for l in inf.splitlines() if l.startswith("**Estado")), "")
    f1 = fi.get("motor_a_f1")
    d = {"estado_pipeline": st.get("estado_analisis"), "paso": st.get("paso"), "auditoria": st.get("auditoria"), "motor": st.get("motor"),
         "motor_a_f1_en_estado": st.get("motor_a_f1"),
         "ficha": {k: fi.get(k) for k in ("estado_analisis", "cubo", "motor", "valor_ponderado", "precio")},
         "ficha_decision": {k: (fi.get("decision") or {}).get(k) for k in ("accion", "precio_objetivo")} if fi.get("decision") else None,
         "ficha_cierre": fi.get("cierre"),
         "ficha_escalera": {k: (fi.get("escalera") or {}).get(k) for k in ("precio", "zona", "precio_si", "ponderado")} if fi.get("escalera") else None,
         "ficha_valores_por_accion": {e: (fi.get("escenarios") or {}).get(e, {}).get("valor_accion") for e in ("MALO", "NORMAL", "BUENO")} if fi else None,
         "ficha_bloque_motor_a_f1": ({"utilizable": f1.get("utilizable_para_conclusion"), "bloquean": sorted({g["id"] for g in f1.get("bloquean") or []})} if isinstance(f1, dict) else None),
         "informe_linea_estado": linea[:400],
         "informe_linea_F1": next((l for l in inf.splitlines() if "Motor A · F1" in l), None)}
    SAL[etiqueta] = d
    print(f"--- {etiqueta}\n" + json.dumps(d, ensure_ascii=False, indent=1))
    return st

def lanzar(c, reac, *extra, max_vueltas=30):
    """Como TS.correr, con argumentos adicionales solo en la primera llamada (p. ej. --desde N)."""
    args = list(extra)
    rc = None
    for _ in range(max_vueltas):
        r = subprocess.run([TS.PY, TS.PIPE, c] + args, capture_output=True, text=True)
        args = []
        rc = r.returncode
        if rc != 10:
            return rc, (r.stdout + r.stderr)
        esp = open(os.path.join(c, "ESPERANDO.md"), encoding="utf-8").read()
        reac(c, esp.split("**")[1])
    return rc, "demasiadas vueltas"

reac = TS.reaccion_normal()
# ---------------- PA: expediente SIN entrada_efectiva.json ni motor_a_f1.json (F1 no se exige), con arrendamientos, precio favorable
c = TS.preparar("EmpresaX_PA", precio=8)
rc, out = lanzar(c, reac)
print("PA código", rc, "·", out.strip().splitlines()[-1][:200] if out.strip() else "")
resumen(c, "PA · sin entrada_efectiva.json ni declaración (F1 no exigido) · empresa NIIF con C49 > 0 · precio 8")
import openpyxl
ev = os.path.join(c, "recalc", "EmpresaX_PA_v63_evaluada.xlsx")
if os.path.exists(ev):
    wb = openpyxl.load_workbook(ev, data_only=True, read_only=True)
    SAL["PA_libro"] = {"Análisis!C49": wb["Análisis"]["C49"].value, "Análisis!C52": wb["Análisis"]["C52"].value, "Historia!L23 (pasivo arrendamientos)": wb["Historia"]["L23"].value,
                       "Historia!L17 (principal)": wb["Historia"]["L17"].value, "Historia!C58 (f, A0)": wb["Historia"]["C58"].value, "Control maestro!L4": wb["Control maestro"]["L4"].value}
    print(json.dumps(SAL["PA_libro"], ensure_ascii=False))
    wb.close()

# ---------------- PB: expediente 4.15 (entrada_efectiva.json), sin declaración F1: bloqueo en el paso 7; después --desde 8 y --desde 13
c = TS.preparar("EmpresaX_PB", precio=8)
json.dump({"modo": "registrada", "motivo": "sonda del revisor: el valor de la etapa 1 prevalece en la empresa sintética"}, open(os.path.join(c, "entrada_efectiva.json"), "w", encoding="utf-8"))
rc, out = lanzar(c, reac)
print("PB-1 código", rc, "·", out.strip().splitlines()[-1][:300] if out.strip() else "")
resumen(c, "PB-1 · 4.15 sin declaración F1: primera pasada")
rc, out = lanzar(c, reac, "--desde", "8")
print("PB-2 código", rc, "·", out.strip().splitlines()[-1][:300] if out.strip() else "")
resumen(c, "PB-2 · relanzado con --desde 8 (se salta el gancho del paso 7)")
rc, out = lanzar(c, reac, "--desde", "13")
print("PB-3 código", rc, "·", out.strip().splitlines()[-1][:300] if out.strip() else "")
st = resumen(c, "PB-3 · relanzado con --desde 13 (se salta el gancho del paso 12)")
SAL["PB_historial_final"] = [h for h in st.get("historial", []) if "F1" in h or "FIN" in h or "CIERRE" in h][-12:]
json.dump(SAL, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("escrito", sys.argv[2])
