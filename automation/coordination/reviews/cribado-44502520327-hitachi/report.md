# Cribado · Hitachi

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-09 |
| Tarea | cribado-44502520327-hitachi |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 10ebbeb3be4917b06094fb9ca64e5a2705d51668551abbe285c91b684dbea318 |
| Huella del envío (bundle_sha256) | c0dcc9e179e2cf55a27d9168ccba0aca9d952fcca3ba623a2c39ab7bcadeeb51 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 78d803cbabebfd01718b3b9aec11977286537f67111f8e21249d60dcea90b7e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 137390 tokens |
| Reserva estimada antes de llamar | USD 1.20492 |
| Uso de tokens | entrada 61943, salida 3560 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.318972; cota 0.318972 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Hitachi/Hitachi_respuesta.md | 1ab9ef8fd5d5894547602b00d3be1f7e117a0fefc6b9076825e4d16d9689ed6d | 34350 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Hitachi/Hitachi_evaluada.xlsx#Análisis | 4706d9411d5cb8741bd640a8b638e3a2ae6c0b5e60329159cb99e63293622daf | 23819 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Hitachi/Hitachi_evaluada.xlsx#Control maestro | 9bd02fc7d400fbd021c83a98dd64b1ded0192ff44e2d34893a0974293d00d6bc | 58337 |

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

    No consta como cifra directa en la hoja; estimación por diferencia ≈ 301.934 mm (Análisis!C54 = 1056927 menos la deuda sin arrendamientos estimada de Control maestro!M51 ≈ 754993).


### Tipo de negocio y motor

    Conglomerado industrial y tecnológico de cinco segmentos (redes eléctricas y nuclear, TI en Japón, ferrocarril, industria) con proyectos largos y anticipos de clientes
    Suma de partes por segmento (Energy, DSS, ferrocarril, industria) con caja libre normalizada neta de anticipos de clientes; el DCF consolidado de la plantilla solo sirve como contraste grueso.

### calidad

    El negocio se entiende en grueso (C11 = Sí) y mejora: ROIC del 7,6 % al 12,4 % y margen bruto del 24,7 % al 30,0 %. Pero el ROIC sigue por debajo del 15 %, la mejora es reciente y coincide con el auge de redes, no hay foso probado (C18 = No) y el perímetro cambia casi cada año. Queda una duda que el estudio por segmentos puede resolver; discrepo del «demasiado difícil» de la hoja porque el negocio sí se explica con el paquete.
    Dato clave: Análisis!C24 = 0.124

### caja

    La caja libre ha sido positiva y creciente desde el ejercicio 2021 (290 a 1.170 bn), con caja operativa/beneficio de 1,525 y una base normalizada de 740.036 mm. Parte de esa caja son anticipos de clientes: la caja libre LTM sin anticipos baja a 513.013 mm y la empresa prevé devolver unos −340 bn en el ejercicio a mar. 2027. Aun así sigue siendo positiva.
    Dato clave: Análisis!C52 = 740036

### balance

    Sin arrendamientos, la deuda de unos 754.993 mm queda por debajo de una caja de 1.504.496 mm; la caja neta ronda los 749.500 mm y la hoja estima −0,47x de deuda neta/EBITDA sin arrendamientos, frente a los −0,26x de Análisis!C33, que sí los incluye. Con caja neta, rating A2/A/AA y líneas comprometidas no dispuestas de 505.000 mm, pasa con holgura incluso para un negocio de proyectos con algo de ciclo.
    Dato clave: Control maestro!M51 = 754993 (deuda sin arrendamientos, estimada) frente a Análisis!C53 = 1504496

### precio

    A 5.597 ¥ la cotización supera el valor ponderado (3.258 ¥), el escenario bueno (4.583 ¥) y el ponderado a r − 2 puntos (4.694 ¥). El precio descuenta un crecimiento del 13,3 % anual (C86), muy por encima de la referencia de Sí de unos 2.000 ¥ de la respuesta. Aunque el DCF consolidado sea dudoso para un conglomerado, la distancia es demasiado grande para que lo cambie.
    Dato clave: Análisis!C83 = 3258.46972495803 frente a Análisis!C37 = 5597

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja no dice nada concreto sobre encaje, salvo su plan del 0 %, que no uso como conclusión.
    Dato clave: Análisis!C104 = 0% · Demasiado difícil · sin posición (dato de etapa 1, no heredado)

### Qué lo cambiaría

    - Una cotización por debajo del valor ponderado de unos 3.258 ¥ (Análisis!C83), o cerca de la referencia de unos 2.000 ¥, pasaría el precio a dudoso o pasa.
    - Una caja libre del ejercicio a mar. 2027, neta de la devolución de anticipos, por debajo de 600 mm¥ haría fallar el filtro de caja.
    - ROIC por segmento sostenido por encima del 12 % durante un ciclo y en perímetro estable resolvería la duda de calidad a favor.

### Qué falta

    - ROIC y caja libre por segmento en un perímetro homogéneo de varios años, para juzgar foso y duración de retornos.
    - Calendario de devolución de los 3,05 billones ¥ de pasivos contractuales (anticipos) y su efecto real en la caja libre.
    - Pasivo por arrendamientos explícito a 30-jun-2026: la deuda sin arrendamientos de Control maestro!M51 es una estimación con arrendamientos a 31-mar.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres.",
          "Filtro balance: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

