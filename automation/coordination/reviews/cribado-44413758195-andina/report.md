# Cribado · Andina

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-15 |
| Tarea | cribado-44413758195-andina |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | b35212aee5f459af3fbe7c309406fc8c3818dddc29af227c788360649a6198f5 |
| Huella del envío (bundle_sha256) | 6546ac29b03f3487a3abc4a802a550b92c7d3f8a1a04e6bf3d0c1bad142e3bd0 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 72938e32f7f23a9a9206fc2c51cacc432f897283c75be4240d74c2e484412831 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 172232 tokens |
| Reserva estimada antes de llamar | USD 1.344288 |
| Uso de tokens | entrada 75392, salida 3914 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.379848; cota 0.379848 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Andina/Andina_respuesta.md | 1c5e6873ffffa938bda475114cec6698c7d405c36731b3330c85e7a07a9d4eab | 47489 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Andina/Andina_evaluada.xlsx#Análisis | 6eaaca023c98704498df8ed8ef00b1de85bc146856d5cfb6c9bb81faca6cbc0f | 24767 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Andina/Andina_evaluada.xlsx#Control maestro | 3d735f27e8164b894d54adf17b0dbdf836d9e4e9de14b6ea1d5d74d4a71deccf | 79258 |

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

    Control maestro!N36 = 30962 (13.230 corrientes + 17.732 no corrientes, a 30-09-2026)


### Tipo de negocio y motor

    Embotellador y distribuidor franquiciado del sistema Coca-Cola en Chile, Brasil, Argentina y Paraguay: consumo básico estable, con riesgo contractual (licencias) y de país (Argentina, 22 % de las ventas).
    El DCF de caja libre de la plantilla en CLP nominales sirve para un embotellador estable, siempre que el capex de mantenimiento esté normalizado y que la no renovación de una licencia se trate como un salto discreto, no como menor crecimiento.

### calidad

    Negocio comprensible y de calidad medible (ROCE después de impuestos del 16,3%, cuotas del 57-75,6% y margen operativo estable en el 13-13,6%), con el foso alquilado porque las licencias vencen entre 2027 y 2028 a discreción de TCCC; discrepo del «DESCARTAR · demasiado difícil» de Análisis!A6, que nace de C13 = No y no de que el negocio no se entienda.
    Dato clave: Análisis!C24 = 0.1628

### caja

    Convierte beneficio en caja (CFO/beneficio 1,96x en Análisis!C26) y la caja libre tras capex y arrendamientos es positiva en todos los años 2018-2025, aunque irregular por el capex (65.700 mm en 2024 frente a 268.745 LTM en Análisis!C40), y la plantilla no separa el capex de mantenimiento.
    Dato clave: Análisis!C52 = 130679

### balance

    El 1,16x de Análisis!C33 incluye arrendamientos y usa EBITDA NIIF 16, así que lo recalculo: deuda neta sin arrendamientos ≈ 764.072 mm sobre un EBITDA de 685.301 menos 16.739 de principal de arrendamientos da ≈1,14x; deuda neta/FCF ≈5,8x con la base de 130.679 y ≈2,8x con el LTM; caja 6,3 veces la deuda a corto (Análisis!C34) y covenants holgados, aunque falta el interés de los arrendamientos para afinar el EBITDA.
    Dato clave: Análisis!C54 = 1361435 (con arrendamientos); sin arrendamientos 1.330.473 mm y deuda neta sin arrendamientos ≈ 764.072 mm (795.034 de Control maestro!M36 − 30.962)

### precio

    La cotización de 4.799 CLP supera el ponderado de 2.945 (Análisis!C83), el escenario bueno de 4.049 (D78) y el ponderado a r del 7% de 4.469 (C90), y está casi 2,8 veces por encima del precio de Sí de la etapa 1 (≈1.740 CLP); con la base LTM de 268.745 el precio de Sí sería ≈3.570 según la respuesta, todavía por debajo del precio.
    Dato clave: Análisis!C37 = 4799

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja no dice nada concreto de encaje más allá de una capitalización de 4.191.648 mm, así que este filtro no elimina.
    Dato clave: Análisis!C41 = 4191648

### Qué lo cambiaría

    - Una cotización por debajo de unos 2.945 CLP (ponderado de Análisis!C83), que la acercaría a estudiar a fondo.
    - Un capex de mantenimiento publicado que justifique una base de FCF cercana a la LTM de 268.745 mm.
    - Un aviso de no renovación o una renovación de licencias en peores condiciones, que pasaría el veredicto a descartar o a demasiado difícil.

### Qué falta

    - Capex de mantenimiento frente a capex de crecimiento: la base de FCF va de 130.679 a 268.745 mm según el periodo y mueve el precio de Sí más del doble.
    - Historial y condiciones económicas de la renovación de las cuatro licencias de TCCC, que vencen entre enero de 2027 y marzo de 2028.
    - Intereses de los arrendamientos, necesarios para calcular exactamente el EBITDA después del alquiler; además, el precio de la serie B es de fuente secundaria (±3 %) frente a un valor por acción que mezcla las dos series.

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

