Trabaja en español. Este es un encargo paralelo autorizado para Mistral Code: preparar evidencia de fuentes de Vidrala y Viscofan para Munger V2. No es una tarea de modificación del producto ni de inversión.

1. Comprueba primero el remoto origin. Debe ser exclusivamente `jluisplagos/munger-v2-evidencias-mistral`. Si el proyecto está conectado a `jluisplagos/munger-v2`, no ejecutes la tarea allí: pide cambiar al repositorio auxiliar. No necesitas acceso de escritura al original, que es público.

2. En el auxiliar, lee la preparación pública sin fusionar ninguna rama del producto:

```bash
git fetch --no-tags https://github.com/jluisplagos/munger-v2.git refs/heads/preparacion/mistral-fuentes-vm
git rev-parse FETCH_HEAD
git archive FETCH_HEAD docs/mistral_fuentes_vm | tar -x
```

Registra el SHA de preparación obtenido. Importa solo ese directorio; no hagas merge, reset ni checkout de una rama del producto. Crea tu rama `mistral/fuentes-vm-01`, o registra la rama de tarea que cree Code.

3. Lee íntegramente `docs/mistral_fuentes_vm/ENCARGO_MISTRAL.md` y los archivos de `entrada/`. Sigue ese encargo completo. Se autoriza el uso de Mistral en esta sesión; las menciones históricas a Opus/Fable no te autorizan a llamar otros proveedores ni a modificar su trabajo.

4. Prepara los insumos con `python3 docs/mistral_fuentes_vm/herramientas/preparar_insumos.py --download`. Si ya hay ZIP o árbol base, usa las opciones documentadas. Son 15 archivos seleccionados, con cinco PDF y dos libros, ligados a huellas. No hay que pedir al usuario las partes del ZIP. Si faltan red o herramientas, registra qué falta y completa lo independiente sin fingir lecturas.

5. Contrasta los 26 objetivos fijados y sus 34 dependencias: acciones, CFO, capex, intereses, arrendamientos, pagos en acciones, ventas, EBIT, amortizaciones y circulante. Lee primero fuente y cabeceras, guarda tu lectura, después compara con el libro y las declaraciones históricas y recalcula derivados. Distingue año, columna, grupo, moneda, escala, signo, versión, dato ausente e hipótesis. No fuerces a dato publicado lo que no lo sea. Preserva E1/D3/E2. El trabajo no incluye Elis/F1, nuevas empresas, política económica ni precios objetivo.

6. Mantén los PDF, XLSX y ZIP fuera de Git. No ejecutes LibreOffice ni el pipeline. Usa herramientas deterministas para huellas y cálculos. Registra el modelo realmente disponible; no inventes un nivel de esfuerzo si la interfaz no lo ofrece. Una sola sesión, sin subagentes ni rondas recursivas. No cambies facturación ni recargas. El presupuesto inicial recomendado es 25 EUR configurados externamente; si no ves el consumo, decláralo y no afirmes que lo estás limitando.

7. Entrega los seis archivos de `resultados/` definidos en el encargo, incluyendo el CSV de 26 objetivos, evidencias, hallazgos, resumen para Claude, recuperación y manifiesto. Ejecuta el comprobador de estructura. Guarda commit y push en tu rama del auxiliar al terminar cada bloque. No abras PR hacia el original ni fusiones. Declara siempre: «Evidencia propuesta por Mistral; pendiente de revisión e incorporación por el integrador». No declares aptitud para dinero real.

Completa este encargo finito sin esperar que termine Claude. Al final devuelve el enlace al commit, recuentos, hallazgos materiales, pendientes y consumo si está disponible. No amplíes el alcance por iniciativa propia.
