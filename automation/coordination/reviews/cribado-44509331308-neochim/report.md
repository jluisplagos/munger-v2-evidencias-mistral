# Cribado · Neochim

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-07 |
| Tarea | cribado-44509331308-neochim |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 5bb5eb618e93107ed4ca31eef4387dcbec6173953db2672a406953bb6d3382b2 |
| Huella del envío (bundle_sha256) | 0e680367dfe582634bdfc997035f869a68de964e71987f6bc59161b5b8794d29 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 14f609c1c7fc21ed3350de6bf0a5f094148b3ce59b721ce9df18be808f757c8b |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 128598 tokens |
| Reserva estimada antes de llamar | USD 1.169752 |
| Uso de tokens | entrada 57761, salida 3305 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.297144; cota 0.297144 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Neochim/Neochim_respuesta.md | 73227f309087a1a999ca0a15522fc6c7759045cc6ff2b190067f45fed56578cc | 34836 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Neochim/Neochim_evaluada.xlsx#Análisis | cab9395b38f8885ba1996e6c836ba992c2167e97960b525ba15201af21d96708 | 23399 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Neochim/Neochim_evaluada.xlsx#Control maestro | 9efecbd08bbda620b515a20f8cdd73617249682bc9f23526f04b0657684eebce | 49699 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | no_pasa |
| caja | no_pasa |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Análisis!C54 = 0.743 (0,324 a corto y 0,419 a largo plazo, según Control maestro!M51)


### Tipo de negocio y motor

    Productor cíclico de materias primas: fertilizantes nitrogenados (amoníaco y nitrato amónico) a partir de gas natural, con una sola planta en Bulgaria.
    Caja o beneficio normalizado de ciclo completo con un capex de mantenimiento realista, con el valor de liquidación del balance (caja menos compromisos y pasivos sociales) como suelo.

### calidad

    El negocio se entiende: un diferencial nitrato–gas–CO2 en una sola planta de 1987. No es de calidad: no tiene foso, tuvo pérdidas operativas en 4 de 11 años y el ROCE de ciclo es del 8,8 % a 10 años (el 0,203 de C24 es LTM), y ventas de ≈46–47 % de los ingresos a un accionista en 2023–2024 y una asignación de capital «Dudosa» (Análisis!C98).
    Dato clave: Análisis!C24 = 0.203

### caja

    La caja libre no es recurrente. La base de 6,447 mm es la media de 2021–2025 y en 3 años es de −6,61. El FCF anual osciló entre −77.943 y +57.888 miles BGN, con 4 de 10 años en FCF ≤0, y el capex/D&A de 0,43x apunta a un mantenimiento infraestimado, aunque la conversión CFO/beneficio sea de 1,04 (Análisis!C26).
    Dato clave: Análisis!C52 = 6.447

### balance

    Sin arrendamientos, la deuda financiera es 0 frente a una caja de 40,694 mm. La caja neta da unos −1,9x sobre un EBITDA LTM de 21,69 menos el alquiler, de modo que el balance pasa. El −1,84x de Análisis!C33 incluye los arrendamientos de 0,743 y no se usa tal cual. Hay dos matices: el dividendo comprometido de 5,326 y un programa de inversión de 97.957 (unidad no indicada) que se financiará con préstamos.
    Dato clave: Deuda sin arrendamientos = 0 (bancos 0 según Control maestro!M51); Análisis!C53 = 40.694

### precio

    La cotización de 14,5 € está justo por debajo del escenario malo (14,71 €), que la respuesta toma como precio de Sí, y muy por debajo del ponderado de 35,31 €. Aun así, el DCF de la plantilla no aplica a una commodity cíclica, por lo que el resultado es dudoso: haría falta valorar con caja de ciclo medio y valor de liquidación, y con r+2 puntos el ponderado ya baja a 27,63 €.
    Dato clave: Análisis!C37 = 14.5 frente a Análisis!B78 = 14.7057810816333

### encaje

    El paquete no trae la cartera; la hoja solo indica un 0 % ligado al cubo de etapa 1, que no hereda este filtro, y el encaje nunca elimina en el cribado.
    Dato clave: Análisis!C104 = 0 % · Demasiado difícil · sin posición

### Qué lo cambiaría

    - Que se conozca un capex de mantenimiento bajo y la caja libre se mantenga positiva a lo largo de un valle completo como 2023–2024.
    - Que se demuestre que las ventas a partes vinculadas se hicieron a precio de mercado.
    - Que la junta apruebe un reparto extraordinario de la caja o una recompra.

### Qué falta

    - Capex de mantenimiento real y unidad del programa de inversión 2026–2030 (97.957), y qué parte es mantenimiento.
    - Condiciones de las ventas a Euro Fert (≈46–47 % de los ingresos en 2023–2024) frente a terceros, y causa de las reexpresiones de 2021–2024.
    - Cotización actualizada: Análisis!C37 procede de una fuente secundaria marcada ACTUALIZAR y la liquidez es muy baja.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro balance: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

