# Cribado · Lifco

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-05 |
| Tarea | cribado-44505954250-lifco |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 96d79b608e3ad1c2d8ded47b5cf1eec066c30e9c6ef5dfe36c215912c6c23eeb |
| Huella del envío (bundle_sha256) | 216eadfbb0225a7f14eadd774700299751af797be5cb85d3f096849b3a9554cf |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 74269191409229245c12c286d780a973ac2c5ca7af75e8db206aad48d3c47940 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 133242 tokens |
| Reserva estimada antes de llamar | USD 1.188328 |
| Uso de tokens | entrada 59853, salida 4178 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.322972; cota 0.322972 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Lifco/Lifco_respuesta.md | b9de9a1f431f9e8fba60caf3c2629e7927a901dc20d951536bda76c1cef9836f | 33187 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Lifco/Lifco_evaluada.xlsx#Análisis | f5c5ef328c92ec4ee592af5e453eb3bd7bd498464b7779cea97c90bb614fe341 | 23257 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Lifco/Lifco_evaluada.xlsx#Control maestro | b12a857067acaf3d81217c2efaa92aec15f84cc5bb0d506524c50803574cd1bd | 56056 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | pasa |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M36 = 1624 (pasivos por arrendamiento a 30-sep-2026, incluidos en Análisis!C54 = 10951)


### Tipo de negocio y motor

    Grupo adquiridor de nichos B2B (dental, demolición y herramientas, sistemas industriales) con 275 filiales descentralizadas, en parte expuesto al ciclo industrial.
    DCF al accionista con la caja libre antes de compras más el valor explícito de la reinversión (orgánico más adquisiciones a ≈7x EBITA con su rendimiento en caja), restando la deuda neta y el put/call de minoritarios que la plantilla no descuenta.

### calidad

    Es un negocio comprensible, con ROCE del 20,5% con goodwill, margen EBITA estable en torno al 22% y 275 filiales sin ningún cliente por encima del 6%. Discrepo del veredicto «DESCARTAR · demasiado difícil» de Análisis!A6, que nace de C13 = No (el valor no se ve sin modelo) y no de que el negocio no se entienda. Pesan el orgánico débil y un ROCE tras impuestos del 12,8%, poco por encima del 9%.
    Dato clave: Análisis!C24 = 0.205

### caja

    La caja libre base es positiva, de 3.909 m (CFO 4.737 − capex 520 − arrendamientos 308), y sube a 4.708 m en el LTM. La conversión CFO/beneficio es de 1,3 y el FCF crece todos los años 2016–2025, aunque el 92% de la caja libre se reinvierte en compras.
    Dato clave: Análisis!C52 = 3909

### balance

    Sin arrendamientos, la deuda neta es de 7.945 m frente a un EBITDA que ya resta el alquiler de unos 7.184 m (7.584 − ≈400, aproximación de la hoja), es decir ≈1,1x (1,5x sumando el put/call de 2.718 m), y ≈2,0x la caja libre base de 3.909 m; es holgado para un negocio diversificado, aunque la caja solo cubre 0,19x la deuda a corto de 7.226 m y depende de refinanciar. El 1,26x de Análisis!C33 incluye arrendamientos y no se usa tal cual.
    Dato clave: Control maestro!M36 = 9328 (préstamos y bonos sin arrendamientos); deuda neta sin arrendamientos 9328 − Análisis!C53 1383 = 7945

### precio

    La cotización de 289,2 SEK está muy por encima del precio de Sí de ≈120,8 SEK y del ponderado de 197,3 SEK; solo iguala el escenario bueno (294,0). El precio descuenta un 12,5% anual de crecimiento, y aun con r al 7% el ponderado (294,6) apenas alcanza la cotización: la conclusión respecto al precio de Sí no cambia con ±2 puntos de tasa.
    Dato clave: Análisis!C37 = 289.2 frente a Análisis!B78 = 120.801978271237 (precio de Sí = mín(120,8; 0,75 × 197,33 = 148,0))

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja no dice nada concreto de encaje, más allá de un 50,5% del capital en manos de insiders, que no sirve para este filtro.
    Dato clave: Análisis!C96 = 0.505 (contexto de control, no de cartera)

### Qué lo cambiaría

    - Una cotización en el entorno de 121 SEK o por debajo (Análisis!B78) con el motor de compras intacto llevaría a estudiar a fondo.
    - Múltiplos de compra por encima de 10x EBITA o un ROCE con goodwill por debajo del 18% de forma sostenida rebajarían la calidad y llevarían a descartar.
    - Una deuda neta sin arrendamientos por encima de unas 3x el EBITDA, o problemas para refinanciar la deuda a corto de 7.226 m, harían fallar el balance.

### Qué falta

    - Control maestro C46/C47/C49 citan una «decisión del inversor (10-nov-2026)», posterior a la fecha de la hoja (5-nov-2026): hay que confirmar la base de FCF de 3.909 m a la fecha de corte.
    - El EBITDA sin arrendamientos es una aproximación de la hoja (−400 m), y no constan el calendario de vencimientos de la deuda a corto (7.226 m) ni los umbrales de covenants.
    - No constan el precio pagado ni el resultado posterior de cada adquisición, que es la variable que decide el valor.

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

