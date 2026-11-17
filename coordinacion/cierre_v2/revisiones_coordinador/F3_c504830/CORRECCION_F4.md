# Corrección F4 · Mistral F · sobre la respuesta a F3 (`98bdf8f` … `c504830`)

- **Para:** Mistral F, rama `mistral/f-alcance-real`.
- **De:** propuesta del revisor independiente, según [REVISION_F3_c504830.md](REVISION_F3_c504830.md). La emite o modifica el coordinador.
- **Alcance:** solo lo que sigue abierto. Escribir solo en `resultados_cierre/alcance_real/`. No se toca el producto, `main`, CONTROL ni ESTADO. Sin LibreOffice ni pipeline. No se fija política económica ni se nombra candidata.

## Clasificación

- **Cerrados:** R3, R4, R5, R7, R8 (y R10, ya en `98bdf8f`).
- **Cerrados con límites:** R6, R9, R11 y R13.
- **Abiertos:** R12, R14 y R15.
- **Se conserva:**
  - el inventario byte a byte con los 4 `.bat` y el alcance negativo 6476/323;
  - los 71 PDF con huella;
  - el contrato C técnico: C62, quiebra, g_t, excedente limpio y ROE de cierre/apertura;
  - las citas del contrato, el protocolo y el MAPA;
  - el manifiesto 53/53.

## Contexto nuevo que la entrega no conocía (posterior a `c504830`, 13:18:19Z)

- **U3 decidida** por la persona responsable (`72c49e5`).
- **FinecoBank** se descargó, se verificó y **no encaja tal como está escrito el protocolo C**: falla C4 y C3 es dudoso (`u3_motor_c/verificacion_fineco_20261117/VERIFICACION_FINECO.md`, `245a2e6b…6839`). Se busca otro candidato (`a79e62d`).
- **U2:** la persona responsable aportó la etapa 1 de Ahold (`3b07d89`; rama `fuentes/ahold-etapa1-20261117`).

## Defectos

| | Defecto | Prueba de cierre |
|---|---|---|
| **F4-1 (R12, medio)** | `PROTOCOLO_CONGELADO.md` §2.1.1–5 (`:24-39`) mantiene criterios propios de admisión y desempate de C, distintos de los de U3: no tiene C2, C3, C4 ni X1–X4, y desempata de otra forma. Con los datos de hoy admitiría a FinecoBank, que U3 rechaza. `:26` repite «antes de nombrar ninguna candidata» sin la salvedad de R12. | §2.1 no tiene criterios propios de C: remite a `u3_motor_c/PROTOCOLO_SELECCION_C.md` con su SHA-256. `:26` lleva la salvedad (U3 había nombrado candidatas a las 09:36:01Z). Ningún texto de F admite un caso que U3 rechaza. |
| **F4-2 (contexto)** | Textos desfasados: «descargas de Fineco denegadas», «lista Fineco/Hannover», «contrato U3 **de la persona responsable**», «Ahold sin Excel de etapa 1» y «candidata fijada por el coordinador».<br>Están en `CONTRATO_C_PROPUESTA.md:3-4,100-105`; `PROTOCOLO_CONGELADO.md:40-43,71-73`; `ENTREGA_F3.json:79,91`; `RESPUESTA_F3.md:53`; `PUNTO_DE_RECUPERACION.md:34-37,57-59`; `SELECCION.csv:2,6`; README (Hallazgos C); `ENTREGA_F2.json:110`. | Reflejan el estado vigente:<br>- FinecoBank verificado y no encaja tal como está escrito el protocolo (cita y SHA-256 de `VERIFICACION_FINECO.md`), y se busca otro candidato;<br>- la elección es de la persona responsable sobre U3;<br>- el contrato U3 es una propuesta del coordinador, no adoptada;<br>- la aportación U2 de Ahold aparece nombrada.<br>Ningún texto da por elegida una candidata. El inventario del ZIP no cambia. |
| **F4-3 (R14)** | Sigue `ENTREGA_F2.json:22`, «@57b34a6 … sin cambios posteriores». Siguen en `COMANDOS.md:164` las citas viejas (`933-945`, `1136-1147`, `147`, `test_fill.py:93-99`). | Las dos corregidas como en `RESPUESTA_F2.md`. `grep -n '933-945\|sin cambios posteriores'` no devuelve nada vigente. |
| **F4-4 (R15)** | - La prueba 4 de `ENTREGA_F2` (`:92`) usa el rango `868f448..98bdf8f`, que excluye los commits cuyas horas declara (`:96`: 90329a1 … 868f448).<br>- La hora final sigue en «09:44» en `ENTREGA_F2.json:17,96` y `RESPUESTA_F2.md:4,35`.<br>- En F3 se repite: dice «13:05–13:16» (`RESPUESTA_F3.md:4,49`; `ENTREGA_F3.json:13`) y el último commit es de las 13:18:19Z; `COMANDOS.md:179` dice «~13:20». | - La prueba 4 lista exactamente los commits cuyas horas declara.<br>- Las horas finales coinciden con el último commit de cada bloque en todos los archivos. |
| **F4-5 (R9)** | Dos «comandos» siguen siendo descripciones con `EJECUTADO` y código 0: `ENTREGA_B3_C1.json:63` (prueba 2) y `ENTREGA_B_PM1.json:69` (prueba 3). Ejecutados tal cual, dan código 2. | Se ejecutan tal cual con código 0, o se declaran como consulta descriptiva (`exit_observado` null y el resultado de la plantilla). RESPUESTA_F3 y ENTREGA_F3 dejan de decir «todos ejecutables tal cual» si no lo son. |
| **F4-6 (R9)** | La prueba de `tablas_vidrala.py` (`ENTREGA_F3` prueba 2; `ENTREGA_B_PM1` prueba 1) pasa aunque el script no se ejecute, porque `git archive` ya trae el CSV. | Se borra el CSV extraído antes del script y se registra un control negativo: sin el script, el `cmp` falla. |
| **F4-7 (nuevo)** | `ENTREGA_F3.json:41` atribuye a `verificar_contrato_c.py` la cobertura de R5 (C62) y de R6 (citas). El script no lee el producto. | Se quitan de esa prueba, o se añade una prueba que los compruebe contra `build_v6.py`/`referencia_V6.3.json` y produzca la evidencia r6 byte a byte. |
| **F4-8 (R6/R15)** | `COMANDOS.md:193`: `sed -n '…960-963p…'` no se ejecuta (`unknown command: '-'`). `<clon_producto>` no está definido (`:183`). | `960,963p` y la variable definida. La salida coincide con la evidencia r6. |
| **F4-9 (R11)** | Restos:<br>- `ENTREGA_B3_C1.json:22`: «verificado por mi en .trabajo/insumos_m2»;<br>- `:99`: siguiente acción de F2;<br>- `PROTOCOLO_CONGELADO.md:47`: «6798/6798 verificados». | Alineados con `ENTREGA_B_PM1` y `PUNTO`: el ZIP, 6799 = 6798 + manifiesto, y la siguiente acción vigente. |
| **F4-10 (R13, cosmético)** | Cambian cuatro filas B del MAPA (1, 5, 10 y 13) que no se habían tocado en `e9f76a9`, y se presentan como «restaurados». | Filas B idénticas a `195766f`, o el cambio declarado como ortográfico nuevo. |

## Entrega

- Un commit por bloque.
- `correccion_f4/ENTREGA_F4.json`, según `PLANTILLA_ENTREGA.json`, y `RESPUESTA_F4.md`, solo con F4-1 a F4-10.
- Manifiesto regenerado con `sha256sum -c` en 0.

**Bloqueos que no son de F:** la elección del candidato C (U3) y el uso de los originales de Ahold (U2) corresponden a la persona responsable.
