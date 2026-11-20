# Pruebas de la candidata `integracion/candidata-cierre-v2` @ 957af65

- **Autor:** el coordinador (Claude). Son pruebas del autor de la candidata, no una revisión independiente.
- **Entorno:** Python 3.13.18, LibreOffice 24.2.7.2, pdftotext 24.02.0 y openpyxl 3.1.5. LibreOffice se usó con exclusión mutua (`flock -x` sobre un único archivo de bloqueo).

## 1. Materialización

Se siguió el procedimiento de la preparación del frente E (README del producto, sección de archivos pesados), sin ejecutar `tools/base_414.py` sobre el código 4.15:
- La base 4.14 se materializó y se verificó en un worktree aparte de `main` (`base_414.py materialize` y `verify`: 6798/6798, `complete:true`; ZIP de la Release `bb51942c…b97b93e`).
- Desde allí se copiaron al worktree de la candidata los 1008 binarios `release_asset`, sin sobrescribir ninguno (`copia_binarios_candidata.json`: 1008 copiados, 0 existentes, 0 distintos y 0 fallos tras la copia).
- **Manifiesto propio de la candidata** (`munger_v2_r1/MANIFIESTO_SHA256.txt`): 7762/7762 OK, 0 ausentes y 0 archivos fuera del manifiesto.
- `git status` muestra 83 JSON sin seguimiento. Son binarios de la 4.14 que el `.gitignore` no cubre. Están en el manifiesto y no se versionan.

## 2. Verificación completa

Se ejecutó sobre una copia aparte del árbol materializado, porque las pruebas escriben dentro de él.

| Paso | Comando | Resultado | Registro |
|---|---|---|---|
| Primer intento | `bash verificar_paquete.sh completa` | Interrumpido por un reinicio del contenedor durante `test_integracion_v64.py`. Todo lo anterior pasa. No se reutilizó la carpeta | `verificar_paquete_completa_interrumpido.log` |
| Segundo intento, en una copia nueva (22:18–23:18 UTC) | `flock -x … bash verificar_paquete.sh completa` | **Código 0. RESULTADO GLOBAL: PASA.**<br>- Manifiesto, entorno y piloto: PASA.<br>- 114/114 y 30/30.<br>- 59/59, 27/27 y 33/33.<br>- 190/190, 62/62 y 5/5.<br>- 199/199, 78/78 y 103/103.<br>- 55/55, 28/28, 45/45 y 55/55 | `verificar_paquete_completa.log` |
| Control 4.14 sobre la misma copia, después | `python3 -I -B …/comprobar_entrega_4_14.py` | Código 1. **29/35**, lo esperado sobre un clon Git (CONTINUIDAD.md §2.3). Las 6 FALLA son las documentadas:<br>- las 3 verificaciones de entradas de los expedientes finales de la 4.14, «no apto por entradas» por diseño con las reglas de la 4.15;<br>- las 3 fechas de archivo que Git no conserva | `comprobar_entrega_4_14.log` |

**No se han ejecutado** los controles de las entregas anteriores a la 4.14 (`LEEME_CONTROLES_HISTORICOS_4_14.md`).

**Límite:** que pasen los controles de software no da aptitud económica ni para dinero real.
