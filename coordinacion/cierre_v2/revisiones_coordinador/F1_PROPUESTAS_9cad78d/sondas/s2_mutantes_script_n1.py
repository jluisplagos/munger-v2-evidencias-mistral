"""Sonda 2 del revisor · mutantes sobre una copia de `n1_alcance_y_actualizacion.py`: ¿falla el script cuando debe?

Cada mutante cambia un literal, una página, una posición, una huella o una cifra de referencia en una COPIA del script
(en sondas/mut/) y lo ejecuta con los mismos argumentos. Se espera código de salida 1 (o salida abortada).
Uso: python3 -I s2_mutantes_script_n1.py <dir scripts del autor (copia)> <raiz munger_v2_r1> <dir release> <libro>
"""
import shutil
import subprocess
import sys
from pathlib import Path

SCR, RAIZ, REL, LIBRO = (Path(x) for x in sys.argv[1:5])
MUT = Path(__file__).with_name("mut")
ORIG = (SCR / "n1_alcance_y_actualizacion.py").read_text(encoding="utf-8")
MUTANTES = [
    ("M01 línea fiscal 2022: valor y literal 0,5 → 0,6", '"fiscal_earnout_2022": ("0.5", "URD2023", 345, "Adjustments and accretion of non-deductible earnouts", 0, 0, -1, "0.5", G)',
     '"fiscal_earnout_2022": ("0.6", "URD2023", 345, "Adjustments and accretion of non-deductible earnouts", 0, 0, -1, "0.6", G)'),
    ("M02 línea fiscal 2022: página 345 → 344", '"fiscal_earnout_2022": ("0.5", "URD2023", 345,', '"fiscal_earnout_2022": ("0.5", "URD2023", 344,'),
    ("M03 APM 2021 neto 3,7: posición −2 → −1 (columna de 2020)", '"3.7", "URD2021", 217, "Costs related to acquisitions and earnout adjustments(a)", 0, 0, -2, "3.7"',
     '"3.7", "URD2021", 217, "Costs related to acquisitions and earnout adjustments(a)", 0, 0, -1, "3.7"'),
    ("M04 APM 2021 neto: valor 3,7 → 4,5 con literal 3.7 (valor distinto del literal)", '("3.7", "URD2021", 217, "Costs related to acquisitions and earnout adjustments(a)"', '("4.5", "URD2021", 217, "Costs related to acquisitions and earnout adjustments(a)"'),
    ("M05 tipo teórico 2021: 28,41 → 25,83 (valor y literal)", '"tipo_teorico_2021": ("28.41", "URD2022", 326, "Theoretical tax rate", 0, 0, -1, "28.41%", G)',
     '"tipo_teorico_2021": ("25.83", "URD2022", 326, "Theoretical tax rate", 0, 0, -1, "25.83%", G)'),
    ("M06 huella de la presentación de 2024 alterada", "d733b56d6fd25e538d945da6434a0c90a4579fd291550558d2ff786cb2ec4e7d", "e733b56d6fd25e538d945da6434a0c90a4579fd291550558d2ff786cb2ec4e7d"),
    ("M07 pasivo 2024 cierre 23,9 → 23,1 (valor y literal)", '"deuda_adquisiciones_2024": ("23.9", "URD2025", 386, "Debt related to acquisitions", 1, 0, 0, "23.9", G)',
     '"deuda_adquisiciones_2024": ("23.1", "URD2025", 386, "Debt related to acquisitions", 1, 0, 0, "23.1", G)'),
    ("M08 conciliación 2024: actualización (5,6) → (6,5) (valor y literal)", '"rel_2024_actualizacion_earnout": ("-5.6", "REL_FY2024_PRES", 52, "Accretion expense for the earnout pertaining to the", 0, 1, 0, "(5.6)", G)',
     '"rel_2024_actualizacion_earnout": ("-6.5", "REL_FY2024_PRES", 52, "Accretion expense for the earnout pertaining to the", 0, 1, 0, "(6.5)", G)'),
    ("M09 referencia −11,190 → −11,290", 'Fr("-11.190")', 'Fr("-11.290")'),
    ("M10 regla N1 con signo contrario (suma el ajuste en lugar de quitarlo)", "n1 = lambda años, tipos=None: {y: [(-earn[y], (tipos or {}).get(y))] for y in años}",
     "n1 = lambda años, tipos=None: {y: [(earn[y], (tipos or {}).get(y))] for y in años}"),
    ("M11 pasaje inexistente", '"heavily impacted by non-deductible earnout adjustments"]', '"heavily impacted by deductible earnout adjustments"]'),
    ("M12 búsqueda sin resultado: página con línea de earnout (URD 2023 p.345 en lugar de URD 2022 p.326)", '("conciliación fiscal de 2021 en el URD 2022", "URD2022", 326)', '("conciliación fiscal de 2021 en el URD 2022", "URD2023", 345)'),
    ("M13 τ de proyección de la ventana en lugar de cinco años (cambia la convención E8.1 sin decirlo)", 'def calcular(aj, aj_bai=None, tau_proy="cinco_años"):', 'def calcular(aj, aj_bai=None, tau_proy="ventana"):'),
    ("M14 actualización tratada como deducible en el cuadre (sin ella debe NO cuadrar): quita la actualización del dato", 'act = {2023: F("FIN_ACTMEX_FR_2023"), 2024: F("FIN_ACTMEX_2024"), 2025: F("FIN_ACTMEX_2025")}', 'act = {2023: Fr(0), 2024: Fr(0), 2025: Fr(0)}'),
]
shutil.rmtree(MUT, ignore_errors=True)
MUT.mkdir()
for f in SCR.glob("*.py"):
    shutil.copy(f, MUT / f.name)
(MUT.parent / "mut_datos").mkdir(exist_ok=True)
base = ["--cifras", str(SCR.parent / "datos" / "cifras_fuente.csv"), "--verificacion", str(SCR.parent / "resultados" / "verificacion_cifras.json"),
        "--libro", str(LIBRO), "--copia", str(SCR.parent / "resultados" / "copia_investigacion_f1.json"), "--fuentes", str(SCR.parent / "datos" / "fuentes.json"),
        "--raiz", str(RAIZ), "--release", str(REL)]
no_detectados = 0
for nombre, a, b in MUTANTES:
    assert ORIG.count(a) == 1, (nombre, ORIG.count(a))
    (MUT / "n1_alcance_y_actualizacion.py").write_text(ORIG.replace(a, b), encoding="utf-8")
    r = subprocess.run([sys.executable, "-I", str(MUT / "n1_alcance_y_actualizacion.py"), *base, "--salida", str(MUT / "s.json"), "--informe", str(MUT / "s.md")],
                       capture_output=True, text=True)
    det = r.returncode != 0
    no_detectados += not det
    cola = (r.stdout.strip().splitlines() or r.stderr.strip().splitlines() or [""])[-1][:300]
    print(f"{'DETECTADO   ' if det else 'NO DETECTADO'} rc={r.returncode} · {nombre}\n      {cola}")
(MUT / "n1_alcance_y_actualizacion.py").write_text(ORIG, encoding="utf-8")
print(f"\nMutantes: {len(MUTANTES)}; no detectados: {no_detectados}")
