# Mejoras pendientes del manual operativo (de T-TRASPASO y de su revisión, 17-nov-2026)

Por prioridad. Se aplicarán en una revisión del manual (G-MANUAL) y, en lo que afecte a documentos del producto, en una corrección documental de la candidata con su propia revisión. **No se aplican aquí.**

1. **Disco.**
   - Fijar el espacio necesario por la vía del repositorio.
   - Poner la limpieza de `pruebas/_v64/` en el paso 10, antes del control 4.8.1.
   - Corregir CONTINUIDAD §2.5, que dice que los controles no recorren `_v64/`. El 4.8.1 lo copia (`comprobar_entrega_4_8_1.py:76-77`) y por eso se quedó sin espacio.
2. **Pasos 12–14.**
   - Avisar de que `elis_motor_A` ya está caducado: el primer relanzamiento hace también la detección del relevo.
   - En el paso 13, cambiar un archivo del material que el paso 12 no regenere.
   - En H9, cambiar una salida que se vuelque en celdas: `fase_c.json`, `fase_b.json` o `entrada_efectiva.json`. Con `fase_c.md` no se distingue el caso que importa.
   - Dar el comando completo, con `--config personaje_v2/config_v2.json`.
3. **Controles históricos sobre el árbol 4.15: escribir el resultado esperado.**
   - **4.10 da 39/44** por un cambio documental de la 4.15: el control exige `.PARTES.txt` en `PROMPT_NUEVA_VENTANA.md` (`comprobar_entrega_4_10.py:181-182`). La cadena está en la 4.14 (`origin/main`), no en `957af65`. Lo comprobó el coordinador.
   - **4.11 da 33/38** por el entorno: la huella del ZIP reconstruido depende de la compresión, y `v6/` no cambia entre la 4.14 y `957af65` (comprobado). El control 4.12 compara miembro a miembro y CUMPLE. Queda por cerrar: la versión de zlib y `comparar_zip.py` sobre esa reconstrucción.
   - Dar el comando y una carpeta de salida fuera del árbol verificado.
4. **Bloqueo de LibreOffice:** una sola ruta y el comando `flock -x` completo, también para `soffice --version`.
5. **Registro del receptor:** exigir para cada paso el comando, el código y la hora; `df` antes de los bloques largos; los scripts improvisados; las huellas antes y después del paso 12.
6. **Comandos que faltan** (N-01, N-02, N-03, N-11): clonado, copia de los binarios, copia limpia y contraste del manifiesto. Puede servir de base `../resultado_20261117/scripts_receptor/copiar_binarios.py`, una vez revisado.
7. **Referencias y detalles:**
   - las citas al repositorio de evidencias, a la rama vigente;
   - si manda `AGENTS.md` o `PROMPT_RECEPTOR.md`;
   - que `verify --report` escribe un JSON en `docs/` del clon de `main`;
   - las 13 esperas, no 4;
   - `python` frente a `python3`;
   - la duración (53–60 min en la 4.15).
