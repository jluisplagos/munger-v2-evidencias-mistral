# Cribado · Tessenderlo

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-08 |
| Tarea | cribado-44512238939-tessenderlo |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | c0fc77abc1653b9755b9df9166c7baa46d7338d87d633b962227fef2206821af |
| Huella del envío (bundle_sha256) | 188f4887bbd81c6b3fe23f9c4bdb2b2e3961b19cbf65fd9015b526bfbed4f0df |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 76323d0502f500abe93d61f5fd0e0cf2053552df3f16643ec3d7150277e99be1 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 156327 tokens |
| Reserva estimada antes de llamar | USD 1.280668 |
| Uso de tokens | entrada 69958, salida 3985 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.359532; cota 0.359532 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Tessenderlo/Tessenderlo_respuesta.md | 33c46dc69bdc53bf319ff0dfae85d078cbc929c23a9d9affb2eb26ae0250c49f | 44461 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Tessenderlo/Tessenderlo_evaluada.xlsx#Análisis | 82838aa6d25102782c32dc2368236466ce0d879ca6de8c67b97cbaf6b791c206 | 24465 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Tessenderlo/Tessenderlo_evaluada.xlsx#Control maestro | 2e651e711a5fb8980256eb02515532534ece48c56e7e01257f15dcd3e6c8ed9f | 66329 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | no_pasa |
| caja | dudoso |
| balance | dudoso |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 58.9 (pasivo por arrendamientos IFRS 16 a 30-jun-2026)


### Tipo de negocio y motor

    Grupo industrial diversificado y cíclico ligado a materias primas (química agrícola de azufre, bio-valorización, soluciones industriales, telares y una central de gas), con el perímetro en cambio.
    Caja de ciclo medio del perímetro nuevo (sin el tolling de T-Power y con PB Leiner al 15%) combinada con una suma de partes que valore aparte la participación en FMC a mercado y la deuda con la que se financió.

### calidad

    El negocio se entiende de forma descriptiva (C11 = Sí), pero no muestra ventaja en las cifras. El ROCE LTM es del 4,6%, por debajo del WACC del 7,1-8,4% que usa la propia empresa. El margen de adjusted EBITDA del núcleo cae del 15,6% al 8,1% y la empresa depende de materias primas y del ciclo; por eso no lo clasifico como «demasiado difícil», como hizo la etapa 1, sino como de baja calidad.
    Dato clave: Análisis!C24 = 0.046

### caja

    La caja libre del accionista es positiva pero inestable y sin tendencia: 8,3–143,2 mm en 2016-2025, 66,2 mm LTM y base de 71,9 mm, que bajaría a 17,9 mm sin T-Power. La conversión de 2,49 que la hoja marca ✓ PASA refleja partidas no monetarias, no calidad, y el capex de mantenimiento no está identificado.
    Dato clave: Análisis!C40 = 66.2

### balance

    Sin arrendamientos, la deuda neta a 30-jun-2026 es de unos 19 mm (154,1 − 134,7), unas 0,1x el EBITDA ya neto de alquiler (≈245,9, aproximación de Control maestro!N36). Tras pagar ≈353,9 mm por FMC con financiación no publicada, la deuda neta pro forma sube a ≈373 mm: ≈1,5x EBITDA (≈2x sin T-Power) y ≈5,6x la caja libre LTM de 66,2, demasiado para un negocio cíclico, aunque la hoja marque ✓ PASA con 0,29x incluidos arrendamientos.
    Dato clave: Control maestro!N51 = 154.1 (deuda sin arrendamientos a 30-jun-2026; caja Análisis!C53 = 134.7)

### precio

    La cotización de 17,62 está muy por encima del precio de Sí (≈10,07, escenario malo) y casi igual al valor ponderado de 17,78. Con ±2 puntos de tasa el valor va de 13,9 a 24,6, de modo que el resultado cambia con la tasa. Además, el DCF de la plantilla no aplica (C62: la financiación cambia mucho), así que no sirve para concluir.
    Dato clave: Análisis!B78 = 10.0708087104629 (escenario malo / precio de Sí) frente a Análisis!C37 = 17.62

### encaje

    El paquete no trae la cartera de la persona responsable, y la hoja solo da contexto de mercado (capitalización de 1.039,5 mm), que no permite juzgar el encaje.
    Dato clave: Análisis!C41 = 1039.5

### Qué lo cambiaría

    - ROCE del perímetro nuevo sostenido por encima del 7,1-8,4% de coste de capital de la propia empresa durante dos ejercicios.
    - Caja libre del accionista de régimen por encima de 70 mm tras la salida de T-Power y PB Leiner.
    - Balance FY2026 que muestre una deuda neta sin arrendamientos por debajo de 1,5x el EBITDA tras FMC, con vencimientos holgados.

### Qué falta

    - Con qué se financiaron los ≈354 mm pagados por el ≈20% de FMC, y la deuda y los intereses resultantes en el balance de FY2026.
    - Reparto del capex entre mantenimiento y crecimiento, imprescindible para medir la caja libre de régimen.
    - Decisión sobre el uso de T-Power y efecto en caja de la sociedad conjunta de PB Leiner con Darling.

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

