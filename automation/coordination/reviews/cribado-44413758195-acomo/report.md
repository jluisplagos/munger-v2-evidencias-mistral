# Cribado · Acomo

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-24 |
| Tarea | cribado-44413758195-acomo |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 65f747a32b93cf892d84eacb58789cb0c2169c144b0a3a6e49a307f7b367a017 |
| Huella del envío (bundle_sha256) | 9e8dfb3a10e8e2b99dd1986482e471612942d5557e5e394b81592ebe01e1694e |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | e77e0af10783dc1fa1586919ee1fe443d8664d9030f625757a0d317b2da8668d |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 149794 tokens |
| Reserva estimada antes de llamar | USD 1.254536 |
| Uso de tokens | entrada 67114, salida 3730 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.343056; cota 0.343056 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Acomo/Acomo_respuesta.md | 0cbe8a9a1b5c4f6b08e74f159f916cb3e629cb5802ba7fcaa3cca145e376d644 | 42816 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Acomo/Acomo_evaluada.xlsx#Análisis | 22ff7c538eb23b9d2c8b73be71c1d327924694dd15534e312ac100a26681b9a8 | 24632 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Acomo/Acomo_evaluada.xlsx#Control maestro | 4c647f57a6df8f28ef3f3e275bb4b082fbdefcad82c08e1894d4a7e7b1ac715f | 61486 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | no_pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 21.0 (pasivo por arrendamientos a 30-06-2026; incluido en Análisis!C54 = 369.8, que sin él queda en 348,8)


### Tipo de negocio y motor

    Intermediario y procesador de ingredientes alimentarios de origen vegetal (abastecimiento, trading, procesado y distribución); cíclico, ligado a materias primas e intensivo en circulante.
    Caja libre de ciclo medio: flujo antes de circulante menos una inversión normal en circulante a lo largo de un ciclo completo de precios de las materias primas, en lugar de la media de 3 años de la plantilla, dominada por el circulante.

### calidad

    El negocio se entiende y el margen de EBITDA ajustado es estable (7,3-8,1 %), pero el ROCE antes de impuestos del 12,9 % (12,5 % de media 2021-25) apenas supera la tasa del 9 % y no hay una ventaja que se vea en las cifras; además depende del ciclo de las materias primas.
    Dato clave: Análisis!C24 = 0.129

### caja

    La conversión de la caja operativa en beneficio neto es de 0,495 en 2021-2025, porque el circulante absorbió 269,7 mm€ (Control maestro!M31), y la caja libre reportada salta de 126,1 a -85,0 mm€ (LTM -7,2). Antes de circulante, el flujo se mantiene en 50-81 mm€ (Control maestro!M30), así que no está claro si el circulante es cíclico o estructural.
    Dato clave: Análisis!C26 = 0.495

### balance

    Sin arrendamientos, la deuda neta de unos 344,4 mm€ equivale a unas 3,09x el EBITDA pre-NIIF 16 estimado (Control maestro!N36) y a unas 17,6x la caja libre base de 19,58 mm€. Para un negocio cíclico es demasiado, y más con 4,4 mm€ de caja frente a 239,0 mm€ de deuda a corto (Control maestro!M37) y con el RCF y el préstamo a plazo que vencen el 30-12-2027 sin refinanciación anunciada. El 3,09x de Análisis!C33 incluye arrendamientos y no sirve tal cual; además, el EBITDA pre-NIIF 16 es una estimación de la hoja, no una cifra publicada.
    Dato clave: Control maestro!N51 = 348.8 (deuda bancaria sin arrendamientos; deuda neta ≈ 344,4 restando Análisis!C53 = 4.4)

### precio

    La cotización de 23,20 € está muy por encima del valor ponderado de 10,70 €, del precio de Sí de 6,70 € (Análisis!B78) y hasta del escenario bueno de 15,70 €, también con la tasa al 7 % (15,16 €). Pero el DCF de la plantilla no es fiable en un negocio dominado por el circulante: con el flujo antes de circulante, la respuesta estima 29,57 €, así que hace falta una caja de ciclo medio para concluir.
    Dato clave: Análisis!C83 = 10.7020976992352 frente a Análisis!C37 = 23.2

### encaje

    El paquete no trae la cartera de la persona responsable; la hoja solo clasifica la empresa como «Cíclica / commodity» (Análisis!C14), sin ningún dato concreto de encaje.
    Dato clave: Análisis!C14 = Cíclica / commodity

### Qué lo cambiaría

    - Que el RCF y el préstamo a plazo se refinancien a largo plazo con la deuda neta sin arrendamientos por debajo de 2,5x el EBITDA.
    - Dos años seguidos de caja libre reportada positiva y estable, por encima de 50 mm€, tras la reducción de circulante prevista para el segundo semestre de 2026.
    - Una caja libre de ciclo medio que dé un valor por acción claramente por encima de la cotización de 23,20 €.

### Qué falta

    - El EBITDA sin arrendamientos (pre-NIIF 16) publicado: la hoja solo lo estima, de modo que el 3,09x sin arrendamientos es una aproximación.
    - Una caja libre de ciclo medio con la inversión normal en circulante, y la posición neta larga o corta en materias primas de cada filial, que no se publica.
    - Los términos y el calendario de la refinanciación del RCF de 420 M€ y del préstamo a plazo que vencen el 30-12-2027.

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

