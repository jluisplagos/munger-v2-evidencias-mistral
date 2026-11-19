# Cribado · Mavi

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-31 |
| Tarea | cribado-44505954250-mavi |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | fc876f45eab2f294cf6cc37e713b56d762e71b8842cbd391b4839d9871239e4c |
| Huella del envío (bundle_sha256) | f5d26608e27c913ed53475039d2a0dbc6b79ab191e50b967665811ad80f6fb8f |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 5aa9ac8701f54cd4693b551ef8e8e2b039d35a087b137021bbc99ac0cfd7bc49 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 134128 tokens |
| Reserva estimada antes de llamar | USD 1.191872 |
| Uso de tokens | entrada 60298, salida 4638 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.333952; cota 0.333952 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Mavi/Mavi_respuesta.md | 20ff126d3283cb64da066c7610672fe40b5a9962f7c4f26558fdd653589a8d0d | 32507 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Mavi/Mavi_evaluada.xlsx#Análisis | 779664a72e14cad0df2131cfb616e5f0db82a18812fcc42871d00b66b8f041c1 | 24440 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Mavi/Mavi_evaluada.xlsx#Control maestro | 7a692ee8242ca02f97b7badf6ac1dad0217c5c5c991e208048bdfef1e7e11332 | 56415 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 3478.2 (CP 1.542,9 / LP 1.935,3; implícito en Análisis!C54 = 6298.8 − deuda bancaria 2.820,6)


### Tipo de negocio y motor

    Marca de ropa vaquera y minorista con tiendas propias, concentrada en Türkiye (91 % de las ventas) y con contabilidad de hiperinflación (TMS 29).
    DCF de caja libre de la plantilla en TL constantes con tasa real, sobre una caja libre económica normalizada (restando intereses imputados en compras y comisiones de tarjeta) y llevando el valor a TL de la fecha de la cotización.

### calidad

    El negocio se entiende y tiene señales de marca (ROIC del 22,6 % con caja, margen bruto estable del 48–53 %), pero el ROIC económico baja al 13,8–14,1 %, el margen operativo se comprime (13,1 % → 11,5 % LTM), las ventas reales caen dos años, el 91 % depende de Türkiye y hay dudas de gobierno (un tercio de compras a partes vinculadas, remuneración del 32 % del beneficio); a diferencia de la etapa 1, no lo trato como «no se entiende», sino como calidad dudosa.
    Dato clave: Análisis!C24 = 0.226

### caja

    La caja libre base es positiva (2.260,5 mm, ya restados intereses, arrendamientos y SBC) y la conversión CFO/beneficio es de 2,62x, pero la caja libre económica normalizada cae 4.509 → 2.518 → 2.240 → 2.186 mm de FY2023 a LTM y su medida cambia un 43–54 % según la definición de C48, así que no es estable.
    Dato clave: Análisis!C52 = 2260.5

### balance

    La hoja da Deuda neta/EBITDA de −0,31x (C33) con arrendamientos; recalculado sin ellos, la deuda bancaria de 2.820,6 menos una caja de 9.470 deja caja neta de −6.649 mm, −0,88x sobre el EBITDA pre-TFRS 16 de 7.513,7 (sensibilidad de la propia hoja), y la caja cubre 3,36x la deuda bancaria, que vence toda a menos de 12 meses.
    Dato clave: Control maestro!M51 (deuda bancaria sin arrendamientos) = 2820.6

### precio

    A 9 % la cotización de 33,46 TL supera claramente el precio de Sí, que es el menor entre el escenario malo (27,39) y ¾ del ponderado (¾ × 50,55 ≈ 37,91), un 22 % por encima incluso si se lleva a TL de octubre (≈29), aunque el ponderado da un margen del 34 % y a r = 11 % aún vale 39,87.
    Dato clave: Análisis!B78 = 27.3872741531587

### encaje

    El paquete no trae la cartera de la persona responsable; solo cabe anotar una capitalización de 25.873 mm TL y una concentración del 91 % de las ventas en Türkiye para contrastarla con ella.
    Dato clave: Análisis!C41 = 25873

### Qué lo cambiaría

    - Una cotización por debajo de ≈27,4 TL (valor del escenario malo, Análisis!B78) llevaría el veredicto a estudiar_a_fondo.
    - Una caja libre económica normalizada por debajo de 1.800 mm o un margen bruto por debajo del 48 % dos ejercicios seguidos llevaría a descartar.
    - Que las compras a partes vinculadas resultaran estar por encima de mercado o que la remuneración resultara abusiva por persona llevaría a descartar por calidad.

### Qué falta

    - Serie en términos reales FY2016–FY2022 (solo existe en TL nominales) para ver cómo se comporta la caja libre en cada bache turco.
    - Precios de compra a Erak y Akay frente a terceros, remuneración por persona de la alta dirección y quién posee el 52,31 % de Mavi USA.
    - Las decisiones que fijan C40, C46–C50, C57 y C88 están fechadas el 09-nov-2026, después de la fecha de la hoja (31-oct-2026), y los valores están en TL de julio frente a un precio en TL de octubre.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

