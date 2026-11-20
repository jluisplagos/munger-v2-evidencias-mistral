#!/usr/bin/env python3
"""Recálculo INDEPENDIENTE del revisor (no usa v63_xml.py, recalc.sh, leer_resultados.py ni precio_de_si.py).
  indep.py LIBRO SALIDA_DIR 'Hoja!REF=valor' ['Hoja!REF=valor' ...]
- copia el libro cambiando celdas de entrada directamente en el XML del zip (regex propia);
- recalcula con LibreOffice headless bajo flock del cerrojo común, con perfil propio (recalcular siempre al cargar);
- lee con openpyxl y calcula con código propio: P* (bisección de G(P) = k·L(P)), zona y crecimiento implícito (tabla A108:B188).
Imprime un JSON."""
import json, os, re, subprocess, sys, zipfile, shutil, hashlib
import openpyxl

LOCK = "/home/user/e_work/libreoffice.lock"
NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"

def parte_de_hoja(z, nombre):
    wb = z.read("xl/workbook.xml").decode("utf-8")
    rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
    m = re.search(r'<sheet\b[^>]*\bname="%s"[^>]*\br:id="([^"]+)"' % re.escape(nombre), wb) or \
        re.search(r'<sheet\b[^>]*\br:id="([^"]+)"[^>]*\bname="%s"' % re.escape(nombre), wb)
    rid = m.group(1)
    m2 = re.search(r'<Relationship\b[^>]*\bId="%s"[^>]*\bTarget="([^"]+)"' % re.escape(rid), rels) or \
         re.search(r'<Relationship\b[^>]*\bTarget="([^"]+)"[^>]*\bId="%s"' % re.escape(rid), rels)
    t = m2.group(1).lstrip("/")
    return t if t.startswith("xl/") else "xl/" + t

def editar(libro, destino, cambios):
    zin = zipfile.ZipFile(libro)
    por_parte = {}
    for clave, val in cambios.items():
        hoja, ref = clave.split("!")
        por_parte.setdefault(parte_de_hoja(zin, hoja), []).append((ref, val))
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as zout:
        for info in zin.infolist():
            datos = zin.read(info.filename)
            if info.filename in por_parte:
                x = datos.decode("utf-8")
                for ref, val in por_parte[info.filename]:
                    pat = re.compile(r'(<c\b[^>]*\br="%s"[^>]*>)(.*?)(</c>)' % re.escape(ref), re.S)
                    m = pat.search(x)
                    assert m, f"celda {ref} no encontrada"
                    assert "<f" not in m.group(2), f"{ref} tiene fórmula"
                    assert re.search(r"<v>[^<]*</v>", m.group(2)), f"{ref} sin <v>"
                    nuevo = re.sub(r"<v>[^<]*</v>", f"<v>{val!r}</v>", m.group(2), count=1)
                    x = x[:m.start()] + m.group(1) + nuevo + m.group(3) + x[m.end():]
                datos = x.encode("utf-8")
            zout.writestr(info, datos)
    zin.close()

def recalcular(entrada, outdir, perfil):
    os.makedirs(os.path.join(perfil, "user"), exist_ok=True)
    open(os.path.join(perfil, "user", "registrymodifications.xcu"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<oor:items xmlns:oor="http://openoffice.org/2001/registry" xmlns:xs="http://www.w3.org/2001/XMLSchema" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n'
        '<item oor:path="/org.openoffice.Office.Calc/Formula/Load"><prop oor:name="OOXMLRecalcMode" oor:op="fuse"><value>0</value></prop></item>\n'
        '<item oor:path="/org.openoffice.Office.Calc/Formula/Load"><prop oor:name="ODFRecalcMode" oor:op="fuse"><value>0</value></prop></item>\n'
        '<item oor:path="/org.openoffice.Office.Common/Misc"><prop oor:name="FirstRun" oor:op="fuse"><value>false</value></prop></item>\n</oor:items>\n')
    os.makedirs(outdir, exist_ok=True)
    r = subprocess.run(["flock", LOCK, "soffice", f"-env:UserInstallation=file://{os.path.abspath(perfil)}", "--headless", "--calc",
                        "--convert-to", "xlsx", "--outdir", outdir, entrada], capture_output=True, text=True, timeout=600)
    out = os.path.join(outdir, os.path.basename(entrada))
    assert os.path.isfile(out), "LibreOffice no produjo salida: " + r.stdout[-300:] + r.stderr[-300:]
    return out

def G(V, p, P): return sum(q * max(v - P, 0.0) for v, q in zip(V, p))
def Lf(V, p, P): return sum(q * max(P - v, 0.0) for v, q in zip(V, p))

def p_estrella_biseccion(V, p, k):
    lo, hi = min(V), max(V)
    f = lambda P: G(V, p, P) - k * Lf(V, p, P)   # decreciente en P
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) >= 0: lo = mid
        else: hi = mid
    return lo

def zona(precio, malo, psi, pond):
    if malo is not None and malo > 0 and precio <= malo: return "bajo_malo"
    if precio <= psi: return "cumple_regla_k"
    if precio <= pond: return "vigilar"
    return "caro"

def leer(libro, k=3.0):
    wb = openpyxl.load_workbook(libro, data_only=True)
    A, D, M = wb["Análisis"], wb["Diagnóstico V6"], wb["Motor"]
    V = [A["B78"].value, A["C78"].value, A["D78"].value]
    p = [A["B69"].value, A["C69"].value, A["D69"].value]
    precio = A["C37"].value
    out = {"C56": A["C56"].value, "motor": D["C5"].value, "r_operativa_C15": D["C15"].value, "r_minima_C17": D["C17"].value, "r_vs_minima_C18": D["C18"].value,
           "V": V, "p": p, "precio": precio, "C83": A["C83"].value, "C86": A["C86"].value, "J6_J8": [M["J6"].value, M["J7"].value, M["J8"].value],
           "estado_B255": M["B255"].value, "B252": M["B252"].value, "B253": M["B253"].value, "B254": M["B254"].value, "B193": M["B193"].value,
           "roic_lp": [wb["Palancas"][c].value for c in ("B18", "C18", "D18")],
           "flujos_normal": [M.cell(7, c).value for c in range(47, 57)], "flujo11_normal": M["BF7"].value, "g_normal": M["H7"].value,
           "ajuste_M7": M["M7"].value, "acciones_P7": M["P7"].value, "semaforo_43": [D["B43"].value, D["C43"].value, D["D43"].value]}
    if all(isinstance(x, (int, float)) for x in V + p) and isinstance(precio, (int, float)):
        P = p_estrella_biseccion(V, p, k)
        pond = sum(v * q for v, q in zip(V, p))
        psi = min(P, V[1])
        out.update({"P_estrella": P, "precio_si": psi, "ponderado": pond, "zona": zona(precio, V[0], psi, pond)})
        # crecimiento implícito: tabla A108:B188 (g, valor), interpolación lineal inversa
        tab = [(A.cell(r, 1).value, A.cell(r, 2).value) for r in range(108, 189)]
        tab = [(g, v) for g, v in tab if isinstance(g, (int, float)) and isinstance(v, (int, float))]
        gi = None
        if len(tab) >= 2:
            if precio < tab[0][1]: gi = "< -10%"
            elif precio > tab[-1][1]: gi = "> 30%"
            else:
                for (g0, v0), (g1, v1) in zip(tab, tab[1:]):
                    if v0 <= precio <= v1:
                        gi = g0 if v1 == v0 else g0 + (g1 - g0) * (precio - v0) / (v1 - v0); break
        out["g_impl_tabla"] = gi
    wb.close()
    return out

if __name__ == "__main__":
    libro, outdir = sys.argv[1], sys.argv[2]
    cambios = {}
    for a in sys.argv[3:]:
        kk, vv = a.split("=", 1); cambios[kk] = float(vv)
    os.makedirs(os.path.join(outdir, "in"), exist_ok=True)
    copia = os.path.join(outdir, "in", os.path.basename(libro))
    editar(libro, copia, cambios)
    rec = recalcular(copia, os.path.join(outdir, "out"), os.path.join(outdir, "perfil"))
    res = leer(rec)
    res["cambios"] = cambios
    print(json.dumps(res, ensure_ascii=False, indent=1, default=str))
