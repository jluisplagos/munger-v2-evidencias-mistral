# Validación del piloto · 17-nov-2026

Estado: preparado y probado localmente; pendiente de prueba de API real y de
revisión por otro contexto. No hay aceptación de entregas ni aptitud económica.

## Ejecutado realmente

- `python3 -m unittest discover -s automation/claude_review -p test_pilot.py -v`:
  **40 pruebas, salida 0**. Transporte Anthropic y registro remoto simulados.
  Incluyen presupuesto, reserva previa, carrera de creación, duplicados, timeout,
  publicación fallida, salida incompleta, citas inventadas, rutas, fuentes
  ausentes, tipos inválidos y credenciales ausentes. Ninguna llamada a Anthropic.
- YAML del workflow leído con PyYAML y comprobados disparadores, permisos,
  ausencia de schedule/pull_request_target y exclusión mutua.
- Preparación con GitHub real y las cuatro fuentes fijadas en request.json:
  **salida 0, PREPARADO_SIN_API, api_messages_sent=0**.
  Código local de ese ensayo: f5a924f02484880e971bbda920801b6f8555e4fb.
  Paquete: 29618 bytes, SHA256
  b2a05a9088f8642be06a10fa4903c721893a3a74aad4419e4e2d6c56e3988614.
  Del original de 36 paquetes se incluyeron solo Q1-028 y Q1-032;
  los otros 34 constan omitidos. Las cuatro fuentes conservaron su SHA256.
- Reserva orientativa calculada solo por bytes (sin conteo del proveedor):
  USD 0,115726 con las tarifas fijadas. Es un cálculo conservador previo, no un
  coste cobrado ni una confirmación de elegibilidad del crédito.
- Prueba CLI contra cambio real oculto con skip-worktree en request.json:
  rechazo con salida 2 y BYTES_DEL_PILOTO_DIFIEREN_DEL_SHA antes de leer red/API.
  Archivo e índice restaurados después de la prueba.
- `git show --check`: sin errores.

## Todavía no comprobado

- Autenticación real con Anthropic y acceso al modelo del piloto.
- Aplicación efectiva del crédito promocional a una llamada.
- Respuesta real del modelo y publicación real del informe de API en la rama
  de registro. Las pruebas del transporte y del registro remoto son simuladas.
- GitHub Actions: el resultado remoto debe consultarse tras publicar la rama.
  No se confunde la validación local del YAML con haber ejecutado Actions.
- No hay conexión automática con ventanas privadas de ChatGPT/Claude/Mistral,
  revisión periódica, ni activación automática de agentes del personaje.

El consumo de Anthropic en estas comprobaciones fue cero peticiones Messages.
El piloto se publica con mode=dry-run. No se fusiona main ni se modifica la
candidata, el control común o las políticas financieras.
