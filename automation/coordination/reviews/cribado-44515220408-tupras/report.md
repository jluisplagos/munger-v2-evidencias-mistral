# Cribado · Tupras

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-01 |
| Tarea | cribado-44515220408-tupras |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 27c1876f7f3e7153ae32bde216140bb436546e9a4311fc6663ab87f534967e5a |
| Huella del envío (bundle_sha256) | 709b89bcfc42c500e2e3211bfb504b6c3768e913a8f609506dcc9461066726a7 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 6312bdf8e1122866f67c07c5fad2fad1e33aa191979b2f98db2a389533c62a6e |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 123585 tokens |
| Reserva estimada antes de llamar | USD 1.1497 |
| Uso de tokens | entrada 56109, salida 4460 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.313636; cota 0.313636 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Tupras/Tupras_respuesta.md | 84d150767721527dd94b69399f0429bdce22c42749b5d18dcf52cdbed1a4a284 | 29815 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Tupras/Tupras_evaluada.xlsx#Análisis | c91b625aaca0915256211ad66c96ef89b87ab78a073b42be384b9ddf93d6ce6a | 23040 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Tupras/Tupras_evaluada.xlsx#Control maestro | 6f438398f4fae546f498cd037e1a95dd7b38184f21298f3bf0459e8aac5845cc | 50058 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `faltan_datos` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    No consta como cifra cerrada: la hoja lo estima en ≈1.092 mm TL dentro de la deuda de 68.201 (Control maestro!M51), aproximado por los derechos de uso (Control maestro!N47).


### Tipo de negocio y motor

    Refinador de petróleo cíclico de materias primas (commodity) con participadas logísticas y energéticas, en Türkiye y con cifras bajo NIC 29
    Caja libre de ciclo medio: margen neto de refino (NRM) normalizado por un volumen de unos 29-30 Mt, en liras constantes o en USD, contrastado con el coste de reposición, en lugar del DCF de diez años sobre la media FY23-25.

### calidad

    El negocio se entiende (volumen por margen de refino, 30 Mt/año y 70 % de la capacidad del país), pero es tomador de precios: el ROIC TTM del 16,9 % está en pico de márgenes, frente al 12,8 % en FY24 y el 10,5 % en FY25 (sin caja, Control maestro!N29), y el margen bruto oscila entre el 2,8 % y el 16,0 %, sin un foso visible en las cifras.
    Dato clave: Análisis!C24 = 0.169

### caja

    El CFO es 1,37 veces el beneficio en FY21-25 y la caja libre base es positiva (64.257 mm, Análisis!C52), pero es muy volátil: hubo -731 mm en 2021 y unos 28.000-30.000 mm en 2024-2025, y el TTM de 139.075 mm (Análisis!C40) va inflado por +85.141 mm de proveedores, así que la conversión es recurrente pero no estable.
    Dato clave: Análisis!C26 = 1.37

### balance

    Sin arrendamientos, la deuda de unos 67.109 mm TL queda muy por debajo de la caja de 195.841 mm (Análisis!C53), lo que da caja neta (-1,23x el EBITDA TTM de 107.449 mm y -0,78x en el peor caso de la hoja); pasa incluso con el límite exigente de una cíclica, aunque los vencimientos y covenants no se pueden verificar sin las notas.
    Dato clave: Deuda sin arrendamientos ≈ 67109 (Análisis!C54 = 68201 menos ≈1092 de arrendamientos estimados en Control maestro!M51); Control maestro!N36: deuda neta/EBITDA sin leases = -1.23

### precio

    La cotización de 343,5 TL supera la referencia mecánica de Sí (mín(196,7; 0,75×413,4) = 196,7 TL) y queda por debajo del ponderado de 413,4 TL, que cae a 328,6 TL con r +2 puntos (Análisis!C92); además, el DCF de la plantilla no aplica a esta cíclica (Análisis!C62) y la hoja es anterior a los resultados 9M26 del 06.11.2026, así que no sirve para concluir; la hoja dice DESCARTAR · demasiado difícil, pero esa conclusión no se hereda aquí.
    Dato clave: Análisis!C37 = 343.5 frente a Análisis!B78 = 196.715101406204

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo da una capitalización de 661.854 mm TL, sin ningún dato concreto de encaje.
    Dato clave: Análisis!C41 = 661854

### Qué lo cambiaría

    - Que los resultados 9M26 muestren un NRM de vuelta a 6-7 USD/bbl y la caja libre acercándose a unos 20.000 mm TL anuales, lo que llevaría a descartar por precio y calidad.
    - Que una serie larga en moneda constante sitúe el valor de ciclo medio claramente por encima de 343,5 TL, lo que llevaría a estudiar_a_fondo.
    - Una cotización por debajo de unos 197 TL (Análisis!B78), en la que el precio pasaría incluso en el escenario malo.

### Qué falta

    - Serie de 10-15 años del margen neto de refino y de la caja libre en USD o en liras constantes, para fijar la caja de ciclo medio que decide el precio.
    - Resultados 9M26 (previstos para el 06.11.2026, Control maestro!N20), posteriores a la fecha de la hoja.
    - Pasivo por arrendamientos exacto y estructura de la deuda (divisa, vencimientos, covenants), no verificables sin las notas (Control maestro!N51).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro precio: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

