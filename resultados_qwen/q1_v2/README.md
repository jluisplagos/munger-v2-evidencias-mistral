# Qwen Q1 · banco propuesto de aceptación · entrega v2 revisada

**Estado:** preparación del banco terminada y comprobada estructuralmente. **Ejecución contra Munger V2: 0/36 casos.** No declara cumplimiento del producto ni aptitud inversora.

- `recibido/`: siete archivos originales de Qwen, sin cambios de contenido. Solo se normalizaron sus nombres; procedencia y SHA reales en `revision/PROCEDENCIA.json`. Qwen declaró correctamente no haber ejecutado Python.
- `banco_revisado/`: copia del integrador, con 36 casos, 50 fixtures, comprobador, plan y resumen. Incluye resultado de ejecución real y manifiesto de 57 archivos.
- `revision/`: dictamen, contraejemplo del comprobador recibido, registro de cambios y verificación aritmética independiente.

La copia a utilizar para preparar la aceptación es **`banco_revisado/`**. No sustituirla por la recibida ni tomar los JSON sintéticos como auditorías auténticas del producto.

## Reproducción del banco

En un directorio aislado con la copia revisada:

```bash
cd resultados_qwen/q1_v2/banco_revisado
sha256sum -c MANIFIESTO_SHA256.txt
python3 -I materializar_fixtures.py
python3 -I comprobar_banco.py --autocontroles --resultado --generar-manifiesto
```

La segunda ejecución actualiza la fecha del resultado y, por tanto, su huella: conservar el manifiesto recibido antes de regenerarlo si se quiere comparar la entrega original. El control comprueba el banco, no ejecuta el personaje.

## Uso posterior

1. Fijar commit y configuración de la candidata del producto.
2. Adaptar las precondiciones por vías soportadas y vincular cada observable a un artefacto o estado real. No calificar como fallo un formato sintético aún no adaptado.
3. Ejecutar los 36 casos aisladamente, recoger evidencias y aplicar `PLAN_DE_EJECUCION.md`.
4. Revisar resultados y dependencias; distinguir contrato, propuesta de aceptación y política pendiente. No modificar fórmulas para conseguir que pase un caso mal adaptado.

No se ordena que Claude cambie ahora de tarea ni que se incorporen estos archivos a la rama técnica o económica. La entrega queda disponible para la fase de aceptación. No se ejecutaron LibreOffice, macros ni el pipeline y no se modificó `jluisplagos/munger-v2`.
