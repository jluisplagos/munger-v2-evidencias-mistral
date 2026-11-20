# Contradictor · Zoetis (ZTS) · zoetis_t1d

**Conclusión atacada:** concluido (provisional) · cubo Demasiado difícil · acción `demasiado_dificil`. El precio de Sí es 73,27 y el precio, 73,08. Es un «no comprar», así que busco solo por qué dejarla pasar sería un error (dirección «sube»). Encuentro **dos objeciones válidas**.

Rehice el motor B y reproduce la hoja al céntimo (`calc/motor_b.py`). Con k = 3 y probabilidades 0,3 / 0,5 / 0,2, el precio de Sí sale así: **P\* = 0,5625·MALO + 0,3125·NORMAL + 0,125·BUENO**.

## O1 · La empresa sí dice qué patentes vencen, y no son las de estas cuatro franquicias

- **Hecho.** El 10-K 2025 (p. 17) trae «a summary of our recent and upcoming key patent expirations». Solo nombra Draxxin, Excede y Cerenia, con vencimientos hasta 2028.
- **Por qué cuenta.**
  - La empresa anuncia estos vencimientos con años de antelación: ya en 2017 dio los de Cerenia, que llegaban a enero de 2027.
  - En ningún 10-K de 2016 a 2025 aparecen Apoquel, Simparica/Trio, Cytopoint ni Librela. Y no por pequeñas: en 2018 la lista recogía tres de los cuatro primeros productos, y no Apoquel.
  - Así que no es un dato ausente. Es un dato negativo: no hay ningún vencimiento clave anunciado de estas franquicias hasta 2028, y es probable que tampoco antes de 2030.
  - Además, el ROIC 0,08 del año 11 cobra dos veces rehacer el foso. La I+D (el 7 % de las ventas) ya está restada en el margen del 34 % que el terminal mantiene para siempre. Encima, el terminal reinvierte el 31 % del beneficio para crecer un 2,5 % (aviso V16 de la hoja).
- **Cuánto mueve.** Pongo el ROIC terminal del NORMAL en 0,11, el extremo alto del rango de la fase B y su propia regla para fechas posteriores a 2030.
  - El NORMAL pasa de 81,65 a **88,55**.
  - El precio de Sí pasa de 73,27 a **75,42**. El efecto va de +0 a +2,15 según la fecha real de vencimiento. Con 0,12 llegaría a 75,90.

## O2 · Draxxin es de ganado; el caso de compañía, Rimadyl, ya cabe en el MALO

- **Hecho.** El 10-K 2025 (p. 25) dice que Rimadyl y Draxxin han caído en EE. UU. desde que llegaron los genéricos «by 39% and 66%, respectively».
  - Rimadyl es un producto para perros. Draxxin es un antibiótico para vacuno, ovino y porcino (p. 14 y 15).
  - Rimadyl tenía genéricos desde 2016. Perdió un 23 % en cinco años y un 39 % en diez, con años de recuperación entremedias.
- **Por qué cuenta.**
  - La fase A dice que «el único precedente con cifras es Draxxin». La fase C dice que el MALO «no es un suelo», y de ahí deduce que no puede acotar el rango.
  - Pero el MALO ya hace caer dermatología y parasiticidas un 5–6 % al año. Es igual o más rápido que Rimadyl (≈ −5 % al año), y estas franquicias ni siquiera tienen genérico.
  - Para bajar del MALO hay que importar el caso de ganado. Aun así, Draxxin aplicado a Simparica y Apoquel deja el valor acotado, entre 47,6 y 54,4.
  - Y no es un cambio científico. Según la dirección, en dermatología entró un competidor nuevo que compite con promociones, y lo de Cytopoint es macro (llamada del T2, p. 13, 15 y 16).
- **Cuánto mueve.** El suelo documentado es el MALO, 57,20.
  - Con la regla B68 de la fase B (g 0,015 si la cartera vieja resiste como genérico con marca), el precio de Sí sube a **73,66**.
  - Sumando O1 y O2 llega a **75,81**: el precio queda un 3,6 % por debajo del precio de Sí, y no a 0,19 USD como ahora.

## Por qué cambia la conclusión, y su límite

El descalificador se apoya en dos patas: «no tengo las fechas» y «el rango no se acota». Los textos contestan las dos. Sin el descalificador, el orden de mando lleva a la zona: `cumple_regla_k`, con holgura.

Hay un límite: la zona depende del BUENO, que aporta el 71 % de la ganancia. Si el BUENO no sumara nada sobre el NORMAL, P\* sería 67,90 (71,31 con O1 y O2). Si la única duda que queda es la I+D, Demasiado difícil debe justificarse por eso, no por las fechas ni por Draxxin.

**Nota.** Fuera de las objeciones dejo tres cosas:
- Un detalle menor a favor: la caja de diciembre de 2025, con el año fiscal alineado, es 2.450 y no 2.312 (10-Q p. 5). Eso suma +0,32 a P\*.
- Vi hechos en contra que no desarrollo: una demanda colectiva de accionistas (10-Q p. 23) y una caída de Simparica Trio de 2 puntos de cuota en el trimestre.
- Con los datos de junio, P\* sería 73,14.

No cambio la tasa del 9 % ni propongo tamaños de posición.
