"""Réplica propia del motor A (Convenciones_financieras_V6_3.md §1–§3, §5 y §10; fórmulas de Motor!AU:BO del libro V6.3.1 F1)
y de la escalera (precio_de_si.py: p_estrella, zona). Solo lectura de los libros; no sustituye al recálculo oficial.

Dictamen de perímetro y G4 · 18-nov-2026 · agente independiente (no es autor de la plantilla, de F1 ni de las fases)."""
import openpyxl

ESC = ("MALO", "NORMAL", "BUENO")
COLS_HIST = "CDEFGHIJKL"


def leer(ruta, rangos):
    """Valores en caché de un libro recalculado: {'Hoja!A1': valor}."""
    wb = openpyxl.load_workbook(ruta, data_only=True, read_only=True)
    v = {}
    for hoja, rango in rangos:
        for fila in wb[hoja][rango]:
            for c in fila:
                if c.value is not None:
                    v[f"{hoja}!{c.coordinate}"] = c.value
    wb.close()
    return v


RANGOS = [("Historia", "A5:L90"), ("Análisis", "B14:D90"), ("Palancas", "B5:I24"), ("Motor", "A6:BT8"), ("Diagnóstico V6", "B5:D50"),
          ("Diagnóstico V6", "B174:D179")]


def base_del_libro(L):
    """Entradas del motor A tal como las usa la hoja Motor (C, D, K, L, J, M, P de la fila 7)."""
    return dict(V0=float(L["Motor!C7"]), m0=float(L["Motor!D7"]), tau=float(L["Motor!K7"]), f=float(L["Motor!L7"]),
                r=float(L["Motor!J7"]), ajuste=float(L.get("Motor!M7") or 0.0), acciones=float(L["Motor!P7"]))


def palancas_del_libro(L):
    out = {}
    for esc, fila in zip(ESC, (6, 7, 8)):
        out[esc] = dict(g5=float(L[f"Motor!E{fila}"]), mobj=float(L[f"Motor!F{fila}"]), s2c=float(L[f"Motor!G{fila}"]),
                        ginf=float(L[f"Motor!H{fila}"]), roic=float(L[f"Motor!I{fila}"]))
    return out


def motor(V0, m0, tau, f, r, g5, mobj, s2c, ginf, roic, ajuste=0.0, acciones=1.0):
    """Motor A: flujo_t = V_t·[m_t(1−τ) − f] − ΔV_t/S2C (t = 1…10); año 11 = V₁₀(1+g∞)[m_obj(1−τ)(1 − g∞/ROIC) − f]."""
    V_prev, vp, flujos, V, reinv = V0, 0.0, [], [], []
    for t in range(1, 11):
        g = g5 if t <= 5 else g5 - (g5 - ginf) * (t - 5) / 5
        Vt = V_prev * (1 + g)
        m = m0 + (mobj - m0) * min(t, 5) / 5
        ri = (Vt - V_prev) / s2c
        fl = Vt * (m * (1 - tau) - f) - ri
        flujos.append(fl)
        reinv.append(ri)
        V.append(Vt)
        vp += fl / (1 + r) ** t
        V_prev = Vt
    V11 = V_prev * (1 + ginf)
    N = mobj * (1 - tau)
    f11 = V11 * (N * (1 - ginf / roic) - f)
    reinv11 = V11 * N * ginf / roic
    vt = f11 / (r - ginf)
    vp_t = vt / (1 + r) ** 10
    total = vp + vp_t + ajuste
    return {"flujos": flujos, "V": V, "reinv": reinv, "flujo_11": f11, "reinv_11": reinv11, "V11": V11, "vp_1_10": vp, "vp_terminal": vp_t,
            "total": total, "por_accion": total / acciones, "peso_terminal": vp_t / (vp + vp_t),
            "rent_marginal": s2c * mobj * (1 - tau), "salto_11": s2c * mobj * (1 - tau) - roic,
            # S2C que el terminal usa de hecho: la reinversión del año 11 es ΔV₁₂ × N/ROIC, así que S2C_terminal = ROIC ÷ N
            "s2c_terminal_implicito": roic / N}


def sin_crecimiento(V0, m0, tau, f, r, ajuste=0.0, acciones=1.0, **_):
    """Motor!BL: V0·(m0(1−τ) − f)/r + ajuste."""
    return (V0 * (m0 * (1 - tau) - f) / r + ajuste) / acciones


def p_estrella(V, p, k=3.0):
    """Precio más alto con G(P) ≥ k·L(P) (precio_de_si.py: forma cerrada por tramos)."""
    s = sorted(zip(V, p))
    for j in (1, 2):
        bajo, alto = s[:j], s[j:]
        num = sum(pp * v for v, pp in alto) + k * sum(pp * v for v, pp in bajo)
        den = sum(pp for v, pp in alto) + k * sum(pp for v, pp in bajo)
        P = num / den
        if s[j - 1][0] - 1e-12 <= P <= s[j][0] + 1e-12:
            return P
    raise AssertionError("P* no cae en ningún tramo")


def zona(precio, malo, precio_si, pond):
    if malo is not None and precio <= malo:
        return "bajo_malo"
    if precio <= precio_si:
        return "cumple_regla_k"
    if precio <= pond:
        return "vigilar"
    return "caro"


def escalera(V, p, precio, k=3.0):
    pond = sum(v * q for v, q in zip(V, p))
    P = p_estrella(V, p, k)
    ps = min(P, V[1])
    return {"V": V, "ponderado": pond, "precio_si": ps, "zona": zona(precio, V[0] if V[0] > 0 else None, ps, pond)}


def tres(base, pal, **cambios):
    """Valores por acción de los tres escenarios. cambios: {'s2c': (a, b, c), 'roic': (...), 'f': x, ...}."""
    b = dict(base)
    for k in ("V0", "m0", "tau", "f", "r", "ajuste", "acciones"):
        if k in cambios:
            b[k] = cambios[k]
    out = []
    for i, e in enumerate(ESC):
        pv = dict(pal[e])
        for k in ("g5", "mobj", "s2c", "ginf", "roic"):
            if k in cambios:
                pv[k] = cambios[k][i]
        out.append(motor(**b, **pv))
    return out


def gramatica(base, pal, c55, c18, umbral_g4=0.03, umbral_g8=0.05, c55_g7=None):
    """G4, G7 y G8 tal como los evalúa comprobar_gramatica.py (:228–239, :261–274, :338–351).
    c55_g7: ancla del ROIC histórico para G7 (por defecto, la del producto: Historia!C55)."""
    h = []
    c55_g7 = c55 if c55_g7 is None else c55_g7
    for e in ESC:
        pv = pal[e]
        if pv["roic"] > base["r"] + umbral_g4 + 1e-9:
            h.append(("G4", e, f"ROIC LP {pv['roic']:.2f} > r + {umbral_g4:.2f} = {base['r'] + umbral_g4:.3f}",
                      "justificable" if c18 == "Sí" else "SIN JUSTIFICACIÓN POSIBLE (C18 ≠ Sí)"))
        rm = pv["s2c"] * pv["mobj"] * (1 - base["tau"])
        if rm > 2 * c55_g7 + 1e-9:
            h.append(("G7", e, f"rentabilidad marginal {rm:.3f} > 2 × {c55_g7:.4f} = {2 * c55_g7:.3f}", "justificable"))
        if abs(rm - pv["roic"]) > umbral_g8 + 1e-9:
            h.append(("G8", e, f"salto del año 11 {rm - pv['roic']:+.3f} (> {umbral_g8})", "justificable (tesis u Observación de B18:D18)"))
    return h
