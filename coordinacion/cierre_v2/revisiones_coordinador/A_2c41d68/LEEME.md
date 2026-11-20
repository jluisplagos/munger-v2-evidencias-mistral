# Revisión del frente A @ 2c41d68 · procedencia

- **Informe y sondas:** hechos por un contexto distinto del autor (un subagente del coordinador). Se copian sin cambios, salvo una cosa: las rutas locales del entorno de revisión se sustituyen por `<rev_A>`, `<descargas>` y `<home>`. Por eso los `.out` y `.json` no coinciden byte a byte con los de la ejecución original. Las huellas de esta carpeta son las de los archivos copiados.
- **Insumos:** las sondas `s00`/`s01` reconstruyen los insumos desde el ZIP de la Release base-4.14 (`bb51942c…b7b93e`). Ese ZIP no se versiona aquí.
- **Comprobación del coordinador:** que `check_columna` (`verificar_contexto.py`) devuelve OK sin mapeo por posición (sus dos últimas salidas) y que la sonda 2a da OK en `s02_sondas_revisor_A.out`.
