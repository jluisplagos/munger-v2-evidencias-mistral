"""Sonda 3c del revisor · mutantes sobre una copia de `umbral_v_f1a_frontera.py`: ¿falla cuando cambia la regla o un estado esperado?"""
import shutil, subprocess, sys
from pathlib import Path
SCR = Path(sys.argv[1])
MUT = Path(__file__).with_name("mut_umbral")
ORIG = (SCR / "umbral_v_f1a_frontera.py").read_text(encoding="utf-8")
M = [
 ("U01 umbral propuesto 0,1 % → 0,2 % en la regla", '"UP01": ("propuesta: e ≤ 0,1 % del FCF base", Fr(1, 1000))', '"UP01": ("propuesta: e ≤ 0,1 % del FCF base", Fr(2, 1000))'),
 ("U02 frontera estricta en la regla (X < u·FCF)", "dentro = X < u * fcf if variante == \"frontera estricta en el umbral sobre el FCF base\" else X <= u * fcf", "dentro = X < u * fcf"),
 ("U03 valor absoluto del FCF base y sin guarda", "        if fcf <= 0 and variante != \"sin la guarda del FCF base no positivo\":\n            return BLQ, \"FCF base no positivo: la medida no está definida y no hay exención\"\n", "        fcf = abs(fcf)\n"),
 ("U04 media sustituida por el último año", "    X = sum(rou) / len(rou)\n    if X == 0 and c49 == 0:", "    X = rou[-1]\n    if X == 0 and c49 == 0:"),
 ("U05 estado esperado de F07 cambiado (AVISO → BLOQUEA con la propuesta)", 'componentes=comp(1, 3)), [BLQ, AVI, BLQ, AVI, AVI, AVI]),\n    ("F08"', 'componentes=comp(1, 3)), [BLQ, BLQ, BLQ, AVI, AVI, AVI]),\n    ("F08"'),
 ("U06 V-F1m ignorado (solo uno positivo pasa al umbral)", '    if (X == 0 or c49 == 0) and variante != "dominio de A0 con «y» en lugar de «o»":\n        return VM,', '    if False:\n        return VM,'),
]
shutil.rmtree(MUT, ignore_errors=True); MUT.mkdir()
for f in SCR.glob("*.py"): shutil.copy(f, MUT / f.name)
for nombre, a, b in M:
    assert ORIG.count(a) == 1, (nombre, ORIG.count(a))
    (MUT / "umbral_v_f1a_frontera.py").write_text(ORIG.replace(a, b), encoding="utf-8")
    r = subprocess.run([sys.executable, "-I", str(MUT / "umbral_v_f1a_frontera.py"), "--salida", str(MUT / "s.json"), "--informe", str(MUT / "s.md")], capture_output=True, text=True)
    print(f"{'DETECTADO   ' if r.returncode else 'NO DETECTADO'} rc={r.returncode} · {nombre}\n      {((r.stdout.strip().splitlines() or r.stderr.strip().splitlines() or [''])[-1])[:300]}")
(MUT / "umbral_v_f1a_frontera.py").write_text(ORIG, encoding="utf-8")
