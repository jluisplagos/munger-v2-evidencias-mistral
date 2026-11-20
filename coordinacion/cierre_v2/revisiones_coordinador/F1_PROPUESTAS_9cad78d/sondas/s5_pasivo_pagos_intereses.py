"""Sonda 5 del revisor · México: conciliación del pasivo ligado a adquisiciones, residuo de 2024 e intereses pagados de 2023.

Cifras leídas de su página del PDF (huella comprobada). Preguntas:
 1. ¿Cierra el pasivo con la actualización dentro, y con qué residuo según la edición y las altas que se supongan?
 2. Residuo +0,8 de 2024: ¿es redondeo? ¿hay algo publicado que lo acote?  (línea «Change in debt related to business
    combinations» de la nota 4.9, que el documento revisado no usa)
 3. Intereses pagados de 2023: ¿cabe la actualización (12,4) dentro de los 70,5 pagados? Contraste con 2024 y 2025,
    donde la empresa publica la conciliación.
 4. ¿Está la actualización en C48, C49 o el FCF base?  (estructura del estado de flujos)
"""
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))   # con -I el directorio del script no entra en sys.path
from pdfnum import lee, pagina  # noqa: E402

f = lambda q, n=1: f"{float(q):+.{n}f}"   # noqa: E731
u = lambda q, n=1: f"{float(q):.{n}f}"    # noqa: E731

# --- saldos (valor razonable, nivel 3) y sus dos líneas de balance
s = {("2022", "URD23"): lee("URD2023", 339, "Debt related to acquisitions", 0, 1)[0], ("2023", "URD23"): lee("URD2023", 339, "Debt related to acquisitions", 0, 0)[0],
     ("2023", "DEU24"): lee("DEU2024FR", 331, "Dettes liées aux acquisitions", 0, 1)[0], ("2024", "DEU24"): lee("DEU2024FR", 331, "Dettes liées aux acquisitions", 0, 0)[0],
     ("2024", "URD25"): lee("URD2025", 386, "Debt related to acquisitions", 0, 1)[0], ("2025", "URD25"): lee("URD2025", 386, "Debt related to acquisitions", 0, 0)[0]}
cor = {("2022", "URD23"): lee("URD2023", 304, "Deferred consideration payable on acquisitions", -1)[0], ("2023", "URD23"): lee("URD2023", 304, "Deferred consideration payable on acquisitions", -2)[0],
       ("2023", "DEU24"): lee("DEU2024FR", 298, "Dette liée aux paiements différés relatifs aux acquisitions", -1)[0], ("2024", "DEU24"): lee("DEU2024FR", 298, "Dette liée aux paiements différés relatifs aux acquisitions", -2)[0],
       ("2024", "URD25"): lee("URD2025", 352, "Deferred consideration payable on acquisitions", -1)[0], ("2025", "URD25"): lee("URD2025", 352, "Deferred consideration payable on acquisitions", -2)[0]}
# --- flujos del año
rev = {2023: -lee("DEU2024FR", 296, "Ajustements de compléments de prix", -1)[0], 2024: -lee("URD2025", 350, "Earnout adjustments", -1)[0], 2025: -lee("URD2025", 350, "Earnout adjustments", -2)[0]}
acc = {2023: lee("DEU2024FR", 259, "Charge de désactualisation du complément de prix de l'acquisition réalisée au Mexique", -1)[0],
       2024: lee("URD2025", 313, "Accretion expense for the earnout pertaining to the acquisition in Mexico", -1)[0],
       2025: lee("URD2025", 313, "Accretion expense for the earnout pertaining to the acquisition in Mexico", -2)[0]}
pag = {2023: -lee("DEU2024FR", 288, "Compléments de prix et paiements différés", 0)[0], 2024: -lee("URD2025", 342, "Earnouts and deferred consideration", 0)[0],
       2025: -lee("URD2025", 341, r"^consideration\s{2,}", 0, regex=True)[0]}
precio = {("2023", "URD23"): lee("URD2023", 292, "PURCHASE PRICE", 0)[0], ("2023", "DEU24"): lee("DEU2024FR", 288, "PRIX D'ACQUISITION", 0)[0],
          ("2024", "DEU24"): lee("DEU2024FR", 286, "PRIX D'ACQUISITION", 0)[0], ("2024", "URD25"): lee("URD2025", 342, "PURCHASE PRICE", 0)[0],
          ("2025", "URD25"): lee("URD2025", 340, "PURCHASE PRICE", 0)[0]}
# desembolsos por columna (2023, DEU 2024 p.288): total, Indaco, Levante, Lavartex, otras
des23 = [lee("DEU2024FR", 288, "Sorties de trésorerie effectuées pour l'acquisition", i)[0] for i in range(5)]
pre23 = [lee("DEU2024FR", 288, "PRIX D'ACQUISITION", i)[0] for i in range(4)]            # total, Indaco, Levante, otras
des24 = lee("URD2025", 342, r"Cash outﬂows for the acquisition\s{2,}|Cash outflows for the acquisition\s{2,}", 0, regex=True)[0]
des25 = lee("URD2025", 341, r"^for the acquisition\s{2,}", 0, regex=True)[0]

print("== 1. Conciliación del pasivo: inicial + altas + revaluación + actualización − pagos = final")
print(f" 2023 · precio y desembolso por columna (DEU24 p.288): Indaco {u(pre23[1])} / {u(-des23[1])}; Levante {u(pre23[2])} / {u(-des23[2])}; "
      f"otras {u(pre23[3])} / {u(-des23[4])} → las «otras» pagan {u(-des23[4] - pre23[3])} MÁS que su precio (altas no determinables)")
alt23_id = (pre23[1] + des23[1]) + (pre23[2] + des23[2])
casos = [
    ("2023 · cierre URD 2023 (117,3), altas = 0 [lo que presenta el documento]", s[("2022", "URD23")], Fr(0), 2023, s[("2023", "URD23")], 5),
    ("2023 · cierre DEU 2024 reexpresado (118,2), altas = 0", s[("2022", "URD23")], Fr(0), 2023, s[("2023", "DEU24")], 5),
    (f"2023 · cierre DEU 2024, altas identificadas (Indaco + Levante = {u(alt23_id)})", s[("2022", "URD23")], alt23_id, 2023, s[("2023", "DEU24")], 9),
    (f"2023 · cierre DEU 2024, altas = precio − desembolso del total ({u(pre23[0] + des23[0])})", s[("2022", "URD23")], pre23[0] + des23[0], 2023, s[("2023", "DEU24")], 7),
    ("2024 · DEU 2024 (precio provisional)", s[("2023", "DEU24")], precio[("2024", "DEU24")] + des24, 2024, s[("2024", "DEU24")], 7),
    ("2024 · URD 2025 (precio definitivo)", s[("2023", "DEU24")], precio[("2024", "URD25")] + des24, 2024, s[("2024", "URD25")], 7),
    ("2025 · URD 2025", s[("2024", "URD25")], precio[("2025", "URD25")] + des25, 2025, s[("2025", "URD25")], 7),
]
for nombre, ini, altas, y, fin, n in casos:
    calc = ini + altas + rev[y] + acc[y] - pag[y]
    res = fin - calc
    cota = Fr(5, 100) * n
    print(f" {nombre}\n    {u(ini)} {f(altas)} {f(rev[y])} {f(acc[y])} {f(-pag[y])} = {u(calc)}; publicado {u(fin)}; residuo {f(res)} "
          f"(cota de redondeo {u(cota, 2)}: {'dentro' if abs(res) <= cota else 'FUERA'}); sin la actualización {f(res + acc[y])}")
print(" → 2025 cierra exactamente. 2024 deja +0,8 en las dos ediciones (no es redondeo). 2023 solo cierra «dentro del redondeo»")
print("   con el cierre de la edición ANTERIOR (URD 2023) y suponiendo altas = 0; con la edición vigente queda entre +0,3 y +3,2 según las altas.")
print("   En todos los casos el residuo sin la actualización es un orden de magnitud mayor: la conclusión cualitativa se sostiene.")

print("\n== 2. Nota 4.9: línea publicada «Change in debt related to business combinations» (pasivo corriente)")
linea = {("2023", "URD23"): lee("URD2023", 304, "Change in debt related to business combinations", -2)[0],
         ("2023", "DEU24"): lee("DEU2024FR", 298, "Variation de la dette liée aux regroupements d'entreprises", -1)[0],
         ("2024", "DEU24"): lee("DEU2024FR", 298, "Variation de la dette liée aux regroupements d'entreprises", -2)[0],
         ("2024", "URD25"): lee("URD2025", 352, "Change in debt related to business combinations", -1)[0],
         ("2025", "URD25"): lee("URD2025", 352, "Change in debt related to business combinations", -2)[0]}
pares = [("2023", "URD23", ("2022", "URD23")), ("2023", "DEU24", ("2022", "URD23")), ("2024", "DEU24", ("2023", "DEU24")), ("2024", "URD25", ("2023", "DEU24")), ("2025", "URD25", ("2024", "URD25"))]
for y, ed, ini in pares:
    var = cor[(y, ed)] - cor[ini]
    print(f" {y} ({ed}): pasivo corriente {u(cor[ini])} → {u(cor[(y, ed)])} = {f(var)}; línea publicada {f(linea[(y, ed)])}; "
          f"diferencia (otras líneas: combinaciones, conversión, otros) {f(var - linea[(y, ed)])}")
print(" → en 2024 el propio cuadro de la nota deja +0,6 del pasivo corriente fuera de esa línea, en las dos ediciones: del mismo signo y tamaño")
print("   que el residuo +0,8. Es coherente con «conversión y otros movimientos» [H]; no lo acredita.")
t = Fr("25.83") / 100
l24 = lee("URD2025", 392, "Adjustments and accretion of non-deductible earnouts", -1)[0]
print(f" La actualización de 2024 no depende de ese residuo: la línea fiscal ({u(l24)}) la acota entre "
      f"{u(-rev[2024] - Fr(5, 100) - (l24 + Fr(5, 100)) / t, 2)} y {u(-rev[2024] + Fr(5, 100) - (l24 - Fr(5, 100)) / t, 2)}, y la conciliación publicada da (5,6).")

print("\n== 3. Intereses pagados de 2023: ¿cabe la actualización dentro de los 70,5?")
pyl = {2023: ("DEU2024FR", 324, "Charge d'intérêts sur emprunts et comptes courants de participation mesurée au coût amorti", "Produits d'intérêts selon la méthode du taux d'intérêt effectif", -1),
       2024: ("URD2025", 379, "at amortized cost", "Interest income using the effective interest rate method", -1),
       2025: ("URD2025", 379, "at amortized cost", "Interest income using the effective interest rate method", -2)}
pagados = {2023: -lee("DEU2024FR", 273, "Intérêts financiers nets versés", -1)[0], 2024: -lee("URD2025", 327, "Net interest paid", -1)[0], 2025: -lee("URD2025", 327, "Net interest paid", -2)[0]}
no_caja = {2024: sum(lee("REL_FY2024_PRES", 52, r, 0)[0] for r in ("Adjustment accrued / non accrued interests", "Notional interests (OCEANE)", "Amortization of issuing costs")),
           2025: sum(lee("REL_FY2025_PRES", 51, r, 0)[0] for r in ("Adjustment accrued / non accrued interests", "Notional interests (OCEANE)", "Amortization of issuing costs"))}
for y, (doc, p, r1, r2, pos) in pyl.items():
    gasto, ingreso = -lee(doc, p, r1, pos)[0], lee(doc, p, r2, pos)[0]
    neto = gasto - ingreso
    extra = f"; partidas sin caja publicadas (devengo, OCEANE, costes de emisión): {u(-no_caja[y])}" if y in no_caja else "; sin conciliación publicada entre las fuentes"
    print(f" {y}: intereses de la deuda en resultados, netos de ingresos = {u(gasto)} − {u(ingreso)} = {u(neto)}; pagados (EFE) {u(pagados[y])}; "
          f"devengado − pagado = {f(neto - pagados[y])}{extra}")
print(f" Si los 12,4 de 2023 estuvieran dentro de los 70,5 pagados, los intereses de la deuda pagados serían {u(pagados[2023] - acc[2023])} "
      f"y la brecha con lo devengado {f(Fr('91.3') - (pagados[2023] - acc[2023]))}, frente a +19,7 en 2024 (año con conciliación publicada).")
txt = " ".join(x.strip() for x in pagina("URD2023", 267))
print(" URD23 p.267, explicación de la empresa del aumento de los intereses pagados en 2023 (sin mención del earnout):",
      "presente" if "increase in net interest paid can be attributed mainly" in txt and "to the rise in interest rates and to the refinancing transactions" in txt else "NO ENCONTRADA")
print(" URD23 p.332, explicación del resultado financiero de 2023 (con mención de la actualización):",
      "presente" if "affected by the accretion expense of the earnout" in " ".join(pagina("URD2023", 332)) else "NO ENCONTRADA")
print(" → la inferencia del documento para 2023 es razonable y puede reforzarse con estas dos frases y con la brecha; sigue siendo [I]:")
print("   la tabla de conciliación de 2023 no está entre las fuentes.")

print("\n== 4. Estructura del estado de flujos (URD25 p.327): dónde podría estar la caja de la actualización")
ls = [x.strip() for x in pagina("URD2025", 327)]
orden = ["Net financial income (expense)", "CASH FLOW BEFORE FINANCE COSTS AND TAX", "NET CASH FROM OPERATING ACTIVITIES", "Acquisition of subsidiaries, net of cash acquired",
         "Lease liability payments (including interest on lease liabilities)", "Net interest paid"]
idx = [next(i for i, x in enumerate(ls) if x.startswith(r)) for r in orden]
print(" orden de las líneas:", " < ".join(orden) if idx == sorted(idx) else "ORDEN DISTINTO")
print(" → el resultado financiero (con la actualización) se suma entero antes del CFO; los pagos del earnout van en «Acquisition of subsidiaries» (inversión);")
print("   C48 toma «Net interest paid» y el interés de arrendamiento; C49, el principal del arrendamiento. La actualización no entra en ninguno.")

print("\n== 5. Política de medición del pasivo por ajuste de precio (nota 1.1, bases de preparación)")
import re as _re
for doc, pag, frs in (("URD2021", 233, ["financial liabilities representing a price adjustment", "recognized in a business combination, which are measured at", "fair value"]),
                      ("URD2022", 265, ["financial liabilities representing a price adjustment", "recognized in a business combination, which are measured at", "fair value"]),
                      ("URD2023", 283, ["financial liabilities representing a price adjustment", "recognized in a business combination, which are measured at", "fair value"]),
                      ("DEU2024FR", 277, ["passifs financiers représentatifs d'un", "ajustement de prix, reconnus dans un regroupement", "qui sont évalués à la juste valeur"]),
                      ("URD2025", 331, ["financial liabilities representing a price adjustment", "recognized in a business combination, which are measured at", "fair value"])):
    t = _re.sub(r"\s+", " ", " ".join(pagina(doc, pag)))
    print(f" {doc} p.{pag}: «pasivos financieros que representan un ajuste de precio… medidos a valor razonable»:", "presente" if all(x in t for x in frs) else "NO ENCONTRADO")
print(" → la base de medición del pasivo (valor razonable) SÍ está publicada, igual en las cinco ediciones. Lo que no se publica es el reparto")
print("   de su variación entre la nota 4.6 (revaluación) y el resultado financiero (actualización).")
