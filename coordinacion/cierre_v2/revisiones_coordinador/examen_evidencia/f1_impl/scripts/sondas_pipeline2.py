#!/usr/bin/env python3
"""Sonda PC del revisor: ¿el cierre (pasos 13–14) comprueba F1? Empresa sintética SIN arrendamientos ni PPA y con la declaración F1 completa (A0):
el paso 7 pasa. Cuando el pipeline espera a la fase C, la declaración cambia a un estado que BLOQUEA (perímetro A2: F1-LIBRO). El paso 12 termina en
no_entregable. Después se relanza con --desde 13. LibreOffice: ejecutar con flock. Uso (desde personaje_v2/ de la COPIA): sondas_pipeline2.py DIR SALIDA.json"""
import json, os, subprocess, sys
PV = os.getcwd()
sys.path.insert(0, os.path.join(PV, "pruebas"))
sys.dont_write_bytecode = True
import test_pipeline_sintetico as TS
TS.BASE = os.path.abspath(sys.argv[1]); os.makedirs(TS.BASE, exist_ok=True)
REG = {"fecha": "2026-11-17", "persona": "sonda del revisor", "motivo": "sonda"}
SAL = {}

def declaracion(per="A0_total"):
    cero = {str(y): {"valor_fuente": 0, "signo": 1, "tratamiento": "ninguno", "documento": "informe anual sintético", "pagina": 1} for y in range(2016, 2026)}
    return {"norma_contable": {"valor": "NIIF", "registro": REG}, "perimetro_reinversion": {"valor": per, "registro": REG},
            "perimetro_margen": {"valor": "EBIT_NIIF16_PPA_constante", "registro": REG}, "perimetro_palancas_s2c": {"valor": per, "registro": REG},
            "perimetro_roic": {"valor": per, "registro": REG}, "clasificacion_compras": {"valor": "sin_compras", "registro": REG},
            "transicion": {"conocida": False, "tratamiento": None, "registro": REG}, "series": {"da_rou": cero, "da_ppa": dict(cero)}}

def resumen(c, etiqueta):
    st = TS.estado(c)
    fi = json.load(open(os.path.join(c, "ficha.json"), encoding="utf-8")) if os.path.exists(os.path.join(c, "ficha.json")) else {}
    inf = open(os.path.join(c, "informe.md"), encoding="utf-8").read() if os.path.exists(os.path.join(c, "informe.md")) else ""
    f1 = fi.get("motor_a_f1")
    d = {"estado_pipeline": st.get("estado_analisis"), "paso": st.get("paso"), "auditoria": st.get("auditoria"), "motor_a_f1_en_estado": st.get("motor_a_f1"),
         "ficha": {k: fi.get(k) for k in ("estado_analisis", "cubo", "valor_ponderado", "precio")},
         "ficha_decision": {k: (fi.get("decision") or {}).get(k) for k in ("accion", "precio_objetivo")} if fi.get("decision") else None,
         "ficha_cierre": fi.get("cierre"),
         "ficha_escalera": {k: (fi.get("escalera") or {}).get(k) for k in ("precio", "zona", "precio_si", "ponderado")} if fi.get("escalera") else None,
         "ficha_bloque_motor_a_f1": ({"utilizable": f1.get("utilizable_para_conclusion"), "bloquean": sorted({g["id"] for g in f1.get("bloquean") or []}),
                                      "perimetro_declarado": f1.get("perimetro_declarado")} if isinstance(f1, dict) else None),
         "informe_linea_estado": next((l for l in inf.splitlines() if l.startswith("**Estado")), "")[:260],
         "informe_linea_F1": next((l for l in inf.splitlines() if "Motor A · F1" in l), None)}
    SAL[etiqueta] = d
    print(f"--- {etiqueta}\n" + json.dumps(d, ensure_ascii=False, indent=1))
    return st

def lanzar(c, reac, *extra, max_vueltas=40):
    args = list(extra)
    for _ in range(max_vueltas):
        r = subprocess.run([TS.PY, TS.PIPE, c] + args, capture_output=True, text=True)
        args = []
        if r.returncode != 10:
            return r.returncode, (r.stdout + r.stderr)
        reac(c, open(os.path.join(c, "ESPERANDO.md"), encoding="utf-8").read().split("**")[1])
    return 10, "demasiadas vueltas"

normal = TS.reaccion_normal()
cambiada = {"hecho": False}
def reac(c, nombre):
    if nombre == "fase_c_turno1" and not cambiada["hecho"]:
        json.dump(declaracion("A2_propio"), open(os.path.join(c, "motor_a_f1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        cambiada["hecho"] = True
        print("   [sonda] la declaración F1 cambia a A2_propio mientras se espera a la fase C (el libro V6.3 calcula A0 → F1-LIBRO)")
    normal(c, nombre)

c = TS.preparar("EmpresaX_PC", precio=8, quitar_etapa1=("C49",))
json.dump({"modo": "registrada", "motivo": "sonda del revisor"}, open(os.path.join(c, "entrada_efectiva.json"), "w", encoding="utf-8"))
p = os.path.join(c, "fase1_v63.json"); f1 = json.load(open(p, encoding="utf-8"))
f1["analisis"]["C49"]["valor"] = 0
for k in ("arrendamientos_principal", "arrendamientos"):
    if f1["historia"]["partidas"].get(k):
        f1["historia"]["partidas"][k]["valores"] = [0] * 10
json.dump(f1, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(declaracion("A0_total"), open(os.path.join(c, "motor_a_f1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
rc, out = lanzar(c, reac)
print("PC-1 código", rc, "·", out.strip().splitlines()[-1][:300] if out.strip() else "")
resumen(c, "PC-1 · F1 pasa en el paso 7; la declaración cambia antes del paso 12")
rc, out = lanzar(c, reac, "--desde", "13")
print("PC-2 código", rc, "·", out.strip().splitlines()[-1][:300] if out.strip() else "")
st = resumen(c, "PC-2 · relanzado con --desde 13 tras el bloqueo F1 del paso 12")
SAL["PC_historial"] = [h for h in st.get("historial", []) if ("F1" in h or "FIN" in h or "CIERRE" in h or "auditor" in h.lower())][-14:]
print("\n".join(SAL["PC_historial"]))
json.dump(SAL, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
