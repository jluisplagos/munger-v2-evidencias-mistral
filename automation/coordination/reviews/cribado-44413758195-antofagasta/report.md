# Cribado · Antofagasta

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-24 |
| Tarea | cribado-44413758195-antofagasta |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 6f6312475ddbd331191cc66a7ee1d76c9a9c2361794fcf6f258ae5508ae22b60 |
| Huella del envío (bundle_sha256) | 0b40bad255d8a15998895db304a3c778cee7884649cb7535a1b69870d37e4fda |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | d30ba5a3b391e5044c53e0cd411f3348ee78bc6c0d79978d44ca9c22e38ac4d8 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 147566 tokens |
| Reserva estimada antes de llamar | USD 1.245624 |
| Uso de tokens | entrada 65243, salida 4531 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.351592; cota 0.351592 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Antofagasta/Antofagasta_respuesta.md | 834bab60ebf4094eb91762eb36910fe25fcb85fbb5307bcb1eb176697aa10e06 | 44236 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Antofagasta/Antofagasta_evaluada.xlsx#Análisis | 50be5850afb546173f96c15215ce8a4725fb15d5c55b2dc84d70b3a710e6d6fa | 23825 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Antofagasta/Antofagasta_evaluada.xlsx#Control maestro | b2bb700be06f46af575b2b34093778154845033091d9aefd31db97b1132dd787 | 58679 |

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

    Control maestro!M51 = 725.1 (pasivo por arrendamientos NIIF 16 a 30-jun-2026; subió desde 162,0 por SIAM II, +509,3)


### Tipo de negocio y motor

    Minera de cobre cíclica y de materias primas (cuatro minas en Chile, con oro, molibdeno y plata como subproductos y un ferrocarril); vende a precio LME y está en fase de capex de crecimiento.
    Caja de ciclo medio (EBITDA y caja libre a precios de cobre y oro normalizados, con el capex de sostenimiento separado), contrastada con una suma de VAN por mina hasta el agotamiento con varios precios de cobre.

### calidad

    El negocio se entiende (C11 = Sí) y el coste es competitivo, pero el ROCE del 25,6 % cae al 11,1 % antes de impuestos con el precio del cobre de 2023, el margen EBITDA oscila entre el 45 % y el 65 % con el metal y el volumen baja de 770,0 kt (2019) a 653,7 kt (2025), así que la ventaja visible es sobre todo precio, no foso.
    Dato clave: Análisis!C24 = 0.256

### caja

    La caja libre LTM es de −343,1 M$ y la base a cinco años de solo 163,4 M$ (negativa en 2022, 2024 y 2025) pese a una conversión CFO/beneficio de 1,49; sin capex de crecimiento sería de 1.134,3 M$, así que el resultado depende de separar el capex de sostenimiento, que la hoja no da en serie.
    Dato clave: Análisis!C40 = -343.1

### balance

    Sin arrendamientos, la deuda neta es de unos 3.241 M$ (3.966,1 − 725,1) frente a un EBITDA LTM de 5.808,2 M$ (unos 5.690 M$ tras restar el principal de arrendamientos de 118,0), es decir ≈0,57x, coincidente con la sensibilidad de la hoja; sin contar las inversiones líquidas sería ≈0,87x, y la caja cubre 4,81x la deuda a corto, holgado incluso para un negocio cíclico.
    Dato clave: Control maestro!N51 = 7401.1 (deuda sin arrendamientos)

### precio

    El DCF de la plantilla no aplica (su ponderado de 3,31 $ frente a 40,75 $ no sirve para concluir) y la hoja no tiene precio de Sí, pero el EV/EBITDA de 8,44x está en la parte alta de su historia de 4,1x–9,7x con el cobre realizado en 6,43 $/lb frente al caso base de la empresa de 4,30 $/lb, lo que apunta a caro a ciclo medio; hace falta una valoración de caja a ciclo medio para decidir.
    Dato clave: Análisis!C42 = 8.44

### encaje

    El paquete no trae la cartera; solo consta que cotiza en la LSE en GBp (3.048,0 GBp a 1,33683 = 40,75 $) y que la familia controla el 64,92 % de las ordinarias, datos a cruzar con la cartera sin que eliminen nada en el cribado.
    Dato clave: Análisis!C37 = 40.75

### Qué lo cambiaría

    - Que tras terminar los proyectos en 2027 la caja libre se asiente por encima de 1.000 M$ en años de precio medio del cobre.
    - Que la cotización baje hasta que el EV sobre un EBITDA de ciclo medio quede en la parte baja de su historia (cerca de 4,1x–7,2x).
    - Que la deuda neta sin arrendamientos supere 2,5x el EBITDA en un año de cobre bajo, con el capex aún comprometido.

### Qué falta

    - Serie de capex de sostenimiento y desarrollo de mina separada del capex de crecimiento, para fijar la caja libre de ciclo medio.
    - Reservas y recursos por yacimiento, con leyes y vida de mina, y un precio de cobre de ciclo medio para el motor adecuado.
    - Calendario de vencimientos y umbrales de los covenants, y la caja restringida a junio de 2026 (no constan en la hoja).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

