# Cribado · Heidelberg

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-25 |
| Tarea | cribado-44502520327-heidelberg |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | ef4530bf99ddb7c81d00dfb98744d879ca7c93d1073681031162e2b38eac6df8 |
| Huella del envío (bundle_sha256) | a6d825111b43c9d7424c8f3dbfd1f80902c3243b2f8097dcef87bed643703081 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 28f4f5a371b06bc8fa98023d21382d3cb5b4e566dfca9968a9791b01b584ce78 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 181477 tokens |
| Reserva estimada antes de llamar | USD 1.381268 |
| Uso de tokens | entrada 80278, salida 4507 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.411252; cota 0.411252 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Heidelberg/Heidelberg_respuesta.md | 7040caaebe02f5be9cd0f43240a36fbe1faf29a4140f788c9eadc3e3a76111ba | 58392 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Heidelberg/Heidelberg_evaluada.xlsx#Análisis | b34ff1847636179887069de25609c98e0aee983c1a5bea0f5066043da03bd719 | 24939 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Heidelberg/Heidelberg_evaluada.xlsx#Control maestro | 6e8fd1429247678c49dbc3032002c178db97079424a4d936a539f2fd5b4799e8 | 77172 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 (desglose de Análisis!C54) = 1206.3 M€ a 30-jun-2026


### Tipo de negocio y motor

    Cíclico de materiales de construcción con producto homogéneo (cemento, áridos, hormigón, asfalto), con mercados locales por flete y expuesto a la energía y al precio del CO2.
    Caja libre de ciclo medio (margen y volumen normalizados por energía y CO2), contrastada con el P/FCF histórico, en lugar de proyectar el FCF de la parte alta del ciclo.

### calidad

    El negocio se entiende (Análisis!C11 = Sí): cemento y áridos con un foso local por flete; pero el ROIC del 10,4% apenas supera el ~8,6% de coste de capital estimado, el margen RCOBD (17-22%) depende de la energía, no hay crecimiento orgánico de volumen y el fondo de comercio es el 24,5% del activo; es un negocio comprensible de calidad media, no «demasiado difícil» como dice la hoja.
    Dato clave: Análisis!C24 = 0.104

### caja

    La caja libre del accionista es positiva todos los años (de 724 a 1.787 M€ entre 2019 y 2025, 1.505 LTM) y la conversión CFO/beneficio es de 1,49x, aunque está plana o a la baja desde 2023, la conversión cae del 51% al 41,2% y el semestre de 2026 da −413 M€ (estacional).
    Dato clave: Análisis!C52 = 1685.5

### balance

    El 1,66x de Análisis!C33 incluye 1.206,3 M€ de arrendamientos y no sirve tal cual; sin ellos la deuda neta es de 6.520,2 M€, ≈1,5x un EBITDA pre-NIIF 16 aproximado (no publicado) y ≈3,9x la caja libre base de 1.685,5 M€; pro forma Maas (~1.000) y recompras (~346) sube a ≈1,8x, holgado para un cíclico con rating BBB/Baa2, sin covenants y con una RCF de 2.000 M€ hasta 2029.
    Dato clave: Control maestro!M36: deuda neta 7726.5 − arrendamientos 1206.3 = 6520.2 M€ sin arrendamientos (≈1,50x el EBITDA pre-NIIF 16 aproximado, unos 4.337 M€)

### precio

    A 147,80 € (Análisis!C37) la cotización está un 30% por encima del escenario malo (114,07 €) y del precio de Sí de la etapa 1 (114 €) y a 15,2x la caja libre base, frente a una mediana histórica de 10,8x (Análisis!C88); como el FCF base recoge márgenes altos del ciclo, una caja de ciclo medio la haría aún más cara, y con r al 8% el precio de Sí (130 €) sigue por debajo.
    Dato clave: Análisis!B78 = 114.070625482156

### encaje

    El paquete no trae la cartera de la persona responsable; solo consta una capitalización de 25.661,9 M€, que no dice nada del encaje.
    Dato clave: Análisis!C41 = 25661.9

### Qué lo cambiaría

    - Una cotización igual o inferior a ~114 € (Análisis!B78) llevaría a estudiar a fondo.
    - Una deuda neta sin arrendamientos por encima de ~2,5x el EBITDA pre-NIIF 16 tras pagar Maas, o el margen RCOBD por debajo del 19% dos ejercicios, llevaría a descartar.
    - Un ROIC después de impuestos sostenido por encima del 12% con la energía normalizada haría pasar el filtro de calidad.

### Qué falta

    - EBITDA sin NIIF 16 publicado: el 1,50x sin arrendamientos de la hoja es una aproximación; faltan además el saldo de factoring y los volúmenes en toneladas para normalizar la caja de ciclo medio.
    - Fechas incoherentes: la decisión del inversor sobre el FCF base (Control maestro, filas 40 y 43) está fechada el 28-oct-2026, después de la fecha de la hoja (25-oct-2026).
    - El precio viene de fuentes secundarias (la hoja pide actualizarlo), los resultados de 9M 2026 son posteriores a la hoja y falta el valor de Simply Wall St (Análisis!C38 vacía).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

