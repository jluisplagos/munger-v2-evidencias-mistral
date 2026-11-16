"""Genera VIDRALA_REPOSICION_CAPACIDAD.csv desde los textos conservados de Vidrala (base 4.14).

Correccion B1 (revision externa 2026-11-16, commit 9366bdd...): las altas de PP&E se toman de
la nota "Property, Plant and Equipment" (fila total de Coste, columna Additions); los valores
antes presentados como PP&E (156.743 ... 45.173) procedian de la nota "Intangible Assets".
PP&E, intangibles (con derechos de emision y goodwill), combinaciones de negocio, ROU y pagos
de caja van en columnas separadas. Cada operando exige contexto: encabezado de nota + columna
Additions + etiqueta de anio + fila exacta, y se contrasta con el comparativo del ejercicio
siguiente. Control negativo: reproduce el error antiguo (intangibles tomados como PP&E) y
verifica que el extractor lo rechaza al faltar el encabezado de la nota PP&E.

No se distingue reposicion de capacidad anadida salvo donde la fuente lo permite; los huecos
se declaran (no se interpola). No se fuerza igualdad entre adiciones, pagos de caja y
mantenimiento economico.
"""
import csv
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
TXT = RAIZ / ".trabajo/insumos_m2/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/vidrala_decisiones/Vidrala/texto"
SALIDA = RAIZ / "resultados_m2/pm1"
T = {y: TXT / f"CF_{y}.txt" for y in range(2017, 2026)}
ES24 = TXT / "ES_2024_informacion_financiera_consolidada.txt"
ES25 = TXT / "ES_2025_informacion_financiera_consolidada.txt"

_cache = {}


def ventana(ruta, lo, hi):
    key = (str(ruta), lo, hi)
    if key not in _cache:
        lineas = ruta.read_text(encoding="utf-8").splitlines()
        _cache[key] = "\n".join(lineas[lo - 1:hi])
    return _cache[key]


def pagina_de(ruta, linea):
    lineas = ruta.read_text(encoding="utf-8").splitlines()
    pagina = "?"
    for i, ln in enumerate(lineas[:linea], 1):
        m = re.match(r"\[PDF PAGE (\d+)\]", ln)
        if m:
            pagina = m.group(1)
    return pagina


def citar(ruta, lo, hi, patron, uso):
    texto = ventana(ruta, lo, hi)
    patron = patron.replace(" ", r"\s+")
    m = re.search(patron, texto, re.IGNORECASE | re.DOTALL)
    if not m:
        raise AssertionError(f"cita no verificada ({uso}): /{patron}/ no esta en {ruta.name} l{lo}-{hi}")
    return {"archivo": str(ruta.relative_to(RAIZ)), "lineas": f"{lo}-{hi}", "pagina_pdf": pagina_de(ruta, hi),
            "cita": " ".join(m.group(0).split())[:400]}


def f(fuente):
    return f'{fuente["archivo"].split("/")[-1]} p{fuente["pagina_pdf"]} l{fuente["lineas"]}'


NOTA_PPE = r"\d+\.\s*Property,\s*Plant\s*and\s*Equipment"
NOTA_INT = r"\d+\.\s*Intangible\s*Assets"


def extraer_fila_nota(ruta, lo, hi, patron_nota, anio, patron_fila, uso):
    """Exige contexto de nota + columna Additions + etiqueta de anio; devuelve tokens de la fila."""
    texto = ventana(ruta, lo, hi)
    if not re.search(patron_nota, texto, re.IGNORECASE | re.DOTALL):
        raise AssertionError(f"falta el encabezado de la nota en la ventana ({uso}): {ruta.name} l{lo}-{hi}")
    if not re.search(r"Additions", texto, re.IGNORECASE):
        raise AssertionError(f"falta la columna Additions en la ventana ({uso}): {ruta.name} l{lo}-{hi}")
    if anio is not None and not re.search(rf"(?m)^\s*{anio}\b", texto):
        raise AssertionError(f"falta la etiqueta de anio {anio} en la ventana ({uso}): {ruta.name} l{lo}-{hi}")
    p = patron_fila.replace(" ", r"\s+")
    m = re.search(p, texto, re.IGNORECASE | re.DOTALL)
    if not m:
        raise AssertionError(f"fila no verificada ({uso}): /{patron_fila}/ no esta en {ruta.name} l{lo}-{hi}")
    fila = " ".join(m.group(0).split())
    return fila.split(), {"archivo": str(ruta.relative_to(RAIZ)), "lineas": f"{lo}-{hi}",
                          "pagina_pdf": pagina_de(ruta, hi), "cita": fila[:400]}


# Nota Property, Plant and Equipment: ventana desde el encabezado de la nota hasta la fila total
# de Coste (columna 2 = Additions; columna 3 numerica = combinacion de negocios, solo en anos
# con adquisiciones y encabezado "Business combination"/"Combination (Note 5)").
# anio: (linea_nota, linea_total, regex_fila_total, adiciones_esperadas)
PPE = {
    2017: (1829, 1848, r"1,174,690 101,154 76,170 \(31,554\) \(13,948\) 2 1,306,514", "101154"),
    2018: (1834, 1854, r"1,306,514 93,148 - \(56,411\) \(3,360\) - 1,339,891", "93148"),
    2019: (1782, 1802, r"1,339,891 108,645 \(126,479\) - 22,290 1,344,347", "108645"),
    2020: (2475, 2494, r"1,344,347 134,263 \(6,140\) - \(30,121\) 1,442,349", "134263"),
    2021: (2248, 2268, r"1,442,349 105,877 \(11,776\) 683 39,823 1,576\.956", "105877"),
    2022: (2335, 2355, r"1,576,956 158,234 \(8,296\) - \(26,551\) 1,700,343", "158234"),
    2023: (2272, 2294, r"1,700,343 134,472 262,679 \(11,221\) - 16,173 2,102,446", "134472"),
    2024: (2473, 2495, r"2,131,588 171,185 \(24,630\) \(177,353\) - \(12,526\) 2,088,264", "171185"),
    2025: (2404, 2426, r"2,088,264 177,848 \(36,070\) - 285 \(35,814\) 2,194,513", "177848"),
}

# Nota Intangible Assets: fila "Additions" con columnas R&D / Emission allowances / software /
# otras / goodwill / Total. anio: (linea_nota, linea_additions, regex_fila)
INT = {
    2017: (1942, 1952, r"Additions 21 3,237 2,822 - 6 - 150,657 156,743"),
    2018: (1954, 1964, r"Additions 126 14,645 3,841 - 11 - - 18,623"),
    2019: (1896, 1906, r"Additions 189 22,147 3,348 - 10 - - 25,694"),
    2020: (2596, 2608, r"Additions 316 26,558 1,792 - - - 28,666"),
    2021: (2374, 2394, r"Additions 724 37,359 5,900 827 - - 44,810"),
    2022: (2475, 2493, r"Additions 167 90,780 2,781 31 - - 93,759"),
    2023: (2403, 2418, r"Additions 677 93,306 6,528 144 - - 100,655"),
    2024: (2611, 2626, r"Additions 316 40,135 7,853 22 - - 48,326"),
    2025: (2565, 2580, r"Additions 433 37,661 6,830 249 - - 45,173"),
}

# Comparativos de adiciones PP&E publicados en el CF del ejercicio siguiente (mismo encabezado
# de nota); la columna 2 debe coincidir con las adiciones del ano propio.
# anio_propio: (anio_CF_siguiente, linea_nota, linea_total_comparativo, regex_fila)
COMP = {
    2017: (2018, 1834, 1891, r"1,174,690 101,154 \(31,554\) \(13,948\) 2 1,306,514"),
    2018: (2019, 1782, 1840, r"1,306,514 93,148 \(56,411\) \(3,360\) - 1,339,891"),
    2019: (2020, 2475, 2533, r"1,339,891 108,645 \(126,479\) - 22,290 1,344,347"),
    2020: (2021, 2248, 2310, r"1,344,347 134,263 \(6,140\) - \(30,121\) 1,442,349"),
    2021: (2022, 2335, 2400, r"1,442,349 105,877 \(11,776\) 683 39,822 1,576\.956"),
    2022: (2023, 2272, 2334, r"1,576,956 158,234 \(8,296\) - \(26,551\) 1,700,343"),
    2023: (2024, 2473, 2536, r"1,700,343 134,472 291,821 \(11,221\) - 16,173 2,131,588"),
    2024: (2025, 2404, 2476, r"2,131,588 171,185 \(24,630\) \(177,353\) - \(12,526\) 2,088,264"),
}

# Discrepancias comparativas 2023 registradas sin resolver (no se fuerza igualdad):
PPE_2023_CF2024 = citar(T[2024], 2473, 2536,
                        r"1,700,343 134,472 291,821 \(11,221\) - 16,173 2,131,588",
                        "comparativo 2023 en la nota PP&E de CF_2024: adiciones 134.472 (igual que CF_2023) pero combinacion de negocios reexpresada 291.821 vs 262.679 y cierre de coste 2.131.588 vs 2.102.446")
INT_2023_CF2024 = citar(T[2024], 2611, 2672,
                        r"Additions 677 93,306 6\.498 144 - 2,170 102,795",
                        "comparativo 2023 en la nota de intangibles de CF_2024: adiciones 102.795 (goodwill 2.170) frente a 100.655 en CF_2023")

# pagos de inmovilizado (EFE), miles eur: (ppe, intangibles, cita)
CAPEX_CASH = {
    2017: (86479, None, citar(T[2018], 305, 306, r"Proceeds from sale of property, plant and equipment \(99,541\) -.*Acquisition of property, plant and equipment \(2,245\) \(86,479\)", "pagos PP&E 2018/2017 (col 2017)")),
    2018: (99541, 2245, citar(T[2018], 305, 307, r"\(99,541\).*\(2,245\).*\(2,541\)", "pagos inmovilizado 2018")),
    2019: (103622, 3547, citar(T[2020], 311, 312, r"Proceeds from sale of property, plant and equipment \(132,117\) \(103,622\).*Acquisition of property, plant and equipment \(2,131\) \(3,547\)", "pagos inmovilizado 2020/2019 (col 2019)")),
    2020: (132117, 2131, citar(T[2020], 311, 312, r"\(132,117\).*\(2,131\)", "pagos inmovilizado 2020")),
    2021: (107604, 2196, citar(T[2022], 305, 306, r"Payments from sale of property, plant and equipment \(117,296\) \(107\.604\).*Payments from sale of other intangible assets \(2,904\) \(2,196\)", "pagos inmovilizado 2022/2021 (col 2021)")),
    2022: (117296, 2904, citar(T[2022], 305, 306, r"\(117,296\).*\(2,904\)", "pagos inmovilizado 2022")),
    2023: (143848, 7852, citar(ES24, 305, 306, r"Pagos por la adquisici.n de inmovilizado material \(160\.063\) \(143\.848\).*Pagos por la adquisici.n de activos intangibles \(8\.737\) \(7\.852\)", "pagos inmovilizado 2024/2023 (col 2023)")),
    2024: (160063, 8737, citar(ES24, 305, 306, r"\(160\.063\).*\(8\.737\)", "pagos inmovilizado 2024")),
    2025: (178746, 9757, citar(ES25, 288, 289, r"Pagos por la adquisici.n de inmovilizado material \(178\.746\).*Pagos por la adquisici.n de activos intangibles \(9\.757\)", "pagos inmovilizado 2025")),
}

# ROU: altas activo / altas pasivo / amortizacion, miles eur
ROU_ACTIVO = {
    2022: (2165, citar(T[2023], 2703, 2703, r"Additions\s+2,165\s+\(633\)\s+1,532", "altas ROU activo 2022")),
    2023: (645, citar(T[2023], 2712, 2712, r"Additions\s+645\s+\(4,624\)\s+\(3,979\)", "altas ROU activo 2023 (sin combinaciones de negocio)")),
    2024: (1485, citar(T[2025], 2879, 2879, r"Additions\s+1,485\s+\(4,768\)\s+\(3,283\)", "altas ROU activo 2024")),
    2025: (2404, citar(T[2025], 2885, 2885, r"Additions\s+2,404\s+\(1,415\)\s+989", "altas ROU activo 2025")),
}
ROU_PASIVO = {
    2022: (2133, citar(T[2023], 2732, 2732, r"Additions\s+643\s+2,133", "altas pasivo arrendamiento 2023/2022 (col 2022)")),
    2023: (643, citar(T[2023], 2732, 2732, r"Additions\s+643\s+2,133", "altas pasivo arrendamiento 2023")),
    2024: (1429, citar(T[2025], 2914, 2914, r"Additions\s+2,404\s+1,429", "altas pasivo arrendamiento 2025/2024 (col 2024)")),
    2025: (2404, citar(T[2025], 2914, 2914, r"Additions\s+2,404\s+1,429", "altas pasivo arrendamiento 2025")),
}
ROU_COMB_NEGOCIO = {
    2023: (46123, citar(T[2023], 2709, 2710, r"Additions due to business\s+46,123.*combinations \(Note 5\)", "altas ROU por combinacion de negocios 2023 ('The Park', Bristol)")),
}
ROU_AMORT = {
    2022: (633, citar(T[2023], 2751, 2751, r"Depreciation of right-of-use assets\s+4,624\s+633", "amort ROU 2023/2022")),
    2023: (4624, citar(T[2023], 2751, 2751, r"Depreciation of right-of-use assets\s+4,624", "amort ROU 2023")),
    2024: (4768, citar(T[2025], 2934, 2934, r"Depreciation of right-of-use assets\s+6,760\s+4,768", "amort ROU 2025/2024")),
    2025: (6760, citar(T[2025], 2934, 2934, r"Depreciation of right-of-use assets\s+6,760", "amort ROU 2025")),
}
ROU_2021 = citar(T[2023], 2701, 2701, r"At 31 December 2021\s+770\s+-\s+770", "saldo ROU 2021 (770); sin tabla de movimientos publicada por separado en 2021")
ROU_OTROS_2025 = citar(T[2025], 2887, 2895, r"Others\s+9,595\s+\(5,345\)\s+4,250.*price update applied to the lease\s*instalment for the .?The Park", "otros ROU activo 2025 (9.595 por actualizacion de precio del arrendamiento 'The Park')")

# vida util y renovacion de hornos
VIDA_UTIL = citar(T[2025], 685, 685, r"Furnaces, installations, and production machinery\s+8 - 16", "vida util hornos 8-16 anos (presente en CF_2017..CF_2025)")
VIDA_UTIL_ES = citar(ES25, 651, 651, r"Hornos, instalaciones y maquinaria de producci.n\s+8 - 16", "vida util hornos 8-16 (ES 2025)")
HORNOS_2024 = citar(T[2024], 2560, 2562, r"Main additions for the fiscal year 2024 correspond to the investments made, primarily in\s*the renewal of furnaces.*Spain, Portugal, and the\s*United Kingdom", "renovacion de hornos 2024 (nota PP&E)")
HORNOS_2025 = citar(T[2025], 2499, 2501, r"The main additions in 2025 and the prior year correspond to the investments made\s*primarily in the renewal of furnaces.*Spain, Portugal\s*and the United Kingdom", "renovacion de hornos 2025 (nota PP&E)")
HORNOS_ES2024 = citar(ES24, 9521, 9522, r"reconstrucci.n de varios hornos en el Grupo, ya que estas operaciones generan cantidades significativas de\s*residuos", "reconstruccion de varios hornos 2024 (memoria no financiera ES 2024)")
HORNOS_PERTE = citar(ES25, 3753, 3757, r"descarbonizaci.n de los hornos de las mencionadas plantas por importes de 10\.298 y 6\.316 miles de\s*euros", "subvenciones PERTE para descarbonizacion de hornos (Crisnova 10.298kEUR y Castellar 6.316kEUR, a invertir desde 2026)")
HORNO_FUTURO = citar(ES25, 6044, 6048, r"En 2025 la gesti.n de los hornos se ha focalizado en eficiencia, capacidad de electrificaci.n y estabilidad\s*operativa.*inversiones en tres frentes", "'Horno del futuro' 2025: inversiones en infraestructura electrica, recuperacion de calor y digital (ES 2025)")

# narrativas de adiciones por pais (nota PP&E)
NARR = {
    2018: citar(T[2018], 1911, 1914, r"Main additions for 2018 correspond to the investment plans for the complete update of\s*the production plants located in Italy \(Euros 27,958 thousand\) and the United\s*Kingdom \(Euros 33,733 thousand\), as well as.*Castellar Vidrio \(Euros 16,329 thousand\)", "adiciones 2018: update plantas Italia/UK + Castellar"),
    2019: citar(T[2019], 1861, 1863, r"Main additions for 2019 correspond to the investment plans for the complete update of\s*the production plants located in Portugal \(Euros 20,250 thousand\) and the United\s*Kingdom \(Euros 44,247 thousand\)", "adiciones 2019: Portugal/UK"),
    2020: citar(T[2020], 2549, 2552, r"Main additions for 2020 and 2019 correspond to the investment plans for the complete\s*update of the production plants located in the United Kingdom \(Euros 77,801 thousand\s*and Euros 44,247 thousand respectively\) and Portugal \(Euros 29,031 thousand and\s*Euros 20,250 thousand respectively\)", "adiciones 2020/2019: UK/Portugal"),
    2021: citar(T[2021], 2328, 2331, r"Main additions for 2021 and 2020.*United Kingdom \(Euros 32,597 thousand\s*and Euros 77,801 thousand respectively\) and Portugal \(Euros 39,792 thousand and\s*Euros 29,031 thousand respectively\)", "adiciones 2021/2020: UK/Portugal"),
    2022: citar(T[2022], 2418, 2421, r"Main additions for 2022 and 2021.*United Kingdom \(Euros 23,479 thousand\s*and Euros 32,597 thousand respectively\) and Portugal \(Euros 94,557 thousand and\s*Euros 39,792 thousand respectively\)", "adiciones 2022/2021: UK/Portugal"),
    2023: citar(T[2023], 2355, 2359, r"The main additions in 2023 correspond to the investments made by the Group in its\s*subsidiaries in Portugal.*business combinations \(Note 5\).*2022.*modernization of the production plants located in the\s*United Kingdom and Portugal", "adiciones 2023: Portugal + combinaciones de negocio; 2022: modernizacion UK/Portugal"),
}
SALE_LEASEBACK = citar(T[2023], 2363, 2365, r"During the financial year 2022, the Group formalized various .?Sale & Leaseback. leasing\s*contracts.*fixed assets affecting their\s*production plants in Spain. During 2023, no new contracts", "sale & leaseback 2022 sobre plantas de Espana")
RECURRING_CAPEX = citar(T[2019], 2082, 2082, r"recurring capex captured in the valuation models", "prueba de deterioro: 'recurring capex captured in the valuation models' (sin cifra; CF_2019..CF_2023)")


def extraer_ppe(anio):
    lo, hi, fila, esperado = PPE[anio]
    tokens, cit = extraer_fila_nota(T[anio], lo, hi, NOTA_PPE, anio, fila, f"adiciones PP&E {anio} (nota PP&E, fila total de Coste, col Additions)")
    if tokens[1].replace(",", "") != esperado:
        raise AssertionError(f"adiciones PP&E {anio}: esperado {esperado}, obtenido {tokens[1]} ({T[anio].name} l{lo}-{hi})")
    bc = ""
    if len(tokens) > 2 and re.fullmatch(r"[\d,]+", tokens[2]) and re.search(r"ombination", ventana(T[anio], lo, hi), re.IGNORECASE):
        bc = tokens[2].replace(",", "")
    return int(esperado), bc, cit


def extraer_intangibles(anio):
    lo, hi, fila = INT[anio]
    tokens, cit = extraer_fila_nota(T[anio], lo, hi, NOTA_INT, anio, fila, f"adiciones intangibles {anio} (nota Intangible Assets, col Additions)")
    texto = ventana(T[anio], lo, hi)
    if not (re.search(r"Emission", texto, re.IGNORECASE) and re.search(r"allowances", texto, re.IGNORECASE)):
        raise AssertionError(f"falta la columna Emission allowances en la nota de intangibles {anio}")
    if not re.search(r"Goodwill", texto, re.IGNORECASE):
        raise AssertionError(f"falta la columna Goodwill en la nota de intangibles {anio}")
    datos = tokens[1:]  # tras la etiqueta "Additions"
    emision = datos[1].replace(",", "")
    goodwill = datos[-2].replace(",", "") if datos[-2] != "-" else "0"
    total = int(datos[-1].replace(",", ""))
    return total, emision, goodwill, cit


def comprobar_comparativos():
    """Las adiciones PP&E de cada ano deben coincidir con el comparativo del CF del ano siguiente."""
    for anio, (y_sig, lo, hi, fila) in COMP.items():
        tokens, _ = extraer_fila_nota(T[y_sig], lo, hi, NOTA_PPE, anio, fila, f"comparativo {anio} en CF_{y_sig} (nota PP&E)")
        esperado = PPE[anio][3]
        if tokens[1].replace(",", "") != esperado:
            raise AssertionError(f"comparativo {anio} en CF_{y_sig}: adiciones {tokens[1]} != {esperado} del ano propio")


def control_negativo():
    """Reproduce el error B1: la fila 'Additions ... <total>' usada antes como PP&E vive en la
    nota Intangible Assets; el extractor de PP&E debe rechazar esa ventana (sin encabezado PP&E)."""
    for anio, (lo, hi, fila) in INT.items():
        ruta = T[anio]
        texto = ventana(ruta, lo, hi)
        assert re.search(NOTA_INT, texto, re.IGNORECASE | re.DOTALL), f"control negativo: {ruta.name} l{lo}-{hi} no es la nota de intangibles"
        assert not re.search(NOTA_PPE, texto, re.IGNORECASE | re.DOTALL), f"control negativo: ventana inesperada con nota PP&E en {ruta.name} l{lo}-{hi}"
        try:
            extraer_fila_nota(ruta, lo, hi, NOTA_PPE, anio, fila, f"control negativo {anio}")
        except AssertionError:
            continue
        raise SystemExit(f"CONTROL NEGATIVO FALLIDO: el extractor de PP&E acepto la nota de intangibles de {anio} (valor antiguo mal clasificado como PP&E)")
    return True


def main():
    comprobar_comparativos()
    assert control_negativo(), "control negativo no superado"
    ppe_rows = {a: extraer_ppe(a) for a in range(2017, 2026)}
    int_rows = {a: extraer_intangibles(a) for a in range(2017, 2026)}

    ruta = SALIDA / "VIDRALA_REPOSICION_CAPACIDAD.csv"
    with ruta.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["anio", "adiciones_ppe_bruto_miles_eur", "adiciones_ppe_comb_negocio_miles_eur", "ppe_fuente",
                    "adiciones_intangibles_bruto_miles_eur", "de_las_cuales_derechos_emision_miles_eur", "de_las_cuales_goodwill_miles_eur", "intangibles_fuente",
                    "pagos_ppe_efe_miles_eur", "pagos_intangibles_efe_miles_eur", "capex_fuente",
                    "altas_rou_activo_miles_eur", "rou_activo_fuente", "altas_rou_pasivo_miles_eur", "rou_pasivo_fuente",
                    "amort_rou_miles_eur", "amort_rou_fuente",
                    "vida_util_hornos", "renovacion_hornos", "adiciones_narrativa", "capacidad_anadida_publicada",
                    "otros", "notas"])
        for anio in range(2017, 2026):
            ppe, bc, ppe_c = ppe_rows[anio]
            itotal, emision, goodwill, i_cit = int_rows[anio]
            cc = CAPEX_CASH[anio]
            ra = ROU_ACTIVO.get(anio)
            rp = ROU_PASIVO.get(anio)
            am = ROU_AMORT.get(anio)
            narr = NARR.get(anio, {"cita": "", "lineas": "", "pagina_pdf": "", "archivo": ""})
            horno = ""
            if anio == 2024:
                horno = f'{HORNOS_2024["cita"][:160]} [{f(HORNOS_2024)}]; {HORNOS_ES2024["cita"][:120]} [ES_2024 p{PAG(HORNOS_ES2024)}]'
            if anio == 2025:
                horno = f'{HORNOS_2025["cita"][:160]} [{f(HORNOS_2025)}]; {HORNOS_PERTE["cita"][:140]} [ES_2025 p{PAG(HORNOS_PERTE)}]; {HORNO_FUTURO["cita"][:120]} [ES_2025 p{PAG(HORNO_FUTURO)}]'
            otros = ""
            if anio == 2023:
                otros = f'altas ROU por combinacion de negocios (The Park): {ROU_COMB_NEGOCIO[2023][0]} miles eur [{f(ROU_COMB_NEGOCIO[2023][1])}]'
            if anio == 2025:
                otros = (otros + "; " if otros else "") + f'otros ROU activo 9.595 (price update The Park) [{f(ROU_OTROS_2025)}]'
            if anio == 2022:
                otros = f'sale & leaseback sobre plantas de Espana [{f(SALE_LEASEBACK)}]'
            notas = []
            if anio == 2017:
                notas.append("Correccion B1: adiciones_ppe_bruto viene de la nota Property, Plant and Equipment; los valores antiguos de esta columna (156.743 etc.) eran de la nota Intangible Assets (ver columnas de intangibles); el control negativo del script reproduce y rechaza ese error")
            if anio == 2021:
                notas.append("ROU: saldo 770 a 31-dic-2021 sin tabla de movimientos publicada por separado [" + f(ROU_2021) + "]")
            if anio == 2023:
                notas.append("Comparativos 2023 en CF_2024 registrados sin resolver: nota PP&E adiciones 134.472 (igual) pero combinacion de negocios reexpresada 291.821 vs 262.679 y cierre de coste 2.131.588 vs 2.102.446 [" + f(PPE_2023_CF2024) + "]; nota de intangibles adiciones 102.795 (goodwill 2.170) frente a 100.655 en CF_2023 [" + f(INT_2023_CF2024) + "]. No se fuerza igualdad entre adiciones, pagos y mantenimiento economico")
            if anio in (2022, 2024):
                notas.append(f"altas ROU activo y pasivo no coinciden ({ra[0] if ra else '-'} frente a {rp[0] if rp else '-'}); no se suponen identicas")
            notas.append("vida util hornos 8-16 anos en todos los anos [" + f(VIDA_UTIL) + "]")
            w.writerow([
                anio, ppe, bc, f(ppe_c), itotal, emision, goodwill, f(i_cit),
                cc[0], cc[1] if cc[1] is not None else "", f(cc[2]),
                ra[0] if ra else "", f(ra[1]) if ra else "",
                rp[0] if rp else "", f(rp[1]) if rp else "",
                am[0] if am else "", f(am[1]) if am else "",
                "8 - 16 anos (nota de inmovilizado, todos los anos)", horno,
                narr["cita"][:300] if narr["cita"] else "",
                "NO PUBLICADA en los bytes conservados: Vidrala no desglosa capacidad anadida vs reposicion; la cita del CFO ('more than pure replacement') es de transcripcion de terceros sin bytes",
                otros, "; ".join(notas),
            ])
    print("escrito", ruta.relative_to(RAIZ))
    for a in range(2017, 2026):
        ppe, bc, _ = ppe_rows[a]
        itotal, emision, goodwill, _ = int_rows[a]
        print(a, "PPE", ppe, "BC", bc or "-", "| intangibles", itotal, "emision", emision, "goodwill", goodwill)
    print("control negativo superado: las filas antiguas de 'PP&E' viven en la nota Intangible Assets y el extractor las rechaza")
    print("recurring capex:", RECURRING_CAPEX["cita"][:120], "[" + f(RECURRING_CAPEX) + "]")


def PAG(c):
    return c["pagina_pdf"]


if __name__ == "__main__":
    main()
