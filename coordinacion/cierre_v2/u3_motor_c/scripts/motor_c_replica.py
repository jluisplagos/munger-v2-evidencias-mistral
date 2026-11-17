# Réplica independiente de las fórmulas del motor C (Motor!Q..BK de build_v6.py:915-945), sin LibreOffice.
def valor_c(B0, ROE0, g1, roe_obj, roe_lp, ginf, r, acciones, p=0.0, rec=0.0):
    L = [B0]; flujos = []
    for t in range(1, 11):
        g = g1 if t <= 5 else g1 - (g1 - ginf) * (t - 5) / 5          # Q..Z
        L.append(L[-1] * (1 + g))                                      # AA..AJ
        m = ROE0 + (roe_obj - ROE0) * min(t, 5) / 5                    # AK..AT
        flujos.append(L[t - 1] * m - (L[t] - L[t - 1]))                # AU..BD (motor C)
    vp = sum(x / (1 + r) ** t for t, x in enumerate(flujos, 1))        # BE
    f11 = L[10] * (roe_lp - ginf)                                      # BF (motor C)
    vt = f11 / (r - ginf)                                              # BG
    vpt = vt / (1 + r) ** 10                                           # BH
    total = vp + vpt                                                   # BI (ajuste M = 0 en C)
    final = (1 - p) * total + p * rec                                  # BJ
    return final / acciones, dict(L=L, flujos=flujos, vp=vp, vpt=vpt)  # BK

# Fixture C_orig (test_fill.py:47-50, 79; EmpresaX: V_2025 = 1000, patrimonio = 0,6·V, beneficio = 0,19·V·0,75)
B0 = 0.6 * 1000; NI = (0.20 - 0.01) * 1000 * (1 - 0.25); ROE0 = NI / B0
P = {'B': (0.03, 0.10, 0.10, 0.02), 'C': (0.06, 0.14, 0.13, 0.025), 'D': (0.08, 0.16, 0.15, 0.03)}
res = {k: valor_c(B0, ROE0, g, m, ro, gi, 0.09, 100)[0] for k, (g, m, ro, gi) in P.items()}
pond = 0.2 * res['B'] + 0.6 * res['C'] + 0.2 * res['D']
print("ROE0 = NI/B0 =", ROE0)
print("B78:D78 =", res, " C83 =", pond)
print("LEEME fixture C_orig: 8,3362525831 / 11,9777149618 / 15,2293638877 · C83 = 11,8997522712")

# Caso del puente: E0 = 1000, beneficio neto atribuible 100, dividendos 40, sin OCI ni recompras ni emisiones
E0, NI1, DIV = 1000.0, 100.0, 40.0
E1 = E0 + NI1 - DIV
print("puente correcto E1 =", E1, "| ROE Historia (cierre) =", NI1 / E1, "| ROE sobre apertura =", NI1 / E0)
print("puente de 52fb120 (BAI 130 + dividendos): E1 =", E0 + 130 + DIV, " diferencia =", E0 + 130 + DIV - E1)
# flujo del motor con B(t-1) = E0, ROE = NI/E0 y B(t) = E1
flujo = E0 * (NI1 / E0) - (E1 - E0)
print("flujo motor = B(t-1)*ROE - (B(t)-B(t-1)) =", flujo, "= dividendos + recompras - emisiones")
# con OCI = -25 y recompras = 10
OCI, REC = -25.0, 10.0
E1b = E0 + NI1 + OCI - DIV - REC
print("con OCI -25 y recompras 10: E1 =", E1b, "flujo motor (NI - dB) =", NI1 - (E1b - E0), "≠ reparto real", DIV + REC, "→ diferencia = -OCI =", NI1 - (E1b - E0) - (DIV + REC))
# payout 0,4 mal colocado en X15 (ROE objetivo) frente a ROE real
v_ok = valor_c(B0, ROE0, 0.06, 0.14, 0.13, 0.025, 0.09, 100)[0]
v_mal = valor_c(B0, ROE0, 0.06, 0.40, 0.13, 0.025, 0.09, 100)[0]
print("NORMAL con X15 = 0,14:", v_ok, " con X15 = 0,40 (payout mal colocado):", v_mal, " ratio", v_mal / v_ok)
