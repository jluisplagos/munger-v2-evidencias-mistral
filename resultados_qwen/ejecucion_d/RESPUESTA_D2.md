# Respuesta D2-R1…R7 · frente D (Mistral D) · sobre `1ac661b`

- **Rama:** `mistral/d-qwen-aceptacion`. **Base revisada:** `1ac661b8efd954a5c79f91a493f9b082a9455e82` (REVISION_D_1ac661b.md / CORRECCION_D2.md de `coordinacion/cierre-v2@57b34a6`; sin cambios posteriores en esa rama: su HEAD sigue en 57b34a6 y ningún otro frente publicó respuesta D2).
- **Carpeta:** `resultados_qwen/ejecucion_d/`. **Alcance:** arnés y paquetes; no ejecuto el personaje (eso lo hace el runtime del coordinador con sus agentes configurados, según MECANISMO_PERSONAJE.md). No toco producto, CONTROL.json ni ESTADO.md.
- **Entorno real comprobado por comandos (2026-11-17):** Python 3.12.15 + openpyxl/lxml/pypdf/jsonschema (pip de usuario); git, gh, sha256sum, flock; **sin pdftotext ni soffice**. Candidata materializada en `/workspace/base_414_main`: main `d69d483` + base 4.14 (ZIP `munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip`, sha256 `bb51942c…7b93e` OK, `tools/base_414.py verify` complete=true 6798/6798) + checkout `957af652cdc3bef3d67e8623c9572138bac685e9` (`git rev-parse HEAD` = esperado, 0 cambios sin commit). Banco desde `git archive 4745f3887f7fd86bb3052f5d5e32285862df18e3` (no la punta de la rama): manifiesto 57/57 OK, `comprobar_banco.py` exit 0.
- **Modelo/herramientas de esta sesión:** mistral-large-4-0; ejecución local de los comandos documentados del producto (verificacion_entradas.py, ficha.py, informe.py, cambiar_base.py preparar). Sin agentes del producto ni LibreOffice.

## Resultado global tras la corrección (fuente única: evidencias/recuentos.json == MATRIZ_EJECUCION.csv)

- 36 casos: **29 PARCIAL_COMPONENTE / CUMPLE de componente** · **1 BLOQUEO_ENTORNO (Q1-026, no cuenta como CUMPLE)** · **6 NO_EJECUTADO** (Q1-028, Q1-030, Q1-031, Q1-032, Q1-033, Q1-035; Q1-028/Q1-032 con observación compartida declarada).
- Veredicto de caso: 29 sin veredicto (pendiente de agente) · 1 NO_OBSERVABLE · 4 sin veredicto · 2 DECISION_PENDIENTE (Q1-030/Q1-035, usuario). **0/36 casos completos del personaje** (igual que el control conocido).
- Criterios del banco: **109**; con aserción del arnés: 59; sin aserción (relevo declarado): 50 → `MAPA_CRITERIOS_BANCO.csv`.
- `pruebas_arnes.py`: **16/16 PASA** (log regenerado en `evidencias/pruebas_arnes.log`).
- Sondas D2 re-ejecutadas sobre el arnés corregido (`sondas/sondas_d2.json`): **P1–P9 todas DETECTA/OK** (sobre 1ac661b P1,P2,P3,P4,P5,P7,P8 eran falsos positivos y P9 acumulaba).

## D2-R1 · Rechazar resultados vacíos/forjados y evidencia fuera de ejecución — CORREGIDO

Cambios: `ejecutar_caso.py` v3 rechaza spec con `pasos`/`criterios` vacíos o criterio sin `afirma` (exit 2, ERROR_ESPECIFICACION); toda aserción se resuelve dentro de `evidencias/<caso>/` o de su RUN_DIR (`run:`), fuera → ERROR; `json_lista_no_contiene` exige `universo > 0` (una salida vacía no acredita); `generar_matriz.py` v3 da CUMPLE solo si el resultado tiene criterios no vacíos todos CUMPLE_COMPONENTE **y** `spec_sha256` coincide con la spec del disco.

| Prueba | Comando | Exit | Salida clave |
|---|---|---|---|
| Sondas P1–P9 | `python3 -I sondas/sondas_d2.py . $BANCO_DIR sondas/sondas_d2.json` | 0 | P1/P2/P3/P4/P5/P7/P8 → DETECTA; P6 DETECTA; P9 OK (`sondas/sondas_d2.json`) |
| pruebas 8–12 | `python3 -B scripts/pruebas_arnes.py` | 0 | 16/16 PASA, incl. P1 spec vacía rc 2, P3 ruta `../` rc 1 con error registrado, P4 forjado sin CUMPLE, P5 negativo sin universo FALLA |

## D2-R2 · Aserciones que prueban algo (control negativo por aserción) — CORREGIDO

- Prueba 15 de `pruebas_arnes.py`: **todas** las aserciones de las 28 specs se evalúan contra un estado previo vacío y **todas fallan** (`aserciones que pasaron en vacío: []`).
- Q1-026 C1 ya no acepta cualquier exit 1 con la subcadena: exige las líneas exactas de AR_2021..AR_2024 en `texto_pdf_faltante_pdftotext` y la presencia separada de ipal/AR_2019/AR_2020 en `otros_errores` (`errores_bloqueo.json`); la sonda P7 con un fallo ajeno («CAMBIO inválido… 'X.txt'») ahora FALLA → DETECTA.
- Q1-027: C2 discrimina (desactualizadas por sha256 + no comprobadas); la aserción `apto_por_entradas=false` quedó en C4 **etiquetada como no discriminante** (ya era false antes de la mutación por los 320 errores de contrato del universo).

## D2-R3 · Q1-026 alineado con el banco; Q1-027 corregido — CORREGIDO

- `CAMBIO_Q1-026.json` regenerado con las cifras del banco: **caja 95→90 millones EUR, deuda 300, deuda neta esperada 210**, cita exacta de `fixtures/f5_026_nota.txt`, bloque `evidencia` (Análisis!C24 E/M) restaurado, periodo 2025. Las cifras viejas (45.000/82.019/37.019, no presentes en el fixture) quedan fuera; `adaptaciones.json` Q1-026 coherente (antes se contradecía a sí mismo).
- La matriz clasifica Q1-026 como **BLOQUEO_ENTORNO** (spec con `bloqueo_entorno`), veredicto de componente vacío, caso NO_OBSERVABLE; ya no cuenta como CUMPLE.
- El stderr del bloqueo separa pdftotext (AR_2021..AR_2024) de ipal/AR_2019/AR_2020 en `evidencias/Q1-026/errores_bloqueo.json`; el paquete runtime del relevo usa las cifras del banco y advierte que pdftotext solo no basta.
- Q1-027: cifras del libro en miles (45054→80000 = 80 millones del fixture f5_027_excel.csv; deuda 300 millones citada); esperado del banco 300−80=220 declarado como observable solo con recálculo (relevo/soffice). Ejecución real: `OK Q1-027 · C1..C4 CUMPLE_COMPONENTE`, exit 0.
- Q1-026 escribe bajo RUN_DIR (nunca en la candidata; `origen_estado.txt` registra `candidata_escribe_el_arnes=false`) y siempre recrea el origen.

## D2-R4 · Relevos completos (Q1-028/Q1-032 especialmente) — CORREGIDO

`generar_relevo.py` v3: los 36 paquetes nombran `falta_para_caso_completo` con **qué, quién y qué necesita**; `comando_relevo: null` solo con `motivo_sin_comando`. Q1-028: reaprobación NUEVA con auditor real + deuda neta vigente 300+40−95=245 pendiente de verificar. Q1-032: recuento 4/1/5 del fixture sobre universo de 5 soportado (el real es 321) o NO_OBSERVABLE. Q1-031/Q1-033: fase A con agente real. Q1-030/Q1-035: decisión del usuario. Todos los ejecutados: recorrido del personaje con agente real. El paquete incluye `recorrido_personaje` (pasos 5/6/8/10/13, modelos sonnet-medio/opus-alto/opus-medio-nuevo, fase C dos turnos mismo agente, código 10 + ESPERANDO.md, sin API) y por caso los 109 criterios del banco con su aserción/cobertura. Ya no aparece «nada pendiente declarado».

## D2-R5 · Matriz y correspondencia de los 109 criterios — CORREGIDO

- `MAPA_CRITERIOS_BANCO.csv` (nuevo, `generar_correspondencia.py`): **109 filas** (36 casos × sus criterios_observables), con aserción del arnés (59) o «sin aserción» + relevo (50).
- `preserva_sentido` justificado caso a caso en `adaptaciones.json` (dato), ya no fijo "sí" en el código; `observacion_compartida` y `veredicto_caso_fijo` también como datos (antes escritos a mano en `generar_matriz.py`).
- Textos caducados corregidos: HALLAZGOS ya no dice 27/28; adaptaciones de Q1-025/Q1-034 actualizadas; `pruebas_arnes.py` re-ejecutado sobre el código entregado (16/16, log nuevo en `evidencias/pruebas_arnes.log`); prueba 5 ya no crea la carpeta de evidencias (control explícito rc 0 con 0 CUMPLE) y la prueba 7 compara de verdad recuentos.json con el CSV.

## D2-R6 · Manifiesto — CORREGIDO

`MANIFIESTO_SHA256.txt` regenerado tras todos los cambios: `cd resultados_qwen/ejecucion_d && sha256sum -c MANIFIESTO_SHA256.txt` → **exit 0** (antes fallaba RESUMEN_PARA_INTEGRADOR.md 3cee4cb3… vs c1c27880…).

## D2-R7 · Precondiciones simuladas rotuladas, aislamiento, procedencia — CORREGIDO

- (a) Toda comprobación escrita por el arnés lleva `_simulada: true` y `[SIMULADO]` en extractor/revisor, también las dadas como diccionario (Q1-002/Q1-020) y el `--revisor` del sellar (prueba 16 PASA: `marcadas=True revisor_sim=True`).
- (b) Una ejecución = carpeta de evidencias limpia: un log por ejecución (prueba 14 PASA: Q1-001 dos veces → 1 «# Caso» en el log; antes 9 casos acumulaban 2–3 ejecuciones).
- (c) `verificar_entorno` exige SHA observado == esperado **y** árbol sin cambios sin commit (prueba 13 P8 PASA: archivo rastreado modificado → rc 2 ERROR_ENTORNO); el resultado guarda `candidata_sha` observado, `banco_casos_sha256` y `spec_sha256`; `preparar_entorno.sh` ya no hace `base_414.py verify … || true` (falla si no está completa), saca el informe fuera del árbol del producto y extrae el banco desde el SHA fijado `4745f38…`, no desde la punta de la rama.

## Comandos de reproducción (desde contexto limpio)

```bash
bash scripts/preparar_entorno.sh            # candidata 957af65 + base 4.14 verificada + banco @4745f38 (SHA fijado)
bash scripts/ejecutar_todo.sh               # 28 specs + matriz + mapa + relevo; exit 0 (Q1-026 BLOQUEO_ENTORNO declarado)
python3 -B scripts/pruebas_arnes.py         # 16/16 PASA -> evidencias/pruebas_arnes.log
python3 -I sondas/sondas_d2.py . "$BANCO_DIR" sondas/sondas_d2.json   # P1-P9 DETECTA (stubs, no producto)
cd resultados_qwen/ejecucion_d && sha256sum -c MANIFIESTO_SHA256.txt  # exit 0
```

## Lo que se conserva y lo que no se afirma

Se conservan: la corrección D-R2 (artefacto heredado, P6 DETECTA), la detección de las sondas D de d375d80 (R1/R2 DETECTA), la declaración de **0 casos del personaje ejecutados**, la separación componente/caso y la naturaleza 31/3/2 del banco. No se afirma aptitud económica ni para dinero real; las precondiciones de extractor/revisor siguen SIMULADAS y rotuladas; los relevos de agente los ejecuta el runtime del coordinador.
