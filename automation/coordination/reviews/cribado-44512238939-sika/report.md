# Cribado · Sika

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-07 |
| Tarea | cribado-44512238939-sika |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 21fa33751a191ed666ad48866658f856968a5a84fd96d797e3693cd6e69643e6 |
| Huella del envío (bundle_sha256) | 53b67755e16744466da284dd731edad36b08106f0039f4a25078014cd864a7ee |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 2a166e244ab66f8938653ddeb7194954b44fa43dff70d06fd996667654a5f42f |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 145654 tokens |
| Reserva estimada antes de llamar | USD 1.237976 |
| Uso de tokens | entrada 65951, salida 4188 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.347564; cota 0.347564 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Sika/Sika_respuesta.md | 3e2e764515e58eb37ec9d0ecbea8bd2ebe1298634e4f7f38164c7af7359ba2ca | 36677 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Sika/Sika_cambios_v2.md | f8e038a1e24f098cebae9535f984a838faa2fcf1964d4451e93214c184bbf8b5 | 5348 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Sika/Sika_evaluada.xlsx#Análisis | 06e541f6155b65e8aea64b5592792946d757995a036a93351f0c98a94af602e8 | 23963 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Sika/Sika_evaluada.xlsx#Control maestro | 33a251f715bdd826385ca5de906fd51f34caee6a387deae68c614dd1565ca0ed | 58629 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | dudoso |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 455.4 (a 30-jun-2026; incluido en la deuda total de 6.098,1 y en el 2,65x de C33)


### Tipo de negocio y motor

    Química especializada para construcción (85 % de las ventas) e industria; negocio de márgenes estables pero ligado al ciclo de la construcción y con crecimiento apoyado en compras financiadas con deuda (Parex, MBCC).
    El DCF de caja libre de la plantilla, contrastado con una caja libre de ciclo medio por la exposición a la construcción (85 % de las ventas) y sin contar como crecimiento orgánico el que viene de compras.

### calidad

    El negocio se entiende y tiene márgenes estables (margen de materiales del 49–55 % y EBITDA del 18–19 %), pero el ROCE antes de impuestos ha caído del 28,7 % (2016) al 12,0 %, con un ROIC después de impuestos con goodwill del 9,3 %, casi igual a la tasa del 9 %; el «demasiado difícil» de A6 viene de C13 = No y no de que el negocio no se entienda.
    Dato clave: Análisis!C24 = 0.1201

### caja

    La caja libre de la plantilla (ya neta de intereses, principal de arrendamientos y SBC) es de 1.117,9 mn de media FY23–25, positiva y con una conversión CFO/beneficio de 1,32x, aunque baja de 1.105,9 (FY24) a 1.025,4 en el LTM a 30-jun-2026.
    Dato clave: Análisis!C52 = 1117.9

### balance

    El 2,65x de Análisis!C33 incluye 455,4 de arrendamientos y no sirve tal cual; sin ellos la deuda neta es unos 4.997 mn, alrededor de 2,6–2,7x un EBITDA que resta el alquiler (la hoja da un 2,62x aproximado) y unas 4,5x la caja libre base de 1.117,9, por encima del objetivo propio de 1,3–2,3x, con la caja cubriendo solo 0,40x los 1.547,1 de pasivos financieros corrientes, un vencimiento de 921,8 el 03-nov-2026 y el precio de Akkim y la clasificación del híbrido sin publicar.
    Dato clave: Control maestro!N51 = 5642.7 (deuda bruta sin arrendamientos; deuda neta sin arrendamientos ≈ 4997.2 = 5452.6 − 455.4, Control maestro!M36)

### precio

    La cotización de 175,5 CHF supera el precio de Sí (unos 84,5 CHF, el escenario malo de B78), el valor ponderado de 120,8 y hasta el escenario bueno de 166,4; ni a r = 7 % (172,3) llega, y el DCF inverso exige un crecimiento del 9,3 %.
    Dato clave: Análisis!C83 = 120.80882070884 (frente a la cotización de Análisis!C37 = 175.5)

### encaje

    El paquete no trae la cartera, y la hoja solo recoge un tamaño de 0 %, que es una decisión de cartera de la etapa 1 y no un dato de encaje.
    Dato clave: Análisis!C104 = 0% · Watchlist (dato de la etapa 1, no se usa)

### Qué lo cambiaría

    - Una cotización en torno a 85–90 CHF o menos (escenario malo de Análisis!B78 = 84,5) con el negocio intacto pasaría a estudiar a fondo.
    - Una deuda neta sin arrendamientos por encima de 3x un EBITDA que reste el alquiler, una vez incluidos Akkim y el híbrido, llevaría a descartar.
    - Un ROCE de FY26 por debajo del 11 % (descartar) o una vuelta por encima del 14 % con orgánico de al menos el 4 % (calidad pasa).

### Qué falta

    - El precio de Akkim (cerrada el 03-sep-2026) y la clasificación IFRS del híbrido de EUR 1.000 mn de ago-2026, sin los que no se conoce la deuda neta posterior al balance.
    - Un EBITDA que reste el alquiler: la hoja solo da un 2,62x aproximado sin arrendamientos.
    - Los competidores, la concentración de clientes y el retorno real de MBCC (sinergias más allá de los 41 mn) para juzgar la calidad.

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

