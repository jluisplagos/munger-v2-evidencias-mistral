"""Revisor: emula el sello de C46 (como lo escribiría `sellar`) en una COPIA ya recalculada, simula otra fase B (C76 = 140), recalcula y
mira qué dice verificacion_entradas.comprobar de C46."""
import datetime as dt, json, os, subprocess, sys
PV, C = sys.argv[1:3]
sys.path.insert(0, os.path.join(PV, "scripts")); os.environ["MUNGER_CONFIG"] = os.path.join(PV, "config_v2_v631_f1.json")
import verificacion_entradas as VE  # noqa: E402
from v63_xml import LibroV63  # noqa: E402
hoy = dt.datetime.now().astimezone().date().isoformat()
p = os.path.join(C, VE.REGISTRO); reg = json.load(open(p, encoding="utf-8"))
e = next(x for x in reg["entradas"] if x["celda"] == "Análisis!C46")
e["comprobacion"].update(revisor="Revisor emulado (prueba)", resultado="verificado", fuente_examinada="registro, AR2024 y AR2025 (prueba)", fecha=hoy)
open(p, "w", encoding="utf-8").write(json.dumps(reg, ensure_ascii=False, indent=1))
h = VE.huellas_registro(C)["Análisis!C46"]
reg = json.load(open(p, encoding="utf-8")); e = next(x for x in reg["entradas"] if x["celda"] == "Análisis!C46")
e["comprobacion"]["vinculo"] = {"huella": h, "elementos": VE.ELEMENTOS_VINCULO, "sellado_por": "Revisor emulado (prueba)", "fecha": hoy, "sellado_en": "emulado"}
open(p, "w", encoding="utf-8").write(json.dumps(reg, ensure_ascii=False, indent=1))
def estado(r, k):
    for cat in ("comprobadas", "pendientes", "desactualizadas", "discrepancias", "errores"):
        for x in r.get(cat) or []:
            if (x == k) or str(x).startswith(k + ": "):
                return cat, str(x)[:230]
    return None, None
print("sellado (emulado), antes de otra fase B:", estado(VE.comprobar(C), "Análisis!C46"))
lb = LibroV63(os.path.join(C, "Jumbo_v63_evaluada.xlsx")); lb.escribir("Análisis", "C76", 140); lb.marcar_modificada("Análisis"); lb.guardar(os.path.join(C, "Jumbo_v63_evaluada.xlsx"))
r = subprocess.run([sys.executable, "-B", os.path.join(PV, "scripts", "entradas_dependientes.py"), "aplicar", C, "--fase", "B"], capture_output=True, text=True)
print("aplicar con C76 = 140:", r.stdout.strip().splitlines()[-1][:220])
reg = json.load(open(p, encoding="utf-8")); e = next(x for x in reg["entradas"] if x["celda"] == "Análisis!C46")
print("comprobación tras el recálculo (no la toca):", {k: e["comprobacion"].get(k) for k in ("revisor", "resultado", "fecha")}, "· vínculo intacto:", e["comprobacion"]["vinculo"]["huella"] == h)
print("después:", estado(VE.comprobar(C), "Análisis!C46"))
