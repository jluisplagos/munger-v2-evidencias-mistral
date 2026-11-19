# Cribado · Ege_Gubre

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-30 |
| Tarea | cribado-44502520327-ege-gubre |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 284d328a235c37f243755e81e39a8700af9fb6577cb445078f1c83e9d928908c |
| Huella del envío (bundle_sha256) | c9ae132f29505c6414d077064cbf5d2fa9e3e8ab2272a9874b4eabf81fffb46b |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | c24632ed25f01b21bed9810e985fdc3a9fa4fe075d1fcb2df1670bdb2fa853f3 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 130161 tokens |
| Reserva estimada antes de llamar | USD 1.176004 |
| Uso de tokens | entrada 58919, salida 4419 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.324056; cota 0.324056 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Ege_Gubre/Ege_Gubre_respuesta.md | c342aeabaf48268df29f5abe6eeb42b4a3602ba0625e5d7f21a1bc64f93e6233 | 31960 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Ege_Gubre/Ege_Gubre_evaluada.xlsx#Análisis | 6206ee162d420a2a3eb9ff6fc2180d401ef966682911a90ce2e5d30e1e34c1a3 | 23775 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Ege_Gubre/Ege_Gubre_evaluada.xlsx#Control maestro | 0b237dd5ecca3481e785b39f1d058421a3874b7507ee04a41f3984ef0a8f63db | 53540 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 125.6 (arrendamientos en EUR/TL, incluidos en Análisis!C54 = 1362.4; principal pagado medio 28,9 mm/año en Análisis!C49, ya restado del flujo)


### Tipo de negocio y motor

    Terminal portuaria multipropósito y de contenedores (Aliağa, İzmir), de activo pesado y en fase de ampliación; la fabricación de fertilizante está suspendida desde noviembre de 2023.
    DCF de la plantilla en TL reales, pero sobre una caja libre normalizada con capex de mantenimiento (no la media 2023–2025 con ampliación) y, si el muelle fuera una concesión, valor de los flujos solo hasta su vencimiento en lugar de una perpetuidad.

### calidad

    El negocio se entiende (puerto con el 99,96 % de la facturación, margen bruto del muelle entre el 53,6 % y el 57,5 % y ROCE real del 9,7–16,1 %), por lo que discrepo del «demasiado difícil» de Análisis!A6; pero las diferencias de cambio suponen el 23,9 % del resultado operativo, faltan competidores y tarifas, y hay salvedad del auditor desde 2019 y litigio de minoritarios.
    Dato clave: Análisis!C24 = 0.161

### caja

    El beneficio sí se convierte en caja operativa (CFO/beneficio neto 1,51 en Análisis!C26), pero la caja libre base es solo de 281 mm frente a 1.674,9 mm de CFO por un capex medio de 1.310,8 mm, con una serie volátil (−345 mm en 2024) y sin separar el capex de mantenimiento del de ampliación.
    Dato clave: Análisis!C52 = 281

### balance

    Sin arrendamientos, la deuda bancaria es de 1.236,8 mm frente a 1.411,9 mm de caja, una caja neta de unos 175 mm; la deuda/EBITDA sin arrendamientos es negativa (≈−0,07x según la sensibilidad de la hoja, frente al −0,02x de Análisis!C33, que incluye arrendamientos) y la caja cubre 2,5x la deuda a corto, aunque a dic-25 había deuda neta de +255 y hay 324 mm de proveedores posiblemente ligados a la grúa.
    Dato clave: Control maestro!M51 = 1236.8 (préstamos bancarios sin arrendamientos, frente a caja Análisis!C53 = 1411.9)

### precio

    La cotización de 81,05 TL casi duplica y media el precio de Sí (≈33,0 TL) y supera el valor ponderado de 66,2 TL a r = 9 %; aunque a r = 7 % el ponderado sube a 95,5 TL, el precio de Sí sigue claramente por debajo, y el DCF inverso exige un crecimiento del 11,7 %, frente al 8 % del escenario normal; la base de caja libre incluye capex de ampliación, pero los escenarios ya lo normalizan.
    Dato clave: Análisis!C37 = 81.05 frente a Análisis!C78 = 33.01916952839 (precio de Sí = mín(malo 33,0; 0,75 × 66,2 = 49,7))

### encaje

    El paquete no trae la cartera; solo consta una liquidez de unos 30 mm TL diarios y una capitalización de 8.105 mm, lo que no basta para juzgar el encaje.
    Dato clave: Control maestro!M38 = 30 (liquidez ≈30 mm TL/día)

### Qué lo cambiaría

    - Una cotización por debajo del precio de Sí de unos 33 TL (Análisis!C78 malo) con calidad y caja aclaradas: pasaría a estudiar_a_fondo.
    - Dos ejercicios con capex cerca de la amortización (unos 600 mm) y una caja libre observada cercana a 900 mm: despejaría la duda de caja y subiría el valor de los escenarios.
    - Pruebas de que el margen depende sobre todo de las diferencias de cambio, de una concesión corta o de una fuga de valor al grupo de control: llevaría a descartar.

### Qué falta

    - Competidores en Aliağa-Nemrut, tarifas reales y su moneda, y concentración de clientes: necesarios para juzgar la ventaja y la parte del margen que se debe al tipo de cambio.
    - Régimen del terreno y del muelle (propio o en concesión, con plazo y condiciones), que decide si aplica una perpetuidad.
    - Desglose del capex entre mantenimiento y ampliación, y el capex previsto para 2026–2027 (513,6 mm en 6M 2026); la amortización de unos 600 mm al año es una estimación de la etapa 1.

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

