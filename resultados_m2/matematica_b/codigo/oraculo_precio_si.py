#!/usr/bin/env python3
"""Oráculo independiente del precio de Sí (Frente C · M2 · rama mistral/m2-matematica-b).

Implementación propia derivada de las ecuaciones del encargo, NO copiada del producto
(no importa nada de `personaje_v2/scripts/`):

  G(P) = Σ p_i · max(V_i − P, 0)      ganancia esperada
  L(P) = Σ p_i · max(P − V_i, 0)      pérdida esperada
  F_k(P) = G(P) − k·L(P)
  P* = max { P : F_k(P) ≥ 0 }         (equivalentemente la única raíz de F_k, que es
                                       continua y estrictamente decreciente)
  precio_de_si = min(P*, V_NORMAL)
  precio_escenario_malo = min(V) si > 0; si no, None
  ponderado = Σ p_i·V_i

Dos soluciones independientes:
  1. `p_estrella_trazos`: forma cerrada por tramos sobre los valores distintos ordenados,
     con aritmética exacta (Fraction) cuando las entradas son racionales.
  2. `p_estrella_biseccion`: bisección sobre F_k en [min V, max V] en coma flotante.

Dominio (definición matemática): V_i reales finitos, p_i ≥ 0 con Σ p_i = 1, k > 0.
El producto añade guardas de política (k ≥ 1, |Σp−1| ≤ 1e-3, valores ordenados B78≤C78≤D78,
precio actual > 0); aquí se distinguen como guardas, no como matemáticas: este módulo
acepta k > 0 y cualquier orden, y marca las guardas del producto en `guardas_producto`.

Uso: importado por los demás scripts de `codigo/`; también ejecutable:
  python3 oraculo_precio_si.py --selftest
"""
from fractions import Fraction
import math


class DominioError(ValueError):
    """Entradas fuera del dominio de la definición (p no es distribución, k ≤ 0, NaN...)."""


def _fraccion(x):
    if isinstance(x, Fraction):
        return x
    if isinstance(x, bool):
        raise DominioError(f"booleano como número: {x!r}")
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, float):
        if not math.isfinite(x):
            raise DominioError(f"número no finito: {x!r}")
        return Fraction(x)  # valor binario exacto del float64
    if isinstance(x, str):
        return Fraction(x)  # decimal exacto escrito a mano
    raise DominioError(f"tipo no numérico: {x!r}")


def validar(V, p, k):
    """Comprueba el dominio matemático; devuelve (V, p, k) como Fraction."""
    V = list(V)
    p = list(p)
    if len(V) == 0 or len(V) != len(p):
        raise DominioError(f"V y p de distinta longitud: {V} {p}")
    Vf = [_fraccion(v) for v in V]
    pf = [_fraccion(x) for x in p]
    kf = _fraccion(k)
    if any(x < 0 for x in pf):
        raise DominioError(f"probabilidades negativas: {p}")
    if sum(pf) != 1:
        raise DominioError(f"las probabilidades no suman 1 exactamente: {p} (Σ = {sum(pf)})")
    if kf <= 0:
        raise DominioError(f"k debe ser > 0: {k}")
    return Vf, pf, kf


def G(V, p, P):
    """Ganancia esperada; admite Fraction o float."""
    return sum(pp * max(v - P, 0 * P) for v, pp in zip(V, p))


def L(V, p, P):
    """Pérdida esperada."""
    return sum(pp * max(P - v, 0 * P) for v, pp in zip(V, p))


def F(V, p, k, P):
    return G(V, p, P) - k * L(V, p, P)


def ponderado(V, p):
    return sum(pp * v for v, pp in zip(V, p))


def p_estrella_trazos(V, p, k):
    """Solución cerrada por tramos (exacta con Fraction). Devuelve Fraction.

    En el tramo [v_(j), v_(j+1)] de los valores distintos ordenados, con masas q_j:
      F(P) = Σ_{l>j} q_l (v_l − P) − k Σ_{l≤j} q_l (P − v_l) = 0
      ⇒ P_j = (Σ_{l>j} q_l v_l + k Σ_{l≤j} q_l v_l) / (Σ_{l>j} q_l + k Σ_{l≤j} q_l)
    La raíz única cae en exactamente un tramo (o en un quiebro).
    """
    Vf, pf, kf = validar(V, p, k)
    s = sorted(zip(Vf, pf), key=lambda t: t[0])
    vals = []  # valores distintos con masa agregada
    for v, q in s:
        if vals and vals[-1][0] == v:
            vals[-1][1] += q
        else:
            vals.append([v, q])
    m = len(vals)
    if m == 1:
        return vals[0][0]  # degenerado: todos los valores (con masa) iguales
    for j in range(m - 1):
        bajo = vals[:j + 1]
        alto = vals[j + 1:]
        sb = sum(q for _, q in bajo)
        sa = sum(q for _, q in alto)
        den = sa + kf * sb
        if den == 0:
            continue
        num = sum(q * v for v, q in alto) + kf * sum(q * v for v, q in bajo)
        P = num / den
        if vals[j][0] <= P <= vals[j + 1][0]:
            return P
    for v, _q in vals:  # raíz exactamente en un quiebro
        if F(Vf, pf, kf, v) == 0:
            return v
    raise AssertionError("la raíz no cayó en ningún tramo: revisar entradas")


def p_estrella_biseccion(V, p, k, iteraciones=200):
    """Segunda solución, numérica e independiente: bisección de F_k en [min V, max V].

    Devuelve (P_float, residuo |F(P)|). La raíz está en [min V, max V] (teorema de
    acotación), F(min V) ≥ 0 y F(max V) ≤ 0.
    """
    Vf, pf, kf = validar(V, p, k)
    lo, hi = float(min(Vf)), float(max(Vf))
    flo = float(F(Vf, pf, kf, Fraction(lo)))
    fhi = float(F(Vf, pf, kf, Fraction(hi)))
    if flo == 0.0:
        return lo, abs(flo)
    if fhi == 0.0:
        return hi, abs(fhi)
    assert flo > 0 > fhi, "F(min V) ≥ 0 ≥ F(max V) debería cumplirse"
    for _ in range(iteraciones):
        mid = (lo + hi) / 2
        fm = float(F(Vf, pf, kf, Fraction(mid)))
        if fm == 0.0:
            return mid, 0.0
        if fm > 0:
            lo = mid
        else:
            hi = mid
    P = (lo + hi) / 2
    return P, abs(float(F(Vf, pf, kf, Fraction(P))))


def precio_de_si(V, p, k, v_normal):
    """Salida recortada del contrato D11: min(P*, V_NORMAL). v_normal es el valor del
    escenario NORMAL (en el producto, la celda del medio tras exigir B78 ≤ C78 ≤ D78)."""
    Vf, pf, kf = validar(V, p, k)
    Ps = p_estrella_trazos(Vf, pf, kf)
    vn = _fraccion(v_normal)
    return min(Ps, vn), Ps


def precio_escenario_malo(V):
    """min(V) si es > 0; si no, None (el producto no da «precio del escenario MALO»)."""
    Vf = [_fraccion(v) for v in V]
    mn = min(Vf)
    return mn if mn > 0 else None


def zona(precio, malo, precio_si, pond):
    """Clasificación de la zona del precio actual (misma regla que el Anexo C §C.4.4)."""
    precio = _fraccion(precio)
    if malo is not None and precio <= malo:
        return "bajo_malo"
    if precio <= precio_si:
        return "cumple_regla_k"
    if precio <= pond:
        return "vigilar"
    return "caro"


def resumen_caso(V, p, k, v_normal=None, precio=None):
    """Paquete completo de un caso, con las dos soluciones y los residuos."""
    Vf, pf, kf = validar(V, p, k)
    Ps = p_estrella_trazos(Vf, pf, kf)
    Pb, res_b = p_estrella_biseccion(Vf, pf, kf)
    res_t = F(Vf, pf, kf, Ps)
    pond = ponderado(Vf, pf)
    if v_normal is None:
        s = sorted(Vf)
        v_normal = s[len(s) // 2] if len(s) % 2 == 1 else None
    psi = min(Ps, v_normal) if v_normal is not None else Ps
    malo = precio_escenario_malo(Vf)
    out = {
        "V": [str(v) for v in Vf], "p": [str(x) for x in pf], "k": str(kf),
        "P_estrella_trazos": str(Ps), "P_estrella_trazos_float": float(Ps),
        "P_estrella_biseccion": Pb, "residuo_F_trazos": str(res_t),
        "residuo_F_biseccion": res_b, "dif_trazos_biseccion": abs(float(Ps) - Pb),
        "ponderado": str(pond), "ponderado_float": float(pond),
        "G_en_P": str(G(Vf, pf, Ps)), "L_en_P": str(L(Vf, pf, Ps)),
        "precio_si": str(psi), "precio_si_float": float(psi),
        "tope_normal_aplicado": (Ps > v_normal) if v_normal is not None else None,
        "precio_escenario_malo": (str(malo) if malo is not None else None),
    }
    if precio is not None:
        out["zona"] = zona(precio, malo, psi, pond)
    return out


def guardas_producto(V, p, k, precio=None):
    """Guardas de POLÍTICA del producto (no matemáticas), según Anexo C §C.1/C.6:
    k ≥ 1 · |Σp − 1| ≤ 1e-3 · p_i ≥ 0 · precio > 0 · valores numéricos · B78 ≤ C78 ≤ D78.
    Devuelve la lista de guardas que fallarían con estas entradas."""
    faltas = []
    Vf, pf, kf = validar(V, p, k)  # si falla el dominio, eso ya es un motivo aparte
    if kf < 1:
        faltas.append(f"k < 1 (producto exige k ≥ 1): k = {kf}")
    if any(x < 0 for x in pf):
        faltas.append("p_i < 0")
    if abs(sum(pf) - 1) > Fraction(1, 1000):
        faltas.append("|Σp − 1| > 1e-3")
    if len(V) == 3 and not (Vf[0] <= Vf[1] <= Vf[2]):
        faltas.append("valores desordenados (B78 ≤ C78 ≤ D78); el producto devuelve error G19")
    if precio is not None and _fraccion(precio) <= 0:
        faltas.append("precio actual ≤ 0")
    return faltas


def selftest():
    """Autocomprobación del oráculo con los cinco casos del Anexo C §C.5 (entradas) y las
    propiedades T1–T12; los valores esperados se calculan aquí, no se copian de ningún sitio."""
    casos = [
        ([60, 100, 150], ["1/4", "1/2", "1/4"], 3, 100, 90.1),
        ([90, 100, 160], ["1/5", "3/5", "1/5"], 3, 100, 90.0),
        ([100, 100, 100], ["1/5", "3/5", "1/5"], 3, 100, 100.0),
        ([-20, 80, 200], ["1/5", "3/5", "1/5"], 3, 80, 50.0),
        ([40, 70, 300], ["3/10", "1/2", "1/5"], 3, 70, 80.0),
    ]
    fallos = []
    for V, p, k, vn, precio in casos:
        r = resumen_caso(V, p, k, v_normal=vn, precio=precio)
        if r["residuo_F_trazos"] != "0":
            fallos.append(f"residuo trazos ≠ 0 en {V}: {r['residuo_F_trazos']}")
        if r["residuo_F_biseccion"] > 1e-9:
            fallos.append(f"residuo bisección > 1e-9 en {V}: {r['residuo_F_biseccion']}")
        if r["dif_trazos_biseccion"] > 1e-9:
            fallos.append(f"trazos ≠ bisección en {V}: {r['dif_trazos_biseccion']}")
        # T5: min V ≤ P* ≤ ponderado (k ≥ 1)
        lo = min(Fraction(str(v)) for v in V)
        if not (lo <= Fraction(r["P_estrella_trazos"]) <= Fraction(r["ponderado"])):
            fallos.append(f"P* fuera de [min V, ponderado] en {V}")
        # invariancia por permutación
        import random
        idx = list(range(len(V)))
        random.Random(7).shuffle(idx)
        Vp = [V[i] for i in idx]
        pp = [p[i] for i in idx]
        if p_estrella_trazos(Vp, pp, k) != Fraction(r["P_estrella_trazos"]):
            fallos.append(f"P* depende del orden en {V}")
        # traslación y escala
        if p_estrella_trazos([v + 7 for v in V], p, k) != Fraction(r["P_estrella_trazos"]) + 7:
            fallos.append(f"no equivariante por traslación en {V}")
        if p_estrella_trazos([2 * v for v in V], p, k) != 2 * Fraction(r["P_estrella_trazos"]):
            fallos.append(f"no equivariante por escala en {V}")
        # monotonía en k
        ks = [Fraction(1), Fraction(3, 2), Fraction(2), Fraction(5, 2), 3, 4, 5, 10]
        Ps = [p_estrella_trazos(V, p, kk) for kk in ks]
        if any(Ps[i + 1] > Ps[i] for i in range(len(Ps) - 1)):
            fallos.append(f"P* no decrece con k en {V}")
        # k = 1 ⇒ P* = ponderado
        if p_estrella_trazos(V, p, 1) != Fraction(r["ponderado"]):
            fallos.append(f"k=1 no da el ponderado en {V}")
    # masa cero: el escenario con p = 0 no arrastra a P*
    if p_estrella_trazos([50, 100, 150], ["0", "1/2", "1/2"], 3) != Fraction(225, 2):
        fallos.append("masa cero: P* debería ser 112.5")
    # dominio inválido
    for V, p, k in [([1, 2, 3], ["1/5", "3/5", "3/10"], 3), ([1, 2, 3], ["1/5", "3/5", "1/5"], 0),
                    ([1, 2, 3], ["-1/5", "6/5", "1/5"], 3), ([1, 2], ["1/2"], 3)]:
        try:
            p_estrella_trazos(V, p, k)
            fallos.append(f"no se rechazó {V} {p} k={k}")
        except DominioError:
            pass
    print("selftest oráculo: " + ("PASA" if not fallos else "FALLA: " + "; ".join(fallos)))
    return 0 if not fallos else 1


if __name__ == "__main__":
    import sys
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    print(__doc__)
