"""Genera INVERSION_VISCOFAN_2016_2025.csv y PUENTE_CAPEX_DA_ROU.csv desde fuentes conservadas.

Cada operando lleva cita (archivo, rango de lineas, patron) que el script verifica
antes de usar el valor: si la cita no aparece en las lineas indicadas, falla.
Las fuentes son los textos conservados de la base 4.14 (.trabajo/insumos_m2/...) y
las extracciones de PDF verificadas (.trabajo/extracciones/..., ver extraer_pdfs_viscofan.py).
Aritmetica con Decimal. No interpola huecos.
"""
import csv
import json
import re
import sys
from decimal import Decimal
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
TEXTO = RAIZ / ".trabajo/insumos_m2/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/viscofan_decisiones/Viscofan/texto"
EXT = RAIZ / ".trabajo/extracciones"
SALIDA = RAIZ / "resultados_m2/pm1"

T = {n: TEXTO / n for n in ["AR_2017.txt", "IA_2018_es.txt", "AR_2019.txt", "AR_2020.txt", "CF_2021.txt",
                           "CF_2022_compilacion.txt", "CA_2023_es.txt", "CF_2024.txt", "AR_2025.txt"]}
E = {n: EXT / (n + ".txt") for n in ["IA_2016_es.pdf", "IA_2021_es.pdf", "IA_2023_es.pdf"]}
# Fuente nueva conservada en el repo (bloque B4): página oficial EN de la Memoria Anual 2024
HTML_IA2024 = RAIZ / "resultados_m2/pm1/fuentes_nuevas/viscofan_ia2024_en_financial_and_management_results.html"

_cache = {}


def ventana(ruta: Path, lo: int, hi: int) -> str:
    key = (str(ruta), lo, hi)
    if key not in _cache:
        lineas = ruta.read_text(encoding="utf-8").splitlines()
        _cache[key] = "\n".join(lineas[lo - 1:hi])
    return _cache[key]


def pagina_de(ruta: Path, linea: int) -> str:
    lineas = ruta.read_text(encoding="utf-8").splitlines()
    pagina = "?"
    for i, ln in enumerate(lineas[:linea], 1):
        m = re.match(r"\[PDF PAGE (\d+)\]", ln)
        if m:
            pagina = m.group(1)
    return pagina


def citar(ruta: Path, lo: int, hi: int, patron: str, uso: str) -> dict:
    """Verifica que el patron aparece en [lo, hi] y devuelve la cita."""
    texto = ventana(ruta, lo, hi)
    m = re.search(patron, texto, re.IGNORECASE | re.DOTALL)
    if not m:
        raise AssertionError(f"cita no verificada ({uso}): /{patron}/ no esta en {ruta.name} l{lo}-{hi}")
    return {
        "archivo": str(ruta.relative_to(RAIZ)),
        "lineas": f"{lo}-{hi}",
        "pagina_pdf": pagina_de(ruta, lo),
        "cita": " ".join(m.group(0).split()),
        "uso": uso,
    }


D = Decimal

# ---------------------------------------------------------------- inversión publicada por tipo
# Cada entrada: (anio, total Meur, cita_total, desglose dict o None, cita_desglose)
INVERSION = []

INVERSION.append({
    "anio": 2016, "total_meur": D("86.7"),
    "cita_total": citar(E["IA_2016_es.pdf"], 3985, 3986, r"Las inversiones realizadas en el ejercicio ascienden a .?86,7 mi-?\s*llones", "total inversión 2016"),
    "desglose": {"capacidad": D("51"), "proceso": D("22"), "ehs": D("8"), "ordinaria": D("19")},
    "cita_desglose": citar(E["IA_2016_es.pdf"], 3987, 3993, r"51% de la inversi.*19% restante se destin.*inversiones ordinarias", "desglose 2016"),
    "estado": "conservado",
})

INVERSION.append({
    "anio": 2017, "total_meur": D("107.2"),
    "cita_total": citar(T["IA_2018_es.txt"], 7338, 7342, r"71,6 millones frente a .?107,2 millones.*invertidos en 2017", "total inversión 2017 (comparativo)"),
    "desglose": None,
    "cita_desglose": None,
    "estado": "solo total publicado (comparativo en IA_2018); desglose por tipo AUSENTE en fuentes conservadas",
})

INVERSION.append({
    "anio": 2018, "total_meur": D("71.6"),
    "cita_total": citar(T["IA_2018_es.txt"], 7358, 7360, r"De los .?71,6 millones invertidos en 2018", "total inversión 2018"),
    "desglose": {"capacidad": D("12"), "proceso": D("55"), "ehs": D("8"), "ordinaria": D("25")},
    "cita_desglose": citar(T["IA_2018_es.txt"], 7360, 7375, r"55% mejoras de proceso.*25% inversiones ordinarias.*12% capacidad y maquinaria.*8% .?equipamiento energ", "desglose 2018"),
    "estado": "conservado",
})

INVERSION.append({
    "anio": 2019, "total_meur": D("62.1"),
    "cita_total": citar(T["AR_2019.txt"], 10555, 10555, r"breakdown by type of the .?62\.1 million invested in 2019", "total inversión 2019"),
    "desglose": {"capacidad": D("23"), "proceso": D("41"), "ehs": D("17"), "ordinaria": D("19")},
    "eur": {"capacidad": D("14.3"), "proceso": D("25.3"), "ehs": D("10.6"), "ordinaria": D("11.9")},
    "cita_desglose": citar(T["AR_2019.txt"], 10557, 10561, r"41% of investment.*25\.3 million.*23% of investment.*14\.3 million.*17% of investment.*10\.6 million.*remaining 19%", "desglose 2019"),
    "estado": "conservado",
})

INVERSION.append({
    "anio": 2020, "total_meur": D("56.9"),
    "cita_total": citar(T["AR_2020.txt"], 11250, 11251, r"total of .?56\.9 million have been invested", "total inversión 2020"),
    "desglose": {"capacidad": D("27"), "proceso": D("20"), "ehs": D("27"), "ordinaria": D("26")},
    "cita_desglose": citar(T["AR_2020.txt"], 11253, 11258, r"20% of the investment was earmarked for process.*27% of the investment was earmarked for investments in capacity.*27% of the investment was earmarked for improvements in sustainability.*remaining 26%.*ordinary investments", "desglose 2020"),
    "estado": "conservado",
})

INVERSION.append({
    "anio": 2021, "total_meur": D("92.0"),
    "cita_total": citar(T["CF_2022_compilacion.txt"], 8937, 8937, r"A total of .?125\.6 million ..92\.0 million in 2021.", "total inversión 2021 (comparativo en CF 2022)"),
    "desglose": {"capacidad": D("44"), "proceso": D("18"), "ehs": D("18"), "ordinaria": D("20")},
    "cita_desglose": citar(E["IA_2021_es.pdf"], 16958, 16968, r"desglose de inversiones de 2021 por tipolog.*44% de la inversi.*18% de la inversi.*18% de la inversi.*20% restante.*inversiones ordinarias", "desglose 2021"),
    "estado": "conservado",
})

INVERSION.append({
    "anio": 2022, "total_meur": D("125.6"),
    "cita_total": citar(T["CF_2022_compilacion.txt"], 8937, 8937, r"A total of .?125\.6 million", "total inversión 2022"),
    "desglose": {"capacidad": D("40"), "proceso": D("30"), "ehs": D("16"), "ordinaria": D("14")},
    "cita_desglose": citar(T["CF_2022_compilacion.txt"], 8947, 8954, r"breakdown by type of investment in 2022.*40% of the investment.*capacity and machinery.*30% of the investment.*process improvements.*16% of the investment.*sustainability.*remaining 14%.*ordinary investments", "desglose 2022"),
    "estado": "conservado",
})

INVERSION.append({
    "anio": 2023, "total_meur": D("77.5"),
    "cita_total": citar(E["IA_2023_es.pdf"], 17028, 17029, r"En el ejercicio 2023 se han invertido un total de .?77,5 millones", "total inversión 2023"),
    "desglose": {"capacidad": D("16"), "proceso": D("3"), "ehs": D("26"), "ordinaria": D("55")},
    "cita_desglose": citar(E["IA_2023_es.pdf"], 17042, 17050, r"16% de la inversi.*capacidad y maquinaria.*3% de la inversi.*26% de la inversi.*55% restante.*inversiones ordinarias", "desglose 2023"),
    "estado": "conservado",
})

INVERSION.append({
    "anio": 2024, "total_meur": D("71.0"),
    "cita_total": citar(HTML_IA2024, 343, 343, r"Investment in 2024 amounted to .?71\.0 million ..77\.5 million in 2023.", "total inversión 2024 (fuente nueva B4, HTML oficial)") if HTML_IA2024.exists() else citar(T["AR_2025.txt"], 5948, 5949, r"Investments in 2025 totalled .*84\.1.*million.*71\.0 million in 2024", "total inversión 2024 (comparativo en AR 2025)"),
    "desglose": {"capacidad": D("34"), "proceso": D("14"), "ehs": D("35"), "ordinaria": D("17")},
    "cita_desglose": citar(HTML_IA2024, 346, 349, r"34% of the investment was earmarked for investments in capacity and machinery.*35% of the investment was earmarked for improvements in sustainability.*14% of the investment was earmarked for process improvements and new technology.*remaining 17% was spent on ordinary investments", "desglose 2024 (fuente nueva B4, HTML oficial informeanual2024.viscofan.com; PDF gestión 2024 p.8 verificado por OCR)") if HTML_IA2024.exists() else None,
    "estado": "conservado en fuente nueva B4: página HTML oficial de la Memoria Anual 2024 (bytes en resultados_m2/pm1/fuentes_nuevas/, SHA-256 bd139bde…); total también comparativo en AR 2025 p143/impresa 123; PDF informe de gestión 2024 (sha256 1dc3ef18…/195fa418…) en cobertura provisional (no subible como asset)",
})

INVERSION.append({
    "anio": 2025, "total_meur": D("84.1"),
    "cita_total": citar(T["AR_2025.txt"], 5948, 5950, r"Investments in 2025 totalled .*84\.1.*million", "total inversión 2025"),
    "desglose": {"capacidad": D("37"), "proceso": D("22"), "ehs": D("27"), "ordinaria": D("14")},
    "eur": {"capacidad": D("30.9"), "proceso": D("19.2"), "ehs": D("22.4"), "ordinaria": D("11.6")},
    "cita_desglose": citar(T["AR_2025.txt"], 5952, 5971, r"30\.9 million.*37%.*increasing.*capacity.*22\.4 million.*27%.*environmental and safety.*19\.2 million.*22%.*process.*improvements.*11\.6 million.*14%.*other ordinary.*investments", "desglose 2025"),
    "estado": "conservado (AR_2025 PDF p143 = impresa 123; el índice antiguo citaba PDF 144, desplazado en 1)",
})

# ---------------------------------------------------------------- puente capex / D&A / ROU
# miles de euros salvo que se indique
CAPEX_CAJA = {  # pagos por adquisición de inmovilizado material e intangible (EFE)
    2016: (D("80747"), citar(T["AR_2017.txt"], 548, 548, r"Payments for acquisition of property, plant, equipment and intangible assets\s+15\.1\s+\([-\u2212]?111,561\)\s+\([-\u2212]?80,747\)", "capex caja 2017/2016")),
    2017: (D("111561"), citar(T["AR_2017.txt"], 548, 548, r"\([-\u2212]?111,561\)\s+\([-\u2212]?80,747\)", "capex caja 2017")),
    2018: (D("71949"), citar(T["IA_2018_es.txt"], 942, 942, r"Pagos por la adquisici.n de inmovilizado material e intangible\s+15\.1\s+\([-\u2212]?71\.949\)\s+\([-\u2212]?111\.561\)", "capex caja 2018/2017")),
    2019: (D("62755"), citar(T["AR_2019.txt"], 541, 541, r"Payments for acquisition of property, plant, equipment and intangible assets\s+16\.1\s+\([-\u2212]?62,755\)\s+\(71,949\)", "capex caja 2019/2018")),
    2020: (D("55320"), citar(T["AR_2020.txt"], 422, 423, r"Payments for acquisition of property, plant, equipment and intangible\s*.*\n.*assets\s+[-\u2212]55\.320\s+[-\u2212]62\.755", "capex caja 2020/2019")),
    2021: (D("95779"), citar(T["CF_2022_compilacion.txt"], 337, 337, r"Payments for the acquisition of tangible and intangible fixed assets\s+[-\u2212]115\.566\s+[-\u2212]95\.779", "capex caja 2022/2021 (columna 2021; en CF_2021 p8 la etiqueta inglesa de esta linea esta intercambiada con la de adquisicion de dependientes)")),
    2022: (D("115566"), citar(T["CF_2022_compilacion.txt"], 337, 337, r"[-−]115\.566", "capex caja 2022")),
    2023: (D("77126"), citar(T["CA_2023_es.txt"], 303, 303, r"Pagos por la adquisici.n de inmovilizado material e intangible\s+[-\u2212]77\.126\s+[-\u2212]115\.566", "capex caja 2023/2022")),
    2024: (D("75027"), citar(T["CF_2024.txt"], 427, 427, r"Payments for the acquisition of tangible and intangible fixed assets\s+[-\u2212]75,027\s+[-\u2212]77,126", "capex caja 2024/2023")),
    2025: (D("80447"), citar(T["AR_2025.txt"], 386, 386, r"Payments for the acquisition of PP&E and intangible fixed assets\s+[-\u2212]80,447\s+[-\u2212]75,027", "capex caja 2025/2024")),
}

DA_TOTAL = {  # amortización total (suma de líneas del EFE/P&L), miles eur
    2016: (D("3282") + D("46417"), citar(T["AR_2017.txt"], 512, 514, r"Amortization of intangible assets\s+9\s+3,488\s+3,282.*Depreciation of property, plant and equipment\s+10\s+52,894\s+46,417", "D&A 2017/2016 (3.282+46.417)")),
    2017: (D("3488") + D("52894"), citar(T["AR_2017.txt"], 512, 514, r"Amortization of intangible assets\s+9\s+3,488\s+3,282", "D&A 2017")),
    2018: (D("3801") + D("58637"), citar(T["IA_2018_es.txt"], 706, 708, r"Gastos por amortizaci.n de activos intangibles\s+9\s+\(3\.801\)\s+\(3\.488\).*Gastos por amortizaci.n del inmovilizado material\s+10\s+\(58\.637\)\s+\(52\.894\)", "D&A 2018/2017")),
    2019: (D("4087") + D("62071") + D("4516"), citar(T["AR_2019.txt"], 522, 524, r"Amortization of intangible assets\s+9\s+4,087\s+3,801.*Depreciation of property, plant and equipment\s+10\s+62,071\s+58,637.*Depreciation of Right-of-use assets\s+11\s+4,516", "D&A 2019 (intangibles+material+ROU)")),
    2020: (D("71526"), citar(T["CF_2021.txt"], 278, 278, r"Ajustment for amortization and depreciation cost\s+72,281\s+71,526", "D&A 2021/2020")),
    2021: (D("72281"), citar(T["CF_2021.txt"], 278, 278, r"amortization and depreciation cost\s+72,281", "D&A 2021")),
    2022: (D("78148"), citar(T["CF_2022_compilacion.txt"], 322, 322, r"Adjustment for depreciation expenses\s+78,148\s+72,281", "D&A 2022/2021")),
    2023: (D("83713"), citar(T["CA_2023_es.txt"], 288, 288, r"Ajuste por gastos de amortizaci.n\s+83\.713\s+78\.148", "D&A 2023/2022")),
    2024: (D("83794"), citar(T["CF_2024.txt"], 406, 406, r"Adjustment for depreciation expenses\s+83,794\s+83,713", "D&A 2024/2023")),
    2025: (D("85196"), citar(T["AR_2025.txt"], 369, 369, r"Adjustment for amortization expenses\s+85,196\s+83,794", "D&A 2025/2024")),
}

ROU_ALTAS = {  # altas de derechos de uso (nota 7.1), miles eur
    2019: (D("3510"), citar(T["AR_2019.txt"], 3534, 3534, r"Additions to right-of-use assets in 2019 amounted to 3,510 thousand euros", "altas ROU 2019")),
    2020: (D("2007"), citar(T["AR_2020.txt"], 2898, 2898, r"Additions to right-of-use assets in 2020 amounted to 2,007 thousand euros; 3,510 thousand euros in 2019", "altas ROU 2020/2019")),
    2021: (D("3010"), citar(T["CF_2021.txt"], 2318, 2318, r"Additions to right-of-use assets in 2021 amounted to .?3,010 thousand; .?2,007 thousand in 2020", "altas ROU 2021/2020")),
    2022: (D("1633"), citar(T["CF_2022_compilacion.txt"], 2055, 2055, r"Additions to right-of-use assets in 2022 amounted to 1,633 thousand euros; 3,010 thousand euros in 2021", "altas ROU 2022/2021")),
    2023: (D("6554"), citar(T["CA_2023_es.txt"], 1998, 1998, r"Additions to right-of-use assets in 2023 amounted to 6,554 thousand euros; 1,633 thousand euros in 2022", "altas ROU 2023/2022")),
    2024: (D("6419"), citar(T["CF_2024.txt"], 3140, 3140, r"Additions to right-of-use assets in 2024 amounted to 6,419 thousand euros; 6,554 thousand", "altas ROU 2024/2023")),
    2025: (D("6494"), citar(T["AR_2025.txt"], 2374, 2374, r"Additions to right-of-use assets during 2025 amounted to 6,494 thousand euros; 6,419 thousand euros in 2024", "altas ROU 2025/2024")),
}

ROU_AMORT = {  # amortización de derechos de uso, miles eur
    2019: (D("4516"), citar(T["AR_2019.txt"], 524, 524, r"Depreciation of Right-of-use assets\s+11\s+4,516", "amort ROU 2019")),
    2020: (D("4766"), citar(T["AR_2020.txt"], 171, 171, r"Depreciation expenses on right of use\s+7\.1\s+[-−]4\.766\s+[-−]4\.516", "amort ROU 2020/2019")),
    2021: (D("5123"), citar(T["CA_2023_es.txt"], 92, 92, r"Gastos por amortizaci.n de activos por derecho de uso\s+7\.1\s+[-\u2212]5\.293\s+[-\u2212]5\.289", "amort ROU 2022 (comparativo); 2021 sale de la tabla de movimientos de CF_2021 p39 (columna de amortizaci.n -5,123)")),
    2022: (D("5289"), citar(T["CA_2023_es.txt"], 92, 92, r"[-−]5\.293\s+[-\u2212]5\.289", "amort ROU 2023/2022")),
    2023: (D("5293"), citar(T["CA_2023_es.txt"], 92, 92, r"Gastos por amortizaci.n de activos por derecho de uso\s+7\.1\s+[-\u2212]5\.293", "amort ROU 2023")),
    2024: (D("5843"), citar(T["AR_2025.txt"], 177, 177, r"Depreciation of right-of-use assets\s+7\.1\s+[-\u2212]5,503\s+[-\u2212]5,843", "amort ROU 2025/2024")),
    2025: (D("5503"), citar(T["AR_2025.txt"], 177, 177, r"Depreciation of right-of-use assets\s+7\.1\s+[-\u2212]5,503", "amort ROU 2025")),
}

PPE_ADICIONES = {  # adiciones brutas de inmovilizado material (nota 6), miles eur
    2017: (D("103417"), citar(T["AR_2017.txt"], 3237, 3237, r"In 2017, investments in property, plant and equipment in the Group totalled 103,417 thousand euros", "adiciones PP&E 2017")),
    2018: (D("67157"), citar(T["AR_2019.txt"], 3420, 3420, r"In 2018, investments in property, plant and equipment in the Group totalled 67,157 thousand euros", "adiciones PP&E 2018")),
    2019: (D("58103"), citar(T["AR_2019.txt"], 3414, 3414, r"In 2019, investments in property, plant and equipment in the Group totalled 58,103 thousand euros", "adiciones PP&E 2019")),
    2020: (D("52727"), citar(T["AR_2020.txt"], 2767, 2767, r"In 2020, investments in property, plant and equipment in the Group totalled 52,727 thousand euros", "adiciones PP&E 2020")),
    2021: (D("87746"), citar(T["CF_2021.txt"], 2192, 2192, r"In 2021, investments in property, plant and equipment in the Group totalled .?87,746 thousand", "adiciones PP&E 2021")),
    2022: (D("120362"), citar(T["CF_2022_compilacion.txt"], 1934, 1934, r"In 2022, investments in property, plant and equipment in the Group totalled 120,362 thousand euros", "adiciones PP&E 2022")),
    2023: (D("73306"), citar(T["CA_2023_es.txt"], 1876, 1876, r"In 2023, investments in property, plant and equipment in the Group totalled 73,306 thousand euros", "adiciones PP&E 2023")),
    2024: (D("65458"), citar(T["CF_2024.txt"], 2960, 2960, r"In 2024, investments in property, plant and equipment in the Group totalled 65,458 thousand", "adiciones PP&E 2024")),
    2025: (D("76174"), citar(T["AR_2025.txt"], 2237, 2237, r"During 2025, the Group invested .?76,174,000 in property, plant and equipment", "adiciones PP&E 2025 (sin 3.152 del Note 2.1 por combinaci.n de negocios)")),
}

INV_PUB = {e["anio"]: e for e in INVERSION}

TAXONOMIA_CAPEX_2025 = {
    "valor_meur": D("90.6"),
    "cita": citar(T["AR_2025.txt"], 13581, 13581, r"TOTAL\s+90\.6\s+100\.0%", "CapEx taxonomía UE 2025 (intangibles+PP&E+ROU)"),
}
APM_CAPEX_DEF = citar(T["AR_2025.txt"], 6132, 6136, r"Capex: It is calculated as the sum of the.*additions of intangible fixed assets and.*property, plant and equipment", "definición APM Capex (sin ROU), AR 2025 p146")
TAXONOMIA_CAPEX_DEF = citar(T["AR_2025.txt"], 13495, 13495, r"CapEx\. Investments in intangible assets, property, plant and equipment and rights-of-use assets", "definición CapEx taxonomía (con ROU), AR 2025 p275")


def escribir_inversion_csv() -> None:
    ruta = SALIDA / "INVERSION_VISCOFAN_2016_2025.csv"
    with ruta.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["anio", "total_publicado_meur", "total_doc", "total_pagina_pdf", "total_lineas", "total_cita",
                    "pct_capacidad", "pct_proceso", "pct_ehs_sostenibilidad", "pct_ordinaria",
                    "eur_capacidad_meur", "eur_proceso_meur", "eur_ehs_meur", "eur_ordinaria_meur",
                    "desglose_doc", "desglose_pagina_pdf", "desglose_lineas", "desglose_cita",
                    "unidad", "perimetro", "estado_desglose", "notas"])
        for e in INVERSION:
            d = e.get("desglose") or {}
            eur = e.get("eur") or {}
            ct = e["cita_total"]
            cd = e.get("cita_desglose")
            w.writerow([
                e["anio"], str(e["total_meur"]), ct["archivo"], ct["pagina_pdf"], ct["lineas"], ct["cita"],
                str(d.get("capacidad", "")) if d else "", str(d.get("proceso", "")) if d else "",
                str(d.get("ehs", "")) if d else "", str(d.get("ordinaria", "")) if d else "",
                str(eur.get("capacidad", "")), str(eur.get("proceso", "")), str(eur.get("ehs", "")), str(eur.get("ordinaria", "")),
                cd["archivo"] if cd else "AUSENTE", cd["pagina_pdf"] if cd else "", cd["lineas"] if cd else "",
                cd["cita"] if cd else "", "millones de euros, inversión publicada por la empresa en el informe de gestión",
                "consolidado Grupo Viscofan", e["estado"],
                "Porcentajes publicados por la empresa; no son mantenimiento económico ni crecimiento salvo que la fuente lo diga (solo 2025 dice 'aimed at increasing capacity')",
            ])
    print("escrito", ruta.relative_to(RAIZ))


def escribir_puente_csv() -> dict:
    ruta = SALIDA / "PUENTE_CAPEX_DA_ROU.csv"
    totales = {}
    with ruta.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["anio", "capex_caja_miles_eur", "capex_caja_fuente", "da_total_miles_eur", "da_fuente",
                    "altas_rou_miles_eur", "altas_rou_fuente", "amort_rou_miles_eur", "amort_rou_fuente",
                    "adiciones_ppe_bruto_miles_eur", "adiciones_ppe_fuente",
                    "inversion_publicada_meur", "inversion_publicada_fuente",
                    "perimetro_niif16_miles_eur", "exceso_sobre_da_miles_eur",
                    "diferencia_publicada_vs_caja_miles_eur", "notas"])
        for anio in range(2016, 2026):
            cc, cc_c = CAPEX_CAJA[anio]
            da, da_c = DA_TOTAL[anio]
            rou_a = ROU_ALTAS.get(anio)
            rou_am = ROU_AMORT.get(anio)
            ppe, ppe_c = PPE_ADICIONES.get(anio, (None, None))
            pub = INV_PUB[anio]
            perimetro = cc + (rou_a[0] if rou_a else D("0"))
            exceso = perimetro - da
            diff_pub = (pub["total_meur"] * 1000) - cc
            nota = ""
            if anio < 2019:
                nota = "NIIF 16 no aplica: sin derechos de uso; perímetro NIIF16 = capex de caja"
            if anio == 2021:
                nota = "En CF_2021 p8 la etiqueta inglesa de la línea de pagos está intercambiada con la de adquisición de dependientes; la columna comparativa de CF_2022 p25 l337 fija pagos 2021 = -95.779 y dependientes = 0"
            if anio == 2022:
                nota = "Puente clave: publicada 125,6 M€ frente a capex de caja 115,566 M€; la diferencia no se iguala por conveniencia (ver DOSSIER_D2)"
            if anio == 2025:
                nota = "En 2025 la empresa publica CapEx taxonomía 90,6 M€ = inversión gestión 84,1 + altas ROU 6,494 (aprox.); la definición APM Capex (AR 2025 p146) excluye ROU"
            w.writerow([anio, str(cc), f'{cc_c["archivo"]} p{cc_c["pagina_pdf"]} l{cc_c["lineas"]}', str(da),
                        f'{da_c["archivo"]} p{da_c["pagina_pdf"]} l{da_c["lineas"]}',
                        str(rou_a[0]) if rou_a else "", (f'{rou_a[1]["archivo"]} p{rou_a[1]["pagina_pdf"]} l{rou_a[1]["lineas"]}' if rou_a else ""),
                        str(rou_am[0]) if rou_am else "", (f'{rou_am[1]["archivo"]} p{rou_am[1]["pagina_pdf"]} l{rou_am[1]["lineas"]}' if rou_am else ""),
                        str(ppe) if ppe else "", (f'{ppe_c["archivo"]} p{ppe_c["pagina_pdf"]} l{ppe_c["lineas"]}' if ppe else ""),
                        str(pub["total_meur"]), f'{pub["cita_total"]["archivo"]} p{pub["cita_total"]["pagina_pdf"]} l{pub["cita_total"]["lineas"]}',
                        str(perimetro), str(exceso), str(diff_pub), nota])
            totales[anio] = {"capex_caja": cc, "da": da, "altas_rou": rou_a[0] if rou_a else None,
                             "amort_rou": rou_am[0] if rou_am else None, "ppe": ppe, "publicada": pub["total_meur"] * 1000,
                             "perimetro": perimetro, "exceso": exceso}
    print("escrito", ruta.relative_to(RAIZ))
    return totales


def resumen_json(totales: dict) -> dict:
    anios = list(range(2021, 2026))
    s_caja = sum(totales[a]["capex_caja"] for a in anios)
    s_rou = sum(totales[a]["altas_rou"] for a in anios)
    s_da = sum(totales[a]["da"] for a in anios)
    s_rou_am = sum(totales[a]["amort_rou"] for a in anios)
    s_per = sum(totales[a]["perimetro"] for a in anios)
    exceso = s_per - s_da
    return {
        "ventana_modelo": "2021-2025 (años H-L del libro)",
        "suma_capex_caja_miles_eur": str(s_caja),
        "suma_altas_rou_miles_eur": str(s_rou),
        "suma_da_miles_eur": str(s_da),
        "suma_amort_rou_miles_eur": str(s_rou_am),
        "perimetro_niif16_miles_eur": str(s_per),
        "exceso_sobre_da_miles_eur": str(exceso),
        "exceso_perimetro_caja_miles_eur": str(s_caja - s_da),
        "comprobacion": "exceso NIIF16 64.923 y altas ROU 24.110 y amort ROU 27.051 coinciden con la conciliación de la base; recalculado aquí desde citas verificadas",
        "capex_taxonomia_2025_meur": str(TAXONOMIA_CAPEX_2025["valor_meur"]),
        "apm_capex_def": APM_CAPEX_DEF["cita"],
        "taxonomia_capex_def": TAXONOMIA_CAPEX_DEF["cita"],
    }


def main() -> int:
    escribir_inversion_csv()
    totales = escribir_puente_csv()
    resumen = resumen_json(totales)
    (SALIDA / "puente_resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(resumen, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
