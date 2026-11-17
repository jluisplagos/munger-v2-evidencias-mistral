"""Sonda 2b del revisor · mutantes sobre cifras NUEVAS (opciones B y A′, residuo de 2024, cierre de 2023): ¿tienen control propio?
Mismo mecanismo que s2 (copia en sondas/mut/). Un «NO DETECTADO» aquí no es un error de las cifras (la sonda 1 las
recalcula por otra vía): indica que esa cifra del documento no está protegida por un control del script."""
import shutil, subprocess, sys
from pathlib import Path
SCR, RAIZ, REL, LIBRO = (Path(x) for x in sys.argv[1:5])
MUT = Path(__file__).with_name("mut")
ORIG = (SCR / "n1_alcance_y_actualizacion.py").read_text(encoding="utf-8")
M = [
 ("N01 opción B calculada con 2021 en lugar de 2022", '"B · N1 en 2022–25 (los ejercicios de τ con ajuste no deducible según lo publicado)": calcular(n1((2022,) + VENT)),',
  '"B · N1 en 2022–25 (los ejercicios de τ con ajuste no deducible según lo publicado)": calcular(n1((2021,) + VENT)),'),
 ("N02 opción A′ con el tipo de 2021 a cero (equivale a A)", "calcular(n1(HOR, {2021: t21})),", "calcular(n1(HOR, {2021: Fr(0)})),"),
 ("N03 sensibilidad de 2022 con el signo del efecto fiscal cambiado", "calcular(n1((2022,) + VENT, {2022: t22}))}", "calcular(n1((2022,) + VENT, {2022: -t22}))}"),
 ("N04 pagos de 2024 con 10 de más en la conciliación del pasivo", 'pagos = {2023: -F("ADQ_EARNDIF_FR_2023"), 2024: -F("ADQ_EARNDIF_2024"), 2025: -F("ADQ_EARNDIF_2025")}',
  'pagos = {2023: -F("ADQ_EARNDIF_FR_2023"), 2024: -F("ADQ_EARNDIF_2024") + 10, 2025: -F("ADQ_EARNDIF_2025")}'),
 ("N05 cierre de 2023 con altas de 2023 = −2,4 (precio − desembolso) en lugar de «n. d.» = 0", 'cuadre(2023, LV["deuda_adquisiciones_2022"], LV["deuda_adquisiciones_2023_ed_anterior"], None, 5,',
  'cuadre(2023, LV["deuda_adquisiciones_2022"], LV["deuda_adquisiciones_2023_ed_anterior"], LV["precio_compras_2023"] + LV["desembolso_compras_2023"], 7,'),
]
shutil.rmtree(MUT, ignore_errors=True); MUT.mkdir()
for f in SCR.glob("*.py"): shutil.copy(f, MUT / f.name)
base = ["--cifras", str(SCR.parent / "datos" / "cifras_fuente.csv"), "--verificacion", str(SCR.parent / "resultados" / "verificacion_cifras.json"),
        "--libro", str(LIBRO), "--copia", str(SCR.parent / "resultados" / "copia_investigacion_f1.json"), "--fuentes", str(SCR.parent / "datos" / "fuentes.json"),
        "--raiz", str(RAIZ), "--release", str(REL)]
for nombre, a, b in M:
    assert ORIG.count(a) == 1, (nombre, ORIG.count(a))
    (MUT / "n1_alcance_y_actualizacion.py").write_text(ORIG.replace(a, b), encoding="utf-8")
    r = subprocess.run([sys.executable, "-I", str(MUT / "n1_alcance_y_actualizacion.py"), *base, "--salida", str(MUT / "s.json"), "--informe", str(MUT / "s.md")], capture_output=True, text=True)
    import json
    extra = ""
    try:
        d = json.loads((MUT / "s.json").read_text(encoding="utf-8"))
        if nombre.startswith("N05"):
            extra = " | 2023 (URD 2023): " + str({k: v for k, v in d["B_actualizacion_del_earnout"]["pasivo_ligado_a_adquisiciones"]["2023 · con el cierre del URD 2023"].items() if k.startswith(("saldo_calc", "residuo", "dentro"))})
        if nombre.startswith("N04"):
            extra = " | 2024: " + str({k: v for k, v in d["B_actualizacion_del_earnout"]["pasivo_ligado_a_adquisiciones"]["2024 · con el URD 2025 (precio definitivo y cierre reexpresado)"].items() if k.startswith(("residuo", "dentro"))})
    except Exception as e:
        extra = f" | (sin salida: {e})"
    print(f"{'DETECTADO   ' if r.returncode else 'NO DETECTADO'} rc={r.returncode} · {nombre}{extra}\n      {(r.stdout.strip().splitlines() or [''])[-1][:260]}")
(MUT / "n1_alcance_y_actualizacion.py").write_text(ORIG, encoding="utf-8")
