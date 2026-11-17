# T-TRASPASO · resultado del 17-nov-2026 · procedencia

- **Receptor.** Un agente nuevo, sin historial, que solo recibió `../PROMPT_RECEPTOR.md` (`788f25c`) y siguió `../../manual/MANUAL_OPERATIVO_957af65.md`. Trabajó desde clones y descargas propias, en una carpeta nueva.
- **Límites declarados:**
  - es de la misma familia de modelo que el autor del manual;
  - no puede lanzar agentes de contexto separado, así que los pasos 13–17 con agentes reales quedan «no ejecutables por el receptor», sin simular nada y sin ningún APROBADO;
  - Mistral A no vale como receptor.
- **Objeto.** La candidata en `957af65`. La integración documental posterior, G-DOCS (`3149128`), cambia solo documentos que este ensayo leyó en su versión anterior.
- **Comprobado por el coordinador.** `registro/paso8_verificar_paquete_completa.log` es **idéntico byte a byte** (SHA-256 `23fd7aa1…`) al de `../../pruebas_candidata/957af65/verificar_paquete_completa.log`. Un receptor nuevo, solo con el manual, obtiene la misma verificación completa: PASA, código 0, las quince baterías con sus recuentos.
- **Rutas.** Las locales se sustituyen por `<traspaso>`, `<e_work>`, `<home>` y `<root>` en 11 archivos. `registro/SHA256_REGISTRO.txt` corresponde a los archivos originales, antes de la sustitución; las huellas de esta carpeta son las de `MANIFIESTO_SHA256.txt`.
- **Pendiente.** La revisión del informe por un agente distinto del receptor. Las deficiencias del manual que encontró (§ ambigüedades: disco, comandos no documentados, relevo ya caducado en los pasos 12–13, H9, referencias desfasadas al control y `verify --report` escribiendo en el clon de `main`) se recogen como mejoras pendientes del manual. No se cambian aquí.
