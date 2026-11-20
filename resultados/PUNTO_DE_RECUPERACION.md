# Punto de recuperación · frente M · rama mistral/fuentes-vm-01

Evidencia propuesta por Mistral; pendiente de revisión e incorporación por el integrador.

## Estado actual

- Repositorio auxiliar: `jluisplagos/munger-v2-evidencias-mistral` (origin verificado). Rama `mistral/fuentes-vm-01` **publicada** en origin. Base: `main` @ `e137b854dc592bcad9ed3e51275f7b80d35d210e`.
- Insumos: `preparar_insumos.py --download` ejecutado; ZIP base-4.14 (1.130.912.246 bytes, sha256 `bb51942c…b7b93e` verificado) y 15 insumos en `.trabajo/insumos/` con sha256 conformes. Selección parcial (`producto_completo_verificado: false`).
- Asociaciones texto↔PDF verificadas (pypdf, 100% tokens numéricos por página) y verificación visual con PyMuPDF en EN2025 p.52 y ES2025 p.14.

## Terminado

- Bloque 1 (commit `5641bec`): primera lectura de 16 entradas antes del contraste; hash `5571ee7f…90f51`.
- Bloque 2 (commit `b278727`): 60 entradas en total; hash bloque 2 `8a7a518f…29c2c`.
- Entrega (commit `6b53ef9`, publicado): 26 filas en `contraste_objetivos.csv` — 23 `COINCIDE_EN_REVISION_MISTRAL`, 3 `HIPOTESIS_O_AUSENCIA` (Vidrala C48/C49/C50); `comprobar_entrega.py` → estructura PASA.
- **Correcciones dirigidas tras la revisión externa de `6b53ef9`** (commit superior en la misma rama, publicado): C49 `valor_leido` 20.492→**20.292** miles y medias recalculadas (pago total 6.764 mm; interés devengado 2.254 mm; diferencia 4.510 mm) sin atribuir diferencia al registro y manteniendo C49 como hipótesis; L7 (EBIT 292.068 **incluye** deterioro 2.362; sin él 294.430; L8 sí lo excluye); L14 («−799 miles = −0,799 millones»); C55 de Vidrala sin atribución a D3 (D3 es de Viscofan); recuperación y resumen actualizados. Hash de `lectura_fuentes.jsonl` tras correcciones: `3d81d01b…fdf42f`. La primera lectura se conserva en el historial (`5641bec`/`b278727`); la auditoría aritmética determinista pasa sin problemas.
- Push verificado: `git ls-remote origin mistral/fuentes-vm-01` coincide con el HEAD local.

## Pendiente / siguiente acción exacta

1. Revisión externa (integrador/Claude) de citas, datos, derivaciones y compatibilidad antes de incorporar cualquier parte de `resultados/`.
2. Nada más en este frente: no ampliar alcance, no PR, no fusión, no tocar el producto ni el trabajo de Claude.

## Modelo y limitaciones

- Sesión: Vibe Code de Mistral AI, modelo `mistral-large-4-0` (único modelo expuesto; sin nivel de esfuerzo porque la interfaz no lo ofrece). Herramientas deterministas: Python stdlib + pypdf 7.1.0 + openpyxl 3.1.5 + PyMuPDF (pip en el sandbox) para huellas, extracción, verificación visual y aritmética.
- Consumo/facturación: no visible desde la sesión; se declara que no se está limitando ni se afirma límite. El **presupuesto de 25 EUR es una recomendación del encargo**; no se ha podido comprobar desde la sesión que esté configurado externamente.
- Red: disponible para GitHub (descarga de release verificada con urllib; `curl` bloqueado por el sandbox). Sin LibreOffice ni pipeline (prohibidos). PDF/XLSX/ZIP fuera de Git (`.trabajo/` excluido).
- No se abrió PR, no hay fusión, no se modificó `munger-v2` ni sus ramas/PR/issues.

## Cierre de la revisión externa

Sobre la corrección de Mistral `44641ff`, ChatGPT retiró únicamente dos menciones residuales a «4,510333»; la media de la diferencia es exactamente **4,510 millones** con los operandos citados. No cambia ningún objetivo, hipótesis, libro ni decisión. Hash actual de `lectura_fuentes.jsonl`: `24ea73e46b953051a1299cf737218d8173ee97bf1558fe50434ad49054482bd0`. Véase `revision_externa/REVISION_CHATGPT_2.md` para alcance y límites de la comprobación.
