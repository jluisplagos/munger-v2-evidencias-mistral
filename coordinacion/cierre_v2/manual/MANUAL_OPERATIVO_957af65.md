# Manual operativo de Munger V2 · candidata `integracion/candidata-cierre-v2` @ 957af65 · BORRADOR

**Estado de este documento:** borrador para revisión (tarea G-MANUAL; su prueba es T-TRASPASO). No es un documento del producto, no está integrado y no lo ha revisado nadie distinto de quien lo escribe. Se ha preparado solo leyendo archivos: no se ha ejecutado ningún comando del producto, ni LibreOffice, ni el pipeline, ni la red.

**Cómo leerlo.**
- Cada afirmación operativa lleva su fuente como `archivo:línea` (o un intervalo de líneas).
- **[NO DOCUMENTADO]** señala lo que el material no dice. **[CONTRADICCIÓN]** señala lo que dos fuentes dicen de forma incompatible. Los dos se recopilan en el §12.
- Los comandos son literales de la fuente citada. Este borrador no añade ninguno. Los marcadores `<…>` son de la fuente.

**Abreviaturas de rutas.** Las rutas son relativas a la raíz del repositorio del producto, salvo `EVID/`.

| Abreviatura | Ruta |
|---|---|
| `PV2/` | `munger_v2_r1/personaje_v2/` |
| `E414/` | `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/` |
| `E415/` | `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/` |
| `EVID/` | raíz del repositorio de evidencias de la coordinación (leído en el commit `9871f59`) |
| `PRUEBAS/` | `EVID/coordinacion/cierre_v2/pruebas_candidata/957af65/` |

---

## 1. Qué es y qué no es

- Munger V2 analiza empresas con una plantilla Excel (V6.3 y, solo con selección expresa, las V6.4 y V6.4.1 experimentales del motor B) y un personaje de juicio. Su pipeline tiene los pasos 0 a 14 y combina scripts deterministas con agentes (`munger_v2_r1/CONTINUIDAD.md:151`).
- **Versión de la candidata:** entrega 4.15 · hito 2, la corrección técnica tras la revisión externa del hito 1 (`munger_v2_r1/VERSION:1`). Commit `957af65`: «cierre del bloque técnico» (registro de Git de la candidata). Después de `0a0020b` solo cambia el texto del registro (`E415/hito2/HITO_2_4_15.md:113-115`, `E415/hito2/PUNTO_DE_RECUPERACION.md:3`).
- **Aptitud:** uso supervisado y experimental. **No es apto para decisiones con dinero real** (`munger_v2_r1/VERSION:1`, `E415/hito2/HITO_2_4_15.md:8`, `CLAUDE.md:10`).
- Superar los controles de software no acredita aptitud (`E415/hito2/HITO_2_4_15.md:8`, `EVID/coordinacion/cierre_v2/PROGRAMA.md:5`, `PRUEBAS/README.md:26`).
- La verificación de las entradas es una condición necesaria, no suficiente (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:36-37`, `E415/HITO_1_4_15.md:299`).
- Un recorrido produce un **análisis experimental**. No es una decisión de inversión ni aprueba ningún parámetro (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:3`). El resultado no se lee como una orden de compra o de venta (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:87`).
- **No cerrado** en la candidata:
  - F1: el motor A no está validado. Su ancla f cuenta dos veces los arrendamientos NIIF 16 y los intangibles adquiridos (`E415/hito2/HITO_2_4_15.md:192-193`).
  - Los expedientes Viscofan, Vidrala y Elis no se han regenerado ni auditado con extractor y revisor reales. Sus registros siguen «no aptos por entradas» (`E415/hito2/HITO_2_4_15.md:194-196`).
  - I19/H9, U1 y U6 (a), y los límites declarados (`E415/hito2/HITO_2_4_15.md:219-220`).
  - El alcance original no está completado (`E414/documentacion_cierre_4_14/HITO_2.md:68-72`).
- Poder leer el repositorio no autoriza a declarar completa la migración ni a iniciar el pipeline financiero (`CLAUDE.md:8`). Ningún trabajo de alcance nuevo empieza sin encargo (`munger_v2_r1/CONTINUIDAD.md:356`).
- **Configuraciones económicas.** Las de demostración o de ensayo no están adoptadas (`munger_v2_r1/CONTINUIDAD.md:69-70`, `munger_v2_r1/CONTINUIDAD.md:74`). `configuracion_economica.json` «no es una adopción» (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:8`). Ninguna convención de la V6.4 está adoptada (`munger_v2_r1/CONTINUIDAD.md:369`). Este manual no adopta ni propone ningún valor: ni R, θ, λ, probabilidades, k ni umbrales. Ningún agente los elige para desbloquear un caso (`EVID/coordinacion/cierre_v2/PROGRAMA.md:7`).

## 2. Reglas que rigen toda la operación

- Idioma: español claro, en tercera persona respecto de la persona responsable. Se distinguen hechos, interpretaciones y propuestas (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:32`).
- Modelos (`CLAUDE.md:28-31`, `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:33-35`):
  - Opus, con esfuerzo alto, para la coordinación y la implementación.
  - Fable, con esfuerzo máximo, de forma selectiva, con aviso y registro.
  - La revisión la hace un agente distinto del autor del cambio.
- No se modifican originales, fuentes ni huellas para legitimar un resultado. No se reactivan aprobaciones retiradas, no se aceptan auditorías de material distinto y no se inventan firmas ni política económica (`CLAUDE.md:22-26`, `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:38-40`).
- Se trabaja en ramas y expedientes nuevos. No se modifican `PV2/empresas_v2/` ni los expedientes anteriores (`munger_v2_r1/CONTINUIDAD.md:369`, `PV2/GUIA_RECORRIDO_SUPERVISADO.md:16`).
- **LibreOffice, siempre en secuencia.** Nunca dos tareas con LibreOffice a la vez: ni el pipeline, ni las baterías, ni los controles que recalculan. `comprobar_entorno.sh` también lo llama (`CLAUDE.md:24`, `munger_v2_r1/CONTINUIDAD.md:128`, `PV2/GUIA_RECORRIDO_SUPERVISADO.md:15`).
  - En una máquina compartida hace falta exclusión mutua verificable, por ejemplo con `flock`, y perfiles aislados (`EVID/coordinacion/cierre_v2/INTEGRACION.md:41`).
  - Las pruebas de la candidata usaron `flock -x` sobre un único archivo de bloqueo (`PRUEBAS/README.md:4`). La ruta del bloqueo y el comando completo **[NO DOCUMENTADO]**: la fuente lo abrevia como `flock -x … bash verificar_paquete.sh completa` (`PRUEBAS/README.md:21`).
- La IA no confirma ceros ni rellena los campos humanos (`decision`, `fecha`, `confirmado_por`) (`munger_v2_r1/CONTINUIDAD.md:376`).
- Un resultado que no se ha ejecutado no se presenta como ejecutado (`munger_v2_r1/CONTINUIDAD.md:375`).

## 3. Requisitos y comprobación del entorno

### 3.1 Requisitos

- Python 3.10 o posterior y GitHub CLI, para descargar la Release y materializar la base (`README.md:39`).
- Comprobados por `PV2/scripts/comprobar_entorno.sh`:
  - módulos de Python `openpyxl`, `lxml`, `pypdf` y `jsonschema` (`PV2/scripts/comprobar_entorno.sh:5-8`);
  - binarios `soffice` (LibreOffice) y `pdftotext` (`PV2/scripts/comprobar_entorno.sh:7`);
  - las rutas `plantilla.*` y `kit_v1.*` de la configuración activa: `MUNGER_CONFIG` o `config_v2.json` (`PV2/scripts/comprobar_entorno.sh:9-14`);
  - el autotest de `precio_de_si.py` (`PV2/scripts/comprobar_entorno.sh:20`).
  - El corpus Damodaran solo da AVISO si falta (`PV2/scripts/comprobar_entorno.sh:15-16`).
- Versiones registradas en las pruebas reales de la candidata: Python 3.13.18, LibreOffice 24.2.7.2, pdftotext 24.02.0 y openpyxl 3.1.5 (`PRUEBAS/README.md:4`). Hito 2: Git, Python 3.13.18, Bash 5.2.21, LibreOffice 24.2.7.2, pdftotext y GitHub CLI (`E415/hito2/HITO_2_4_15.md:14`). Versiones mínimas de LibreOffice y de las bibliotecas **[NO DOCUMENTADO]**.
- **Disco** (medido en la 4.14, sobre un ZIP) (`munger_v2_r1/CONTINUIDAD.md:133-138`):
  - la descompresión ocupa unos 1,9 GB;
  - la verificación completa deja unos 1,7 GB en `PV2/pruebas/_v64/`;
  - el control de la 4.8.1 usa unos 2 GB en `/tmp`;
  - conviene tener al menos 7 GB libres después de descomprimir.
  - El espacio necesario por la vía del repositorio **[NO DOCUMENTADO]**: clon de `main`, ZIP de 1,13 GB, base materializada y copia limpia.
- Para los recorridos reales hace falta una sesión que pueda lanzar agentes nuevos de contexto separado. Si no puede, se declara que la auditoría no es independiente (`munger_v2_r1/CONTINUIDAD.md:148`). La capacidad se comprueba con comandos, no por el nombre del modelo (`EVID/coordinacion/cierre_v2/PROGRAMA.md:13`). El comando para comprobar esa capacidad **[NO DOCUMENTADO]**.
- No se añaden credenciales al repositorio (`README.md:60`).

### 3.2 Comprobación

- En una sesión nueva, comprobar el acceso al repositorio, Python, LibreOffice y la descarga de la Release antes del pipeline (`README.md:58`).
- El comprobador es `PV2/scripts/comprobar_entorno.sh` (`README.md:58`). Se ejecuta desde `personaje_v2/` (`PV2/README_v2.md:24`, documento histórico). También es el paso 0 del pipeline (`PV2/scripts/comprobar_entorno.sh:2`) y el segundo bloque de `verificar_paquete.sh` (`munger_v2_r1/verificar_paquete.sh:65-69`).
  - Resultado esperado: código 0. Código 1 si falta algo (`PV2/scripts/comprobar_entorno.sh:2`).
  - **Llama a LibreOffice** (`soffice --version`): va en secuencia (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:15`).

## 4. Instalación y recuperación de los binarios

### 4.1 Principio

- La base histórica 4.14 tiene dos partes (`CLAUDE.md:7`, `README.md:13`):
  - 5790 archivos de texto en Git;
  - 1008 binarios, dentro del ZIP original de la Release `base-4.14`.
- El índice `baselines/4.14.json` lo confirma: `git` 5790 y `release_asset` 1008 (lectura directa del campo `storage` de `files`, hecha para este borrador).
- **Las herramientas de recuperación son exclusivas de la base histórica 4.14** (`CLAUDE.md:37`). La verificación de la 4.14 no se aplica al código modificado de la 4.15. El árbol de la 4.15 se contrasta con el `MANIFIESTO_SHA256.txt` de su rama (`README.md:5`, `README.md:56`).
- No se usan `base_414.py` ni `restore_assets_414.py` para una entrega posterior (`docs/RECEPCION_ENTREGA_CLAUDE.md:9`).
- La alternativa parcial (`baselines/4.14_assets.json`, `tools/restore_assets_414.py`) quedó sustituida por el ZIP completo (`README.md:62`, `CLAUDE.md:37`).
- `main` y el ZIP no se modifican (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:18`). La candidata no se sobrescribe con la base 4.14 (`EVID/coordinacion/cierre_v2/PROGRAMA.md:13`, `CLAUDE.md:35`).

### 4.2 Paso a paso

1. **Clonar `main`.** Recuperar y verificar allí los binarios. Después, pasar a la rama de la 4.15 (`README.md:5`, `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:15-19`). El comando de clonado **[NO DOCUMENTADO]**.
2. **Descargar el ZIP** de la Release `base-4.14`, desde la raíz del clon (`README.md:41`):

       gh release download base-4.14 --repo jluisplagos/munger-v2 --pattern munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip --dir .downloads

   - Si `gh release download` no funciona, se usa la API REST (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:15-16`, `E415/hito2/PUNTO_DE_RECUPERACION.md:55-56`):

         gh api -H "Accept: application/octet-stream" repos/jluisplagos/munger-v2/releases/assets/750814858 > <zip>

   - También vale la descarga manual (`README.md:45`).
   - `.downloads/` está en el `.gitignore` de la raíz (`.gitignore:26`).
3. **Comprobar el ZIP** (`README.md:33-35`):
   - tamaño: 1130912246 bytes;
   - SHA-256: `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e`.

   El comando para calcular la huella **[NO DOCUMENTADO]** en esta vía. La vía ZIP de CONTINUIDAD usa `sha256sum <zip>` (`munger_v2_r1/CONTINUIDAD.md:109`).
4. **Materializar y verificar la base 4.14**, en el clon de `main` (`README.md:42-43`):

       python tools/base_414.py materialize --source .downloads/munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip
       python tools/base_414.py verify --report docs/VERIFICACION_BASE_COMPLETA_LOCAL.json

   - Variante del mensaje de arranque: `python3 -I tools/base_414.py materialize --source <zip>` y después `verify` (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:17`).
   - **Esperado:** código 0, `complete: true` y 6798/6798, sin ningún archivo ausente o alterado (`README.md:46`, `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:18`).
   - El script verifica todo el origen antes de escribir y no sobrescribe un archivo distinto (`tools/base_414.py:111`, `tools/base_414.py:123`). Su código de salida es 0 solo si `complete` es verdadero (`tools/base_414.py:163`).
   - Solo lo versionado en Git: `python tools/base_414.py verify --git-only` (`README.md:51`).
5. **Obtener la candidata.** La rama es `integracion/candidata-cierre-v2` @ `957af65` (`EVID/coordinacion/cierre_v2/PROGRAMA.md:12`).
   - El mensaje de arranque nombra otra rama, la de trabajo del hito 2: `claude/hopeful-bardeen-qap6y0` (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:19`). **[CONTRADICCIÓN]** (C-03).
6. **Copiar los binarios a la 4.15.** Las pruebas reales de la candidata (`PRUEBAS/README.md:8-11`):
   - materializaron la base en un worktree aparte de `main`;
   - copiaron desde allí los 1008 binarios `release_asset` al worktree de la candidata, sin sobrescribir ninguno: 1008 copiados, 0 existentes, 0 distintos y 0 fallos tras la copia (`PRUEBAS/copia_binarios_candidata.json`).
   - El README del producto describe otra vía: cambiar de rama en el mismo clon (`README.md:5`).
   - **[NO DOCUMENTADO]**: ningún documento del producto da el comando ni el script de esta copia. Tampoco dice qué hacer si un binario de la 4.14 tiene una versión distinta en la 4.15. En la candidata no ocurre: el manifiesto pasa con los 1008 copiados (`PRUEBAS/README.md:11`).
7. **Verificar con el manifiesto propio de la candidata.**
   - `munger_v2_r1/MANIFIESTO_SHA256.txt` tiene 7762 entradas, todas salvo él mismo (`munger_v2_r1/MANIFIESTO_SHA256.txt:1`).
   - Resultado de las pruebas: 7762/7762, 0 ausentes y 0 fuera del manifiesto (`PRUEBAS/README.md:11`).
   - La comprobación es el primer bloque de `verificar_paquete.sh` y se hace antes de las pruebas (`munger_v2_r1/verificar_paquete.sh:28-29`, `munger_v2_r1/verificar_paquete.sh:38-63`). Un comando independiente del manifiesto **[NO DOCUMENTADO]**.
   - `git status` muestra 83 JSON sin seguimiento: son binarios de la 4.14 que el `.gitignore` no cubre. Están en el manifiesto y no se versionan (`PRUEBAS/README.md:12`, `E415/hito2/HITO_2_4_15.md:21`).

## 5. Verificación del paquete y resultados esperados

### 5.1 Cómo

- **Sobre una copia limpia** de `munger_v2_r1/`, sin `personaje_v2/.lo_perfil/` ni `__pycache__` (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:22`). El comando para hacer la copia **[NO DOCUMENTADO]**.
- Ejecutar desde la raíz `munger_v2_r1/` (`munger_v2_r1/verificar_paquete.sh:2-4`, `munger_v2_r1/CONTINUIDAD.md:110`):

      bash verificar_paquete.sh completa

- **Una sola vez por carpeta.** Las pruebas escriben dentro del árbol (`PV2/pruebas/`, `PV2/.lo_perfil/` y `.pyc`) y fuera (temporales y `~/.cache` de LibreOffice). Para repetir, hace falta una copia nueva (`munger_v2_r1/CONTINUIDAD.md:132`, `munger_v2_r1/verificar_paquete.sh:28-29`).
  - En la candidata, el primer intento se interrumpió por un reinicio del contenedor. No se reutilizó la carpeta: se repitió en una copia nueva (`PRUEBAS/README.md:20-21`).
- Duración:
  - 25–45 min según la documentación (`munger_v2_r1/CONTINUIDAD.md:110`, `PV2/GUIA_RECORRIDO_SUPERVISADO.md:14`);
  - en la candidata, de 22:18 a 23:18 UTC (`PRUEBAS/README.md:21`). **[CONTRADICCIÓN]** menor (C-11).
- **Modo rápido** (`bash verificar_paquete.sh`, sin `completa`): manifiesto, entorno, piloto y `test_comprobadores.py` (`munger_v2_r1/verificar_paquete.sh:3`, `PV2/pruebas/ejecutar_pruebas_reparacion.sh:18`). Su PASA solo cubre lo que lista (`munger_v2_r1/verificar_paquete.sh:26`). Ningún modo sustituye a los controles de los expedientes reales ni a sus auditorías (`munger_v2_r1/verificar_paquete.sh:27`).

### 5.2 Resultado esperado de `completa` en la candidata

- Valores de referencia: `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:23-26`, `munger_v2_r1/CONTINUIDAD.md:111-126` y `E415/hito2/PUNTO_DE_RECUPERACION.md:10-13`.
- Obtenido en la candidata, código 0: `PRUEBAS/verificar_paquete_completa.log:4-59`.

| Bloque | Esperado | Mínimo exigido | Obtenido en 957af65 |
|---|---|---|---|
| Manifiesto | 0 modificados · 0 ausentes · 0 de más | — | 7762 · 0 · 0 · 0 (`PRUEBAS/verificar_paquete_completa.log:4-5`) |
| Entorno | PASA | — | PASA (`…log:7-8`) |
| Piloto Vidrala 2025 | 35 CUMPLEN, salida idéntica a la de referencia | — | PASA (`…log:10-11`) |
| `test_comprobadores.py` | 114/114 | — | 114/114 (`…log:14`) |
| `test_pipeline_sintetico.py` | 30/30, con los nombres de la línea de base v2.2 | — | 30/30 · faltan 0 · nuevas 0 (`…log:16-19`) |
| Vigencia H5 | 59/59 | 59 (`verificar_paquete.sh:95`) | 59/59 |
| Juicio sobre el objetivo | 27/27 | 27 (`:114`) | 27/27 |
| Entradas 4.14 | 33/33 | 33 (`:133`) | 33/33 |
| Entradas 4.15 | 190/190 | 190 (`:152`) | 190/190 |
| Entrada efectiva | 62/62 | 62 (`:171`) | 62/62 |
| Relevo caducado (LibreOffice) | 5/5 | 5 (`:190`) | 5/5 |
| Integración V6.4 | 199/199 | 199 (`:209`) | 199/199 |
| Trazabilidad | 78/78 | 78 (`:228`) | 78/78 |
| Integridad de la auditoría | 103/103 | 103 (`:247`) | 103/103 |
| Solicitudes de auditoría | 55/55 | 55 (`:266`) | 55/55 |
| Estados | 28/28 | 28 (`:285`) | 28/28 |
| Resumen | 45/45 | 45 (`:304`) | 45/45 |
| Cierre | 55/55 | 55 (`:323`) | 55/55 |
| **Global** | `RESULTADO GLOBAL: PASA`, código 0 | — | PASA (`…log:59`; `PRUEBAS/README.md:21`) |

- En «completa», las quince baterías son obligatorias. Si una falla, no se ejecuta o tiene menos pruebas que el mínimo, el resultado es FALLA (`munger_v2_r1/CONTINUIDAD.md:130`, `munger_v2_r1/verificar_paquete.sh:332-333`).
- Usan LibreOffice: `test_comprobadores.py`, la sintética, `test_integracion_v64.py`, `test_estados_v2.py`, `test_cierre_v2.py`, `test_resumen_v2.py` (`munger_v2_r1/CONTINUIDAD.md:128`) y `test_relevo_i19_415.py` (`munger_v2_r1/verificar_paquete.sh:24-25`, `PV2/pruebas/test_relevo_i19_415.py:10`).

### 5.3 Después, sobre la misma copia: control de la 4.14

- Comando (`munger_v2_r1/CONTINUIDAD.md:131`):

      python3 -I -B personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/scripts/comprobar_entrega_4_14.py

- **Esperado sobre un clon Git: 29/35, código 1** (`munger_v2_r1/CONTINUIDAD.md:131`, `E415/hito2/HITO_2_4_15.md:122-123`). Obtenido en la candidata: 29/35 (`PRUEBAS/comprobar_entrega_4_14.log:36`, `PRUEBAS/README.md:22`). Las seis FALLA esperadas son:
  - tres verificaciones de las entradas de los expedientes finales de la 4.14, «no apto por entradas» por diseño con las reglas de la 4.15 (`PRUEBAS/comprobar_entrega_4_14.log:7,15,23`, `E415/HITO_1_4_15.md:211`);
  - tres fechas de archivo que Git no conserva, con el contenido idéntico al manifiesto (`PRUEBAS/comprobar_entrega_4_14.log:10,18,26`, `munger_v2_r1/CONTINUIDAD.md:131`).
- Sobre una descompresión del ZIP se esperaba 32/35 (`munger_v2_r1/CONTINUIDAD.md:131`). La 4.15 no tiene un ZIP completo: el paquete del hito 2 es de cambios y no se versiona (`E415/hito2/HITO_2_4_15.md:183-187`).
- **No se da por superado** (`E415/hito2/HITO_2_4_15.md:123`).
- **Controles de las entregas anteriores** (`E414/resultados/LEEME_CONTROLES_HISTORICOS_4_14.md`):
  - Ese LEEME describe el árbol 4.14, no el 4.15 (`E414/resultados/LEEME_CONTROLES_HISTORICOS_4_14.md:1-3`).
  - CONTINUIDAD dice que «sustituye, para este árbol, al de la 4.13» (`munger_v2_r1/CONTINUIDAD.md:131`).
  - El resultado esperado sobre el árbol 4.15 **[NO DOCUMENTADO]**. En la candidata no se ejecutaron (`PRUEBAS/README.md:24`).

## 6. Recorrido supervisado de una empresa

> Requiere encargo expreso (`CLAUDE.md:8`, `munger_v2_r1/CONTINUIDAD.md:356`). Se hace en un expediente nuevo y con agentes reales (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:16`, `PV2/GUIA_RECORRIDO_SUPERVISADO.md:85`). La guía es de la 4.13/4.14 y el hito 2 no la reescribió (`E415/hito2/HITO_2_4_15.md:199-200`). Lo que ya no vale está en `CONTRADICCIONES_GUIA.md`.

### 6.1 Preparar el expediente

- **Nueva base económica o corrección de datos de un expediente cerrado:** se escribe un `CAMBIO.json` (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:20`, `PV2/GUIA_RECORRIDO_SUPERVISADO.md:100`) y se ejecuta:

      python3 -I personaje_v2/scripts/cambiar_base.py preparar CAMBIO.json

  - Crea un expediente nuevo y nunca sobrescribe el origen (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:100`, `PV2/scripts/cambiar_base.py:4-5`).
  - Una corrección de la Historia va en `correcciones_fase1_partes` (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:101`).
  - Si se perdiera una entrada `analisis` del origen, la preparación se detiene (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:102`).
- **Novedades del hito 1, que la guía no recoge:**
  - las entradas `analisis` se declaran con su cálculo;
  - las heredadas del origen se reconocen con `analisis_que_se_conservan` / `_que_se_descartan` (`E415/HITO_1_4_15.md:145-148`);
  - `cambiar_base.py` escribe por defecto `entrada_efectiva.json` en modo «estricta» en todo expediente nuevo. En ese modo, `rellenar_fase1_v63.py --estricta` se detiene con código 7 si una entrada del FCF base depende de un valor migrado (`E415/HITO_1_4_15.md:149-151`, `munger_v2_r1/CONTINUIDAD.md:16`).
  - Por lectura del código, esa parada termina el expediente en `pendiente_de_datos` en el paso 2 (`PV2/scripts/pipeline.py:667-669`). Cómo resolverla **[NO DOCUMENTADO]** en la guía.
- **Modo de la entrada efectiva** (`E415/hito2/HITO_2_4_15.md:74-76`):
  - un `entrada_efectiva.json` ilegible, con una errata o con un modo distinto del declarado detiene el paso 2;
  - sin ningún rastro del modo, se aplica «registrada» (límite U6 (a)).
- **Configuración económica (motor B):** la escribe la orquestación, nunca un agente de juicio (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:8`).
  - Lleva su trazabilidad (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:23-29`) y se valida con:

        python3 -B personaje_v2/scripts/configuracion_economica.py validar configuracion_economica.json

    (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:30`).
  - Ningún parámetro, protocolo ni perímetro queda adoptado (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:26-29`).

### 6.2 Registro de las entradas (verificación de las entradas financieras)

- Plantilla del registro: `python3 -B scripts/verificacion_entradas.py plantilla CARPETA`, desde `personaje_v2/`. Se hace en una copia (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:94`). Escribe `verificacion_entradas.plantilla.json` (`PV2/scripts/verificacion_entradas.py:83`).
- **El extractor** rellena cada entrada (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:95`). Reglas añadidas en la 4.15:
  - `pagina` es la página del PDF, un entero; el folio impreso va aparte, en `folio`. Una página inexistente es una discrepancia (`E415/HITO_1_4_15.md:19-21`).
  - Una fuente local tiene que existir dentro del expediente o del paquete y llevar su sha256 vigente. Si no, la entrada queda pendiente (`E415/HITO_1_4_15.md:26-27`).
  - Una lectura externa no cuenta como comprobada (`E415/HITO_1_4_15.md:28`).
  - Las cifras tienen que ser numéricamente equivalentes, sin redondeo (`E415/HITO_1_4_15.md:32-37`).
  - `valor_fuente` es la cifra **publicada, con su signo**. `signo` y `escala` son la transformación posterior. Un signo −1 exige su `tratamiento` (`E415/hito2/HITO_2_4_15.md:30`, `E415/hito2/HITO_2_4_15.md:42-43`).
  - El universo incluye las cifras que usan las fases de juicio (`ambito = "juicio"`) (`munger_v2_r1/CONTINUIDAD.md:15`).
- **El revisor, distinto del extractor**, comprueba cada entrada. Desde la 4.15 solo vale lo que sella con (`PV2/scripts/verificacion_entradas.py:84`, `E415/HITO_1_4_15.md:55-61`):

      verificacion_entradas.py sellar <expediente> --revisor NOMBRE --fecha AAAA-MM-DD(hoy) CELDA [CELDA …]

  - Sin vínculo, la comprobación queda pendiente. Si cambia lo vinculado, queda desactualizada (`E415/HITO_1_4_15.md:53-54`).
  - El vínculo detecta cambios, pero no acredita autoría (`E415/HITO_1_4_15.md:63`).
- Comprobación: `python3 -B scripts/verificacion_entradas.py comprobar CARPETA` (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:97`). El pipeline la repite en el paso 12 (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:97`).
- Un registro no apto no impide recorrer el pipeline, y ninguna salida se presenta como apta para dinero real (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:98`, primera frase).
- Las firmas no se simulan. La revisión del significado económico de cada derivado (U1) la hace un revisor independiente (`E415/hito2/HITO_2_4_15.md:194-196`, `E415/hito2/HITO_2_4_15.md:66-68`).

### 6.3 Ejecutar el pipeline

- Comandos por plantilla. La selección es siempre explícita (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:34`, `PV2/GUIA_RECORRIDO_SUPERVISADO.md:105-107`):

      python3 personaje_v2/scripts/pipeline.py CARPETA --config personaje_v2/config_v2_v64_experimental.json     (V6.4, motor B)
      python3 personaje_v2/scripts/pipeline.py CARPETA --config personaje_v2/config_v2_v641_experimental.json    (V6.4.1)

  - Motor A: `--config config_v2.json` (V6.3) (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:107`).
  - Opciones: `[--config …] [--agentes-simulados DIR] [--hasta N] [--reiniciar] [--desde N]` (`PV2/scripts/pipeline.py:4`).
  - `--agentes-simulados` solo vale para pruebas técnicas, nunca en un expediente real (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:49`, `PV2/GUIA_RECORRIDO_SUPERVISADO.md:85`).
- Una pasada que guarda la salida completa: `…_4_13/scripts/paso_pipeline.py CARPETA [--config …]` (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:34`).
- Códigos de salida (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:36-43`):

| Código | Qué significa | Qué se hace |
|---|---|---|
| 0 | terminado: concluido, pendiente o no entregable, con su diagnóstico | leer la ficha, el informe y `diagnostico.md` |
| 10 | espera a un agente (`ESPERANDO.md`, `prompts_generados/`) | lanzar el agente y volver a ejecutar |
| 2 | parada sin escribir: selección, configuración o material incoherentes | corregir la causa; no forzar |
| 3 | límite del modelo | es un resultado legítimo; se documenta |
| 5 | retirada de una aprobación pendiente de registrar | volver a ejecutar cuando el resumen sea escribible |
| 6 | estado del pipeline o registro de auditorías ilegible | restaurar desde una copia o relanzar con `--reiniciar`; nunca seguir como aprobado |

- **LibreOffice en secuencia.** El pipeline recalcula y su paso 0 llama a LibreOffice, así que nunca corre junto a otra prueba o control (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:15`).

### 6.4 Relevos (código 10) con agentes reales en contextos separados

- Cada relevo se resuelve con un agente real (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:45-49`):
  - el agente recibe el prompt generado, `prompts_generados/NN_<fase>.md`;
  - modelo y esfuerzo, según `modelos` de la configuración: extracción, Sonnet medio; fases A, B y C, Opus alto; verificación, Opus medio (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:46`). Los mismos valores constan en `PV2/config_v2.json` y `PV2/config_v2_v64_experimental.json` → `modelos`;
  - reglas: escribe solo su salida; sin internet ni memoria; no ejecuta el pipeline ni LibreOffice; no abre Excel (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:47`).
- **La fase C tiene dos turnos con el mismo agente**: se continúa su conversación (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:48`, `EVID/coordinacion/cierre_v2/PROGRAMA.md:38`).
- **Cada auditoría la hace un agente nuevo, de contexto separado** (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:60`, `munger_v2_r1/CONTINUIDAD.md:148`):
  - sin contexto del trabajo y sin que se le diga qué se espera (`PV2/PROMPT_CLAUDE_CODE.md:30`, documento histórico);
  - el actor y el contexto tienen que ser distintos de quien produjo el material (`EVID/coordinacion/cierre_v2/PROGRAMA.md:38`);
  - si no se puede lanzar, se declara que la auditoría no es independiente (`munger_v2_r1/CONTINUIDAD.md:148`).
  - Precedente: en la prueba de traspaso de la 4.14, la auditoría la hizo el mismo receptor (`E414/documentacion_cierre_4_14/traspaso/LEEME_TRASPASO.md:15`).
- Orden habitual: extracción → fase A → fase B → recálculo y variantes (paso 10) → fase C, turno 1 → turno 2 → verificación y auditoría → cierre. Puede haber vueltas (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:51`).
- Qué mira la persona responsable en cada relevo: `PV2/GUIA_RECORRIDO_SUPERVISADO.md:53-60`. La línea de materialidad que traza el agente es un juicio, sin umbral adoptado (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:58`).
- APROBADO solo vale para el material fijado (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:60`).

### 6.5 Leer el resultado

- Estado, acción y cubo: ficha e informe, línea 1 (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:64`).
- **Aptitud por entradas (I20, hito 2).** La ficha y el informe de todas las plantillas, también la V6.3, muestran el bloque `verificacion_entradas` (`E415/hito2/HITO_2_4_15.md:82-88`, `PV2/scripts/ficha.py:383-391`):
  - si es apto o no por entradas, y el recuento;
  - `apto_para_dinero_real: false`;
  - el modo de la entrada efectiva, aplicado y declarado, con su procedencia.
  - El bloque aparece si hay registro de entradas o alguna declaración o registro del modo. Las salidas históricas sin ninguno de los dos no cambian (`E415/hito2/HITO_2_4_15.md:85-87`).
- `aptitud_de_uso` (V6.4): mientras diga «experimental», ni «concluido» ni APROBADO hacen el resultado apto para dinero real (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:65`).
- Objetivo, rango calculado, avisos de dominio, acción final y fechas: `PV2/GUIA_RECORRIDO_SUPERVISADO.md:66-75`. El rango **no es un intervalo de confianza** (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:72`).

## 7. Vigencia, cambios, invalidación y reanudación

### 7.1 Vigencia e invalidación

- Cualquier cambio del material auditado retira la aprobación en la **primera** llamada de cualquier herramienta, y el pipeline repite lo afectado. También la retira una estructura JSON incorrecta en un campo de control. Las salidas cerradas no se editan a mano (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:79`).
- `entrada_efectiva.json` forma parte del material auditado desde el hito 2 (`E415/hito2/HITO_2_4_15.md:88`).
- Una comprobación de entradas cuyo vínculo ya no coincide queda desactualizada (`E415/HITO_1_4_15.md:53`).
- Un defecto del código que escribe el material provisional se corrige en el código y se relanza `pipeline.py … --desde 13`. El material se regenera y se fija de nuevo, y hace falta una auditoría nueva (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:60`).
- **Pruebas:** un cambio invalida solo las pruebas materialmente afectadas, y el integrador justifica esa dependencia (`EVID/coordinacion/cierre_v2/PROGRAMA.md:49`).

### 7.2 Reanudación

- Si el pipeline se corta, se vuelve a ejecutar con el mismo comando. Retoma en el paso guardado en `estado_pipeline.json`. Un agente que no terminó se relanza con el mismo `prompts_generados/NN_*.md` (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:111`).
- `--desde N` repite desde el paso N cuando cambia una entrada de ese paso. Por ejemplo, `--desde 12` para el registro de las entradas (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:112`).
- Si el material cambia después de una auditoría, la aprobación se retira sola y se emite una solicitud nueva. Una auditoría anterior no responde a ella (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:113`).

### 7.3 Relevo caducado (I19, corregido en el hito 2)

- **Comportamiento vigente.** Mientras el paso 13 espera, el pipeline compara el material fijado con el vigente. Si difieren (`E415/hito2/HITO_2_4_15.md:89-92`, `munger_v2_r1/CONTINUIDAD.md:147`, `PV2/scripts/pipeline.py:1060-1084`):
  - lo registra en `estado_pipeline.json → relevos_caducados`, con el material fijado, el vigente y los archivos cambiados;
  - repite el paso 12;
  - pide la auditoría del material vigente, y la solicitud antigua queda «sustituida»;
  - la solicitud nueva comunica al auditor el relevo y los archivos cambiados.
- **Basta relanzar el pipeline con el mismo comando, sin `--desde`** (`munger_v2_r1/CONTINUIDAD.md:147`, `PV2/pruebas/test_relevo_i19_415.py:33-37`).
- Una aprobación de la solicitud antigua no cierra nada (`PV2/pruebas/test_relevo_i19_415.py:73-77`).
- Lo cubre la batería `test_relevo_i19_415.py`, 5/5, sobre una empresa sintética con agentes simulados (`PV2/pruebas/test_relevo_i19_415.py:10`, `PRUEBAS/verificar_paquete_completa.log:36`).
- Con el código anterior al hito 2 se usaba `pipeline.py … --desde 12` (`munger_v2_r1/CONTINUIDAD.md:147`). **No es el procedimiento vigente.**
- **Límite H9, pendiente de verificar por cambio afectado.**
  - El relevo caducado vuelve **siempre al paso 12**. Si cambian salidas de fases anteriores (fase_a/b/c, entrada efectiva), haría falta volver al paso que las consume. Hay una propuesta, sin aplicar (`E415/hito2/HITO_2_4_15.md:92-93`, `E415/hito2/PUNTO_DE_RECUPERACION.md:33-34`, `munger_v2_r1/CONTINUIDAD.md:11`).
  - El programa de cierre lo deja **pendiente de verificar por cambio afectado** (`EVID/coordinacion/cierre_v2/PROGRAMA.md:40`). La tarea T-CAMBIOS pide ensayar un cambio anterior y el punto real de reanudación (`EVID/coordinacion/cierre_v2/CONTROL.json:594`).
  - Qué hacer cuando `relevos_caducados[].archivos_cambiados` contiene salidas de fases anteriores **[NO DOCUMENTADO]**. No consta que la regla general de `--desde N` (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:112`) sea correcta en ese caso. Hasta que se verifique, el operador lo registra y lo comunica a la persona responsable. No lo da por resuelto.

### 7.4 Relevos de expedientes anteriores o sustituidos

- **Relevos pendientes del paquete** (`munger_v2_r1/CONTINUIDAD.md:139-142`). Ninguno pertenece a un expediente vigente:
  - `E414/elis_motor_A/Elis` está caducado y sustituido;
  - las ramas `viscofan/` y `vidrala/` de la 4.14 no se auditan;
  - `vidrala_decisiones_INVALIDO_perdio_analisis` no se reanuda.
- Reglas (`munger_v2_r1/CONTINUIDAD.md:144-148`):
  - se resuelve en una **copia hermana, a la misma profundidad (`cp -a`)**, nunca en su sitio;
  - se relanza primero el pipeline con el mismo comando: regenera los prompts con las rutas actuales y sale con código 10;
  - las plantillas de relevo de la 4.13 son históricas;
  - la auditoría la hace un agente nuevo, de contexto separado.

## 8. Recepción de entregas nuevas

- No se interrumpe ni se repite un encargo en curso de otra sesión. Su entrega final se conserva y se importa como versión nueva, sobre una copia completa. Nunca se sobrescribe con la base histórica (`CLAUDE.md:35`, `docs/RECEPCION_ENTREGA_CLAUDE.md:3`). Una entrega posterior no se incorpora automáticamente (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:43-44`).
- Pasos del producto (`docs/RECEPCION_ENTREGA_CLAUDE.md:7-12`):
  1. Conservar el ZIP, su SHA-256, el manifiesto, la verificación externa y el registro de cambios. Si es un parche, también la identidad exacta de su base.
  2. Subirlo completo a una Release nueva. Antes, comprobar el tamaño: el límite es de 2 GiB por archivo.
  3. Comprobar la huella y la integridad de sus miembros. Extraerlo en una carpeta nueva y verificar el manifiesto de **esa** entrega. Sin `base_414.py` ni `restore_assets_414.py`.
  4. Importarla en una rama nueva, con los bytes exactos y los binarios registrados aparte. Comparar con la base histórica completa. Un archivo ausente no es automáticamente un alta.
  5. Ejecutar los controles de la entrega sobre la copia materializada y registrar resultados reales.
  6. Revisarla contra los contraejemplos y los bloqueos económicos. No dar por apto un resultado porque pasen los controles de software.
- Paquete de cambios de la 4.15 frente a la base 4.14 (`E415/hito2/HITO_2_4_15.md:183-187`):
  - 17 cambiados · 964 nuevos · 0 desaparecidos, más el manifiesto sustituido (7762 entradas);
  - se reconstruye con `python3 -I personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/scripts/empaquetar_cambios_4_15.py . <…>/reproduccion/codigo_4_14/MANIFIESTO_SHA256.txt.txt <salida.zip> "<etiqueta>" --comprobar <ZIP base 4.14> <dir temporal>`;
  - el ZIP no se versiona, y su SHA-256 consta en el mensaje del commit de cierre.
- En el programa de cierre (`EVID/coordinacion/cierre_v2/INTEGRACION.md:23-35`):
  - se lee el HEAD y la ENTREGA del autor y se fija su SHA;
  - se leen las diferencias y se identifican las dependencias afectadas;
  - se reproducen los comandos;
  - autor y revisor reales: la misma sesión no revisa su propio cambio;
  - nunca se fusionan ramas auxiliares completas;
  - se verifica la candidata real, no una constante de un registro.
- **[CONTRADICCIÓN]** (C-05): la recepción y CONTINUIDAD §11.4 exigen un «ZIP completo». El mensaje de arranque dice que desde la 4.15 el proyecto vive en el repositorio. El hito 2 se entregó como rama y paquete de cambios.

## 9. Traspaso a un contexto limpio

- La fuente de verdad es el repositorio y sus pruebas, no la memoria de conversaciones anteriores (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:11`).
- El mensaje de arranque vigente es el texto bajo la línea de `munger_v2_r1/PROMPT_NUEVA_VENTANA.md` (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:5-7`). El de la 4.14, con el ZIP, se conserva en `E415/reproduccion/codigo_4_14/PROMPT_NUEVA_VENTANA.md.txt` (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:3-4`).
- **Primera tarea del receptor:** comprobar el estado y no iniciar ningún otro trabajo (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:13-29`):
  - leer;
  - materializar y verificar la base;
  - cambiar a la rama;
  - comprobar el manifiesto;
  - leer `HITO_2_4_15.md` y `PUNTO_DE_RECUPERACION.md`;
  - `verificar_paquete.sh completa` en una copia limpia;
  - informar por bloques, con las discrepancias;
  - esperar la indicación de la persona responsable.
- **Puntos de recuperación:**
  - `E415/hito2/PUNTO_DE_RECUPERACION.md`: estado de las pruebas, pendientes y siguiente paso exacto (`E415/hito2/PUNTO_DE_RECUPERACION.md:49-53`);
  - en la coordinación, cada bloque publica su `PUNTO_DE_RECUPERACION.md` con la siguiente acción exacta (`EVID/coordinacion/cierre_v2/INTEGRACION.md:17`).
- **Precedente de la 4.14** (`E414/documentacion_cierre_4_14/traspaso/LEEME_TRASPASO.md:5-17`):
  - el receptor verificó el paquete y resolvió un relevo en una copia hermana;
  - su auditoría no fue independiente;
  - las dificultades quedaron en I18–I21 (`E414/documentacion_cierre_4_14/INCIDENCIAS_4_14.md:144-182`);
  - la prueba quedó por repetir con un agente capaz de lanzar auditores de contexto separado (`munger_v2_r1/CONTINUIDAD.md:353`).
- **[CONTRADICCIÓN]** (C-04): CONTINUIDAD §12 sigue pidiendo adjuntar el ZIP de la 4.14 (`munger_v2_r1/CONTINUIDAD.md:386-390`). El mensaje de arranque vigente arranca desde el repositorio (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:3`, `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:15-22`).

## 10. Lista de comprobación de la prueba de traspaso (T-TRASPASO)

- **Para quién:** un receptor sin historial que solo dispone del repositorio, de este manual y del mensaje de arranque.
- **Qué pide la tarea:** reproducir desde la documentación y la fuente fijadas, y registrar lo que no se puede ejecutar (`EVID/coordinacion/cierre_v2/CONTROL.json:618`).
- **Requisitos de cada paso:** **S** = sin LibreOffice ni agentes; **LO** = solo con LibreOffice, en secuencia; **AG** = solo con agentes reales de contexto separado; **RED** = descarga de la Release.

| # | Paso | Requisito | Resultado esperado | Fuente |
|---|---|---|---|---|
| 1 | Leer `README.md`, `CLAUDE.md`, `munger_v2_r1/CONTINUIDAD.md`, `munger_v2_r1/PROMPT_NUEVA_VENTANA.md`, `E415/hito2/HITO_2_4_15.md` y `PUNTO_DE_RECUPERACION.md` | S | Identifica la versión 4.15 · hito 2, la aptitud experimental y los pendientes (F1, regeneración, H9, U1, U6 (a)). Señala que `README.md:1` y `CLAUDE.md:1` dicen «hito 1» | `munger_v2_r1/VERSION:1`; `E415/hito2/HITO_2_4_15.md:219-220` |
| 2 | Clonar `main` y descargar el ZIP de `base-4.14` | RED | 1130912246 bytes; SHA-256 `bb51942c…7b93e` | `README.md:33-35`, `README.md:41` |
| 3 | `materialize` y `verify` con `tools/base_414.py`, en `main` | S | 6798/6798, `complete: true`, código 0 | `README.md:42-46` |
| 4 | Obtener `integracion/candidata-cierre-v2` @ `957af65` | S | HEAD `957af65`; `VERSION` dice «4.15 · hito 2» | `EVID/coordinacion/cierre_v2/PROGRAMA.md:12` |
| 5 | Copiar los 1008 binarios `release_asset` a la candidata, sin sobrescribir | S | 1008 copiados · 0 existentes · 0 distintos · 0 fallos. **Procedimiento [NO DOCUMENTADO]**: el receptor registra cómo lo hizo | `PRUEBAS/README.md:10` |
| 6 | Comprobar que no se ha ejecutado `base_414.py` sobre el árbol 4.15 | S | Ninguna orden de `base_414.py` en el registro del receptor sobre la candidata | `CLAUDE.md:37`, `README.md:56` |
| 7 | Hacer una copia limpia de `munger_v2_r1/` (sin `.lo_perfil/` ni `__pycache__`) | S | Copia nueva; nunca la carpeta de una verificación anterior. **Comando [NO DOCUMENTADO]** | `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:22`, `munger_v2_r1/CONTINUIDAD.md:132` |
| 8 | `bash verificar_paquete.sh completa`, una vez, con exclusión mutua de LibreOffice | LO | Los valores de la tabla del §5.2: 7762 · 0 · 0 · 0 … 55/55; `RESULTADO GLOBAL: PASA`, código 0 | `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:23-26`; `PRUEBAS/verificar_paquete_completa.log` |
| 9 | Después, en la misma copia, `comprobar_entrega_4_14.py` | S (sin LibreOffice conocido: **[NO DOCUMENTADO]**) | 29/35, código 1; las seis FALLA de §5.3 y ninguna otra | `munger_v2_r1/CONTINUIDAD.md:131`; `PRUEBAS/comprobar_entrega_4_14.log` |
| 10 | Controles históricos (`LEEME_CONTROLES_HISTORICOS_4_14.md`) | LO (algunos) | Resultado esperado sobre el árbol 4.15 **[NO DOCUMENTADO]**: registrar lo observado sin calificarlo | `E414/resultados/LEEME_CONTROLES_HISTORICOS_4_14.md:1-3`; `PRUEBAS/README.md:24` |
| 11 | Localizar los relevos pendientes del paquete y su regla | S | Ninguno pertenece a un expediente vigente; ninguno se reanuda en su sitio | `munger_v2_r1/CONTINUIDAD.md:139-145` |
| 12 | Practicar un relevo en una copia hermana (`cp -a`) y relanzar con el mismo comando | LO | Código 10; los prompts se regeneran con las rutas actuales; el original no cambia | `munger_v2_r1/CONTINUIDAD.md:145-146` |
| 13 | Relevo caducado: con la auditoría pedida, cambiar un archivo del material y relanzar **sin `--desde`** | LO (+ AG en un expediente real) | `relevos_caducados` registrado, paso 12 repetido, solicitud nueva y la antigua «sustituida». En sintético lo cubre `test_relevo_i19_415.py` (5/5) | `munger_v2_r1/CONTINUIDAD.md:147`; `PV2/pruebas/test_relevo_i19_415.py:56-68` |
| 14 | H9: un relevo caducado cuyo cambio afecta a salidas de fases anteriores | LO + AG | **Pendiente de verificar.** Se registra a qué paso vuelve (12) y si el consumo del cambio queda cubierto. No se declara resuelto | `EVID/coordinacion/cierre_v2/PROGRAMA.md:40`; `E415/hito2/HITO_2_4_15.md:92-93` |
| 15 | Fase C: los dos turnos con el mismo agente | AG | El turno 2 continúa la conversación del turno 1 | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:48` |
| 16 | Auditoría por un agente nuevo, de contexto separado | AG | APROBADO solo del material fijado vigente. Si no se puede lanzar el agente, se declara que la auditoría no es independiente | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:60`; `munger_v2_r1/CONTINUIDAD.md:148` |
| 17 | La ficha y el informe (también V6.3) muestran `verificacion_entradas` con `apto_para_dinero_real: false` | LO + AG (hace falta un expediente recorrido con el código 4.15) | Bloque presente con el recuento, el modo aplicado y el declarado, y su procedencia | `E415/hito2/HITO_2_4_15.md:82-88` |
| 18 | Comprobar que no se adopta ninguna política económica | S | Ninguna configuración de demostración se presenta como adoptada; no se fija R, θ, λ, probabilidades, k ni umbrales | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:8`; `EVID/coordinacion/cierre_v2/PROGRAMA.md:7` |
| 19 | Informe del receptor | S | Por bloques; hechos, interpretaciones y propuestas separados; en tercera persona; lo no ejecutado se marca como no ejecutado | `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:27-28`, `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:32` |

**Qué solo puede comprobarse con LibreOffice:** pasos 8, 10 (en parte), 12, 13, 14 y 17, y el bloque de entorno, porque `comprobar_entorno.sh` llama a `soffice` (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:15`).

**Qué solo puede comprobarse con agentes reales:** pasos 13 (en un expediente real), 14, 15, 16 y 17. Con agentes simulados solo valen como prueba técnica (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:49`).

**Condición de la prueba:** el receptor no es quien escribió este manual, y un revisor distinto revisa el resultado (`EVID/coordinacion/cierre_v2/CONTROL.json:503-519`, `CLAUDE.md:31`).

## 11. Pendientes que el operador no puede cerrar

- **F1 (otra tarea).** Ver §1.
- **Regeneración y auditoría** de Viscofan, Vidrala y Elis con extractor y revisor reales; sin firmas simuladas (`E415/hito2/PUNTO_DE_RECUPERACION.md:39`).
- **H9/I19**, **U1** y **U6 (a)** (`E415/hito2/PUNTO_DE_RECUPERACION.md:33-38`).
- **Control de la 4.14**, 29/35: no se da por superado (`E415/hito2/PUNTO_DE_RECUPERACION.md:42`).
- Las pruebas de la candidata son del autor de la candidata, no una revisión independiente (`PRUEBAS/README.md:3`).

## 12. Registro de [NO DOCUMENTADO] y [CONTRADICCIÓN]

### 12.1 [NO DOCUMENTADO]

| Id | Qué falta | Dónde se nota |
|---|---|---|
| N-01 | Comando o script para copiar los 1008 binarios de la base materializada a la rama 4.15, y qué hacer si un binario difiere | §4.2.6; `README.md:5` solo dice «cambiar a esta rama»; `PRUEBAS/README.md:10` da el resultado, no el comando |
| N-02 | Comando independiente para contrastar el árbol con `munger_v2_r1/MANIFIESTO_SHA256.txt` fuera de `verificar_paquete.sh` | §4.2.7; `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:19` |
| N-03 | Comando para hacer la «copia limpia» de `munger_v2_r1/` | §5.1; `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:22` |
| N-04 | Resultado esperado de los controles históricos sobre el árbol 4.15 | §5.3; `E414/resultados/LEEME_CONTROLES_HISTORICOS_4_14.md:1-3` |
| N-05 | Espacio en disco por la vía del repositorio (clon, ZIP, base, copia limpia) | §3.1; `munger_v2_r1/CONTINUIDAD.md:133-138` solo mide la vía ZIP |
| N-06 | Ruta del archivo de bloqueo y comando `flock` completo | §2; `PRUEBAS/README.md:4,21` |
| N-07 | Cómo comprobar con un comando que la sesión puede lanzar agentes reales de contexto separado | §3.1; `EVID/coordinacion/cierre_v2/PROGRAMA.md:13` |
| N-08 | Procedimiento ante un relevo caducado cuyo cambio afecta a salidas de fases anteriores (H9) | §7.3 |
| N-09 | Cómo resolver la parada del modo «estricta» (código 7 de `rellenar_fase1_v63.py`) en un expediente nuevo | §6.1 |
| N-10 | Versiones mínimas de LibreOffice y de las bibliotecas de Python | §3.1 |
| N-11 | Comando de clonado y de cálculo de la huella del ZIP en la vía del repositorio | §4.2.1 y §4.2.3 |
| N-12 | Si `comprobar_entrega_4_14.py` usa LibreOffice | §10, paso 9 |

### 12.2 [CONTRADICCIÓN]

| Id | Fuente A | Fuente B | Nota |
|---|---|---|---|
| C-01 | `README.md:1-7` y `CLAUDE.md:1`: «rama de revisión 4.15, hito 1», «conserva exactamente el código recibido» | `munger_v2_r1/VERSION:1`: «4.15 · hito 2»; rama `integracion/candidata-cierre-v2` | Las instrucciones de la raíz describen otra rama |
| C-02 | `README.md:17`, `CLAUDE.md:35`, `docs/MIGRATION_STATUS.json:9,12-13`: las correcciones de Claude «no están incorporadas», «esperar» | `E415/hito2/HITO_2_4_15.md:1-10`: el hito 2 está en el árbol | Estado de migración desfasado |
| C-03 | `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:19` y `munger_v2_r1/CONTINUIDAD.md:6`: rama del hito 2 `claude/hopeful-bardeen-qap6y0` | `EVID/coordinacion/cierre_v2/PROGRAMA.md:12`: candidata `integracion/candidata-cierre-v2` desde `957af65` | El receptor tiene que saber qué rama comprobar |
| C-04 | `munger_v2_r1/CONTINUIDAD.md:386-390` (§12): adjuntar el ZIP 4.14 y pegar el mensaje | `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:3`: desde la 4.15, el repositorio y no un ZIP adjunto | Traspaso |
| C-05 | `munger_v2_r1/CONTINUIDAD.md:370`, `munger_v2_r1/CONTINUIDAD.md:377` y `docs/RECEPCION_ENTREGA_CLAUDE.md:7-9`: entrega como ZIP completo, con `empaquetar_zip.py` | `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:3`; `E415/hito2/HITO_2_4_15.md:183-187`: rama y paquete de cambios no versionado | Recepción |
| C-06 | `munger_v2_r1/CONTINUIDAD.md:109` (§2.1): «Descomprimir el ZIP» | `README.md:5`, `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:15-22`: clon y materialización | Verificación |
| C-07 | `munger_v2_r1/CONTINUIDAD.md:130`: «Las doce que siguen a la sintética»; `:132`: el modo rápido omite «las diez» | `munger_v2_r1/verificar_paquete.sh:85-330`: trece baterías solo en «completa» (H5 … cierre) | Recuento desfasado |
| C-08 | `munger_v2_r1/CONTINUIDAD.md:371`: «las diez baterías obligatorias … integración V6.4 (198)» | `munger_v2_r1/CONTINUIDAD.md:130` (quince) y `munger_v2_r1/verificar_paquete.sh:209` (mínimo 199) | Regla 11.4 desfasada |
| C-09 | `munger_v2_r1/CONTINUIDAD.md:191` y `:287`: «en la V6.3 queda en `estado_pipeline.json` (I20)», «un relevo caducado no se avisa (I19)»; `:351-352`: I19 e I20 «requiere encargo» | `munger_v2_r1/CONTINUIDAD.md:9`; `E415/hito2/HITO_2_4_15.md:82-93`: corregidos | No reintroducir: ver `CONTRADICCIONES_GUIA.md` |
| C-10 | `munger_v2_r1/CONTINUIDAD.md:131`: el LEEME de la 4.14 «sustituye, para este árbol» | `E414/resultados/LEEME_CONTROLES_HISTORICOS_4_14.md:1-3`: describe el árbol 4.14 | Ver N-04 |
| C-11 | `munger_v2_r1/CONTINUIDAD.md:110`, `PV2/GUIA_RECORRIDO_SUPERVISADO.md:14`: 25–45 min | `PRUEBAS/README.md:21`: 22:18–23:18 UTC | Menor: es una estimación |
| C-12 | `munger_v2_r1/CONTINUIDAD.md:194`: `test_integracion_v64.py` (198) | `munger_v2_r1/verificar_paquete.sh:209` y `PRUEBAS/verificar_paquete_completa.log:39`: 199 | Recuento desfasado |
| C-13 | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:98` y `:114` | `E415/hito2/HITO_2_4_15.md:82-93` | Detalle en `CONTRADICCIONES_GUIA.md` |

## 13. Fuentes leídas (candidata `957af65`; evidencias en `9871f59`)

SHA-256 abreviados (16 hex) de los archivos citados, calculados al leerlos:

| Archivo | SHA-256 (prefijo) |
|---|---|
| `README.md` | `d74809472d2f239e` |
| `CLAUDE.md` | `d41ad7a19a1afea3` |
| `docs/RECEPCION_ENTREGA_CLAUDE.md` | `c8a999643828e649` |
| `docs/MIGRATION_STATUS.json` | `cf9e7927c5427b97` |
| `tools/base_414.py` | `56a3e62f4d186275` |
| `munger_v2_r1/CONTINUIDAD.md` | `a0a1f0c52b1dff24` |
| `munger_v2_r1/verificar_paquete.sh` | `f304ededb0950be1` |
| `munger_v2_r1/VERSION` | `f92618d605ccdff8` |
| `munger_v2_r1/PROMPT_NUEVA_VENTANA.md` | `ed804aab69a5526b` |
| `munger_v2_r1/MANIFIESTO_SHA256.txt` | `15a175a5f3293515` |
| `PV2/GUIA_RECORRIDO_SUPERVISADO.md` | `108dbea152299703` |
| `PV2/README_v2.md` | `c5d6f2ff37c20948` |
| `PV2/PROMPT_CLAUDE_CODE.md` | `988e52c781015e49` |
| `PV2/ESTADO.md` | `0f383331529082d5` |
| `PV2/DECISIONES.md` | `16cc6de4f874aff4` |
| `PV2/scripts/comprobar_entorno.sh` | `a9508c32033aac1d` |
| `PV2/scripts/pipeline.py` | `3999a95afed93c76` |
| `PV2/scripts/ficha.py` | `c3ba3d86a678313b` |
| `PV2/pruebas/test_relevo_i19_415.py` | `663a922555abbe5c` |
| `E415/HITO_1_4_15.md` | `f1697a9468730535` |
| `E415/hito2/HITO_2_4_15.md` | `8b1a19d99cb75756` |
| `E415/hito2/PUNTO_DE_RECUPERACION.md` | `cf08466e1447f0c8` |
| `E414/documentacion_cierre_4_14/HITO_2.md` | `367932cca24b4300` |
| `E414/documentacion_cierre_4_14/INCIDENCIAS_4_14.md` | `bb141a50e38ee27b` |
| `E414/documentacion_cierre_4_14/traspaso/INFORME_TRASPASO.md` | `eb6e494a7707f88b` |
| `E414/documentacion_cierre_4_14/traspaso/LEEME_TRASPASO.md` | `ef1bf2548f25e18a` |
| `E414/resultados/LEEME_CONTROLES_HISTORICOS_4_14.md` | `34212e1cefd2a010` |
| `EVID/coordinacion/cierre_v2/PROGRAMA.md` | `03730269609b5aec` |
| `EVID/coordinacion/cierre_v2/INTEGRACION.md` | `57ab214f5a9f0ba9` |
| `EVID/coordinacion/cierre_v2/CONTROL.json` | `8a00c41db5c54905` |
| `PRUEBAS/` | manifiesto propio en `PRUEBAS/MANIFIESTO_SHA256.txt` |

**Observación del entorno de lectura (hecho):** el worktree leído tiene 10 JSON sin seguimiento en `PV2/empresas_v2/*/` (`*.conciliacion.json` y `*.fase1.registro.json`). Coinciden con los binarios de la 4.14 que el `.gitignore` no cubre (`PRUEBAS/README.md:12`). Este borrador no los ha modificado.
