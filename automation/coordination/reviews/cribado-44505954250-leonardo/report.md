# Cribado · Leonardo

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 17/10/2026 |
| Tarea | cribado-44505954250-leonardo |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 55312c938946ba4b81df8df581939e5ad5e69ed128ce60c3fe76539a43ba4c67 |
| Huella del envío (bundle_sha256) | a987e2461c35e267d01d07558e16989d2292ec24b548824e80caeb72b924ca79 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 8987a91aa7ede84882599ce65ceed1f7bd02a4667d9800894afb2ebb70ee575e |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 130721 tokens |
| Reserva estimada antes de llamar | USD 1.178244 |
| Uso de tokens | entrada 59541, salida 3731 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.312784; cota 0.312784 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Leonardo/Leonardo_respuesta.md | 95c05f1f94140998fcf52012fd12db445e63a9bb84992b0eda060629d84e056e | 30529 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Leonardo/Leonardo_evaluada.xlsx#Análisis | 3c263d1da8051a442ce35a4b46df527d0ad3c7bbd218fdfb2744f056a850f49a | 23287 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Leonardo/Leonardo_evaluada.xlsx#Control maestro | f4045df60452fda89e4295e2757287fb932a99919cc2e3d6ae826e0ec7305bfc | 56033 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M36 = 624 (incluidos en la deuda neta del grupo de 3.248 m; coincide con 4.513 − 3.889 de Control maestro!M51)


### Tipo de negocio y motor

    Contratista aeroespacial y de defensa con contratos largos, a menudo a precio fijo, con gobiernos; cíclico según el gasto público, con participadas en JV y una filial cotizada (DRS) con minoritarios.
    Caja libre de ciclo medio normalizada (anticipos y circulante neutralizados) más suma de partes que sume las participadas estratégicas (MBDA, Thales Alenia Space, ATR, Hensoldt) y reste los minoritarios de DRS.

### calidad

    El negocio se entiende (contratista de defensa con clientes públicos y una cartera de 58.581 m), pero la ventaja no se ve en las cifras: ROI antes de impuestos del 14,8 %, ROS de 7-9 % sin expansión, cargos todos los años, Aerostructures en pérdidas y demanda ligada al ciclo de gasto público. Discrepo de la etapa 1: es una duda de calidad, no un caso de demasiado difícil.
    Dato clave: Análisis!C24 = 0.148

### caja

    La caja libre de la plantilla es positiva (462 m de base 2023-25) y la serie normalizada sin circulante es de 577/543/430/699/727 m en 2021-25 (Control maestro!M30), con una conversión CFO/beneficio de 1,35 (Análisis!C26), aunque 2018-21 fue casi nula y parte de la caja reciente depende de anticipos de clientes.
    Dato clave: Análisis!C52 = 462

### balance

    Sin arrendamientos, la deuda neta de 2.624 m es unas 1,03x el EBITDA pre-NIIF 16; la hoja usa 1,22x (Análisis!C33) con 624 m de arrendamientos, que no sirve tal cual. El nivel es holgado incluso para un negocio cíclico, con BBB/Baa2 y una línea de crédito de 1.800 m sin disponer, aunque la caja solo cubre el 0,35 de la deuda corriente (Análisis!C34 = No) y faltan los vencimientos.
    Dato clave: Control maestro!N36 = 1.03 (deuda neta sin arrendamientos = 3.248 − 624 = 2.624 m, Control maestro!M36; deuda bruta sin arrendamientos 3.889 m, Control maestro!M51)

### precio

    A 50,42 € (Análisis!C37) la cotización triplica el valor ponderado de 17,59 €, supera el escenario bueno (25,90 €) y el valor a r del 7 % (25,52 €), y el DCF inverso exige un 21,7 % anual (Análisis!C86). Aunque el DCF de la plantilla solo aplica a medias (omite dividendos de participadas e incluye el 100 % de DRS), la distancia es demasiado grande para cerrarla con esos ajustes.
    Dato clave: Análisis!C83 = 17.5938897688244

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja no da datos concretos de encaje más allá de una capitalización de 29.082 m.
    Dato clave: Análisis!C41 = 29082

### Qué lo cambiaría

    - Una cotización cercana o inferior al valor ponderado de unos 17,6 €, o al de unos 25 € con los dividendos de participadas, que llevaría el precio a pasa.
    - Que los pasivos contractuales (anticipos, 10.893 m) empiecen a bajar y la caja libre normalizada vuelva a niveles de 2018-2021, lo que haría no_pasa la caja y daría descartar.
    - Que la deuda neta sin arrendamientos supere unas 2,5x el EBITDA por adquisiciones (Raft, plan inorgánico de 1.800 m) o que aparezcan deterioros en IDV.

### Qué falta

    - Márgenes por programa y estimaciones a fin de contrato (el 81 % de los ingresos se reconoce a lo largo del tiempo), clave para juzgar la calidad.
    - Perfil de vencimientos de la deuda y condiciones de los depósitos de la JV MBDA (1.818 m) dentro de la deuda corriente.
    - Valor y dividendos repetibles de las participadas y valor de los minoritarios de DRS, que el motor adecuado necesita; además, los resultados de 9M 2026 (4-nov-2026) son posteriores a la fecha de corte.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

