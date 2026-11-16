# Respuesta a la revisión externa M2 · Frente C · commit de revisión `9366bdd`

**Declaración:** Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación por el integrador. Rama `mistral/m2-matematica-b` (mantenida; la rama de revisión no se fusionó). Escritura solo en `resultados_m2/matematica_b/`. Sin LibreOffice, pipeline, macros, PR, fusión ni autoaprobación.

Revisado: `revision_externa/m2/REVISION_CHATGPT_M2.md` y `revision_externa/m2/CORRECCION_C.md` leídos con `git show 9366bdd…:ruta` (y `SONDA_C_D7_CAJA.json`). Mi entrega revisada era `fe46f0761cb0590a280907b42e4605f6d3fec845`.

## C1 · La comparación de D7 es la de perímetro Caja — corregida

1. **Se retira la afirmación de «discrepancia no reproducible de 0,0092 €»** de todos los informes (dossier, hallazgos, resumen, recuperación). El problema era de identificación de la comparación (mezcla de perímetros), no del oráculo: mi comparación activa NIIF 16 (+1,5477811279 €) no refuta el cambio Caja (+1,5386459068 €) porque responden a preguntas distintas.
2. **Caso añadido con huella y procedencia:** H6 = Viscofan 4.13 variante `perimetro_alternativo` (Caja), vector `[30.6406803941772, 44.8547080140724, 59.2982622162535]` verificado en la fuente `personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_13/viscofan/Viscofan/configuracion_v64_variantes.json` (sha256 `c8e7270f8b174172…913d2`, el mismo que registra la revisión en `SONDA_C_D7_CAJA.json`), `precio_si` publicado 40,82634677728604. Universo: 56 → **57 casos** (no se mantuvo 56 artificialmente).
3. **Tabla 2×2 Caja recalculada con el oráculo propio desde las fuentes** (H5 Caja 4.12 vs H6 Caja 4.13; p 4.12 = [0,25, 0,60, 0,15], p referencia = [0,20, 0,60, 0,20], k = 3), contrastada con `SONDA_C_D7_CAJA.json`:

   | Celda Caja | p 4.12 | p referencia | esperado revisión | residuo |
   |---|---:|---:|---:|---:|
   | V Caja 4.12 · p412 | 39,2877008705048 | | 39,2877008705048 | ≤ 1e-12 |
   | V Caja 4.12 · pref | | 40,94819933093843 | 40,94819933093843 | ≤ 1e-12 |
   | V Caja 4.13 · p412 | 39,19204962434291 | | 39,19204962434291 | ≤ 1e-12 |
   | V Caja 4.13 · pref | | 40,82634677728604 | 40,82634677728604 | ≤ 1e-12 |

   - Cambio total Caja 4.12→4.13: **+1,538645906781241 € → +1,5386 € como D7. COINCIDE.**
   - Efecto de p según orden: **+1,6604984604336295** (sobre V 4.12) o **+1,6342971529431338** € (sobre V 4.13); Shapley +1,6473978067 €. Efecto de V: −0,0956512462 € o −0,1218525537 € según orden. Todos coinciden con la sonda al 1e-12.
   - La tabla NIIF 16 (activa, H4→H3) se conserva aparte con su etiqueta (+1,5477811279 €; efecto p Shapley +1,6412 €; efecto V −0,0934 €), etiquetada por fecha, perímetro, variante, V y p en cada fila de `EFECTOS_PROBABILIDADES.csv`.
4. **Comprobación añadida contra comparaciones cruzadas de perímetro:** `efectos_probabilidades.py` ahora etiqueta cada fila con `perimetro` y calcula `misma_pregunta`; todo «cambio total entre entregas» se comprueba dentro de un mismo (empresa, perímetro) y mezclarlos queda marcado `PREGUNTA_DISTINTA` (la fila de control informa OK/FALLA). Resultado ejecutado: **guarda OK** (ningún cambio total mezcla perímetros; la fila 5 documenta que NIIF16 vs Caja son preguntas distintas).
5. Archivos regenerados: `casos_fijados.json` (57), `resultados_casos.json` (57 filas, 10/10 propiedades), `COMPARACION_IMPLEMENTACION.csv` (57 filas, residuo máx vs producto 2,842e-14), `EFECTOS_PROBABILIDADES.csv` (30 filas con perímetros y guardas), `SENSIBILIDAD_FINITA.csv` (192, sin cambios de rejilla), `PROTOCOLOS_COBERTURA.csv` (cobertura 24/24), `DOSSIER_D1_D7_D11.md`, `HALLAZGOS.md`, `RESUMEN_PARA_CLAUDE.md`, `INVENTARIO_Y_PLAN.md`, `COMANDOS.md`, `MANIFIESTO_SHA256.txt`, `PUNTO_DE_RECUPERACION.md`.

## Hallazgo sobre `p_estrella` interna — matizado como indica la revisión

La llamada directa a `p_estrella` con p fuera de contrato devuelve un número sin negarse, pero la **vía pública `calcular()` rechaza el caso ensayado** («probabilidades inválidas»). Se documentan las precondiciones del contrato (p distribución con |Σp−1| ≤ 1e-3, k ≥ 1, n = 3, B78 ≤ C78 ≤ D78, precio > 0) en `COMPARACION_IMPLEMENTACION.csv`/`HALLAZGOS.md`; **no se declara un fallo material de producción** sin una vía pública reproducible. El oráculo propio valida en la propia función (`DominioError`). No se modifica el producto ni se amplía la corrección a sus guardas.

## Comprobaciones realmente ejecutadas (tras la corrección)

```
python3 codigo/oraculo_precio_si.py --selftest     # PASA
python3 codigo/generar_casos_fijados.py            # 57 casos
python3 codigo/ejecutar_casos.py                   # exit 0; 10/10 propiedades; res. máx vs paquete 1,4e-14
python3 codigo/comparar_producto.py                # 57 filas; res. máx oráculo-vs-producto 2,842e-14
python3 codigo/efectos_probabilidades.py            # 30 filas; total Caja +1,538645906781241 €; guarda OK
python3 codigo/sensibilidad_finita.py              # 192 filas
python3 codigo/protocolos_cobertura.py             # 58 filas; cobertura coincide 24/24
```

## Límites pendientes

- D1, D7 y D11 siguen siendo **decisiones/políticas pendientes**: no se adopta k, probabilidades ni protocolo; no se usan los precios históricos (90,10 € / 54,70 €) como objetivos vigentes.
- La «variante probabilidades de referencia» (opción 2 de D7) sigue sin estar calculada por el producto en el rango de variantes; aquí solo se da su valor exacto con el oráculo (precio_si = f(V, p, k, V_N)).
- La guarda de perímetros es de este auxiliar; extenderla al producto sería una propuesta separada de software.
- Sigue pendiente la revisión del integrador sobre el commit congelado de esta rama; no se abren ciclos recursivos.

Modelo: `mistral-large-4-0` (Vibe Code de Mistral AI). Consumo no visible desde la sesión.
