# Informe de revisión G-MANUAL · Mistral A (revisor independiente del autor)

- **Solicitud:** CONTROL.json @ `cdec2f5dab654a9149ed510475feae3ed2f0662f` → tarea G-MANUAL, `solicitud_revision.estado=LISTA`, `sha_autor=341831fd8b4c9081c09f1ebe7b31799042402d0f`, `base_revisada=957af652cdc3bef3d67e8623c9572138bac685e9`, diff_rutas `coordinacion/cierre_v2/manual/`, revisor asignado «Mistral A, en rama propia `mistral/g-manual-traspaso`, carpeta `resultados_cierre/manual_revision/` (reanudación c241a59)». No había rama remota `mistral/g-manual-traspaso` antes de esta revisión: no se duplica trabajo previo.
- **Base de esta rama:** `cdec2f5dab…` (control vigente, contiene el manual; el contenido de `coordinacion/cierre_v2/manual/` es idéntico a `341831f` — verificado con `git diff 341831f cdec2f5 -- coordinacion/cierre_v2/manual/` vacío). Rama A (`mistral/m2-cobertura-vm` @ `8b88fab`) intacta en su checkout original; esta revisión vive en worktree separado.
- **Material revisado:** `MANUAL_OPERATIVO_957af65.md` (503 líneas) y `CONTRADICCIONES_GUIA.md` (90 líneas) de `341831f`; fuentes del producto leídas solo con `git show` sobre `jluisplagos/munger-v2 @ 957af65`; evidencias `EVID/` y `PRUEBAS/` leídas sobre el auxiliar @ `9871f59`.
- **Método y distinciones:**
  - *Lectura documental ejecutada:* verificación de citas `archivo:línea`, hashes SHA-256 de §13, literalidad de comandos, tablas G-1…G-9 / O-1…O-18, requisitos S/LO/AG/RED de T-TRASPASO, manejo de I19/I20/H9, ausencia de políticas/valores. Script: `scripts/verificar_manual.py` → `verificacion_criterios.json` (11 hallazgos, todos CONFORME; checks adicionales de comandos y números de §5.2 contra los logs de `PRUEBAS/`).
  - *Comandos realmente ejecutados:* solo `git show`/`git ls-tree`/`git diff` (lectura) y `python3 -B verificar_manual.py` (sobre textos, exit 0). **Nada del producto ejecutado: ni pipeline, ni `verificar_paquete.sh`, ni LibreOffice, ni red, ni agentes.**
  - *No ejecutable en este entorno:* la prueba T-TRASPASO completa (pasos LO/AG) y cualquier afirmación de reproducción con LibreOffice — no se afirma.

## Resultado por criterio (los cinco de la solicitud)

1. **Cada afirmación operativa sale de su fuente `archivo:línea` en 957af65; ningún comando inventado — CONFORME.** 266 citas `archivo:línea` del manual+guía resueltas y dentro de rango (0 faltantes, 0 fuera de rango) contra producto@957af65 y auxiliar@9871f59. Los 30 hashes SHA-256 declarados en §13 coinciden exactamente con los archivos reales. Los 11 comandos en bloques del manual son literales de la fuente (p. ej. `gh release download base-4.14 …` en `README.md:41`; `base_414.py materialize/verify` en `README.md:42-43,51`; `bash verificar_paquete.sh completa`; `comprobar_entrega_4_14.py` en `CONTINUIDAD.md:131`; `sellar … --revisor …` = `verificacion_entradas.py:84`; los dos comandos pipeline con `config_v2_v64/v641_experimental.json` = `GUIA_RECORRIDO_SUPERVISADO.md:34`). Los [NO DOCUMENTADO] N-01…N-12 son ausencias reales del material (comprobadas en muestra: no hay comando de copia de los 1008 binarios ni de la copia limpia en las fuentes citadas).
2. **No reintroduce I19/I20 corregidos; H9/I19 marcado pendiente — CONFORME.** Verificado en código: `CONTINUIDAD.md:9` declara I19/I20 corregidos; `HITO_2_4_15.md:82-93` cubre I20 (`verificacion_entradas` en ficha/informe de todas las plantillas; `ficha.py:383-391`) e I19 (relevo caducado; `pipeline.py:1060-1083` `relevos_caducados`); `test_relevo_i19_415.py` existe con ≥5 pruebas `paso(...)` y exige `n>=5`; `HITO_2_4_15.md:92-93` declara H9 (vuelta siempre al paso 12) como límite abierto. El manual y la guía no presentan `--desde 12` como procedimiento vigente del relevo caducado y marcan H9 «pendiente de verificar por cambio afectado» (PROGRAMA.md:40 del control).
3. **No adopta política ni valores (R, θ, λ, probabilidades, k, umbrales); experimental supervisado, no apto para dinero real — CONFORME.** Búsqueda regex sobre manual+guía: ninguna asignación de parámetros; el manual declara «no adopta ni propone ningún valor» (§1) y «no apto para decisiones con dinero real» (`VERSION:1`, `HITO_2_4_15.md:8`, `CLAUDE.md:10`). VERSION real @957af65 = «4.15 · hito 2».
4. **Tabla G-1…G-9 y O-1…O-18 correcta y completa en lo afectado — CONFORME (alcance muestral).** Las 27 filas (9 G + 18 O, 77 citas) son alcanzables en 957af65/9871f59; muestra textual de 8 entradas verificada (G-1@GUIA:114 «Relevo caducado», G-2@98, G-7@1, G-8@14, O-1@CONTINUIDAD:351 I19, O-5@130-132 «quince», O-8@386-390 ZIP, O-15@PROMPT_DEL_AGENTE_RECEPTOR:31-32 «198/198»+«PASAN») — todas coinciden. La completitud absoluta no se puede probar por muestreo; el método queda registrado en `verificacion_criterios.json`. Las contradicciones C-01…C-13 del manual se confirman en muestra (C-01: `README.md:1`/`CLAUDE.md:1` dicen «hito 1»; C-03: `PROMPT_NUEVA_VENTANA.md:19` nombra `claude/hopeful-bardeen-qap6y0`).
5. **T-TRASPASO ejecutable por un receptor sin historial y separa LO/AG/RED — CONFORME (documental).** La tabla §10 tiene los 19 pasos con requisito S/LO/AG/RED y fuente por fila; la separación LibreOffice/agentes está explícita y es coherente con el código (`comprobar_entorno.sh` llama a `soffice`; `verificar_paquete.sh` ejecuta el bloque de entorno). Los números de §5.2 coinciden con los logs de pruebas del autor (`verificar_paquete_completa.log`: PASA global, 7762, 114/114, 199/199, 190/190, 62/62, 55/55; `comprobar_entrega_4_14.log`: 29/35; `PRUEBAS/README.md`: 22:18–23:18 UTC, flock, 1008 copiados). Esos logs son pruebas del autor de la candidata, no revisión independiente — el manual lo declara (§11).

## Clasificación

**CONFORME CON LÍMITES** para los cinco criterios, en el alcance de una revisión documental por muestreo (266/266 citas alcanzables; 30/30 hashes; 11/11 comandos literales; 8/8 muestras textuales G/O; 19/19 pasos T-TRASPASO con fuente).

## Límites de esta revisión (honestos)

- No se ejecutó nada del producto: ni `verificar_paquete.sh`, ni LibreOffice, ni agentes, ni red. T-TRASPASO queda **no ejecutado** (es la prueba pendiente del autor+receptor distinto).
- La verificación textual de citas es muestral (no las 266 línea a línea); la completitud de la tabla G/O se afirma «en lo afectado» según el método declarado, no exhaustiva.
- Los 12 [NO DOCUMENTADO] del manual son carencias reales del material del producto, no defectos del borrador: el borrador las marca bien.
- Este informe no acredita aptitud económica ni integra nada en el producto.

## Correcciones propuestas

- Ninguna material. Sugerencia menor (no corrección): en el bloque de comando de `sellar`, añadir la ruta completa `PV2/scripts/verificacion_entradas.py sellar …` para que el receptor no tenga que buscarla (ya está citada en CONTRADICCIONES_GUIA G-3).

## Evidencias

- `verificacion_criterios.json` (11 hallazgos CONFORME + chequeos adicionales), generado por `scripts/verificar_manual.py` (exit 0).
- `ENTREGA.json`, `PUNTO_DE_RECUPERACION.md`, `MANIFIESTO_SHA256.txt` en esta carpeta.
- Modelo: `mistral-large-4-0`; consumo/facturación no visible desde la sesión.
