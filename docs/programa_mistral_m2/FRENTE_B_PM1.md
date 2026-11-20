# Frente B · fundamento económico de reinversión y P-M1

Leer PROGRAMA.md. Rama `mistral/m2-fundamento-pm1`; escribir en `resultados_m2/pm1/`. Este frente aborda un bloqueo económico pendiente de los dos casos B. No es F1/Elis ni adopta una familia, parámetro o política.

## Leer como índice y propuestas a contrastar

Bajo `personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/documentacion_cierre_4_14/`:

- `EVIDENCIA_ECONOMICA_4_14.md`.
- `DESCOMPOSICION_VISCOFAN_4_14.md`.
- `DECISIONES_PENDIENTES_4_14.md`, especialmente D2/D5 y sus dependencias.
- `DECISIONES_ENTRADAS_4_14.md` y `MATRIZ_ALCANCE_4_14.md`.

También `personaje_v2/scripts/configuracion_economica.py` y los archivos de configuración y fases de los dos expedientes finales de decisiones. No ejecutar ni editar código del producto. Los informes antiguos orientan búsquedas; no se copian como nueva evidencia.

## Viscofan · datos operativos y conciliación

1. Extraer inversión por capacidad, proceso, EHS/sostenibilidad y ordinaria para 2016–2025, distinguiendo cada fuente y los años sin desglose. Pistas conservadas: AR2025 p.PDF144 (impresa123), IA2021 p213, CF2022 p202, IA2023 p250. Verificarlas, no heredarlas.
2. Conservar las fuentes oficiales que faltaban: informe de gestión/anual 2024 y presentación Beat'30 si son accesibles. El PDF financiero CF2024 no se convierte por su nombre en informe anual completo. Usar solo fuentes oficiales sin pagos a terceros; registrar URL final, fecha, nombre, SHA, tamaño, versión, número de páginas y estado de acceso.
3. Conciliar importes, porcentajes y perímetros: pagos de caja frente a adiciones; bruto frente a neto; ROU y adquisiciones; unidades y comparativos. La base documenta 2022 inversión 125,6 M€ frente a capex de caja 115,566 M€ y 2025 con ROU en la taxonomía: recomprobar y explicar el puente, no igualarlos por conveniencia.
4. Recalcular las tablas y alternativas de θ conservadas en el informe, con script y operandos. El script allí citado `agentes/B/scripts/theta_desglose_viscofan.py` no está en la base y no se puede invocar como evidencia disponible.
5. No equiparar automáticamente categorías de inversión con mantenimiento económico o crecimiento. Una cifra de θ negativa se conserva como diagnóstico de definición/identificación: truncarla a cero no valida θ=0, la familia ni el punto actual.

## Vidrala · reposición, capacidad e índices

1. Extraer datos publicados sobre reconstrucción de hornos, vida útil, capacidad, modernización e inversiones. Distinguir reposición de capacidad añadida solo donde la fuente lo permita.
2. Revisar las altas ROU y sus perímetros activo/pasivo, incluidas las diferencias que documenta la base. No suponer que ambas líneas deben ser idénticas.
3. Evaluar las propuestas de λ del informe. Si se usan series INE/Eurostat, descargar datos y metadatos primarios de series concretas y justificar frecuencia, base, país/sector y fechas; conservar código de transformación y cambios de base. No usar snippets ni un índice genérico como si representara exactamente activos, tecnología y geografía del grupo.
4. Calcular rangos condicionados por supuestos explícitos y mostrar lo que no está identificado. La vida útil 8–16 años es una pista a contrastar; no una distribución ya adoptada. No fabricar mezcla reposición/capacidad ni nivel de mantenimiento para cerrar el bloqueo.

## Preservación y salidas

Este frente es el **único propietario de las fuentes nuevas**. Puede crear en el repositorio auxiliar una Release `fuentes-mistral-m2-20261116` con assets de documentos oficiales nuevos y un índice SHA-256. No modificar Releases del original ni la base4.14; no sustituir bytes bajo un mismo nombre. Si la herramienta no permite preservar archivos recuperables, registrar la fuente como provisional, conservar URL/hash/tamaño y dejar pendiente su revisión: una lectura web sin bytes no se presenta como documento conservado. No subir PDF/XLSX/ZIP al historial Git.

Entregar, además de los comunes:

- `FUENTES_NUEVAS.csv` y `FUENTES_CONSERVADAS.csv` con procedencia y estado reales.
- `INVERSION_VISCOFAN_2016_2025.csv` y `PUENTE_CAPEX_DA_ROU.csv` con dato/fuente/unidad/perímetro y huecos, sin interpolar.
- `VIDRALA_REPOSICION_CAPACIDAD.csv` y, si proceden, series primarias de índices en CSV con metadatos.
- `CALCULOS_PM1.json`, scripts reproducibles y tablas generadas: distinguir derivación de dato, inferencia y política.
- `DOSSIER_D2.md`: qué queda identificado, qué no, opciones defendibles condicionadas, evidencia ausente, consecuencias y decisión que correspondería a la persona responsable.

No elegir θ/λ ni justificar un parámetro porque dé un precio conservador. No actualizar precios, emitir compra/venta ni declarar P-M1 resuelto por haber calculado muchas variantes. Una entrega con identificación insuficiente pero bien demostrada es un resultado útil.
