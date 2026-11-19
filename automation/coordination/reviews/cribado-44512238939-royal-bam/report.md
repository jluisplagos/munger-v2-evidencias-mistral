# Cribado · Royal_BAM

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-07 |
| Tarea | cribado-44512238939-royal-bam |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 2a807f4812510ca525e2773344afd8799fe2865c9de2030ac8bef03abe73bc58 |
| Huella del envío (bundle_sha256) | 97db423438756628034fac0f6992c62a64aadfd42b7a8ccbcb8074349b493134 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | a96ec51aeaacac1acf43b748b4cbf17e4ed705f597cb9cfaeb9a5e1327d014d8 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 148839 tokens |
| Reserva estimada antes de llamar | USD 1.250716 |
| Uso de tokens | entrada 66166, salida 4787 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.360404; cota 0.360404 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Royal_BAM/Royal_BAM_respuesta.md | 0db11eca5eeae148c6949c359295697a500aeae9fde7b3289305e06bc398b0c9 | 43144 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Royal_BAM/Royal_BAM_evaluada.xlsx#Análisis | d45261ea3d9875ec05734a53fb6fc894fb071748da0a469fe54d97a8dc08bf28 | 24342 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Royal_BAM/Royal_BAM_evaluada.xlsx#Control maestro | de59ffab15d9377318adbee6d62d364e2b698421bd18ed85433fb401b147bc16 | 60559 |

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

    Control maestro!M51 = 296 (pasivos por arrendamiento a 30-jun-2026; Análisis!C54 = 415 los incluye)


### Tipo de negocio y motor

    Constructora y contratista de obra civil, edificación y promoción residencial (Países Bajos, Reino Unido e Irlanda): un negocio cíclico de proyectos, con circulante negativo y riesgo de ejecución.
    Caja libre de ciclo medio normalizada sin circulante (margen medio del ciclo sobre ingresos, menos capex y alquileres), contrastada con la cartera de pedidos y con el valor del suelo residencial.

### calidad

    Se trata de una contratista sin foso (Análisis!C18 = No), con ingresos planos en una década y un ROCE que oscila entre el 5,6 % y el 17,2 % en 2021-25 (−4,2 % en 2020) y sobrecostes de proyecto cada año, de modo que el 19,2 % LTM (Análisis!C24) no basta para demostrar una ventaja duradera; coincide con las banderas de la etapa 1.
    Dato clave: Control maestro!N29 = 0,056/0,168/0,137/0,058/0,172 (ROCE 2021-25)

### caja

    La caja libre del accionista no es recurrente: la base media 2023-2025 es de solo 53,12 mm (rentabilidad del 1,7 % sobre 3.208 mm) y la media de cinco años es de −5,0 mm, aunque la conversión CFO/beneficio de 1,25x (Análisis!C26) y la caja antes de circulante positiva apuntan a que parte del problema es de circulante y de las devoluciones de impuestos del Covid.
    Dato clave: Análisis!C52 = 53.12

### balance

    Sin arrendamientos, los préstamos de 119 mm frente a 496 mm de caja de libre disposición dan caja neta de unos 377 mm y una deuda neta/EBITDA de aproximadamente −1,15x sobre un EBITDA sin NIIF 16 de 326,5 mm (Control maestro!N36), holgado incluso para un negocio cíclico y con la compra de A.Hak (504 mm de valor empresa); el −0,18x de Análisis!C33 incluye arrendamientos y no se usa tal cual.
    Dato clave: Control maestro!M51 = 119 (préstamos sin arrendamientos a 30-jun-2026)

### precio

    La cotización de 12,61 € está muy por encima del escenario malo de 2,10 € (Análisis!B78) y del ponderado de 3,66 €, incluso con r al 7 % (5,23 €), pero el DCF de la plantilla no aplica; con la caja normalizada sin circulante de 209,9 mm que cita la respuesta, el escenario malo seguiría en 8,31 €, por debajo del precio, y haría falta una valoración de caja de ciclo medio para concluir.
    Dato clave: Análisis!C37 = 12.61

### encaje

    El paquete no trae la cartera de la persona responsable (solo la capitalización de 3.208 mm como contexto) y no se considera el tamaño de posición de la hoja; este filtro no elimina.
    Dato clave: Análisis!C41 = 3208

### Qué lo cambiaría

    - Un ROCE por encima del 15 % y un margen EBITDA ajustado por encima del 6 % en 2026 y 2027 con el residencial holandés flojo, que mostraría una mejora estructural y no cíclica.
    - Una caja libre del accionista por encima de 150 mm tres años seguidos sin ayuda del circulante.
    - El cobro de las órdenes de variación holandesas de 362 mm, o bien su pérdida o un sobrecoste nuevo de más de 100 mm, que confirmaría el descarte.

### Qué falta

    - El desenlace histórico de las reclamaciones (570 mm de contraprestación variable reconocida, 362 mm de un solo proyecto): cuánto se reconoció y cuánto se cobró.
    - La concentración de clientes, el reparto público/privado, el importe del préstamo puente y la asignación del precio de compra (PPA) de A.Hak.
    - Coherencia de fechas: el Control maestro registra decisiones del inversor del 15-nov-2026, posteriores a la fecha de la hoja (2026-11-07), y la nota del tercer trimestre de 2026 no trae cifras.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Un texto menciona un tamaño de posición o un porcentaje de cartera."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

