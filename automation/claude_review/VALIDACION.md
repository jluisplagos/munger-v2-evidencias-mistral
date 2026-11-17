# Cierre real y recuperación sin nueva inferencia

Dos llamadas reales: workflows 44067759033 y 44068831767. La primera se rechazó
por salida incompleta; la segunda devolvió una respuesta completa dentro de un
envoltorio Markdown JSON. Los registros originales no se alteraron.

El resultado guardado del segundo ensayo se fijó por commit y SHA256 y se validó
retirando únicamente ese envoltorio: 9 hallazgos con citas literales.

Pruebas locales finales: 49 correctas, 0 fallidas. Añadidas pruebas de envoltorio
anclado, rechazo de prosa/múltiples bloques y replay que no llama a Anthropic,
conserva los originales y sigue rechazando citas inventadas.

Replay con GitHub real y salida local: informe documental pendiente de revisión
humana, 9 hallazgos, cero nuevas llamadas, coste estimado conjunto USD 0,164726.
No se aceptó ni integró ninguna entrega de Mistral.

Modo publicado: replay. Su ejecución remota se consulta en Actions tras publicar.
Las secciones siguientes conservan la historia de las validaciones anteriores;
las limitaciones de autenticación inicial quedaron superadas.

---

# Validación del piloto · 17-nov-2026

## Adenda del segundo ensayo

- El primer ensayo autenticó contra Anthropic y publicó su consumo real de tokens.
  Se conserva su resultado incompleto, sin aceptación: 14704/4096 tokens, coste
  estimado USD 0,070368, workflow 44067759033.
- Ajuste probado: 43 pruebas locales pasan. Se añaden el cómputo acumulado del
  presupuesto y rechazos de consumo previo contradictorio y paquete cambiado.
- El segundo ensayo no puede reservar si su reserva + consumo previo supera
  USD 0,25. Con el paquete actual, la reserva conjunta calculada por bytes es
  USD 0,227054 (no es una factura ni un segundo conteo del proveedor).
- Las afirmaciones de falta de autenticación de la sección histórica inferior
  quedan superadas por el primer ensayo. La aplicación del crédito promocional
  sigue requiriendo comprobar Console; no se infiere del uso devuelto por API.
- Sigue pendiente un informe completo y validado de salida. El segundo ensayo
  conserva texto visible y stop_reason para poder diagnosticarlo sin repetirlo.

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
