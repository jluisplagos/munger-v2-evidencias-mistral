# Cribado · NKT

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-09 |
| Tarea | cribado-44509331308-nkt |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 09da7237fbc1c9cf75218b6f4d9f60ab5c2794bc1679efbd837a0b4bdf895276 |
| Huella del envío (bundle_sha256) | 49f34c4ff7356ebcf238013fa0b72a558cc3f23e59f1bb088bf894e24f54137f |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 17bf74f36953b1ada6254ddf05fb3fbf8bb970cbcdc49f4f3e8489b725a9e01c |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 140379 tokens |
| Reserva estimada antes de llamar | USD 1.216876 |
| Uso de tokens | entrada 63561, salida 4502 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.344284; cota 0.344284 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/NKT/NKT_respuesta.md | 4fc9f2f66be125db7b7409310dbf3a2daf51601bc1893478800a8aae51b05763 | 34191 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/NKT/NKT_cambios_v2.md | 98684d1a55b7665636ca6dbf39426a94fa7161fe3d564c4f618b29b867f7f8c8 | 4370 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/NKT/NKT_evaluada.xlsx#Análisis | f4518675b3a2645f8c3c0cad9db7adc987d90afa318d9682ec6ceaebbf4f9357 | 23067 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/NKT/NKT_evaluada.xlsx#Control maestro | 204f202c302b3e1f2e3a616dece549052284ead42f72f4509d88c864ce2fc6e3 | 57762 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 128 (arrendamientos a 30-jun-2026, incluidos en la deuda total de 259 de Análisis!C54)


### Tipo de negocio y motor

    Industrial cíclico de proyectos: fabricación e instalación de cables de alta tensión/HVDC prefinanciados con anticipos de clientes, además de distribución y accesorios.
    Caja de propietario de ciclo medio, normalizada sin la variación de anticipos y con el capex de mantenimiento (≈4 % de las ventas), valorada sobre un ciclo completo de adjudicaciones de alta tensión.

### calidad

    El negocio se entiende con el paquete y hoy tiene un RoCE del 20 % en los últimos doce meses (la hoja manda frente al 24 % de 2025 que cita la respuesta) y una cartera de unos 10.200 mm, pero el RoCE fue negativo en 2018–2020 y la ventaja no está probada a lo largo del ciclo; difiero del «demasiado difícil» de la etapa 1 (Análisis!A6), porque lo que no se entiende es la economía a diez años, no el negocio.
    Dato clave: Análisis!C24 = 0.2

### caja

    La caja libre base de 132,1 mm (media 2021–2025) no es recurrente: es de −134 mm en los últimos doce meses a junio de 2026 (Control maestro!M40) y negativa en todas las ventanas sin circulante (−203/−151/−349, Control maestro!N43); la conversión de 3,2x (Análisis!C26) se debe en un 55 % a anticipos, pero el capex de crecimiento de unos 2.000 mm en 2025–2028 impide saber cuál es la caja de propietario de ciclo medio.
    Dato clave: Análisis!C52 = 132.1

### balance

    Sin arrendamientos, la deuda es de 131 mm frente a una caja de 850 mm (Análisis!C53), así que hay caja neta (−1,85x sobre EBITDA antes de NIIF 16 según la hoja; el −1,459x de Análisis!C33 incluye arrendamientos y no sirve tal cual) y los estreses de la hoja también pasan; la salvedad es que esa caja procede de anticipos netos de clientes por 1.668 mm, con 3.358 mm de garantías bancarias detrás.
    Dato clave: Control maestro!N51 = 131 (deuda sin arrendamientos a 30-jun-2026; deuda neta sin arrendamientos 131 − 850 = −719)

### precio

    La cotización de 114,92 € supera con holgura el valor ponderado de 50,90 €, el del escenario bueno de 79,63 € y el de 73,66 € con una tasa del 7 % (Análisis!C90), y el precio exige un crecimiento del 17,6 % anual (Análisis!C86); pero el DCF de la plantilla no aplica (Análisis!C62), así que no concluyo: hace falta una valoración con caja de ciclo medio.
    Dato clave: Análisis!C37 = 114.92 frente a Análisis!C83 = 50.90

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo aporta contexto, como la capitalización de 6.142,3 mm, sin nada concreto sobre el encaje.
    Dato clave: Análisis!C41 = 6142.3

### Qué lo cambiaría

    - Una cotización cercana o inferior a un valor de caja de ciclo medio, por ejemplo por debajo de los 50,90 € del valor ponderado de la hoja.
    - Un RoCE que se mantenga por encima del 15 % en una fase de pocas adjudicaciones, o una cartera que caiga dos años seguidos por debajo de unos 8.000 mm.
    - Una reversión de los anticipos netos (1.668 mm) que lleve la deuda neta sin arrendamientos a terreno positivo.

### Qué falta

    - Caja libre de propietario de ciclo medio sin la variación de anticipos ni el capex de crecimiento: solo hay una estimación gruesa de 190–200 mm de la respuesta.
    - EBITDA reportado después del alquiler: la hoja solo estima el EBITDA anterior a la NIIF 16 de forma implícita (−1,85x).
    - Capacidad del sector y márgenes por contrato a lo largo de un ciclo completo; además, la cotización es de una fuente secundaria a 09-10-2026.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres.",
          "Filtro caja: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

