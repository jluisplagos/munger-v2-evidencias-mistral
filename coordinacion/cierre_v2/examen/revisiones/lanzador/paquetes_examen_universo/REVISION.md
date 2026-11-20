# Revisión independiente · paquetes del examen y del universo (análisis directo)

- Rama revisada: `automatizacion/paquetes-examen-y-universo` en `4715abb` (commits `2be86dc`, `a2981be`, `4715abb`) sobre `origin/main` `833cd50`.
- Revisor: agente Claude (Opus 5.5), distinto del autor. Revisión enfocada en riesgos, no exhaustiva. Fecha: 19-nov-2026.
- No se ha tocado la rama del autor. Sin llamadas a la API.

## Veredicto

**Conforme con correcciones.** Dos correcciones menores en la copia de los datos de Vinci (C1 y C2). Todo lo demás conforme; quedan observaciones para la persona responsable.

## 1. Límites de seguridad

- `git diff origin/main 4715abb` no cambia `.github/`, `direct_analysis.py`, `revalidar.py`, `screening.py`, `excepciones_ceguera.json` ni `automation/coordination/`. Solo cambian los dos README; lo demás es nuevo.
- El workflow sigue igual: entorno `inferencia-aprobada` (aprobación humana), `--max-usd` desde `coste_maximo_usd`, tope acumulado y reserva de AUTO1 intactos.
- `preparar_paquete.py`, `universo.py` y `finalistas.py` no usan red, API ni variables de entorno. El workflow no los ejecuta.
- No hay claves en los archivos nuevos. Las reservas de todos los paquetes nuevos están por debajo de 5 USD (lo comprueba `test_paquetes.py`).

## 2. Reproducibilidad (ejecutado por el revisor)

- `unittest discover` en `automation/direct_analysis`: 59 pruebas OK. En `automation/screening`: 44 pruebas OK.
- Prueba sin API (`direct_analysis.py` sin `--execute-api`, con todas las ramas remotas visibles para la ceguera):
  - `vinci`, `zoetis-t2`, `fw-thorpe`, `azkoyen`, `betsson` y `cocacola` quedan en `PREPARADO_SIN_API`, con 0 mensajes.
  - `elis` falla con `SOLAPE_CON_MATERIAL_CIEGO:…/evidencia_ronda2/fecha_del_precio_en_los_12.txt`, como declara el autor. El control de solape funciona y no se ha relajado.
- `preparar_paquete.py comprobar`, con los PDF y el HTML descargados de la Release `fuentes-examen-20261118` y los clones del auxiliar y del producto (`ee1ca6a`): **Vinci da `IGUAL`** y **Zoetis T2 da `IGUAL`**.
  - No se reprodujeron Elis (bloqueado; falta el ZIP del universo en local) ni `recetas/zoetis.json` (falta el 10-Q del T1 en esa Release).
- `finalistas.py`, con el registro `9e1868d` (que es el `origin` actual) y las cuatro ejecuciones declaradas, regenera el `.md` idéntico: 61 empresas leídas; finalistas FW_Thorpe, Azkoyen, Betsson y CocaCola.

## 3. Ceguera e independencia

- Ningún paquete lleva rúbrica, contradictor ni revisiones. Los paquetes del universo solo llevan la etapa 1 (respuesta y cuatro hojas en CSV). La mención «regla del personaje» de FW_Thorpe está en la respuesta de etapa 1 de la persona, que sí debe ir.
- Las notas «SUPUESTO DE LA ORQUESTACIÓN» y las referencias a decisiones de la persona responsable (P-O1 (c) del 18-nov, P-O2, Z-ACC) en `datos_v63.md` y `fase1_v63.json` son tratamientos de datos del expediente. La misma práctica está en los paquetes ya fusionados de Ahold, Jumbo y Zoetis T1, y son los mismos datos que recibe el personaje. Se aceptan por coherencia con esos paquetes; ver la observación O1.
- **Edición de Vinci (retirada de la «1 bis»): legítima.** El diff con el original del producto (`ee1ca6a`) muestra solo la sección «1 bis» y las tres remisiones «; ver 1 bis». Las cifras de la Historia quedan intactas. La sección era una regla del método:
  - perímetro F1 y vara del foso P-FOSO;
  - remisiones a la gramática G4/G7;
  - una cita de `coordinacion/cierre_v2/DECISIONES_PARA_EL_USUARIO.md` del 18-nov-2026, posterior al corte.

  No era un dato de la empresa. La edición está declarada en la receta y en la descripción del manifiesto, y el original no se toca.
- **C1 (corrección):** la retirada deja restos de la regla en dos filas y una línea de `datos_v63.md` de Vinci: «s2c_medio / roic_medio_5 (todo el capital: con F1 en el perímetro declarado, solo frente al sector)» y «ROIC 5 años de todo el capital (F18 = C55)». La primera es una instrucción del método («solo frente al sector», es decir, no comparar con r). Además remite a un perímetro declarado que ya no está en el paquete. Ningún otro paquete la lleva.

## 4. Corte temporal

- **Vinci (10-oct-2026):** las fuentes son el URD 2025 y el semestral a 30-jun-2026. No entra nada de los nueve meses (22-oct). Las fechas posteriores al corte que hay en las fuentes son vencimientos o calendarios, no información nueva.
  - Decisiones del inversor de la etapa 1 fechadas el 23-oct (M43, M44, M48): solo usan cifras hasta el 30-jun. Se aceptan con el aviso del autor.
  - Notas de proceso del 18 y 19-nov en `fase1_v63.json`: no traen información de mercado. Se aceptan.
  - **C2 (corrección):** `datos_v63.md` (fila del precio) y `fase1_v63.json` citan «107,32 € el 14-oct-2026 (Tradegate)» como contraste. Es un dato de mercado posterior al corte. Es poco material, pero rompe la regla «nada posterior al 10-oct», y quitarlo es barato.
- **Zoetis T2 (5-nov-2026):** la cotización es un extracto fiel de la transcripción (`4eeff61`, líneas 2, 7, 16–20 y 22). No entran las filas del 6 al 17-nov. El 10-Q del T3, el comunicado y la presentación son del 5-nov. No hay fechas posteriores salvo vencimientos de deuda. Los datos y la etapa 1 son byte a byte los del T1 (`cmp`).

## 5. Criterio de finalistas

- Mecánico, declarado en el código y en el `.md`, y reproducible. Usa solo los resultados de los filtros devueltos por el modelo, que quedan marcados como sin revisar. No usa el veredicto.
- Es coherente con el cribado. Las cuatro finalistas tienen veredicto `estudiar_a_fondo`. El filtro de precio deja fuera a las de calidad alta y precio `no_pasa` (ABB, ASML, Ferrari, Hermès, LVMH, etc.), como manda el criterio.
- Ver la observación O3 sobre las dos empresas con `estudiar_a_fondo` que quedan fuera.

## Correcciones exigidas

- **C1.** En la receta `recetas/vinci.json`, añadir reemplazos declarados que dejen neutras las dos etiquetas de C54/C55: «(todo el capital: con F1 en el perímetro declarado, solo frente al sector)» pasa a «(todo el capital)». Regenerar `datos_v63.md`, la huella del manifiesto y la descripción («y sus remisiones»).
- **C2.** En la misma receta, retirar de las copias de `datos_v63.md` y `fase1_v63.json` la cita «y 107,32 € el 14-oct-2026 (Tradegate)», dejando la del 9-sep. Declararlo en la descripción del manifiesto. Regenerar las huellas, volver a pasar `comprobar` y la prueba sin API, y actualizar la cota y la reserva del README si cambian.

## Observaciones (no bloquean; decide la persona responsable)

- **O1.** Los datos de Vinci y Zoetis llevan decisiones de la persona posteriores a la etapa 1 sobre el tratamiento de los datos (P-O1 (c), P-O2, precedente E1). Esto es coherente con «los mismos datos verificados que el personaje», pero es más que la etapa 1. Conviene que la persona lo confirme de forma explícita para el análisis directo.
- **O2.** Los datos y la etapa 1 de Zoetis T2 siguen con el precio del 8-oct (73,08 USD). Solo la cabecera de la cotización dice que la sustituye 82,11 USD. Además, la transcripción trae 89,2 USD el 4-nov, entre 82,99 y 82,11. Es fiel a la fuente, pero conviene comprobarlo.
- **O3.** Ege_Profil e Italian_Wines tienen veredicto `estudiar_a_fondo`, pero no entran por el criterio (dos «dudoso» en calidad, caja y balance). Es correcto según lo declarado, pero la persona debe saberlo.
- **O4.** Elis sigue bloqueado. Las dos salidas que propone el autor (excepciones con huella en el lanzador, o editar las copias de la etapa 1) requieren decisión y revisión. No se debe desbloquear por otra vía.

## Ronda 2 · `8e9b5da` (commits `cd24039` y `8e9b5da`)

**Veredicto: conforme.** C1 y C2 están corregidas y O2 está atendida. No hay correcciones nuevas. No se integra en `main`: eso exige la frase de la persona responsable.

### Comprobaciones (ejecutadas por el revisor)

- **Límites de seguridad.** `git diff origin/main 8e9b5da` no cambia `.github/`, `direct_analysis.py`, `revalidar.py`, `screening.py`, `excepciones_ceguera.json` ni `automation/coordination/`. `finalistas.py` tampoco cambia. `universo.py` solo añade la lectura de fechas en texto («25-oct-2026»), sin red ni API.
- **C1.** En `datos_v63.md` de Vinci, las etiquetas de C54 y C55 pasan a «(todo el capital)». No queda ninguna mención de «perímetro declarado» ni de «1 bis». La edición está declarada en la receta.
- **C2.** Ya no aparecen «107,32» ni «Tradegate» en `datos_v63.md` ni en `fase1_v63.json` de Vinci.
- **O2 (Zoetis T2).** Las copias de los datos llevan una nota inicial inequívoca:
  - C37 = 82,11 USD del 5-nov-2026;
  - C41 = 34.890,8 mm (comprobado: 82,11 × 424,927535 = 34.890,80);
  - C55 y `fase1_v63.json` se ajustan igual;
  - el resto es del primer tiempo y no se recalcula;
  - la etapa 1 queda sin cambios y rige el precio nuevo.

  La cabecera de la cotización declara que la fila del 4-nov (89,2 USD) no se ha podido contrastar. Suficiente.
- **Recetas.** `preparar_paquete.py comprobar` da `IGUAL` para Vinci y para Zoetis T2, con los assets de `fuentes-examen-20261118` y los clones del auxiliar y del producto.
- **Universo.** `universo.py --escribir` con el asset `universo_etapa1.zip.zip` de la Release `universo-etapa1-20261118` regenera las ocho empresas finalistas sin ninguna diferencia en Git (bytes y manifiestos idénticos).
- **Baterías.** `automation/direct_analysis`: 60 pruebas OK. `automation/screening`: 44 pruebas OK.
- **Prueba sin API.**
  - `vinci`, `zoetis-t2`, `moury`, `spie`, `strabag`, `tupras` y `fw-thorpe` quedan en `PREPARADO_SIN_API`, con 0 mensajes. La ceguera se comprobó con todas las ramas remotas.
  - `elis` sigue rechazado por `SOLAPE_CON_MATERIAL_CIEGO` (O4 sin cambios).
  - Fechas de corte de las nuevas: Moury 31-oct, Spie 7-nov, Strabag 11-oct, Tupras 1-nov.
- **Finalistas.** `finalistas.py` sobre el registro `6fee3d2` con las siete ejecuciones declaradas regenera el `.md` idéntico: 111 empresas, todas utilizables. Las finalistas son FW_Thorpe (nivel 1) y, en nivel 2, Azkoyen, Betsson, CocaCola, Moury, Spie, Strabag y Tupras. Las etapas 1 nuevas no mencionan rúbrica, contradictor ni coordinación.

### Observaciones (no bloquean)

- **O3 (actualizada).** Ege_Profil, Italian_Wines y Omer tienen veredicto `estudiar_a_fondo` y quedan fuera por el criterio. Tupras entra con veredicto `faltan_datos`, porque el criterio no usa el veredicto. Es coherente con lo declarado, pero la persona debe saberlo.
- O1 y O4 siguen como en la ronda 1.
