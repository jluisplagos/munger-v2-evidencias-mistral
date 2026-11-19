# Encargo para Mistral · M7 · Contraste independiente de las cifras que cambió la orquestación

**Para pegar en una ventana nueva de Mistral.** Fecha: 19-nov-2026. Encarga: el coordinador Claude. Revisa: un agente Claude distinto. Lee antes `AGENTS.md` del repositorio auxiliar y cumple sus reglas (no escribir en `jluisplagos/munger-v2`, no subir PDF/XLSX a Git, no aprobar tu propio trabajo, **no valorar ni recomendar**).

## 1. Para qué sirve

Hoy la orquestación (agentes Claude) ha cambiado muchas cifras de entrada en cuatro expedientes del examen. Un revisor Claude ya las ha examinado, pero quiero **una segunda lectura de otra familia de modelos**: tú compruebas cada cifra cambiada directamente en el texto de su fuente, sin fiarte de lo que dice el expediente.

## 2. Dónde está

Repo `jluisplagos/munger-v2`, rama **`examen/expedientes-f1`** (solo lectura), carpeta `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_examen_universo/`. Para cada expediente, la lista de cambios está en su carpeta `resultados/` y los textos de las fuentes en `<Empresa>/texto/` (marcas `[PDF PAGE n]`):

| Expediente | Archivos de cambios en `resultados/` |
|---|---|
| `ahold_f4/Ahold` | `registro_cambios_ahold_f4.json`, `registro_correcciones_revision_ahold_f4.json`, `fuentes_mercado_ahold_f4.json` |
| `jumbo_g/Jumbo` | `registro_cambios_jumbo_g.json`, `registro_tras_sellado_jumbo_g.json`, `fuentes_mercado_y_registro_jumbo_g.json`, y `Jumbo/recalculo_dependientes.json` |
| `zoetis_t1d/Zoetis` | `registro_cambios*` y `vigencia_extracto_t1d.json` (y los demás `*.json` de esa carpeta que listen cambios) |
| `vinci/Vinci` | `correcciones_revision_montaje.json`, `declaracion_f1_vinci.json` |

## 3. Qué haces

Para **cada cifra cambiada** (valor nuevo con su fuente y página): ábrela en `texto/`, busca la línea y comprueba el número impreso, la columna/año, la unidad, el signo y, si es un cálculo, rehaz la cuenta con las cifras impresas. Atención especial a: los doce meses hasta el 3T 2026 de Ahold (C24, C33, C40, C42, C53, C54; LTM = ejercicio 2025 + 39 semanas de 2026 − 39 semanas de 2025), el recálculo de C46/C40 de Jumbo con C76 = 150, el EBIT de Zoetis (beneficio antes de impuestos + gasto por intereses), las acciones exactas de Zoetis (424.927.535) y las series de Vinci.

## 4. Qué entregas

Rama nueva **`mistral/m7-contraste`**, carpeta `resultados_examen/m7_contraste/`: `CONTRASTE.csv` con `expediente, celda, valor_expediente, valor_que_encuentras, archivo, pagina, cita_literal, coincide (si/no/no_se_encuentra), nota`, y `ENTREGA.md` (máximo una página) con el recuento y cada «no» explicado. Commit y push por expediente.

---

### Frase para pegar

> Lee `coordinacion/cierre_v2/examen/mistral_m7/ENCARGO_MISTRAL_M7_CONTRASTE.md` en la rama `coordinacion/cierre-v2` del repositorio `jluisplagos/munger-v2-evidencias-mistral` y hazlo entero. Entrega en la rama `mistral/m7-contraste`.
