# Propuesta de corrección documental · `munger_v2_r1/CONTINUIDAD.md` §2.5 (espacio en disco) · candidata `3149128` · NO APLICADA

**Qué es.** El texto exacto que este borrador propondría cambiar en CONTINUIDAD §2, punto 5, de la candidata `integracion/candidata-cierre-v2` @ `3149128`. **No se aplica aquí.** Si se acepta, irá en una corrección documental aparte, con su propia revisión por un agente distinto del autor (`CLAUDE.md:31`), como G-DOCS. El manual operativo no corrige el producto: solo señala la contradicción (C-14 de `MANUAL_OPERATIVO_3149128.md`, §3.2 y §12.2).

**Por qué.** `munger_v2_r1/CONTINUIDAD.md:143` dice que «los controles no recorren `_v64/`». El control de la 4.8.1 sí lo recorre: copia `personaje_v2/` excluyendo solo `empresas_v2`, `.lo_perfil` y `__pycache__`, así que copia `pruebas/_v64/` (`personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_8_1/scripts/comprobar_entrega_4_8_1.py:76-77`). Por eso se quedó sin espacio en la prueba de traspaso del 17-nov (`EVID/coordinacion/cierre_v2/traspaso/revision_20261117/REVISION_TRASPASO.md:197`; `EVID/coordinacion/cierre_v2/traspaso/revision_20261117/MEJORAS_MANUAL.md:8`). La frase es cierta para el resultado (no evalúa `_v64/`), pero no para el disco.

`EVID/` = repositorio `jluisplagos/munger-v2-evidencias-mistral`, rama `coordinacion/cierre-v2` @ `6889b02`.

---

## Cambio 1 (el que se pide): corregir la frase sobre `_v64/`

**Dónde:** `munger_v2_r1/CONTINUIDAD.md:143`, tercera frase del párrafo.

**Frase actual (literal):**

> Si falta espacio, terminada la verificación se pueden borrar los `*.xlsx` y `vigencia/` de `personaje_v2/pruebas/_v64/` (los controles no recorren `_v64/`), registrando las rutas (regla 11.10).

**Frase nueva (propuesta):**

> Si falta espacio, terminada la verificación se pueden borrar los `*.xlsx` y `vigencia/` de `personaje_v2/pruebas/_v64/`, registrando las rutas (regla 11.10). Hay que hacerlo antes del control de la 4.8.1: ese control copia `personaje_v2/` con `pruebas/_v64/` en temporales de `/tmp` (`comprobar_entrega_4_8_1.py`, función `arbol`), aunque no evalúa su contenido.

**Fuentes:**

| Afirmación de la frase nueva | Fuente |
|---|---|
| El 4.8.1 copia `personaje_v2/` con `pruebas/_v64/` | `…/2026-11_Vidrala_ensayo_4_8_1/scripts/comprobar_entrega_4_8_1.py:73-77` (función `arbol`; exclusiones en `:76-77`) |
| En temporales de `/tmp` | `comprobar_entrega_4_8_1.py:38` (`tempfile.mkdtemp(prefix="control481_")`); se borran solo al final, en `:184`; `arbol` se llama en `:109`, `:125` y `:130` |
| No evalúa su contenido | `REVISION_TRASPASO.md:197` («copia `_v64/`, pero no lo evalúa») |
| Se quedó sin espacio al copiar `_v64/vigencia/` | `EVID/coordinacion/cierre_v2/traspaso/resultado_20261117/registro/paso10_controles_historicos/resumen.md:17` (`shutil.Error` sobre `…/pruebas/_v64/vigencia/…` → `/tmp/control481_…`) |
| Borrar antes del 4.8.1 basta para que termine, con el mismo resultado | `…/registro/paso10b_4_8_1_reintento.txt:38` (25 de 30); `…/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/resultados/LEEME_CONTROLES_HISTORICOS_4_14.md:36` (25 de 30 en el árbol 4.14); `REVISION_TRASPASO.md:194-196` |
| Borrar y registrar las rutas lo autoriza el propio §2.5 | `munger_v2_r1/CONTINUIDAD.md:143`; regla 11.10 (`munger_v2_r1/CONTINUIDAD.md:384-386`) |

**Qué no dice, a propósito:**
- No afirma que ningún otro control recorra `_v64/`. Por lectura, el 4.11, el 4.12 y el 4.13 lo excluyen (`comprobar_entrega_4_11.py:87`, `comprobar_entrega_4_12.py:91`, `comprobar_entrega_4_13.py:107`); de los demás no hay comprobación.
- No fija un orden respecto de los otros controles históricos: en el traspaso se limpió después de la primera pasada y solo se repitió el 4.8.1 (`EVID/coordinacion/cierre_v2/traspaso/resultado_20261117/INFORME_TRASPASO.md:34`).

## Cambio 2 (opcional): dejar constancia de lo observado en la 4.15

Es una decisión del revisor de la corrección. Sus cifras de espacio libre son **autodeclaradas**: el receptor no registró ningún `df` (`REVISION_TRASPASO.md:67-68`).

**Dónde:** `munger_v2_r1/CONTINUIDAD.md:143`, segunda frase del párrafo.

**Frase actual (literal):**

> Conviene tener al menos 7 GB libres después de descomprimir.

**Frase nueva (propuesta):**

> Conviene tener al menos 7 GB libres después de descomprimir. En la prueba de traspaso de la 4.15 (vía del repositorio, 17-nov-2026), unos 8,4 GB libres al empezar los controles no bastaron para el de la 4.8.1; tras la limpieza que sigue, con unos 13 GB, terminó con el mismo resultado que en el árbol 4.14 (25 de 30).

**Fuentes:** `INFORME_TRASPASO.md:33` (8,4 GB, `[Errno 28]`), `:34` (13 GB, 25 de 30) y `:78` (pico de ≈9,8 GB ocupados en la carpeta); `…/registro/paso10b_4_8_1_reintento.txt:38`; `REVISION_TRASPASO.md:207`.

**Variante sin cifras autodeclaradas**, si el revisor no quiere citarlas en un documento del producto:

> Conviene tener al menos 7 GB libres después de descomprimir. En la prueba de traspaso de la 4.15 (vía del repositorio) esa cantidad no bastó para el control de la 4.8.1, que terminó después de la limpieza que sigue.

**Qué no hace:** no fija un mínimo nuevo para la vía del repositorio. Ninguna fuente lo da (`MANUAL_OPERATIVO_3149128.md`, N-05).

---

## Efectos de aplicarla (para quien haga la corrección)

- **Archivos que cambian:** `munger_v2_r1/CONTINUIDAD.md` y, por estar en el manifiesto, `munger_v2_r1/MANIFIESTO_SHA256.txt` y `munger_v2_r1/CAMBIOS_ARCHIVOS.txt` (`CONTINUIDAD.md` está en `CAMBIOS_ARCHIVOS.txt:81`). G-DOCS los regeneró con `personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/scripts/generar_cambios_y_manifiesto_4_15.py` (`munger_v2_r1/CAMBIOS_ARCHIVOS.txt:1`).
- **Sin cambios de código** ni de ninguna prueba.
- **Controles que leen `CONTINUIDAD.md`.** Los históricos sí lo leen (por ejemplo, `…/2026-11_Vidrala_ensayo_4_8_1/scripts/comprobar_entrega_4_8_1.py:177-180`). Sondeo de lectura de este borrador, sin ejecutar nada: con los cambios 1 y 2 aplicados sobre una copia del archivo en la carpeta temporal, ningún texto literal de los scripts de `personaje_v2/empresas_v2_correcciones/*/scripts/`, `personaje_v2/pruebas/` ni `contrastes/*/scripts/` aparece ni desaparece. *Interpretación:* no se espera que cambie el resultado de ningún control. La corrección documental lo comprueba por su cuenta.
- **No cambia** ninguna política económica, aprobación, firma ni aptitud. El producto sigue siendo experimental supervisado y no apto para dinero real.

## Fuera de esta propuesta (observaciones, sin texto propuesto)

Se anotan para que la corrección documental decida si las incluye. Aquí no se proponen.
- `munger_v2_r1/CONTINUIDAD.md:115`: «25–45 minutos»; en la 4.15 la verificación completa tardó 53–60 min (C-11 del manual).
- `munger_v2_r1/CONTINUIDAD.md:151` frente a `:152`: «sale con código 10 sin hacer nada más» frente a la detección del relevo caducado al relanzar (C-15 del manual).
