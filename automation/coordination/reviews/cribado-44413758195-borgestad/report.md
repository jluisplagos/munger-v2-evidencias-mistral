# Cribado · Borgestad

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-04 |
| Tarea | cribado-44413758195-borgestad |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 19d0c0230e54b3f6d1013c8a649e82c0db887a6f7555e3050b66713a91d714b9 |
| Huella del envío (bundle_sha256) | a6ab63af20535c4fcfdc6ab969ab255716fd63a14f915b855f5ec22c651fbefa |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 834829cc6ddff774cfee7bbcdbb4977c91457f9af197a9221b95c01157a58e31 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 132774 tokens |
| Reserva estimada antes de llamar | USD 1.186456 |
| Uso de tokens | entrada 60304, salida 3571 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.312636; cota 0.312636 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Borgestad/Borgestad_respuesta.md | 8fcab3429843d70d970af124afe0337f6004dddd37e567059f66667a6d1f4b3d | 32606 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Borgestad/Borgestad_evaluada.xlsx#Análisis | 1954f4438a652e7b09695d39ee0a783373d27fdaa1180ee50f7f22f4b2f4d2bc | 23135 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Borgestad/Borgestad_evaluada.xlsx#Control maestro | 7bdf6e2bb5e4eb56e99eceac47debe47db6479cf93cd258d953ee1e14d8306b5 | 56165 |

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

    Control maestro!M51 = 74.2 (arrendamientos NIIF 16 incluidos en la deuda total Análisis!C54 = 494.4, a 30/06/2026; subió desde 46,2 en el 1S26)


### Tipo de negocio y motor

    Holding con dos activos sin relación: refractarios e instalación industrial nórdica (cíclico, 93 % de los ingresos, con un 30,32 % de minoritarios) y un centro comercial en Polonia financiado con deuda sin recurso.
    Suma de partes: Agora Bytom a valor de activo menos su hipoteca sin recurso, el 69,68 % del refractario por su caja de ciclo medio y el coste de la matriz restado.

### calidad

    El ROCE del 7,1 % (máximo ajustado de 9,5 % en 2021–25) queda por debajo del 9 %, con un margen EBIT medio del refractario del ≈2,9 % en 2016–25, sin foso, con una cartera de pedidos de 106 frente a 145 y tres recapitalizaciones (≈413x acciones); se entiende, pero no es de calidad, así que discrepo del «✓ estables» de C27 y de la etiqueta «demasiado difícil» de A6.
    Dato clave: Análisis!C24 = 0.071

### caja

    La caja libre base es positiva (40,58) solo tras quitar el circulante y con un capex ≈0,6x la amortización, mientras que el FCF de 2021–25 fue −25,3/−83,8/110,5/116,1/−11,3 y la caja operativa fue nula o negativa en 6 de 10 años; además, la parte atribuible al accionista, neta del 30,32 % de minoritarios, ronda solo 27.
    Dato clave: Análisis!C52 = 40.58

### balance

    Sin arrendamientos, la deuda neta es ≈300,5 frente a un EBITDA que ya resta el alquiler de ≈103,5 (126,8 − 23,3), unas 2,9x, en línea con el 2,84–2,90x de la hoja y no con el 2,95x NIIF 16 de Análisis!C33; equivale a ≈7,4x la caja libre base de 40,58, con el préstamo de Agora (≈MEUR 27) venciendo el 31/12/2028; es mucho para un negocio cíclico, aunque es sin recurso salvo MEUR 5 y el LTV estimado es del ≈45 %.
    Dato clave: Control maestro!N51 = 420.2 (deuda bruta sin arrendamientos; neta 420.2 − caja 119.7 = 300.5)

### precio

    La cotización de 16,45 está por debajo del ponderado de la hoja (17,77; la respuesta decía ≈18,0 y manda la hoja) pero muy por encima del escenario malo (9,61), y con r +2 puntos el ponderado cae a 13,86; además, el DCF de grupo no aplica a este holding con minoritarios, y con la caja atribuible la propia respuesta estima ≈12, de modo que hace falta una suma de partes para concluir.
    Dato clave: Análisis!C43 = 17.7705710545193

### encaje

    El paquete no trae la cartera de la persona responsable; solo consta una liquidez muy baja, de ≈16.600 acciones al día, que no elimina en el cribado.
    Dato clave: Control maestro!N38 = 16600 (acciones/día de liquidez media)

### Qué lo cambiaría

    - Que Höganäs Borgestad sostenga un margen EBIT ≥10 % varios años con un ROCE del grupo por encima del 9 %.
    - Que Agora se venda cerca de su valor contable (726,9) y la deuda neta del grupo sin arrendamientos quede cerca de cero.
    - Que la caja libre sin circulante y neta de minoritarios crezca tres años seguidos con un capex al menos igual a la amortización.

### Qué falta

    - Tasación independiente de Agora y los términos de su refinanciación de 2028 (solo hay un valor en uso, con una holgura del ≈2,4 %).
    - Caja libre atribuible a Borgestad neta de minoritarios, medida por segmento (la hoja solo da una estimación de ≈27).
    - Capex de mantenimiento y de producción tras la venta de Bjuv, y los estados completos del tercer trimestre de 2026.

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

