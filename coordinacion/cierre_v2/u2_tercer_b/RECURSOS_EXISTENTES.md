# U2 · Recursos existentes para el tercer caso B fuera de muestra (17-nov-2026)

- **Autor:** subagente Claude (Opus 5.5) del coordinador.
- **Qué hice:**
  - leí el material local;
  - descargué fuentes públicas del sitio oficial del emisor.
- **Qué no hice:**
  - ningún commit, push ni cambio en los repositorios;
  - no ejecuté LibreOffice ni el pipeline;
  - no contacté con nadie;
  - no fijé parámetros económicos;
  - no consulté precios.
- **Separación de contenido:**
  - **Hechos:** lo que tiene ruta y huella.
  - **Interpretaciones:** van marcadas.

## 1. Material leído (puntos de lectura)

| Recurso | Ruta / referencia | SHA-256 |
|---|---|---|
| ZIP base-4.14 | `<e_work>/dl_base414/munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip` (Release `base-4.14`) | `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e` (recalculado hoy) |
| Árbol 4.14 materializado | `<e_work>/wt_main414/munger_v2_r1` | — (manifiesto `MANIFIESTO_SHA256.txt` del propio árbol) |
| Paquete F-B3 de Mistral C/F | `munger-v2-evidencias-mistral`, `52fb1206cace5cc56112e5fd1c54773e5185e8e6`, `resultados_cierre/alcance_real/preparacion_b3_c1/` | ver §4 |
| Revisión del coordinador | `origin/coordinacion/cierre-v2`. Leída en `57b34a6`; los dos archivos no cambian hasta `6662170` | ver §4 |
| Guía del producto | `<home>/wt/candidata/munger_v2_r1/personaje_v2/GUIA_RECORRIDO_SUPERVISADO.md`, `PROMPT_CLAUDE_CODE.md` §2, `scripts/pipeline.py`, `scripts/volcar_datos_v63.py`, `prompts/fase_a.md` | — |

## 2. Ahold Delhaize: qué existe hoy

### 2.1 En el ZIP y en el árbol 4.14

| Recurso | Ruta (relativa a `munger_v2_r1/`) | SHA-256 | Qué dice |
|---|---|---|---|
| `.bat` de descarga | `personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/documentacion_cierre_4_14/descargas_bat/descargar_fuentes_ahold.bat` | `04feebd409754a91e509dfde1e8dd63a1e8534695d05cb75fffca6a97bd53d88` (= manifiesto) | Descarga 2016, 2017, 2018 y el folleto NIIF 16 de 2018 en la carpeta `KONINKLIJKE AHOLD DELHAIZE\descargas_2026` del equipo de la persona responsable. Dice: «La carpeta tiene los informes 2019-2025». |
| Registro de la selección | `…/documentacion_cierre_4_14/tercera_empresa/SELECCION_TERCERA_EMPRESA.md` (idéntico en `hito1/`) | `d8b9464d2a8e408ecfabc25b13a24586d6c8a64d08309c341c358ae504ffd9b7` | Decisión del 14-nov-2026, 10:36: «de las 116 empresas analizadas en la etapa 1», Elis es la primera candidata y Ahold la reserva. Se eligió «por las características del negocio y la disponibilidad de un expediente existente, antes de examinar su valoración». Fija seis reglas. |
| Matriz del alcance | `…/documentacion_cierre_4_14/MATRIZ_ALCANCE_4_14.md` | `f7bb3e99b1a7fb05cbc330faa2e143c7e70375e9389a421542b551b1ab507914` | §3: Ahold sin Excel de la etapa 1 y sin ejecutar el `.bat`. §8: Elis salió por el motor A. |
| Registro de la entrega 4.14 | `…/2026-11_Vidrala_ensayo_4_14/REGISTRO_ENTREGA_4.14.md` | `af6c11c2382437f9521c88f8a677b1b299356b3b4f3c2f9310cd4810fd64b16a` | Línea 59: «el .bat está preparado; la persona responsable no lo ha ejecutado ni ha entregado el Excel de la etapa 1». |
| Continuidad | `CONTINUIDAD.md` | `dc8edfc18dc985ec5bc62056a9b9bbb4aa63e44a837e5d4e2547c932423ceb62` | Línea 339: la persona ejecuta el `.bat` y entrega el Excel; después, inventario sin repetir la etapa 1. |

**Comprobado, nada más de Ahold:**
- `unzip -l` del ZIP: 7467 líneas; la única ruta que contiene `ahold` o `delhaize` es el `.bat`.
- `find / -iname '*ahold*'` solo encuentra copias del mismo `.bat` en otros árboles de trabajo.
- Una búsqueda de texto en `<home>` y en el scratchpad solo encuentra menciones en documentos.
- Las 22 ramas remotas de `munger-v2-evidencias-mistral`: solo `sonda9_ahold_y_financieras_en_zip.py`.
- Releases de `munger-v2` (`base-4.14`) y de `munger-v2-evidencias-mistral` (`fuentes-elis-e-20261117`, `fuentes-mistral-m2-20261116`): ningún archivo de Ahold.

**Resultado:** no hay ningún Excel, respuesta, PDF, texto ni extracción de Ahold conservados. Esto confirma la sonda 9 de la revisión.

### 2.2 Descargado hoy (público, fuera de Git)

En `<e_work>/u2_ahold/` están:
- los diez informes anuales completos, de 2016 a 2025;
- el índice `INDICE_FUENTES.csv` (copia en este directorio);
- `SHA256SUMS_pdf.txt`;
- los textos con `pdftotext -layout` en `texto/`;
- las páginas HTML oficiales usadas para localizar los enlaces, en `html/`.

Detalle y estado en `PROPUESTA_TERCER_B.md` §6 y en el índice. Resumen:

| Archivo | Bytes | SHA-256 | Págs. |
|---|---|---|---|
| AD_annual-report-2016.pdf | 12328415 | `1971488fd5c0b2411e4be6311eb1434b79857bc25018b1eccd18e97f63aa5f69` | 251 |
| AD_annual-report-2017.pdf | 48981559 | `c6453a9cd486b914fe5a0979b2f392551d90d00a88b850daf97bb82bb7918e11` | 285 |
| AD_annual-report-2018.pdf | 10705670 | `1166874b7e7271382d9ef4c65ef5b72747ee2b67a8b73a3843b96c829f3d58f2` | 241 |
| AD_annual-report-2019.pdf | 12426820 | `0cf336d20c10d2f13460662a0e1285a52b5b64fdad6c29becff58813049be31a` | 219 |
| AD_annual-report-2020.pdf | 16151687 | `7488a11679813708833c789e05c61a7e45d60d62916613aa0cb8d86ee0e24610` | 253 |
| AD_annual-report-2021.pdf | 15864835 | `96f7b7b01b8d6dc2cd96d79120b01a6cb3b88f46caadf59fc65199dd987540bb` | 290 |
| AD_annual-report-2022.pdf | 10829225 | `20506e23a1007d0221733a37a51d9d8f66128a58ff18a4ef160a6fdc77ece40a` | 317 |
| AD_annual-report-2023.pdf | 63256896 | `418802abb4f55eab0e019214ecdbdbaa6146409b442fa721653ae1b0bd169106` | 340 |
| AD_annual-report-2024.pdf | 47722143 | `eb5cbebf6b2635219883a8d2620c9e77bf42ef0e25653ee8c347963e4cb32b13` | 382 |
| AD_annual-report-2025.pdf | 17713203 | `11a2faee6b25677b14e9f3eee071d44d5e1483fe8ac3fd4e6cef64a22c47967a` | 365 |
| Folleto NIIF 16 de 2018 (URL del `.bat`) | — | — | **HTTP 404**: no descargado |

**El folleto no se pierde en sustancia.** La nota 36 del informe 2019 (PDF pp. 188–192) reexpresa 2018 y el 1-ene-2018 por la NIIF 16. Además, declara las dos reclasificaciones en que difiere del folleto del 25-mar-2019 (PDF p. 190, notas 1 y 2): 81 + 17 M€ en activo corriente y 12 M€ en pasivo corriente.

**Las URL de 2016, 2017 y 2018 son las mismas del `.bat`.** Si la persona ejecuta el `.bat`, obtendrá los mismos bytes. En 2018 lo he comprobado con `content-length` = 10705670.

## 3. Los demás posibles casos fuera de muestra

| Caso | Qué hay | ¿Fuera de muestra? | Sirve como tercer B |
|---|---|---|---|
| Elis | Expediente completo de 4.14 (`elis/`, `elis_motor_A/`, `elis_decisiones/`); etapa 1 original `Elis_evaluada.xlsx` `b775e6b061b752cc531d72d82ba84a803fb0bfe3431c17b70bad7dbd5b43151b`; `Elis_respuesta.md` `999c42d452ec42aa861bc15e9e8e893980bb5b247417697d3be0a2871599c9fe`; 14 PDF propios; Release de 11 PDF | Ya usado como tercera empresa | **No.** La fase A eligió el motor A, con cierre `no_entregable · límite del modelo`. Forzar el B está prohibido. |
| Hermès, Aarsleff, Nike, Rational | `personaje_v2/empresas_v2/<E>/` con etapa 1 y libros V6.3 (motor A) | No: están dentro de la muestra | No. Solo como control de variabilidad. |
| Vidrala y Viscofan | Expedientes B de 4.14 (`vidrala_decisiones/`, `viscofan_decisiones/`). Etapa 1: `Vidrala_evaluada.xlsx` `05111669…fef5`, `Vidrala_respuesta.md` `e080936a…7a79c`, `Viscofan_evaluada.xlsx` `8e0d1ce7…96dffa`, `Viscofan_respuesta.md` `a19a8870…2d847e` | No: son los dos casos B | No |
| Meliá, Gestamp | Solo el nombre (`SELECCION_TERCERA_EMPRESA.md` línea 5: propuesta del frente C de «empezar desde cero», **descartada por la persona responsable**) | Sí | No hay etapa 1. Reabrirlo contradice la decisión del 14-nov. |
| Las otras ≈113 empresas de la etapa 1 | **Nada conservado.** La lista solo se cita (`SELECCION…md:3`, `REQUISITO_VERIFICACION_ENTRADAS.txt:13`) | Probablemente sí | No observable desde aquí |
| Financieras (para C, no para B) | Solo los dos fixtures sintéticos | — | No aplica a B |

**Modelos de «qué entra en la etapa 1»** (sirven para preparar el expediente de Ahold, no son datos suyos):
- `vidrala_decisiones/Vidrala/etapa1/` (V5.3 evaluada, respuesta y `cambios_v2.md`);
- `viscofan_decisiones/Viscofan/etapa1/`;
- `elis/Elis/etapa1/`;
- el inventario `tercera_empresa/INVENTARIO_ELIS.md` (`97ad216220817c34cafff0a7c61fe65d14f9bddeff8cf28a0a231fccf5065634`).

## 4. Estado del paquete F-B3 y de su revisión

| Archivo @ `52fb120` | SHA-256 del blob |
|---|---|
| `SELECCION.csv` | `d4b58b61a7fcead3e9c19601bf2aaec7340fe77aafb892b5f7cfcc1e5b6148fd` |
| `PROTOCOLO_CONGELADO.md` | `a1c5734503984ad501a7cab1c5527f584833467ab00091de3ec2b6960565aa39` |
| `INVENTARIO_Y_HUECOS.csv` | `1f15efcb0fbdbfdb6291835e2b1c05e28a81d2aea1a441f89e6d21873d2c45b0` |
| `MAPA_ENTRADAS.jsonl` | `1e793bb0270725cdd18262b613b515e184f3de2242acc45a61e223ae72a85358` |
| `REVISION_F_223f16d_52fb120.md` (coordinación) | `666673150c9935348c7a594f889374545eebd40a9152c1d82eb38bc4d9d01031` |
| `CORRECCION_F2.md` (coordinación) | `80c5c16600e30eaeedede2ac33abc4b24aa376363ab5485a4bdce29c1c1552fe` |

Lo que se mantiene del paquete y lo que cambia:
- **Se mantiene:**
  - Ahold es la principal condicionada;
  - Hermès y Aarsleff no sirven como principal;
  - Elis queda excluida;
  - ningún precio interviene en la selección.
- **Cambia con lo de hoy:**
  1. «sin .bat»: falso, el `.bat` existe (la revisión 2c ya lo matizó);
  2. «sin PDF/fuentes conservados»: hoy hay diez informes oficiales con huella, pendientes de una preservación duradera;
  3. la elegibilidad de negocio «filial cambiante» seguía sin fuente. Los hechos de financiación con página que cito en `PROPUESTA_TERCER_B.md` §5 la describen, pero no deciden el motor.
- **Sigue pendiente de Mistral:** los defectos F2-D1, D2 y D4–D7 del inventario. No afectan a este documento.

## 5. Qué es historia irrecuperable y qué es público

### 5.1 Solo la persona responsable puede darlo

| # | Qué | Por qué no se reconstruye | ¿Imprescindible? |
|---|---|---|---|
| H1 | `Ahold_evaluada.xlsx` (V5.3 evaluada de la etapa 1), tal como lo produjo, con bytes y SHA-256 | El pipeline se para sin él en el paso 1 (`pipeline.py:636-638`: «falta etapa1/<E>_evaluada.xlsx (V5.3 decidida por el v1, D2)», S-1). Contiene sus decisiones fechadas: las 37 celdas del v1, el motor heredado C62, la **r heredada C56**, que la fase A «no cambia» (`prompts/fase_a.md:13`; `personaje_munger_v2.md:155`: «la r viene heredada de la etapa 1 (o de la configuración)»), y el Control maestro con su evidencia de la fase 1 a esa fecha. Rehacerlo hoy sería otra etapa 1, con otra fecha y otro juicio. Obligaría además a fijar r, que es un parámetro económico. La regla 1 de la selección prohíbe repetirla automáticamente. | **Sí** |
| H2 | `Ahold_respuesta.md` de la etapa 1, más `juicio.json`, `extracto.md` o un archivo de cambios (como `Vidrala_cambios_v2.md`) si existen | Es la herencia que `volcar_datos_v63.py:55-73` vuelca en la sección 6 de `datos_v63.md`: cubo, precio de Sí v1, seis preguntas y qué le haría cambiar. `PROMPT_CLAUDE_CODE.md` §2 la exige junto con el Excel. | **Sí** (la respuesta); lo demás, si existe |
| H3 | Huellas SHA-256 de los PDF 2019–2025 de su carpeta `KONINKLIJKE AHOLD DELHAIZE` (basta `certutil` o el `HUELLAS.txt` que genera el `.bat`). Si alguna no coincide con §2.2, el archivo. | La etapa 1 cita páginas de **sus** ediciones. Si coinciden con las oficiales de hoy, no hace falta nada más. Si son otra edición, sus copias son las únicas que casan con esas citas. | Solo las huellas |
| H4 | Una línea: ¿el cubo o el precio de Sí de la etapa 1 de Ahold influyeron en que fuera la reserva? | El registro dice «antes de examinar su valoración», pero la respuesta de la etapa 1 ya lleva un juicio de precio. La limpieza de la selección «fuera de muestra» solo la puede afirmar ella. | Recomendable; no bloquea |

**La lista de las 116 no es imprescindible.**
- Mientras Ahold siga siendo la candidata, no se necesita.
- Si Ahold no llegara o la persona prefiriera otra empresa, bastaría con **el nombre de una empresa de las 116 y su etapa 1** (H1 y H2 de esa empresa).
- La lista completa solo sería imprescindible si la persona quisiera que la elección entre las 116 la hiciera el programa con un protocolo congelado, en vez de designarla ella.

### 5.2 Público y recopilable por nosotros

| Qué | Estado |
|---|---|
| Informes anuales 2016–2025 (sitio oficial) | **Descargados**, 10/10, con huella (§2.2) |
| Reexpresión NIIF 16 de 2018 | Folleto en 404. **Sustituido** por la nota 36 del informe 2019, descargado |
| Paquetes ESEF 2023–2025 (versión legal en XHTML) | Localizados en las páginas oficiales (`aholddelhaize-2023-12-31-en.zip`, `esef-package-annual-report-2024.zip`, `aholddelhaize-2025-12-28-en.zip`); no descargados (40–84 MB; no los pide el producto) |
| Informe anual 2015 de Ahold y de Delhaize (antes de la fusión) | Localizados (`/investors/annual-reports/2015/`); no descargados (fuera de la Historia 2016–2025) |
| Páginas oficiales de recompras 2016–2026 | Localizadas (`/investors/share-buyback-programs/<año>/`); índice guardado en `html/sbb.html` |
| Documentos de 2026 (resultados del 1T al 3T y hechos posteriores a la base) | Se piden **después** del inventario de la etapa 1, solo los materiales (regla 4). Los comunicados están en `newsroom.aholddelhaize.com`, un host que no está permitido en este entorno. |
| Precio, acciones y tipo sin riesgo a la fecha de análisis | Se recopilan en la fase 1 (`fase1_metadatos.json`), con su fecha. **No se han consultado:** no intervienen en la selección. |

## 6. Cambio de entorno hecho en esta tarea

- El proxy rechazaba `www.aholddelhaize.com` y `media.aholddelhaize.com` (`connect_rejected`). La web redirige además al dominio raíz.
- Con la aprobación de la persona en el aviso del sistema, añadí `www.aholddelhaize.com`, `media.aholddelhaize.com` y `aholddelhaize.com` a la lista de hosts permitidos del entorno personal «munger-v2 (fuentes Elis)». Es el mismo precedente que `fr.elis.com`.
- No se tocó nada más.
- **Preservación:** la descarga está en el sandbox, que es efímero. Como en U1, una copia duradera exige que la persona elija dónde guardarla, por ejemplo una Release como `fuentes-elis-e-20261117`.
