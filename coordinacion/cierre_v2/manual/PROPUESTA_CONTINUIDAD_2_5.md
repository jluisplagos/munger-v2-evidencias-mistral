# Propuesta de corrección documental · `munger_v2_r1/CONTINUIDAD.md` §2.5 (espacio en disco) · candidata `b129b36` · NO APLICADA

**Qué es.** El texto exacto que este borrador propondría cambiar en CONTINUIDAD §2, punto 5, de la candidata `integracion/candidata-cierre-v2` @ `b129b36` (`munger_v2_r1/CONTINUIDAD.md` es igual que en `3149128`: G-RAIZ solo cambia tres archivos de la raíz). **No se aplica aquí.** Si se acepta, irá en una corrección documental aparte, con su propia revisión por un agente distinto del autor (`CLAUDE.md:33` de `b129b36`; `:31` en `3149128`), como G-DOCS. El manual operativo no corrige el producto: solo señala la contradicción (C-14 de `EVID/coordinacion/cierre_v2/manual/MANUAL_OPERATIVO_b129b36_v4.md`, §3.2 y §12.2; antes, de la v3, `EVID/coordinacion/cierre_v2/manual/MANUAL_OPERATIVO_3149128_v3.md`).

**Revisión 3.** Corrige M1 (el control 4.8 también copia `_v64/`), m2 (el 4.8.1 no excluye solo tres carpetas), m7 (el temporal del sistema), m8 (fuentes sin prefijo) y m9 (método del sondeo de literales) de `EVID/coordinacion/cierre_v2/revisiones_coordinador/MANUAL_v2_ef36ab1/REVISION_MANUAL_v2_ef36ab1.md`. La revisión 2 está en Git, en el commit `ef36ab1`. La propuesta **sigue sin aplicarse**.

**Revisión 4.** Atiende los menores n6 y n9 de `EVID/coordinacion/cierre_v2/revisiones_coordinador/MANUAL_v3_88144b5/REVISION_MANUAL_v3.md` (§4.2) y la cita de `CLAUDE.md` desplazada por G-RAIZ (N1). **No cambia el texto de ninguna frase propuesta ni actual**: el sondeo de literales y su resultado siguen valiendo tal cual. La revisión 3 está en Git, en el commit `88144b5`.

**Fuentes.** Las rutas sin prefijo son del producto, relativas a la raíz del repositorio en `3149128`; en `b129b36` son iguales, salvo `CLAUDE.md`, que se cita en `b129b36`. `EVID/` = repositorio `jluisplagos/munger-v2-evidencias-mistral`, rama `coordinacion/cierre-v2`, leída en `acea175` (los archivos de `EVID/` que se citan aquí no cambian desde `6889b02`). Las fuentes de `EVID/` se citan siempre con la ruta completa: el producto tiene otro `INFORME_TRASPASO.md`, el de la 4.14 (`munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/documentacion_cierre_4_14/traspaso/INFORME_TRASPASO.md`), cuyas líneas dicen otra cosa.

**Por qué.** `munger_v2_r1/CONTINUIDAD.md:143` dice que «los controles no recorren `_v64/`». Por lectura del código de los 19 controles que lanza `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_13/scripts/controles_historicos_4_13.py:28-48`, dos sí lo copian:
- **4.8.1.** Copia `personaje_v2/` excluyendo `empresas_v2`, `.lo_perfil`, `__pycache__` y, dentro de `empresas_v2_correcciones/`, todo salvo `2026-11_Vidrala_ensayo_4_6_1`; así que copia `pruebas/_v64/` (`munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_8_1/scripts/comprobar_entrega_4_8_1.py:76-77`). Por eso se quedó sin espacio en la prueba de traspaso del 17-nov (`EVID/coordinacion/cierre_v2/traspaso/revision_20261117/REVISION_TRASPASO.md:197`; `EVID/coordinacion/cierre_v2/traspaso/revision_20261117/MEJORAS_MANUAL.md:8`).
- **4.8.** Copia `personaje_v2/` excluyendo `empresas_v2`, `empresas_v2_correcciones`, `.lo_perfil`, `__pycache__` y `sintetico`; así que también copia `pruebas/_v64/` (`munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_8/scripts/comprobar_entrega_4_8.py:60`, función `arbol_codigo_471`). Lo hace una vez, en un temporal (`:75`, `tempfile.mkdtemp(prefix="c48_")`), que borra al final (`:195`). En el traspaso no falló: se ejecutó antes que el 4.8.1 (`controles_historicos_4_13.py:39`, `:41`) y dio 32 de 36 (`EVID/coordinacion/cierre_v2/traspaso/resultado_20261117/registro/paso10_controles_historicos/resumen.md:15`).
- **4.9.** Recorre todo el árbol con `os.walk`, sin excluir `_v64/` (`munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_9/scripts/comprobar_entrega_4_9.py:84`). *Interpretación:* no afecta al resultado ni al disco, porque el conjunto obtenido (`actuales`) no se usa después.

La frase es cierta para el resultado del 4.8.1 (no evalúa `_v64/`, `EVID/coordinacion/cierre_v2/traspaso/revision_20261117/REVISION_TRASPASO.md:197`), pero no para el disco, ni en el 4.8.1 ni en el 4.8.

---

## Cambio 1 (el que se pide): corregir la frase sobre `_v64/`

**Dónde:** `munger_v2_r1/CONTINUIDAD.md:143`, tercera frase del párrafo.

**Frase actual (literal):**

> Si falta espacio, terminada la verificación se pueden borrar los `*.xlsx` y `vigencia/` de `personaje_v2/pruebas/_v64/` (los controles no recorren `_v64/`), registrando las rutas (regla 11.10).

**Frase nueva (propuesta):**

> Si falta espacio, terminada la verificación se pueden borrar los `*.xlsx` y `vigencia/` de `personaje_v2/pruebas/_v64/`, registrando las rutas (regla 11.10). Hay que hacerlo antes de los controles de la 4.8 y la 4.8.1: los dos copian `personaje_v2/` con `pruebas/_v64/` en el temporal del sistema (`${TMPDIR:-/tmp}`; `comprobar_entrega_4_8.py`, función `arbol_codigo_471`, y `comprobar_entrega_4_8_1.py`, función `arbol`). El de la 4.8.1 no evalúa su contenido.

**Fuentes:**

| Afirmación de la frase nueva | Fuente |
|---|---|
| El 4.8.1 copia `personaje_v2/` con `pruebas/_v64/` | `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_8_1/scripts/comprobar_entrega_4_8_1.py:73-77` (función `arbol`; exclusiones en `:76-77`) |
| El 4.8 copia `personaje_v2/` con `pruebas/_v64/` | `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_8/scripts/comprobar_entrega_4_8.py:54-60` (función `arbol_codigo_471`; exclusiones en `:60`; se llama en `:82`) |
| En el temporal del sistema (`${TMPDIR:-/tmp}`) | `comprobar_entrega_4_8_1.py:38` (`tempfile.mkdtemp(prefix="control481_")`), que se borra solo al final (`:184`); `arbol` se llama en `:109`, dos veces en el bucle de `:124-125` y en `:130`. `comprobar_entrega_4_8.py:75` (`tempfile.mkdtemp(prefix="c48_")`), que se borra al final (`:195`). `tempfile.mkdtemp` usa `TMPDIR`, `TEMP` o `TMP` si están definidas y, si no, `/tmp` (después, `/var/tmp`, `/usr/tmp` o la carpeta actual; biblioteca estándar de Python, `tempfile._candidate_tempdir_list`). El propio §2.5 dice `/tmp` (`munger_v2_r1/CONTINUIDAD.md:141`). `${TMPDIR:-/tmp}` es una **simplificación** del caso habitual, no la regla completa |
| El de la 4.8.1 no evalúa su contenido | `EVID/coordinacion/cierre_v2/traspaso/revision_20261117/REVISION_TRASPASO.md:197` («copia `_v64/`, pero no lo evalúa») |
| El 4.8.1 se quedó sin espacio al copiar `_v64/vigencia/` | `EVID/coordinacion/cierre_v2/traspaso/resultado_20261117/registro/paso10_controles_historicos/resumen.md:17` (`shutil.Error` sobre `…/pruebas/_v64/vigencia/…`, con destino en `control481_…`, dentro del temporal del sistema) |
| Borrar antes del 4.8.1 basta para que termine, con el mismo resultado | `EVID/coordinacion/cierre_v2/traspaso/resultado_20261117/registro/paso10b_4_8_1_reintento.txt:38` (25 de 30); `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/resultados/LEEME_CONTROLES_HISTORICOS_4_14.md:36` (25 de 30 en el árbol 4.14); `EVID/coordinacion/cierre_v2/traspaso/revision_20261117/REVISION_TRASPASO.md:194-196` |
| Borrar y registrar las rutas lo autoriza el propio §2.5 | `munger_v2_r1/CONTINUIDAD.md:143`; regla 11.10 (`munger_v2_r1/CONTINUIDAD.md:384-386`) |

**Qué no dice, a propósito:**
- No dice que la limpieza deje igual el resultado del 4.8. En el traspaso, el 4.8 se ejecutó **antes** de la limpieza (32 de 36; `EVID/coordinacion/cierre_v2/traspaso/resultado_20261117/registro/paso10_controles_historicos/resumen.md:15`). Ese es también su resultado en el árbol 4.14 (`munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/resultados/LEEME_CONTROLES_HISTORICOS_4_14.md:32`). Su resultado **después** de la limpieza no se ha observado. La corrección documental lo comprueba antes de aplicar la frase o, si no puede, la limita al 4.8.1.
- No dice que el 4.8 no evalúe `_v64/`. Por lectura, el 4.8 ejecuta en el árbol copiado `reproducir_xa_xc.py` y `test_estados_v2.py` (`comprobar_entrega_4_8.py:85`, `:94`). Que ninguno de los dos lea `pruebas/_v64/` no se ha comprobado.
- No afirma nada de los otros 17 controles. Por lectura: el 4.9 recorre `_v64/` sin efecto (`comprobar_entrega_4_9.py:84`); el 4.11, el 4.12 y el 4.13 lo excluyen (`comprobar_entrega_4_11.py:87`, `comprobar_entrega_4_12.py:91`, `comprobar_entrega_4_13.py:107`); los demás no copian ni recorren el árbol entero. Con la limpieza antes de la pasada completa, su resultado no se ha observado.
- No unifica las dos formas del temporal. Si se aplica la frase 1, `munger_v2_r1/CONTINUIDAD.md:141` (`/tmp`) y `:143` (`${TMPDIR:-/tmp}`) quedan juntas con dos formas. La corrección documental decide si ajusta también `:141` o si deja la diferencia; esta propuesta no da texto para `:141`, porque eso cambiaría el sondeo de literales.
- No fija un orden respecto de los demás controles históricos: en el traspaso se limpió después de la primera pasada y solo se repitió el 4.8.1 (`EVID/coordinacion/cierre_v2/traspaso/resultado_20261117/INFORME_TRASPASO.md:34`).

## Cambio 2 (opcional): dejar constancia de lo observado en la 4.15

Es una decisión del revisor de la corrección. Sus cifras de espacio libre son **autodeclaradas**: el receptor no registró ningún `df` (`EVID/coordinacion/cierre_v2/traspaso/revision_20261117/REVISION_TRASPASO.md:67-68`).

**Dónde:** `munger_v2_r1/CONTINUIDAD.md:143`, segunda frase del párrafo.

**Frase actual (literal):**

> Conviene tener al menos 7 GB libres después de descomprimir.

**Frase nueva (propuesta):**

> Conviene tener al menos 7 GB libres después de descomprimir. En la prueba de traspaso de la 4.15 (vía del repositorio, 17-nov-2026), unos 8,4 GB libres al empezar los controles no bastaron para el de la 4.8.1; tras la limpieza que sigue, con unos 13 GB, terminó con el mismo resultado que en el árbol 4.14 (25 de 30).

**Fuentes:**
- `EVID/coordinacion/cierre_v2/traspaso/resultado_20261117/INFORME_TRASPASO.md:33` (8,4 GB, `[Errno 28]`), `:34` (13 GB, 25 de 30) y `:78` (pico de ≈9,8 GB ocupados en la carpeta);
- `EVID/coordinacion/cierre_v2/traspaso/resultado_20261117/registro/paso10b_4_8_1_reintento.txt:38`;
- `EVID/coordinacion/cierre_v2/traspaso/revision_20261117/REVISION_TRASPASO.md:207`.

**Variante sin cifras autodeclaradas**, si el revisor no quiere citarlas en un documento del producto:

> Conviene tener al menos 7 GB libres después de descomprimir. En la prueba de traspaso de la 4.15 (vía del repositorio) esa cantidad no bastó para el control de la 4.8.1, que terminó después de la limpieza que sigue.

**Qué no hace:** no fija un mínimo nuevo para la vía del repositorio. Ninguna fuente lo da (`EVID/coordinacion/cierre_v2/manual/MANUAL_OPERATIVO_b129b36_v4.md`, N-05, igual que en la v3).

---

## Efectos de aplicarla (para quien haga la corrección)

- **Archivos que cambian:** `munger_v2_r1/CONTINUIDAD.md` y, por estar en el manifiesto, `munger_v2_r1/MANIFIESTO_SHA256.txt` y `munger_v2_r1/CAMBIOS_ARCHIVOS.txt` (`CONTINUIDAD.md` está en `CAMBIOS_ARCHIVOS.txt:81`). G-DOCS los regeneró con `personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/scripts/generar_cambios_y_manifiesto_4_15.py` (`munger_v2_r1/CAMBIOS_ARCHIVOS.txt:1`).
- **Sin cambios de código** ni de ninguna prueba.
- **Controles que leen `CONTINUIDAD.md`.** Los históricos sí lo leen (por ejemplo, `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_8_1/scripts/comprobar_entrega_4_8_1.py:177-180`). **Sondeo de literales de este borrador**, sin ejecutar nada del producto (script y salida en `EVID/coordinacion/cierre_v2/manual/sondeo_literales_v3/`, a partir de `EVID/coordinacion/cierre_v2/revisiones_coordinador/MANUAL_v2_ef36ab1/sondas/herramientas/sonda_literales.py`):
  - *método:* se reúnen todas las constantes de texto (las `ast.Constant` de tipo `str`; en una f-string, cada trozo fijo) de los 145 scripts `*.py` de `personaje_v2/empresas_v2_correcciones/*/scripts/`, `personaje_v2/pruebas/` y `contrastes/*/scripts/` de `3149128`, 13129 distintas. Después se aplican en memoria, con `git show`, los cambios 1 y 2 (o el 1 y la variante del 2) al texto de `CONTINUIDAD.md`, y se mira qué constantes están en un texto y no en el otro. Las dos frases actuales están una vez cada una;
  - *resultado sin filtro:* con los cambios 1 y 2, y con el 1 y la variante, aparecen 3 constantes: `'$'`, `'TMP'` y `'TMPDIR'`. Salen del `${TMPDIR:-/tmp}` de la frase 1 y son de `dependencias_v63.py:24`, `empaquetar_cambios_4_15.py:47`, `reproducir_r1_r3.py:47` y `propuesta_excel.py:49`. Ninguna desaparece;
  - *filtros:* (A) constantes de los 19 controles que lanza `controles_historicos_4_13.py:28-48`: 0 aparecen o desaparecen; (B) constantes de los 11 scripts que nombran `CONTINUIDAD`: 0;
  - *interpretación:* no se espera que cambie el resultado de ningún control. La conclusión depende de esos filtros: `propuesta_excel.py`, que el control 4.7 nombra, usa `'TMPDIR'` para elegir un temporal (`propuesta_excel.py:49`), no para buscarlo en `CONTINUIDAD.md`. El sondeo no sustituye a ejecutar los controles: la corrección documental lo comprueba por su cuenta.
- **No cambia** ninguna política económica, aprobación, firma ni aptitud. El producto sigue siendo experimental supervisado y no apto para dinero real.

## Fuera de esta propuesta (observaciones, sin texto propuesto)

Se anotan para que la corrección documental decida si las incluye. Aquí no se proponen.
- `munger_v2_r1/CONTINUIDAD.md:115`: «25–45 minutos»; en la 4.15 la verificación completa tardó 53–60 min (C-11 del manual).
- `munger_v2_r1/CONTINUIDAD.md:151` frente a `:152`: «sale con código 10 sin hacer nada más» frente a la detección del relevo caducado al relanzar (C-15 del manual).
