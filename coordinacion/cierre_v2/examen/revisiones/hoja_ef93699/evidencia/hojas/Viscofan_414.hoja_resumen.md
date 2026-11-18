# Viscofan, S.A. (VIS (BME, Bolsa de Madrid, mercado continuo)) · hoja resumen

> Material de estudio en lenguaje llano, generado después del cierre a partir de las salidas oficiales. No es una salida oficial ni la sustituye; si la ficha cambia, esta hoja se regenera (`hoja_resumen.py`). Ficha leída: `1114e3fa7de3656c…`.

**Veredicto del personaje** — concluido · cubo **Vigilar** · acción **esperar** · precio de Sí **39,80 €** (precio actual 54,70 €, caro: por encima del valor ponderado) · **experimental; no apto para dinero real** — según la ficha, aptitud_de_uso de la entrega 4.14.

## En pocas palabras

Viscofan es el mayor fabricante de envolturas para embutidos y el único con todas las tecnologías (extracto: AR_2025 p. 180), con un ROIC de entre el 12,1 % y el 16,7 % en diez años y una cuota que subió del 30 % al 41 % entre los productores de envoltura a medida en 2015-2022. [1] Es un buen negocio, no uno extraordinario: las ventas crecieron un 71 % en la década, pero el margen EBIT bajó del 21,1 % al 16,4 %, el capital nuevo rindió en torno a un 9 % (filas 7 y 32) y el FCF al accionista de 2025 (93,8 M€) quedó por debajo del de 2019 (108,5 M€), mientras la deuda sube para repartir más de lo que genera. [2] La frontera con No es una sola: si la compresión del margen es estructural. [3] Viscofan transforma pieles bovinas, celulosa y gas en un insumo industrial y no ha sabido trasladar sus costes: el margen EBIT cayó del 21,1 % de 2016 al 15,1 % de 2023, las subidas de precio solo compensaron en parte en 2022 y 2023 (extracto: CF_2022 p. 93) y en 2025 la mezcla de precios bajó con volumen récord: la cuota se puede estar pagando con precio, frente a competidores que ni siquiera sé nombrar. [4] Si el margen sigue la pendiente de la década, mi MALO (29,78 €) es el caso central y 54,70 € pagan un 84 % más que él. [5] Que la compresión del margen sea estructural: un margen EBIT por debajo del 15 % dos años seguidos con volumen récord, o un desglose que muestre la cuota pagada con precio; también la deuda neta por encima de 1,5 veces el EBITDA por pagar al accionista (C98 pasaría a Dudosa) o una adquisición grande fuera del negocio. [6]

*Origen de cada frase* (fase_c.json, texto del personaje; solo se quitan las referencias a celdas y páginas, que están en el informe, §8 y §10): [1] tesis (Análisis!B101), frase 1 · [2] tesis (Análisis!B101), frase 2 · [3] tesis (Análisis!B101), frase 5 · [4] tesis inversa (Análisis!B102), frase 2 · [5] tesis inversa (Análisis!B102), frase 6 · [6] «qué me haría cambiar de cubo»: a No, frase 1.

## Lo que lo haría falso

*Texto del personaje* (fase_c.json: `cambiaria_de_cubo` y `decision.condiciones_revision`; sin referencias a corchetes de fuente):

- Pasaría a **No**: Que la compresión del margen sea estructural: un margen EBIT por debajo del 15 % dos años seguidos con volumen récord, o un desglose que muestre la cuota pagada con precio; también la deuda neta por encima de 1,5 veces el EBITDA por pagar al accionista (C98 pasaría a Dudosa) o una adquisición grande fuera del negocio.
- Pasaría a **Sí**: Un precio igual o inferior al precio de Sí (≤ 39,80 €, condicionado por la configuración) con el negocio intacto: margen EBIT de 2026 y 2027 en el 16 % o más con volumen al alza, cuota ganada con producto según el desglose de ventas, deuda bancaria neta por debajo de 1,5 veces el EBITDA, y saber quién es el competidor que más daño puede hacer (AR_2025 p. 399 no lo nombra). Antes de comprar, la comprobación conjunta tendría que superar las hipótesis de la configuración sin fundamento suficiente (estructura, θ, familia) y la lista D10 tendría que revisarse para esa compra.
- Pasaría a **Demasiado difícil**: Que el valor pase a depender de predecir el coste de las pieles bovinas o del dólar porque la empresa deja de repercutirlos (el descalificador de materias primas), que un sustituto cambie el volumen del mercado de envolturas (riesgo citado sin cuantificar) o que Danville se convierta en una contingencia que no pueda estimar.
- Revisión **a la baja**: Bajaría si el margen EBIT cae por debajo del 15 % con volumen récord (el MALO pasa a ser el caso central), si la deuda bancaria neta pasa de 1,5 veces el EBITDA por el reparto, o si se documenta que el exceso de inversión de 2021–2022 fue sobre todo reposición (θ alto: 38,13 € en la variante θ = 1, parametro_maximo, configuracion_v64_variantes.md). La dilución potencial del plan 2025–2027, no adoptada, lo llevaría a 39,53 € (incentivo objetivo) o 39,39 € (máximo) si se entregara con acciones nuevas (AR_2025.txt, PDF pp. 129–130; resultados/efecto_decisiones_viscofan.json).
- Revisión **al alza**: Subiría el precio de Sí si el margen EBIT publicado de 2026 y 2027 se sostiene en el 16,5 % o más con volumen al alza (el NORMAL deja de ser una hipótesis), si la descomposición de ventas muestra que la cuota se gana con producto y no con precio, o si se documenta que la inversión de 2021–2024 clasificada como «capacidad y maquinaria» fue crecimiento y no sustituyó capacidad existente (θ bajo: 41,47 € en la variante θ = 0, parametro_minimo, configuracion_v64_variantes.md).

## Cuánto depende de la tasa

Recalculado en copias del libro evaluado cambiando solo la tasa exigida (Análisis!C56). Precio actual: 54,70 €.

| Tasa | Precio de Sí | Valor ponderado | Dónde queda el precio actual | Crecimiento que el precio da por hecho (años 1–5) |
|---|---|---|---|---|
| 7 % | 57,92 € | 64,60 € | cumple: en el precio de Sí o por debajo | 0,9 % |
| 8 % | 47,39 € | 52,46 € | caro: por encima del valor ponderado | 5,5 % |
| 9 % (heredada) | 39,80 € | 43,81 € | caro: por encima del valor ponderado | 10,1 % |
| 10 % | 34,07 € | 37,33 € | caro: por encima del valor ponderado | 14,7 % |
| 11 % | 29,60 € | 32,30 € | caro: por encima del valor ponderado | 19,5 % |

- **El 9 % es provisional**: es la tasa heredada; la tasa no está decidida.
- **La prueba del 10 % es información, no condición.**
- Conclusión **firme: la zona no cambia entre el 8 y el 10 % (caro: por encima del valor ponderado)**.
- Comprobación: a la tasa heredada la copia reproduce exactamente el precio de Sí oficial de precio.json: **sí**.

## Predicciones fechadas

Se comprueban en esta fecha con este dato:

1. **31 de marzo de 2028** — Las ventas consolidadas de 2027 que publique Viscofan en su informe anual de 2027 estarán entre 1.300 y 1.420 M€ (1.252,0 M€ en 2025). Probabilidad que le da el personaje: 65 %.
2. **31 de marzo de 2028** — El margen de explotación de 2027 (resultado de explotación ÷ ventas consolidadas del informe anual de 2027) estará entre el 15,5 % y el 17,5 % (16,4 % en 2025). Probabilidad que le da el personaje: 65 %.
3. **31 de marzo de 2028** — La deuda bancaria neta a 31-dic-2027, con la definición de la empresa, no superará 1,5 veces el EBITDA de 2027 (206,1 M€ sobre 290,0 M€ de EBITDA, 0,71 veces, a 31-dic-2025). Probabilidad que le da el personaje: 70 %.

## Fechas y versión

- Análisis: 14 de noviembre de 2026.
- Datos base (último ejercicio de la Historia): ejercicio 2025 (cierre fiscal: diciembre).
- Precio: 3 de noviembre de 2026 (fase1_metadatos.json).
- Acciones: 31 de diciembre de 2025 (fase1_metadatos.json).
- Fuentes: documentos de los ejercicios 2016 a 2025 (10 ejercicios; fase1_fuentes.json).
- Versión del personaje: v2.2 · plantilla V6.4.1 experimental · configuración 0.2.2+v641exp.1 · hoja resumen 1.0.
