"""Genera VIDRALA_REPOSICION_CAPACIDAD.csv desde los textos conservados de Vidrala (base 4.14).

Cada operando lleva cita (archivo, rango de lineas, patron) verificada antes de usarse.
No se distingue reposición de capacidad añadida salvo donde la fuente lo permite;
los huecos se declaran (no se interpola).
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
    return {"archivo": str(ruta.relative_to(RAIZ)), "lineas": f"{lo}-{hi}", "pagina_pdf": pagina_de(ruta, lo),
            "cita": " ".join(m.group(0).split())[:400]}


def f(fuente):
    return f'{fuente["archivo"].split("/")[-1]} p{fuente["pagina_pdf"]} l{fuente["lineas"]}'


# adiciones brutas de PP&E (nota de inmovilizado material, fila Additions, columna Total), miles eur
PPE_ADD = {
    2017: (156743, citar(T[2017], 1952, 1952, r"Additions 21 3,237 2,822 - 6 - 150,657 156,743", "adiciones PP&E 2017")),
    2018: (18623, citar(T[2018], 1964, 1964, r"Additions 126 14,645 3,841 - 11 - - 18,623", "adiciones PP&E 2018")),
    2019: (25694, citar(T[2019], 1906, 1906, r"Additions 189 22,147 3,348 - 10 - - 25,694", "adiciones PP&E 2019")),
    2020: (28666, citar(T[2020], 2608, 2608, r"Additions 316 26,558 1,792 - - - 28,666", "adiciones PP&E 2020")),
    2021: (44810, citar(T[2021], 2394, 2394, r"Additions 724 37,359 5,900 827 - - 44,810", "adiciones PP&E 2021")),
    2022: (93759, citar(T[2022], 2493, 2493, r"Additions 167 90,780 2,781 31 - - 93,759", "adiciones PP&E 2022")),
    2023: (100655, citar(T[2023], 2418, 2418, r"Additions 677 93,306 6,528 144 - - 100,655", "adiciones PP&E 2023")),
    2024: (48326, citar(T[2024], 2626, 2626, r"Additions 316 40,135 7,853 22 - - 48,326", "adiciones PP&E 2024")),
    2025: (45173, citar(T[2025], 2580, 2580, r"Additions 433 37,661 6,830 249 - - 45,173", "adiciones PP&E 2025")),
}
# discrepancy declarada: CF_2024 p51 l2672 presenta el comparativo 2023 con total 102,795 (columna extra 2,170)
PPE_2023_CF2024 = citar(T[2024], 2672, 2672, r"Additions 677 93,306 6\.498 144 - 2,170 102,795", "comparativo 2023 en CF_2024 (total 102,795; difiere del 100,655 de CF_2023)")

# pagos de inmovilizado (EFE), miles eur: (ppe, intangibles)
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

# ROU: altas activo / altas pasivo / amortización, miles eur
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
    2023: (46123, citar(T[2023], 2709, 2710, r"Additions due to business\s+46,123.*combinations \(Note 5\)", "altas ROU por combinación de negocios 2023 ('The Park', Bristol)")),
}
ROU_AMORT = {
    2022: (633, citar(T[2023], 2751, 2751, r"Depreciation of right-of-use assets\s+4,624\s+633", "amort ROU 2023/2022")),
    2023: (4624, citar(T[2023], 2751, 2751, r"Depreciation of right-of-use assets\s+4,624", "amort ROU 2023")),
    2024: (4768, citar(T[2025], 2934, 2934, r"Depreciation of right-of-use assets\s+6,760\s+4,768", "amort ROU 2025/2024")),
    2025: (6760, citar(T[2025], 2934, 2934, r"Depreciation of right-of-use assets\s+6,760", "amort ROU 2025")),
}
ROU_2021 = citar(T[2023], 2701, 2701, r"At 31 December 2021\s+770\s+-\s+770", "saldo ROU 2021 (770); sin tabla de movimientos publicada por separado en 2021")
ROU_OTROS_2025 = citar(T[2025], 2887, 2895, r"Others\s+9,595\s+\(5,345\)\s+4,250.*price update applied to the lease\s*instalment for the .?The Park", "otros ROU activo 2025 (9.595 por actualización de precio del arrendamiento 'The Park')")

# vida útil y renovación de hornos
VIDA_UTIL = citar(T[2025], 685, 685, r"Furnaces, installations, and production machinery\s+8 - 16", "vida útil hornos 8-16 años (presente en CF_2017..CF_2025)")
VIDA_UTIL_ES = citar(ES25, 651, 651, r"Hornos, instalaciones y maquinaria de producci.n\s+8 - 16", "vida útil hornos 8-16 (ES 2025)")
HORNOS_2024 = citar(T[2024], 2560, 2562, r"Main additions for the fiscal year 2024 correspond to the investments made, primarily in\s*the renewal of furnaces.*Spain, Portugal, and the\s*United Kingdom", "renovación de hornos 2024 (nota PP&E)")
HORNOS_2025 = citar(T[2025], 2499, 2501, r"The main additions in 2025 and the prior year correspond to the investments made\s*primarily in the renewal of furnaces.*Spain, Portugal\s*and the United Kingdom", "renovación de hornos 2025 (nota PP&E)")
HORNOS_ES2024 = citar(ES24, 9521, 9522, r"reconstrucci.n de varios hornos en el Grupo, ya que estas operaciones generan cantidades significativas de\s*residuos", "reconstrucción de varios hornos 2024 (memoria no financiera ES 2024)")
HORNOS_PERTE = citar(ES25, 3753, 3757, r"descarbonizaci.n de los hornos de las mencionadas plantas por importes de 10\.298 y 6\.316 miles de\s*euros", "subvenciones PERTE para descarbonización de hornos (Crisnova 10.298k€ y Castellar 6.316k€, a invertir desde 2026)")
HORNO_FUTURO = citar(ES25, 6044, 6048, r"En 2025 la gesti.n de los hornos se ha focalizado en eficiencia, capacidad de electrificaci.n y estabilidad\s*operativa.*inversiones en tres frentes", "'Horno del futuro' 2025: inversiones en infraestructura eléctrica, recuperación de calor y digital (ES 2025)")

# narrativas de adiciones por país (nota PP&E)
NARR = {
    2018: citar(T[2018], 1911, 1914, r"Main additions for 2018 correspond to the investment plans for the complete update of\s*the production plants located in Italy \(Euros 27,958 thousand\) and the United\s*Kingdom \(Euros 33,733 thousand\), as well as.*Castellar Vidrio \(Euros 16,329 thousand\)", "adiciones 2018: update plantas Italia/UK + Castellar"),
    2019: citar(T[2019], 1861, 1863, r"Main additions for 2019 correspond to the investment plans for the complete update of\s*the production plants located in Portugal \(Euros 20,250 thousand\) and the United\s*Kingdom \(Euros 44,247 thousand\)", "adiciones 2019: Portugal/UK"),
    2020: citar(T[2020], 2549, 2552, r"Main additions for 2020 and 2019 correspond to the investment plans for the complete\s*update of the production plants located in the United Kingdom \(Euros 77,801 thousand\s*and Euros 44,247 thousand respectively\) and Portugal \(Euros 29,031 thousand and\s*Euros 20,250 thousand respectively\)", "adiciones 2020/2019: UK/Portugal"),
    2021: citar(T[2021], 2328, 2331, r"Main additions for 2021 and 2020.*United Kingdom \(Euros 32,597 thousand\s*and Euros 77,801 thousand respectively\) and Portugal \(Euros 39,792 thousand and\s*Euros 29,031 thousand respectively\)", "adiciones 2021/2020: UK/Portugal"),
    2022: citar(T[2022], 2418, 2421, r"Main additions for 2022 and 2021.*United Kingdom \(Euros 23,479 thousand\s*and Euros 32,597 thousand respectively\) and Portugal \(Euros 94,557 thousand and\s*Euros 39,792 thousand respectively\)", "adiciones 2022/2021: UK/Portugal"),
    2023: citar(T[2023], 2355, 2359, r"The main additions in 2023 correspond to the investments made by the Group in its\s*subsidiaries in Portugal.*business combinations \(Note 5\).*2022.*modernization of the production plants located in the\s*United Kingdom and Portugal", "adiciones 2023: Portugal + combinaciones de negocio; 2022: modernización UK/Portugal"),
}
SALE_LEASEBACK = citar(T[2023], 2363, 2365, r"During the financial year 2022, the Group formalized various .?Sale & Leaseback. leasing\s*contracts.*fixed assets affecting their\s*production plants in Spain. During 2023, no new contracts", "sale & leaseback 2022 sobre plantas de España")
RECURRING_CAPEX = citar(T[2019], 2082, 2082, r"recurring capex captured in the valuation models", "prueba de deterioro: 'recurring capex captured in the valuation models' (sin cifra; CF_2019..CF_2023)")


def main():
    ruta = SALIDA / "VIDRALA_REPOSICION_CAPACIDAD.csv"
    with ruta.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["anio", "adiciones_ppe_bruto_miles_eur", "ppe_fuente", "pagos_inmovilizado_efe_miles_eur", "capex_fuente",
                    "altas_rou_activo_miles_eur", "rou_activo_fuente", "altas_rou_pasivo_miles_eur", "rou_pasivo_fuente",
                    "amort_rou_miles_eur", "amort_rou_fuente",
                    "vida_util_hornos", "renovacion_hornos", "adiciones_narrativa", "capacidad_anadida_publicada",
                    "otros", "notas"])
        for anio in range(2017, 2026):
            ppe, ppe_c = PPE_ADD[anio]
            cc = CAPEX_CASH[anio]
            capex_total = cc[0] + (cc[1] or 0)
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
                otros = f'altas ROU por combinación de negocios (The Park): {ROU_COMB_NEGOCIO[2023][0]} miles eur [{f(ROU_COMB_NEGOCIO[2023][1])}]'
            if anio == 2025:
                otros = (otros + "; " if otros else "") + f'otros ROU activo 9.595 (price update The Park) [{f(ROU_OTROS_2025)}]'
            if anio == 2022:
                otros = f'sale & leaseback sobre plantas de España [{f(SALE_LEASEBACK)}]'
            notas = []
            if anio == 2021:
                notas.append("ROU: saldo 770 a 31-dic-2021 sin tabla de movimientos publicada por separado [" + f(ROU_2021) + "]")
            if anio == 2023:
                notas.append("CF_2024 presenta el comparativo 2023 de adiciones PP&E con total 102.795 (columna extra 2.170) frente a 100.655 en CF_2023 [" + f(PPE_2023_CF2024) + "]; se registra la diferencia sin resolverla")
            if anio in (2022, 2024):
                notas.append(f"altas ROU activo y pasivo no coinciden ({ra[0] if ra else '-'} frente a {rp[0] if rp else '-'}); no se suponen idénticas")
            notas.append("vida útil hornos 8-16 años en todos los años [" + f(VIDA_UTIL) + "]")
            w.writerow([
                anio, ppe, f(ppe_c), capex_total, f(cc[2]),
                ra[0] if ra else "", f(ra[1]) if ra else "",
                rp[0] if rp else "", f(rp[1]) if rp else "",
                am[0] if am else "", f(am[1]) if am else "",
                "8 - 16 años (nota de inmovilizado, todos los años)", horno,
                narr["cita"][:300] if narr["cita"] else "",
                "NO PUBLICADA en los bytes conservados: Vidrala no desglosa capacidad añadida vs reposición; la cita del CFO ('more than pure replacement') es de transcripción de terceros sin bytes",
                otros, "; ".join(notas),
            ])
    print("escrito", ruta.relative_to(RAIZ))
    # comprobación de la cita de recurring capex
    print("recurring capex:", RECURRING_CAPEX["cita"][:120], "[" + f(RECURRING_CAPEX) + "]")


def PAG(c):
    return c["pagina_pdf"]


if __name__ == "__main__":
    main()
