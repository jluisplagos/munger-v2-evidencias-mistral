#!/usr/bin/env python3
"""Genera `casos_fijados.json` a partir de los insumos verificados (solo lectura en
`.trabajo/insumos_m2/`, extraídos del ZIP base-4.14 con sha256 `bb51942c…b7b93e`).

Los casos fijados son:
  - A1–A5: los cinco casos del Anexo C §C.5 (entradas publicadas en el documento; los
    valores esperados NO se toman de ahí ni del código: los calcula el oráculo propio).
  - S1–S7: casos sintéticos propios (masas cero, valores repetidos, negativos, orden,
    k < 1, p inválidas, n = 2).
  - H1–H5: casos históricos fijados de los expedientes conservados (vectores V, p, k y
    precio publicados en los JSON del paquete, con su ruta y sha256).
  - V-Vidrala-4.14 / V-Viscofan-4.14: los vectores de TODAS las variantes calculadas de
    `configuracion_v64_variantes.json` (4.14), para contrastar el precio de Sí variante
    a variante.

Uso: python3 generar_casos_fijados.py   (escribe ../casos_fijados.json junto a este script)
"""
import hashlib
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
INSUMOS = os.path.join(REPO, ".trabajo", "insumos_m2")
COMMIT_PRODUCTO = "059f4f68dca7acf465b5f5b21de2dede84c885ff"
ZIP_SHA256 = "bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e"

E414 = "personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14"
E413 = "personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_13"


def sha256_rel(rel):
    with open(os.path.join(INSUMOS, rel), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def prov(rel):
    return {"ruta": rel, "sha256": sha256_rel(rel), "commit_producto": COMMIT_PRODUCTO,
            "zip_base_4_14_sha256": ZIP_SHA256}


def leer(rel):
    with open(os.path.join(INSUMOS, rel), encoding="utf-8") as f:
        return json.load(f)


def vector_de_variantes(rel):
    """[(clave, V, precio_si_publicado, zona, parametros_variados)] de un variantes.json."""
    d = leer(rel)
    out = []
    for v in d.get("variantes") or []:
        V = v.get("V") or v.get("valores")
        out.append({"clave": v.get("clave"), "V": V, "p": (d.get("vector_escenarios_activa") or {}).get("probabilidades"),
                    "k": d.get("k"), "precio": d.get("precio"),
                    "precio_si_publicado": v.get("precio_si"), "zona_publicada": v.get("zona"),
                    "parametros_variados": v.get("parametros_variados")})
    return out, d.get("k"), d.get("precio"), prov(rel)


def main():
    casos = {"meta": {"commit_producto": COMMIT_PRODUCTO, "zip_base_4_14_sha256": ZIP_SHA256,
                      "generado_por": "codigo/generar_casos_fijados.py",
                      "nota": "Entradas fijadas; los esperado los calcula el oráculo propio, nunca el código del producto."},
             "anexo_c": [], "sinteticos": [], "historicos": [], "variantes": []}

    anexo = "personaje_v2/ANEXO_C_precio_de_si.md"
    casos["anexo_c"] = [
        {"id": "A1", "V": ["60", "100", "150"], "p": ["1/4", "1/2", "1/4"], "k": "3",
         "v_normal": "100", "precio": "90", "proveniencia": prov(anexo),
         "nota": "Anexo C §C.5 caso 1 (tramo [MALO, NORMAL])"},
        {"id": "A2", "V": ["90", "100", "160"], "p": ["1/5", "3/5", "1/5"], "k": "3",
         "v_normal": "100", "precio": "95", "proveniencia": prov(anexo),
         "nota": "Anexo C §C.5 caso 2 (tramo [NORMAL, BUENO]; tope NORMAL)"},
        {"id": "A3", "V": ["100", "100", "100"], "p": ["1/5", "3/5", "1/5"], "k": "3",
         "v_normal": "100", "precio": "100", "proveniencia": prov(anexo),
         "nota": "Anexo C §C.5 caso 3 (degenerado)"},
        {"id": "A4", "V": ["-20", "80", "200"], "p": ["1/5", "3/5", "1/5"], "k": "3",
         "v_normal": "80", "precio": "50", "proveniencia": prov(anexo),
         "nota": "Anexo C §C.5 caso 4 (MALO negativo; sin precio del escenario MALO)"},
        {"id": "A5", "V": ["40", "70", "300"], "p": ["3/10", "1/2", "1/5"], "k": "3",
         "v_normal": "70", "precio": "80", "proveniencia": prov(anexo),
         "nota": "Anexo C §C.5 caso 5 (tope NORMAL)"},
    ]

    casos["sinteticos"] = [
        {"id": "S1", "V": ["50", "100", "150"], "p": ["0", "1/2", "1/2"], "k": "3",
         "v_normal": "100", "precio": "100",
         "nota": "masa cero en el MALO: no arrastra a P* (bound relevante: min con p > 0)"},
        {"id": "S2", "V": ["100", "100", "200"], "p": ["1/5", "3/5", "1/5"], "k": "3",
         "v_normal": "100", "precio": "110",
         "nota": "dos valores iguales (masa agregada 4/5 en 100)"},
        {"id": "S3", "V": ["-50", "-10", "0"], "p": ["1/5", "3/5", "1/5"], "k": "3",
         "v_normal": "-10", "precio": "-20",
         "nota": "valores todos ≤ 0: la matemática admite P* negativo; el producto rechaza precio ≤ 0"},
        {"id": "S4", "V": ["150", "60", "100"], "p": ["1/4", "1/4", "1/2"], "k": "3",
         "v_normal": "100", "precio": "90",
         "nota": "entrada desordenada: el oráculo ordena (invariancia por permutación); el producto exige B78≤C78≤D78 (error G19)"},
        {"id": "S5", "V": ["60", "100", "150"], "p": ["1/4", "1/2", "1/4"], "k": "1/2",
         "v_normal": "100", "precio": "110",
         "nota": "k < 1: matemáticamente P* > ponderado; el producto rechaza k < 1 (guarda de política)"},
        {"id": "S6", "V": ["60", "100", "150"], "p": ["1/5", "3/5", "3/10"], "k": "3",
         "v_normal": "100", "precio": "90", "espera_dominio_error": True,
         "nota": "p no suma 1: fuera del dominio; el producto también se niega (|Σp−1| > 1e-3)"},
        {"id": "S7", "V": ["80", "120"], "p": ["1/2", "1/2"], "k": "3",
         "v_normal": "120", "precio": "100",
         "nota": "n = 2 escenarios: el oráculo es general; el producto está cableado a n = 3"},
    ]

    vid414 = f"{E414}/vidrala_decisiones/Vidrala"
    vis414 = f"{E414}/viscofan_decisiones/Viscofan"
    vis413 = f"{E413}/viscofan/Viscofan"
    vis412 = f"{E413}/viscofan/antecedentes/ejecucion_1_4_13"

    def hist(id_, rel_precio, rel_variantes, clave_variante, nota):
        precio = leer(rel_precio)
        d = leer(rel_variantes)
        va = d.get("vector_escenarios_activa") or {}
        v = next((x for x in d.get("variantes") or [] if x.get("clave") == clave_variante), None)
        V = (v or {}).get("V") or va.get("V")
        return {"id": id_, "V": [repr(x) for x in V],
                "p": [repr(x) for x in (va.get("probabilidades") or precio.get("p"))],
                "k": repr(d.get("k") if d.get("k") is not None else precio.get("k")),
                "v_normal": repr(V[1]), "precio": repr(precio.get("precio")),
                "precio_si_publicado": (v or {}).get("precio_si", precio.get("precio_si")),
                "zona_publicada": (v or {}).get("zona", precio.get("zona")),
                "P_estrella_publicado": precio.get("P_estrella"),
                "proveniencia": {**prov(rel_precio), "variantes": prov(rel_variantes)},
                "nota": nota}

    casos["historicos"] = [
        hist("H1", f"{vid414}/precio.json", f"{vid414}/configuracion_v64_variantes.json", "activa",
             "Vidrala 4.14 expediente final, variante activa (precio 90,10 € a 31-dic-2025, zona publicada «caro»)"),
        hist("H2", f"{vis414}/precio.json", f"{vis414}/configuracion_v64_variantes.json", "activa",
             "Viscofan 4.14 expediente final, variante activa (precio 54,70 €, p = 0,20/0,60/0,20, zona «caro»)"),
        hist("H3", f"{vis413}/configuracion_v64_variantes.json", f"{vis413}/configuracion_v64_variantes.json", "activa",
             "Viscofan 4.13 activa (p = 0,20/0,60/0,20); precio de la entrega 4.13"),
        hist("H4", f"{vis412}/configuracion_v64_variantes.json", f"{vis412}/configuracion_v64_variantes.json", "activa",
             "Viscofan 4.12 (antecedente ejecucion_1_4_13) activa, p = 0,25/0,60/0,15 (desviación de la referencia)"),
        hist("H5", f"{vis412}/configuracion_v64_variantes.json", f"{vis412}/configuracion_v64_variantes.json", "perimetro_alternativo",
             "Viscofan 4.12 variante «perímetro Caja» (p = 0,25/0,60/0,15); base de la descomposición D7"),
        hist("H6", f"{vis413}/configuracion_v64_variantes.json", f"{vis413}/configuracion_v64_variantes.json", "perimetro_alternativo",
             "Viscofan 4.13 variante «perímetro Caja» (p = 0,20/0,60/0,20, p de referencia); añadido tras la revisión externa C1: D7 compara el perímetro Caja entre entregas"),
    ]

    # Etiquetas de perímetro por caso (de los expedientes publicados): la activa de
    # Viscofan declara perímetro NIIF 16 en 4.14; «perimetro_alternativo» es «Caja».
    casos["perimetros"] = {
        "H1": "Vidrala 4.14 activa (perímetro declarado en su configuracion_economica.json)",
        "H2": "Viscofan 4.14 activa · perímetro NIIF 16 (configuracion_economica.json 4.14)",
        "H3": "Viscofan 4.13 activa · NIIF 16 (perímetro vigente; D4 del paquete)",
        "H4": "Viscofan 4.12 activa (ejecucion_1_4_13) · NIIF 16 (perímetro vigente; D4 del paquete)",
        "H5": "Viscofan 4.12 variante perimetro_alternativo · Caja",
        "H6": "Viscofan 4.13 variante perimetro_alternativo · Caja",
        "nota": "La comparación D7 («+1,5386 €») es la de perímetro Caja (H5→H6); la de activa NIIF 16 (H4→H3) es otra pregunta (+1,5478 €). Nunca mezclar perímetros en un mismo cambio total.",
    }

    for tag, rel in (("V-Vidrala-4.14", f"{vid414}/configuracion_v64_variantes.json"),
                     ("V-Viscofan-4.14", f"{vis414}/configuracion_v64_variantes.json")):
        filas, k, precio, p = vector_de_variantes(rel)
        casos["variantes"].append({"grupo": tag, "k": k, "precio": precio, "filas": filas, "proveniencia": p})

    # vectores de probabilidades de referencia / desviación (fase_b publicados)
    casos["probabilidades_referencia"] = {
        "referencia_mecanica": [0.2, 0.6, 0.2],
        "desviacion_4_12": [0.25, 0.6, 0.15],
        "proveniencia": {
            "fase_b_vidrala_4_14": prov(f"{vid414}/fase_b.json"),
            "fase_b_viscofan_4_14": prov(f"{vis414}/fase_b.json"),
            "fase_b_viscofan_4_13": prov(f"{vis413}/fase_b.json"),
            "fase_b_viscofan_4_12": prov(f"{vis412}/fase_b.json"),
            "fase_b_viscofan_4_12_sufijo": prov(f"{E413}/viscofan/antecedentes/fase_b.json.4_12"),
        },
        "nota": "En todas las fases B publicadas, referencia_mecanica = 0,2/0,6/0,2; la 4.12 se desvió a 0,25/0,6/0,15 (desviacion ±0,05, clase «fundamentada»); la 4.13 y la 4.14 vuelven a la referencia.",
    }

    destino = os.path.join(AQUI, "..", "casos_fijados.json")
    with open(destino, "w", encoding="utf-8") as f:
        json.dump(casos, f, ensure_ascii=False, indent=1)
    n = (len(casos["anexo_c"]) + len(casos["sinteticos"]) + len(casos["historicos"])
         + sum(len(g["filas"]) for g in casos["variantes"]))
    print(json.dumps({"casos_fijados": n, "destino": os.path.normpath(destino)}, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
