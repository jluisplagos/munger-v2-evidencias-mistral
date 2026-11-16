"""CALCULOS_PM1: recálculo con Decimal de las tablas de theta y rangos de lambda.

Lee los CSV generados por tablas_viscofan.py (INVERSION_VISCOFAN_2016_2025.csv,
PUENTE_CAPEX_DA_ROU.csv) y las series primarias de Eurostat (indices/).

Definición del modelo (configuracion_economica.py, solo lectura, como índice):
familia Theta: theta x exceso histórico medio; exceso = sum(capex + altas ROU - D&A) 2021-2025.
M (reposición) estimada con el desglose por tipo publicado por Viscofan, tres definiciones:
  estrecha = solo ordinaria; media = ordinaria + EHS; amplia = todo lo que no es capacidad.
  theta = (sum M - sum D&A) / exceso.

NO adopta theta ni lambda: solo delimita. Una theta negativa se conserva como diagnóstico
de definición/identificación (no se trunca a 0). Lambda se calcula como rango condicionado
a serie y vida útil explícitas. Conclusión del frente: P-M1 no delimitada con la evidencia
disponible; se mantiene el bloqueo de la conclusión afectada.
"""
import csv
import json
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 40
D = Decimal
RAIZ = Path(__file__).resolve().parents[3]
SALIDA = RAIZ / "resultados_m2/pm1"

AÑOS = [2021, 2022, 2023, 2024, 2025]


def leer_csv(nombre):
    with (SALIDA / nombre).open(encoding="utf-8") as f:
        return {int(r["anio"]): r for r in csv.DictReader(f)}


def leer_indice(nombre):
    with (SALIDA / "indices" / nombre).open(encoding="utf-8") as f:
        return {int(r["anio"]): D(r["indice_2021_100"]) for r in csv.DictReader(f) if r["indice_2021_100"]}


def main():
    inv = leer_csv("INVERSION_VISCOFAN_2016_2025.csv")
    puente = leer_csv("PUENTE_CAPEX_DA_ROU.csv")

    base = {}       # perímetro NIIF16 = capex caja + altas ROU (miles eur)
    da = {}
    pct = {}
    pub = {}
    for a in AÑOS:
        cc = D(puente[a]["capex_caja_miles_eur"])
        rou = D(puente[a]["altas_rou_miles_eur"])
        base[a] = cc + rou
        da[a] = D(puente[a]["da_total_miles_eur"])
        pct[a] = {"capacidad": D(inv[a]["pct_capacidad"]) / 100, "proceso": D(inv[a]["pct_proceso"]) / 100,
                  "ehs": D(inv[a]["pct_ehs_sostenibilidad"]) / 100, "ordinaria": D(inv[a]["pct_ordinaria"]) / 100}
        pub[a] = D(inv[a]["total_publicado_meur"]) * 1000

    sum_base = sum(base.values())
    sum_da = sum(da.values())
    exceso = sum_base - sum_da
    exceso_caja = sum(D(puente[a]["capex_caja_miles_eur"]) for a in AÑOS) - sum_da
    sum_pub = sum(pub.values())
    exceso_pub = sum_pub - sum_da

    def M(definicion):
        tot = {}
        for a in AÑOS:
            if definicion == "estrecha":
                m = base[a] * pct[a]["ordinaria"]
            elif definicion == "media":
                m = base[a] * (pct[a]["ordinaria"] + pct[a]["ehs"])
            else:  # amplia
                m = base[a] * (1 - pct[a]["capacidad"])
            tot[a] = m
        return tot

    resultados_theta = {}
    for definicion in ("estrecha", "media", "amplia"):
        m = M(definicion)
        sum_m = sum(m.values())
        theta = (sum_m - sum_da) / exceso
        resultados_theta[definicion] = {
            "sum_M_miles_eur": str(sum_m),
            "sum_DA_miles_eur": str(sum_da),
            "exceso_miles_eur": str(exceso),
            "theta": str(theta),
            "M_por_anio_miles_eur": {str(a): str(m[a]) for a in AÑOS},
            "M_menor_que_DA_en_cada_anio": all(m[a] < da[a] for a in AÑOS),
        }

    # contraste: definición amplia aplicada al total publicado (base a la que pertenecen los
    # porcentajes publicados); cálculo SEPARADO del de abajo, que es extrapolación de perímetro
    m_pub = {a: pub[a] * (1 - pct[a]["capacidad"]) for a in AÑOS}
    sum_m_pub = sum(m_pub.values())
    theta_pub = (sum_m_pub - sum_da) / exceso_pub
    contraste = {
        "etiqueta": "TRANSFORMACIÓN sobre la base correcta: porcentajes aplicados al total publicado al que pertenecen",
        "sum_M_sobre_publicado_miles_eur": str(sum_m_pub),
        "exceso_sobre_publicado_miles_eur": str(exceso_pub),
        "theta": str(theta_pub),
    }

    # sensibilidad sobre el perímetro NIIF16 (capex caja + altas ROU): HIPÓTESIS de extrapolación
    # de perímetro (los porcentajes se aplican a una base distinta del total publicado)
    cap = {a: base[a] * pct[a]["capacidad"] for a in AÑOS}
    sum_cap = sum(cap.values())
    m_amplia = M("amplia")
    sum_m_amplia = sum(m_amplia.values())
    sensibilidad_hipotesis = []
    for th in (D("0"), D("0.2"), D("0.5"), D("1")):
        m_necesaria = sum_da + th * exceso
        reclasificar = m_necesaria - sum_m_amplia
        sensibilidad_hipotesis.append({
            "theta": str(th),
            "M_necesaria_miles_eur": str(m_necesaria),
            "capacidad_a_reclasificar_miles_eur": str(reclasificar),
            "fraccion_de_la_capacidad_publicada": str(reclasificar / sum_cap),
        })
    # sensibilidad sobre el total publicado (base correcta), calculada aparte y separada
    cap_pub = {a: pub[a] * pct[a]["capacidad"] for a in AÑOS}
    sum_cap_pub = sum(cap_pub.values())
    sensibilidad_publicado = []
    for th in (D("0"), D("0.2"), D("0.5"), D("1")):
        m_necesaria_pub = sum_da + th * exceso_pub
        reclas_pub = m_necesaria_pub - sum_m_pub
        sensibilidad_publicado.append({
            "theta": str(th),
            "M_necesaria_miles_eur": str(m_necesaria_pub),
            "capacidad_a_reclasificar_miles_eur": str(reclas_pub),
            "fraccion_de_la_capacidad_publicada": str(reclas_pub / sum_cap_pub),
        })
    sensibilidad = {
        "hipotesis_extrapolacion_perimetro_NIIF16_capex_caja_mas_altas_ROU": sensibilidad_hipotesis,
        "sobre_total_publicado_base_correcta": sensibilidad_publicado,
    }

    # ---------------- lambda (Vidrala) ----------------
    series = {}
    metadatos = {}
    for nombre, tag in [("eurostat_sts_inpp_a_ES_C23_I21_NSA.csv", "C23 productos minerales no metálicos (incluye vidrio)"),
                        ("eurostat_sts_inpp_a_ES_C28_I21_NSA.csv", "C28 maquinaria y equipo")]:
        with (SALIDA / "indices" / nombre).open(encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        s = {int(r["anio"]): D(r["indice_2021_100"]) for r in rows if r["indice_2021_100"]}
        series[tag] = s
        metadatos[tag] = {k: rows[0][k] for k in ("dataset", "geo", "nace_r2", "unidad", "ajuste_estacional", "url_api", "sha256_json", "fecha_actualizacion_dataset")}

    T = 2025
    lambdas = {}
    for tag, s in series.items():
        vals = []
        for L in range(8, 17):
            if T - L in s:
                lam = s[T] / s[T - L]
                vals.append({"vida_util_L": L, "anio_base": T - L, "indice_t": str(s[T]), "indice_t_menos_L": str(s[T - L]), "lambda": str(lam)})
        lambdas[tag] = {
            "metadatos": metadatos[tag],
            "formula": "lambda = PPI(2025) / PPI(2025 - L), L vida útil del activo que se repone (hornos 8-16 años según nota de Vidrala)",
            "valores": vals,
            "rango_L_8_16": [str(min(v["lambda"] for v in vals)), str(max(v["lambda"] for v in vals))],
        }

    out = {
        "clasificacion": "derivación sobre datos publicados verificados; NO es adopción de parámetros",
        "modelo": {
            "familia_theta": "theta x exceso histórico medio; theta en [0,1] por definición de la familia",
            "exceso_NIIF16_2021_2025_miles_eur": str(exceso),
            "exceso_perimetro_caja_2021_2025_miles_eur": str(exceso_caja),
            "sum_capex_caja_2021_2025_miles_eur": str(sum(D(puente[a]["capex_caja_miles_eur"]) for a in AÑOS)),
            "sum_altas_rou_2021_2025_miles_eur": str(sum(D(puente[a]["altas_rou_miles_eur"]) for a in AÑOS)),
            "sum_DA_2021_2025_miles_eur": str(sum_da),
            "base_por_anio_miles_eur": {str(a): str(base[a]) for a in AÑOS},
        },
        "clasificacion_calculos": {
            "datos": "totales y porcentajes por tipo publicados por Viscofan 2021-2025 (INVERSION_VISCOFAN_2016_2025.csv) y capex caja / altas ROU / D&A (PUENTE_CAPEX_DA_ROU.csv); cada operando con cita verificada",
            "transformacion_sobre_base_publicada": "contraste_amplia_sobre_total_publicado: los porcentajes se aplican al total publicado al que pertenecen (base correcta)",
            "hipotesis_extrapolacion_de_perimetro": "resultados (estrecha/media/amplia) y sensibilidad sobre (capex caja + altas ROU): los porcentajes publicados se aplican a un perímetro distinto del total publicado; se trata como HIPÓTESIS, no como dato ni como identificación",
            "diagnostico_condicional": "theta negativa (fuera de [0,1]) y sensibilidad de reclasificación: diagnósticos condicionales; truncar a 0 no valida theta=0",
            "politica": "ninguna adoptada; una política prudencial solo podría ser propuesta humana explícita, no parámetro identificado",
        },
        "theta_desglose_viscofan": {
            "definicion_M": "porcentajes publicados por Viscofan aplicados a (capex caja + altas ROU) de cada año",
            "etiqueta_definicion_M": "HIPÓTESIS (extrapolación de perímetro): base distinta del total publicado al que pertenecen los porcentajes",
            "resultados": resultados_theta,
            "contraste_amplia_sobre_total_publicado": contraste,
            "inversion_de_capacidad_2021_2025_miles_eur": {"hipotesis_perimetro_NIIF16": str(sum_cap), "sobre_total_publicado_base_correcta": str(sum_cap_pub)},
            "sensibilidad_reclasificacion_capacidad": sensibilidad,
            "lectura": "Con la clasificación de la propia empresa, M < D&A en los cinco años bajo las tres definiciones sobre el perímetro NIIF16 (hipótesis de extrapolación) y también en el contraste sobre el total publicado; theta resulta negativa (fuera del dominio [0,1]) en todos los casos y se conserva como diagnóstico de definición/identificación: truncarla a 0 no valida theta=0. Una theta negativa no identifica ningún valor de theta, y aceptar la clasificación de la empresa no identifica la estructura ni la familia de P-M1. Para theta>=0 haría falta tratar como reposición desde el ~60% (theta=0) hasta el 100% (theta=1) de lo que la empresa declara como capacidad (sensibilidad, diagnóstico condicional). Conclusión: P-M1 no delimitada con la evidencia disponible y bloqueo de la conclusión afectada (D2 y, de ella, D5/D6, pendientes de la persona responsable). Dato concreto que permitiría avanzar: evidencia publicada (o aceptación humana documentada) de qué fracción de la inversión declarada es reposición y, para Vidrala, el desglose reposición/capacidad de las reconstrucciones de hornos. Qué fracción es creíble es un juicio económico de la persona responsable; este frente no lo fija.",
        },
        "lambda_vidrala": {
            "proposito": "rango condicionado a serie primaria y vida útil explícitas; NO adopta lambda",
            "series": lambdas,
            "limites": [
                "Mide la variación de precios de producción del sector (output), no el precio de un horno concreto (input de capital).",
                "No captura cambio técnico (un horno nuevo puede ser más barato por tonelada) ni cambio de capacidad en la reconstrucción.",
                "Serie de España, anual, media, sin ajustar (NSA), base 2021=100; no representa exactamente activos, tecnología y geografía del grupo Vidrala.",
                "La vida útil 8-16 años es una pista de la nota contable contrastada, no una distribución adoptada.",
            ],
        },
        "conclusion_frente_B": "P-M1 no delimitada con la evidencia disponible; bloqueo de la conclusión afectada (D2/D5/D6 pendientes de la persona responsable). Datos concretos que permitirían avanzar: desglose por tipo 2017 de Viscofan; desglose reposición/capacidad de las reconstrucciones de hornos de Vidrala (nº de hornos, calendario, coste, capacidad antes/después); evidencia de qué fracción de la inversión declarada es reposición.",
        "pendiente": [
            "theta y lambda no identificados por la evidencia disponible; P-M1 no delimitada y bloqueo de la conclusión afectada; no se elige valor.",
            "Desglose por tipo de 2017 de Viscofan ausente en bytes conservados.",
            "Vidrala no publica desglose reposición/capacidad de las reconstrucciones de hornos (nº de hornos, calendario, coste, capacidad antes/después).",
            "Familia Lambda no contrastada para Viscofan; estructura de P-M1 no delimitada con el desglose.",
        ],
    }
    ruta = SALIDA / "CALCULOS_PM1.json"
    ruta.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print("escrito", ruta.relative_to(RAIZ))
    for k, v in resultados_theta.items():
        print(k, "sumM", v["sum_M_miles_eur"], "theta", v["theta"])
    print("contraste", contraste["theta"])
    for k, lista in sensibilidad.items():
        for s in lista:
            print(k, "theta", s["theta"], "frac capacidad", s["fraccion_de_la_capacidad_publicada"])
    for tag, l in lambdas.items():
        print(tag, "rango lambda:", l["rango_L_8_16"])


if __name__ == "__main__":
    main()
