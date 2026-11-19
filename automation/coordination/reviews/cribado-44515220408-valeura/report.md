# Cribado · Valeura

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-27 |
| Tarea | cribado-44515220408-valeura |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 1c4608e5af3de48c99b5a8fa2c1a72f029b2b330718fa52a0878a53fafcc62d9 |
| Huella del envío (bundle_sha256) | 17f9b56aa93aab2a08e71adf0cbbeb7b0cd397e2497ac5b662af8a0270e79e01 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 472a9a249f13b1fc0afc88844e5dcdbdbee0d7b5d77ff63ebf2f1926b5596008 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 183827 tokens |
| Reserva estimada antes de llamar | USD 1.390668 |
| Uso de tokens | entrada 83453, salida 3919 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.412192; cota 0.412192 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Valeura/Valeura_respuesta.md | f7d190dd6bc2c4cc2326f0242e93683581d44802db6f586ccea607798762d549 | 33294 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Valeura/Valeura_evaluada.xlsx#Análisis | cc4a76060fa5b43a426d7b8aa6679b73cd34ef7bb9689ff9062256c0308fcafb | 23091 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Valeura/Valeura_evaluada.xlsx#Control maestro | 7d2042da415bace0b31baba8cd49f6bbd9f284ed1e59267cb6755f1dfd812a05 | 105805 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | no_pasa |
| caja | dudoso |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Análisis!C54 = 67.7 (pasivos por arrendamiento NIIF 16: 21.5 corriente + 46.2 no corriente); aparte, desmantelamiento contabilizado 89.1 mm y 186.3 mm nominal sin descontar (Control maestro!M36)


### Tipo de negocio y motor

    Productor de petróleo offshore (E&P upstream) en el Golfo de Tailandia: materia prima cíclica, activos maduros que se agotan y licencias con vencimiento.
    Valor de las reservas (NPV después de impuestos de 1P y 2P a varios precios del crudo, hasta el vencimiento de las licencias) más caja neta menos desmantelamiento, contrastado con caja de ciclo medio.

### calidad

    Se entiende, pero no muestra calidad: tomador de precio sin coberturas, dos clientes con el 97% de los ingresos de crudo, vida de reservas 2P de 7.5 años, licencia B5/27 que expira en 2031 y margen a precio constante comprimiéndose del 11.5% al 8.5% LTM, con un ROCE (0.185) que oscila ±12.2 pp por cada 10 US$/bbl.
    Dato clave: Análisis!C27 = Comprimiendo

### caja

    El FCF base normalizado es positivo (79.2 mm) y el LTM es 83.4 mm, pero la serie es irregular ((83.9) → 145.0 → 91.4 → 124.3), el 108% del FCF LTM viene de Q2 2026, a Brent 64 el FCF del accionista es ≈0 y la guía de capex 2026 de 220-235 mm supera los 172.4 de la base.
    Dato clave: Análisis!C52 = 79.216

### balance

    Sin arrendamientos la deuda financiera dispuesta es 0 frente a 300.7 mm de caja no restringida, es decir caja neta y deuda/EBITDA sin sentido; la hoja marca C33 como N/A con un cálculo que sí incluye arrendamientos (caja neta 233.0), aquí recalculado sin ellos, y la revolving de hasta 325 mm está sin disponer.
    Dato clave: Deuda financiera sin arrendamientos = 0 (Control maestro!M51); Análisis!C53 = 300.7 → caja neta sin arrendamientos 300.7

### precio

    El DCF de la plantilla no aplica y no se usa para concluir, aunque apunta a caro (ponderado 11.07 frente a 12.16, y 8.84-14.87 con r ±2 pts) y el NAV 2P de la empresa (≈C$12.97, unos 9.25 US$) también queda por debajo; haría falta un NAV de reservas 1P/2P a varios precios más caja menos desmantelamiento, y la hoja es anterior a los resultados de Q3 2026.
    Dato clave: Análisis!C37 = 12.16

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja no dice nada concreto sobre encaje más allá de una capitalización de 1291.2 mm; este filtro no elimina.
    Dato clave: Análisis!C41 = 1291.2

### Qué lo cambiaría

    - Que el NPV después de impuestos de las reservas 1P a precio bajo más la caja neta menos el desmantelamiento supere la cotización de 12.16 US$.
    - Que el margen a precio constante deje de comprimirse y mejore dos semestres seguidos con el nuevo CPP de Wassana desde 2027.
    - Que se conceda la prórroga de B5/27 más allá de ago-2031 y la reposición 2P siga por encima del 150% sin compras.

### Qué falta

    - NPV10 después de impuestos de las reservas probadas (1P) a precio bajo del crudo; solo consta el NPV10 2P (692.0 mm).
    - Resultados de Q3 2026 (se publican el 11-nov-2026, después de la fecha de la hoja) y confirmación de la guía de capex 2026.
    - Condiciones de prórroga de las licencias B5/27 (ago-2031) y G10/48 (dic-2035), que concentran el 70.8% de las 2P.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

