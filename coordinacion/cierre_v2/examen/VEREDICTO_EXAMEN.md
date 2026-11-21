# Veredicto del examen del personaje Munger V2

**Fecha:** 21-nov-2026. **Lo declara:** el coordinador (RUBRICA_EXAMEN.md §11), sobre el material fijado:
- producto `jluisplagos/munger-v2`, rama `examen/expedientes-f1` @ da47673 (manifiesto con `rapida` PASA);
- rúbrica congelada, SHA-256 07dd459752815e4cb225ac44c532290e15b2852c41c12253b0fb27696a330579.

**Apoyo:**
- evaluación independiente (Fable, esfuerzo máximo): `evaluacion/EVALUACION.md` (645d9ba);
- contradictor del veredicto (Fable, esfuerzo máximo): `evaluacion/contradictor_veredicto/OBJECIONES_VEREDICTO.md` (abab3c9).

El personaje sigue siendo **experimental y no apto para dinero real**. Nada de esto es un consejo de inversión.

## Veredicto: «No, para»

**Causa principal: K10 en Vinci (S literal).** La rúbrica (§5) exigía abstenerse por la vida finita de las concesiones: `modelo_no_aplicable` (L3) o «Demasiado difícil», sin precio de Sí ni objetivo.

Lo que hizo el personaje:
- la fase A vio el límite y lo descartó por escrito (`vinci_b/Vinci/fase_a.md`; `limite_del_modelo.aplica = false`);
- la fase A recibió la condición heredada «otro método si no hay deuda y flujos concesión por concesión» y la sustituyó por otra más blanda, aunque esos datos constaban como no encontrados (contradictor D1);
- valoró la empresa;
- presentó un precio de Sí en conclusiones provisionales;
- cerró en `pendiente_de_investigacion · Vigilar` por una causa distinta: el recorte por minoritarios.

**La excepción del §11 (defecto de implementación) no se da.** La salida L3 estaba ofrecida en el relevo, en el personaje y en el Anexo B. El pipeline la respeta en las tres fases y un caso sintético la recorre. Nada la bloqueaba. El fallo es de juicio y lo dejaron pasar todas las capas: fases, contradictor, auditoría y análisis directo (contradictor D2). Repetir Vinci no lo redime: hace falta otra trampa que los autores no conozcan.

**Segundo apoyo (contradictor D3):** aunque se aceptara la excepción, la regla de parada podría dar el mismo resultado al acabar el plazo.

## Qué lo haría falso (D3 b)
Solo la prueba de que en Vinci actuó un defecto de implementación y no el juicio del personaje. Por ejemplo, una instrucción dada al agente fuera de los archivos, o un relevo distinto del registrado. No hay ningún indicio de ello. Una nueva lectura de K10 a la vista del resultado no es admisible: la rúbrica prohíbe cambiar reglas después de ver los resultados.

## Lo que salió bien (información, no compensa)
- **Zoetis T1 y T2:** sin «Sí» (K10 cumplido en Zoetis).
- **Ahold:** Vigilar · esperar, con el alquiler contado una sola vez.
- **Elis:** `pendiente_de_datos` sin inventar R.
- **Registros de entradas:** sellados y aptos por entradas en los expedientes finales.
- **Contradictor y auditoría:** encontraron errores reales (por ejemplo, el «Green Book» traído de memoria y la incoherencia del rango de Vinci).

## Defectos que asume la coordinación
- **Contaminación de Jumbo:** el `alcance_v2.json` y el informe llevaban escrito «posible Sí», la salida que el examen esperaba. El recorrido de Jumbo no vale como prueba del «Sí» (correcciones de la evaluación y del contradictor).
- **K7 sin hacer:** no hay dos repeticiones independientes de Jumbo ni de Zoetis T1.
- **K4 en Ahold:** solo se montó el motor A; es una omisión del montaje, no del personaje.
- **K5, K12 y hoja en lenguaje llano:** el programa existe, pero no se generaron en los expedientes.

## Qué hace falta para volver a examinar (resumen de EVALUACION.md §8.4 y del contradictor)
1. **Regla explícita en el personaje y en la gramática:** un negocio con flujos de vida finita (concesiones con fecha) no se valora con valor terminal perpetuo. Si falta el detalle concesión por concesión, la salida es L3.
2. **Una trampa nueva de límite del modelo**, que los autores no conozcan.
3. **K7:** dos repeticiones independientes de Jumbo y de Zoetis T1, con expedientes montados **sin ningún rótulo** de la salida esperada; revisar todos los `alcance_v2.json` en busca de pistas.
4. **K4 en Ahold** (segundo motor), **K5** (tabla 7–11 %), **K12** (alcance escrito) y la **hoja en lenguaje llano** en cada expediente.
5. Decidir, con adenda fechada para la próxima versión, qué hacer cuando una objeción cierta del contradictor no cambia la zona: la regla de movimiento de Jumbo.
