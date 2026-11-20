"""Sonda 3 del revisor · umbral de V-F1a: implementación independiente de la regla propuesta, los 30 casos del autor,
mutantes de implementación y casos de frontera adicionales.

No ejecuta `evaluar` del autor: solo toma de su script la lista CASOS (entradas y estado esperado) y OPCIONES.
Uso: python3 -I s3_umbral_independiente.py <dir scripts del autor (copia)> [cifras.csv libro.xlsx]
"""
import importlib.util
import sys
from fractions import Fraction as Fr
from pathlib import Path

SCR = Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("autor", SCR / "umbral_v_f1a_frontera.py")
A = importlib.util.module_from_spec(spec)
spec.loader.exec_module(A)
OPC = list(A.OPCIONES)                       # U0, UP01, UR, UP1, UP5, UV1
U = {"UP01": Fr(1, 1000), "UP1": Fr(1, 100), "UP5": Fr(5, 100)}


def q(x):
    return None if x is None else Fr(str(x))


def cota(componentes):
    tot = Fr(0)
    for año in componentes:
        neto = {}
        for ident, coef, dec in año:
            neto[ident] = (neto.get(ident, (Fr(0), dec))[0] + coef, dec)
        tot += sum(abs(c) * Fr(1, 2) * Fr(10) ** (-d) for c, d in neto.values())
    return tot / len(componentes)


def regla(c, o, mut=None):
    """Regla de la propuesta (§4 y §6), escrita desde el texto del documento. `mut` = mutante de implementación."""
    if c.get("motor", "A") != "A" or c.get("perimetro", "A0_total") != "A0_total":
        return "no aplica"
    rou, c49 = [q(x) for x in c["rou"]], q(c["c49"])
    if c49 < 0 or any(x is not None and x < 0 for x in rou):
        return "V-F1e BLOQUEA"
    if any(x is None for x in rou):
        return "V-F1b BLOQUEA" if c49 > 0 else "fuera de E5"
    n, suma = len(rou), sum(rou)
    if suma == 0 and c49 == 0:
        return "A0 admisible"
    if suma == 0 or c49 == 0:
        return "V-F1m BLOQUEA"
    fcf = q(c["fcf"])
    ventas = [q(v) for v in c["ventas"]]
    if o == "U0":
        return "V-F1a BLOQUEA"
    if o == "UR":
        return "V-F1a AVISO" if suma <= n * cota(c["componentes"]) else "V-F1a BLOQUEA"
    if o == "UV1":
        return "V-F1a BLOQUEA" if suma * len(ventas) >= Fr(5, 1000) * sum(ventas) * n else "V-F1a AVISO"
    u = U[o]
    if mut == "división sin guarda (e = X/FCF ≤ u)":
        if fcf == 0:
            return "ERROR división por cero"
        return "V-F1a AVISO" if (suma / n) / fcf <= u else "V-F1a BLOQUEA"
    if mut == "coma flotante":
        return "V-F1a AVISO" if float(fcf) > 0 and sum(float(x) for x in rou) / n / float(fcf) <= float(u) else "V-F1a BLOQUEA"
    if mut == "suma sin dividir por n":
        return "V-F1a AVISO" if suma <= u * fcf else "V-F1a BLOQUEA"
    if mut == "último año en lugar de la media":
        return "V-F1a AVISO" if rou[-1] <= u * fcf else "V-F1a BLOQUEA"
    if mut == "máximo en lugar de la media":
        return "V-F1a AVISO" if max(rou) <= u * fcf else "V-F1a BLOQUEA"
    if mut == "C49 en lugar de la D&A ROU":
        return "V-F1a AVISO" if c49 <= u * fcf else "V-F1a BLOQUEA"
    if mut == "frontera estricta (<)":
        return "V-F1a AVISO" if suma < u * n * fcf else "V-F1a BLOQUEA"
    if mut == "denominador FCF base + X (flujo sin el doble cómputo)":
        return "V-F1a AVISO" if fcf > 0 and suma <= u * n * (fcf + suma / n) else "V-F1a BLOQUEA"
    if mut == "ρ sobre ventas con el umbral del flujo":
        return "V-F1a AVISO" if suma * len(ventas) <= u * sum(ventas) * n else "V-F1a BLOQUEA"
    if mut == "valor absoluto del FCF base":
        return "V-F1a AVISO" if suma <= u * n * abs(fcf) else "V-F1a BLOQUEA"
    return "V-F1a AVISO" if suma <= u * n * fcf else "V-F1a BLOQUEA"     # sin dividir: FCF ≤ 0 bloquea solo


print("== 1. Los 30 casos del autor con la regla escrita por el revisor")
mal = []
for ident, desc, caso, esperado in A.CASOS:
    mio = [regla(caso, o) for o in OPC]
    if mio != esperado:
        mal.append((ident, mio, esperado))
print(f" casos: {len(A.CASOS)}; coinciden con el estado esperado del autor: {len(A.CASOS) - len(mal)}; discrepancias: {mal}")

print("\n== 2. Mutantes de implementación: ¿los detecta algún caso de los 30? (opción UP01, la propuesta)")
MUTS = ["división sin guarda (e = X/FCF ≤ u)", "coma flotante", "suma sin dividir por n", "último año en lugar de la media", "máximo en lugar de la media",
        "C49 en lugar de la D&A ROU", "frontera estricta (<)", "denominador FCF base + X (flujo sin el doble cómputo)", "ρ sobre ventas con el umbral del flujo",
        "valor absoluto del FCF base"]
for m in MUTS:
    det = [ident for ident, _, caso, esperado in A.CASOS if regla(caso, "UP01", m) != esperado[OPC.index("UP01")]]
    print(f" {'detectado   ' if det else 'NO DETECTADO'} · {m}: {', '.join(det) or '—'}")

print("\n== 3. Casos de frontera que los 30 no cubren (estado con la regla del documento)")
comp = A.comp
extra = [
    ("R1 igualdad con el FCF base REGISTRADO (300,000) cuando el exacto sería 299,9996: la regla usa el registrado",
     dict(rou=["0.3"] * 3, c49="0.3", fcf="300.000", ventas=[3000] * 3, componentes=comp(1, 3)), "V-F1a AVISO",
     dict(rou=["0.3"] * 3, c49="0.3", fcf="299.9996", ventas=[3000] * 3, componentes=comp(1, 3)), "V-F1a BLOQUEA"),
    ("R2 definición del denominador: X = 0,3001 con FCF base 300 (e = 0,10003 %; sobre FCF base + X sería 0,09993 %)",
     dict(rou=["0.3001"] * 3, c49="0.3", fcf=300, ventas=[3000] * 3, componentes=comp(1, 3)), "V-F1a BLOQUEA", None, None),
    ("R3 fila de D&A ROU vacía con C49 = 0 (el documento lo anota como caso que E5 no nombra)",
     dict(rou=["0.3", None, "0.3"], c49=0, fcf=100, ventas=[1000] * 3, componentes=comp(1, 3)), "fuera de E5", None, None),
    ("R4 C49 negativo", dict(rou=["0.3"] * 3, c49="-0.3", fcf=100, ventas=[1000] * 3, componentes=comp(1, 3)), "V-F1e BLOQUEA", None, None),
    ("R5 fila vacía y otra negativa a la vez: ¿V-F1e o V-F1b? (orden de E5: invariantes antes que fila vacía)",
     dict(rou=["-0.1", None, "0.3"], c49="0.3", fcf=100, ventas=[1000] * 3, componentes=comp(1, 3)), "V-F1e BLOQUEA", None, None),
    ("R6 FCF base negativo, arrendamiento ínfimo: |FCF| daría AVISO; la regla bloquea",
     dict(rou=["0.01"] * 3, c49="0.01", fcf=-300, ventas=[3000] * 3, componentes=comp(1, 3)), "V-F1a BLOQUEA", None, None),
]
for nombre, c1, e1, c2, e2 in extra:
    r1 = regla(c1, "UP01")
    linea = f" {nombre}\n    → {r1} (esperado por el revisor: {e1}) {'OK' if r1 == e1 else 'DISTINTO'}"
    if c2 is not None:
        r2 = regla(c2, "UP01")
        linea += f"; con el valor exacto → {r2} (esperado {e2}) {'OK' if r2 == e2 else 'DISTINTO'}"
    print(linea)
print(" mutantes frente a R2 y R6:")
for m in ("denominador FCF base + X (flujo sin el doble cómputo)", "valor absoluto del FCF base"):
    c = extra[1][1] if "X" in m.split("(")[0] or "denominador" in m else extra[5][1]
    print(f"   {m}: da {regla(c, 'UP01', m)} · la regla da {regla(c, 'UP01')}")

print("\n== 4. Qué exime de verdad cada umbral: D&A ROU máxima tolerada (en % de las ventas) según el margen de FCF base")
print(" FCF base/ventas |  0,1 %   1 %    5 %   | 0,5 % ventas (v1), en % del FCF base")
for m in (2, 5, 10, 20, 30):
    print(f"      {m:>3} %      | " + "  ".join(f"{float(u * m):.3f}" for u in (Fr(1, 1000), Fr(1, 100), Fr(5, 100))) + f" | {50 / m:.1f}")

if len(sys.argv) >= 4:
    import csv
    import openpyxl
    v = {}
    for r in csv.DictReader(open(sys.argv[2], encoding="utf-8"), delimiter=";"):
        if r["tipo"] == "tabla" and r["edicion"] == "vigente":
            v[r["id"]] = Fr(r["valor_publicado"])
    wb = openpyxl.load_workbook(sys.argv[3], data_only=True, read_only=True)
    H, P, An, M = wb["Historia"], wb["Palancas"], wb["Análisis"], wb["Motor"]
    S = {2023: "_FR_2023", 2024: "_2024", 2025: "_2025"}
    rou = {y: -v["DA_ROU" + s] for y, s in S.items()}
    ventas = {y: v["IS_VENTAS" + s] for y, s in S.items()}
    X, fcf = sum(rou.values()) / 3, Fr(str(An["C52"].value))
    rho = sum(rou.values()) / sum(ventas.values())
    f_A0, tau5 = Fr(H["C58"].value), Fr(str(H["C52"].value))
    V0 = ventas[2025]
    m0 = (v["IS_BAI_2025"] - v["IS_FIN_2025"]) / V0
    F0_A0 = V0 * (m0 * (1 - tau5) - f_A0)
    F0_A1 = V0 * (m0 * (1 - tau5) - (f_A0 - rho))
    print("\n== 5. Elis (solo información): qué mide e y qué no")
    print(f" X = {float(X):.3f}; FCF base = {float(fcf):.3f}; e = X/FCF base = {100 * float(X / fcf):.2f} %; ρ = {100 * float(rho):.4f} %")
    print(f" exceso en la base 2025 = ρ·V0 = {float(rho * V0):.3f}")
    print(f" flujo sin crecimiento: A0 = {float(F0_A0):.3f}; A1 = {float(F0_A1):.3f}; infravaloración relativa = ρ·V0/F0_A1 = {100 * float(rho * V0 / F0_A1):.2f} % (e = {100 * float(X / fcf):.2f} %)")
    for n, c, k in (("MALO", "B", 6), ("NORMAL", "C", 7), ("BUENO", "D", 8)):
        g15, mobj, roic, ginf = (Fr(str(P[f"{c}{i}"].value)) for i in (14, 15, 18)), None, None, None
        g15, mobj, roic = list(g15)
        ginf = Fr(str(An[f"{c}68"].value))
        V = V0
        for t in range(1, 11):
            V *= 1 + (g15 if t <= 5 else g15 - (g15 - ginf) * Fr(t - 5, 5))
        f11_A0 = V * (1 + ginf) * (mobj * (1 - tau5) * (1 - ginf / roic) - f_A0)
        exc = rho * V * (1 + ginf)
        assert abs(f11_A0 - Fr(M[f"BF{k}"].value)) < Fr(1, 10 ** 6)
        print(f" año 11 {n}: A0 = {float(f11_A0):.3f}; exceso ρ·V10·(1+g∞) = {float(exc):.3f}; infravaloración relativa sobre A1 = {100 * float(exc / (f11_A0 + exc)):.2f} %")
    print(" → e no es la infravaloración relativa de los flujos que se valoran: es X sobre el FCF base registrado (medida de tamaño).")
print("\nRESULTADO:", "los 30 casos coinciden" if not mal else f"{len(mal)} discrepancias")
sys.exit(1 if mal else 0)
