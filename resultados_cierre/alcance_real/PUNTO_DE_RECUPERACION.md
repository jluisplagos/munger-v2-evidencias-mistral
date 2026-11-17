# Punto de recuperación · rama mistral/f-alcance-real · bloque F-REV

- **Base de la rama**: `ff0c60c` (paquete de coordinación `coordinacion/cierre_v2`, contiene el encargo
  `ec707a5ba2bd684381a63ce0f6f6c143aa59f4c0`). Rama creada desde ese commit; escribe solo en
  `resultados_cierre/alcance_real/`.
- **Bloques F-REV (Cola 1)**: (1) contraste de F1 W1–W3 @ `d519eb0` (base `716cbd6`): CUMPLE los 4
  criterios, sin defecto material. (2) contraste de **C20 (U1–U6 del verificador) @ `bf0d5c2`**
  (base `d519eb0`): **CUMPLE los 5 criterios**, sin defecto material; rerun propio de las 752 filas
  (736/752 byte-idénticas, 0 diferencias en tabla; 16 filas texto solo por falta de poppler raw en el
  sandbox) + sondas U1–U6 sobre ambas versiones del código + end-to-end en páginas exportadas
  hash-ligadas. (3) contraste del **bloque CSV @ `77ff89f8`**: **CUMPLE los 4 criterios** — 10 filas
  nuevas OK con el verificador sin cambios (verificador idéntico, sha256 igual), 752 sin cambiar,
  contraste 292/0 y copia 67/0 re-ejecutados byte-idénticos con el libro real, y los 4 mutantes
  negativos (columna por sociedad como grupo → no OK). Evidencias en `revisiones_claude/` +
  `evidencias/c20/` + `evidencias/csv/`. (4) **B-PM1 @ `daa7478`** (dossier de Mistral B, rama
  `mistral/m2-fundamento-pm1` intacta): CONFIRMADO — 9/9 altas PP&E reproducidas por extracción
  independiente propia sobre textos hash-verificados (101.154…177.848 k€), 8/8 comparativos OK,
  error antiguo localizado en la nota de intangibles (2017: 156.743 = 3.237 + 150.657 goodwill),
  script del autor rerun byte-idéntico con control negativo superado; θ/λ siguen sin identificarse
  y el bloqueo P-M1 se conserva (no elegí ningún valor). Límite declarado: misma familia de modelo
  que el autor (Mistral B), independencia de sesión/método/hashes. Evidencias en `revisiones_b_pm1/`.
  Nada adoptado; producto/libros/candidata intactos; frente C (`mistral/m2-matematica-b` @ 1ec4f18) intacto.
- **Estado de las colas tras consultar CONTROL.json** (`git fetch origin coordinacion/cierre-v2`):
  - Cola 1: F-REV (W1–W3), C20 y CSV hechos por mí (informes en `revisiones_claude/`); en el
    último fetch de CONTROL.json los tres quedaron **CONFORME_CON_LIMITES / RESPONDIDA**
    (F1-W, C20, CSV). E-ELIS (93a9780) está EN_CURSO en cola B_E (no es mi cola). Cola C_F:
    F-REV y B-PM1 hechos (conformes con límites); F-B3/F-C1 en PREPARACIÓN (no ejecutados).
    B-PM1 hecho por mí (informe en `revisiones_b_pm1/`); bloqueo P-M1 conservado (θ/λ no
    identificados, 4 PDF con preservación pendiente por el 401 de uploads).
  - Cola 2: **F-B3 / F-C1 paquete de PREPARACIÓN entregado** (`preparacion_b3_c1/`; NO ejecutados): inventario
    de recursos conservados (ZIP base-4.14, 6798/6798), SELECCION.csv (B: principal condicionada
    Ahold bloqueada por insumo; C: banco/aseguradora con fuente oficial pendiente), protocolo
    congelado antes de calcular, MAPA_ENTRADAS.jsonl, contrato C propuesto (E62: no valida
    solvencia). Bloqueos: Ahold sin etapa 1; ninguna financiera conservada; solo GitHub alcanzable.
    La ejecución real es Cola 3 (agentes/pipeline, copias aisladas).
  - Cola 3: bloqueada salvo que lleguen insumos externos (etapa 1 de Ahold; fuente oficial de
    banco/aseguradora) y el coordinador fije candidata revisada; ejecución con agentes/pipeline
    en copias aisladas, no por mí (prohibido LibreOffice/pipeline en este frente).
  - Estado global según CONTROL.json: «Cierre en preparación: entregas parciales y revisiones
    pendientes; sin aptitud económica global acreditada».
- **Bloque F2 (2026-11-17, commits 195766f / e9f76a9 / 9873234 y siguientes de esta rama)**:
  respuesta a CORRECCION_F2 @ `F_223f16d_52fb120` en `correccion_f2/` (RESPUESTA_F2.md +
  ENTREGA_F2.json): D1/D2/D7 inventario byte a byte con 71/71 PDF + release SHA-256 completo;
  D3 contrato C y mapa fieles a `build_v6.py`/`test_fill.py` @ 957af65 con ejemplo numérico
  comprobado; D4 esta recuperación actualizada; D5 estados propios (preparación entregada, no
  ejecutado; CONTROL solo lo toca el coordinador); D6 protocolo de C con criterios previos sin
  precios + horas reales de commit; D7 rutas por argumento en todos los scripts.
- **Siguiente acción exacta**: que el coordinador (Claude) registre en CONTROL.json la respuesta
  a CORRECCION_F2 @ `F_223f16d_52fb120` (esta rama, `correccion_f2/ENTREGA_F2.json`) y asigne su
  contraste; si llega antes, contraste G-MANUAL (solicitud LISTA en CONTROL @ 57b34a6).
  Bloqueos materiales sin resolver (datos de la persona responsable): Excel de etapa 1 de Ahold
  con sus fuentes (o empresa fuera de muestra designada) y banco/aseguradora designados con
  informes oficiales en bytes y SHA-256. Cola 3 (ejecución real) sigue bloqueada por esos insumos.
- **Temporales**: `.trabajo/f-rev/` (git-ignored) contiene los artefactos descargados y el rerun; no se commitea.
- **Declaración**: Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación
  por el integrador (Claude). No APROBADO ni aptitud financiera general.
