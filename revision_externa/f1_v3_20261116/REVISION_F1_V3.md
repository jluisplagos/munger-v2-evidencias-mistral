# Revisión externa dirigida · F1/Elis · correcciones V1–V11

16-nov-2026. Material fijado: `jluisplagos/munger-v2`, rama `auditoria/economica-f1-frente-e`, HEAD `716cbd6794b7fcde8b3862c9d1e7acdaf516d262`. Cambios sustantivos: `593a391`, `6a48bc4`, `fd474d3`, respecto de `bb28319`. El último commit 716cbd6 solo cambia recuperación/manifiesto. Revisión anterior: `8fcc7fd`. Se consultó el remoto de nuevo al terminar las pruebas: mismo HEAD.

## Dictamen

**La mayor parte de V1–V11 está corregida y las salidas se reproducen. La especificación aún necesita tres correcciones acotadas antes de implementarse: W1 (horizontes temporales que atraviesan el terminal), W2 (salto del terminal y relación con G8) y W3 (dominio de A0 frente a su guarda).** No se recomienda otra revisión general ni repetir lo ya conforme.

La revisión NO adopta las decisiones (1a)–(5b), no elige R, no cambia libros ni producto, no integra en main y no libera Elis. C48=108, C49=128,1, FCF base=307,933 y E1/D3/E2/E6 se conservan. No se ha enviado ningún mensaje a empresas o terceros.

| Plano | Estado |
|---|---|
| Entregado | V1–V11 y recuperación, en la rama autora |
| Revisado aquí | Cambios documentales/de especificación, scripts nuevos, salidas y fuentes afectadas |
| Integrado | No implementado en producto/libros; no fusionado a main |
| Probado aquí | Tres scripts del autor; recálculo separado; pasajes de PDF con dos extractores; sondas propias de especificación |
| Apto para uso económico de Elis | No acreditado; siguen carencias materiales y políticas no adoptadas |

## Reproducción y evidencia

- **Manifiesto: 374/374 conforme**, antes de ejecutar, incluido el punto de recuperación actualizado.
- `controles_sinteticos_f1.py`: exit 0, **32 casos**, 14 coherentes/18 incoherencias ilustradas, 23 con crecimiento, ocho con ancla calculada; nueve casos externos, tres guardas y caso fiscal. JSON idéntico al publicado.
- `copia_investigacion_f1.py --raiz`: exit 0, **55 controles**, cero fallidos; **14/14 literales y 12/12 pasajes** en sus PDF y huellas correctas. JSON e informe idénticos.
- `contraste_f1.py`: exit 0, **292 comprobaciones**, cero fallidas; JSON e informe idénticos. Consume el resultado conservado de caja no nula; no se volvió a ejecutar LibreOffice.
- Recálculo separado, sin importar el código de cálculo del autor: se ejecutó `revision/scripts_revisor_p1_p4/recalculo_independiente.py` de la revisión anterior sobre el nuevo resultado. **108 valores de 12 escenarios y 89 celdas del libro coinciden**; cero fallos. El código de ese revisor comparte CSV/precondiciones, no constituye una auditoría nueva de las 752 filas.
- `revision/scripts_revisor_p1_p4/evidencia_pdf.py`: **25 pasajes**, cero fallos; huellas de cinco PDF conformes, con pdftotext y pypdf. Se revisaron además las ventanas de tabla de actualización de earnout, adquisiciones, ajustes y conciliación fiscal, con sus cabeceras/ejercicios. La definición publicada excluye adquisiciones importantes, no todas las compras; se conservan M6 y los límites de interpretación.

Cinco salidas principales son idénticas byte a byte: controles JSON, copia JSON/MD y contraste JSON/MD. REPRODUCCION.json conserva hashes y códigos. Los documentos [LECTURA] siguen fuera del CSV verificado; no se convierten en filas acreditadas por esta revisión ni se aplican como política.

## Estado por observación anterior

| Observación | Resultado de esta revisión |
|---|---|
| V1 · compras pequeñas | Conforme en la corrección del fundamento. Se comprueba definición, fuentes y materialidad; (4b) ofrece opciones sin adoptar reposición cero. M6 sigue abierto |
| V2 · doble cargo del ancla | Conforme para los casos corregidos: X^v sale del denominador; se conservan negativos con la fórmula anterior y positivos con la corregida |
| V3 · earnout publicado | Conforme como evidencia/documentación y sensibilidad: caja en adquisiciones y actualización 12,4/5,6/0,7 comprobadas. Falta su paso por el procedimiento CSV, como el autor declara |
| V4 · regla fiscal/alcance | Conforme: recalculados N1, τ, alcance 2021–22 y sensibilidades. No se adopta una ventana ni alcance nuevos |
| V5 · ROU y sensibilidad conjunta | Conforme: pagos −16,778; amortización ROU +10,118; total −6,660 en A1/A2; PPA +4,206 y efectos conjuntos −5,913, con supuestos declarados |
| V6 · terminal | Parcial: distingue igualdad exacta y comparación vigente, pero hay discrepancia de signo y falta reconciliar G8: W2 |
| V7 · término explícito | Parcial: define X_t y X11, pero no resuelve un horizonte temporal posterior al año 10: W1 |
| V8 · cota de R | Conforme: acota R_propia más transición, no R_total; adquisiciones separadas |
| V9 · pruebas | Conforme para los 32 casos y sendas ensayadas; no cubre W1 ni las fronteras de W3 |
| V10 · sincronización | Mejorada, pendiente la coherencia A0/E5 (W3) y tablas del terminal (W2) |
| V11 · aprobación | Conforme: opciones y controles separados; no se adopta el paquete en esta revisión |

## W1 · material para una implementación · gasto temporal que termina después del año 10

**Dónde:** E3, fórmula del término y horizonte; E4, terminal; propuesta §2, fila de transición; T15. E3 dice X11=0 si H≤10, pero admite un horizonte sin límite superior. Para H>10, restar X11 del flujo que entra en Gordon puede perpetuar un coste temporal. La tabla de la propuesta dice «término explícito: solo si es permanente» en el año 11, lo que tampoco describe un coste temporal todavía vigente ese año.

Se comprobó en el libro: Motor!BF7 es flujo del año 11; BG7=`BF7/(J7-H7)` y BH7 lo descuenta diez años. Los tests sintéticos comparan caja de los años 1–11, no su continuación ni el valor terminal completo.

**Sonda ejecutada**, con importes ficticios, r=10%, g=0, caja sostenible=68 y coste temporal=7 hasta H inclusive. Se usa el motor sintético del autor para la proyección y una suma descontada independiente de la caja finita:

| Horizonte H | PV si X11 entra en Gordon | PV de caja con el coste finito | Diferencia |
|---|---:|---:|---:|
| 5 | 653,464493 | 653,464493 | 0 |
| 10 | 636,988030 | 636,988030 | 0 |
| 11 | 610 | 634,534573 | −24,534573 |
| 12 | 610 | 632,304157 | −22,304157 |

Los cuatro casos coinciden en caja hasta el año 11. Para H=11 y H=12, la especificación resumida no distingue el coste posterior al año 11; el valor de la caja sí difiere. Es un hueco de la **propuesta**, no un fallo ejecutado del producto ni una estimación de Elis.

**Corrección acotada:** definir la caja temporal pendiente más allá del año 10 y separarla de la base sostenible del terminal, con prueba de PV; o declarar que ese horizonte no está soportado y bloquear solo la conclusión afectada. No elegir un horizonte ficticio ni hacer X11=0 por conveniencia. No implementar una extensión financiera sin la aprobación que corresponda. Conservar los positivos H≤10 y los 32 casos conformes.

## W2 · menor, antes de implementar · signo del salto y control técnico ya existente

**Dónde:** `copia_investigacion_f1.py`, P4_ROIC_terminal; propuesta §4; especificación E4/E5 y respuesta V6.

El libro calcula fila 178 = **rentabilidad marginal − ROIC**; positivo significa que la rentabilidad cae al pasar al terminal. La copia calcula **ROIC − rentabilidad marginal**, pero lo rotula «salto del libro (fila 178)». En MALO/NORMAL/BUENO el libro da +0,4739/+0,6770/+2,41395 puntos, mientras la salida rotulada del libro da −0,474/−0,677/−2,414. La copia ya guarda los valores reales de la fila 178, pero no contrasta el signo del valor derivado que presenta como el mismo salto. Sonda SONDAS.json.

El aviso vigente compara **magnitud**: `patch_v62_base.py`, AVISO_TRANSICION, usa MAX(ABS(...)) frente a C179. `comprobar_gramatica.py` G8 usa `abs(sv)>umbral` y exige justificación (`requiere_justificacion=True`). Esos dos archivos son idénticos en 716cbd6 y en la candidata técnica 957af65.

La respuesta V6 elimina «debe justificarse» como obligación nueva, pero no reconcilia esta exigencia técnica ya existente. No se afirma que los tres escenarios actuales deban avisar: están por debajo de cinco puntos.

**Corrección:** conservar el signo/rotulado del libro, explicitar comparación absoluta y describir la relación entre V-F1k y G8 sin suprimir silenciosamente el requisito existente ni inventar otro. Si se propone cambiar G8, separarlo como decisión/cambio de alcance. Añadir positivos/negativos de salto en ambas direcciones y frontera del umbral vigente, sin cambiarlo.

## W3 · menor, antes de implementar · A0 solo con ambos ceros, guarda solo con ambos positivos

**Dónde:** decisión (1a), E2 (dominio A0), E5 V-F1a y sincronización V10.

E2 y (1a) solo admiten A0 si D&A ROU=0 **y** C49=0. V-F1a bloquea si D&A ROU>0 **y** C49>0. Quedan sin tratamiento explícito dos combinaciones no admisibles según E2: ROU>0/C49=0 y ROU=0/C49>0. No se demuestra doble cargo en todos esos casos; pueden ser problemas de calendario/definición o entrada que requieran aclaración. No se propone cambiar AND por OR sin interpretar el caso.

**Corrección:** dar un resultado coherente para los cuatro casos (dos positivos, uno solo positivo y ambos ceros), distinguiendo fuera del dominio, incompleto/conflicto y doble cargo demostrado. No convertir la ausencia de V-F1a en una aprobación de A0. Conservar el bloqueo vigente para ambos positivos, sin inventar umbral económico. Esta es una inconsistencia escrita de la propuesta, no una prueba de conducta actual del producto.

## Lo que no bloquea esta revisión por defecto

- No se reabre toda la matemática, los 32 ejemplos, el verificador de 752 cifras ni pruebas antiguas sin cambio relevante.
- C20/U1–U6 y las cifras [LECTURA] al CSV son trabajos técnicos pendientes separados. Su encargo no equivale a aprobar (1a)–(5b). Primero preservar/arreglar el verificador afectado, después pasar por él las cifras nuevas con edición/fila/columna/unidad/perímetro verificables.
- La búsqueda de M1/M2/M6/N2 puede avanzar en paralelo sobre fuentes públicas. No se ha encargado aquí contactar con Relación con Inversores ni enviar mensajes.
- No se considera que una política o firma subsane datos ausentes. No se elige un punto de R en 736,0–867,2, ni θ/λ/k/probabilidades o un umbral nuevos.

## Alcance e independencia

Revisor: ChatGPT/Codex en esta conversación, distinto de la sesión autora Claude. Identificador exacto de modelo y ajuste de esfuerzo no expuestos de forma verificable; no se atribuyen. Python 3.12.14, pdftotext 25.03.0, pypdf 6.21.4 y openpyxl. Los scripts del autor se ejecutan para reproducir, no cuentan como implementación independiente. El recálculo separado y los dos extractores proceden del revisor anterior; se reutilizan sus herramientas con procedencia, no se atribuye su autoría a esta sesión. Las sondas W1–W3 sí se preparan aquí.

Se leyó la propuesta completa, las secciones E0–E8 y T15/T16 y el diff de E9; T14, extenso y sin cambios, se consultó para delimitar, sin repetir su auditoría. Se revisaron scripts de controles/copia, diff del informe y respuesta V1–V11. Fuentes: cinco PDF y libro desde el ZIP ya verificado; **selección parcial de seis archivos**, no materialización de la base completa. No se reejecutaron la auditoría histórica de 752 filas, LibreOffice, aceptación Qwen, motores B/C ni recuperación completa. El informe no acredita aptitud para dinero real.

Encargo siguiente: CORRECCION_PARA_CLAUDE.md. Secuencia y condiciones de cierre: PLAN_DE_CIERRE.md. No se ha enviado ningún encargo a sesiones externas.
