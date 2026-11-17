#!/usr/bin/env python3
"""Mutaciones del revisor sobre una COPIA (nunca sobre el repositorio): cada una cambia una línea de pipeline.py o de motor_a_f1.py, ejecuta la batería
obligatoria pruebas/test_motor_a_f1.py y restaura el archivo. Uso (desde personaje_v2/ de la copia): python3 -I mutaciones_revisor.py"""
import subprocess, sys
P = "scripts/pipeline.py"; M = "scripts/motor_a_f1.py"
orig_p = open(P, encoding="utf-8").read(); orig_m = open(M, encoding="utf-8").read()
def bateria():
    r = subprocess.run([sys.executable, "-B", "pruebas/test_motor_a_f1.py"], capture_output=True, text=True)
    return (r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-200:]), [l[:110] for l in r.stdout.splitlines() if l.startswith("FALLA")]
def mut(nombre, archivo, orig, viejo, nuevo):
    assert orig.count(viejo) >= 1, (nombre, "patrón no encontrado")
    open(archivo, "w", encoding="utf-8").write(orig.replace(viejo, nuevo, 1))
    try:
        print(f"{nombre} → {bateria()}")
    finally:
        open(archivo, "w", encoding="utf-8").write(orig)
mut("R1 gancho del pipeline desactivado (return False al entrar)", P, orig_p,
    "        import motor_a_f1 as F1\n        if self.st.get(\"motor\") != \"A\" or not F1.exigido(self.c):\n            return False\n",
    "        import motor_a_f1 as F1\n        return False\n        if self.st.get(\"motor\") != \"A\" or not F1.exigido(self.c):\n            return False\n")
mut("R2 el gancho trata el código 4 (límite del modelo: F1-LIBRO, V-F1a, US GAAP) como «sigue»", P, orig_p, "        if rc == 0:\n            return False\n        bl = ", "        if rc in (0, 4):\n            return False\n        bl = ")
mut("R3 A0 con C49 = 0 y ROU vacía se admite", M, orig_m, "        if rou_vacio_w and not c49_pos:\n", "        if False and rou_vacio_w and not c49_pos:\n")
mut("R4 F1-REGISTRO desactivada", M, orig_m, "        if val is not None and not _registro_ok(reg):", "        if False and val is not None and not _registro_ok(reg):")
mut("R5 compras proporcionales sin cargo en el año 11", M, orig_m, "        X11 = (lambda V11: a_prop * V11) if a_prop is not None else Fr(0)", "        X11 = Fr(0)")
mut("R6 V-F1c sin la transición en R_propia", M, orig_m, "rp = media(R_por[y][\"R_propia\"] + R_por[y][\"transicion\"] for y in ventana)", "rp = media(R_por[y][\"R_propia\"] for y in ventana)")
mut("R7 K3 no clasifica la ROU de A0 como doble cómputo", M, orig_m, "\"doble_computo\" if (k3_rou > 0 and c49_pos) else", "\"explicada\" if (k3_rou > 0 and c49_pos) else")
mut("R8 el CLI devuelve 0 con un bloqueo de falta de datos", M, orig_m, "    return 5 if \"implementacion\" in ep else 3 if ep == \"pendiente_de_datos\" else 4", "    return 5 if \"implementacion\" in ep else 0 if ep == \"pendiente_de_datos\" else 4")
mut("R9 ancla E4 sin restar X^v", M, orig_m, "+ (H[\"adq\"][y] or Fr(0)) for y in horiz) - xv", "+ (H[\"adq\"][y] or Fr(0)) for y in horiz)")
mut("R10 N1 no toca el EBIT del año base (m0)", M, orig_m, "        m0 = ebit[anios[-1]] / V0", "        m0 = H[\"EBIT\"][anios[-1]] / V0")
