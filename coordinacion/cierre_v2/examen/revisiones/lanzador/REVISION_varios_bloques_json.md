# Revisión crítica independiente · varios bloques JSON y revalidación fuera de línea (93eeb79)

- Repositorio: `jluisplagos/munger-v2-evidencias-mistral`
- Rama `automatizacion/varios-bloques-json`, cabeza `93eeb7953ba110907de2a91e005077b702cc08f3`
  sobre `main` `3300424` (worktree `/home/user/e_work/wt_analisis_directo`, árbol limpio).
- Diff revisado: `git diff 3300424 automatizacion/varios-bloques-json`
  (`direct_analysis.py` +54/−13, `revalidar.py` nuevo, `test_direct_analysis.py` +45).
- Revisor: agente distinto del autor. No se ha modificado la rama ni hecho commit. Ninguna
  llamada a la API de Anthropic.
- Evidencia: rama `automatizacion/claude-api-piloto-registro` en `f8669b8`
  (`report.json` publicado en `fe870f7`), carpeta
  `automation/coordination/reviews/analisis-directo-ahold-44290314915/`.

## Veredicto

**CONFORME CON LÍMITES.**

La unión de bloques es estrecha y la revalidación de Ahold es correcta y reproducible byte a
byte. `revalidar.py` no toca reserva, tope ni registro y no presenta nada como aceptado. Los
límites: `revalidar.py` no comprueba que el paquete corresponda al informe ni restringe qué
errores originales puede «rescatar», y el README no recoge el cambio. Nada de esto invalida la
revalidación de Ahold, que verifiqué a mano. Conviene corregirlo antes de volver a usar la
herramienta.

## 1. Unión de bloques (`leer_respuesta`)

Orden de lectura: (a) objeto solo o un único bloque `` ```json ``; (b) **dos o más bloques
`` ```json ``, sin nada fuera salvo espacios en blanco**, cada uno un objeto, sin claves de
primer nivel repetidas entre bloques ni dentro de cada uno → unión superficial y nota
`objeto_json_partido_en_N_bloques_unido`; (c) si no, un único objeto con texto alrededor
(comportamiento anterior). Si hay varios bloques sin texto fuera y la unión falla, sale
`JSON_INVALIDO` directamente, sin pasar a (c). Después, `nulos_no_disponibles`,
`normalize_enums` y `check_schema` completos, como antes.

**¿Hace falta exigir que la unión tenga exactamente las claves del esquema?** No hace falta
añadir nada: `check_schema` ya exige `set(valor) == set(required)` en el primer nivel y en
cada objeto anidado (equivale a `additionalProperties: false` con todas las claves
obligatorias). Comprobado: una clave extra o una ausente en la unión dan
`ESQUEMA_INVALIDO:$`.

Pruebas propias sobre la salida real de Ahold (variantes construidas con sus dos bloques):

| Caso | Resultado |
|---|---|
| Salida original (2 bloques, `\n\n` entre ellos) | Acepta, con nota |
| Dos versiones completas seguidas | Rechaza `JSON_INVALIDO` (claves repetidas) |
| Versión completa + bloque de corrección `{cubo, accion}` | Rechaza `JSON_INVALIDO` |
| El esquema como bloque + el objeto | Rechaza `ESQUEMA_INVALIDO:$` |
| Un bloque que es una lista | Rechaza `JSON_INVALIDO` |
| Un objeto anidado partido (`escenarios` en dos bloques) | Rechaza `JSON_INVALIDO` |
| Texto entre bloques (también un espacio de ancho cero) | Rechaza `JSON_INVALIDO` |
| Segundo bloque con `` ``` `` sin etiqueta `json` | Rechaza `JSON_INVALIDO` |
| Clave extra o clave ausente en la unión | Rechaza `ESQUEMA_INVALIDO:$` |
| Bloques en orden inverso (citas primero) | Acepta, con nota |
| Tres bloques; o un bloque `{}` vacío en medio | Acepta («3 bloques») |
| Bloques pegados sin salto (`` ``````json ``) | Acepta, con nota |
| Borrador de 4 claves + resto de **otra** versión (cubo «sí» en el resto) | **Acepta**, con nota |
| Bloque «ejemplo» `{"resumen": "EJEMPLO"}` + el resto real sin `resumen` | **Acepta**, con nota |

Conclusión: no puede aceptar dos versiones completas del análisis, ni un ejemplo que repita
claves, ni el esquema, ni prosa intercalada. Lo que **no** puede distinguir es una partición
de claves disjuntas que procedan de borradores distintos, porque sintácticamente es idéntica
a la respuesta legítima. Es improbable sin texto entre bloques, y la salida en bruto se
conserva, pero es un límite real: la coherencia entre bloques solo la ve la revisión a
ciegas.

En la ejecución real la partición coincide exactamente con el orden del esquema: bloque 1 =
`resumen` … `justificacion_breve` (12 claves); bloque 2 = `que_la_haria_falsa`,
`lo_que_no_se`, `citas`. Entre ellos solo hay `"\n\n"`. Las dos partes no comparten claves,
y ninguna clave está repetida dentro de un bloque. Es la firma de un único objeto cortado,
no de dos respuestas.

## 2. `revalidar.py`

| Pregunta | Respuesta |
|---|---|
| ¿Llama a la red o a la API? | **No.** Solo lee dos archivos, ejecuta `git rev-parse HEAD` y llama a `da.validate` dentro de `da.configured(...)`. No invoca `cr.run`, ni `DirectHTTP`, ni `count_tokens`. |
| ¿Cambia la reserva, el tope o el registro? | **No.** Escribe solo `SALIDA_DIR/revalidacion.json`. `configured()` toca globales de `critical_review` en el proceso y los restaura; el `Decimal('5')` que pasa no se usa. No escribe en `reservation.json` ni en la rama de registro. |
| ¿Presenta el resultado como aceptado? | **No.** `estado = REVALIDADO_FUERA_DE_LINEA_PENDIENTE_DECISION_HUMANA`, `nota` «No es aceptación ni aptitud». No reutiliza el nombre `report.json` ni el estado `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`. |
| ¿Reproducible? | **Sí, en este caso.** Registra `report_sha256`, `sources_sha256` y `codigo_que_revalida` (HEAD). Ver límites R2 y R3. |

### Reproducción de Ahold 44290314915

```
git fetch origin automatizacion/claude-api-piloto-registro   # FETCH_HEAD = f8669b8
git show FETCH_HEAD:automation/coordination/reviews/analisis-directo-ahold-44290314915/{report,sources}.json
python3 -I automation/direct_analysis/revalidar.py report.json sources.json out/
→ {"estado": "REVALIDADO_FUERA_DE_LINEA_PENDIENTE_DECISION_HUMANA", "resultado": "VALIDO_CON_EL_VALIDADOR_ACTUAL", ...}  rc=0
```

- `out/revalidacion.json` es **idéntico byte a byte** al de
  `coordinacion/cierre_v2/examen/analisis_directo/ahold_44290314915/revalidacion.json`
  (sha256 `d8e21d7a…c308ccd`).
- Huellas: `report.json` `8962f4d6…a9fc7f`; `sources.json` `42f3ca89…bc072cad` =
  `bundle_sha256` del informe **y** de `reservation.json`. Además comprobé a mano que
  `package_sha256` (`3307053e…`) se recalcula igual desde `sources.json`, que las 12 fuentes
  coinciden con su `sha256` declarado y que `task_id` y `code_sha` (`3300424`) coinciden con
  los del informe. El paquete revalidado es, por tanto, exactamente el enviado.
- El informe original: `stop_reason=end_turn`, `api_messages_sent=1`, `error=JSON_INVALIDO`,
  `state=RESULTADO_NO_ACEPTADO_NO_REINTENTAR`, coste estimado 1,923 USD, reserva 4,505924 USD.
  Nada de eso cambia.
- Contenido revalidado (coincide con `LEEME.md`): `concluido · vigilar · esperar`; precio
  actual 36,05 (13-nov-2026); V = 23,38 / 34,68 / 47,10 con p = 0,2/0,6/0,2; escalera
  recalculada (Anexo C) P* = precio de Sí = 31,611, ponderado = 34,904, zona `caro`, igual que
  la declarada; 25 de 28 citas literales, con avisos en 20, 21 y 26. Las tres son de
  `fuentes_ad_q3_2026_interim_report_compact`, que existe en el paquete: son citas no
  literales, no archivos inventados. Única nota: `objeto_json_partido_en_2_bloques_unido`.
  No hubo normalizaciones de enumeraciones ni de `null`.

## 3. Reglas del repositorio (AUTO1) y riesgo de «reintentar gratis»

- **Una llamada, sin reintentos, aprobación humana:** se respetan. El cambio en línea no toca
  `cr.run`, la reserva, el tope ni el workflow. `revalidar.py` no hace ninguna inferencia: no
  es un reintento en el sentido de AUTO1 (no hay segundo gasto). El precedente de AUTO1 es
  `claude_review` en `mode=replay`, que revalida un resultado pagado sin llamar.
- **Riesgo de rescatar rechazos de contenido:** bajo hoy, pero la herramienta no lo impide.
  Las decisiones de contenido (revisión a ciegas, rúbrica) no están en `report.json`, así que
  `revalidar.py` no puede revertirlas. Pero la herramienta acepta **cualquier** informe con
  `end_turn` y le aplica el validador **del momento**, sea cual sea el error original. Probé
  con el mismo bruto: `error=ESQUEMA_INVALIDO:$.citas`, o un informe ya
  `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`, salen igualmente `VALIDO_CON_EL_VALIDADOR_ACTUAL`.
  El riesgo es acumulativo: aflojar `validate` poco a poco para recuperar salidas pagadas
  («ir buscando validador»). La mitigación actual es la etiqueta, la revisión del código y la
  decisión humana. Ver R1.
- **Desviación consciente de AUTO1:** el piloto de AUTO1 (`claude_review/pilot.py`) prueba y
  documenta «prosa/múltiples bloques rechazados». El análisis directo pasa a admitir varios
  bloques en su propio validador. AUTO1 no se ve afectado, pero es una decisión de política de
  forma que debería constar por escrito (R4).

## 4. Pruebas, exactamente como CI

```
python3 -I -m unittest discover -s automation/claude_review   -p 'test_*.py'  → Ran 49  OK
python3 -I -m unittest discover -s automation/coordination    -p 'test_*.py'  → Ran 97  OK
python3 -I -m unittest discover -s automation/direct_analysis -p 'test_*.py'  → Ran 46  OK
```

La prueba de `revalidar` imprime su línea JSON en stdout durante la ejecución (sin efecto).
Faltan pruebas para: bloque que no es objeto, unión con clave extra o ausente
(`ESQUEMA_INVALIDO`), `revalidar` con `stop_reason` distinto de `end_turn` (rc 1,
`SIN_SALIDA_COMPLETA_QUE_REVALIDAR`, comprobado a mano) y la rama `SIGUE_INVALIDO`.

## Hallazgos

| Id | Gravedad | Hallazgo | Propuesta |
|---|---|---|---|
| R1 | **Media** | `revalidar.py` no restringe qué errores originales revalida, ni muestra qué cambió entre el validador original (`report.code_sha`) y el actual. Cualquier relajación futura de `validate` rescataría en silencio salidas rechazadas por otras causas. | Admitir solo `error_original` de forma (p. ej. `JSON_INVALIDO`), salvo con un argumento explícito y anotado. Registrar `code_sha` original junto a `codigo_que_revalida`, y las notas que hicieron pasar la salida (ya van en `review.normalizaciones_enum`). |
| R2 | **Media** | No vincula el paquete con el informe: con un `sources.json` distinto (probé uno de una sola fuente y otra huella) sale `VALIDO_CON_EL_VALIDADOR_ACTUAL`, y las comprobaciones de citas pasan a referirse a otro material. En Ahold el vínculo se cumple (verificado a mano). | Exigir `sha256(sources.json) == report['bundle_sha256']` y que coincidan `task_id` y `code_sha`. Opcional: recalcular `package_sha256` y las huellas de cada fuente. AUTO1 `replay` exige el SHA del resultado pagado. |
| R3 | Baja | `codigo_que_revalida` es `git rev-parse HEAD` sin comprobar que el árbol está limpio: con cambios locales sin commit, el commit registrado no sería el código ejecutado. Tampoco se registra el commit de la rama de registro de donde salen los archivos. | Comparar `direct_analysis.py` y `revalidar.py` con `HEAD` (como `verify_code`) o registrar sus sha256. Admitir un argumento opcional con el commit de origen del registro. |
| R4 | Baja | El README del lanzador no se actualiza: no menciona la unión de bloques ni `revalidar.py`, y «Límites conocidos» sigue diciendo que un fallo de forma se revisa fuera de línea sin decir con qué herramienta ni con qué salvaguardas. Es una desviación consciente de AUTO1 («múltiples bloques rechazados»). | Documentarlo en el README: qué se une y qué no, el estado de salida y que no es aceptación. |
| R5 | Baja | Límite inherente: se unen particiones de claves disjuntas aunque vengan de borradores distintos, o un «ejemplo» de pocas claves seguido del resto. Se aceptan también bloques vacíos `{}` y cualquier orden. | Rechazar bloques vacíos. Anotar en la nota las claves de cada bloque (p. ej. `bloque 1: resumen…justificacion_breve`). Opcional: exigir que la concatenación siga el orden del esquema (la salida real lo cumple). |
| R6 | Baja | `revalidacion.json` no lleva `accepted=false`, `integrated=false` ni `product_executed=false`, como los informes y el `replay` de AUTO1. Un modelo no autorizado sale como `SIGUE_INVALIDO / MODELO_NO_AUTORIZADO`, que no es un problema de la salida. `configured()` no hace falta para `validate`. | Añadir los tres campos. Separar los errores de entrada (rc 2) de `SIGUE_INVALIDO`. |
| R7 | Baja (anterior al cambio) | La nueva regla del encargo cambia el texto de sistema: las ejecuciones posteriores (Zoetis, repetibilidad) no tendrán el mismo sistema que la de Ahold, aunque `encargo_sha256` del archivo no cambie. `system_sha256` solo se escribe en `preflight.json` cuando se aborta: no está en el `report.json` de Ahold, aunque el README diga que es «la huella del sistema enviado». | Incluir `system_sha256` en `report.json`. Al comparar ejecuciones, contrastar esa huella y no solo `package_sha256`. |

## Qué no se ha comprobado

- La calidad económica del análisis de Ahold ni la falta de literalidad de las citas 20, 21
  y 26, que corresponden a la revisión a ciegas.
- La conciliación del coste en Claude Console.
- Que la decisión de usar el análisis revalidado como entrada del examen esté registrada: le
  corresponde a la persona responsable.

## Respuesta del autor (coordinador)
- R1: `revalidar.py` solo admite rechazos de forma (`JSON_INVALIDO`); otros → `SOLO_SE_REVALIDAN_RECHAZOS_DE_FORMA`.
- R2: exige `bundle_sha256` del paquete = el del informe → si no, `PAQUETE_DISTINTO_DEL_ENVIADO`.
- Bajos: marca `+cambios_sin_confirmar` si el árbol de `automation/` no está limpio; `accepted`/`integrated`/`product_executed` = false; README con la desviación frente a AUTO1; pruebas nuevas (rechazos de contenido, otro paquete, `stop_reason` ≠ `end_turn`, bloques con claves extra/ausentes o no objeto). `system_sha256` en `report.json` queda para un cambio posterior (está en el preflight).
- La revalidación de 44290314915 se ha repetido con el código corregido y se ha reemplazado en `analisis_directo/ahold_44290314915/revalidacion.json`.
- CI local: 49 + 97 + 48 OK.
