# Frente A · cobertura integral de entradas de Vidrala y Viscofan

Leer primero PROGRAMA.md. Rama `mistral/m2-cobertura-vm`; escritura exclusivamente en `resultados_m2/cobertura_vm/`. No ejecutar otros frentes.

## Universo fijado

- Vidrala final: `..._4_14/vidrala_decisiones/Vidrala`: **347 entradas**.
- Viscofan final: `..._4_14/viscofan_decisiones/Viscofan`: **330 entradas**. No usar las 328 del antecesor.
- Total **677**: 454 datos publicados, 13 ceros comprobados, 101 derivados, 6 ausencias, 52 hipótesis, 35 convenciones y 16 no aplicables.
- El piloto ya cubrió 60 entradas (26 Vidrala y 34 Viscofan), incluidos 14 derivados. Quedan **617 entradas** (321 y 296) y **87 derivados** fuera del piloto. Reutilizar la evidencia corregida, sin contabilizarla como investigación nueva.
- Hay 161 entradas de Historia por empresa. Cubrir todos los ejercicios que realmente figuran, no solo 2025. La delimitación completa está en `entrada/registro_base.json` y `entrada/catalogo_entradas.csv`.

## Trabajo

1. Inventariar el universo y sus dependencias. Relacionar cada fuente de texto con PDF conservado o ausente. Clasificar la tarea de cada fila según su naturaleza. Identificar referencias que solo llegan a una web o a una cita secundaria.
2. Revisar por documento/página y bloques de no más de 30 entradas: permite comprobar una tabla una sola vez y reutilizar la observación. Publicar el primer lote pronto. Priorizar cálculo y juicio materiales, sin eliminar los demás del universo.
3. Para los 467 datos/ceros declarados, comprobar literal, posición, período, versión/reexpresión, unidad/escala, signo y perímetro en los bytes originales. Un cero no se acredita por no encontrar una palabra. Registrar comparación con el XLSX en modo de solo lectura.
4. Para los 101 derivados, construir un grafo de orígenes, detectar huecos/ciclos, recalcular con script propio y documentar el significado de la fórmula. Son 87 reconstrucciones nuevas; los 14 del piloto se referencian y se revisan solo si un origen cambia. No inferir una política económica a partir de que la fórmula dé el valor esperado.
5. Para ausencias/hipótesis/convenciones/no aplicables, registrar qué existe, qué falta, su justificación y qué salida afecta. No declararlos datos verificados. Las convenciones se etiquetan como decisiones, no hechos publicados.
6. Preparar un mapa de dependencias para la futura regeneración: qué entrada puede reutilizarse con huella vigente, qué debe revisarse, qué requiere decisión o fuente. No generar un `verificacion_entradas.json` oficial ni simular sus sellos/revisor.

## Salidas específicas

- `COBERTURA_677.csv`: exactamente 677 filas, una por empresa/celda, con clase, materialidad declarada, estado propuesto, evidencia y límites, documento/hash/página/columna, transformación, comparación con libro y dependencia. Identificar `origen_revision=M1_REUTILIZADA` para las 60 del piloto.
- `OBSERVACIONES.jsonl`: evidencia reutilizable por fuente/página/tabla, sin convertir el registro antiguo en su propia prueba.
- `DERIVADOS.json`: 101 nodos, origen de cada operando, expresión, unidad, redondeo, significado, estado y resultado. Distinguir los 14 reutilizados y 87 nuevos.
- `scripts/` y `resultados/`: cálculos y control de cobertura/referencias. El control debe rechazar filas duplicadas/faltantes, fuentes referenciadas inexistentes presentadas como examinadas, operandos incoherentes y reutilización de resultados tras cambiar datos sin recalcular.
- `MAPA_REGENERACION.md`: qué puede aprovechar Claude y qué queda bloqueado. No es orden de modificar libros ni de adoptar decisiones.

Estados permitidos: `COINCIDE_PROPUESTO`, `DIFERENCIA`, `NO_ACREDITADO`, `HIPOTESIS`, `CONVENCION`, `DATO_AUSENTE`, `NO_APLICABLE`. «COINCIDE» no significa suficiente para invertir. No fijar como objetivo 677 coincidencias.

Aplicar además los entregables comunes del programa. Concluir con recuentos por empresa/clase/estado, conciliados con 677 y con las 60 reutilizadas. Si un dato exige un PDF no conservado, registrarlo sin sustituirlo por una traducción o versión distinta no comparable. Las nuevas fuentes opcionales se documentan, pero su preservación deberá seguir el protocolo de la Release auxiliar del frente B; no disputar su gestión.
