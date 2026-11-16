# Revisión independiente de las entregas F 223f16d (B-PM1) y 52fb120 (F-B3/F-C1)

- **Revisor:** subagente Claude (Opus 5.5) lanzado por el coordinador. No es autor del material revisado: los autores son Mistral C/F (las dos entregas) y Mistral B (dossier daa7478). **Límite:** el coordinador que me lanza también es Claude y registrará la aceptación. Este informe da hechos reproducibles; no decide la aceptación.
- **Fecha:** 2026-11-16.
- **Objeto:** rama `origin/mistral/f-alcance-real` de `munger-v2-evidencias-mistral`:
  - `223f16d`: `revisiones_b_pm1/`;
  - `52fb120`: `preparacion_b3_c1/`;
  - `868f448`: checkpoint final.
  - Material extraído con `git archive … | tar -x` en `<rev_F>/<commit>/`, sin checkout ni worktree.
- **Reglas aplicadas:** `origin/coordinacion/cierre-v2` @ `704e6bb` (`PROGRAMA.md`, `INTEGRACION.md`, `PROMPT_MISTRAL_C_F.md`, `PLANTILLA_ENTREGA.json`, `CONTROL.json`).
- **Material local:**
  - `<zip>`, con SHA-256 `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e` (comprobado);
  - `<base414>`, el árbol 4.14 materializado.
- **Herramientas:** `python3 -I`, `pdftotext -layout` por página, `unzip`, `sha256sum` y `git show`/`git diff` locales.
- **Lo que no hice:** commit, push, ningún cambio en repositorios, red, LibreOffice ni el pipeline.
- **Sondas:** las sondas y sus salidas están en `<rev_F>/sondas/`; sus huellas, al final.

## Resumen de veredictos

| # | Criterio | Veredicto |
|---|---|---|
| 1a | Las nueve altas PP&E están en su página del PDF, con la huella correcta | **CUMPLE** el dato. La evidencia de F **CUMPLE CON LÍMITES**: no comprobó páginas ni PDF. |
| 1b | «CONFIRMADO» se sostiene | **CUMPLE** |
| 1c | Se conservan el bloqueo P-M1 y la no identificación de θ/λ | **CUMPLE** |
| 2a | Protocolo fijado antes de calcular | **CUMPLE CON LÍMITES** |
| 2b | Selección reproducible y sin precios | Sin precios: **CUMPLE**. Reproducible: **CUMPLE CON LÍMITES**. |
| 2c | Bloqueo de Ahold bien fundado | **CUMPLE** |
| 2d | Ninguna financiera conservada | **CUMPLE** en el ZIP. Para las 116 empresas: **NO OBSERVABLE AQUÍ**, porque la lista no está conservada. |
| 3a | `inventario_desde_zip.py` reproduce `INVENTARIO_Y_HUECOS.csv` | **NO CUMPLE** |
| 3b | `huellas_fuentes_conservadas.csv` (29 PDF) frente al ZIP | **CUMPLE CON LÍMITES** |
| 4a | Contrato C presentado como propuesta | **CUMPLE** |
| 4b | Declara lo que no valida (solvencia, capital regulatorio) | **CUMPLE** |
| 4c | No introduce umbrales ni políticas sin decisión | **CUMPLE CON LÍMITES**. Además hay un defecto material de contenido (D3). |
| 5 | ENTREGA_B_PM1 / ENTREGA_B3_C1 frente a la plantilla | **CUMPLE CON LÍMITES** |
| 6a | Manifiesto `sha256sum -c` | **CUMPLE** |
| 6b | Sin PDF/XLSX/ZIP/caché/secreto en `c7716a0..868f448` | **CUMPLE** |
| 6c | Checkpoint 868f448 y control común | **CUMPLE CON LÍMITES**: F no tocó ningún CONTROL ni ESTADO, pero el punto de recuperación está caducado. |

Reglas del programa:
- Nadie elige R, θ, λ, probabilidades ni umbrales: **CUMPLE**. El mapa lista `r` y las probabilidades como entradas «convención/juicio», sin valor y sin decir quién decide (límite menor).
- No hay contacto con terceros. El `.bat` de Ahold no se ejecutó y solo se consultó GitHub del propio proyecto.
- No se adopta ninguna política.
- La selección no usa precios.

## Defectos encontrados

| Id | Gravedad | Defecto | Contraejemplo / evidencia |
|---|---|---|---|
| **D1** | Material para la trazabilidad del inventario | `INVENTARIO_Y_HUECOS.csv` no lo genera el script publicado. En las 7 filas de «correcciones 4.14», el CSV pone todo en `n_otros` y 0 en xlsx/json/docs/pdf. El script, sobre `<zip>`, sí reparte por tipo. | Fila `elis`: publicado `0,0,0,0,105`; reproducido `6,26,46,14,13`. Ocurre igual con `unzip -l` y con `unzip -Z1` (`sondas/inventario/diff_inv_*.txt`). En `ENTREGA_B3_C1.json`, la prueba 0 declara `exit_observado 0` y como evidencia ese CSV. |
| **D2** | Medio | Inventario incompleto sin declararlo: <br>• el filtro omite `elis_decisiones` (`\w+` captura `elis_decisiones`, que no está en la tupla admitida), el expediente final de Elis que cita la MATRIZ;<br>• no recorre `contrastes/` ni `…/2026-11_Vidrala_ensayo/fuentes`, donde están los PDF de Vidrala;<br>• por eso marca 0 PDF en Vidrala y Viscofan, aunque el propio paquete conserva 29 PDF con huella. | `sondas/inventario/inv_desde_unzip_Z1.csv`: no hay fila `elis_decisiones`. `sondas/sonda3_out.txt`: el ZIP tiene 71 PDF y 42 no llevan huella en el paquete (Elis, 14 distintos × 3 expedientes). |
| **D3** | Material para usar el contrato C | `CONTRATO_C_PROPUESTA.md` y `MAPA_ENTRADAS.jsonl` describen mal las palancas y el puente del motor C del producto (detalle debajo). | `sondas/sonda4_out.txt`. Puente propuesto con E0=1000, beneficio neto 100, impuesto 30 y dividendos 40: da E1=1170 frente a 1060 real, y «otros movimientos» tendría que absorber −110. Si B15 se rellena con un *payout* del 40 %, el motor lo lee como ROE objetivo del 40 %: el valor ilustrativo se multiplica por 2,42. |
| **D4** | Medio | Recuperación caducada. En `PUNTO_DE_RECUPERACION.md` @ 868f448, la «Siguiente acción exacta» sigue siendo «contraste documental dirigido B/P-M1 @ daa7478»: ya se hizo en 223f16d y no se actualizó desde 90329a1. INTEGRACION exige una siguiente acción exacta vigente. | `git show 868f448:resultados_cierre/alcance_real/PUNTO_DE_RECUPERACION.md` |
| **D5** | Menor | Sobredeclaración de estado (detalle debajo). | `ENTREGA_B3_C1.json`, `PUNTO_DE_RECUPERACION.md`, mensaje de 868f448 |
| **D6** | Menor | Horas de `COMANDOS.md` incoherentes con los commits (detalle debajo). Impide fechar el «protocolo antes de calcular» por otra vía que el commit. | `git log --format=%ad` frente a `COMANDOS.md` |
| **D7** | Menor | Comandos no ejecutables tal cual (detalle debajo). | `ENTREGA_*.json` |

**Detalle de D3.** En el producto (`v6/scripts/relacion_entradas_materiales.py`, `V6.1/build_v6.py`, `V6.1/test_fill.py`):
- `Palancas!X14` es el crecimiento de los años 1–5;
- `X15` es el **ROE objetivo** del año 5;
- `X18` es el ROE a largo plazo;
- g∞ está en Análisis B68:D68;
- el ROE de partida es beneficio neto atribuible (Historia L9) ÷ patrimonio neto atribuible de cierre (L21);
- el flujo es B(t−1)·ROE − ΔB;
- el terminal es B10·(ROE_lp − g∞)/(r − g∞).

El contrato y el mapa dicen otra cosa:
- «g∞ del patrimonio (B14), payout (B15)» y «B14/B15 (g, payout)»;
- «ROE = BAI / patrimonio medio»;
- un puente de patrimonio «BAI + OCI **+ dividendos** − recompras…»;
- un valor «patrimonio × múltiplos … (o valor liquidativo)».

Es decir: los dividendos tienen el signo cambiado, se usa el beneficio antes de impuestos y el método de valor no es el del motor. Las diferencias no se declaran.

**Detalle de D5.**
- `ENTREGA_B3_C1.json` incluye en `criterios_cubiertos` «principal y reserva por recorrido» y «datos oficiales … con huecos». En C no hay ninguna entidad nombrada, ni principal ni reserva. En B, la principal está bloqueada y las reservas están dentro de la muestra. No se preparó ningún dato oficial de candidata.
- `PUNTO_DE_RECUPERACION.md` dice «F-B3 / F-C1 HECHOS» y «Cola C_F completa». CONTROL los tiene en `PARCIAL/PENDIENTE`.
- El mensaje de 868f448 junta «CONTROL registra…», que es cierto, con «cola C_F completa», que es una valoración propia de F. Leído deprisa, parece que lo registra CONTROL.

**Detalle de D6.**
- `COMANDOS.md` sitúa B-PM1 en «~22:00–22:20 UTC», pero el commit 223f16d es de las 21:50:14 y `verificacion_fuentes_y_runs.txt`, de las 21:48:58Z.
- Sitúa la Cola 2 en «~22:30 UTC», pero el commit 52fb120 es de las 22:07:15.

**Detalle de D7.**
- En ENTREGA_B3_C1, la prueba 0 encadena `unzip -l … | python3 … /tmp/zip_list.txt` con una tubería sin sentido.
- En ENTREGA_B_PM1, la prueba 0 es una descripción («sha256 de 11 textos … vs unzip -p»), no un comando.
- `extraccion_independiente_pm1.py` lleva una ruta absoluta de `/workspace`. Para reproducirlo hubo que cambiar una línea (`sondas/rerun_extraccion/diff_unica_linea_cambiada.txt`).

## 1. B-PM1 (223f16d)

### 1a. Página, huella y cifra de las nueve altas

**Sonda 1 (`sondas/sonda1_pdf_paginas_ppe.py`, exit 0, `FALLOS: 0`).** Para cada año:
- comprueba el SHA-256 del PDF de Vidrala en `<base414>` frente a `FUENTES_CONSERVADAS.csv` @ daa7478;
- ejecuta `pdftotext -layout -f p -l p` sobre la página que cita `VIDRALA_REPOSICION_CAPACIDAD.csv` @ daa7478;
- exige el título de nota «Property, Plant and Equipment», la cabecera del año con «Additions», la fila total de Coste tras «Work in progress» y el token 2 = alta del dossier;
- exige que el total de intangibles (la lectura antigua errónea) no esté en esa fila;
- exige que la página del texto conservado (`[PDF PAGE N]`) contenga la misma cifra.

| Año | PDF (página) | Fila total de Coste en el PDF (slot 2 = Additions) |
|---|---|---|
| 2017 | 1285_en-2017 (p. 42) | 1,174,690 · **101,154** · 76,170 (combinaciones) · … · 1,306,514 |
| 2018 | 1291_en-2018 (p. 40) | 1,306,514 · **93,148** · … · 1,339,891 |
| 2019 | 1297_en-2019 (p. 41) | 1,339,891 · **108,645** · … · 1,344,347 |
| 2020 | 1304_en-2020 (p. 50) | 1,344,347 · **134,263** · … · 1,442,349 |
| 2021 | 1413_en-2021 (p. 39) | 1,442,349 · **105,877** · … · 1,576.956 (sic, en el PDF) |
| 2022 | 1668_en-2022 (p. 40) | 1,576,956 · **158,234** · … · 1,700,343 |
| 2023 | 1831_en-2023 (p. 43) | 1,700,343 · **134,472** · 262,679 · … · 2,102,446 |
| 2024 | 2145_en-2024 (p. 47) | 2,131,588 · **171,185** · … · 2,088,264 |
| 2025 | 2355_en-2025 (p. 43) | 2,088,264 · **177,848** · … · 2,194,513 |

**Comprobación manual de tres altas (`sondas/sonda2_tres_altas_manual.txt`).** En 2019, 2023 y 2025:
- lectura directa de la página, con el título de la nota y la cabecera `Additions` en la columna 2;
- cuadre aritmético de la fila: apertura + movimientos = cierre, exacto en los tres años.

**Otras comprobaciones:**
- Intangibles 2017, PDF p. 44: `Additions 21 · 3,237 · 2,822 · – · 6 · – · 150,657 · 156,743`. El valor antiguo, 156.743, sale de la nota de intangibles: emisiones 3.237 y goodwill 150.657.
- Comparativo 2023 en CF_2024, PDF p. 48: altas 134,472, iguales; combinación reexpresada 291,821; cierre 2,131,588. Coincide con lo que registran el dossier y F.
- Sonda 8: los 11 textos CF/ES dan en `<zip>` (`unzip -p`) la misma huella que publica F (11/11).
- Sonda 3: los 29 PDF de FUENTES_CONSERVADAS coinciden en bytes y SHA-256 con el ZIP (29/29).

**Reproducción de F:**
- `extraccion_independiente_pm1.py`, cambiando solo la línea de la ruta: exit 0, salida **byte-idéntica** a `extraccion_independiente_out.txt` (`sondas/rerun_extraccion/`).
- `tablas_vidrala.py` del autor @ daa7478, en raíz aislada: exit 0, CSV **byte-idéntico** al publicado y log igual al de F (`sondas/rerun_tablas_vidrala/`).

**Límites de la evidencia de F** (los hechos se sostienen):
- trabajó con textos, no con PDF, porque declara que no tenía poppler;
- no comprobó las páginas citadas (el encargo pedía «páginas/cabeceras»);
- su extractor compara con valores esperados fijados a mano desde el dossier, así que no es una lectura ciega;
- no tiene control negativo propio: se apoya en el del autor;
- la independencia es de sesión, no de familia de modelo, y F lo declara.

Mis sondas cubren las páginas y el negativo.

### 1b. «CONFIRMADO»

Se sostiene en el alcance contrastado:
- nueve altas;
- ocho comparativos;
- localización del error antiguo en la nota de intangibles;
- discrepancia de 2023 registrada sin resolver.

No encuentro contraejemplo.

### 1c. Bloqueo P-M1 y θ/λ

En `CALCULOS_PM1.json` @ daa7478:
- `conclusion_frente_B`: «P-M1 no delimitada … bloqueo»;
- `pendiente`: «θ y λ no identificados … no se elige valor»;
- `theta_desglose_viscofan` es una HIPÓTESIS de perímetro, con θ negativa como diagnóstico condicional;
- `lambda_vidrala` es un «rango condicionado … NO adopta lambda»;
- `politica`: «ninguna adoptada».

F no propone valores y conserva el bloqueo. **CUMPLE.**

## 2. Selección y protocolo (52fb120)

**2a. Protocolo antes de calcular: CUMPLE CON LÍMITES.**
- En el paquete no hay ningún cálculo ni valoración, así que no hay resultado que pudiera haber guiado la elección.
- Pero el protocolo entra en el mismo commit que la selección y las horas de COMANDOS no son fiables (D6), por lo que el orden solo es verificable por ausencia de cálculo.
- Para C no fija criterios operativos: ni tipo de entidad, ni cotización, ni fuente mínima, ni regla para elegir entre candidatas. El texto se queda en «p. ej. entidad con informe anual/SFCR público». Quien elija después podría hacerlo por conveniencia.
- En §3.4 escribe «I18/I20», no «I19/I20» (errata).

**2b. Sin precios: CUMPLE.**
- `SELECCION.csv` no tiene columnas de precio ni de valoración, y el grep no encuentra ninguno en el paquete.

**Reproducible: CUMPLE CON LÍMITES.**
- La selección es una tabla de juicio documental, razonada y con motivos.
- Pero se apoya en un inventario que no se reproduce (D1/D2).
- La elegibilidad de negocio de Ahold («distribución, filial cambiante») no cita fuente.
- La búsqueda de fuente oficial para C que pedía el encargo no se intentó: el límite de red se toma del frente B (401, TLS) y F no registra ningún intento propio.

**2c. Ahold: CUMPLE** (`sondas/sonda9_out.txt`).
- En las 6799 entradas del ZIP, lo único de Ahold es `documentacion_cierre_4_14/descargas_bat/descargar_fuentes_ahold.bat`.
- No hay ningún xlsx de Ahold entre los 843, ni respuesta de la etapa 1, ni PDF, ni extracción.
- `MATRIZ_ALCANCE_4_14.md` y `REGISTRO_ENTREGA_4.14.md` dicen que la persona responsable «no lo ha ejecutado ni ha entregado el Excel de la etapa 1».
- **Matiz que F no registra:** el propio `.bat` dice «La carpeta tiene los informes 2019-2025; para la Historia de 10 años faltan 2016, 2017 y 2018». Esos informes 2019–2025 existirían en el equipo de la persona, fuera del ZIP.

**2d. Financieras: CUMPLE en el ZIP.**
- Ningún nombre de archivo apunta a banco o aseguradora.
- Las empresas con expediente son Aarsleff, Hermès, Nike, Rational, Vidrala, Viscofan y Elis, más los ejemplos ABB y EmpresaX.
- Del motor C solo hay `Fixture_motorC_original.xlsx` y `Fixture_motorC_palancas_A.xlsx`.
- La lista de las 116 empresas de la etapa 1 no está conservada: solo se menciona en 3 archivos. Si alguna de las 116 es financiera es **NO OBSERVABLE AQUÍ**, y F lo registra correctamente como hueco.

## 3. Inventario con huellas

**3a. NO CUMPLE (D1, D2).**
- Ejecuté `python3 -I scripts/inventario_desde_zip.py` sobre `unzip -l <zip>` y sobre `unzip -Z1 <zip>`. En los dos casos salen 13 recursos.
- Las 6 filas de `empresas_v2` coinciden.
- Las 7 de «correcciones 4.14» no coinciden con lo publicado (`sondas/inventario/diff_inv_l.txt`, `diff_inv_Z1.txt`).
- Las filas añadidas a mano (Ahold, financiera, ZIP) y la columna `motor_usado` no salen del script. Por eso «regenera INVENTARIO_Y_HUECOS.csv» es falso.

**3b. CUMPLE CON LÍMITES.**
- Las 29 filas PDF de `huellas_fuentes_conservadas.csv` coinciden en bytes y SHA-256 con el ZIP y con FUENTES_CONSERVADAS @ daa7478 (29/29).
- Límites:
  - es una copia de la lista de B, no un inventario propio;
  - deja sin huella 42 de los 71 PDF del ZIP;
  - la fila de la Release lleva el SHA truncado (`bb51942c`);
  - «6798/6798 verificados … por mi listado»: un listado no verifica contenidos. La verificación es la del hito 2.

## 4. Contrato C propuesto

**4a. CUMPLE.** «Estado: PROPUESTA, no ejecutada, no validado». El contrato no se presenta como decisión.

**4b. CUMPLE.** Cita E62 («NO valida la solvencia ni el capital regulatorio») y advierte que la plantilla no valida el negocio ni permite tratar igual a todos los bancos y aseguradoras.

**4c. CUMPLE CON LÍMITES.**
- No hay umbrales numéricos ni valores de R, probabilidades o palancas para el caso real: los valores de B14/B15/B18 se citan como fixture.
- Pero:
  - propone usar el capital regulatorio como «guarda» sin definirla, lo que exigiría una decisión;
  - propone una base de valor («múltiplos», «valor liquidativo en aseguradoras») que no es la del motor, sin marcarla como cambio de método.

**Defecto material D3:** la descripción del motor está equivocada en palancas, ROE y puente. Con este texto, quien rellene el primer caso C metería el *payout* en la celda del ROE objetivo. Hay que corregirlo antes de usarlo.

## 5. ENTREGA frente a la plantilla — CUMPLE CON LÍMITES

`sondas/sonda7_entregas_vs_plantilla.txt`:
- Las dos ENTREGA tienen todos los campos de la plantilla, sin campos de más.
- Cada prueba lleva comando, código esperado y observado, y resultado. Las no ejecutadas se marcan `NO_EJECUTADO` con motivo.
- Usan `commit_entrega` sin autorreferencia, `integrado_en_producto: false` y `apto_dinero_real: "No se declara…"`.
- No hay ningún «APROBADO» y las dos dicen expresamente que no se autoaprueban.
- Los límites son honestos en lo esencial: misma familia de modelo, sin poppler, parte de Viscofan no ejecutada, bloqueos de Ahold y de C.

Defectos: D1 (exit 0 declarado sobre un CSV que el script no produce), D5 (sobredeclaración) y D7 (comandos descriptivos o no ejecutables).

## 6. Higiene

**6a. CUMPLE.** `sha256sum -c` da 0 en `alcance_real/` @ 223f16d (24 archivos), @ 52fb120 (34) y @ 868f448 (34). El listado del manifiesto coincide con la carpeta (`sondas/sonda5_manifiestos.txt`).

**6b. CUMPLE.** `git diff --name-only c7716a0 868f448` da 19 rutas, todas bajo `resultados_cierre/alcance_real/`. No hay PDF/XLSX/ZIP/pyc/caché/`.trabajo` ni patrones de secreto en las líneas añadidas (`sondas/sonda6_higiene_git.txt`).

**6c. CUMPLE CON LÍMITES.**
- Desde su base `ff0c60c`, la rama F no toca nada fuera de `alcance_real/`.
- `coordinacion/cierre_v2/CONTROL.json`, `ESTADO.md` y `VALIDACION_CONTROL.json` son blobs idénticos en ff0c60c y 868f448.
- Todos los commits de `coordinacion/cierre-v2` posteriores son de Claude.
- «CONTROL registra F1-W/C20/CSV como CONFORME_CON_LIMITES/RESPONDIDA» es una lectura exacta de CONTROL @ 9454b44 (21:52, el último antes de 868f448). No es una escritura.
- Límites:
  - D4 (recuperación caducada);
  - D5 (en el mismo mensaje, «cola C_F completa» es una valoración propia);
  - la rama F arrastra una copia antigua de CONTROL.json heredada de su base. No la modificó, pero quien la lea en esa rama verá un estado viejo.

## Qué bloquea de verdad F-B3 y F-C1 (datos que faltan)

**F-B3 (tercer B fuera de muestra):**
1. El Excel evaluado de la etapa 1 de Ahold Delhaize y su respuesta. Solo puede entregarlo la persona responsable. La etapa 1 no se repite automáticamente (`SELECCION_TERCERA_EMPRESA.md`).
2. Los informes anuales 2016–2018 y el folleto de reexpresión NIIF 16 de 2018, que descargaría el `.bat` si la persona lo ejecuta. Además, los informes 2019–2025 que el `.bat` da por presentes en su carpeta, entregados con bytes y SHA-256. Hoy no hay ningún PDF de Ahold en el ZIP.
3. Si Ahold no llega, otra empresa fuera de muestra. Requiere la lista de las 116 empresas o una nueva preselección de la persona responsable. Hermès y Aarsleff no sirven: están dentro de la muestra.

Después hacen falta el recorrido con agentes reales y una auditoría de otro contexto (Cola 3). Nada de esto lo puede producir F.

**F-C1 (primer C real):**
1. Una entidad financiera concreta (banco o aseguradora) designada por la persona responsable, o identificada en la lista de las 116, que no está conservada.
2. Sus informes oficiales (cuentas anuales, Pilar 3 o SFCR), con bytes y SHA-256. Si existe, también su Excel de la etapa 1.
3. Un contrato C corregido según el motor real (D3): B14 = crecimiento de los años 1–5; B15 = ROE objetivo; B18 = ROE a largo plazo; g∞ en Análisis 68; ROE = beneficio neto atribuible ÷ patrimonio de cierre; puente con los dividendos restando. La «guarda» de capital regulatorio y cualquier base de valor distinta del motor deben quedar como propuestas sujetas a decisión.
4. Un protocolo de selección de C con criterios fijados antes de nombrar candidata.

## Comandos principales (reproducibles)

```bash
# extracción (sin checkout ni worktree)
git -C <repo> archive <commit> resultados_cierre/alcance_real | tar -x -C <rev_F>/<commit>
sha256sum <zip>
# 1a
python3 -I <rev_F>/sondas/sonda1_pdf_paginas_ppe.py <base414> <rev_F>/sondas/FUENTES_CONSERVADAS_daa7478.csv   # exit 0, FALLOS: 0
python3 -I <rev_F>/sondas/rerun_extraccion/extraccion_independiente_pm1_rutalocal.py <base414>/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/vidrala_decisiones/Vidrala/texto   # byte-idéntica
python3 -I <rev_F>/sondas/rerun_tablas_vidrala/raiz/resultados_m2/pm1/scripts/tablas_vidrala.py   # con los textos copiados en raiz/.trabajo/insumos_m2/…; CSV byte-idéntico
# 2c/2d
python3 -I <rev_F>/sondas/sonda9_ahold_y_financieras_en_zip.py <zip>
# 3
unzip -l <zip> > listado_unzip_l.txt; unzip -Z1 <zip> > listado_unzip_Z1.txt
python3 -I <rev_F>/52fb120/…/scripts/inventario_desde_zip.py listado_unzip_Z1.txt inv_desde_unzip_Z1.csv   # difiere del publicado
python3 -I <rev_F>/sondas/sonda3_huellas_vs_zip.py <zip> <rev_F>/52fb120/…/fuentes/huellas_fuentes_conservadas.csv <rev_F>/sondas/FUENTES_CONSERVADAS_daa7478.csv
# 4
python3 -I <rev_F>/sondas/sonda4_contrato_c_vs_motor.py <base414> <rev_F>/52fb120/…/CONTRATO_C_PROPUESTA.md <rev_F>/52fb120/…/MAPA_ENTRADAS.jsonl
# 6
(cd <rev_F>/<commit>/resultados_cierre/alcance_real && sha256sum -c --quiet MANIFIESTO_SHA256.txt)
git diff --name-only c7716a0 868f448; git diff --name-only ff0c60c 868f448
```

*Revisión independiente con límites declarados. No es una aprobación ni acredita aptitud económica. La aceptación la registra el coordinador.*
