# Encargo para Mistral · Zoetis, segundo tiempo · los doce últimos meses hasta el 30-sep-2026

**Para pegar en una ventana nueva de Mistral.** Fecha: 19-nov-2026. Encarga: el coordinador Claude. Revisa: un agente Claude distinto. Reglas de `AGENTS.md`; **no valorar ni recomendar**.

## 1. Para qué sirve

El segundo tiempo de Zoetis añade lo publicado el 5-nov-2026. Ya entregaste las cifras del T3 (`mistral/examen-zoetis-t2`, `resultados_examen/zoetis_t2/CIFRAS_T3.csv`). Ahora necesito **las cifras de los doce últimos meses (LTM) hasta el 30-sep-2026**, calculadas con las cifras impresas: LTM = ejercicio 2025 (10-K 2025) + nueve meses 2026 − nueve meses 2025 (10-Q T3 2026).

## 2. Qué calculas (cada una con la cuenta y la página de cada componente)

Ventas; beneficio antes de impuestos; gasto por intereses; **EBIT = beneficio antes de impuestos + gasto por intereses** (en los 10-K de Zoetis el gasto por intereses se imprime en positivo dentro de «Costs and expenses»); D&A (las dos líneas que publica, sin sumarlas dos veces); EBITDA; CFO; capex; FCF (CFO − capex); intereses pagados si se publican; beneficio neto atribuible; y, al 30-sep-2026: caja, deuda financiera (corto y largo), pasivos por arrendamiento operativo y financiero por separado, patrimonio, minoritarios (si salen negativos, dilo: la regla del producto los guarda como 0 con aviso), acciones en circulación de la portada del 10-Q. Ojo con la «Fiscal Year Alignment» (nota 2 del 10-Q): los nueve meses de 2025 del 10-Q T3 están reexpresados; dilo en cada cifra que lo use y no mezcles bases sin avisar.

## 3. Qué entregas

En tu rama `mistral/examen-zoetis-t2` (la misma de antes), carpeta `resultados_examen/zoetis_t2/`: `LTM_3T.csv` con `partida, valor_ltm, unidad, cuenta (componentes con su valor), archivos, paginas, citas_literales, nota_base (reexpresada/as previously reported)`, y una sección nueva en `ENTREGA.md`. Commit y push.

---

### Frase para pegar

> Lee `coordinacion/cierre_v2/examen/zoetis/ENCARGO_MISTRAL_ZOETIS_T2_LTM.md` en la rama `coordinacion/cierre-v2` del repositorio `jluisplagos/munger-v2-evidencias-mistral` y hazlo entero. Entrega en la rama `mistral/examen-zoetis-t2`.
