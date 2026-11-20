"""Réplica propia del motor A (Convenciones_financieras_V6_3.md, tabla de motores y convenciones 1-3, 5) para medir sensibilidades.
No sustituye al recálculo oficial."""

def valor(V0, m0, tau, f, g5, mobj, s2c, ginf, roic, r, exceso=0.0, acciones=905.0, detalle=False):
    V_prev, pv, flujos = V0, 0.0, []
    for t in range(1, 11):
        g = g5 if t <= 5 else g5 - (g5 - ginf) * (t - 5) / 5
        V = V_prev * (1 + g)
        m = m0 + (mobj - m0) * min(t, 5) / 5
        fl = V * (m * (1 - tau) - f) - (V - V_prev) / s2c
        flujos.append(fl)
        pv += fl / (1 + r) ** t
        V_prev = V
    f11 = V_prev * (1 + ginf) * (mobj * (1 - tau) * (1 - ginf / roic) - f)
    vt = f11 / (r - ginf)
    pv_t = vt / (1 + r) ** 10
    tot = pv + pv_t + exceso
    if detalle:
        return tot / acciones, flujos, f11, pv, pv_t
    return tot / acciones

BASE = dict(V0=92352.0, m0=0.0383532571032571, tau=0.21436, f=0.0036081074685145, r=0.09)
ESC = {"MALO": dict(g5=0.0, mobj=0.03, s2c=3.9, ginf=0.01, roic=0.09),
       "NORMAL": dict(g5=0.03, mobj=0.035, s2c=4.8, ginf=0.02, roic=0.12),
       "BUENO": dict(g5=0.045, mobj=0.04, s2c=6.9, ginf=0.025, roic=0.12)}
P = [0.25, 0.6, 0.15]

def tres(**kw):
    b = dict(BASE); b.update({k: v for k, v in kw.items() if k in ("V0", "m0", "tau", "f", "r")})
    extra = {k: v for k, v in kw.items() if k in ("exceso", "acciones")}
    return [valor(**b, **ESC[e], **extra) for e in ("MALO", "NORMAL", "BUENO")]

def precio_si(V, p=P, k=3.0):
    """P* tal que ganancia esperada = k × pérdida esperada: sum p_i max(V_i-P,0) = k sum p_i max(P-V_i,0). Bisección."""
    lo, hi = min(V), max(V)
    for _ in range(200):
        mid = (lo + hi) / 2
        G = sum(pi * max(v - mid, 0) for pi, v in zip(p, V))
        L = sum(pi * max(mid - v, 0) for pi, v in zip(p, V))
        if G - k * L > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def resumen(nombre, **kw):
    V = tres(**kw)
    pond = sum(pi * v for pi, v in zip(P, V))
    ps = precio_si(V)
    print(f"{nombre:<62} MALO {V[0]:6.2f}  NORMAL {V[1]:6.2f}  BUENO {V[2]:6.2f}  pond {pond:6.2f}  P_si {ps:6.2f}")
    return V, pond, ps

if __name__ == "__main__":
    V, pond, ps = resumen("Libro (réplica)")
    print("oficial: 23.6164157478233 30.0962623953428 38.8923100254644 pond 29.7957078779812 P* 27.735943834595208")
    print("dif:", [a - b for a, b in zip(V, (23.6164157478233, 30.0962623953428, 38.8923100254644))], pond - 29.7957078779812, ps - 27.735943834595208)
