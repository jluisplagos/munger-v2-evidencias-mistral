# Revisión independiente · plantilla V6.3.1 F1 del motor A

- **Revisor:** agente distinto del autor (Claude, Opus), 18-nov-2026. No modifiqué ningún repositorio.
- **Material:** rama `f1/plantilla-v631`, copia `/home/user/e_work/wt_v631` @ `4928fc9` (sobre `f1/implantacion` @ `24e9a30`). Sigue en `4928fc9` y sin cambios.
- **Dónde trabajé:** en copias bajo `/tmp/claude-0/revision_v631/` (borradas al terminar). LibreOffice siempre con `flock /home/user/e_work/libreoffice.lock`, una ejecución detrás de otra.
- **Evidencia:** `/home/user/e_work/revision_v631/evidencia/`, con mis guiones (`difform.py`, `indep_elis.py`, `libros.py`, `ataques.py`, `ataques2.py`, `pipe_r21*.py`) y sus salidas (`*.json`, `difform.txt`, `ataques2_salida.txt`, `pruebas_autor.txt`).
- **Aptitud:** uso supervisado experimental. No apta para decisiones con dinero real. Que pase estas pruebas no la acredita.

## Veredicto: CORRECCIONES (acotadas)

**La plantilla está bien.** Con perímetro vacío o `A0_total` da lo mismo que la V6.3, lo comprobé por una vía distinta de la del autor. Con A1 y A2 da los valores E9: los reproduje con un cálculo propio.

El oráculo detecta todas las manipulaciones del libro que probé dentro del pipeline.

Hacen falta correcciones antes del examen por cuatro motivos:

1. **R2-1 sigue abierto.** Lo reproduje con la V6.3.1: el expediente llega a `concluido` con un libro que no corresponde a la declaración.
2. **`F1-SERIES` acepta cifras que no son la publicada** (por coincidencia parcial de dígitos o de otro ejercicio) y fuentes sin huella. Es justo el caso en que libro y capa coinciden y los dos están mal.
3. **La aptitud por entradas y su huella no ven el perímetro ni las series.**
4. Hay dos incoherencias menores en el ancla.

## Hallazgos

### V631-1 · media (requisito antes del examen) · R2-1 sigue abierto en la V6.3.1

**Evidencia** (`pipe_r21b.py`, `resultado_pipe_r21_v2.json`). Usé la empresa sintética con arrendamientos y A1 de `prueba_pipeline_v631.py`. Primero la cerré con la V6.3.1: `concluido · esperar · precio objetivo 19,614`, con F1 utilizable. Este estado confirma también el `concluido` del §7 del README.

| Caso, sobre una copia del expediente cerrado | Resultado |
|---|---|
| R21a · borro `motor_a_f1_resultado.*` y lanzo `--reiniciar --desde 13` | **`concluido` · ficha oficial con la plantilla V6.3.1 F1 · esperar · 19,614**; bloque F1: «el motor no es el A» |
| R21b · como R21a, con la declaración cambiada (D&A de derechos de uso del 30 % al 40 %; el libro calcula el 30 %) | **`concluido` · esperar · 19,614**, sin evaluación F1 |
| Control 1 · declaración cambiada, resultado borrado, `--desde 13` sin `--reiniciar` | `no_entregable` en el paso 12 por `F1-LIBRO` |
| Control 2 · declaración cambiada, resultado conservado, `--reiniciar --desde 13` | `no_entregable` en el paso 12 (por `verificar_todo.sh`, no por F1) |

**¿La V6.3.1 lo agrava?**
- En el mecanismo, no. `vigencia()` y el gancho no cambiaron. Un expediente nuevo deja resultado en el paso 7, así que hace falta borrar ese resultado (equivale a PC2-4).
- En el efecto, sí cambia: lo que se cuela ahora es la conclusión de un libro A1 o A2 sin oráculo, sin `F1-SERIES` ni guardas F1, y además con una declaración distinta de la del libro (R21b). Antes se colaba la de un libro A0.

**Corrección:** la ya probada en R2-1. Si el estado no dice el motor, `vigencia()` lo toma de `fase_a.json`. Si no se corrige, `pipeline.py` debe rechazar `--reiniciar` junto con `--desde`.

### V631-2 · media · `F1-SERIES` no acredita la cifra: libro y capa coinciden y los dos están mal

**Evidencia:** `ataques.py` (E1) y `ataques2.py` (S1–S6), sobre el texto real de Elis y una fuente sintética.

- **E1 · ejercicio equivocado.** Declaro la D&A de derechos de uso de 2025 con la cifra de 2024, «(132.2)», que está en la misma página (URD2025 p. 350):
  - `F1-SERIES`, `F1-LIBRO` y `F1-REPLICA` no saltan;
  - el libro, recalculado, coincide con la capa;
  - f pasa de 0,012624 a **0,013889**, C53 de 2,445 a 2,498 y el año 11 NORMAL de 413,85 a **404,91**.

  Nada lo detecta: la guarda no mira ni el ejercicio ni la columna.
- **S1/S3 · coincidencia parcial.** La guarda solo busca el literal como subcadena del texto de la página, sin espacios:
  - «149.5» se acepta en una página que solo tiene «(1149.57)»;
  - «8.5», positivo, se acepta en una página que solo tiene «(2008.5)».

  T9 se cumple frente al literal que escribe el declarante, no frente a la página. Quitar los paréntesis basta para pasar.
- **S4/S5/S6 · la fuente.**
  - Cualquier `.txt` con marcas `[PDF PAGE n]` creado en el expediente sirve: no hay huella ni registro.
  - `VE._ruta_fuente` admite rutas de todo el paquete, así que el texto de otro expediente (el de Elis, desde una carpeta vacía) pasa.
  - `documento` (lo que el libro escribe en M86) y `archivo` (lo que se examina) no se contrastan: se acepta `documento` URD2022 con `archivo` del URD2025.

**Corrección mínima:**
- buscar la cifra como token completo, con los límites del número y los paréntesis, igual que el literal;
- `archivo` solo dentro del expediente, con su SHA-256 declarado y comprobado, y ligado a `documento`;
- `ejercicio` y `columna` declarados por año y contrastados, o bien llevar las series al universo de `verificacion_entradas.py`, que ya comprueba ejercicio, columna y perímetro.

### V631-3 · media · La aptitud por entradas y la huella de entradas no ven el perímetro ni las series

**Evidencia:**
- En un libro V6.3.1 de Elis con A1, `VE.universo` tiene 292 celdas y **ninguna de las filas 85–87 de la Historia**.
- `entradas_economicas.instantanea` da **la misma huella** para el libro A1 y para el A2, que tienen valoraciones distintas. La razón es que la relación de entradas materiales es la de la V6.3 (`v6/scripts/relacion_entradas_materiales.py`).

**Consecuencias:**
- Con una verificación de entradas completa, la ficha diría «apto por entradas: sí» aunque las cifras que mueven f, unos 139 en el flujo sin crecimiento de Elis, estén sin verificar (punto 6 de CLAUDE.md).
- El registro de la verificación de entradas seguiría vigente al pasar de A1 a A2.
- La retirada de la aprobación del cierre no depende de esto: `motor_a_f1.json` está en `MATERIAL_FIJO`.

El autor lo declara fuera de alcance (§8.4). Para el examen no basta con declararlo.

**Corrección:** con un libro V6.3.1 y perímetro distinto de A0, `apto_por_entradas = false`, con su motivo, hasta que C85:L87 entren en la relación de entradas materiales y en la huella.

### V631-4 · baja (del lado seguro) · Con `A0_total`, el veredicto F1 de la V6.3.1 no es el de la V6.3

**Evidencia** (`ataques2.py`, E7 y E7b de `ataques.py`). En el libro de Elis vacío el capex de 2021, que está fuera de la ventana de f:
- la V6.3.1 con A0 calcula C53 = 6,329 (la rama A0 admite tres años o más, como la V6.3);
- la capa calcula el ancla con los cinco años de **todos** los perímetros, así que da vacío;
- resultado: `F1-LIBRO` bloquea («C53 6,329 ≠ capa None»). Con el libro V6.3 no bloquea.

Las celdas del libro son idénticas, pero el oráculo no lo es.

**Corrección:** para A0, contrastar C53 solo si la capa lo calcula (como ya hace `F1-REPLICA`), o reproducir la regla de la V6.3. Si no se corrige, declararlo.

### V631-5 · baja · Ancla con A1/A2: «vacío no es cero» solo vale para D_X

**Evidencia** (E2). En el libro de Elis con A1 vacío las adquisiciones y el circulante de 2021, que están fuera de la ventana:
- la fila 31 (con `N()`) y la capa (`or Fr(0)`) los cuentan como 0;
- C53 pasa de 2,445 a **2,699**, con V05 OK y sin ninguna guarda.

Viene de la V6.3. Pero si E4 se lee con los cinco años H–L, la exigencia debe alcanzar a todos los términos del denominador.

**Corrección:** con A1/A2, que C53 exija las filas 12, 13, 14 y 88 numéricas en H–L (0 explícito si no hubo), en el libro y en la capa.

### V631-6 · baja (límite) · El oráculo contrasta valores en caché, no fórmulas

**Evidencia** (E3e). Tomo un libro V6.3 (fórmulas A0) y le copio en caché las filas 30–31 y 84–89, C53, C58, C76 y los 33 flujos de un libro A1: `F1-LIBRO` y `F1-REPLICA` no saltan.

- **En el pipeline está cubierto:** recálculo forzado del libro evaluado y `verificar_v631.py` dentro de `verificar_todo.sh` en el paso 12, antes de la evaluación F1 que cuenta.
- **No está cubierto** si se usa `motor_a_f1.py evaluar` a mano sobre un libro de origen desconocido.

**Corrección** (barata): que `F1-LIBRO` exija que `--libro-origen` pase `verificar_v631.py` frente a su referencia. Si no, declararlo.

### V631-7 · menor · Rótulos de la conciliación

Historia A30 y A76 siguen diciendo «capex − D&A + circulante». Con A1/A2 es capex − D_X, y E3 pide que la conciliación muestre la D_X media y sus componentes. La D_X media solo está dentro de C76.

**Corrección:** rótulo condicional o nota en A90.

### V631-8 · menor · Pruebas y registros

- La comprobación P6 de `prueba_pipeline_v631.py` acepta cualquier estado no nulo, aunque el README dice `concluido`. Yo obtuve `concluido`, pero la prueba no lo exige.
- En el control 2, la ficha `no_entregable` conserva el rótulo F1 «utilizable» de la evaluación anterior.
- `test_v631_f1.py`, `probar_v631_f1.py` y `prueba_pipeline_v631.py` no están en `verificar_paquete.sh` (el autor lo declara).

## Comprobaciones pedidas

### 1 · No regresión

- **La V6.3 no cambia.** `Plantilla_V6.3.xlsx` tiene la huella `8381a6cd7b1d…`, igual que su referencia, el manifiesto e `IDENTIFICACION_V6_3.txt`. El diff `24e9a30..4928fc9` no toca `v6/` fuera de `v631_f1/`.
- **La reconstrucción es determinista.** `construir_v631_f1.py` desde la V6.3 da `266d53bdd8af…`, la huella del entregable.
- **El diff de fórmulas (comparador propio) son exactamente las celdas declaradas.** Son 42 celdas:
  - fila 30;
  - C53, C58 y C76;
  - la sección A84:A90, con C88:L89;
  - Motor E205;
  - cuatro etiquetas.

  En C53, C58 y C76 la rama A0 es literalmente la fórmula de la V6.3. La rama A1/A2 de C58 es la de la V6.3 más la guarda de C88 vacía y la reinversión de la fila 30. Fila 31 sin cambios.
- **Comparación de celdas por una vía distinta de la del autor.** Apliqué el guion de construcción al libro ya relleno, sin traslado de entradas, y comparé con el libro V6.3 original recalculado (comparador propio, todas las hojas, tolerancia 0, excluidas las 4 etiquetas y las filas 84–90).

  | Libro | Celdas | Perímetro vacío | `A0_total` |
  |---|---|---|---|
  | Elis | 39.751 | 0 distintas | 0 distintas |
  | Empresa X | 39.751 | 0 distintas | 0 distintas |
  | ABB | 39.751 | 0 distintas | 0 distintas |
  | Hermès | 39.751 | 0 distintas | 0 distintas |

  Los orígenes no cambian. El matiz de A0 en la capa está en V631-4.

### 2 · Corrección del valor

Mi cálculo independiente (`indep_elis.py`) parte de la Historia del libro V6.3 de Elis y de las series del frente E, con fracciones exactas. Los flujos A1/A2 salen de los flujos A0 del libro sumando V_t·(f_A0 − f_p), y el año 11 de V₁₀·(1+g)·(f_A0 − f_p).

| | f (revisor) | E9 | C53 (revisor) | E9 | Año 11 MALO / NORMAL / BUENO |
|---|---|---|---|---|---|
| A1 | 0,012624225323284527 | 0,012624225323285 | 2,4453316953316953 | 2,445331695332 | 294,942490 / 413,845195 / 488,862108 |
| A2 | −0,006118601744164796 | −0,006118601744165 | 1,6125243033052494 | 1,612524303305 | 402,413238 / 546,310848 / 633,271007 |

- Los 33 flujos coinciden con E9 a 1,0·10⁻¹².
- El año 11 NORMAL, A1 − A0, es 205,363093.
- El libro V6.3.1 recalculado con LibreOffice difiere de mi cálculo en 7·10⁻¹⁷ en f, 5·10⁻¹⁵ en C53 y 8·10⁻¹³ en el año 11. Conciliación «✓ cuadra» y V05 OK.
- **Las fórmulas siguen la especificación:**
  - fila D_X: E2;
  - filas 30/31 y C58: E3, misma ventana y mismas guardas, con D_X en vez de la D&A;
  - C53: E4 sin X^v, que solo aparece con términos explícitos, y esos siguen bloqueados;
  - E205: tres causas nuevas que solo saltan con A1/A2 o con un texto no reconocido.
- **Casos en que libro y capa coinciden y los dos están mal:** V631-2 (E1, la cifra de otro ejercicio) y V631-5 (E2, el vacío que cuenta como 0 en el ancla). Hay un tercero que no probé con libro: si la fila 8 ya excluye la D&A de derechos de uso, A1 la resta dos veces. E205 solo lo detecta si D_X queda negativa, porque los dos comparten las mismas entradas.

### 3 · El oráculo

| Ataque | Resultado |
|---|---|
| Libro A1, declaración A2 (otro perímetro) | **Bloquea** (perímetro efectivo, D_X, f) |
| Serie de la declaración +0,1 después de aplicar (caché que ya no corresponde) | **Bloquea** (serie, D_X, f) |
| D_X manipulada en 2016, fuera de la ventana y del horizonte | **Bloquea** (`F1-LIBRO` y `F1-REPLICA`) |
| D_X de 2025 + 10⁻⁶ | **Bloquea** |
| Libro V6.3 con la sección 84–89 de un libro A1 en caché | **Bloquea** |
| Libro aplicado y sin recalcular | `ErrorDeclaracion` → el pipeline da `no_entregable` |
| Sin perímetro declarado y libro con C85 = A1 | Bloquea `F1-PERIMETRO` (`F1-LIBRO` no salta porque `per` está vacío) |
| Libro V6.3 con **todas** las salidas contrastadas copiadas de un libro A1 | **No bloquea** → V631-6 (lo cubre el pipeline) |
| Ejercicio o columna equivocados en las series; vacíos del ancla | **No bloquea** → V631-2 y V631-5 |

### 4 · Seguridad

- Dentro del pipeline, el único camino que encontré a `concluido` con arrendamientos sin que libro y capa coincidan es **R2-1** (V631-1).
- Cerrados:
  - `--desde 7` con la declaración cambiada (P8 del autor);
  - `--desde 13` sin `--reiniciar` (mi control 1);
  - `--reiniciar --desde 13` conservando el resultado (control 2).
- Una configuración económica con la V6.3.1 se rechaza.
- Un expediente V6.3 empezado no se ejecuta con la V6.3.1, ni al revés (pruebas del autor; leí `comprobar`).
- Si se borra `plantilla_activa.json` y se lanza con la V6.3, el libro V6.3.1 no pasa el verificador de la V6.3 en el paso 12.

### 5 · Las dos preguntas del autor

**(a) E4 con cinco años H–L: sí, es la lectura correcta.**
- E4 define C53 como la suma de H a L, sin mínimo.
- La regla «≥ 3» de la V6.3 divide el ΔV de cinco años entre la reinversión de tres o cuatro, lo que sobrevalora S2C.
- La referencia E9 depende de las entradas de 2021–2025.

Hay que ser coherente en dos cosas:
- la misma exigencia para todos los términos del denominador (V631-5);
- la rama A0, que debe seguir siendo la de la V6.3, no debe hacer bloquear al oráculo por esa diferencia (V631-4).

**(b) `F1-SERIES` como condición mínima: no basta tal como está** (V631-2 y V631-3). Basta como condición mínima del examen supervisado si se cumple todo esto:
- búsqueda por token;
- fuente dentro del expediente, con huella y ligada a `documento`;
- aptitud por entradas en «no» mientras las series estén fuera del universo;
- contraste humano registrado de ejercicio, columna y página de cada año de la D&A de derechos de uso y de la PPA.

La PPA declarada a cero sigue sin contraste en la Historia (§8.3 del autor).

### 6 · H10, H11 y H12

- **H10: cerrado.** Las compras con importes exigen los años 1–10 y el 11, o la proporción. Con el ancla que los excluye, los importes históricos H–L. La transición como término exige sus importes históricos y que el ancla la excluya. El año 11 cobra el importe declarado. Las pruebas REV2 pasan. Los términos siguen bloqueados por `F1-LIBRO`.
- **H11: cerrado en su alcance.** `F1-C49`, `F1-ROU-HISTORIA` y registro de «sin transición conocida». Queda sin hacer el registro de la normalización, pero N1 sigue bloqueado por `F1-PARAM`.
- **H12: mitigado, no cerrado** (V631-2 y V631-3).

### 7 · Pruebas ejecutadas en copias

| Orden | Resultado |
|---|---|
| `python3 -B pruebas/test_v631_f1.py` | `21/21 pruebas V6.3.1 F1 (sin LibreOffice) PASAN` |
| `python3 -B pruebas/test_motor_a_f1.py` | `155/155 pruebas del motor A F1 (4.15) PASAN` |
| `python3 -I probar_v631_f1.py estructura` | `21/21 … (estructura) PASAN` |
| `flock … probar_v631_f1.py a0` | `22/22 comprobaciones V6.3.1 F1 (a0) PASAN` |
| `flock … probar_v631_f1.py f1` | `32/32 comprobaciones V6.3.1 F1 (f1) PASAN` |
| `flock … prueba_pipeline_v631.py` | `6/6 pruebas de la V6.3.1 F1 en el pipeline PASAN` (`evidencia/pruebas_autor.txt`) |
| Mis guiones (`libros.py`, `ataques.py`, `ataques2.py`, `pipe_r21*.py`) | los resultados de arriba |

No repetí `verificar_paquete.sh completa`: no vi motivo, porque el cambio no toca el resto de baterías salvo `test_motor_a_f1.py`, que sí ejecuté.

**No comprobé:**
- Excel real (todo el recálculo es LibreOffice);
- `regresion_elis_f1.py`;
- el tercer caso de V631-2 (fila 8 sin la D&A de derechos de uso) con libro.
