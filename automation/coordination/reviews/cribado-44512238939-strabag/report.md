# Cribado · Strabag

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-11 |
| Tarea | cribado-44512238939-strabag |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | b2ca875289eada73640963e11d31f125c3ea3571b16e65106decd895c6a277b8 |
| Huella del envío (bundle_sha256) | 967859f9ef9bc7ec1fa0b331a488e64ebc51c280bc92f01f6fa9de502bd222f9 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 3578a3ac285a2eaa212aeff3fc3a128c180f49152e604c2b65ac54c018c2a205 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 133148 tokens |
| Reserva estimada antes de llamar | USD 1.187952 |
| Uso de tokens | entrada 60879, salida 4212 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.327756; cota 0.327756 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Strabag/Strabag_respuesta.md | 81f37127f5d7cfbce2fe1e1afe30df44875957272560d78fa84c988766296c1a | 32624 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Strabag/Strabag_evaluada.xlsx#Análisis | fc70dfabfda8b26e4b051d5467e07a3ba5e74b6f410e882cb41e9f509dbdf387 | 23064 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Strabag/Strabag_evaluada.xlsx#Control maestro | ecee37c13bfa156d344efb9b4ebad1420a65b0cf45ecdbfe5a06e633399c0667 | 56474 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `estudiar_a_fondo` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 ≈ 397,7 mm (estimado por la hoja; incluido en los 933,4 mm de Análisis!C54)


### Tipo de negocio y motor

    Constructora por contrato, cíclica (infraestructura y edificación, ~70 % de clientes públicos), con flotante de anticipos de clientes y caja neta
    Caja de ciclo medio: caja libre antes de circulante con un margen EBIT normalizado (en torno al 4–5 %, frente al 6,7 % récord), sin contar como permanente el flotante de anticipos.

### calidad

    El negocio se entiende (C11 = Sí, así que la etiqueta «demasiado difícil» de A6 no encaja con la propia hoja), pero el ROCE del 14,5 % y el margen del 6,7 % de 2025 son máximos de la serie tras un ROCE de 4,1–7,6 % en 2015–2020, con cuotas del 2–6 % y una multa de cártel ampliada en 100,63 mn: falta probar que haya foso.
    Dato clave: Análisis!C24 = 0.145

### caja

    La caja libre base de 982,9 mm (media 2023–25, ya neta de capex y de 69,1 mm de principal de arrendamientos) fue positiva todos los años y la caja antes de circulante sube de 518 a 846 mm (2021–25), aunque el CFO/beneficio de 2,04x lleva unos 228 mm al año de anticipos que podrían devolverse y la serie oscila (120 mm en 2022, 1.213 en 2023).
    Dato clave: Análisis!C52 = 982.9

### balance

    Sin arrendamientos, la deuda es de unos 535,7 mm frente a 3.430,2 mm de caja, una caja neta de unos 2.894 mm que el apalancamiento de la hoja (−1,24x con NIIF 16; −1,51x sin arrendamientos, con un EBITDA aproximado) confirma, y que se mantiene aunque se descuenten los 497,6 mm de Rasperia y unos 362,7 mm de pensiones.
    Dato clave: Control maestro!M51 = préstamos bancarios ~535,7 mm (933,4 − arrendamientos ~397,7), frente a caja Análisis!C53 = 3430.2

### precio

    La cotización de 102,2 € está por debajo del valor ponderado de 129,19 € y del normal de 124,06 €, pero no hay precio de Sí, el escenario malo da 70,35 €, a r + 2 puntos el valor baja a 99,81 € (por debajo del precio) y la base de caja lleva circulante de un ciclo alto, así que hace falta valorar con caja de ciclo medio.
    Dato clave: Análisis!C83 = 129.188530015553

### encaje

    El paquete no trae la cartera de la persona responsable, así que a la fecha de la hoja (11-oct-2026) no hay base para juzgar el encaje, y este filtro no elimina.
    Dato clave: Análisis!D4 = 2026-10-11

### Qué lo cambiaría

    - Un margen EBIT de 2026 por debajo de la guía del 5,5–6 % o una media de caja libre a tres años por debajo de 700 mm haría no_pasa calidad o caja (descartar).
    - Una cotización por debajo de unos 100 € (valor ponderado a r = 11 %, Análisis!C92 = 99.8) haría pasar el precio incluso con una tasa exigente.
    - Que los litigios de Rasperia resulten contra STRABAG y ejecutables sobre activos fuera de Rusia cambiaría el balance.

### Qué falta

    - Valoración con margen de ciclo medio y caja antes de circulante: la hoja solo da la sensibilidad del margen normalizado del 5,1 % sobre el ROCE, no sobre el valor.
    - Desglose exacto de préstamos y arrendamientos (la hoja estima ~535,7 y ~397,7 mm) y EBITDA LTM exacto después de alquileres.
    - Importe de las provisiones y reclamaciones del cártel austriaco y de Chile, y contra quién van los litigios de Rasperia (medida de 1.090 mn).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

