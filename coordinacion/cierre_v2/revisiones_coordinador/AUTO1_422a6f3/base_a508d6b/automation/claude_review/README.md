# Piloto Claude API · resultado real y modo actual

Primer puente comprobado: GitHub Actions → Claude API → informe en GitHub.
Revisión documental parcial de Q1-028/Q1-032 en D @d032691. No ejecuta el
personaje ni sus pruebas, no acepta entregas, no modifica CONTROL/ESTADO y no
escribe en el repositorio producto. No es aún una coordinación de tres plataformas.

## Ensayos y resultado

1. Workflow 44065901791: preparación correcta sin Anthropic y 40 pruebas.
2. Workflow 44067759033, munger-d-relevos-001: autenticación correcta, respuesta
   incompleta al alcanzar 4096 tokens. Uso: 14704 entrada, 4096 salida (3735 de
   razonamiento). Coste estimado USD 0,070368. Resultado y reserva conservados.
3. Workflow 44068831767, munger-d-relevos-002: Sonnet 5.5, esfuerzo high explícito
   y razonamiento adaptativo, límite 8192. Respuesta completa, end_turn: 14704 de
   entrada y 6495 de salida (2906 de razonamiento). Coste estimado USD 0,094358.
   El parser inicial rechazó el bloque Markdown JSON; ese workflow consta fallido.
4. Se retiró exclusivamente un único envoltorio Markdown JSON completo, sin buscar
   JSON dentro de prosa. El objeto y sus 9 citas literales validan contra el paquete
   conservado. No se hizo una tercera llamada.

Total estimado de las dos llamadas: USD 0,164726. Se calcula desde uso y tarifas,
no es una factura. El crédito promocional o comprado descontado se comprueba en
Claude Console. La validación de citas y formato no acredita por sí sola la
verdad semántica de toda observación; eso queda pendiente del coordinador.

## Modo actual: replay, sin nueva inferencia

request.json queda en mode=replay. Lee el resultado pagado desde el commit fijo
5b1295017ccedb3f68bc04e69a99307719c5af1f del registro y exige su SHA256.
Reúne de nuevo las cuatro fuentes en SHA fijos y comprueba el paquete.
No necesita la clave de Anthropic ni llama a sus endpoints, tampoco al conteo.

Publica únicamente postprocessed_report.json y postprocessed_report.md en:
rama automatizacion/claude-api-piloto-registro,
carpeta automation/claude_review/results/munger-d-relevos-002/.

Ambos resultados y reservas originales permanecen intactos. La normalización no
equivale a una aceptación de Mistral. El informe lleva accepted=false,
integrated=false y product_executed=false. La fotografía revisada es d032691,
no las entregas que se publiquen después.

## Controles

- Único escritor del control e integrador: Claude coordinador existente.
- El piloto escribe solo su rama de registro del auxiliar. Sin cambios en main
  ni en la candidata del producto.
- Fuentes fijadas, máximo de paquete y rechazo en lugar de truncado silencioso.
- Modelo sin herramientas ni credenciales en su prompt; scripts del autor no
  ejecutados. Ninguna salida del modelo se convierte en órdenes.
- Una reserva durable por ensayo antes de la llamada. Un timeout no permite un
  reintento automático ni se considera coste cero.
- El segundo ensayo enlaza el registro real del primero y exige coste previo +
  reserva nueva ≤ USD 0,25. No borra ni reinicia la reserva anterior.
- Tarifas verificadas el 17-nov-2026: Sonnet 5.5, USD 2/MTok entrada, USD 10/MTok
  salida. No se solicitó Priority, caché o herramientas. La factura y límites
  efectivos corresponden a Anthropic.
- No se preparan terceros intentos. Si alguien cambia a mode=api, la reserva
  ya existente bloquea nuevas llamadas.
- El secreto ANTHROPIC_API_KEY está configurado en GitHub; nunca se publica.
- Sin calendario ni bucles de espera. No despierta ventanas privadas.
- E1/D3/E2/E6, C48=108, C49=128,1, FCF base=307,933 y Elis pendiente se conservan.

## Reproducción

Desde la raíz del checkout:

    python3 -m unittest discover -s automation/claude_review -p test_pilot.py -v
    python3 automation/claude_review/pilot.py --request automation/claude_review/request.json --output /tmp/munger-api-replay --code-sha "$(git rev-parse HEAD)"

El segundo comando, en mode=replay, revalida y publica los dos archivos derivados.
Requiere GH_TOKEN con escritura en este auxiliar, sin llamadas Anthropic.
Para preparar sin publicar, versionar mode=dry-run. El CLI comprueba los bytes del
script y de request.json contra HEAD incluso con skip-worktree.

Pruebas locales finales: 49 correctas. Incluyen presupuesto acumulado, reserva,
duplicados, timeout, publicación fallida, citas inventadas, formato incompleto,
envoltorio único, prosa/múltiples bloques rechazados y replay sin Anthropic.

## Fuentes oficiales

- https://platform.claude.com/docs/en/models/sonnet-5-5/overview
- https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide
- https://platform.claude.com/docs/en/about-claude/pricing
- https://platform.claude.com/docs/en/build-with-claude/token-counting
- https://platform.claude.com/docs/en/api/versioning
- https://support.claude.com/en/articles/8977456-how-do-i-pay-for-my-claude-api-usage
- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
