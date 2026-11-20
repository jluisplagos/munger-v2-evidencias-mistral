# Revisión independiente · `producto/minoritarios-cero` (decisión Z-MIN: minoritarios impresos en negativo → 0 con aviso)

- **Rama revisada:** `producto/minoritarios-cero` @ `cce98da` sobre `examen/expedientes-f1` @ `ebf47fc`:
  - `18a3ad2`: solo el manifiesto del árbol del examen en `ebf47fc`;
  - `6a3ef30`: el cambio;
  - `cce98da`: el manifiesto.
- **Revisor:** agente Claude distinto del autor (Opus, esfuerzo alto), 19-nov-2026. No modifiqué la rama.
- **Copias:**
  - copia limpia `git archive cce98da` con los 1059 binarios del manifiesto (copiados solo si su huella coincidía): 9832 archivos · 0 modificados / 0 ausentes / 0 de más;
  - `git archive` de los scripts de `ebf47fc` y de `cce98da` para comparar antes y después.

  Las borré al terminar.
- **Evidencia:** `evidencia/`.
- **Decisión que se aplica:** Z-MIN, `DECISIONES_PARA_EL_USUARIO.md` línea 133 y `examen/PREGUNTAS_PARA_LA_PERSONA.md`: «(a) cero con aviso y la cifra impresa en el registro».
- Experimental supervisado. **No apto para dinero real.**

## Veredicto: **CONFORME**

La regla hace exactamente lo que se decidió y nada más:

- `ajustar` devuelve `Fraction(0)` cuando `k == "minoritarios"` y el valor es negativo. Así no queda un −0: la prueba comprueba que se guarda «0.0».
- Las demás partidas y pensiones siguen con el valor absoluto, como antes.
- Las decisiones humanas de `fase1_decisiones.json` no pasan por `ajustar` y se copian igual que antes.
- El aviso de `historia_revision.md` da la cifra impresa, el año, el archivo y la página, y la fuente de la fila conserva «(impreso −2.0: minoritarios deficitarios → 0, decisión Z-MIN)».
- La plantilla no cambia: la fila 26 sigue ≥ 0.

### Comprobaciones

- **Diagnóstico.** Ejecuté `construir` con `ebf47fc` y con `cce98da` sobre copias de los **51** expedientes con `fase1_partes`, **Vinci incluido** (`vinci/Vinci` y `vinci/montaje/Vinci`). Comparé `fase1_v63.json`, `historia_revision.md` y la salida del programa (`evidencia/comparacion_51_expedientes.txt`).
  - Solo cambian las **3 copias de Zoetis** (zoetis_t1, t1b, t1c): minoritarios 2022 pasa de 2 a 0 y 2023 de 6 a 0, con su fuente, la tabla y el texto del aviso.
  - Los otros 37 que construyen, Vinci incluido, salen idénticos.
  - Los 11 que no construyen dan el mismo error con las dos versiones.
- **Pruebas.**
  - `test_minoritarios_cero.py` da **11/11**. Con el código de `ebf47fc` da **5/11**, y las 5 que pasan son comprobaciones de que el resto no cambia (construye; los demás años, el resto de la Historia y pensiones iguales; pensiones sin aviso). Ninguna pasa por el motivo equivocado.
  - El ajuste en `test_acciones_metadatos_exactas.py` es coherente: su comprobación del aviso de signo pasa de esperar 2.0 a esperar 0.0.
- **Baterías en la copia limpia** (`evidencia/bateria.txt`):

| Batería | Resultado |
|---|---|
| `verificar_paquete.sh` rápido (manifiesto 9832 · 0/0/0; bloque nuevo de minoritarios; acciones exactas; redondeo; entradas dependientes…) | **PASA GLOBAL** |
| `test_minoritarios_cero.py` | 11/11 |
| `test_acciones_metadatos_exactas.py` | 30/30 |
| `test_redondeo_historia.py` | 44/44 |
| `test_acciones_unidad_examen.py` | 10/10 |
| `test_entrada_efectiva_415.py` (LibreOffice) | PASA |
| `test_verificacion_entradas_414.py` | PASA |
| `test_motor_a_f1.py` | 177/177 |
| `test_pieza1.py` | 17/17 |
| `test_v631_f1.py` | 29/29 |

- **Manifiesto.**
  - `18a3ad2` lista el árbol de `ebf47fc`: 20 entradas de jumbo_g que el manifiesto `77bfd86` no tenía, sin cambios de producto.
  - `cce98da` solo cambia los 4 archivos del cambio.
  - La copia limpia verifica 9832 · 0/0/0.

### Observaciones (sin corrección)

1. **Alcance de la regla.** La decisión se tomó para Zoetis, pero queda como regla general del producto para todas las empresas. Es lo coherente con la opción (a) y con la plantilla. Hoy solo afecta a Zoetis.
2. **El bloque de `verificar_paquete.sh` es vacío sin el expediente.** Si falta zoetis_t1c, `minimo=0` y el bloque pasa con 0 comprobaciones; lo dice («OMITIDA»), pero no prueba nada. Mejora posible: un expediente sintético mínimo con un minoritario impreso en negativo, para que la regla se pruebe en cualquier paquete.
3. **Mensaje de reexpresión.** Si el informe propio y el comparativo imprimen minoritarios negativos distintos, el aviso de reexpresión mostrará «0 · 0», porque pasa por `ajustar`. El umbral sigue usando las cifras impresas, así que solo afecta al texto.
4. **Registro de las entradas.** La decisión pide «la cifra impresa en el registro». El producto la deja en la fuente y en `historia_revision.md`. En el expediente nuevo de Zoetis, las entradas `Historia!I26` y `J26` deben declararse 0 con la cifra impresa (−2 y −6) en su conciliación. Las entradas selladas de los expedientes actuales no se tocan.
5. **Pensiones**, como en la revisión de `minoritarios-acciones`: queda en valor absoluto y sin aviso, por diseño. La ambigüedad déficit/superávit sigue abierta para un cambio aparte.

## Integración en `examen/expedientes-f1`

- **Base:** `a28f851`. Es `ebf47fc` más un commit de jumbo_g (fase C turno 1), solo con archivos de jumbo_g.
- **`c1b0b77`**, `merge --no-ff` de `producto/minoritarios-cero` (`cce98da`):
  - Entran solo los 4 archivos aceptados: `personaje_v2/scripts/fase1_historia.py`, `personaje_v2/pruebas/test_minoritarios_cero.py`, `personaje_v2/pruebas/test_acciones_metadatos_exactas.py` y `verificar_paquete.sh`. Los 4 son idénticos a `cce98da`.
  - El manifiesto de la rama no se fusionó, porque no cubría `a28f851`.
  - No entró nada ajeno sin commit: ni los archivos `ahold_f4/` y `configuracion/cambio_ahold_f4.json`, que están sin seguimiento, ni la modificación en curso de `jumbo_g/Jumbo/fase_c.json`.
  - No ejecuté el pipeline ni toqué ningún expediente.
- **`6242bda`**, manifiesto regenerado en su propio commit. Lo generé sobre una copia limpia de `c1b0b77` con los 1059 binarios: **9838** archivos.
  - Frente al manifiesto anterior cambian los 4 archivos aceptados y 26 de jumbo_g. Esos 26 son los 20 que el autor ya había listado en `18a3ad2`, que comprobé, y los 8 de `a28f851`; dos están en los dos grupos.
  - Los de jumbo_g solo se listan; esta integración no los acredita.
- **`verificar_paquete.sh` rápido sobre esa copia:** **RESULTADO GLOBAL PASA** (9838 · 0/0/0). Salida en `evidencia/verificar_paquete_rapida_integracion_6242bda.txt`.
- **Push:** `origin/examen/expedientes-f1` = `6242bda`.

Nota: los agentes de jumbo_g, ahold_f4 y Vinci trabajan en el mismo worktree. Desde `c1b0b77`, cualquier `construir` que lancen usa la regla Z-MIN, pero en sus expedientes el diagnóstico no da ningún cambio. Además, el paso 2 del pipeline solo construye si falta `fase1_v63.json`.
