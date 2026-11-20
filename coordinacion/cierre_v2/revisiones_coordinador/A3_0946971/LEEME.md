# Procedencia

- **Autoría:** el informe y las sondas los hizo un contexto distinto del autor (un subagente del coordinador), sin red ni LibreOffice.
- **Límite de independencia:** el revisor y el coordinador son los dos Claude.
- **Rutas:** las locales se sustituyen por `<rev_A3>`, `<rev_A2>`, `<zip>`, `<repo>` y `<home>`, así que algunas salidas no coinciden byte a byte con las de la ejecución original.
- **`sondas/s12_pypdf.out`:** recortado. Se conservan el principio y el final, que llevan el mensaje relevante; el resto son avisos repetidos de pypdf sobre fuentes.
- **No se versionan** las copias de trabajo (`entrega/`, `repro/`, `commits/`, `r7neg/`). Se reproducen con `s00`/`s01` desde el ZIP base-4.14.
