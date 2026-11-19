# Cribado · Grupa

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-04 |
| Tarea | cribado-44502520327-grupa |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 25cf81c089c906b612bcdd1935e8de4711c505b6d18e099618606f199700cad2 |
| Huella del envío (bundle_sha256) | 2bc3367da3a28eded5367b9e6dda933de4aad085a825cf5d6dac4491ed113739 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 35bc443e3d6949d861e66d5a7c3d99f3e866b766767cd7e135190d31a2abab2d |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 128329 tokens |
| Reserva estimada antes de llamar | USD 1.168676 |
| Uso de tokens | entrada 58584, salida 4249 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.319316; cota 0.319316 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Grupa/Grupa_respuesta.md | 1b440959ecb6de4c1f757e02ad0bc92c22d67aadcc04e26513c41bb805c0cdd4 | 29802 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Grupa/Grupa_evaluada.xlsx#Análisis | 9c59b5312d6845c078796e7755d8662aad5fcb9170cdce4693b673074c63583e | 22709 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Grupa/Grupa_evaluada.xlsx#Control maestro | fd2bca3a977f0dbad651aaedeae19d124a5410268d523af800dd6732e4a7dda3 | 55062 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | no_pasa |
| caja | no_pasa |
| balance | dudoso |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51: arrendamiento financiero 3,110 mm (incluido en Análisis!C54 = 22.628 y excluido aquí del cociente); el arrendamiento operativo está fuera de balance bajo normas polacas (UoR) y su importe no consta en la hoja; la concesión de Cracovia (0,730 mm) va aparte.


### Tipo de negocio y motor

    Grupo de servicios funerarios en Polonia (pompas fúnebres, crematorios, cementerio en concesión) que crece por compras financiadas con deuda: roll-up joven con demanda estable.
    Para un roll-up joven que crece comprando con deuda, valorar la caja orgánica normalizada de las sociedades ya integradas (más la concesión de Cracovia hasta 2044) y tratar cada compra futura por su retorno sobre el precio pagado y la deuda que añade, en lugar de un DCF del accionista con financiación inestable.

### calidad

    El servicio funerario se entiende (Análisis!C11 = Sí), pero el ROCE del 2,8 % queda por debajo del coste aparente de la deuda (~6 %), el margen operativo cae del 15,5 % (2024r) al 5,7 % (2025) y la asignación de capital es dudosa (dividendo del 51 % del beneficio tras incumplir covenants); por eso no lo trato como «demasiado difícil», como hace la etapa 1, sino como calidad no demostrada.
    Dato clave: Análisis!C24 = 0.028

### caja

    La caja libre base normalizada es solo 0,772 mm (rendimiento del 0,5 % sobre 162,226 mm), con caja libre reportada negativa tres años (−7,29, −1,30 y −6,25 mm) y CFO del 1S26 negativo (−3,90 mm declarado); discrepo del ✓ PASA de Análisis!C26 = 1.08, que depende de la ventana elegida (0,22 con los tres ejercicios).
    Dato clave: Análisis!C52 = 0.772

### balance

    La hoja da 1,62x (Análisis!C33) con el leasing financiero dentro; sin arrendamientos la deuda neta es ≈14,85 mm, unas 1,3–1,6x el EBITDA de 11,104 mm según se reste o no el alquiler, pero equivale a ≈19 veces la caja libre base de 0,772 mm, con covenants incumplidos a 31-12-2025, pagos de compras pendientes (Glob 9,39 mm, Gloria ~11 + ~11 mm) y un pro forma Gloria de ~2,63x, así que no basta para dar el ✓ PASA de la hoja.
    Dato clave: Análisis!C54 = 22.628 menos arrendamiento financiero 3,110 (Control maestro!M51) = 19,518 mm de créditos; deuda neta sin arrendamientos 19,518 − 4,670 (Análisis!C53) = 14,848 mm

### precio

    La cotización de 6,80 PLN está muy por encima de todos los escenarios del DCF a r = 9 % (malo 0,39; ponderado 1,16; bueno 2,93 PLN), incluso a r = 7 % (máximo 2,00 PLN), y aunque ese DCF es de aplicación dudosa, el contraste con el motor alternativo apunta igual: EV/EBITDA de 16,4x frente a ~5,5x que paga la propia empresa en sus compras.
    Dato clave: Análisis!C37 = 6.8 frente a Análisis!D78 = 2.92709967950561

### encaje

    El paquete no trae la cartera; la hoja solo señala una liquidez muy baja (1 mm PLN ≈ 44 sesiones sobre una capitalización de 162,226 mm), lo que no elimina en el cribado.
    Dato clave: Análisis!C41 = 162.226

### Qué lo cambiaría

    - Que el anual 2026 y el 2027 muestren caja libre positiva y reconciliada de ~3 mm o más sin reclasificaciones.
    - Que el ROCE sin ingresos únicos supere con claridad el ~6 % del coste de la deuda durante varios años.
    - Que la deuda neta sin arrendamientos deje de crecer tras pagar Gloria y Glob, con covenants cumplidos.

### Qué falta

    - Reconciliación del CFO del 1S26 (−3,90 mm declarado frente a 1,70 mm por aritmética) y cifras del 3T26.
    - Deuda y caja tras el pago de Gloria (11 mm en sep-26) y Glob (9,39 mm), y umbrales de los covenants del crédito PKO.
    - Pagos totales por arrendamientos (financiero y operativo) del periodo TTM para fijar el EBITDA después de alquiler; además, la hoja cita decisiones del inversor del 10-nov-2026, posteriores a su fecha de análisis (04-11-2026).

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

