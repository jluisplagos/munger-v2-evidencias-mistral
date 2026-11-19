# Cribado · WEG

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-10 |
| Tarea | cribado-44515220408-weg |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 7f8addae2953242089e9179a15fe8b98dca0e7280e59694d164289f8b4220d8f |
| Huella del envío (bundle_sha256) | 08ba6b9b041577248dfa24a26e5ea025a4fe413907a043cd18664e66f00167af |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 7eab3027372a3081b38072f276f8fa9e8fe0183634084652fe1f1067882532f5 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 128643 tokens |
| Reserva estimada antes de llamar | USD 1.169932 |
| Uso de tokens | entrada 59464, salida 4205 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.321956; cota 0.321956 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/WEG/WEG_respuesta.md | b24fdd59fade077ed6b4e6a3368e6b8443be45da7e2804d2f07050c0ee9b4ab5 | 31231 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/WEG/WEG_evaluada.xlsx#Análisis | b157d93417158bc5bb25b77508e60bceee88778985c3ce8b75069bb518e79d60 | 23759 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/WEG/WEG_evaluada.xlsx#Control maestro | cbb0e225f33f87dec33dbb7c5fcf40bb8abd019b4b5b91335f856bc665530d83 | 52809 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | pasa |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 768.4 (pasivo por arrendamientos a 30/06/2026; pagos IFRS 16 ya dentro del CFO, Control maestro!M46)


### Tipo de negocio y motor

    Fabricante industrial de bienes de capital eléctricos (motores, generadores, transformadores/T&D, automatización y tintas), con componente cíclico y caja neta.
    El DCF de caja libre de la plantilla, pero con un FCF normalizado de ciclo medio que separe capex de mantenimiento y de crecimiento, porque el FCF actual está deprimido por capex de capacidad.

### calidad

    Negocio entendible con ROIC propio del 29,4 % LTM, margen EBIT estable en el 19–20 % desde 2023 y caja neta todos los años, aunque con ciclo industrial y foso no probado con cuotas; discrepo del «DESCARTAR · demasiado difícil» de A6, que nace de C13 = No (el precio), no de la calidad.
    Dato clave: Análisis!C24 = 0.294

### caja

    La caja libre base es positiva (4.032,4 mm, después de SBC y con alquileres ya dentro del CFO) y la conversión CFO/beneficio es de 0,918 (C26), pero el FCF ha bajado de unos 5.400 a 3.760–4.050 mm desde 2024 por un capex de 2,7x la amortización, así que la hoja marca C25 «Sí» con más optimismo del que da la serie reciente.
    Dato clave: Análisis!C52 = 4032.4

### balance

    Sin arrendamientos, la deuda es de 5.066,3 mm frente a 7.750,3 mm de caja (Análisis!C53) más 1.062,7 de aplicaciones, es decir, caja neta (−0,43x según la hoja); aun restando las distribuciones pendientes de 5.933,1 mm quedaría en torno a +0,25x, muy holgado para un fabricante algo cíclico (el −0,335x de C33 incluye arrendamientos y no se usa tal cual).
    Dato clave: Control maestro!M51 = 5066.3 (préstamos sin arrendamientos, 30/06/2026)

### precio

    La cotización de 51,47 está muy por encima del valor ponderado de 11,87 (C83) y del escenario bueno de 17,86 a la r del 15 % de la hoja, y recalculando sus escenarios al 9 % salen aprox. 14 / 24 / 41 (ponderado ≈25,6), todavía claramente por debajo del precio, que exige >30 % de crecimiento anual (C86).
    Dato clave: Análisis!D78 = 17.8554590265235 (escenario bueno a r 15 %) frente a Análisis!C37 = 51.47

### encaje

    El paquete no trae la cartera; la hoja solo aporta contexto como una capitalización de 215.959,4 mm (C41) y un bloque de control del 64,36 %, sin nada concreto sobre encaje.
    Dato clave: no consta en la hoja (cartera no incluida en el paquete)

### Qué lo cambiaría

    - Una cotización cerca o por debajo de ≈ R$ 25 por acción (valor ponderado aproximado al 9 %) con la calidad intacta.
    - ROIC propio por debajo del 20 % dos años seguidos o margen EBIT por debajo del 15 % con el cobre estable.
    - Deuda sin arrendamientos más distribuciones pendientes por encima de ~1,5x EBITDA, o FCF que no se recupere en 2027-28 tras el capex de 2026.

### Qué falta

    - La hoja valora a r = 15 % y no al 9 %; el valor al 9 % es un recálculo aproximado propio (ponderado ≈ R$ 25,6), no una cifra de la hoja.
    - EBITDA sin NIIF 16 no publicado (la hoja da −0,43x aproximado) y desglose del capex entre mantenimiento y crecimiento.
    - Competidores y cuotas de mercado para confirmar el foso; además, la hoja cita decisiones del 10-nov-2026, posteriores a su fecha de análisis (10/10/2026).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

