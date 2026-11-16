# Revisión de F @ 223f16d (B-PM1) y 52fb120 (F-B3/F-C1) · procedencia

- **Autoría:** el informe y las sondas los hizo un contexto distinto del autor (un subagente del coordinador, sin red). Hay un límite de independencia, declarado en el informe: el revisor y el coordinador que registra la aceptación son ambos Claude.
- **Rutas:** las rutas locales se sustituyen por `<rev_F>`, `<zip>`, `<base414>`, `<repo_auxiliar>` y `<home>`. Por eso algunas salidas no coinciden byte a byte con las de la ejecución original.
- **Listados omitidos:** no se versionan los dos listados completos del ZIP (`sondas/inventario/listado_unzip_*.txt`, ≈2 MB). Se reproducen con `unzip -l <zip>` y `unzip -Z1 <zip>`.
- **Comprobación del coordinador (D3):** `sondas/sonda4_out.txt` lee las definiciones del producto (Palancas X14 = crecimiento de los años 1–5, X15 = ROE objetivo en C, X18 = rentabilidad terminal; g∞ en Análisis B68) y las fórmulas de `test_fill`.
