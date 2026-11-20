"""Sonda 4 del revisor · la indicación fiscal de 2021 (medida «net income from ordinary operations», URD21 p.217)
y la línea fiscal del earnout de 2022–2025, con aritmética de intervalos sobre las cifras impresas.

Cada cifra se lee de su página del PDF (huella comprobada) por rótulo y posición. Preguntas:
 1. ¿La medida neta de impuesto de 2021 distingue lo no deducible, o aplica un tipo a todo?  (línea IFRS 2)
 2. ¿Qué parte del ajuste de earnout de 2021 (3,0) lleva efecto fiscal en esa medida, según el tipo que se suponga a
    los costes de transacción (2,1)?  El autor supone el tipo teórico (28,41 %): aquí se barre de 0 % a 34 %.
 3. Comprobación que no depende de ese supuesto: la nota 4.6 entera (16,1 → 11,5) frente a 2022 y 2023.
 4. ¿Cómo rotula la empresa el efecto fiscal de esta medida en las ediciones recientes?  («at standard rates»)
 5. Línea fiscal de 2022–2025 con intervalos (¿cuadra con el ajuste, y con el ajuste y la actualización?).
"""
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))   # con -I el directorio del script no entra en sys.path
from pdfnum import intervalo, lee, pagina  # noqa: E402

f = lambda q, n=3: f"{float(q):.{n}f}"      # noqa: E731
pct = lambda q: f"{100 * float(q):.1f} %"   # noqa: E731

print("== 1. ¿La medida de 2021 distingue lo no deducible? Línea IFRS 2")
ifrs2_bruto, l1 = lee("URD2021", 255, "Equity-settled share-based payments", -2)
ifrs2_neto, l2 = lee("URD2021", 217, "IFRS 2 expense(a)", -2)
ifrs2_bruto20, _ = lee("URD2021", 255, "Equity-settled share-based payments", -1)
ifrs2_neto20, _ = lee("URD2021", 217, "IFRS 2 expense(a)", -1)
print(f" 2021: gasto IFRS 2 bruto {l1} [URD21 p.255] → neto de impuesto {l2} [URD21 p.217]: efecto fiscal {pct(1 - ifrs2_neto / -ifrs2_bruto)}")
print(f" 2020: bruto {f(-ifrs2_bruto20, 1)} → neto {f(ifrs2_neto20, 1)}: efecto fiscal {pct(1 - ifrs2_neto20 / -ifrs2_bruto20)}")
txt = " ".join(pagina("URD2021", 290))
print(" URD21 p.290, conciliación del impuesto: «Permanent differences (including non-deductible IFRS 2 expenses)»:",
      "presente" if "Permanent differences (including non-deductible IFRS 2 expenses)" in txt else "AUSENTE")
print(" → en la misma tabla de 2021, una partida no deducible aparece casi sin efecto fiscal: la medida no aplica un tipo a todo.")

print("\n== 2. Línea conjunta de 2021: costes de adquisición (2,1) y ajustes de earnout (3,0)")
bruto, lb = lee("URD2021", 253, "Costs related to acquisitions and earnout adjustments", -2)
neto, ln = lee("URD2021", 217, "Costs related to acquisitions and earnout adjustments(a)", -2)
ct, lct = lee("URD2022", 285, "Acquisition-related transaction costs", -1)
ea, lea = lee("URD2022", 285, "Earnout adjustments", -1)
t21, lt = lee("URD2022", 326, "Theoretical tax rate", -1)
t21 /= 100
print(f" bruto {lb} [URD21 p.253] = {lct} + {lea} [URD22 p.285]; neto {ln} [URD21 p.217]; tipo teórico {lt} [URD22 p.326]")
B, N, CT, EA = intervalo(-bruto), intervalo(neto), intervalo(-ct), intervalo(-ea)
ef = (B[0] - N[1], B[1] - N[0])                    # efecto fiscal implícito de la línea
print(f" efecto fiscal implícito: {f(-bruto - neto, 1)}, con el redondeo entre {f(ef[0], 2)} y {f(ef[1], 2)}; "
      f"sobre el bruto: {pct((-bruto - neto) / -bruto)} (entre {pct(ef[0] / B[1])} y {pct(ef[1] / B[0])})")
print(" Parte del ajuste de earnout (3,0) que lleva efecto fiscal, según el tipo de los costes de transacción (t_ct)")
print(" y el tipo al que tributa el propio ajuste (t_ea). Mínimo con el redondeo de las cifras impresas:")
print("   t_ct    t_ea=28,41 %   t_ea=34 % (máximo estatutario relevante)")
for tct in (Fr(0), Fr(19, 100), Fr(25, 100), t21, Fr(34, 100)):
    fila = []
    for tea in (t21, Fr(34, 100)):
        central = ((-bruto - neto) - tct * -ct) / tea
        minimo = (ef[0] - tct * CT[1]) / tea
        fila.append(f"{f(central, 2)} (mín. {f(minimo, 2)})")
    print(f"   {pct(tct):>7}   {fila[0]:<18} {fila[1]}")
print(f" Si el ajuste de earnout NO llevara efecto fiscal, los costes de transacción necesitarían un tipo de {pct((-bruto - neto) / -ct)}"
      f" (mínimo {pct(ef[0] / CT[1])}).")
print(f" Si los costes de transacción NO fueran deducibles, el ajuste necesitaría un tipo de {pct((-bruto - neto) / -ea)} (mínimo {pct(ef[0] / EA[1])}): imposible.")
print(" → dentro de la lectura «la medida refleja el efecto fiscal real», casi toda la línea (las dos partidas) lleva impuesto;")
print("   con los dos tipos al máximo (34 %), al menos", f(((ef[0] - Fr(34, 100) * CT[1]) / Fr(34, 100)), 2), "de 3,0. El «2,4 a 3,0» del autor supone t_ct = t_ea = 28,41 %.")

print("\n== 3. Sin suponer nada de los costes de transacción: la nota 4.6 entera")
datos = {}
for año, (docb, pb, posb, docn, pn, posn, earn) in {
        2021: ("URD2022", 285, -1, "URD2022", 249, -1, -ea),
        2022: ("URD2023", 302, -1, "URD2023", 267, -1, None),
        2023: ("URD2023", 302, -2, "URD2023", 267, -2, None)}.items():
    tot, _ = lee(docb, pb, "OTHER OPERATING INCOME AND EXPENSES", posb)
    net, _ = lee(docn, pn, "Other operating income and expenses(a)", posn)
    e, _ = lee(docb, pb, "Earnout adjustments", posb)
    datos[año] = (-tot, net, -e)
for año, (tot, net, e) in datos.items():
    T, Nn, E = intervalo(tot), intervalo(net), intervalo(e)
    efn = (T[0] - Nn[1], T[1] - Nn[0])
    con = (efn[0] / T[1], efn[1] / T[0])
    resto = (T[0] - E[1], T[1] - E[0])
    sin = (efn[0] / resto[1], efn[1] / resto[0])
    print(f" {año}: nota 4.6 {f(tot, 1)} → neto {f(net, 1)}; ajuste de earnout {f(e, 1)} (gasto +). Efecto fiscal {f(tot - net, 1)}:")
    print(f"       · si el ajuste lleva impuesto como el resto: tipo medio {pct((tot - net) / tot)} ({pct(con[0])}–{pct(con[1])})")
    print(f"       · si el ajuste NO lleva impuesto: el resto ({f(tot - e, 1)}) necesita {pct((tot - net) / (tot - e))} ({pct(sin[0])}–{pct(sin[1])})")
print(" → 2023 (earnout no deducible según la nota 9): el resto lleva ~17 %. 2022: ~17–18 % si el abono no tributa.")
print("   2021: sin efecto fiscal en el earnout, el resto necesitaría ~35 %, más que cualquier tipo del grupo y el doble que en 2022–23.")
print("   La indicación de 2021 se sostiene también a nivel de nota, sin el supuesto sobre los costes de transacción.")

print("\n== 4. Cómo rotula la empresa el efecto fiscal de esta medida")
for doc, pag, frag in (("URD2021", 217, "(a) Net of tax effect."), ("URD2023", 267, "(a) Net of tax effect."), ("DEU2024FR", 259, "Effet impôt"),
                       ("URD2025", 313, "Tax effect (at standard rates)"), ("REL_H1_2026_COM", 5, "Tax effect (using the standard tax rates)")):
    print(f" {doc} p.{pag}: «{frag}»:", "presente" if any(frag in x for x in pagina(doc, pag)) else "AUSENTE")
print(" → desde el URD 2025 la empresa dice que el efecto fiscal de la medida se calcula «a tipos estándar». El documento revisado no lo cita.")
print("   No invalida la indicación (la línea IFRS 2 de 2021 muestra que la medida distinguía lo no deducible), pero es un límite que debe verse.")

print("\n== 5. Línea fiscal «Adjustments and accretion of non-deductible earnouts» con intervalos")
t = Fr("25.83") / 100
filas = {2022: (lee("URD2023", 345, "Adjustments and accretion of non-deductible earnouts", -1)[0], lee("URD2023", 302, "Earnout adjustments", -1)[0], Fr(0)),
         2023: (lee("DEU2024FR", 337, "compléments de prix non déductibles", -1)[0], lee("DEU2024FR", 296, "Ajustements de compléments de prix", -1)[0],
                lee("DEU2024FR", 259, "Charge de désactualisation du complément de prix de l'acquisition réalisée au Mexique", -1)[0]),
         2024: (lee("URD2025", 392, "Adjustments and accretion of non-deductible earnouts", -1)[0], lee("URD2025", 350, "Earnout adjustments", -1)[0],
                lee("URD2025", 313, "Accretion expense for the earnout pertaining to the acquisition in Mexico", -1)[0]),
         2025: (lee("URD2025", 392, "Adjustments and accretion of non-deductible earnouts", -2)[0], lee("URD2025", 350, "Earnout adjustments", -2)[0],
                lee("URD2025", 313, "Accretion expense for the earnout pertaining to the acquisition in Mexico", -2)[0])}
e22a = lee("URD2022", 285, "Earnout adjustments", -2)[0]
def solapa(a, b):
    return a[0] <= b[1] and b[0] <= a[1]
for y, (linea, earn, acc) in filas.items():
    L = intervalo(linea)
    solo = tuple(sorted((t * (earn - Fr(5, 100)), t * (earn + Fr(5, 100)))))
    amb = tuple(sorted((t * (earn - acc - Fr(1, 10)), t * (earn - acc + Fr(1, 10))))) if acc else solo
    print(f" {y}: línea {f(linea, 1)}; ajuste {f(earn, 1)}; actualización {f(acc, 1)} → solo el ajuste [{f(solo[0])}, {f(solo[1])}] "
          f"{'SOLAPA' if solapa(L, solo) else 'no solapa'}; ajuste y actualización [{f(amb[0])}, {f(amb[1])}] {'SOLAPA' if solapa(L, amb) else 'no solapa'}")
L22 = intervalo(filas[2022][0])
print(f" 2022 con la cifra anterior a la reexpresión ({f(e22a, 1)}): [{f(t * (e22a - Fr(5, 100)))}, {f(t * (e22a + Fr(5, 100)))}] "
      f"{'SOLAPA' if solapa(L22, (t * (e22a - Fr(5, 100)), t * (e22a + Fr(5, 100)))) else 'no solapa'}")
print(f" 2022: tipo implícito si los 2,4 enteros no tributan y la línea se calculó a otro tipo: entre {pct(L22[0] / (filas[2022][1] + Fr(5, 100)))} y {pct(L22[1] / (filas[2022][1] - Fr(5, 100)))}"
      " (tercera lectura posible, que el documento no enumera: línea calculada a un tipo local inferior al teórico)")
acc24 = (filas[2024][1] - Fr(5, 100) - intervalo(filas[2024][0])[1] / t, filas[2024][1] + Fr(5, 100) - intervalo(filas[2024][0])[0] / t)
print(f" 2024: la línea fiscal (0,8) acota por sí sola la actualización no deducible entre {f(acc24[0], 2)} y {f(acc24[1], 2)} (publicada: 5,6)")
