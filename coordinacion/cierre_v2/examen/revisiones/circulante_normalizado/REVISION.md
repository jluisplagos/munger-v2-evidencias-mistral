# Revisión independiente · `f1/circulante-normalizado` (V-CIRC (a): circulante normalizado en la reinversión y plantilla V6.3.2 F1)

- **Rama revisada:** `f1/circulante-normalizado` @ `fbb146d`, sobre `ebf47fc`. Commits:
  - `eededd1`: código, pruebas y documentación (54 archivos);
  - `f4b44e8` y `fbb146d`: manifiesto;
  - `ca85eab`: registro de la verificación rápida.

  Diff revisado: `git diff ebf47fc..fbb146d`, 55 archivos (42 nuevos y 13 modificados). Ninguno está en `2026-11_examen_universo/`.
- **Revisor:** agente Claude distinto del autor (Opus 5.5), 19-nov-2026.
  - No toqué la rama del autor ni ningún expediente. De `vinci/Vinci` y de los demás expedientes solo hice copias o lecturas.
  - No leí la rúbrica ni `contradictor/`.
- **Copias** (en `/dev/shm`, borradas al terminar):
  - `nuevo`: `git archive fbb146d` con los 1060 binarios del manifiesto, copiados solo si su huella coincidía;
  - `antes`: el código de `ebf47fc`;
  - `mixto`: la prueba nueva sobre el código anterior;
  - copias de `vinci/Vinci` para el diagnóstico.
- **LibreOffice:** siempre con `flock /home/user/e_work/libreoffice.lock`, una ejecución cada vez.
- **Evidencia:** `evidencia/` (resultados literales, baterías y scripts del revisor).
- Experimental supervisado. **No es apto para dinero real.** Esta revisión no acredita aptitud por entradas ni aptitud económica.

## Veredicto: **CONFORME CON CORRECCIONES** (C1). La rama **no** se integra

Para VINCI, la rama hace lo que dice. Reproduje sus cifras de tres formas: con un cálculo propio en fracciones, con el libro V6.3.2 recalculado con LibreOffice y con la capa.

- Las pruebas distinguen el código nuevo del anterior.
- Sin la declaración no cambia nada: ni en la capa (6 expedientes) ni en la huella de entradas (925 libros).
- El manifiesto falla solo por los 20 archivos ajenos de `jumbo_g`.

**Queda una corrección.** La guarda F1-CIRC no impide del todo lo que se le pide (§2). Una declaración con dos partidas C46 que se compensan hace pasar la normalización en una empresa cuya caja base **sí** cuenta el circulante. Con un libro V6.3.2, el resultado queda utilizable sin que bloquee nada. La documentación afirma lo contrario.

**Dos decisiones son de la persona y no corrigen el código:**

1. Confirmar que el ajuste entra también en el ancla de S2C (§1).
2. Conocer el límite del capital del balance (§3).

| VINCI (A2_propio) | f | Reinversión media | Flujo sin crecimiento | Ancla S2C | Bloquean |
|---|---|---|---|---|---|
| Estado actual (V6.3.1, sin la declaración) | 4,4899 % | −1.514,333 | 3.016,069 | 5,9595 | F1-K3c |
| V6.3.2 con la normalización 2021–2025 | 1,5744 % | +575,667 | 5.190,977 | 2,3226 | — |

Las dos filas coinciden en el libro, en la capa y en mi cálculo propio. Diferencias entre libro y capa: f −1·10⁻¹⁶ y ancla 1·10⁻¹³.

## 1. El ancla de S2C (5,96 → 2,32): coherente, pero la tiene que confirmar la persona

**Las cifras.** Hice el cálculo en fracciones desde la Historia del libro recalculado (`evidencia/calculo_independiente_vinci.txt`):

- incremento de ventas (L6 − G6): 74.599 − 43.234 = 31.365;
- denominador H–L con la fila 14: Σ fila 31 = 5.263, de donde el ancla es 5,9595;
- denominador H–L sin el circulante: 5.263 + 8.241 = 13.504, de donde el ancla es 2,3226. Los 8.241 son el circulante excluido de 2021–2025: 1.579 + 392 + 1.463 + 2.311 + 2.496.

**Es la lectura coherente**, por tres razones:

- **Lo que dice la decisión.** (a) pide «ni entradas ni salidas de circulante». Si el ancla cuenta las entradas de circulante como reinversión negativa (5,96), esas entradas vuelven a la proyección por la palanca S2C: el crecimiento parece más barato. Lo mismo ocurre con un ancla que normaliza solo la ventana (2,720): mezcla dos definiciones en un mismo cociente. La rama rechaza esa ancla y exige cubrir H–L.
- **F1 (4a)** (`DECISIONES_PARA_EL_USUARIO.md:74`): «un solo perímetro para f, el ancla de S2C, el margen y el ROIC del terminal». Entre f y el ancla se cumple: con la normalización, la fila 30 entra en los dos cálculos con la misma fila 96. Con el ROIC del terminal no del todo, porque el capital del balance sigue llevando el circulante (§3).
- **El precedente de D-US2.** La implementación aplica el ajuste del circulante con US GAAP (`retira_de_14`) en f y en el ancla, con la misma función `WC_de` (`motor_a_f1.py:1301` y `1321`). Exige sus importes en la ventana y en H–L, y así se revisó (`examen/revisiones/f1_usgaap/REVISION_R1.md:193`). El texto de la decisión D-US2 (`DECISIONES_PARA_EL_USUARIO.md:98`) no habla del ancla: el precedente es de implementación, no una decisión de la persona.

**Pero es una decisión económica que la persona no tomó de forma explícita.**

- `vinci/resultados/diagnostico_k3c_vinci.md` dejaba aparte, como punto (3), «decidir si el ajuste entra también en el ancla». La persona respondió «(a)» y nada más (`DECISIONES_PARA_EL_USUARIO.md:134`).
- (a) y D-US2 no hablan del ancla. (4a) se decidió para el perímetro, es decir, qué activos entran (derechos de uso y PPA), no para el circulante. Llevar el ajuste al ancla es una interpretación del autor, bien razonada, y él mismo lo dice (`F1_CIRCULANTE.md` §3.1 y §8.7).
- Es la consecuencia más material para las fases. El ancla se divide por 2,57: hay 2,57 veces más reinversión por euro de crecimiento.
- **Cuándo confirmarla:** antes de lanzar la fase A de `vinci_b`. La fase A ya ve las anclas en `datos_v63.md`. La fase B ancla el S2C en `Historia!C53` (Palancas F16).

No es una corrección de código. El producto aplica una sola regla coherente. Si la persona quiere el ancla sin normalizar, hará falta otro cambio de producto.

## 2. ¿Impide la guarda usar la normalización para silenciar K3c en otra empresa? Solo en parte (C1)

**Lo que sí impide.** Pongamos una empresa cuya caja base cuenta el circulante y cuya declaración no trae una partida C46 igual a la media de la fila 14. F1-CIRC bloquea con DATOS INVÁLIDOS: lo muestra la prueba «G · caja base CON el circulante», y yo lo reproduje también con un libro V6.3.2.

**Lo que no impide.** Lo comprobé con dos sondas: `evidencia/sonda_partidas_compensadas.txt` y `evidencia/sonda_partidas_compensadas_v632.txt`. La segunda usa un libro V6.3.2 sintético de tipo VINCI, recalculado por el oráculo de la propia prueba, que no depende de `motor_a_f1`. Su caja base cuenta el circulante, como en la prueba del autor. A la declaración le añadí la normalización y dos partidas C46 que se compensan: «circulante excluido» por −2.090 y «compensación» por +2.090. Las dos citan un documento que no existe: «x», página 1.

| Libro V6.3.2, caja base que cuenta el circulante | Bloquean | Utilizable | f | Flujo sin crecimiento |
|---|---|---|---|---|
| Normalización sin partida C46 del circulante | F1-CIRC | no | −1,3411 % | 7.365,885 |
| **Normalización + dos partidas C46 que se compensan** | **ninguna** | **sí** | **−1,3411 %** | **7.365,885** |
| Referencia: caja base sin el circulante y partida genuina | ninguna | sí | 1,5744 % | 5.190,977 |

Con la declaración amañada, K3a cuadra, F1-CIRC da por buena la partida de −2.090 y K3c no salta. El flujo sin crecimiento queda un 42 % por encima del caso genuino y 2,4 veces el que da VINCI sin normalizar. Con un libro V6.3.1, en la prueba del autor, solo bloquea F1-LIBRO, y lo hace porque la V6.3.1 no normaliza: es un límite declarado, no una protección.

**Por qué ocurre:**

- K3a suma las partidas por componente (`motor_a_f1.py:1477`).
- F1-CIRC solo busca una partida C46 cuyo importe sea la media de la fila 14 (`motor_a_f1.py:661`).
- Nada contrasta las fuentes de `conciliacion_fcf_base`. K3a exige que el campo `fuente` no esté vacío (`motor_a_f1.py:1474`). Ningún otro script lee esas partidas, salvo `entradas_dependientes.py` para las entradas dependientes, y `verificacion_entradas.py` no las revisa. Este hueco ya existía antes de la rama, pero F1-CIRC se apoya ahora en él.
- En VINCI hay dos partidas C46 genuinas, −2.090 (circulante) y +37,333 (dividendos). Exigir una sola partida C46 no sirve. Cualquier regla que mire solo las partidas declaradas se cumple declarando partidas.

**La documentación dice más de lo que la guarda comprueba:**

- `F1_CIRCULANTE.md` §3.4 (línea 81) y §8.2 (línea 179): «K3a garantiza que esa partida explica de verdad la diferencia entre C46 y el CFO». K3a garantiza solo que **la suma** de las partidas C46 la explica.
- La docstring de `_guarda_circulante`, punto (v) (`motor_a_f1.py:632`): «la caja base excluye de verdad ese circulante».
- El nombre de la prueba G (`test_circulante_f1.py:315`): «la normalización no sirve para ocultar entradas de circulante».

**En VINCI la partida es genuina.** −2.090 es la media de 1.463, 2.311 y 2.496. La línea «Changes in operating working capital requirement and current provisions» está en las páginas citadas: URD 2024, PDF 336 (2.311 y 1.463), y URD 2025, PDF 358 (2.496 y 2.311). Lo comprobé en `texto/`.

**C1. Lo que hay que hacer:**

- **(a) Corregir las cuatro afirmaciones** para que digan lo que F1-CIRC comprueba de verdad: que existe una partida C46 declarada con ese importe. No comprueba que sea cierta ni que otra partida C46 no la compense. El README de la V6.3.2 y el §12 de `F1_IMPL.md` no exageran; los busqué.
- **(b) Añadir a `test_circulante_f1.py` el caso de las partidas C46 que se compensan.** Debe registrar lo que haga la guarda: que bloquee si se endurece, o que pase como límite declarado si no.
- **(c) Recomendado** antes de usar la normalización en cualquier empresa distinta de VINCI: endurecer F1-CIRC con datos verificados, no con partidas declaradas. El diseño es del autor. Hay tres vías posibles:
  - contrastar las fuentes de las partidas de `conciliacion_fcf_base`: que el documento esté en el expediente, que la página exista y que la cifra aparezca, como hace `verificacion_entradas` con las entradas. Esto cerraría también el hueco previo de K3a;
  - exigir que la exclusión del circulante figure en la derivación registrada y sellada de Análisis C46;
  - como mínimo, una comprobación expresa del revisor de entradas o del auditor sobre las partidas C46 cuando haya normalización.

  Hasta entonces, la protección real es humana: la decisión de la persona para esa empresa y la revisión de sus partidas C46. Hay que decirlo así.

## 3. El límite declarado: el capital invertido del balance sigue llevando el circulante

Lo comprobé en las fórmulas. Las filas 32 y 33, C54 (S2C medio de todo el capital) y C55 (ROIC medio) son idénticas en la V6.3.1 y en la V6.3.2. La normalización solo toca los flujos (filas 30, 95 y 96, y C53, C58 y C76).

- En VINCI, el capital invertido de 2021–2025 es 44.652, 45.460, 45.522, 52.607 y 53.059. La fila 32 es patrimonio + deuda + arrendamientos − caja.
- C54 vale 1,406 y C55, 10,50 %. Con la normalización no cambian.
- Según el autor, el circulante es negativo en VINCI. No lo he cuantificado.

Con (a), la reinversión de la proyección no lleva circulante, pero el capital del que se toma el ROIC sí. El ROIC terminal que fijan las fases puede quedar alto. Conviene enseñárselo a la persona junto con la decisión del §1. No es una corrección: el autor lo declara en §8.1, y aplicar ahí el mismo criterio sería otra decisión.

## 4. Pruebas, ejecutadas por mí

| Batería | Resultado |
|---|---|
| `pruebas/test_circulante_f1.py` (nueva) | **77/77**. Con el código de `ebf47fc` pasan 8 de 77, así que distingue. |
| `f1_circulante/scripts/mutaciones_circulante.py` | **33/33** mutaciones detectadas (283 comprobaciones por mutación) |
| V6.3.2 F1 con LibreOffice: estructura · a0 · circ · pipeline | 26/26 · 39/39 · 16/16 · 8/8 |
| V6.3.1 F1 con LibreOffice: f1 · pipeline · libro US GAAP · gancho F1 | 35/35 · 9/9 · 18/18 · 8/8 |
| `test_motor_a_f1` · `test_motor_a_f1_usgaap` · `test_v631_f1` · `test_perimetro_foso` · `test_f1_series_escala` | 177/177 · 294/294 · 29/29 · 72/72 · 80/80 |
| `test_entradas_dependientes` · `test_redondeo_historia` · `test_acciones_metadatos_exactas` | 51/51 · 44/44 · 30/30 |
| `test_auditorias_v2` · `test_estados_v2` · `test_integridad_auditoria_v2` · `test_juicio_objetivo_414` · `test_resumen_v2` | 55/55 · 28/28 · 103/103 · 27/27 · 45/45 |
| Con LibreOffice: `test_cierre_v2` · `test_verificacion_entradas_415` | 55/55 · 190/190 |
| Con LibreOffice: reparación completa (`ejecutar_pruebas_reparacion.sh`) | PASA: comprobadores 114/114, pipeline sintético 30/30 y los mismos 30 nombres que la línea de base |
| Con LibreOffice: `test_integracion_v64` | 199/199 |
| `verificar_paquete.sh rapida` sobre una copia limpia de `fbb146d` | **No ejecutada.** La cancelé mientras esperaba el cerrojo de LibreOffice, para no retener los pipelines de otras sesiones. El manifiesto lo comprobé por huellas (§7). Los demás bloques de la rápida están sueltos en esta tabla, salvo el del entorno y el del piloto. El autor registró la suya sobre `f4b44e8` en `ca85eab`. |

Resultados literales en `evidencia/baterias/`, `evidencia/t_circ_nuevo.txt` y `evidencia/mut_circ.txt`. Las 77 pruebas solo cubren el caso honesto de la caja base (§2). El caso de las partidas que se compensan no está.

## 5. Sin la declaración no cambia nada

- **La capa** (`evidencia/efecto_nulo_revisor.txt`). Ejecuté el código de `ebf47fc` y el de `fbb146d` sobre el libro recalculado de cada expediente. Las salidas son idénticas salvo la versión y la fecha:

  | Expediente | f | Flujo sin crecimiento | Bloquean |
  |---|---|---|---|
  | `ahold_f3` | 0,0140 % | 2.769,835 | — |
  | `ahold_f4` | 0,0140 % | 2.769,835 | — |
  | `jumbo_g` | −0,4247 % | 327,146 | — |
  | `zoetis_t1c` | 1,0095 % | 2.484,631 | — |
  | `zoetis_t1d` | — | — | — |
  | `vinci/Vinci` | 4,4899 % | 3.016,069 | F1-K3c |

- **La huella de entradas** (`evidencia/huellas_entradas_925_libros.txt`). Calculé `entradas_economicas.instantanea` con los dos códigos sobre los 925 libros `.xlsx` de `empresas_v2_correcciones` en `wt_expedientes`. Hay 0 huellas distintas. C93 y C94:L94 solo entran en un libro V6.3.2.
- **La plantilla.** Entre la V6.3.2 y la V6.3.1 hay exactamente 36 fórmulas distintas:
  - las filas 30, 95 y 96 (C–L), C97, C53, C58 y C76;
  - Motor!E205, que añade dos mensajes: «no reconocida» (INV) y años de la ventana sin marcar (INC);
  - Panel!A1, con el rótulo de la versión.

  Con «ninguna», la batería a0 da 0 celdas distintas frente a la V6.3. La huella de la plantilla es `046b64fc…` y coincide con el manifiesto.

## 6. Diagnóstico de VINCI, reproducido

`diagnostico_vinci_circulante.py`, que vuelvo a ejecutar sobre una copia (`evidencia/diagnostico_vinci_circulante.md`), da lo mismo que el del autor:

- f 1,5744 %, flujo sin crecimiento 5.190,977 y ancla 2,3226;
- libro − capa: f −1,0·10⁻¹⁶, ancla 1,0·10⁻¹³ y reinversión −3,3·10⁻¹⁰;
- verificador del libro V6.3.2: ÍNTEGRO;
- F1-CIRC conforme y F1-K3c sin saltar.

El puente K3 suma bien: 4.419,333 + 424,636 − 182,807 − 45,852 − 1.514,333 + 2.090,000 = 5.190,977. Por perímetro, el flujo sin crecimiento es A0 4.333,2 · A1 5.095,9 · A2 5.191,0 · cota B 4.591,9.

Mi cálculo propio en fracciones coincide (`evidencia/calculo_independiente_vinci.txt`). Avisos que siguen: F1-SERIES-CERO (la PPA de 2021 = 0, pendiente de revisor) y V-F1f.

## 7. El manifiesto de la rama

`fbb146d` tiene 9.860 entradas (`evidencia/manifiesto_fbb146d.txt`). Fallan 6 archivos modificados y sobran 14. Son exactamente los 20 archivos de `jumbo_g` de `ebf47fc`, y ninguno está fuera de `jumbo_g`. Es lo que decía el encargo.

## 8. Integración: no hecha (falta C1)

Dejo preparado lo que comprobé:

- Durante la revisión, el destino avanzó de `b8b151e` a `de26eb5` (ahold_f4, de otra sesión). `wt_expedientes` estaba limpio.
- `git merge-tree` de los dos destinos con `fbb146d` solo choca en `MANIFIESTO_SHA256.txt`.
- `verificar_paquete.sh` se mezcla sin conflicto: lleva el bloque de minoritarios-cero y el de la V6.3.2, y pasa `bash -n`. Los 33 archivos que cambian de `b8b151e` a `de26eb5` son todos de `ahold_f4`.
- El manifiesto del destino tiene 1059 binarios. La rama añade `v6/v632_f1/entregables/Plantilla_V6.3.2_F1.xlsx`, que hace 1060.
- En `de26eb5` hay 43 archivos ya comprometidos sin entrada en el manifiesto (23 en `b8b151e`). Habrá que aceptarlos al regenerarlo, junto con los de la rama.

## 9. Observaciones menores (no bloquean)

1. `entradas_economicas.instantanea` reconoce la V6.3.2 solo por el rótulo de Historia A92. `f1_libro_v631.es_v632` exige además la fórmula de C97. En un libro V6.3.2 íntegro, que trae las dos cosas, da lo mismo. Convendría usar un solo criterio.
2. Motor!E205 avisa solo de los años de la ventana que falten. Si falta un año de H–L, el libro deja C53 vacía y la capa bloquea con F1-CIRC: es coherente, aunque el Motor no lo dice.
3. Los encargos de las fases (`prompts/`) no cambian, como declara el autor en §8.6. La nota de `datos_v63.md` es lo único que les explica la normalización y el ancla nueva. Lo comprueba la prueba DATOS.

## Qué tiene que hacer cada uno

- **El autor:** C1 (a) y (b). Recomendado: C1 (c) antes de usar la normalización fuera de VINCI.
- **El revisor**, en una ronda corta: comprobar C1 e integrar en la misma ronda si queda conforme.
- **La persona responsable:**
  - confirmar o corregir el ancla de S2C normalizada (§1) antes de lanzar la fase A de `vinci_b`;
  - conocer el límite del capital del balance (§3).
