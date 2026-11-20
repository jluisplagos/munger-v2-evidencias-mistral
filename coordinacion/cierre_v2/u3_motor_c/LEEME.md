# U3 · contrato C corregido, protocolo y candidatos · BORRADOR para revisión

- **Autoría:** un subagente del coordinador, el 17-nov-2026, por encargo de la persona responsable (U3). Hace falta la **revisión de un contexto distinto** antes de aceptarlo.
- **Rutas:** las rutas locales se sustituyen por `<scratchpad>`, `<candidata>`, `<e_work>` y `<home>`.

## Estado

| Parte | Estado |
|---|---|
| `CONTRATO_C_DESDE_EL_MOTOR.md` | **Completo.** Escrito desde el código y las celdas de la candidata 957af65, con cita `archivo:línea`. Corrige F2-D3: X14 = crecimiento del patrimonio en los años 1–5; X15 = ROE objetivo; X18 = ROE a largo plazo; g∞ en Análisis B68; ROE = beneficio neto atribuible ÷ patrimonio de cierre; puente 1000 + 100 − 40 = 1060. Réplica independiente del motor C (`scripts/motor_c_replica.py`), que reproduce los dos fixtures del motor C. Pendientes de decisión, sin números: PD-1…PD-6 |
| `PROTOCOLO_SELECCION_C.md` | **Completo.** Fijado antes de nombrar candidatos: SHA-256 `3e28d9c0…`, a las 09:30Z. Sin precios ni umbrales |
| `CANDIDATOS_C.md` | **Propuestos y NO VERIFICADOS.** FinecoBank (banco) y Hannover Rück (reaseguro). Lo que se dice de cada uno es conocimiento previo, marcado [a verificar]. No se ha descargado ni leído ningún documento oficial (`INDICE_FUENTES.csv`: intentos y códigos HTTP) |

## Por qué faltan los documentos

- FinecoBank: el control de permisos de la sesión **denegó** la descarga, aunque el host ya estaba permitido en el entorno. No se ha intentado sortear.
- Hannover Re: el propio sitio responde 403 (CloudFront) a `curl`. No se ha cambiado el agente de usuario para eludirlo.

## Hallazgos del producto, por lectura estática y sin recalcular, para el frente técnico

- **H-C1, comprobado por el coordinador.** `v6/scripts/relacion_entradas_materiales.py:77-79` declara «Ventas» (Historia fila 6) solo para A y B. Según el autor, los controles V02–V04 y C43 la usan para todos los motores; esto falta por comprobar. Si se confirma, «Ventas» bloquearía el motor C sin entrar en su cálculo.
- **H-C2.** La Historia mide el ROE sobre el patrimonio de cierre y el motor lo aplica al de apertura: 9,43 % frente a 10 % en el caso.
- **H-C3.** En C, el crecimiento del patrimonio se compara con cuartiles de crecimiento de *ventas* del sector.

Son observaciones para revisión. No se corrigen aquí.
