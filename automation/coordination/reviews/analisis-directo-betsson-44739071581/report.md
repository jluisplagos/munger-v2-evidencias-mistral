# Análisis directo · Betsson, etapa 1 del universo (hoja del 2026-10-25)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | betsson |
| Fecha de corte | 2026-10-25 |
| Tasa | 9 % |
| Tarea | analisis-directo-betsson-44739071581 |
| SHA del código | 779b55abd380e8427650233fcb8a9c9fa74472f4 |
| Huella del paquete (package_sha256) | e8dcab3484736323d5a227b7f3957fc01542afad84d169846bba2853325c5cd7 |
| Huella del envío (bundle_sha256) | 11506e8ee06b59ccd420568a94f0620e3dba56249ec6ca0d448e5bb74122dadd |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 176900 tokens |
| Reserva estimada antes de llamar | USD 1.36296 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.36296 |
| Uso de tokens | entrada 78317, salida 22165 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.756568; cota 0.756568 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/betsson/etapa1/Betsson_respuesta.md | 779b55abd380 | a637521a9b8d5de0c31b535a496053b5b9414649c86789ab835344b08e01c331 | 50977 |
| hoja_analisis | datos_analisis_directo/betsson/etapa1/Betsson_evaluada__Análisis.csv | 779b55abd380 | 2334efd015826843243656d07a81b6994b4dd90511a853a8a18e5c4f3a5b94a1 | 24973 |
| hoja_guia_simply_wall_st | datos_analisis_directo/betsson/etapa1/Betsson_evaluada__Guía_Simply_Wall_St.csv | 779b55abd380 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/betsson/etapa1/Betsson_evaluada__Opciones.csv | 779b55abd380 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/betsson/etapa1/Betsson_evaluada__Control_maestro.csv | 779b55abd380 | 93c36358990165f8b3ab1e7c0e88f458bd4c162d890f252d75a235e67f7d2ced | 69828 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `pendiente_de_datos` · cubo «Vigilar» · acción `esperar` · zona `cumple_regla_k`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 74.97 | 0.3 |
| normal | 153.38 | 0.6 |
| bueno | 252.19 | 0.1 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 99.05 | |
| Precio del escenario malo | 74.97 | 74.97 |
| P* | 115.45 | 115.45 |
| Precio de Sí = mín(P*, V_normal) | 115.45 | 115.45 |
| Ponderado | 139.74 | 139.738 |
| Crecimiento implícito al precio actual / del normal (%) | -5.9 / 4 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 159.33 | 197.06 | cumple_regla_k |
| 8 % | 133.82 | 163.58 | cumple_regla_k |
| 9 % | 115.45 | 139.74 | cumple_regla_k |
| 10 % | 101.58 | 121.9 | cumple_regla_k |
| 11 % | 90.72 | 108.06 | vigilar |

### Resumen

    Betsson genera caja, tiene caja neta (−83,0 MEUR de deuda financiera neta) y sus ingresos crecen. Sin embargo, su margen se está comprimiendo por impuestos al juego y cambios regulatorios que fija cada Estado: el margen bruto ha bajado del 65,3 % al 55,5 % y el EBIT de 9M26 cae un 39 %. Brasil prohibió el juego online por decreto. Parto de los escenarios de la hoja, que reviso y hago míos: caja libre base LTM de 111,8 MEUR, crecimientos de −5 %, 4 % y 10 % y terminales del 1 %, 2 % y 2,5 %. Al 9 % salen 74,97, 153,38 y 252,19 SEK por acción. Con probabilidades 0,3/0,6/0,1, el ponderado es 139,74 SEK y el precio de Sí 115,45 SEK. El precio de 99,05 SEK queda en la zona que cumple la regla k = 3, pero con poco margen: basta un recorte de la caja base de alrededor del 14 % para que el precio iguale el precio de Sí. Falta un dato material: cuánto aportaba Brasil a la caja que sirve de base. Por eso el análisis queda pendiente de datos, en Vigilar y a la espera.


### Moneda

    SEK


### Justificación

    Con los escenarios al 9 % el precio cumple la regla k = 3, pero por poco: el precio de Sí está solo un 14 % por encima del precio actual. Los valores escalan linealmente con la caja base, de modo que un recorte de alrededor del 14 % de los 111,8 MEUR anula la holgura. La base LTM incluye Brasil, que quedó prohibido por decreto, y la empresa no publica cuánto aportaba: Latinoamérica es el 36 % de los ingresos del 3T26, sin desglose por país ni márgenes por mercado. Además, el escenario normal ya es generoso (terminal de 14,6x frente a 8,6x histórico). Por eso no compro y no concluyo. Tampoco lo dejo en Demasiado difícil: el riesgo regulatorio queda acotado por un escenario malo positivo y un balance con caja neta. Lo que falta es una cifra concreta, así que queda en Vigilar a la espera del dato.


### Probabilidades

    Uso 0,3/0,6/0,1 en lugar de 0,2/0,6/0,2 por tres motivos. Primero, el registro regulatorio de ocho años es asimétrico: ocho cambios adversos frente a uno favorable (Estonia). Segundo, la prohibición de Brasil (decreto del 25-9-2026, autorizaciones expiradas el 25-10-2026) aún no está recogida en la caja base LTM. Tercero, el escenario bueno exige dos cosas que no se han visto en seis trimestres: que el escalón fiscal se agote y que la inversión se convierta en margen. Con 0,2/0,6/0,2 el ponderado sería 157,46 SEK y el precio de Sí unos 133,9 SEK, así que la conclusión no depende de este cambio.


### Fórmula aplicada

    Valores en SEK al 9 %: Vm = 74,97, Vn = 153,38, Vb = 252,19; p = 0,3/0,6/0,1. Entre Vm y Vn: G(P) = 0,6·(153,38−P) + 0,1·(252,19−P) y L(P) = 0,3·(P−74,97). G = 3L da 1,6·P = 0,6·153,38 + 0,1·252,19 + 0,9·74,97 = 92,03 + 25,22 + 67,47 = 184,72, de donde P* = 115,45. Precio de Sí = mín(115,45; 153,38) = 115,45. Ponderado = 0,3·74,97 + 0,6·153,38 + 0,1·252,19 = 139,74. Zona: el precio de 99,05 está por encima de 74,97 y por debajo de 115,45, luego cumple_regla_k.


### Crecimiento implícito

    El modelo es de caja libre, no de ventas. Uso el crecimiento de la caja libre como aproximación al de las ventas suponiendo margen constante, que es lo que asume el escenario normal. Mantengo el normal desde el año 6 (+4 %), el terminal del 2 % y r = 9 %, y busco el crecimiento de los años 1 a 5 que iguala el valor al precio (8,8986 EUR, es decir 1.220,5 MEUR para 137,16 M de acciones). Por iteración sale ≈ −5,9 % anual. Como contraste, el DCF inverso de la hoja a 10 años da −1,93 % anual. En el normal la caja crece un 4 % y la etapa 1 atribuye a sus ventas en torno a un +5 %.

### Escenario malo

    Siguen llegando subidas de impuestos y prohibiciones, el B2B no recupera al cliente perdido y el margen bruto sigue bajando desde el 55,5 %. Caja libre: −5 % anual durante 10 años y g terminal del 1 %. La base es de 111,8 MEUR (CFO 196,3 − capex 72,3 − arrendamientos 8,6 − SBC 3,6) y hay 137,16 M de acciones diluidas. El resultado son 6,7349 EUR por acción (hoja, fila 78) × 11,1310 SEK/EUR = 74,97 SEK. Es un negocio sin deuda que encoge, no una quiebra.

### Escenario normal

    La cuota de ingresos con regulación local se acerca al techo y el escalón fiscal deja de crecer. Los ingresos crecen a un dígito medio, con Latinoamérica (36 % de los ingresos del 3T26, +51,8 %) compensando a los Nórdicos y al CEECA. Caja libre: +4 % anual durante 10 años y g terminal del 2 %. Resultado: 13,7797 EUR × 11,1310 = 153,38 SEK. Este escenario es generoso: su terminal implica 14,6x la caja libre frente a un P/FCF histórico medio de 8,6x. Con 8,6x de salida bajaría a unos 10,76 EUR (cálculo de la etapa 1).

### Escenario bueno

    El escalón fiscal se agota y la inversión de 2025-26 (capex LTM de 72,3 frente a una media de 3 años de 52,0) se traduce en apalancamiento operativo. Caja libre: +10 % anual durante 10 años, hasta unos 290 MEUR en el año 10, y g terminal del 2,5 %. Resultado: 22,6566 EUR × 11,1310 = 252,19 SEK.

### Sensibilidad (comentarios)

    7 %: Vm = 96,45, Vn = 217,13 y Vb = 378,46 SEK. El ponderado reconcilia con el de la hoja (17,70 EUR).
    8 %: Vm = 84,22, Vn = 179,91 y Vb = 303,64 SEK (cálculo propio).
    9 %: Coincide con la escalera. El ponderado es igual al de la hoja (12,554 EUR × 11,131).
    10 %: Vm = 67,70, Vn = 133,53 y Vb = 214,73 SEK. El precio queda solo un 2,5 % por debajo del precio de Sí.
    11 %: Vm = 61,83, Vn = 118,13 y Vb = 186,30 SEK. El ponderado reconcilia con la hoja (9,708 EUR). El precio supera el de Sí.

### Qué haría falsa la conclusión

    - Que el informe anual de 2026 o la empresa cuantifiquen Brasil por debajo de ~5 % de la caja libre o del EBIT del LTM. Eso mantendría la base y llevaría el análisis a concluido y probablemente a Sí a este precio.
    - Que Brasil (o el conjunto de pérdidas regulatorias) supere el ~15 % de la caja base. El precio quedaría por encima del precio de Sí y el cubo pasaría a No por precio.
    - Nuevas subidas de impuestos al juego en mercados grandes (gravamen del 3 % de la UE aprobado, Lituania al 30 %) o la pérdida de otra licencia relevante en 2027. Eso empujaría la probabilidad del escenario malo por encima de 0,3.
    - Que el margen bruto siga cayendo por debajo del 55,5 % dos trimestres más con la cuota regulada ya cerca del techo. Eso invalidaría la tesis de escalón de nivel en la que se apoya el escenario normal.
    - Que el margen bruto se mantenga plano dos trimestres y el B2B recupere ingresos con clientes nuevos. Eso reforzaría el normal y el bueno.
    - Un deterioro grande del goodwill (484,9 MEUR, el 36,5 % del activo, en una sola UGE) en el test de 2026, o una adquisición cara para compensar.
    - Una sentencia del Tribunal de Justicia de la UE que obligue a devolver pérdidas de jugadores o invalide contratos de juego con efecto material.

### Lo que no sabe

    - El efecto cuantificado de la prohibición de Brasil sobre ingresos, EBIT y caja: el informe del 3T26 da el hecho, no la cifra. Es el dato material que deja el análisis pendiente.
    - Márgenes por mercado o región: la empresa tiene un solo segmento operativo y no los publica.
    - Qué parte de los 284,7 MEUR de caja es restringida (saldos de jugadores 48,5, dividendo 44,4). No sumo caja en exceso, aunque la etapa 1 estima un exceso de 0,15 a 0,75 EUR por acción: es un sesgo conservador.
    - El precio de 99,05 SEK incluye el segundo pago de dividendo de 0,33 EUR (ex 10-11-2026). Sin él serían unos 8,57 EUR (~95,4 SEK), y el DCF no incluye esa caja.
    - Los flujos están en EUR y los convierto a SEK al tipo del BCE del 23-10-2026 (11,1310). No modelo el riesgo de tipo de cambio.
    - La respuesta de la etapa 1 está fechada el 28-10-2026 y varias decisiones de la hoja (base LTM, C28, C31) están fechadas el 28-oct-2026, después de la fecha de corte. No las uso como hechos: la elección de la base LTM la hago yo, con los datos disponibles antes del corte.
    - El precio sale de fuentes secundarias (comdirect, Nordnet), no de Nasdaq Nordic. La SBC del LTM es una estimación (el 3T no la desglosa) y las acciones diluidas (137,16 M) también son una estimación.
    - El crecimiento implícito es de caja libre, usada como aproximación a las ventas con margen constante. El modelo no separa ventas y márgenes.
    - No sé si el Parlamento brasileño ratificará el decreto, si se aprobará el gravamen europeo ni cómo resolverá el Tribunal de Justicia de la UE.
    - No conozco competidores ni la cuota de mercado de Betsson: ningún documento del paquete los nombra.

### Citas

    [hoja_control_maestro] «Cierre Nasdaq Stockholm 99,05 SEK (comdirect, Nordnet) ÷ BCE 11,1310 SEK/EUR» → Precio actual en SEK y tipo de cambio usado para convertir los valores
    [hoja_control_maestro] «99,05 / 11,1310 = 8,8986 EUR» → Precio en EUR usado por la hoja
    [hoja_control_maestro] «Incluye el 2º pago de dividendo 0,33 EUR (ex 10/11/2026): sin él ≈8,57 EUR.» → El precio incluye el dividendo pendiente
    [hoja_analisis] «Cash from Operations. Media de 3–5 años.,196.3» → CFO LTM de la caja base
    [hoja_analisis] «Capex: inversión en activos (mm),Capital Expenditures. Escríbelo en POSITIVO.,72.3» → Capex LTM
    [hoja_analisis] «8.6,ℹ se resta del FCF» → Principal de arrendamientos restado
    [hoja_analisis] «3.6,ℹ se resta del FCF» → SBC restada
    [hoja_analisis] «Aproximación al flujo del accionista si la financiación es razonablemente estable.,111.8» → Caja libre base de 111,8 MEUR
    [hoja_analisis] «Acciones diluidas (mm),Diluted shares outstanding.,137.16» → Número de acciones diluidas
    [hoja_analisis] «Crecimiento de la caja libre · años 1–10,-0.05,0.04,0.1» → Crecimientos de los tres escenarios
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.01,0.02,0.025» → Crecimientos terminales
    [hoja_analisis] «Probabilidad que le das,0.3,0.6,0.1» → Probabilidades usadas
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,6.73485391230823,13.7797443287183,22.6566123642373» → Valores por acción en EUR al 9 %, convertidos a SEK
    [hoja_analisis] «r − 2 pts (7.0%),16.629853160579,17.7034511275042» → Contraste del ponderado al 7 %
    [hoja_analisis] «r + 2 pts (11.0%),9.4611019525255,9.70787472143262» → Contraste del ponderado al 11 %
    [hoja_analisis] «DCF inverso: crecimiento de FCF (años 1–10) que haría que el valor fuese igual al precio actual.,-0.0193328523275794» → Crecimiento implícito a 10 años de la hoja
    [hoja_analisis] «ℹ 14.6x implícito vs 8.6x histórico · investiga la diferencia» → El terminal del escenario normal es generoso
    [hoja_control_maestro] «P/FCF histórico media 8,6x (mediana 7,6x; rango 6,9–13,2x)» → Múltiplo histórico de contraste
    [hoja_control_maestro] «FCF base resultante (sin SBC): 3a 180,8 / 5a 157,0 / LTM 115,4.» → Alternativas de caja base según el periodo
    [hoja_control_maestro] «se avisa de que el capex LTM (72,3) está por encima de la media de 3 años (52,0)» → La base LTM tiene un capex elevado
    [hoja_control_maestro] «bonos 173,8 + arrendamientos 27,9 − caja 284,7 = −83,0» → Caja neta
    [hoja_control_maestro] «exceso 20–102 → 0,15–0,75 EUR/acción» → Exceso de caja no sumado
    [hoja_control_maestro] «goodwill auditado 484,9 / activo total 1.328,0 = 36,5%» → Peso del goodwill
    [respuesta] «El informe del 3T26 da el hecho y la suspensión de depósitos y marketing, no la cifra.» → Dato material ausente sobre Brasil
    [respuesta] «y Brasil prohibiendo todo el juego online por decreto presidencial el 25-9-2026 con las autorizaciones expirando el 25-10-2026» → Prohibición de Brasil
    [respuesta] «Latinoamérica (36 % de los ingresos del 3T26, +51,8 %)» → Peso de Latinoamérica
    [respuesta] «Margen bruto trimestral 65,3 % (4T24) → 64,2 (3T25) → 60,5 (4T25) → 57,6 (1T26) → 57,2 (2T26) → 55,5 (3T26)» → Compresión del margen bruto
    [respuesta] «el ingreso de licencia B2B pasó de 76,9 a 46,7 MEUR en un trimestre» → Caída del B2B
    [respuesta] «a favor, solo Estonia del 6 % al 5,5 %. Ocho a uno no es simetría.» → Motivo de las probabilidades asimétricas
    [hoja_control_maestro] «Decisión del inversor (28-oct-2026): FCF base con LTM» → Decisiones fechadas después de la fecha de corte

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 115.44999999999999,
          "precio_si": 115.44999999999999,
          "ponderado": 139.738,
          "precio_escenario_malo": 74.97
        },
        "citas_total": 30,
        "citas_literales": 30,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

