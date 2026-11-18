# Cribado · Airbus

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-24 |
| Tarea | cribado-44413758195-airbus |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 7711e34e13c2b9b29938324dea122aec753b3a561d232a06c976e7e7bfc233f8 |
| Huella del envío (bundle_sha256) | dcc2ad3ee601cb9f820a1aea3f542617fe60b47796cce82691abb30baf67ee49 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | ccebc3256358416fc65105c2a3943c0025493873a98dc428a3fb31fbfe9d39b5 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 166626 tokens |
| Reserva estimada antes de llamar | USD 1.321864 |
| Uso de tokens | entrada 74566, salida 4133 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.380924; cota 0.380924 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Airbus/Airbus_respuesta.md | 20df5f074034c2a08884f8435830bb86adf611a3e3f7e343146b0dc3bddcc673 | 50795 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Airbus/Airbus_evaluada.xlsx#Análisis | 5558b5ce6ceb5a9b821c007886caa28a3168bbecd4c6e942d87d714fbb61e641 | 24387 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Airbus/Airbus_evaluada.xlsx#Control maestro | 3da90435fdda5ba829085ef9b20cabe04de26b7c15538609774793285ef4b136 | 70736 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | pasa |
| caja | dudoso |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = pasivos financieros 14.276 mm, que incluyen arrendamientos por 2.425 mm (también en Control maestro!M36); pasivo por arrendamiento a corto de 385 mm según Control maestro!N46


### Tipo de negocio y motor

    Fabricante industrial aeroespacial y de defensa (aviones comerciales, helicópteros, defensa y espacio), cíclico, con cartera larga cobrada en parte por adelantado y en fase de ramp-up de producción
    Caja libre normalizada de ciclo medio, una vez terminado el ramp-up (capex próximo a la amortización y circulante estabilizado), idealmente con márgenes y caja por programa y una sensibilidad explícita al €/$ más allá de la cobertura de 2030.

### calidad

    El negocio se entiende (Análisis!C11 = Sí) y muestra calidad en las cifras: ROCE antes de impuestos del 18%, margen EBIT Adjusted estable en torno al 9-10% y una cartera de unos ocho años; las dudas sobre la duración del foso (COMAC en los 2030, €/$ más allá de 2030) son materia del estudio y no impiden entenderlo, por lo que discrepo del «demasiado difícil» de la etapa 1, basado en C12 = No.
    Dato clave: Análisis!C24 = 0.18

### caja

    La caja libre base es positiva (3.088 mm) y la conversión CFO/beneficio es de 1,55 (Análisis!C26), pero la caja libre está plana desde 2022 mientras el EBIT sube un 27%: el capex medio de 3.561 mm supera la amortización de 3.213 mm y los inventarios crecen con el ramp-up, y en 2020 la caja fue de −6.935 mm, así que no se puede afirmar todavía una conversión recurrente a lo largo del ciclo.
    Dato clave: Análisis!C52 = 3088

### balance

    Sin arrendamientos, la deuda es de 11.851 mm (14.276 − 2.425) frente a 23.376 mm de caja y valores, lo que da una caja neta de unos 10.785 mm y una deuda neta/EBITDA de aproximadamente −1,0x, recalculada con un EBITDA LTM de 10.423 menos unos 297 mm de alquiler; el −0,8x de Análisis!C33 incluye arrendamientos y no sirve tal cual, aunque la conclusión es la misma: holgura amplia incluso para un negocio cíclico, con la caja cubriendo 2,13 veces la deuda a corto.
    Dato clave: Análisis!C54 = 14276 (deuda con arrendamientos); sin los 2.425 de arrendamientos (Control maestro!M51) la deuda es 11.851 mm

### precio

    La cotización de 192,46 € supera con claridad el valor ponderado de 77,50 €, el escenario bueno de 126,41 € e incluso el ponderado con r al 7% (111,89 €), y el precio exige un crecimiento del 18,3% anual (Análisis!C86; la respuesta dice 17,6%, manda la hoja); aunque el DCF de la plantilla es dudoso para este negocio, la distancia es tan grande que también con la base de caja libre de la empresa (unos 113 € según la respuesta) sigue sin pasar.
    Dato clave: Análisis!C37 = 192.46 frente a Análisis!C83 = 77.4965513308757

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja no dice nada concreto de encaje más allá del tamaño de posición de la etapa 1, que no se usa aquí.
    Dato clave: Análisis!C104 = 0% · Demasiado difícil (dato de la etapa 1, no heredado)

### Qué lo cambiaría

    - Una cotización por debajo del escenario bueno de la hoja (126 €) y acercándose al valor ponderado (unos 77,5 €), que llevaría a estudiar a fondo
    - Caja libre antes de financiación a clientes por encima de 4.816 mm dos años seguidos con el circulante estabilizado (resolvería la duda de caja)
    - Un margen de aviones comerciales sostenido por debajo del 8% o una cuota relevante del C919, que rebajarían la calidad hasta descartar

### Qué falta

    - Resultados de 9M 2026 (28/10/2026), posteriores a la fecha de la hoja y no incluidos en el paquete
    - Margen y caja por programa, y calendario de coberturas €/$ más allá de 2030
    - Entregas y cuota del C919 año a año para juzgar la duración del foso

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro balance: motivo de más de 400 caracteres.",
          "Filtro precio: motivo de más de 400 caracteres.",
          "Un texto menciona un tamaño de posición o un porcentaje de cartera."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

