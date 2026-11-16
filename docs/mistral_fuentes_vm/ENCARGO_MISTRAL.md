# Munger V2 · frente M · fuentes de Vidrala y Viscofan

## Resultado y separación

Preparar evidencia verificable para la futura regeneración de dos expedientes. No corregir el producto ni emitir una valoración. Claude mantiene el frente técnico y F1/Elis. Este trabajo no sustituye su auditoría final.

Repositorio de trabajo exclusivo: `jluisplagos/munger-v2-evidencias-mistral`. No iniciar la tarea en `munger-v2`. La conexión de Mistral debe estar autorizada solo para el auxiliar. El original público puede consultarse sin acceso de escritura. No cambiar sus ramas, PR, issues, etiquetas, releases ni configuraciones. No enviar mensajes a terceros.

Fuente histórica fijada: commit `059f4f68dca7acf465b5f5b21de2dede84c885ff` del original y binarios de la Release `base-4.14`. No seguir ramas móviles. La evidencia nueva se contrastará otra vez con la versión final de Claude antes de usarla.

## Alcance exacto

Dos expedientes finales de decisiones, no sus antecesores:

- `personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/vidrala_decisiones/Vidrala`.
- `personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/viscofan_decisiones/Viscofan`.

Por empresa: `Análisis!C55`, `C46`, `C47`, `C48`, `C49`, `C50`; `Historia!L6`, `L7`, `L8`, `L12`, `K14`, `L14`, `L15`. Son **26 objetivos**, con **34 dependencias adicionales**: 60 entradas en total. El universo está fijado en los archivos de `entrada/`.

Importancia práctica: acciones en circulación frente a media diluida, CFO, capex, intereses, arrendamientos, pagos en acciones, ventas, EBIT, amortizaciones y circulante. Comprobar sobre todo ejercicio/columna, grupo frente a sociedad/segmento, moneda/unidad/escala, signo, versión/reexpresión y clasificación económica. Que una cifra aparezca en un PDF no acredita estos atributos.

No abordar Elis/F1, P-M1, probabilidades, k, motor C, otra empresa, precio objetivo, actualización del precio ni elección de una política económica. No relanzar la investigación completa ni añadir más objetivos sin un encargo posterior.

## Configuración y coste

Usar Mistral Code. Registrar modelo/proveedor/modo que realmente exponga la sesión, sin inventar nombres, esfuerzo ni configuración. Usar el modelo de código más capaz disponible para el contraste semántico; para huellas, extracción y aritmética, herramientas deterministas. Si el selector ofrece Devstral 2, es una opción de agente de código; no se presupone que tenga visión ni un selector de esfuerzo.

No crear subagentes ni rondas automáticas de revisión en este primer encargo. Una sesión, un universo finito y una entrega. El trabajo no se firma como auditoría independiente aprobada. No gastar el saldo entero por disponer de 250 EUR. Como control externo se recomienda un presupuesto inicial de 25 EUR para este frente, configurado por la persona responsable; este texto no impone un límite de facturación ni garantiza el coste. No cambiar pagos, límites, credenciales o recargas. Si el consumo no es visible, declararlo.

## Preparación

1. Verificar que `origin` apunta exclusivamente al repositorio auxiliar. Crear allí una rama `mistral/fuentes-vm-01` (o usar la rama de tarea que cree Code, registrándola). No fusionar a `main`.
2. Leer `entrada/configuracion.json`, `entrada/objetivos_lectura.csv` e `entrada/indice_fuentes.json`. Los metadatos heredados son pistas, no hechos acreditados.
3. Ejecutar `python3 docs/mistral_fuentes_vm/herramientas/preparar_insumos.py --download`. Si ya se dispone del ZIP original, usar `--zip RUTA`. Si existe un árbol base íntegro, `--base-tree RUTA`. El script verifica los archivos seleccionados y guarda copias en `.trabajo/insumos/`; no modifica el origen. La descarga completa pesa aproximadamente 1,13 GB; solo se extraen los insumos de este encargo. No subir el ZIP ni los PDF/XLSX a Git.
4. No presentar esta extracción parcial como materialización ni validación de los 6.798 archivos del producto. Si la red, el espacio o un archivo impiden trabajar, registrar el bloqueo exacto y continuar con las fuentes accesibles. No solicitar automáticamente más documentos al usuario ni sustituir un PDF por una página web.

## Trabajo en orden

### 1. Lectura de fuentes antes del contraste

Primero los diez objetivos iniciales: Historia L6, L7, L8 y L12 y Análisis C55 de ambas empresas. Después los otros dieciséis. Completar ambos bloques en este encargo sin pedir confirmación entre ellos.

Trabajar con las páginas pertinentes y sus cabeceras/notas; ampliar el contexto cuando el concepto lo exija. No volcar los cinco PDF enteros al contexto ni repetir lecturas idénticas por cada celda: conservar observaciones reutilizables con su huella y referencia exacta.

Para cada cifra fuente de los objetivos y de sus dependencias:

- Abrir el PDF conservado y comprobar título, versión, ejercicio y perímetro; la asociación texto→PDF del índice es una candidata que debe verificarse.
- Leer la tabla con sus cabeceras, rótulo y notas pertinentes. Conservar página PDF (1-based), página impresa si existe, una cita corta suficiente y localización de fila/columna. Distinguir número del documento y número de página.
- Usar texto/layout y, para columnas ambiguas, una representación visual o una segunda extracción independiente. Si no se puede resolver, no acreditar la cifra. Un OCR necesita revisión contra el original y no se convierte en fuente primaria.
- Anotar lo leído en `resultados/lectura_fuentes.jsonl` **antes** de compararlo con los valores heredados. Registrar el hash de esa primera lectura. Esto reduce anclaje, pero no se presenta como una revisión ciega formal.

### 2. Comparación y aritmética

Leer después `entrada/declaraciones_historicas.json`. Ese archivo conserva valores y derivaciones del registro, pero elimina sus afirmaciones de revisión para no heredarlas como prueba.

- Comparar con la fuente y con la celda real del XLSX, abierto en modo de solo lectura; conservar huella del libro. Distinguir valor almacenado y fórmula. No ejecutar LibreOffice, macros, pipeline o scripts de publicación.
- Recalcular cada derivado desde las dependencias verificadas; mostrar expresión, operandos, unidad, transformación de signo y redondeo. Una media de tres años exige tres datos comparables; no sustituir ausencias por cero.
- En Vidrala, C48 es ausencia y C49/C50 son hipótesis en el registro histórico: pueden concluir NO_ACREDITADO o HIPOTESIS_O_AUSENCIA. No convertirlos en datos publicados para completar el recuento.
- Preservar E1, D3 y E2 y sus condiciones. Distinguir las acciones de cierre de 2025, las medias para BPA y la fecha de precio; no volver a proponer la media diluida como sustituto automático. Mantener K14 publicado en Vidrala y registrar aparte la reserva sobre la plusvalía, sin descontarla como si fuera un dato.
- Si se detecta algo que parece erróneo, entregar un hallazgo con evidencia y propuesta separada. No editar el XLSX, el registro oficial ni las decisiones.

### 3. Entrega finita

Entregar exclusivamente en el repositorio auxiliar:

- `resultados/lectura_fuentes.jsonl`: una observación por entrada fuente examinada, con documento/hash, página, cita, columna, período, unidad, escala, signo, perímetro y límites. Los derivados enlazan estas observaciones.
- `resultados/contraste_objetivos.csv`: exactamente 26 filas, una por objetivo; columnas de la plantilla. Estados: COINCIDE_EN_REVISION_MISTRAL, DIFERENCIA, NO_ACREDITADO, HIPOTESIS_O_AUSENCIA. No existe estado APROBADO ni APTO.
- `resultados/HALLAZGOS.md`: hallazgos priorizados por efecto potencial, cada uno con reproducción y qué falta comprobar. Separar error del dato, conflicto de fuente, hipótesis y límite de cobertura. Si no hay hallazgos, decir qué se comprobó y con qué límites.
- `resultados/RESUMEN_PARA_CLAUDE.md`: máximo dos páginas; objetivo, commits/huellas, recuento por estado, fuentes examinadas, pendientes y rutas. Incluir «Evidencia propuesta por Mistral; pendiente de revisión e incorporación por el integrador».
- `resultados/PUNTO_DE_RECUPERACION.md`: terminado/pendiente, siguiente acción exacta, modelo real y limitaciones de acceso/consumo. Commit y push al acabar cada bloque, sin datos binarios ni credenciales.
- `resultados/MANIFIESTO_SHA256.txt`: huellas de la entrega, salvo el propio manifiesto.

Comprobar estructura con `python3 docs/mistral_fuentes_vm/herramientas/comprobar_entrega.py`. Este control verifica completitud formal y referencias, no verdad semántica ni aptitud financiera. Una entrega honesta con objetivos pendientes es admisible; no mejorar el recuento inventando evidencia.

No abrir PR hacia `munger-v2`, no fusionar, no emitir recomendaciones y no declarar aptitud para dinero real. El integrador verificará las citas, datos, derivaciones y compatibilidad antes de incorporar cualquier parte.
