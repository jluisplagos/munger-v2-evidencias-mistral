#!/usr/bin/env python3
"""ILUSTRACIÓN DEL REVISOR (no es una declaración ni una valoración): órdenes de magnitud de F1 en el libro de datos real de Ahold (paso 5 del
expediente 2026-11_examen_universo/ahold_4_15, solo lectura) con la amortización de derechos de uso leída en los informes anuales:
2023 (1.336) AR2023 PDF p.262 · 2024 (1.333) AR2024 PDF p.321 · 2025 (1.400) AR2025 PDF p.272. Sin verificar con verificacion_entradas.py.
Uso: ilustracion_ahold.py RUTA_personaje_v2 LIBRO_AHOLD"""
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, sys.argv[1] + "/scripts")
import motor_a_f1 as M
L = M.leer_libro(sys.argv[2])
print("libro sha256:", L["sha256"][:16], "· L4:", L.get("Control maestro!L4"), "· C49:", L.get("Análisis!C49"), "· C70 (FCF base):", L.get("Historia!C70"),
      "· C53 (ancla S2C A0):", repr(L.get("Historia!C53")), "· C76 (reinversión neta media):", L.get("Historia!C76"), "· C63:", L.get("Historia!C63"))
REG = {"fecha": "2026-11-17", "persona": "ILUSTRACIÓN DEL REVISOR", "motivo": "orden de magnitud"}
rou = {"2023": (-1336, "AR2023 PDF p.262"), "2024": (-1333, "AR2024 PDF p.321"), "2025": (-1400, "AR2025 PDF p.272")}
d = {"norma_contable": {"valor": "NIIF", "registro": REG}, "perimetro_reinversion": {"valor": "A1_sin_ROU", "registro": REG},
     "series": {"da_rou": {y: {"valor_fuente": v, "signo": -1, "tratamiento": "publicado entre paréntesis", "documento": doc, "pagina": 1} for y, (v, doc) in rou.items()}}}
r = M.evaluar(L, d, motor_libro="A")
for k, v in r["diagnostico_por_perimetro"].items():
    print(f"  {k}: f {v['f']:.6f} · flujo sin crecimiento {v['flujo_sin_crecimiento']:.1f} · ancla S2C {v['ancla_s2c_E4']}")
print("  diferencias frente a A0:", r["diferencias_frente_a_A0_flujo_sin_crecimiento"])
print("  materialidad V-F1a:", r["materialidad_V_F1a"])
# motor B: coste de la deuda C63 con y sin el interés de los arrendamientos (465 en 2025, AR2025 PDF p.212)
rows = {k: L.get(f"Historia!{k}") for k in ("L15", "K22", "L22", "K23", "L23", "C64")}
dm = (rows["K22"] + rows["K23"] + rows["L22"] + rows["L23"]) / 2
kd0, kd1 = rows["L15"] / dm, (rows["L15"] + 465) / dm
E = 36.05 * 905; D = rows["C64"]; t = L.get("Historia!C52"); rr = 0.09
print(f"  motor B · C63 = {kd0:.4%} (intereses {rows['L15']} ÷ deuda media con arrendamientos {dm:.0f}); con el interés de arrendamientos (465): {kd1:.4%}")
print(f"  motor B · r operativa (fórmula de Diagnóstico V6!C15, capitalización 36,05 × 905): {(rr*E + kd0*(1-t)*D)/(E+D):.4%} → {(rr*E + kd1*(1-t)*D)/(E+D):.4%}")
