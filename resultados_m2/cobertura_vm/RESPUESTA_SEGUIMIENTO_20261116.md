# Respuesta al seguimiento externo · Frente A M2 · base revisada `54c8ddc`

Seguimiento leído desde `63e366b` (`revision/chatgpt-seguimiento-20261116`): `PROMPTS.md` («Mistral A · pegar en la sesión A») y apartado A de `SEGUIMIENTO.md`, con `git fetch` + `git show` (sin fusionar). Rama propia confirmada: `mistral/m2-cobertura-vm` (HEAD remoto = local = `54c8ddc` al empezar).

**Propuesta de evidencia de Mistral; pendiente de revisión e incorporación por el integrador.**

## Respuesta numerada a los puntos del apartado A

1. **Sobrealcance de estados corregido.** La regla v2 de `check_entrada` exige que TODAS las dimensiones pertinentes (fila, columna, unidad, signo, perímetro, versión, reexpresión) estén OK o NO_APLICA para marcar REVISADO_CONTEXTUAL; cualquier NO_DECIDIBLE pasa a PENDIENTE_CONTEXTUAL. Resultado: fuentes REVISADO_CONTEXTUAL **423 → 264**; totales (677): **315 REVISADO_CONTEXTUAL (264 fuentes + 51 derivados), 196 PENDIENTE_CONTEXTUAL, 60 REUTILIZADO_M1, 106 NO_APLICA, 0 CONFLICTO_CONTEXTUAL**. Las 70 fuentes con dimensiones pendientes que el revisor señaló (perímetro 51, signo 20, unidad 6, columna 2) ya no se presentan como plenamente revisadas.
2. **Unidad/escala corregida.** Eliminada la aceptación «la página menciona euros ⇒ miles de euros/escala 0,001». Ahora se exige frase de escala explícita en la página («miles de euros / thousands of euros») o en la cabecera del documento (primeras 8 páginas); si la página declara otra escala explícita («Amounts in euros», «in euros») con miles declarados → **CONFLICTO**. La sonda exacta del revisor (`check_unidad(['Amounts in euros','Revenue 1000'],1,'miles de euros','0.001',1000,'Revenue 1000')`) ahora devuelve CONFLICTO (antes OK) y está incluida como negativo 1/1 en `control_negativo.json`. Unidad: 459 OK / 8 NO_DECIDIBLE (páginas sin frase de escala ni en la cabecera del documento).
3. **Versión/reexpresión con evidencia independiente.** `check_version`: OK solo si el año del informe declarado (nombre del archivo) aparece en la página o en la cabecera del documento (467/467 OK). `check_reexpresion` (nuevo): contrasta el comparativo con el **texto conservado del año original** (p. ej., CF_2024.txt, CF_2017.txt): 238 OK (incluye reexpresados confirmados, p. ej., acreedores 2024 de Viscofan −2.953 en AR_2025 frente a −2.639 en CF_2024 original), 158 NO_DECIDIBLE (sin texto del año original —p. ej., comparativos 2016 de CF_2017— o partida no localizada), 71 NO_APLICA (columna del ejercicio corriente). Ya no se copia el metadato: el detalle antiguo «no decidible desde una página» desaparece como OK automático.
4. **No aplicable ≠ no comprobado.** Signo de ceros → NO_APLICA (13); perímetro declarado «no aplica» → NO_APLICA (4); reexpresión en columna corriente → NO_APLICA (71). El resto de no decidibles → PENDIENTE, no REVISADO.
5. **Propagación a derivados y mapa.** `DERIVADOS.json`: 51 REVISADO_CONTEXTUAL / 36 PENDIENTE / 14 REUTILIZADO_M1, con `limites_contextuales` propagados de los orígenes. `MAPA_REGENERACION.md` actualizado con la tabla de estados por grupo.
6. **Negativos ampliados** (`control_negativo.py`, 198 mutaciones en memoria sobre 49 entradas + la sonda del revisor): **151 detectadas por el verificador contextual; 40 por el mecánico (solo las de versión, porque cambian el archivo y falla la existencia)**. Desglose: euros frente a miles 1/1 (sonda del revisor), versión/informe equivocado 40/40, reexpresión declarada «no aplica» 3/3, columna/año 33/40, perímetro 38/40, partida 32/40, unidad 4/34. No se usa la ausencia de conflictos como prueba: los fallos restantes son límites del automatismo declarados (unidad en páginas sin frase de escala; filas no tabulares como el boletín BME; páginas sin marca de perímetro; partidas en filas de continuación lejanas).
7. **Conservado íntegramente**: los 677 registros, las huellas (251 insumos), los estados mecánicos (568 COINCIDE_PROPUESTO, 52 HIPOTESIS, 35 CONVENCION, 16 NO_APLICABLE, 6 DATO_AUSENTE), las 60 M1 (`REUTILIZADO_M1`), la evidencia contextual válida y la asociación texto↔PDF. No reabrí las 677 entradas a mano: la corrección es determinista sobre las entradas afectadas, con re-lectura documental solo donde procedía (cabeceras de documento para unidad/perímetro; textos del año original para reexpresión).

## Comandos realmente ejecutados (todos `python3 -B`, `PYTHONPATH=.trabajo/pylibs`)

- `git fetch origin revision/chatgpt-seguimiento-20261116` y `git show 63e366b:...PROMPTS.md` / `...SEGUIMIENTO.md` (lectura, sin fusionar).
- `python3 -B scripts/verificar_contexto.py` (v2) → `resultados/verificacion_contexto.jsonl`, `OBSERVACIONES.jsonl`.
- `python3 -B scripts/derivaciones.py` → `DERIVADOS.json` (estados/limites contextuales propagados).
- `python3 -B scripts/construir_cobertura.py` → `COBERTURA_677.csv` (677 filas; `estado_mecanico` sin cambios; `estado_contextual` corregido).
- `python3 -B scripts/control_negativo.py` → `resultados/control_negativo.json` (198 mutaciones; 151 ctx / 40 mec).
- `python3 -B scripts/control_cobertura.py` → **PASS, 0 violaciones** (exit 0).
- `python3 -B scripts/revisar_lote.py L00..L21` → lotes regenerados con estados contextuales v2.
- `python3 -B scripts/generar_manifiesto.py` → `MANIFIESTO_SHA256.txt`.

## Límites pendientes (honestos, no forzados)

- 160 fuentes en PENDIENTE_CONTEXTUAL: reexpresión no decidible en 158 (sin texto conservado del año original o partida no localizada en él), perímetro no decidible en 40 páginas sin marca (ni en la cabecera del documento), unidad no decidible en 8, signo en 7, columna en 3, fila en 1 (`Vidrala Historia!G23`). 36 derivados heredan esos límites.
- 52 HIPOTESIS, 35 CONVENCION, 16 NO_APLICABLE, 6 DATO_AUSENTE sin cambio (no son datos verificados).
- La heurística contextual (sinónimos ES/EN, anclaje de fila, contraste de reexpresión por etiqueta) tiene límites declarados en los negativos; no sustituye la revisión documental por otro contexto.

## Entrega

Rama `mistral/m2-cobertura-vm`; commits de esta corrección publicados con push (ver `git log` desde `54c8ddc`); escritura solo en `resultados_m2/cobertura_vm/`; sin PR, fusiones, producto, libros oficiales, decisiones ni políticas; sin LibreOffice/pipeline/macros; sin ciclos de autoaprobación. Modelo: `mistral-large-4-0`; consumo no visible desde la sesión.
