# Búsqueda de huellas históricas de los PDF de Ahold Delhaize (etapa 1) · 17-nov-2026

- **Autoría:** subagente Claude (Opus 5.5) del coordinador, por la decisión U2 del 17-nov.
- **Modo:** solo lectura y sin red. Escribí únicamente en `<huellas>/`. No modifiqué ningún repositorio, ZIP ni árbol. No ejecuté nada de lo extraído, ni LibreOffice, ni el pipeline. No rehíce la etapa 1.
- **Lectura del ZIP:** con `unzip -l`/`unzip -p` y con Python `zipfile` en memoria, sin extraer a disco. Los `.xlsx` anidados se leyeron también en memoria. Por eso no hizo falta copiar el ZIP.

**Marcadores**

| Marcador | Ruta |
|---|---|
| `<e_work>` | `<e_work_local>` |
| `<zip>` | `<e_work>/dl_base414/munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip`: 1 130 912 246 B, SHA-256 `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e` (recalculado hoy; coincide con `RECURSOS_EXISTENTES.md`). Tiene 6799 entradas de archivo. |
| `<aux>` | `<huellas>/`: anexos y scripts de esta búsqueda (`zip_menciones_ahold.txt`, `scripts/`) |
| `<B414>` | `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/`, dentro de `<zip>` y de los árboles |

## 1. Resultado principal

**No existe ninguna huella histórica (SHA-256, MD5 ni `HUELLAS.txt`) de ningún PDF de Ahold Delhaize** en el material disponible. Esto incluye los PDF usados en la etapa 1 (28-oct-2026) y cualquier otro de Ahold.

La única huella antigua relacionada con Ahold es la del propio `.bat`: `04feebd409754a91e509dfde1e8dd63a1e8534695d05cb75fffca6a97bd53d88`.
- Está en `<zip>!munger_v2_r1/MANIFIESTO_SHA256.txt:3631`.
- También en `munger_v2_r1/CAMBIOS_ARCHIVOS.txt:3149` y `:6272`.
- La recalculé con `unzip -p … | sha256sum` y es igual.

Esa huella identifica un script, no un PDF.

## 2. Qué se buscó y dónde

| # | Lugar | Método | Resultado |
|---|---|---|---|
| 1 | `<zip>`: 6799 entradas y 844 contenedores anidados (`xlsx`/`zip`) leídos en memoria | Texto `ahold\|delhaize\|koninklijke` en todo el contenido; los 10 SHA-256 y 10 MD5 NUEVOS; los identificadores de URL (`ycfni1cc`, `wsafdah4`, `jr2l1zc2`, `tumbdiev`, `ghbbd455`, `j3tncmcj`, `jqwgchdo`, `bbwfuqw5`, `sedod1fo`, `k0pnhvk5`); `AD_annual`, `restatement-booklet`. Scripts en `<aux>/scripts/` | 12 blobs con mención (anexo `<aux>/zip_menciones_ahold.txt`), todos documentales (§3). **Ningún** PDF de Ahold. **Ninguna** huella de PDF de Ahold. Ningún hash NUEVO aparece en el ZIP. Las coincidencias de `annual-report-20` son de Viscofan y ABB, y una de `ahold` está dentro de un base64 del ESEF de Vidrala: ruido. |
| 2 | `<zip>`: las 45 entradas cuyo nombre contiene `huella`, `sha256` o `md5` (`HUELLAS*`, `*.sha256`, `MANIFIESTO_SHA256*`), listadas con `unzip -l` | Mismo barrido | Ninguno menciona Ahold. Son de Elis, Viscofan y Vidrala o manifiestos de código. |
| 3 | Árboles materializados `<e_work>/wt_main414`, `<e_work>/wt_hito415`, `<e_work>/traspaso_20261117`, `<e_work>/inventario`, `<e_work>/textos_pdf` y el resto de `<e_work>` salvo `u2_ahold` | `grep -rilI`, `find -iname`, `grep -F -f` de los hashes NUEVOS | Las mismas menciones documentales que en el ZIP, copiadas en cada árbol. Ningún `HUELLAS*` de Ahold. Ningún hash NUEVO fuera de `u2_ahold`. |
| 4 | `munger-v2`: 11 ramas remotas (`main`, `revision/4.15-hito1`, `auditoria/*`, `integracion/*`, `claude/*`, `preparacion/*`) | `git grep -i ahold $(git for-each-ref … refs/remotes)`, hashes NUEVOS e identificadores de URL | 21 rutas con mención, todas documentales (el `.bat`, `CONTINUIDAD`, `MATRIZ`, `SELECCION`, `HITO_1`, manifiestos, `baselines/4.14*`, `docs/validacion_economica_paralela/*`). **Ninguna** huella de PDF de Ahold. |
| 5 | `munger-v2-evidencias-mistral`: 26 ramas remotas | Ídem | Menciones en `coordinacion/cierre_v2/*` (`CONTROL`, `ESTADO`, `DECISIONES`, revisiones y sondas), `mistral/f-alcance-real` (inventario F-B3: solo la huella del `.bat`) y `fuentes/ahold-etapa1-20261117` @ `726eea6` (originales de la etapa 1, §4). Los hashes NUEVOS solo aparecen en `coordinacion/cierre_v2/u2_tercer_b/` (la descarga del 17-nov). |
| 6 | Resto del disco: `<home>/{wt,wt_auto1,rev_*,…}`, los scratchpads de `/tmp` y `find /` | `find` de `*ahold*`, `AD_*.pdf`, `*annual-report-20*.pdf` y `*huella*` (355 archivos de huellas, revisados con `grep`) | Solo copias del mismo `.bat`. Los únicos PDF de Ahold son los 10 NUEVOS de `<e_work>/u2_ahold/pdf/`. **Ningún** archivo de huellas menciona Ahold. |

## 3. Registros históricos de Ahold encontrados (ninguno contiene huellas de PDF)

| Fuente exacta | Línea | Qué dice |
|---|---|---|
| `<zip>!<B414>documentacion_cierre_4_14/descargas_bat/descargar_fuentes_ahold.bat` (SHA-256 `04feebd4…d53d88`) | 3–4 | «informes anuales 2016-2018 (14-nov-2026). La carpeta tiene los informes 2019-2025; para la Historia de 10 anos faltan 2016, 2017 y 2018.» |
| ídem | 11 | Destino: la subcarpeta `KONINKLIJKE AHOLD DELHAIZE\descargas_2026` del equipo de la persona responsable. Ruta personal omitida aquí. |
| ídem | 16, 18, 20, 22 | URL de 2016 (`…/ycfni1cc/ahold-delhaize-annual-report-2016.pdf`), 2017 (`…/wsafdah4/annual-report-2017.pdf`), 2018 (`…/jr2l1zc2/annual-report-2018.pdf`) y del folleto NIIF 16 (`www.aholddelhaize.com/media/8952/2018-restatement-booklet-ifrs-16-dated-march-25-2019.pdf`) |
| ídem | 28–32 | `HUELLAS.txt` se genera **solo con `AD_*.pdf` de `descargas_2026`**, es decir, con los 3 informes y el folleto que descarga el `.bat`. **No incluye los informes 2019–2025** de la carpeta madre. |
| `<zip>!<B414>REGISTRO_ENTREGA_4.14.md` | 59 | «el .bat está preparado; la persona responsable no lo ha ejecutado ni ha entregado el Excel de la etapa 1» |
| `<zip>!<B414>documentacion_cierre_4_14/MATRIZ_ALCANCE_4_14.md` | 41 | Ahold: «aún no ha entregado el Excel de la etapa 1 ni ha ejecutado el .bat» |
| `<zip>!munger_v2_r1/CONTINUIDAD.md` | 339 | La persona ejecuta el `.bat` y entrega el Excel; inventario sin repetir la etapa 1 |
| `<zip>!<B414>documentacion_cierre_4_14/{tercera_empresa,hito1}/SELECCION_TERCERA_EMPRESA.md` | 3 | Decisión del 14-nov-2026: Elis primera candidata, Ahold reserva |
| `<zip>!<B414>documentacion_cierre_4_14/hito1/HITO_1.md` | 14, 102 | Ahold de reserva |
| `munger-v2` @ `origin/auditoria/economica-f1`: `docs/validacion_economica_paralela/fuentes_traspaso/CONTINUIDAD_TRASPASO.md` | 78, 155 | Repite que el `.bat` no se ha ejecutado |
| `munger-v2-evidencias-mistral` @ `origin/mistral/f-alcance-real`: `resultados_cierre/alcance_real/preparacion_b3_c1/INVENTARIO_Y_HUECOS.csv` | 134, 137 | `.bat` «conservado… NO ejecutado»; Ahold «sin conservar» |

**Conclusión de los registros.** Hasta la entrega 4.14 (14-nov) consta que el `.bat` **no se ejecutó**. Por tanto, al menos hasta esa fecha no existía ningún `HUELLAS.txt` generado por él. Y, aunque exista ahora, solo cubriría 2016–2018 y el folleto, no los PDF 2019–2025 que usó la etapa 1.

> **Observación para el control.** `coordinacion/cierre_v2/CONTROL.json:545` y `ESTADO.md:55` (rama `coordinacion/cierre-v2`) piden las «huellas de sus PDF 2019–2025 (HUELLAS.txt del .bat)». Según las líneas 28–32 del `.bat`, ese `HUELLAS.txt` **no puede contener** 2019–2025. Para esos años hace falta un `certutil -hashfile <pdf> SHA256` sobre los archivos de la carpeta madre `KONINKLIJKE AHOLD DELHAIZE`.

## 4. Originales de la etapa 1 aportados hoy (no son huellas de PDF, pero informan de las fuentes)

Rama `munger-v2-evidencias-mistral` `origin/fuentes/ahold-etapa1-20261117` @ `726eea6b6ae9b3388fa99ca6be6438259e10c1d7`, carpeta `fuentes_usuario/ahold_etapa1/`. Comprobé los blobs con `git show … | sha256sum`.

| Archivo | Bytes | SHA-256 |
|---|---|---|
| `Ahold_evaluada.xlsx` | 69 210 | `c4e5c82e7391300bc7bc591cd9e5996c7c9cb88113283231f93b1ad8a038a293` |
| `Ahold_respuesta.md` | 49 066 | `bb7597fa4e967e11eb70402c906a85440c5942b0cdc5c40b0e92c5cbc15aa013` |

**Contenido relativo a las fuentes.** No contienen ninguna huella ni ningún nombre de archivo PDF. Lo que sí dicen:
- **Hoja «Control maestro»:**
  - `L5` = 46320, es decir, «Última revisión de fuentes» 2026-10-25.
  - `J17:J19`: «Informe anual 2025 (Annual Report 2025, interactive) y Financial statements 2025».
  - `K17`: `https://www.aholddelhaize.com/investors/annual-reports/`, la página índice y no la URL del PDF.
  - `L35`: «FS25 p5 y p27 (impresas 213/235)».
  - `L47`: «FS25 p51 (impresa 259)».
  - `J29`, `J34`, `J37`, `J40`, `J42` y `M56`: `pkg_OPS`, `pkg_BAL`, `pkg_FIN`, `pkg_VAL` y `pkg_CAP`.
  - `J31`, `J33`, `J55` y `J73`: «Informes anuales 2021–2025 / 2020–25 / 2019–25».
  - `J50:J52`: «Informe Q2 2026».
  - Cuatro celdas más: `K38` (beursgenoten), `K39` (Simply Wall St), `K41` (newsroom, 20-oct-2026) y `K75` (registro AFM).
- **`Ahold_respuesta.md`:** cita por año y página AR2020, AR2021, AR2022, AR2023, AR2024, AR2025 y Q2-2026. Por ejemplo, `[AR2025 p. 12, 58]`, `[AR2020 p. 99]`, `[AR2021 p. 191; AR2023 p. 212]` y `[Q2-2026 p. 2-9]`.
- **Metadatos del xlsx (solo observación):** `created` 2026-10-06T08:06:44Z y `modified` 2026-10-28T11:51:57Z.

## 5. Huellas NUEVAS del 17-nov (no prueban el origen)

Fuente: `<e_work>/u2_ahold/SHA256SUMS_pdf.txt`, idéntico a `coordinacion/cierre_v2/u2_tercer_b/SHA256SUMS_pdf.txt` (comprobado con `diff`).
- Hoy pasan `sha256sum -c`: 10/10.
- Los MD5 los calculé hoy sobre los mismos bytes. Son NUEVOS y sirven solo para buscarlos en registros antiguos; no se encontraron.

| Doc. | Archivo NUEVO | SHA-256 NUEVO | MD5 NUEVO | Huella histórica | Comparación |
|---|---|---|---|---|---|
| AR 2016 | `AD_annual-report-2016.pdf` | `1971488fd5c0b2411e4be6311eb1434b79857bc25018b1eccd18e97f63aa5f69` | `37dad4e219f16134ae91f9e2e8cf02cb` | ninguna | **SIN_HISTÓRICA** |
| AR 2017 | `AD_annual-report-2017.pdf` | `c6453a9cd486b914fe5a0979b2f392551d90d00a88b850daf97bb82bb7918e11` | `8f6f24ed0aba1a4c055a5a1acae7dde4` | ninguna | **SIN_HISTÓRICA** |
| AR 2018 | `AD_annual-report-2018.pdf` | `1166874b7e7271382d9ef4c65ef5b72747ee2b67a8b73a3843b96c829f3d58f2` | `cd58a0bdbd77eda07a9f215aa9202f82` | ninguna | **SIN_HISTÓRICA** |
| AR 2019 | `AD_annual-report-2019.pdf` | `0cf336d20c10d2f13460662a0e1285a52b5b64fdad6c29becff58813049be31a` | `97aba2825250dd78a94477d43814a389` | ninguna | **SIN_HISTÓRICA** |
| AR 2020 | `AD_annual-report-2020.pdf` | `7488a11679813708833c789e05c61a7e45d60d62916613aa0cb8d86ee0e24610` | `ce1da4e5c0207a793e1a3ed1a3d2a87b` | ninguna | **SIN_HISTÓRICA** |
| AR 2021 | `AD_annual-report-2021.pdf` | `96f7b7b01b8d6dc2cd96d79120b01a6cb3b88f46caadf59fc65199dd987540bb` | `e537b0f1bb1bcab68cabdd5cb4e1753d` | ninguna | **SIN_HISTÓRICA** |
| AR 2022 | `AD_annual-report-2022.pdf` | `20506e23a1007d0221733a37a51d9d8f66128a58ff18a4ef160a6fdc77ece40a` | `263f3fcb63789bdee0a9061f6488033e` | ninguna | **SIN_HISTÓRICA** |
| AR 2023 | `AD_annual-report-2023.pdf` | `418802abb4f55eab0e019214ecdbdbaa6146409b442fa721653ae1b0bd169106` | `7d43de109eb352efab50b6dbc5351516` | ninguna | **SIN_HISTÓRICA** |
| AR 2024 | `AD_annual-report-2024.pdf` | `eb5cbebf6b2635219883a8d2620c9e77bf42ef0e25653ee8c347963e4cb32b13` | `020d4176d185bc05406f038829c01dff` | ninguna | **SIN_HISTÓRICA** |
| AR 2025 | `AD_annual-report-2025.pdf` (interactivo) | `11a2faee6b25677b14e9f3eee071d44d5e1483fe8ac3fd4e6cef64a22c47967a` | `5d6a83846043586c36d8a29bcabc7882` | ninguna | **SIN_HISTÓRICA** |
| Folleto NIIF 16 de 2018 | (no descargado: HTTP 404) | — | — | ninguna | **SIN_HISTÓRICA** (y sin NUEVA) |

**Recuento:** IGUAL 0 · DISTINTA 0 · SIN_HISTÓRICA 11.

**Documentos que la etapa 1 cita y que no tienen ni huella histórica ni NUEVA:**
- «Financial statements 2025» (FS25);
- el informe Q2 2026;
- los `pkg_*`;
- el informe Q2 2025, que la etapa 1 declara no encontrado (`Control maestro!N34`);
- las fuentes secundarias web.

## 6. Indicios de edición (no son huellas ni verificación de entradas)

Contrasté una muestra de citas de la etapa 1 con el texto `pdftotext` de los PDF NUEVOS (`<e_work>/u2_ahold/texto/`, script `<aux>/scripts/pagecheck.py`). Es una comprobación de coherencia, no una prueba de identidad de bytes.

| Cita de la etapa 1 | En el PDF NUEVO | Lectura |
|---|---|---|
| AR2025 p. 12 y 58: 9.551 tiendas | «9,551» en PDF p. 12 y 58 | Coincide (numeración de página PDF, no impresa: la PDF p. 12 lleva impreso 11) |
| AR2025 p. 43 y 50: cuota de mercado | «market share» en p. 43 y 50 | Coincide |
| AR2025 p. 54–55: BBB+/Baa1, covenant 5,5 | «Baa1» y «5.5» en p. 55, no en la 54 | Coincide en el rango |
| AR2025 p. 69 y 76: *agentic*/IA | «agentic» en p. 69; IA en p. 76 | Coincide |
| AR2025 p. 270–271: pagos en acciones | «share-based» en p. 270 y 271 | Coincide |
| FS25 p5 / p27 / p51 «(impresas 213/235/259)» | En el AR 2025 interactivo NUEVO, las impresas 213, 235 y 259 son las PDF p. 214 (balance consolidado), 236 (nota 14, activos intangibles y fondo de comercio) y 260 (nota 28, «Cash flow continued», con «interest paid»). La sección «financial statements and sustainability» empieza en la impresa 209. | Coherente con un PDF separado de estados financieros que empieza en la impresa 209. `<e_work>/u2_ahold/html/ar_2025.html` enlaza `…/xiknotj4/financial-statements-and-sustainability-notes.pdf`, **no descargado** y sin huella. |
| AR2022 p. 13: «magnitude of inflation» | p. 13 | Coincide |
| AR2023 p. 13–14: «relatively consistent» | p. 14 | Coincide en el rango |
| AR2024 p. 43–44: Stop & Shop | p. 43 y 44 | Coincide |
| AR2021 p. 191 y AR2023 p. 212: FreshDirect | p. 191 y p. 212 | Coincide |
| **`Control maestro!L17`: «p. 210 (Share performance)»** | «Share performance» solo en la PDF p. **61**. La p. 210 es la portada de la sección de estados financieros. | **No coincide**: otra edición, otro documento o error de cita. Sin resolver. |
| `[AR2023 p. 13-14; AR2021 p. 7; AR2022 p. 13]` (sub-OPV de bol.com, línea 35 de la respuesta) | La OPV de bol.com aparece en las p. 6 y 8 del AR2021 NUEVO, no en la 7 | Ambiguo: la cita agrupa varias afirmaciones |

**Lectura (interpretación).** La mayoría de las citas casan con la paginación PDF de los informes NUEVOS 2021–2025. Esto es compatible con que la etapa 1 usara las mismas ediciones, pero **no lo demuestra**: otra copia con otros bytes y la misma paginación daría el mismo resultado. Hay una discrepancia (`L17`).

## 7. Correspondencia histórica que queda sin verificar

1. **Qué PDF concretos usó la etapa 1.** No hay nombres de archivo ni huellas en el Excel ni en la respuesta. Solo constan etiquetas (`AR2020`…`AR2025`, `FS25`, `Q2-26`, `pkg_*`) y la URL índice `…/investors/annual-reports/`.
2. **Identidad de bytes de los informes 2019–2025** de la carpeta `KONINKLIJKE AHOLD DELHAIZE` con los NUEVOS. Solo la puede dar la persona con `certutil -hashfile <archivo> SHA256` sobre esos archivos. **El `HUELLAS.txt` del `.bat` no los cubre** (§3).
3. **Edición del AR 2025.** El Excel dice «interactive», igual que el NUEVO (`ad-annual-report-2025-interactive.pdf`). Pero `L17` (p. 210, «Share performance») no casa. Además, en el sitio hay ediciones por capítulos (strategic report, performance review, corporate governance, financial statements). No está verificado que la copia de la etapa 1 sea la misma.
4. **FS25 («Financial statements 2025»).** Es probablemente un PDF separado, con paginación que empieza en la impresa 209. No se ha descargado y no tiene huella. No está verificado cuál fue.
5. **Q2 2026** (citado de p. 2 a p. 29), **Q2 2025** (declarado no encontrado) y **`pkg_OPS/BAL/FIN/VAL/CAP`**: no se sabe qué son (¿paquetes de datos de la fase 1, hojas de cálculo de IR?). No hay ni copia ni huella.
6. **2016–2018.**
   - Según el `.bat` (línea 4), no estaban en la carpeta al preparar el `.bat` el 14-nov, que es posterior a la etapa 1 del 28-oct. Por tanto, probablemente no se usaron como PDF en la etapa 1. Aun así, la respuesta cita una serie de ventas 2016–2025, de origen no verificado (¿resumen plurianual?).
   - Las URL del `.bat` para 2016, 2017 y 2018 **son las mismas** que las de la descarga NUEVA (`descargas.tsv`). El folleto NIIF 16 da 404 hoy.
   - No consta que el `.bat` se haya ejecutado. Si se ejecutó después del 14-nov, su `HUELLAS.txt` sería posterior a la etapa 1 y tampoco acreditaría el origen.
7. **Año y ejercicio:** sin verificar que «AR2020» de la etapa 1 sea el informe del ejercicio cerrado el 3-ene-2021, de 53 semanas, y no otro documento del mismo año.
8. **Originales del Excel y de la respuesta:** sin verificar que los bytes de `726eea6` coincidan con la copia del disco de la persona (ya consta en su `LEEME.md`).

## 8. Qué permitiría cerrarlo (sin rehacer la etapa 1)

- **Lo mínimo:** la persona ejecuta `certutil -hashfile "<archivo>" SHA256` sobre cada PDF de su carpeta `KONINKLIJKE AHOLD DELHAIZE` (2019–2025, y FS25, Q2-2026 o los `pkg_*` si están allí) y entrega la salida. Comparar con §5 da IGUAL o DISTINTA por documento.
- **Si alguna es DISTINTA:** el archivo de la persona es el único que casa con las citas. Se conserva ese y no el NUEVO.
- **Si no conserva los archivos:** la correspondencia queda **no verificable**. Los indicios de §6 sirven solo como coherencia y se mantiene el rótulo NUEVAS.

## Resumen

1. No hay ninguna huella histórica de PDF de Ahold en `<zip>`, en los árboles 4.14 y 4.15, en `munger-v2` (11 ramas), en `munger-v2-evidencias-mistral` (26 ramas) ni en el disco.
2. La única huella antigua es la del `.bat` (`04feebd4…d53d88`), y es de un script.
3. Comparación: IGUAL 0, DISTINTA 0, SIN_HISTÓRICA 11 (diez informes 2016–2025 y el folleto en 404).
4. Los registros 4.14 dicen que el `.bat` no se ejecutó hasta el 14-nov.
5. Aunque exista, su `HUELLAS.txt` solo cubriría 2016–2018 y el folleto, no los PDF 2019–2025 de la etapa 1. `CONTROL.json:545` y `ESTADO.md:55` deberían corregirse.
6. Los originales de `726eea6` no tienen huellas ni nombres de PDF. Citan AR2020–25, FS25, Q2-26 y `pkg_*`, y la URL índice del sitio.
7. Indicio: la mayoría de las citas casan con la paginación de los PDF NUEVOS. `Control maestro!L17` (p. 210, «Share performance») no casa.
8. FS25 parece un PDF separado (empieza en la impresa 209). Ni FS25, ni Q2-26, ni los `pkg_*` tienen copia ni huella.
9. Las URL 2016–2018 del `.bat` son las mismas que las de la descarga NUEVA.
10. Para cerrarlo hace falta un `certutil` de la persona sobre su carpeta. Sin él, la correspondencia queda no verificable y las huellas siguen rotuladas como NUEVAS.
