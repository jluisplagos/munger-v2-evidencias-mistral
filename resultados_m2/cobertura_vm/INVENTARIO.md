# Inventario del frente A · cobertura integral M2

Evidencia propuesta por Mistral; pendiente de revisión e incorporación por el integrador.

## Alcance fijado

- Entradas: **677** (Vidrala 347, Viscofan 330); piloto reutilizado: 60; nuevas: 617.
- Clases: cero_comprobado=13, convencion=35, dato_ausente=6, dato_publicado=454, derivado=101, hipotesis=52, no_aplicable=16.
- Derivados: 101 en total (14 del piloto, 87 nuevos).
- Historia: 161 entradas por empresa.
- Catálogo `entrada/catalogo_entradas.csv` coincide con el registro: True; coincide con `configuracion.json`: {'entradas': True, 'piloto': True, 'nuevas': True, 'derivados': True, 'derivados_piloto': True, 'por_clase': True}.

## Fuentes disponibles y faltantes

| empresa | archivo | estado | entradas que la citan |
|---|---|---|---|
| Vidrala | `texto/CF_2017.txt` | CONFORME (huella_ok=True) | 21 |
| Vidrala | `texto/CF_2018.txt` | CONFORME (huella_ok=True) | 19 |
| Vidrala | `texto/CF_2019.txt` | CONFORME (huella_ok=True) | 22 |
| Vidrala | `texto/CF_2020.txt` | CONFORME (huella_ok=True) | 26 |
| Vidrala | `texto/CF_2021.txt` | CONFORME (huella_ok=True) | 22 |
| Vidrala | `texto/CF_2022.txt` | CONFORME (huella_ok=True) | 23 |
| Vidrala | `texto/CF_2023.txt` | CONFORME (huella_ok=True) | 26 |
| Vidrala | `texto/CF_2024.txt` | CONFORME (huella_ok=True) | 22 |
| Vidrala | `texto/CF_2025.txt` | CONFORME (huella_ok=True) | 55 |
| Vidrala | `texto/ES_2024_informacion_financiera_consolidada.txt` | CONFORME (huella_ok=True) | 1 |
| Vidrala | `texto/ES_2025_informacion_financiera_consolidada.txt` | CONFORME (huella_ok=True) | 4 |
| Viscofan | `fuentes_mercado/BMadrid_boletin_20261103_seccion_16.txt` | CONFORME (huella_ok=True) | 1 |
| Viscofan | `texto/AR_2017.txt` | CONFORME (huella_ok=True) | 18 |
| Viscofan | `texto/AR_2019.txt` | CONFORME (huella_ok=True) | 21 |
| Viscofan | `texto/AR_2020.txt` | CONFORME (huella_ok=True) | 25 |
| Viscofan | `texto/AR_2025.txt` | CONFORME (huella_ok=True) | 59 |
| Viscofan | `texto/CA_2023_es.txt` | CONFORME (huella_ok=True) | 20 |
| Viscofan | `texto/CF_2021.txt` | CONFORME (huella_ok=True) | 18 |
| Viscofan | `texto/CF_2022_compilacion.txt` | CONFORME (huella_ok=True) | 22 |
| Viscofan | `texto/CF_2024.txt` | CONFORME (huella_ok=True) | 25 |
| Viscofan | `texto/IA_2018_es.txt` | CONFORME (huella_ok=True) | 20 |

Selección de insumos: 251 archivos conformes con huella verificada y 29 PDF candidatos en `.trabajo/insumos_m2` (**selección parcial; producto completo no verificado**).

## Dependencias de los derivados

- Nodos con derivación: 101; orígenes que no existen en el registro (huecos): 0.

## Plan finito de lotes (≤30 entradas)

| lote | tipo | n | empresa(s) | documento |
|---|---|---|---|---|
| L00 | PILOTO_M1_REUTILIZADA | 60 | Vidrala,Viscofan | `—` |
| L01 | NUEVO | 30 | Vidrala | `—` |
| L02 | NUEVO | 30 | Vidrala | `—` |
| L03 | NUEVO | 30 | Vidrala | `—` |
| L04 | NUEVO | 30 | Vidrala | `—` |
| L05 | NUEVO | 30 | Vidrala | `texto/CF_2018.txt` |
| L06 | NUEVO | 30 | Vidrala | `texto/CF_2019.txt` |
| L07 | NUEVO | 30 | Vidrala | `texto/CF_2020.txt` |
| L08 | NUEVO | 30 | Vidrala | `texto/CF_2022.txt` |
| L09 | NUEVO | 30 | Vidrala | `texto/CF_2023.txt` |
| L10 | NUEVO | 30 | Vidrala | `texto/CF_2024.txt` |
| L11 | NUEVO | 30 | Vidrala,Viscofan | `texto/CF_2025.txt` |
| L12 | NUEVO | 30 | Viscofan | `—` |
| L13 | NUEVO | 30 | Viscofan | `—` |
| L14 | NUEVO | 30 | Viscofan | `—` |
| L15 | NUEVO | 30 | Viscofan | `texto/AR_2017.txt` |
| L16 | NUEVO | 30 | Viscofan | `texto/AR_2019.txt` |
| L17 | NUEVO | 30 | Viscofan | `texto/AR_2025.txt` |
| L18 | NUEVO | 30 | Viscofan | `texto/AR_2025.txt` |
| L19 | NUEVO | 30 | Viscofan | `texto/CF_2021.txt` |
| L20 | NUEVO | 30 | Viscofan | `texto/CF_2022_compilacion.txt` |
| L21 | NUEVO | 17 | Viscofan | `texto/IA_2018_es.txt` |

Todas las comprobaciones se reproducen con los scripts de `scripts/`; los cálculos numéricos usan `Decimal`.
