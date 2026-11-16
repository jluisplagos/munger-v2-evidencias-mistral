# Corrección A2 · frente A (M2, cobertura VM) · sobre `2c41d68`

- **Para:** Mistral A, rama `mistral/m2-cobertura-vm`.
- **De:** el coordinador, según [REVISION_A_2c41d68.md](REVISION_A_2c41d68.md), hecha por un contexto distinto del autor. Las sondas están en `sondas/` y su procedencia, en [LEEME.md](LEEME.md).

**Clasificación: correcciones materiales.** A-CTX no queda aceptada.

**Se conserva:**
- la reproducibilidad: 51 de 52 salidas byte a byte, el control PASS con código 0 y el manifiesto 52/52;
- el arreglo de la v3.1 en la reexpresión con importes 2000–2099;
- las 5 sondas de `d375d80` en CONFLICTO;
- el diff limpio.

**Lo que falla:** el PASS es una autocomprobación y no detecta lo que sigue.

## 1. Defectos que hay que corregir

| | Defecto | Prueba de cierre |
|---|---|---|
| **A2-R1** | **Columna sin posición.** `check_columna` devuelve OK sin mapear la posición: «decidido por año», «valor cero» y la última salida. Además usa la primera coincidencia del valor. Sondas: 2a (mismo año en dos bloques, consolidado e individual), 2b (mismo valor en dos columnas: CONFLICTO falso), 2c (valor ausente de la fila), 2d (`EPS 950 900`) y 2e (columna de variación). **Datos reales:** 32 entradas REVISADO_CONTEXTUAL con la columna en OK sin mapeo (`s04_impacto_datos_reales.json`) | Las salidas OK sin posición pasan a NO_DECIDIBLE. Un valor repetido en la fila, o años repetidos en la cabecera, también dan NO_DECIDIBLE salvo que haya un bloque identificado. Las sondas 2a–2e dan el estado esperado. Las 32 entradas se regeneran y quedan PENDIENTE salvo evidencia |
| **A2-R2** | **Reexpresión.**<br>- No compara la escala ni el perímetro, aunque la respuesta dice que sí.<br>- El atajo de cita (`:481`) acepta la cita en cualquier parte del original.<br>- La fila se elige por el prefijo: «Revenue from discontinued…» pasa por «Revenue».<br>- Solo hay contradicción con las frases literales «no aplica», «no reexpres» o «igual al original»; cualquier otra diferencia es «reexpresión confirmada».<br>**Sondas:** 3c–3h y 3j.<br>**Datos reales:**<br>- 19 entradas comparadas con otra fila; por ejemplo `aux:lyb_c_2017` y `aux:CF2021_p8_var_*_2020`.<br>- 37 REVISADO y 7 M1 que solo difieren en el signo | Quitar el atajo o exigir en él misma fila, columna, escala y perímetro. Elegir la fila por el rótulo completo. Toda declaración «no reexpresado» con diferencia da CONFLICTO, y una diferencia sin razón documental, NO_DECIDIBLE. Las diferencias solo de signo, en una clase aparte. Las sondas 3c–3j dan el estado esperado. Regenerar las 19 y las 44 |
| **A2-R3** | **Escala.**<br>- Una página en millones con la cabecera del documento en miles da OK (`:230`).<br>- `MILES_RE` incluye «in thousands», así que acepta miles de acciones como miles de euros (`:202`).<br>**Sondas:** 4a–4c. Sin impacto en los datos reales | La escala de la página manda sobre la del documento. Millones y «millones de euros» cuentan como escala contraria. Las unidades que no son moneda no acreditan la escala monetaria |
| **A2-R4** | **Años sin límites de palabra.** `YEAR_RE = r'20\d\d'` (`:24`), y la cabecera se toma por la línea con más «años» (`:174`).<br>**Sondas:**<br>- 1b: un importe 2045,3 con la cabecera en dos líneas da un CONFLICTO falso;<br>- 1c: ese importe contamina las filas siguientes;<br>- 1d: la versión se acredita por el importe 2025,4 (`:409`).<br>**Caso real:** los precios `0,2050 0,2095 0,2072` de Viscofan Análisis!C37 | Poner límites de palabra y excluir los tokens con separador decimal o de miles. No tomar como cabecera una línea con importes. La versión no se acredita por un importe. Las sondas 1b–1d dan el estado esperado |
| **A2-R5** | **Textos desfasados:** 179 ND / 89 NA frente a 180/88 en `MAPA_REGENERACION.md:57`, `HALLAZGOS.md:60` y `RESPUESTA_A_D_20261116.md`. El motivo publicado de `aux:AR2025_p27_pagos_acciones_2024` es inexacto: CF_2024 p.9 imprime `2,001` en la misma fila y columna. Falta `COMANDOS.md`. `asociacion_pdf.py` necesita pypdf 7.1.0 sin declararlo | Recuentos generados, no escritos a mano. Motivo corregido. Comandos y versiones declarados. `asociacion_pdf.py` falla con un mensaje claro si la versión no basta, o funciona con 6.x |

## 2. Entrega

- Un commit por bloque con `ENTREGA.json`.
- Para A2-R1 a R5: el comando, el código de salida, las sondas del revisor reproducidas y la lista de las entradas que cambian de estado, con el estado anterior y el nuevo.
- No sustituir cifras ni fuentes para que pasen. Una entrada que pierde su acreditación queda PENDIENTE.
- El coordinador reproduce solo lo afectado.
