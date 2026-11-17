# Revisión de la respuesta A2 (`8b88fab`) · procedencia

- **Autoría:** el informe y las sondas los hizo un contexto distinto del autor (un subagente del coordinador), sin red y sin LibreOffice.
- **Rutas:** las rutas locales se sustituyen por `<rev_A2>`, `<rev_A>`, `<zip>`, `<repo_auxiliar>` y `<home>`. Por eso las salidas `.out` y `.json` no coinciden byte a byte con las de la ejecución original. Las huellas del manifiesto son las de estos archivos.
- **No se versionan** la entrega extraída ni la copia de reproducción con los insumos: salen del ZIP base-4.14 con la sonda `s00`.
- **Comprobación del coordinador:** `normalize_num` y la comparación de columna en `verificar_contexto.py` @ `8b88fab` (`:130` y `:438`).
