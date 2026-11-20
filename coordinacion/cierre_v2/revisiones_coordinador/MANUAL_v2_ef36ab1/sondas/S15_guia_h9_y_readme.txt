$ <home>/rev_manual_v2/sondas/herramientas/cita.sh PV2/GUIA_RECORRIDO_SUPERVISADO.md 136-141
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 136	   - **Relevo caducado.** Si, mientras el paso 13 espera, cambia o aparece un archivo del material (`cierre_v2.MATERIAL_FIJO`), la solicitud pendiente ya no se puede aprobar. Desde el hito 2 de la 4.15 (I19 corregido), al relanzar el **mismo comando, sin `--desde`**, el paso 13:
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 137	     - lo detecta y lo registra en `estado_pipeline.json → relevos_caducados`;
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 138	     - repite la verificación del paso 12;
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 139	     - pide la auditoría del material vigente. La solicitud antigua queda «sustituida», y su aprobación no cierra nada (`…_4_15/hito2/HITO_2_4_15.md`; `pruebas/test_relevo_i19_415.py`).
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 140	
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 141	     **Límite abierto (H9):** la vuelta es siempre al paso 12. Si lo cambiado son salidas de fases anteriores (fases A, B o C, o la entrada efectiva), volver al paso 12 no basta, y el procedimiento para ese caso no está documentado: está pendiente de verificar por cambio afectado.
[código 0]

$ <home>/rev_manual_v2/sondas/herramientas/cita.sh EVID/coordinacion/cierre_v2/PROGRAMA.md 40-40
[EVID/coordinacion/cierre_v2/PROGRAMA.md:] 40	7. Preparar manual actual, instalación/recuperación y traspaso limpio. Leer la guía histórica junto con Hito2; no reintroducir límites I19/I20 ya corregidos. H9/I19 (volver siempre a paso12) sigue pendiente de verificar por cambio afectado.
[código 0]

$ <home>/rev_manual_v2/sondas/herramientas/cita.sh PV2/GUIA_RECORRIDO_SUPERVISADO.md 41-41
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 41	`python3 personaje_v2/scripts/pipeline.py CARPETA --config personaje_v2/config_v2_v64_experimental.json` (V6.4) o `--config personaje_v2/config_v2_v641_experimental.json` (V6.4.1, con el perímetro). La selección de la plantilla es siempre explícita: la V6.4 rechaza una configuración con perímetro y la V6.4.1 exige declararlo si hay requisito. `…_4_13/scripts/paso_pipeline.py CARPETA [--config …]` hace una pasada y guarda la salida completa en `resultados/pipeline_NN_*.txt`.
[código 0]

$ <home>/rev_manual_v2/sondas/herramientas/cita.sh PV2/GUIA_RECORRIDO_SUPERVISADO.md 127-129
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 127	5. **Configuración por motor.**
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 128	   - Motor B: `--config config_v2_v64_experimental.json` (V6.4) o `config_v2_v641_experimental.json` (V6.4.1, con perímetro).
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 129	   - Motor A: `--config config_v2.json` (V6.3).
[código 0]

$ <home>/rev_manual_v2/sondas/herramientas/cita.sh PV2/GUIA_RECORRIDO_SUPERVISADO.md 102-116 | cut -c1-200
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 102	2. **Registro de las entradas.** `python3 -B scripts/verificacion_entradas.py plantilla CARPETA` crea el registro. Para no tocar el expediente, hágase en una 
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 103	   - **El extractor** rellena cada entrada: fuente con archivo, página, cita que contenga la cifra, escala y signo; o una derivación con orígenes y fórmula
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 104	     - `pagina` es la página del PDF, un entero, y el folio impreso va aparte;
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 105	     - la fuente local tiene que existir y llevar su sha256 vigente;
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 106	     - la cita tiene que contener la cifra equivalente, sin redondeo;
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 107	     - `valor_fuente` es la cifra publicada con su signo, y la transformación (`signo`, `escala`) se declara;
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 108	     - las cifras de juicio también entran en el registro.
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 109	
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 110	     Fuentes: `…_4_15/HITO_1_4_15.md`, R1–R3 e I8/I9; `…_4_15/hito2/HITO_2_4_15.md`, R415-SIGNO.
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 111	   - **Un revisor distinto** rellena `comprobacion` en cada entrada (revisor, resultado, fuente examinada y nota) y la **sella**: `python3 -B scripts/verificac
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 112	     - Sin ese vínculo con huella, la entrada queda pendiente.
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 113	     - Si cambia lo vinculado, queda desactualizada.
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 114	
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 115	     Fuente: `…_4_15/HITO_1_4_15.md`, I13.
[PV2/GUIA_RECORRIDO_SUPERVISADO.md:] 116	   - `python3 -B scripts/verificacion_entradas.py comprobar CARPETA` dice si el registro es apto. El pipeline lo vuelve a comprobar en el paso 12.
[código 0]

$ git -C <candidata> diff origin/main 3149128 --stat -- README.md .gitignore tools/base_414.py
 README.md | 16 ++++++++++------
 1 file changed, 10 insertions(+), 6 deletions(-)
[código 0]

$ git -C <candidata> show origin/main:README.md | grep -n -E 'gh release download|base_414.py'
14:- `tools/base_414.py`: verifica o recupera la base histórica completa.
31:    gh release download base-4.14 --repo jluisplagos/munger-v2 --pattern munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip --dir .downloads
32:    python tools/base_414.py materialize --source .downloads/munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip
33:    python tools/base_414.py verify --report docs/VERIFICACION_BASE_COMPLETA_LOCAL.json
41:    python tools/base_414.py verify --git-only
[código 0]

