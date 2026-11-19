# Encargo para Mistral · M12 · Borrador de la evaluación con la rúbrica (Ahold y Zoetis primer tiempo)

**Para pegar en una ventana nueva de Mistral.** Fecha: 19-nov-2026. Encarga: el coordinador Claude. Revisa y decide: un evaluador Claude distinto (Fable si hay cuota). **Tu trabajo es un borrador de evaluador independiente**: no valoras las empresas ni recomiendas nada; compruebas si las salidas del personaje cumplen lo que pide la rúbrica.

## Material
- **Rúbrica congelada:** `coordinacion/cierre_v2/examen/RUBRICA_EXAMEN.md` (huella en `RUBRICA_EXAMEN.sha256`; comprueba que coincide) — secciones 0, 1 (Ahold), 3 (Zoetis, solo el primer tiempo), 7, 8, 9 y 10.
- **Expedientes cerrados** (repo `jluisplagos/munger-v2`, rama `examen/expedientes-f1`, solo lectura), carpeta `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_examen_universo/`: `ahold_f4/Ahold` y `zoetis_t1d/Zoetis` (`fase_a.*`, `fase_b.*`, `fase_c.*`, `ficha.json`, `informe.md`, `precio.json`, `resultados.json`, `auditoria.md`, `extracto_v63.md`, `datos_v63.md`, `verificacion_entradas.json`).
- **Contradictor:** `coordinacion/cierre_v2/examen/contradictor/{ahold_f4,zoetis_t1d}/OBJECIONES.{json,md}`.
- **Análisis directo** (para la sección 10): rama `automatizacion/claude-api-piloto-registro`, `automation/coordination/reviews/analisis-directo-*/report.json` de Ahold y de Zoetis.

## Qué entregas
Para cada caso, la fila de la tabla de la sección 7 rellena (salida, ¿correcta?, S, E, G, m, K6, hechos con † encontrados, sensibilidad 7–11 % y prueba del 10 %, contradictor, resultado), **cada casilla con la cita del archivo y la línea/sección del expediente que la justifica**; la ficha del contradictor de la sección 9; y la comparación personaje frente a análisis directo de la sección 10. Donde no puedas decidir, escribe «duda» y por qué. Rama nueva **`mistral/m12-evaluacion`**, carpeta `resultados_examen/m12_evaluacion/`: `EVALUACION_AHOLD.md`, `EVALUACION_ZOETIS_T1.md` y `ENTREGA.md`. Commit y push.

### Frase para pegar
> Lee `coordinacion/cierre_v2/examen/evaluacion/ENCARGO_MISTRAL_M12_BORRADOR_EVALUACION.md` en la rama `coordinacion/cierre-v2` del repositorio `jluisplagos/munger-v2-evidencias-mistral` y hazlo entero. Entrega en la rama `mistral/m12-evaluacion`.
