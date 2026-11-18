# Revisión crítica independiente · hoja resumen en lenguaje llano · ronda 2 (y última)

- **Revisor:** agente distinto del autor (el mismo revisor de la ronda 1). **Fecha:** 18 de noviembre de 2026.
- **Objeto:** rama `examen/hoja-resumen` @ `6406a99` (sobre `ef93699`; base integrada `1694f08`), worktree `/home/user/e_work/wt_hoja`.
  Cambia siete archivos: `personaje_v2/scripts/hoja_resumen.py` (versión 2.0), su README y su batería
  (`pruebas/test_hoja_resumen.py`, 85 casos), `scripts/cierre_v2.py` (+30 líneas), `scripts/pipeline.py` (+14),
  `verificar_paquete.sh` y el manifiesto.
- **Respuesta del autor revisada:** `RESPUESTA_RONDA1.md` (en esta misma carpeta) y `respuesta_ronda1/`.
- **No he modificado la rama ni he hecho ningún commit.** Todo se ejecutó en copias bajo `/tmp/claude-0/revision_hoja_r2/`,
  borradas al terminar. LibreOffice, siempre con el cerrojo común.

## Veredicto: CONFORME CON LÍMITES

Con **dos condiciones** y una lista de **límites** que tiene que aceptar la persona responsable (no yo, ni el coordinador en su nombre).

En pocas palabras:

1. **Los cuatro hallazgos graves de la ronda 1 están corregidos**, y lo he comprobado con reproducciones mías, no con las del autor.
2. **En los 12 expedientes reales con cierre vigente la hoja nueva dice lo que dice la ficha:** sin precio de compra donde la ficha no
   lo da, «no vale para decidir con dinero real» en todas, y cifras iguales a mis recálculos independientes.
3. **La vía oficial no retrocede.** Todas las baterías oficiales dan los mismos recuentos que la referencia `1694f08`. Las dos
   decisiones del coordinador (archivar la hoja al retirar una aprobación y al relanzar el pipeline) funcionan en el flujo real.
4. **Queda un defecto en la vía oficial, de caso límite** (R2-1): si la hoja no se puede archivar al relanzar, el pipeline termina con
   una traza de Python antes de comprobar la vigencia. Es poco probable y no hace decir nada falso a la hoja, pero rompe una regla que
   el propio pipeline enuncia. El arreglo son pocas líneas y lo he probado en mi copia.
5. **Quedan tres frases fijas que dicen más, o distinto, de lo que dice la ficha** (R2-2, R2-3 y R2-4). Dos son de casos que hoy no
   tiene ningún expediente real; la tercera sí sale hoy en Vidrala y Viscofan 4.14.

### Condiciones

| | Condición | Cuándo | Cómo se comprueba |
|---|---|---|---|
| **C1** | Proteger el archivo de la hoja en `pipeline.py` para que un fallo ahí nunca detenga la llamada (R2-1) | Antes de integrar la rama en la vía oficial | Repetir A9b y A9c (apartado 5, R2-1): con el obstáculo puesto, la llamada avisa, **retira la aprobación** y sigue con su código habitual |
| **C2** | Corregir tres frases fijas: «esperar» que no es por precio (R2-2), «comprar» sin precio objetivo (R2-3) y «datos de entrada verificados: sí» sin la reserva de la ficha (R2-4) | Antes de dar hojas a la persona como material de estudio | Tres casos nuevos en la batería (texto en cada hallazgo) |

Las dos condiciones son cambios de pocas líneas. No piden rediseño. Como tocan el pipeline y el texto de la hoja, su comprobación
la debe hacer alguien distinto del autor; con las pruebas de aceptación de este informe basta, no hace falta una ronda entera.

### Límites (resumen; detalle en el apartado 6)

- **L1.** La hoja no es «una página»: tiene entre 1.995 y 2.569 palabras, y el texto del personaje conserva su jerga.
- **L2.** Una hoja escrita fuera del expediente (`--salida`) no se archiva sola.
- **L3.** Sin probar: motor C, expediente favorable real, V6.3.1 F1 real y expediente sin escalera de precios.
- **L4.** «Vigente» no significa «el análisis de referencia»: hay ocho expedientes vigentes de Vidrala y tres de Viscofan, con precios distintos.
- **L5.** La hoja copia la ficha: no la audita. Si la ficha está mal, la hoja también.
- **L6.** No se ha ejecutado `verificar_paquete.sh completa` de una sola vez (sí todos sus bloques, uno a uno).

---

## 1. Qué he hecho

| Comprobación | Resultado | Evidencia (`evidencia_ronda2/`) |
|---|---|---|
| Copia limpia de `6406a99` (`git archive` + los 1.059 archivos fuera de Git, copiados por su huella del manifiesto) y **verificación rápida** | `RESULTADO GLOBAL: PASA` · manifiesto 8.052 archivos, 0 modificados, 0 ausentes, 0 de más · entorno · piloto · 114/114 comprobadores | `verificar_paquete_rapida_6406a99_revisor.txt` |
| Batería del autor, sin envolver en `flock` | **85/85** | `bateria_hoja_resumen_6406a99_revisor.txt` |
| La misma, como la lanza `verificar_paquete.sh completa` (cerrojo ya tomado) | **85/85**; el bloque nuevo del script la aceptaría (umbral 85) | `bateria_hoja_resumen_modo_verificar_paquete.txt` |
| Puerta de la hoja frente a la vigencia oficial en 18 expedientes reales | 12 vigentes → hoja (código 0); 6 de `empresas_v2/` no vigentes → sin hoja (código 3) | `puerta_expedientes_reales.txt`, `lote_reales_r2.txt` |
| `--comprobar` y `--verificar-origen` sobre las 12 hojas | 12 de 12 con código 0 | `comprobar_12_hojas.txt` |
| Cifras de la tabla frente a mis recálculos independientes de la ronda 1 | 11 de 11 filas iguales (diferencia máxima 7,1e-15) | `analisis_12_hojas.txt` |
| Cifras del motor A recalculadas sin LibreOffice (flujos del libro descontados a mano, precio de Sí por bisección propia) | Elis 4.14 (5 tasas) y dos sintéticas: diferencia relativa máxima 4,9e-15 | `dcf_puro_r2.txt` |
| Vigencia: ocho reproducciones (S1 a S8) | Apartado 3 | `vigencia_*.txt` |
| Vía oficial con una hoja dentro: escenarios A, B y C con el pipeline real | Apartado 3 | `pipeline_*.txt` |
| Regresión de las baterías oficiales | Apartado 4: todas iguales a la referencia | `regresion/` |
| Pruebas de función del veredicto, la aptitud, los códigos de error y casos nuevos | Apartados 2 y 5 | `unidad_*.txt`, `sinteticos_favorable_y_pendientes.txt` |

Las 12 hojas regeneradas están en `evidencia_ronda2/hojas/`. Mis guiones, en `evidencia_ronda2/herramientas/`.

---

## 2. Estado de los 14 hallazgos de la ronda 1

| Nº | Gravedad | Qué era | Estado | Mi comprobación |
|---|---|---|---|---|
| 1 | ALTA | Sin conclusión oficial, la hoja ponía un «precio de Sí» en el veredicto y callaba el motivo | **Corregido** | Elis 4.14: «Sin conclusión: falta un dato», motivo de la ficha y «la ficha no da precio de compra… esa cifra no es utilizable». Vidrala 4.12 y 4.13 con bloqueo: «la ficha dice que el objetivo está bloqueado». Vidrala 4.12, 4.13 y 4.14 y Viscofan 4.12, 4.13 y 4.14 condicionados: «Es un precio provisional: el objetivo está condicionado». Sintéticos `pendiente_de_investigacion` y `pendiente_de_datos` cerrados con el pipeline real: sin precio de compra y con la causa. Residuales: R2-2, R2-3, R2-8 |
| 2 | ALTA | Se generaba con material que el sistema oficial no da por vigente (F1 incluido) | **Corregido** | La puerta es la oficial (`cierre_v2.motivo_vigencia`) más cierre registrado y F1. `fase_c.json` o `precio.json` alterados → código 3 y la hoja anterior apartada. Retirada oficial → hoja archivada con el antecedente. Restaurar todo a mano no la reactiva (S8). F1 cambiada tras el cierre (P8, P10) → hoja archivada y código 3, también reponiendo a mano el `fin` antiguo. Residuales: R2-1, R2-5 y el límite L2 |
| 3 | ALTA | Aptitud: callaba «apto por entradas: no» y F1, y podía proclamar «apto para dinero real» | **Corregido**, con un residual | Todas las hojas: «¿Sirve para decidir con dinero real? No. Experimental…». Sintéticos: «Datos de entrada verificados contra sus fuentes: no (0 de 288…)». Con marcas `apto_para_dinero_real = true` forzadas en los tres bloques: no las repite y lo explica. Residual: R2-4 (el «sí») |
| 4 | ALTA | Se escribía aunque fallase su propia verificación | **Corregido** | Códigos 4, 5 y 6 provocados: no queda `hoja_resumen.md`, la anterior pasa a `hoja_resumen.NO_VIGENTE.*` y `--comprobar` da 4. Control con filas correctas: código 0 |
| 5 | MEDIA | La selección de frases dejaba fuera salvedades | **Corregido** (a costa de la longitud: L1) | 12 de 12 hojas llevan la tesis y la tesis inversa enteras. Textos sintéticos vacíos → código 4 por contenido mínimo, sin hoja |
| 6 | MEDIA | No era lenguaje llano | **Parcial; límite declarado (L1)** | Los textos fijos son llanos y hay glosario (13 a 17 términos). El texto del personaje conserva entre 60 y 89 apariciones de jerga por hoja y frases de hasta 82 palabras (132 en Elis) |
| 7 | MEDIA | Faltaban los avisos oficiales de la escalera y de la tasa | **Corregido** | Por fila: «por debajo de la mínima de la hoja» y «descuenta al…» (motor B). Aviso A2 en Viscofan (su 9 % queda bajo la mínima, 9,5 %). Notas fijas: la zona no es la conclusión, el escenario malo no es un suelo, regla experimental k = 3 |
| 8 | MEDIA | «Precio actual» no era el de hoy | **Corregido**, con un residual | «Precio usado en el análisis: 90,10 € (31 de diciembre de 2025)… **Ojo:** es un precio de 318 días antes del análisis, no el de hoy». Residual: R2-6 |
| 9 | MEDIA | La página no estaba protegida por huella | **Corregido** | Conclusión cambiada a mano a «Compraría…» → `--comprobar` y `--verificar-origen` dan 4 («HOJA EDITADA») |
| 10 | BAJA | Un recálculo que no recalculase no se detectaba | **Corregido** | Cinco filas idénticas simuladas → código 6 |
| 11 | BAJA | Cerrojo | **Corregido** | `flock -w` por recálculo; modo «cerrojo ya tomado»; la batería pasa en los dos modos |
| 12 | BAJA | Rótulos | **Corregido** | 0,085 → «8,5 %»; desaparece «firme»; «no se puede calcular» explicado |
| 13 | BAJA | Entradas mal formadas | **Corregido, salvo un caso** | Siete de ocho JSON rotos → código 3 con mensaje. `ficha.provisional` como texto → traza de Python (no escribe hoja; R2-11) |
| 14 | BAJA | La batería no cubría lo anterior | **Corregido en lo principal** | 85 casos, registrada en `verificar_paquete.sh completa`. Faltan: «comprar», «esperar» que no es por precio, `--reiniciar`, hoja no archivable y retirada por la llamada normal del pipeline (R2-11) |

**Sobre el hallazgo 6.** En la ronda 1 escribí que los hallazgos 5 a 9 debían quedar «corregidos o aceptados expresamente como
límites por la persona responsable». El autor declara el límite en su respuesta y en el README. Esa aceptación no me consta y no
puedo darla yo.

---

## 3. Las dos decisiones del coordinador en la vía oficial

### 3.1 Al retirar una aprobación, la hoja se archiva con el antecedente (`cierre_v2.archivar_salidas`)

`archivar_salidas` (líneas 1035 a 1038) llama a `archivar_hoja_resumen` después de mover las salidas oficiales. El fallo de esa llamada
está protegido (`except OSError`), así que no puede impedir la retirada.

| Reproducción | Qué hice | Resultado |
|---|---|---|
| **C3** (sintética, pipeline real) | Cierre vigente con hoja; cambio el material auditado (`fase_c.json`); `pipeline.py EXP` sin opciones | «SALIDAS OFICIALES ARCHIVADAS (historial_cierres/01_…)». Dentro quedan `hoja_resumen.NO_VIGENTE.md` y `.json` y `HOJA_RESUMEN_NO_VIGENTE.json`; `RETIRADA.json` anota `hoja_resumen_no_vigente`. El control sin hoja da lo mismo salvo eso. `--comprobar`: «SIN HOJA» (4). Generar: código 3 |
| **C4 a C6** | Después, `--desde 13`: auditoría nueva del material nuevo y cierre | Cierre nuevo vigente. Ficha igual a la del control. La vía oficial reconoce las mismas auditorías con hoja que sin ella (2 y 2). Hoja nueva: vigente. Llamada normal posterior: código 0, nada cambia |
| **S2** (Vidrala 4.14 real, copia) | `asegurar_vigencia` con la hoja dentro | Hoja archivada con el antecedente; no queda ninguna en el expediente |
| **S8** (la misma copia) | Restauro a mano **todo** con sus bytes originales (ficha, informe, `cierre_vigente.json`, `fase_c.json`, `estado_pipeline.json`) y vuelvo a poner la hoja antigua | Vigencia oficial: «la aprobación… ya se retiró…: restaurar archivos antiguos no la reactiva». `--comprobar`: 4. Generar: 3, y aparta la hoja |
| **S1, S4** | `fase_c.json` o `precio.json` alterados, sin pasar por el pipeline | Generar: 3 y aparta la hoja. `--comprobar`: 4 |

**Conforme.** La hoja respeta «no reactivar aprobaciones retiradas».

Una observación menor. Si la hoja ya estaba apartada por el propio programa (`hoja_resumen.NO_VIGENTE.*` en el expediente), la
retirada oficial no la mueve al historial (S1): se queda suelta, con ese nombre, y la siguiente apartada la sustituye. El nombre
avisa, pero dentro de la página nada dice que ya no vale.

### 3.2 Al relanzar con `--desde` o `--reiniciar`, la hoja se archiva y `fin` pasa a `fin_anterior` (`pipeline.py`)

| Reproducción | Qué hice | Resultado |
|---|---|---|
| **A2** | `pipeline.py EXP` sin opciones, con hoja vigente | Código 0; nada cambia; la hoja sigue |
| **A3, A4** | Llamadas que el pipeline rechaza (`--reiniciar --desde 13`; plantilla equivocada) | Código 2; la hoja sigue (el análisis sigue vigente) |
| **A5** | `--desde 13` | Hoja a `historial_hojas_resumen/01_relanzamiento_…`. Cierre anterior archivado por la vía oficial y cierre nuevo. `fin` nuevo y `fin_anterior` con el antiguo. Ficha idéntica a la de un control sin hoja |
| **A6** | Hoja nueva sobre el cierre nuevo | Vigente; `--comprobar`: 0 |
| **A7, A8** | `--reiniciar` | Hoja a `02_relanzamiento_…`; cierre nuevo; hoja nueva vigente |
| **P8, P10** (V6.3.1 F1 sintética) | Declaración F1 cambiada tras el cierre; `--desde 7` y `--desde 12` | Antes de relanzar, `--comprobar`: 4. Al relanzar: hoja archivada, salidas oficiales archivadas, estado `no_entregable`, sin `fin` y con `fin_anterior`. Generar: código 3. **Reponiendo a mano el `fin` antiguo: código 3 también** («no hay cierre registrado») |

**Conforme en el flujo normal.** `fin` no lo lee nadie más en el paquete (solo `hoja_resumen.py`; lo escribe `pipeline.py`, línea
1232), y ningún esquema valida las claves de `estado_pipeline.json`: la clave nueva `fin_anterior` no afecta a nada oficial.
La puerta de la hoja no depende solo de `fin`.

Un matiz. Cuando en la misma llamada hay relanzamiento y retirada, la hoja va a `historial_hojas_resumen/` con el motivo
«relanzamiento», no junto al antecedente. No se pierde nada: la hoja archivada guarda la huella de la ficha que resumía.

**El defecto está en el caso en que la hoja no se puede archivar: R2-1.**

---

## 4. Regresión de la vía oficial

Cada batería se ejecutó en la copia limpia de `6406a99`; las que usan LibreOffice, bajo `flock` del cerrojo común.
La referencia es la verificación completa de `1694f08` (`revisiones/integracion_1694f08/verif_examen_completa_1694f08.txt`).

| Batería | `6406a99` | Referencia |
|---|---|---|
| `test_comprobadores` (dentro de la rápida) | 114/114 | 114/114 |
| `test_cierre_v2` (toca `archivar_salidas`) | 55/55 | 55/55 |
| `test_vigencia_h5` | 59/59 | 59/59 |
| `test_estados_v2` | 28/28 | 28/28 |
| `test_auditorias_v2` | 55/55 | 55/55 |
| `test_integridad_auditoria_v2` | 103/103 | 103/103 |
| `test_resumen_v2` | 45/45 | 45/45 |
| `test_trazabilidad_v2` | 78/78 | 78/78 |
| `test_relevo_i19_415` | 5/5 | 5/5 |
| `prueba_pipeline_f1` (gancho F1) | 7/7 | 7/7 |
| `prueba_pipeline_v631` (usa `--desde`) | 9/9 | 9/9 |
| `test_pipeline_sintetico` | 30/30; mismos 30 nombres que la línea de base | 30/30 |
| `test_integracion_v64` | 199/199 | 199/199 |
| `test_juicio_objetivo_414` | 27/27 | 27/27 |
| `test_verificacion_entradas_414` | 33/33 | 33/33 |
| `test_verificacion_entradas_415` | 190/190 | 190/190 |
| `test_entrada_efectiva_415` | 62/62 | 62/62 |
| `test_motor_a_f1` | 163/163 | 163/163 |
| `test_v631_f1` | 28/28 | 28/28 |
| `probar_v631_f1.py` estructura · a0 · f1 | 21/21 · 22/22 · 35/35 | 21/21 · 22/22 · 35/35 |
| `test_hoja_resumen` (nueva) | 85/85 | — |

**Sin regresiones.** Son todos los bloques de `verificar_paquete.sh completa`, ejecutados uno a uno. No la he lanzado de una sola
vez (unos 80 minutos con el cerrojo tomado, que habría parado a otras sesiones); el autor tampoco. Conviene hacerlo una vez al integrar.

Estas baterías no ponen una hoja dentro del expediente, así que por sí solas no prueban el código nuevo de `cierre_v2.py` y
`pipeline.py`. Eso lo cubren los escenarios A, B y C del apartado 3 y los casos H2 de la batería de la hoja.

---

## 5. Hallazgos nuevos de la ronda 2

Gravedad: **ALTA**, la hoja dice algo falso o engañoso en un caso real o probable; **MEDIA**, riesgo u omisión relevante, o defecto
en la vía oficial; **BAJA**, caso límite, redacción o cobertura. **No hay ninguno de gravedad ALTA.**

### R2-1 · MEDIA · Vía oficial: el archivo de la hoja al relanzar no está protegido y puede detener la llamada antes de la vigencia

**Dónde.** `pipeline.py`, líneas 1952 a 1962: el bloque que archiva la hoja va antes de `Pipeline(...)` y de
`asegurar_vigencia`, sin `try`. En `cierre_v2.archivar_salidas` la misma operación sí está protegida.

**Por qué importa.** El pipeline cuida que la vigencia se compruebe en todas las ramas de entrada, también en las llamadas que
rechaza (líneas 1928 y 1942) y con el estado ilegible (línea 1968). Lo enuncia así (línea 1919): «una excepción de estructura es
un motivo, nunca una salida que deje la aprobación sin retirar». El bloque nuevo añade un punto donde una excepción sale antes de
esa comprobación.

**Evidencia** (`pipeline_A9_hoja_no_archivable.txt`). Expediente sintético cerrado y vigente, con hoja; un **archivo** llamado
`historial_hojas_resumen` impide crear la carpeta; `fase_c.json` cambiado después de la auditoría.

| Llamada | Con el obstáculo | Control sin obstáculo |
|---|---|---|
| `pipeline.py EXP --desde 13` (A9b) | Código 1, traza `NotADirectoryError`. Después siguen presentes `ficha.json`, `informe.md` y `cierre_vigente.json`, aunque la aprobación ya no vale. Retiradas registradas: 1 (las de antes) | «HOJA RESUMEN ARCHIVADA…», «SALIDAS OFICIALES ARCHIVADAS (historial_cierres/03_…)». Retiradas: 2 |
| `pipeline.py EXP --reiniciar` (A9c) | Código 1, misma traza. Además `estado_pipeline.json` **ya se ha borrado** (línea 1951, antes del bloque) y las salidas oficiales siguen | — |

**Alcance real.** Es un caso límite: hace falta un obstáculo con ese nombre exacto o un fallo de disco o de permisos en ese
instante. La hoja no llega a decir nada falso: `--comprobar` da «HOJA NO VIGENTE» (4) en los dos casos, y una llamada posterior sin
el obstáculo retira la aprobación. Lo que falla es la regla de que nada accesorio detenga la vía oficial.

**Corrección.** Envolver el bloque en `try/except Exception`, avisar y seguir:

```python
    if a.reiniciar or a.desde is not None:
        try:
            ...  # el bloque actual, sin cambios
        except Exception as _e:  # la hoja es material de estudio: nunca detiene la vía oficial
            print(f"AVISO: la hoja resumen no se pudo archivar ({type(_e).__name__}: {str(_e)[:120]}); el pipeline continúa")
```

Con eso, si además hay que retirar la aprobación, `archivar_salidas` se lleva la hoja con el antecedente; y si no, `fin` pasa a
`fin_anterior` y la puerta de la hoja queda cerrada.

**La corrección, probada.** La he aplicado en mi copia del paquete, no en la rama, y he repetido los dos casos
(`propuesta_C1_probada_en_mi_copia.txt`). Con `--desde 13` y con `--reiniciar` la llamada imprime el aviso, archiva las salidas
oficiales (`historial_cierres/03_…`, con la hoja dentro como `hoja_resumen.NO_VIGENTE.*`) y termina con código 10, igual que el
control. Después restauré `pipeline.py` y comprobé su huella contra el manifiesto.

**Prueba de aceptación (C1).** Repetir A9b y A9c sobre la rama corregida: la llamada debe imprimir el aviso, archivar las salidas
oficiales y terminar con el código que daría sin hoja (10 en mi control). Añadir el caso a la batería.

### R2-2 · MEDIA (latente) · «Esperar a mejor precio» cuando la espera no es por precio

**Dónde.** `hoja_resumen.py`, línea 85: `"esperar": "No comprar ahora; esperar a mejor precio."`

**Qué pasa.** La regla oficial (`pipeline.py`, líneas 1843 a 1849) admite un «esperar» con el precio ya en zona de compra
(`cumple_regla_k` o `bajo_malo`), y entonces **exige** «una condición concreta que no sea de precio». En ese caso la frase fija es
falsa: no se espera mejor precio. La página se contradiría a sí misma tres líneas después.

**Evidencia** (`unidad_esperar_sin_precio_y_comprar.txt`, simulación de presentación sobre la ficha de Vidrala 4.14):

> - **Qué concluye:** No comprar ahora; esperar a mejor precio. (Categoría del personaje: «Vigilar».)
> - **Precio usado en el análisis:** 50,00 € …: en el precio de Sí o por debajo (cumple la regla de precio; no basta para comprar…)

Hoy no lo tiene ningún expediente real: los nueve «esperar» vigentes están en zona «caro».

**Mi parte.** La frase es la que propuse yo en la ronda 1 (apartado 4.2 de `REVISION_HOJA.md`). El autor la aplicó tal cual. No
distinguí este caso.

**Corrección.** Elegir la frase por la zona. Con `cumple_regla_k` o `bajo_malo`: «No comprar todavía: el precio ya cumple la regla,
pero espera a que se cumpla una condición que no es de precio (ver «Condición»).» Con «caro» o «vigilar», la actual.

### R2-3 · BAJA (latente, caso favorable) · «Compraría…» seguido de «la ficha no da precio de compra»

**Dónde.** `hoja_resumen.py`, líneas 636 a 650.

**Qué pasa.** «Comprar» puede cerrarse con `precio_objetivo` nulo; así cierra el pipeline real la empresa sintética «sobrevive».
La hoja dice entonces (`sinteticos_favorable_y_pendientes.txt`):

> - **Qué concluye:** Compraría al precio del análisis. Es la conclusión del personaje, no una recomendación. (Categoría del personaje: «Sí».)
> - **A qué precio compraría:** **la ficha no da precio de compra.** La hoja de cálculo arroja un precio de Sí de 18,12 €, pero la ficha no la emite como objetivo.

Las dos líneas se contradicen. El error cae del lado prudente, pero es el caso en que la persona leerá con más atención.

**Corrección.** Con «comprar» y sin precio objetivo: «al precio del análisis ({precio}). La ficha no fija un precio máximo; el
precio de Sí de la hoja de cálculo es {psi}.» La batería no tiene ningún caso «comprar»: añadirlo.

### R2-4 · MEDIA · «Datos de entrada verificados contra sus fuentes: sí» dice más que la ficha

**Dónde.** `hoja_resumen.py`, línea 693. Sale hoy en Vidrala 4.14 y Viscofan 4.14.

**Qué dice la ficha** (`aptitud_de_uso.verificacion_entradas`, Vidrala 4.14): `apto_por_entradas: true`, con esta nota: «condición
necesaria, no suficiente, para presentar una conclusión como apta para dinero real; los controles automáticos comprueban cobertura,
conciliaciones y coherencia, **no la corrección semántica** (revisión independiente de las fuentes)».

**Qué dice la hoja:** «Datos de entrada verificados contra sus fuentes: **sí**.» Sin la nota y sin las cuentas. Un lector lego
entiende que alguien cotejó cada cifra con su documento, que es justo lo que la nota dice que los controles no hacen.

**Contexto del proyecto.** La revisión externa de la 4.14 encontró que esa verificación acepta una página inexistente, una fuente
local ausente si no lleva huella y un redondeo como cifra exacta. El «sí» de la 4.14 vale menos de lo que suena.

**Atenuante.** Justo encima la hoja dice «¿Sirve para decidir con dinero real? No.», y el informe oficial dice «apta por entradas:
sí» también sin la nota. La hoja no contradice a la ficha: la resume con una frase más fuerte que la suya.

**Mi parte.** En la ronda 1 propuse la redacción del «no»; no fijé la del «sí».

**Corrección.** Para el «sí»: «Comprobación automática de los datos de entrada: sin discrepancias ({n} comprobaciones). Es condición
necesaria, no suficiente: comprueba cobertura, conciliaciones y coherencia, no que cada cifra sea correcta.» La segunda frase es la
nota de la ficha.

Si conviene añadir en las hojas de la 4.14 un aviso sobre los tres huecos conocidos de su verificación, lo decide la persona
responsable: la hoja no debe inventar política.

### R2-5 · BAJA · Una retirada que llega mientras la hoja se genera deja una hoja «vigente» en un expediente retirado

**Dónde.** `hoja_resumen.py`, `generar()` (líneas 1026 a 1086): la puerta se comprueba al principio; el recálculo tarda minutos; al
final se escribe sin volver a mirar.

**Evidencia** (`unidad_carrera_retirada_durante_la_generacion.txt`; simulación sin LibreOffice sobre una copia de Vidrala 4.14: en
el lugar del recálculo cambia el material y la vía oficial retira la aprobación):

```
   (durante el recálculo) retirada oficial: el material cambió después de la auditoría (fase_c.json)… archivado en historial_cierres/01_…
   OK: …/hoja_resumen.md · VIGENTE · concluye · 18 frases con origen · …
generar() devuelve 0
   archivos en el expediente: ['aprobaciones_retiradas.json', …, 'hoja_resumen.json', 'hoja_resumen.md', …]
   --comprobar → 4 · HOJA NO VIGENTE: faltan archivos del cierre…
```

Hace falta que alguien toque el expediente en esos minutos, cosa posible con varias sesiones. `--comprobar` lo detecta.

**Corrección.** Antes de escribir, repetir `leer_expediente(exp)` y comparar las huellas con las del principio; si falla o cambian,
código 3 sin hoja. Refuerzo opcional: que el paso 14 del pipeline archive cualquier `hoja_resumen.*` que encuentre al cerrar.

### R2-6 · BAJA · La fecha del precio se lee de un archivo que no es material auditado

`fecha_precio()` (línea 734) lee `fase1_metadatos.json`, que no está en el material auditado. Cambiando ahí 2025-12-31 por
2026-11-13 **antes** de generar, la vigencia oficial no se inmuta y la hoja sale con la fecha cambiada y sin el «Ojo: 318 días»
(`vigencia_S3_S5_S7.txt`, S5). Si el cambio es **posterior** a la hoja, `--comprobar` sí lo detecta («HOJA DESACTUALIZADA», S5b).

En los 12 expedientes reales la fecha coincide con la del libro auditado (`Palancas!C45`, «Fecha del precio»;
`fecha_del_precio_en_los_12.txt`): hoy no hay ningún error.

**Corrección.** Leer la fecha de `Palancas!C45` del libro evaluado, que la hoja ya abre, o cruzar las dos y no escribir si difieren.

### R2-7 · BAJA · Recortes: cortan a mitad de frase y el «Alcance» pierde justo lo más llano

- **Elis, motivo** (línea 795, 420 caracteres): «…frente a 7,30 € de la hoja, que por el supuesto F1 no es … (sigue en la ficha)».
  La palabra que falta es «utilizable». La línea siguiente lo dice, así que no engaña, pero el corte cae en la peor palabra.
- **Alcance** (línea 815, 220 caracteres): se queda con la parte técnica y pierde las frases llanas del aviso. Vidrala 4.14 pierde
  «No es un backtest ni una valoración adoptada». Elis pierde «No es una valoración actualizada a 2026: no recoge la recompra de
  2026 ni la conversión de la OCEANE». Viscofan pierde «no es una valoración a cierre de 2025 ni un backtest».

**Corrección.** Cortar solo en final de frase y, en el Alcance, conservar siempre las frases que empiezan por «No es» o contienen «no es».

### R2-8 · BAJA · Fichas antiguas sin bloque `objetivo`: la línea del precio no anuncia la salvedad

En Vidrala 4.6.1, 4.10.1 y 4.11 la ficha da `decision.precio_objetivo` y pone la reserva en texto libre. La hoja escribe «a 65,69 €
por acción o menos» sin más, y la reserva sale debajo, en las salvedades:

- 4.6.1, condición: «…no es una valoración comparable con el precio. El precio objetivo es el precio de Sí mecánico, resultado
  mecánico de un ensayo exploratorio…».
- 4.11, fundamento: «Precio objetivo provisional: lo condiciona la reposición…».

La reserva está en la página, unas líneas más abajo. **Corrección:** cuando haya salvedades, añadir siempre a la línea del precio
«(con las salvedades de abajo)».

### R2-9 · BAJA · Elis: la hoja no dice que su cierre es anterior a la comprobación F1

Para Elis 4.14 el módulo oficial devuelve `exento`: «cierre histórico registrado anterior a F1-IMPL…: antecedente; su valor A0 no
queda validado por F1». La hoja solo dice «La ficha no dice nada sobre la aptitud; no se presume ninguna». El lector se entera del
problema por las palabras del personaje, no por una línea fija. **Corrección:** cuando `F1.vigencia` devuelva `exento`, añadir en
la aptitud: «Motor A · F1: análisis anterior a esa comprobación; la cifra de la hoja de cálculo no está validada por F1.»

### R2-10 · BAJA · Expediente vigente sin escalera de precios: código 5 con un mensaje que no es el motivo

La vía oficial admite cierres con `precio.json` sin escalera (`sin_lectura`). Con uno así (simulado en la capa de lectura,
`unidad_sin_escalera.txt`) la hoja devuelve 5: «LA SENSIBILIDAD NO REPRODUCE EL PRECIO DE SÍ… {"motivo": "sin escalera en
precio.json"}». No escribe hoja, que es el lado seguro, pero esos análisis («el modelo no sirve para este negocio») se quedan sin
hoja y el mensaje confunde. **Corrección:** hoja sin tabla, o un mensaje propio. Mientras tanto, declararlo en el README.

### R2-11 · BAJA · Varios

- **README, línea 3:** «Una página por empresa para estudiar sin jerga». Su propio apartado «Límites» dice lo contrario.
- **Rótulo de antecedente** (línea 784): falta el punto antes de «Esta hoja solo sirve…».
- **Pie de una hoja escrita con `--salida`:** aconseja `hoja_resumen.py Vidrala --comprobar`, sin `--salida`. Así se obtiene «SIN
  HOJA» (lado seguro), no una respuesta sobre esa copia.
- **El pie no identifica el expediente:** solo el nombre de la carpeta («Vidrala») y el principio de la huella. Vidrala 4.12 y 4.13
  condicionados dan páginas casi iguales (56,02 €, 12 de noviembre). Poner la ruta relativa del expediente.
- **`ficha.provisional` como texto** (línea 472): traza `AttributeError`; no escribe hoja.
- **Antecedentes del motor A sin F1** (Hermès, Nike; solo con `--antecedente`): tras «Sin conclusión: el motor de cálculo A no se
  puede usar para concluir (F1)» sale «Qué lo resolvería, según la ficha: El informe financiero semestral…», que responde a otra
  pregunta. Lo que falta ahí es la evaluación F1.
- **`archivar_salidas`:** si la hoja no se pudiera archivar, el `except OSError` lo calla. Mejor anotarlo en `RETIRADA.json`.
- **Repeticiones del personaje:** «Bajaría el precio de Sí si… Bajaría el precio de Sí: …». Y el resto declarado «cálculo propio con)».
- **Batería:** faltan los casos de C1 y C2, `--reiniciar`, la retirada por la llamada normal del pipeline, la carrera de R2-5 y el
  expediente sin escalera.

---

## 6. Límites

**L1 · Longitud y jerga (declarado por el autor).** Entre 1.995 y 2.569 palabras por hoja, frente a las 1.000 a 1.300 de la versión
anterior (cifra del autor). Es el precio de dar la tesis inversa entera, que pedí yo. La parte de arriba, hasta «Por qué», tiene entre 244 y 434
palabras y sí funciona como resumen de una página: conclusión, precio, aptitud y salvedades. El texto del personaje conserva su
jerga («ROIC», «capex», «λ 1,10», «PM1.estructura»), explicada solo en parte por el glosario. La solución de fondo que apunta el
autor, un resumen llano escrito por el personaje y auditado con el resto, me parece la correcta y queda fuera de esta rama.

**L2 · Hoja fuera del expediente (declarado).** Comprobado (S3): tras la retirada oficial la copia de fuera sigue ahí, y
`--comprobar --salida` da 4. Depende de que alguien lo ejecute. La cabecera avisa: «Deja de valer si el análisis oficial cambia».

**L3 · Sin probar.** Motor C: no hay expediente (declarado). Caso favorable y V6.3.1 F1: solo con empresas sintéticas. Sin escalera
de precios: solo simulado (R2-10). Otra máquina: la ruta del cerrojo no se ha probado fuera de esta.

**L4 · «Vigente» no es «el de referencia».** Para la vía oficial están vigentes a la vez ocho expedientes de Vidrala (precio de
compra 65,69 · 66,52 · 57,74 · 56,02 · 56,02 · 56,00 € y dos sin precio) y tres de Viscofan (39,29 · 40,16 · 39,80 €). La hoja de
cada uno sale como vigente y no puede saber cuál es el bueno. Eso lo decide el catálogo de expedientes, no la hoja.

**L5 · La hoja copia; no audita.** Es su diseño y es correcto. Los defectos conocidos del material (verificación de entradas de la
4.14, C48 de Elis, F1 del motor A) llegan a la hoja tal como estén en la ficha.

**L6 · Verificación completa.** Ver apartado 4.

---

## 7. Método, incidencias y lo que no he comprobado

- **Copias.** Copia limpia del paquete (`git archive 6406a99` más los archivos fuera de Git por su huella del manifiesto) y copias
  de expedientes. La rama y sus expedientes no se han tocado: `git status` vacío en `wt_hoja` al acabar, HEAD `6406a99`.
- **Cerrojo.** El pipeline y las baterías, envueltos en `flock /home/user/e_work/libreoffice.lock`. La hoja y su batería toman el
  cerrojo por dentro, así que no se envuelven, salvo en el modo «ya tomado».
- **Incidencia 1.** Detuve a medias un guion mío de regresión. Un proceso hijo del pipeline siguió vivo unos 20 segundos y pudo usar
  LibreOffice sin cerrojo mientras se recalculaba mi hoja de Elis. Lo paré. Regeneré la hoja de Elis y sus filas son idénticas;
  además coinciden con el cálculo sin LibreOffice (4,9e-15). Las baterías se repitieron enteras después. No me consta efecto sobre
  otras sesiones.
- **Incidencia 2.** El primer intento de A9b lo cortó el límite de 30 minutos de las tareas en segundo plano mientras esperaba el
  cerrojo; el resto del guion siguió y la prueba no valía. Se repitió en copias nuevas, que son las del informe.
- **Simulaciones.** R2-2, R2-5 y R2-10 se han reproducido en la capa de lectura o de presentación de la hoja, no con un expediente
  cerrado de ese tipo. R2-1 y R2-3, con el pipeline real.
- **No comprobado.** La corrección de los hallazgos de esta ronda en la rama (no hay otra ronda; la de R2-1 solo la he probado en
  mi copia). `verificar_paquete.sh completa` de una vez. La aceptación de los límites por la persona responsable.
- **Este repositorio de evidencias.** Su `AGENTS.md` pide no ejecutar aquí LibreOffice ni el pipeline y no subir binarios. Aquí
  solo he dejado este informe y evidencia en texto (`.txt`, `.md`, `.json`, `.py`, `.sh`); las ejecuciones se hicieron en mis
  copias temporales del paquete, como pedía el encargo. No he hecho commit: queda a decisión del coordinador.

---

## 8. Evidencia (`evidencia_ronda2/`)

| Archivo | Contenido |
|---|---|
| `verificar_paquete_rapida_6406a99_revisor.txt` | Verificación rápida en copia limpia |
| `bateria_hoja_resumen_6406a99_revisor.txt`, `bateria_hoja_resumen_modo_verificar_paquete.txt` | Batería del autor, 85/85 en los dos modos |
| `regresion/` | Salidas de todas las baterías oficiales y sus resúmenes |
| `puerta_expedientes_reales.txt`, `lote_reales_r2.txt`, `comprobar_12_hojas.txt` | Puerta, generación y comprobación en los expedientes reales |
| `hojas/` | Las 12 hojas regeneradas, sus salidas y tres hojas sintéticas |
| `veredictos_reales_1.txt`, `veredictos_reales_2.txt`, `veredictos_antecedente.txt` | Cabeceras de las hojas |
| `analisis_12_hojas.txt`, `dcf_puro_r2.txt` | Cifras frente a mis recálculos; longitud, jerga y avisos |
| `vigencia_S1_S2_S4_S6.txt`, `vigencia_codigos.txt`, `vigencia_S3_S5_S7.txt`, `vigencia_S8_reactivacion.txt` | Reproducciones de vigencia. Los «(código 0)» del primer archivo son un defecto de mi captura; los códigos reales están en `vigencia_codigos.txt` |
| `pipeline_relanzamientos.txt` | Escenarios A y B (`--desde`, `--reiniciar`, P8, P10) |
| `pipeline_retirada_con_hoja_y_recierre.txt` | Escenario C (retirada por la llamada normal y cierre nuevo) |
| `pipeline_A9_hoja_no_archivable.txt` | R2-1: A9b, su control y A9c |
| `propuesta_C1_probada_en_mi_copia.txt` | R2-1: la corrección propuesta, aplicada solo en mi copia, y los dos casos repetidos |
| `unidad_veredicto_aptitud_codigos.txt`, `unidad_esperar_sin_precio_y_comprar.txt`, `sinteticos_favorable_y_pendientes.txt` | Veredicto, aptitud y códigos; R2-2 y R2-3 |
| `unidad_carrera_retirada_durante_la_generacion.txt` | R2-5 |
| `fecha_del_precio_en_los_12.txt` | R2-6 |
| `unidad_sin_escalera.txt` | R2-10 |
| `rutas_del_expediente.txt` | La puerta con rutas escritas de otra forma y con la carpeta renombrada |
| `herramientas/` | Mis guiones |
