#!/usr/bin/env python3
"""Extractor complementario del registro de entradas de Ahold (examen). Completa la copia de trabajo:
21 celdas F1 sin entrada, 30 hipótesis sin fundamento y 6 celdas de Análisis sin resolver. No toca las entradas de Mistral.
Uso: completar.py CARPETA (copia de trabajo con verificacion_entradas.json de Mistral, ronda 1)"""
import copy
import hashlib
import json
import os
import re
import sys

W = sys.argv[1]
EXT = "claude-opus-extractor-complementario"
HOY = "2026-11-18"
REG = os.path.join(W, "verificacion_entradas.json")
reg = json.load(open(REG, encoding="utf-8"))
por = {e["celda"]: e for e in reg["entradas"]}
EVID = json.load(open(sys.argv[2], encoding="utf-8"))  # filas del Control maestro del libro (evidencia_libro)
A = json.load(open(os.path.join(W, "celdas_A.json"), encoding="utf-8"))
B = json.load(open(os.path.join(W, "celdas_B.json"), encoding="utf-8"))


def sha(p):
    return hashlib.sha256(open(os.path.join(W, p), "rb").read()).hexdigest()


def pagina(archivo, n):
    t = open(os.path.join(W, archivo), encoding="utf-8").read()
    m = re.search(r"\[PDF PAGE %d\]" % n, t)
    fin = re.search(r"\[PDF PAGE \d+\]", t[m.end():])
    return t[m.end(): m.end() + fin.start()] if fin else t[m.end():]


def linea(archivo, n, desde, despues=None):
    """Fragmento literal de la línea de la página n que contiene `desde` (desde ahí hasta el final de la línea); con `despues`, la
    primera línea así situada tras la línea que contiene `despues`."""
    lineas = pagina(archivo, n).split("\n")
    i0 = 0
    if despues:
        i0 = next(i for i, l in enumerate(lineas) if despues in l)
    for l in lineas[i0:]:
        j = l.find(desde)
        if j >= 0:
            return l[j:].rstrip()
    raise SystemExit(f"no encuentro {desde!r} en {archivo} p.{n}")


def comp(fuente_examinada, nota):
    return {"extractor": EXT, "revisor": None, "fecha": HOY, "resultado": "pendiente", "fuente_examinada": fuente_examinada, "nota": nota}


# metadatos de los documentos, tal como los registró Mistral (documento y versión del PDF oficial)
DOCS = {}
for e in reg["entradas"]:
    f = e.get("fuente") or {}
    if str(f.get("archivo") or "").startswith("texto/") and f["archivo"] not in DOCS:
        DOCS[f["archivo"]] = {"documento": f["documento"], "version": f["version"], "sha256": f["sha256"]}
for a, d in DOCS.items():
    assert sha(a) == d["sha256"], a

AR = {y: f"texto/AD_annual-report-{y}.txt" for y in range(2016, 2026)}
Q2 = "texto/AD_q2-2026-interim-report.txt"
CIERRE = {2016: "2017-01-01 (52 sem.)", 2017: "2017-12-31 (52 sem.)", 2018: "2018-12-30 (52 sem.)", 2019: "2019-12-29 (52 sem.)",
          2020: "2021-01-03 (53 sem.)", 2021: "2022-01-02 (52 sem.)", 2022: "2023-01-01 (52 sem.)", 2023: "2023-12-31 (52 sem.)",
          2024: "2024-12-29 (52 sem.)", 2025: "2025-12-28 (52 sem.)"}
COL = dict(zip("CDEFGHIJKL", range(2016, 2026)))


def fuente(archivo, pag, folio, ubicacion, concepto, columna, periodo, valor_fuente, cita, signo=1, tratamiento="cifra tal como se publica; signo 1, sin transformación",
           reexpresado="no aplica (ejercicio corriente del informe)", unidad="millones de euros"):
    d = DOCS[archivo]
    return {"documento": d["documento"], "version": d["version"], "archivo": archivo, "sha256": d["sha256"], "pagina": pag, "folio": folio,
            "ubicacion": ubicacion, "concepto": concepto, "columna": columna, "periodo": periodo, "unidad": unidad, "escala": 1, "signo": signo,
            "tratamiento": tratamiento, "perimetro": "consolidado", "reexpresado": reexpresado, "valor_fuente": valor_fuente, "cita": cita}


def nueva(celda, ident, clase, valor, ambito="calculo", **kw):
    e = {"celda": celda, "id": ident, "ambito": ambito, "uso": None, "material": True, "clase": clase, "valor_modelo": valor, "fuente": {},
         "derivacion": None, "hipotesis": None, "justificacion": None}
    e.update(kw)
    e.setdefault("incidencia", None)
    return e


nuevas = []

# ------------------------------------------------------------------------------------------------ 1. filas F1 (Historia 85–87)
decl = json.load(open(os.path.join(W, "motor_a_f1.json"), encoding="utf-8"))
reg_per = decl["perimetro_reinversion"]["registro"]
nuevas.append(nueva(
    "Historia!C85", "F1.perimetro_reinversion", "hipotesis", "A2_propio",
    hipotesis={
        "identificacion": "H-F1.perimetro_reinversion (motor_a_f1.json → perimetro_reinversion)",
        "fundamento": ("Decisión registrada de la persona responsable, 18-nov-2026, «Examen · F1-A · Reinversión necesaria (regla general)» "
                       "(munger-v2-evidencias-mistral, coordinacion/cierre_v2/DECISIONES_PARA_EL_USUARIO.md, línea 88): «en las empresas del examen del motor A "
                       "con arrendamientos, si la empresa no publica el reparto entre mantenimiento y crecimiento, la reinversión necesaria se iguala a su "
                       "amortización propia sin los derechos de uso (perímetro A2, «A2_propio»), como hipótesis declarada, no como dato». La declaración F1 del "
                       "expediente la recoge (motor_a_f1.json → perimetro_reinversion.valor = «A2_propio»; registro: " + json.dumps(reg_per, ensure_ascii=False)
                       + ") y su nota dice «La reinversión A2 es una HIPÓTESIS DECLARADA, no un dato». Hecho que la condiciona: Ahold no publica el reparto del capex "
                       "entre mantenimiento y crecimiento (motor_a_f1.json → clasificacion_compras.fundamento). El libro escribe C85 con f1_libro_v631.py aplicar."),
        "alternativas": ("A0_total (toda la D&A de la fila 8 como reposición, el perímetro de la V6.3: celda vacía); A1_sin_ROU (sin la D&A de derechos de uso, "
                         "con la PPA dentro); A3_estimado (reinversión estimada: no existe en el libro V6.3.1 F1 y dejaría C85 vacío). La decisión F1 (1a) del "
                         "17-nov (excluir la amortización ROU) es compatible con A1 y con A2; F1-A elige A2 para todas las empresas del examen."),
        "limites": ("Hipótesis declarada, no dato publicado; una firma no la demuestra y no se adopta para dinero real. Con A2 la D_X (fila 88) exige D&A, "
                    "ROU y PPA del año: con la PPA de 2021–2022 desconocida (filas 86–87 vacías) el ancla de S2C de A2 (cinco años H–L) queda vacía y f "
                    "solo se calibra con 2023–2025 (motor_a_f1.json → series.da_ppa_sin_declarar.efecto). Solo se separa como PPA la clase «Franchisee and "
                    "affiliate relationships»; el resto de intangibles adquiridos queda dentro de la D&A propia. Los deterioros de derechos de uso siguen en "
                    "la fila 8. El personaje la presenta condicionada y con su sensibilidad (F1-A)."),
        "procedencia": "motor_a_f1.json (declaración F1 del expediente) → Historia!C85 del libro (f1_libro_v631.py aplicar)"},
    comprobacion=comp("motor_a_f1.json → perimetro_reinversion; DECISIONES_PARA_EL_USUARIO.md:88 (rama coordinacion/cierre-v2 del repositorio auxiliar)",
                      "Configuración de la capa F1 (tipo «configuracion» del universo): hipótesis declarada por la persona, no dato; se registra con su fundamento, "
                      "alternativas y límites. El revisor comprueba que el texto citado de la decisión es el vigente.")))

ROU = {2021: (AR[2022], 251, 250, "2022 · 2021", "comparativo del informe 2022; el informe 2021 publica la misma cifra (AR2021, PDF p. 242: «(1,134)»)"),
       2022: (AR[2023], 262, 261, "2023 · 2022", "comparativo del informe 2023; el informe 2022 publica la misma cifra (AR2022, PDF p. 251: «(1,300)»)"),
       2023: (AR[2024], 321, 320, "2024 · 2023", "comparativo del informe 2024; el informe 2023 publica la misma cifra (AR2023, PDF p. 262: «(1,336)»)"),
       2024: (AR[2025], 272, 271, "2025 · 2024", "comparativo del informe 2025; el informe 2024 publica la misma cifra (AR2024, PDF p. 321: «(1,333)»)"),
       2025: (AR[2025], 272, 271, "2025 · 2024", "no aplica (ejercicio corriente del informe)")}
for c, y in COL.items():
    k = f"Historia!{c}86"
    if y in ROU:
        arch, pag, fol, cols, reex = ROU[y]
        s = decl["series"]["da_rou"][str(y)]
        vf = s["valor_fuente"]
        cita = linea(arch, pag, "Depreciation charge for right-of-use assets")
        nuevas.append(nueva(k, "F1.da_rou", "dato_publicado", -vf, fuente=fuente(
            arch, pag, fol, "nota 33 Leases, cuadro «Amounts recognized in the income statement» (columnas " + cols + ")",
            "Depreciation charge for right-of-use assets: amortización de derechos de uso (NIIF 16), incluidos los derechos de uso de inversiones "
            "inmobiliarias; los deterioros de derechos de uso se publican aparte, bajo el cuadro, y no están en esta línea",
            f"{y} (" + ("columna del ejercicio corriente" if y == 2025 else "columna comparativa") + f" del cuadro {cols})",
            f"ejercicio {y} (cerrado el {CIERRE[y]})", vf, cita, signo=-1,
            tratamiento="cargo publicado entre paréntesis («" + s["literal"] + "» = −" + f"{-vf:,}".replace(",", ".") + "); el libro guarda la magnitud positiva (signo −1), como la declaración F1 "
                        f"(motor_a_f1.json → series.da_rou.{y})", reexpresado=reex),
            comprobacion=comp(f"{arch} [PDF PAGE {pag}]", f"Serie F1 da_rou {y} de motor_a_f1.json (documento, página y literal coinciden). La cita de la "
                                                          "declaración no es literal (omite la otra columna): aquí se cita la línea completa de la página.")))
    elif y <= 2017:
        nuevas.append(nueva(k, "F1.da_rou", "no_aplicable", None, justificacion=(
            f"Ejercicio {y} en base NIC 17: la NIIF 16 se adoptó en 2019 con reexpresión solo de 2018 (AR2019; historia_revision.md, «ebit 2018»: "
            "«Cifras 2018 reexpresadas por la adopción de IFRS 16 (método retrospectivo completo, nota 36)»; AR2025, PDF p. 65, nota 1: «Financial "
            "information prior to December 30, 2018, has not been restated for the impact of the implementation of IFRS 16»). En " + str(y) + " no hay "
            "activos por derecho de uso ni su amortización; la Historia de ese año es NIC 17 (fila 23 de arrendamientos = 0). Celda vacía en el libro "
            "(declaración F1 sin ese año); no es un cero comprobado porque el libro no escribe 0."),
            comprobacion=comp(f"{AR[2025]} [PDF PAGE 65] (nota 1 del resumen plurianual)", "Vacía en el libro. Alternativa: registrar «cero comprobado» si el "
                                                                                        "libro escribiera 0; con la celda vacía, «no aplicable».")))
    else:
        pub = {2018: ("AR2019, PDF p. 183", "(1,000)"), 2019: ("AR2020, PDF p. 208", "(1,052)"), 2020: ("AR2021, PDF p. 242", "(1,083)")}[y]
        nuevas.append(nueva(k, "F1.da_rou", "dato_ausente", None, justificacion=(
            f"El libro deja la celda vacía (fila 86: «vacío = desconocido») porque la declaración F1 (motor_a_f1.json → series.da_rou) solo declara "
            f"2021–2025: f se calibra con 2023–2025 y el ancla de S2C usa los cinco años H–L. Para {y} no hay dato en el libro que contrastar. "
            f"El informe sí publica la cifra ({pub[0]}, «Depreciation charge for right-of-use assets» {pub[1]}, comparativo o corriente): "
            "registrarla exigiría que la persona la añadiera a la declaración; no se escribe aquí."),
            incidencia=f"Dato publicado disponible ({pub[0]}: {pub[1]}) que el libro no usa; no cambia f ni el ancla con la ventana declarada.",
            comprobacion=comp(f"motor_a_f1.json → series.da_rou; {pub[0]}", "Celda vacía (= desconocido) en el libro; no es cero.")))

PPA = {2023: (AR[2024], 284, 283, "Year ended December 31, 2023", "no aplica: el informe 2024 es el primero que separa la clase «Franchisee and affiliate "
              "relationships» (con 2023 reexpresado); el informe 2023 la incluía en «Other» (AR2023, PDF p. 227)"),
       2024: (AR[2025], 236, 235, "Year ended December 29, 2024", "comparativo del informe 2025; el informe 2024 publica la misma cifra (AR2024, PDF p. 284, bloque "
              "«Year ended December 29, 2024»: «(18)»)"),
       2025: (AR[2025], 236, 235, "Year ended December 28, 2025", "no aplica (ejercicio corriente del informe)")}
OTHER = {2016: "AR2016, PDF p. 154", 2017: "AR2017, PDF p. 165", 2018: "AR2018, PDF p. 131", 2019: "AR2019 (nota de intangibles)",
         2020: "AR2020 (nota de intangibles)", 2021: "AR2022, PDF p. 215–216", 2022: "AR2023, PDF p. 226–227"}
for c, y in COL.items():
    k = f"Historia!{c}87"
    if y in PPA:
        arch, pag, fol, bloque, reex = PPA[y]
        s = decl["series"]["da_ppa"][str(y)]
        vf = s["valor_fuente"]
        cita = linea(arch, pag, "Amortization", despues=bloque)
        nuevas.append(nueva(k, "F1.da_ppa", "dato_publicado", -vf, fuente=fuente(
            arch, pag, fol, "nota 14 Intangible assets, cuadro de movimientos, bloque «" + bloque + "», fila «Amortization»",
            "Amortización de la clase «Franchisee and affiliate relationships» (relaciones con franquiciados y afiliados de Grecia y Bélgica reconocidas "
            "en la fusión Ahold Delhaize: la única clase que el informe atribuye expresamente a una combinación de negocios; PPA de la declaración F1)",
            f"columna «Franchisee and affiliate relationships» (cuarta columna de importes) del bloque «{bloque}» (ejercicio {y})",
            f"ejercicio {y} (cerrado el {CIERRE[y]})", vf, cita, signo=-1,
            tratamiento="cargo publicado entre paréntesis («(18)» = −18); el libro guarda la magnitud positiva (signo −1), como la declaración F1 "
                        f"(motor_a_f1.json → series.da_ppa.{y}); no se reparte ninguna otra clase de intangible", reexpresado=reex),
            comprobacion=comp(f"{arch} [PDF PAGE {pag}]", "Serie F1 da_ppa de motor_a_f1.json. La cita de la declaración es la frase de política (no contiene la "
                                                          "cifra); aquí se cita la fila «Amortization» del bloque del año, cuyo cuarto importe es (18). La columna es "
                                                          "una clase de activo, no un ejercicio: el año lo fija el bloque (F1-SERIES la deja «pendiente»).")))
    else:
        j = ((decl["series"].get("da_ppa_sin_declarar") or {}).get(str(y)))
        base = (f"Declaración F1 (motor_a_f1.json → series.da_ppa_sin_declarar.{y}): «{j}»" if j else
                f"La declaración F1 no declara {y} (motor_a_f1.json → series.da_ppa solo 2023–2025)")
        nuevas.append(nueva(k, "F1.da_ppa", "dato_ausente", None, justificacion=(
            base + f". Hasta el informe 2023 la amortización de las relaciones con franquiciados va dentro de «Other» junto con otros intangibles "
            f"(«“Other” mainly includes intangible assets related to relationships with franchisees and affiliates recognized in connection with the Ahold "
            f"Delhaize merger, location development rights, deed restrictions and similar assets»; {OTHER[y]}); el informe no la separa y no se reparte. "
            "Celda vacía en el libro («vacío = desconocido»), no cero."),
            comprobacion=comp(f"motor_a_f1.json → series; {OTHER[y]}", "Celda vacía (= desconocido) en el libro; no es cero.")))

# ------------------------------------------------------------------------------------------------ 2. hipótesis (30)
sys.path.insert(0, "/home/user/e_work/wt_examen/munger_v2_r1/personaje_v2/scripts")
import verificacion_entradas as V  # noqa: E402
INST = V.universo(W)
CAMBIOS_VM = []
for k, e in por.items():
    if e.get("clase") != "hipotesis":
        continue
    ev = EVID[k]
    n = ev["N"]
    m_cl = re.match(r"\[Clase: ([^\]]+)\] \[Confianza: ([^\]]+)\]", n)
    clase_decl, conf = m_cl.group(1), m_cl.group(2)
    clase = "convencion" if clase_decl.startswith("convenci") else "hipotesis"
    ref = re.search(r"(Referencia mecánica:.*?)(?=\s*Apoyo:|\s*Lo sustituiría:|$)", n, re.S)
    sust = re.search(r"(Lo sustituiría:.*)$", n, re.S)
    rango = re.search(r"(Rango[^.]*?\d[^.]*?)\.(?:\s|$)", n)
    alt = " · ".join(x.group(1).strip() for x in (ref, sust) if x) or "El texto de la fase no declara alternativa."
    fase = "fase A (celdas_A.json)" if k in A else "fase B (celdas_B.json)" if k in B else None
    proc = (f"Control maestro!N{ev['fila']} del libro (Ahold_v63_evaluada.xlsx)" + (f"; escrito en la {fase}" if fase else
            f"; fila de metadatos ({k} no está en celdas_A.json ni en celdas_B.json)"))
    fund = n + (f" [Evidencia preparada, Control maestro!M{ev['fila']}: {ev['M']}]" if ev.get("M") else "")
    e["clase"] = clase
    if not V.EE.iguales(e.get("valor_modelo"), INST["celdas"].get(k)) if hasattr(V.EE, "iguales") else e.get("valor_modelo") != INST["celdas"].get(k):
        CAMBIOS_VM.append(f"{k}: {e.get('valor_modelo')!r} → {INST['celdas'].get(k)!r}")
    e["valor_modelo"] = INST["celdas"].get(k)
    e["hipotesis"] = {
        "identificacion": ("V-" if clase == "convencion" else "H-") + str(e["id"]),
        "fundamento": fund,
        "alternativas": alt,
        "limites": ((f"Rango declarado: {rango.group(1)}." if rango else "Sin rango declarado.") + f" Confianza declarada: {conf}. Es juicio del inversor "
                    f"({ev.get('D')}), clase declarada «{clase_decl}»: no es un dato publicado ni se demuestra con una firma; las cifras y páginas de apoyo "
                    "no se han contrastado en este registro (apoyan el juicio, no son entradas). Texto del expediente en curso (fase C, turno 2, provisional): "
                    "si la fase C lo reescribe, este fundamento deja de describir la celda."),
        "procedencia": proc}
    e["comprobacion"] = comp(proc, f"Fundamento, alternativas y límites copiados del texto de la fase (Control maestro!N{ev['fila']}); clase «{clase}» según la "
                                   f"clase que declara la fase («{clase_decl}»). No se juzga su acierto.")
    e.pop("incidencia", None)
    e["incidencia"] = None

# ------------------------------------------------------------------------------------------------ 3. Análisis sin resolver
ET1 = "etapa1/Ahold_evaluada.xlsx"


def et1(fila, cols="GHIJKLMN"):
    ev = EVID_E1[str(fila)]
    return " · ".join(f"{c}: «{ev[c]}»" for c in cols if ev.get(c))


EVID_E1 = json.load(open(sys.argv[3], encoding="utf-8"))  # filas del Control maestro de etapa1/Ahold_evaluada.xlsx (por número de fila)


def aux_pub(clave, ident, archivo, pag, folio, ubicacion, concepto, columna, periodo, vf, cita, nota, **kw):
    return nueva(clave, ident, "dato_publicado", vf, ambito=None, fuente=fuente(archivo, pag, folio, ubicacion, concepto, columna, periodo, vf, cita, **kw),
                 comprobacion=comp(f"{archivo} [PDF PAGE {pag}]", nota))


def set_entrada(k, **kw):
    e = por[k]
    for c in ("fuente", "derivacion", "hipotesis", "justificacion"):
        e[c] = {} if c == "fuente" else None
    e.update(kw)
    e.setdefault("incidencia", None)


# C26 · CFO ÷ beneficio neto, Σ 2021–2025
o26 = [f"Historia!{c}11" for c in "HIJKL"] + [f"Historia!{c}9" for c in "HIJKL"]
set_entrada("Análisis!C26", clase="derivado", derivacion={
    "origenes": o26,
    "formula": "round((" + " + ".join(f'o["{x}"]' for x in o26[:5]) + ") / (" + " + ".join(f'o["{x}"]' for x in o26[5:]) + "), 4)",
    "conciliacion": ("Cálculo de la etapa 1 de la persona (etapa1/Ahold_evaluada.xlsx, Control maestro fila 31, columna M: «Literal: Σ CFO 31.257 ÷ Σ beneficio neto "
                     "10.694 = 2,92x»; período «Σ FY2021–FY2025»): CFO 2021–2025 (Historia H11:L11) = 5.468 + 6.110 + 6.466 + 6.224 + 6.989 = 31.257; beneficio "
                     "neto atribuible 2021–2025 (H9:L9) = 2.246 + 2.546 + 1.874 + 1.764 + 2.264 = 10.694; 31.257 ÷ 10.694 = 2,922854… → round(…, 4) = 2,9229 "
                     "= libro (Análisis!C26). El valor lo escribe la etapa 1 (no está en fase1_v63.json → analisis; DEP_ANALISIS de fase1_historia.py "
                     "lo asocia a cfo y beneficio_neto)."),
    "unidad": None},
    comprobacion=comp(f"{ET1} (Control maestro fila 31; Análisis!C26) e Historia H9:L11", "Derivado exacto (fracciones) desde diez celdas de la Historia; "
                      "la fórmula es la que declara la etapa 1. Mistral daba 3,0877 con otra lectura; esta reproduce 2,9229."))

# C33 · deuda neta ÷ EBITDA LTM a 28-jun-2026
nuevas += [
    aux_pub("aux:Q2-2026_p11_operating_income_hy2026", "aux_ebitda_ltm", Q2, 11, 11, "cuenta de resultados consolidada (interim)",
            "Operating income, columna HY 2026", "HY 2026 (26 semanas hasta el 28-jun-2026)", "primer semestre 2026 (cerrado el 2026-06-28)", 1760,
            linea(Q2, 11, "Operating income"), "Componente del EBITDA LTM de C33 y C42 (resultado operativo LTM = FY2025 + HY2026 − HY2025)."),
    aux_pub("aux:Q2-2026_p11_operating_income_hy2025", "aux_ebitda_ltm", Q2, 11, 11, "cuenta de resultados consolidada (interim)",
            "Operating income, columna HY 2025", "HY 2025 (26 semanas hasta el 29-jun-2025)", "primer semestre 2025 (cerrado el 2025-06-29)", 1741,
            linea(Q2, 11, "Operating income"), "Componente del EBITDA LTM de C33 y C42.", reexpresado="comparativo del informe interino Q2 2026"),
    aux_pub("aux:Q2-2026_p15_da_impairments_hy2026", "aux_ebitda_ltm", Q2, 15, 15, "estado consolidado de flujos de caja (interim), ajustes",
            "Depreciation, amortization and impairments, columna HY 2026", "HY 2026 (26 semanas hasta el 28-jun-2026)", "primer semestre 2026 (cerrado el 2026-06-28)",
            1828, linea(Q2, 15, "Depreciation, amortization and impairments"), "Componente del EBITDA LTM (D&A y deterioros LTM = FY2025 + HY2026 − HY2025)."),
    aux_pub("aux:Q2-2026_p15_da_impairments_hy2025", "aux_ebitda_ltm", Q2, 15, 15, "estado consolidado de flujos de caja (interim), ajustes",
            "Depreciation, amortization and impairments, columna HY 2025", "HY 2025 (26 semanas hasta el 29-jun-2025)", "primer semestre 2025 (cerrado el 2025-06-29)",
            1870, linea(Q2, 15, "Depreciation, amortization and impairments"), "Componente del EBITDA LTM de C33 y C42.",
            reexpresado="comparativo del informe interino Q2 2026"),
]
EBITDA = ('(o["Historia!L7"] + o["aux:Q2-2026_p11_operating_income_hy2026"] - o["aux:Q2-2026_p11_operating_income_hy2025"]'
          ' + o["Historia!L8"] + o["aux:Q2-2026_p15_da_impairments_hy2026"] - o["aux:Q2-2026_p15_da_impairments_hy2025"])')
O_EBITDA = ["Historia!L7", "aux:Q2-2026_p11_operating_income_hy2026", "aux:Q2-2026_p11_operating_income_hy2025", "Historia!L8",
            "aux:Q2-2026_p15_da_impairments_hy2026", "aux:Q2-2026_p15_da_impairments_hy2025"]
set_entrada("Análisis!C33", clase="derivado", derivacion={
    "origenes": ["Análisis!C54", "Análisis!C53"] + O_EBITDA,
    "formula": f'round((o["Análisis!C54"] - o["Análisis!C53"]) / {EBITDA}, 4)',
    "conciliacion": ("Cálculo de la etapa 1 (etapa1/Ahold_evaluada.xlsx, Control maestro fila 36, M: «(deuda bruta con arrendamientos 19.261 − caja 3.196) = 16.065 ÷ "
                     "EBITDA LTM 7.252 (resultado operativo 3.561 + D&A 3.535 + deterioros 156)»). Deuda bruta 19.261 (C54, Q2-26 PDF p. 23) − caja 3.196 (C53, "
                     "Q2-26 p. 13) = 16.065. EBITDA LTM a 28-jun-2026: resultado operativo 3.542 (L7, FY2025) + 1.760 − 1.741 (Q2-26 p. 11) = 3.561; D&A y "
                     "deterioros 3.733 (L8, flujos FY2025) + 1.828 − 1.870 (Q2-26 p. 15) = 3.691 (= 3.535 + 156 de la etapa 1: misma suma, otro desglose); "
                     "EBITDA 7.252. 16.065 ÷ 7.252 = 2,215250… → round(…, 4) = 2,2153 = libro. Mistral daba 2,2152 con otro desglose."),
    "unidad": None},
    comprobacion=comp(f"{ET1} (Control maestro fila 36); {Q2} [PDF PAGE 11, 13, 15, 23]", "Derivado exacto; la definición (deuda bruta con arrendamientos − "
                      "caja y equivalentes; EBITDA NIIF 16 con deterioros, LTM) es la de la etapa 1, no la «net debt» de la empresa (15.961, que resta "
                      "también depósitos 15 y el fondo de bonos 89)."))

# C42 · EV / EBITDA
nuevas.append(aux_pub("aux:Q2-2026_p13_investments_jv_hy2026", "aux_ev", Q2, 13, 13, "balance consolidado (interim)",
                      "Investments in joint ventures and associates, columna June 28, 2026", "June 28, 2026", "a 28-jun-2026 (cierre del primer semestre 2026)",
                      244, linea(Q2, 13, "Investments in joint ventures and associates"), "Resta del EV de la etapa 1 («− negocios conjuntos 244»)."))
nuevas.append(nueva("aux:etapa1_capitalizacion_oct2026", "aux_ev", "convencion", 28626, ambito=None,
                    hipotesis={"identificacion": "V-capitalizacion_etapa1 (Análisis!C41 de etapa1/Ahold_evaluada.xlsx)",
                               "fundamento": ("Capitalización que usó la etapa 1 de la persona para el EV de C42: etapa1/Ahold_evaluada.xlsx, hoja Análisis, celda C41 = "
                                              "28626 (con C37 = 33,14 €, precio de oct-2026) y Control maestro fila 42, M: «EV = 28.626 + deuda neta 16.065 … − negocios "
                                              "conjuntos 244 = 44.447 ÷ EBITDA IFRS 16 LTM 7.252 = 6,1x»; G: «EV: precio oct-2026 + deuda 28-jun-2026». 33,14 × 863,79 M "
                                              "acciones en circulación = 28.626,0 (las 863,79 M son el denominador que la etapa 1 usa en C96). Ni el precio 33,14 "
                                              "(fase1_v63.json → precio.fuente: «33,14 (cierre 2026-10-23, DeBelegger)», web de terceros) ni las 863,79 M están en una "
                                              "fuente conservada del expediente."),
                               "alternativas": ("Capitalización vigente del libro: Análisis!C41 = 32.625,25 (36,05 € del 13-nov-2026 × 905 M diluidas), con la que la "
                                                "misma fórmula da (32.625,25 + 19.261 − 3.196 − 244) ÷ 7.252 = 6,680; o 36,05 × acciones en circulación del Q2-26."),
                               "limites": ("No es un dato publicado: es la entrada de la etapa 1 tal como la dejó la persona; desfasada frente al precio vigente del "
                                           "libro (C37). Su cambio movería C42."),
                               "procedencia": "etapa1/Ahold_evaluada.xlsx → Análisis!C41 y Control maestro fila 42"},
                    comprobacion=comp(f"{ET1} (Análisis!C41, C37, C42; Control maestro fila 42)", "Entrada de la etapa 1 sin fuente conservada; se aísla como "
                                      "convención para que la derivación de C42 sea exacta y el hueco quede a la vista.")))
set_entrada("Análisis!C42", clase="derivado", derivacion={
    "origenes": ["aux:etapa1_capitalizacion_oct2026", "Análisis!C54", "Análisis!C53", "aux:Q2-2026_p13_investments_jv_hy2026"] + O_EBITDA,
    "formula": ('round((o["aux:etapa1_capitalizacion_oct2026"] + o["Análisis!C54"] - o["Análisis!C53"] - o["aux:Q2-2026_p13_investments_jv_hy2026"]) / '
                + EBITDA + ', 3)'),
    "conciliacion": ("Cálculo de la etapa 1 (Control maestro fila 42, M): EV = 28.626 (capitalización de la etapa 1, convención) + deuda neta 16.065 (= C54 19.261 − "
                     "C53 3.196, la de C33) + híbridos 0 + minoritarios 0 − negocios conjuntos 244 (Q2-26 p. 13) = 44.447; ÷ EBITDA LTM 7.252 (el de C33) = "
                     "6,128929… → round(…, 3) = 6,129 = libro. Con la capitalización vigente del libro (C41 = 32.625,25) saldría 6,680."),
    "unidad": None},
    justificacion_clase=("Análisis!C42 es un dato del modelo (juicio_C42) que se deriva de una convención: la capitalización de la etapa 1 (28.626, precio 33,14 € "
                         "de oct-2026 × 863,79 M acciones) no tiene fuente conservada en el expediente. El resto de orígenes son datos publicados. Se declara así "
                         "(N2) en lugar de forzar una cita o de cambiar el valor del libro."),
    incidencia=("C42 está desfasado frente a C37/C41 del libro (36,05 € × 905 M): con ellos, la misma definición da 6,680. No se cambia el libro; lo decide la "
                "persona responsable o la fase que lo use."),
    comprobacion=comp(f"{ET1} (Control maestro fila 42); {Q2} [PDF PAGE 11, 13, 15, 23]", "Derivado exacto con un origen convencional (capitalización de la "
                      "etapa 1)."))

# C60 · CAGR de acciones diluidas (raíz enésima: no expresable)
set_entrada("Análisis!C60", clase="convencion", hipotesis={
    "identificacion": "V-juicio_C60 (valor de la etapa 1)",
    "fundamento": ("etapa1/Ahold_evaluada.xlsx, hoja Análisis, celda C60 = -0.033; Control maestro fila 55: " + "{E55}" + ". Comprobación fuera del registro con "
                   "las acciones diluidas medias de la Historia (F20:L20, datos publicados de las notas de BPA): (905 ÷ 1.001)^(1/3) − 1 = −3,305 % "
                   "(2022→2025) y (905 ÷ 1.072)^(1/5) − 1 = −3,330 % (2020→2025); los dos redondean a −0,033."),
    "alternativas": "CAGR de 3 años (−0,03305), de 5 años (−0,03330) o con el Q2-26 como punto final (−3,25 % a −3,30 %, Control maestro fila 55, N).",
    "limites": ("Redondeo a 3 decimales de la etapa 1; la elección entre 3 y 5 años no cambia el valor redondeado. No es un dato publicado."),
    "procedencia": "etapa1/Ahold_evaluada.xlsx → Análisis!C60 y Control maestro fila 55"},
    justificacion_clase=("Dato del modelo (juicio_C60) calculado por la etapa 1 de la persona: un CAGR exige una raíz enésima, que el contrato de las fórmulas "
                         "(+ − × ÷, round, min, max, abs, sum; sin potencias) no admite, y ninguna fuente publica −0,033. No se puede registrar como derivado ni "
                         "como dato publicado; se declara como convención con su cálculo reproducible."),
    comprobacion=comp(f"{ET1} (Análisis!C60; Control maestro fila 55) e Historia F20:L20", "Valor de la etapa 1; reproducido a mano, no por la máquina."))

# C88 · mediana P/FCF 2019–2025 (red de ordenación de 7 entradas)
MCAP = {2025: 30659, 2024: 28668, 2023: 24615, 2022: 26232, 2021: 30482, 2020: 24197, 2019: 24751}
COLM = {2025: "December 28, 2025", 2024: "December 29, 2024", 2023: "December 31, 2023", 2022: "January 1, 2023", 2021: "January 2, 2022",
        2020: "January 3, 2021", 2019: "December 29, 2019"}
POS = {2025: "1.ª", 2024: "2.ª", 2023: "3.ª", 2022: "4.ª", 2021: "5.ª", 2020: "6.ª", 2019: "7.ª"}
cita_m = linea(AR[2025], 65, "Market capitalization")
HC = {2019: "F", 2020: "G", 2021: "H", 2022: "I", 2023: "J", 2024: "K", 2025: "L"}
from fractions import Fraction as Fr  # noqa: E402
import openpyxl  # noqa: E402
wv = openpyxl.load_workbook(os.path.join(W, "Ahold_v63_evaluada.xlsx"), data_only=True)["Historia"]
pf_keys = []
mil = lambda n: f"{int(n):,}".replace(",", ".")
dec = lambda x, d: f"{x:.{d}f}".replace(".", ",")
for y in range(2019, 2026):
    km = f"aux:AD_annual-report-2025_p65_market_capitalization_{y}"
    nuevas.append(aux_pub(km, "aux_pfcf", AR[2025], 65, 64, "resumen plurianual («Multiple-year overview continued»), «Balance sheet and other information»",
                          f"Market capitalization (€ million) al cierre del ejercicio {y}", f"columna «{COLM[y]}» ({POS[y]} columna de importes; cierre del ejercicio {y})",
                          f"al cierre del ejercicio {y} ({CIERRE[y]})", MCAP[y], cita_m, f"Capitalización de cierre {y} para el P/FCF de C88.",
                          reexpresado="no aplica (capitalización bursátil, no se reexpresa)"))
    c = HC[y]
    org = [km, f"Historia!{c}11", f"Historia!{c}12", f"Historia!{c}16", f"Historia!{c}17"]
    v = {x: wv[x.split("!")[1]].value for x in org[1:]}
    val = Fr(MCAP[y]) / (Fr(v[org[1]]) - Fr(v[org[2]]) - Fr(v[org[3]]) - Fr(v[org[4]]))
    kp = f"aux:pfcf_{y}"
    pf_keys.append(kp)
    nuevas.append(nueva(kp, "aux_pfcf", "derivado", float(val), ambito=None, derivacion={
        "origenes": org,
        "formula": f'o["{km}"] / (o["Historia!{c}11"] - o["Historia!{c}12"] - o["Historia!{c}16"] - o["Historia!{c}17"])',
        "conciliacion": (f"P/FCF {y} con la definición de la fila 52 (antes de SBC): capitalización de cierre {mil(MCAP[y])} ÷ (CFO {mil(v[org[1]])} − capex {mil(v[org[2]])} − "
                         f"intereses en financiación {mil(v[org[3]])} − arrendamientos {mil(v[org[4]])}) = {dec(float(val), 4)}; la etapa 1 da {dec(round(float(val), 1), 1)} "
                         f"(Control maestro fila 73, M)."),
        "unidad": None},
        comprobacion=comp(f"{AR[2025]} [PDF PAGE 65] e Historia {c}11:{c}17", "Componente de la mediana de C88.")))
NET = [(0, 6), (2, 3), (4, 5), (0, 2), (1, 4), (3, 6), (0, 1), (2, 5), (3, 4), (1, 2), (4, 6), (2, 3), (4, 5), (1, 2), (3, 4), (5, 6)]
w = [f'o["{k}"]' for k in pf_keys]
for a_, b_ in NET:
    w[a_], w[b_] = f"min({w[a_]}, {w[b_]})", f"max({w[a_]}, {w[b_]})"
set_entrada("Análisis!C88", clase="derivado", derivacion={
    "origenes": pf_keys,
    "formula": f"round({w[3]}, 1)",
    "conciliacion": ("Mediana de los P/FCF de cierre 2019–2025 de la etapa 1 (Control maestro fila 73, M: «Mediana P/FCF con la definición de la fila 52 (antes de "
                     "SBC): 14,7x (2019 16,4; 2020 12,4; 2021 21,9; 2022 15,5; 2023 12,4; 2024 14,7; 2025 13,8)»). Los siete P/FCF (aux:pfcf_2019…2025) "
                     "reproducen esos siete valores redondeados. La fórmula es la salida central (4.ª de 7) de una red de ordenación de siete entradas "
                     "(16 comparadores min/max, verificada con las 128 entradas 0/1), es decir, la mediana: la de 2024, 28.668 ÷ 1.952 = 14,6865 → "
                     "round(…, 1) = 14,7 = libro."),
    "unidad": None},
    comprobacion=comp(f"{ET1} (Control maestro fila 73); {AR[2025]} [PDF PAGE 65]; Historia F11:L17", "Derivado exacto: mediana expresada con min/max "
                      "(el contrato no tiene función mediana)."))

# C96 · % de insiders (registro AFM y acciones en circulación sin fuente conservada)
set_entrada("Análisis!C96", clase="convencion", hipotesis={
    "identificacion": "V-juicio_C96 (valor de la etapa 1)",
    "fundamento": ("etapa1/Ahold_evaluada.xlsx, hoja Análisis, celda C96 = 0.0007; Control maestro fila 75: " + "{E75}" + ". 613.101 ÷ 863,79 M = 0,000710 → "
                   "0,0007. Las tenencias proceden del registro de la AFM (Wft 5:48, consulta de oct-2026) y el denominador de 863,79 M acciones en "
                   "circulación no figura en ningún texto conservado del expediente."),
    "alternativas": ("Con el informe anual 2025 (AR25 p. 180 según la etapa 1): 566.744 acciones a 28-dic-2025 = 0,064 % (0,0006 con 4 decimales), que no es el "
                     "valor del libro."),
    "limites": ("Cifra mínima (no incluye al ExCo fuera del Management Board ni a los nombrados el 13-oct-2026, según la etapa 1). No es un dato publicado: "
                "suma de notificaciones individuales de un registro externo no conservado."),
    "procedencia": "etapa1/Ahold_evaluada.xlsx → Análisis!C96 y Control maestro fila 75"},
    justificacion_clase=("Dato del modelo (juicio_C96) de la etapa 1 de la persona sin derivación posible con fuentes conservadas: el registro de la AFM y el número "
                         "de acciones en circulación (863,79 M) no están en el expediente, y la fuente conservada (AR2025) da 0,0006. No se fuerza una cita."),
    comprobacion=comp(f"{ET1} (Análisis!C96; Control maestro fila 75)", "Valor de la etapa 1; no reproducible desde las fuentes del expediente."))

# completar los textos de la etapa 1 en los fundamentos
for k, fila in (("Análisis!C60", 55), ("Análisis!C96", 75)):
    h = por[k]["hipotesis"]
    h["fundamento"] = h["fundamento"].replace("{E%d}" % fila, et1(fila))

# ------------------------------------------------------------------------------------------------ escribir
for e in nuevas:
    assert e["celda"] not in por, e["celda"]
    por[e["celda"]] = e
reg["entradas"] = list(reg["entradas"]) + nuevas
for e in reg["entradas"]:
    c = e.get("comprobacion") or {}
    c.pop("vinculo", None)
reg["extractor_complementario"] = EXT
reg["fecha_extraccion_complementaria"] = HOY
reg["nota_del_extractor_complementario"] = (
    f"Completado el {HOY} por {EXT} sobre el registro de Mistral (ronda 1, commit 9a06d4a): 21 celdas F1 nuevas (Historia C85:L87), fundamento, alternativas y "
    "límites de las 30 hipótesis (texto de las fases en el Control maestro del libro), y Análisis C26, C33, C42, C60, C88 y C96. Todas las comprobaciones quedan "
    "«pendiente», sin revisor ni vínculo. Ver NOTAS_EXTRACTOR_COMPLEMENTARIO.md.")
json.dump(reg, open(REG, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("entradas", len(reg["entradas"]), "nuevas", len(nuevas)); print("valor_modelo de hipótesis actualizados:", *CAMBIOS_VM, sep="\n  ")
