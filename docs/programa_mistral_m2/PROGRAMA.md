# Munger V2 · programa Mistral M2 · 16-nov-2026

## Propósito y estado

Encargo autorizado por la persona responsable: aprovechar el crédito de Mistral para adelantar trabajo necesario, manteniendo los criterios de aceptación. Tres sesiones autoras distintas pueden trabajar en paralelo, con ramas y carpetas diferentes. Claude conserva la integración técnica y F1/Elis. Ningún resultado se incorpora automáticamente.

Referencia económica: commit `059f4f68dca7acf465b5f5b21de2dede84c885ff` del repositorio público `jluisplagos/munger-v2`, con los binarios históricos de la Release `base-4.14`. Sus registros y fuentes son material a contrastar, no verdades heredadas. Antes de incorporar cualquier propuesta se comprobará su compatibilidad con la versión final de Claude.

El piloto aceptado con límites está fijado en `0e3b505ba9eed82efa42651b98df5359a6f7aa84` del auxiliar. Leer sus correcciones: una suma manual equivocada y una interpretación errónea del EBIT demuestran por qué pasar un comprobador de estructura no acredita economía.

## Tres frentes y propietarios

| Frente | Rama | Única carpeta de escritura de la investigación | Entrega |
|---|---|---|---|
| A · cobertura integral Vidrala/Viscofan | `mistral/m2-cobertura-vm` | `resultados_m2/cobertura_vm/` | Evidencia de 677 entradas, 617 fuera del piloto, y 101 derivados con 87 nuevos |
| B · fundamento P-M1 | `mistral/m2-fundamento-pm1` | `resultados_m2/pm1/` | Fuentes, conciliación de reinversión, límites de θ/λ y dossier D2 |
| C · matemática de precio/objetivo | `mistral/m2-matematica-b` | `resultados_m2/matematica_b/` | Oráculo independiente, demostraciones, contraste de k y probabilidades; dossier D1/D7/D11 |

Cada sesión ejecuta solo su frente. Las carpetas de preparación son de lectura. Instalaciones de bibliotecas, descargas y temporales van a `.trabajo/`; no se cambian configuraciones de otras sesiones. No usar subagentes en las sesiones autoras iniciales: los tres frentes ya separan el trabajo. La revisión posterior requiere otro contexto y se encargará sobre commits concretos.

## Preparación de insumos

```bash
python3 docs/programa_mistral_m2/herramientas/preparar_insumos.py --download
```

Si `.trabajo/base414.zip` existe, se verifica y reutiliza. También se admiten `--zip RUTA` o `--base-tree RUTA`. El resultado es `.trabajo/insumos_m2/`: **selección parcial**, no producto completo validado. No pedir al usuario otra vez las partes del ZIP. Si no hay acceso o espacio, declarar el bloqueo concreto y continuar lo independiente; no inventar lecturas.

El índice preparado contiene los 29 PDF candidatos conservados de Vidrala/Viscofan y otros insumos concretos con huellas. Una asociación entre texto y PDF debe comprobarse con contenido y contexto; compartir números no basta. Las fuentes ausentes siguen ausentes hasta conservar y examinar sus bytes.

Para evitar cargar registros completos al contexto, el frente A dispone de `herramientas/consultar_lote.py`, con lotes de hasta 30 entradas y posibilidad de excluir las 60 ya cubiertas por el piloto. No volcar documentos enteros si bastan páginas contextualizadas.

## Reglas comunes de calidad

1. Separar dato publicado, derivación, hipótesis, convención, ausencia y no aplicable. No convertir hipótesis en hechos para completar recuentos. Preservar E1/D3/E2/E6; una decisión antigua no se vuelve a preguntar por aparecer en una lista histórica.
2. Fuente primaria identificada por documento, versión, bytes, SHA-256, página PDF, cabecera/columna, período, moneda, escala, signo y perímetro. Registrar límites de OCR, traducción, reexpresión y comparabilidad.
3. Los números calculados deben salir de scripts reproducibles con `Decimal`/fracciones donde proceda, no de sumas redactadas por el modelo. Conservar operandos y fórmulas. Generar las tablas desde una única salida de cálculo; no mantener medias diferentes a mano en varios informes.
4. La lectura numérica no acredita el significado económico; un subtotal puede incluir un gasto presentado en otra línea. Revisar identidades y notas. No confundir importe devengado con pago, mantenimiento con categoría contable ni inversión con crecimiento automáticamente.
5. Si el dato o política no se identifica, acotar con evidencia o dejar pendiente la conclusión afectada. Más escenarios no demuestran que la incertidumbre real esté cubierta.
6. Nada de sellos oficiales, firmas humanas ficticias, reactivaciones de aprobaciones, cambios de referencias del producto o cambios silenciosos de parámetros.

## Entregas y recuperación

- Primer commit: inventario, alcance, plan finito y fuentes disponibles/faltantes; no esperar al trabajo completo.
- Después, commit y push al cerrar cada lote o bloque importante, con `PUNTO_DE_RECUPERACION.md`: hecho, evidencia, pendiente, siguiente comando/acción y límites.
- Entrega final en la carpeta del frente: `RESUMEN_PARA_CLAUDE.md` (máximo dos páginas), datos/observaciones, scripts y comandos, resultados de comprobaciones, `HALLAZGOS.md`, `MANIFIESTO_SHA256.txt` y recuperación. Todas las rutas referenciadas deben existir o llevar estado AUSENTE.
- Declaración: «Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación por el integrador». No APROBADO ni aptitud financiera general.
- No abrir PR al original ni fusionar ramas. No modificar los resultados M1 ya revisados. Las discrepancias se documentan por separado.

## Finalización, revisión y presupuesto

Un frente termina cuando entrega su universo finito y sus pendientes honestos; no cuando consigue que todas las filas pasen. Hacer una autocomprobación reproducible, pero no presentarla como revisión independiente. La revisión de otro contexto se hará después sobre el commit congelado; los hallazgos materiales se corrigen o se mantienen como bloqueo, nunca se descartan por coste o fecha.

No repetir pruebas completas ni lecturas enteras por cambios solo de redacción. Las correcciones numéricas sí deben regenerar resultados afectados, sus referencias y huellas. Una corrección que abre casos nuevos necesita revisión de esas dependencias.

La persona responsable informa de crédito cercano a 250 EUR con caducidad próxima. Eso no es un objetivo de gasto. Recomendación operativa: reservar hasta 100 EUR para las tres primeras entregas y el resto para revisión y trabajo posterior, sujeto al saldo y condiciones reales. Este documento **no configura ni garantiza un tope de facturación**. Registrar el consumo si la sesión lo expone; si no, decirlo. No comprar créditos, activar recargas ni usar servicios externos de pago. Usar el modelo Mistral disponible y registrar el real, sin inventar esfuerzo máximo si no existe ese selector.

## Fuera de alcance

F1/Elis, cambios de software financiero, nuevas valoraciones actuales, decisiones de cartera, motor C y tercer caso B completo. Ahold no tiene Excel evaluado, respuesta ni PDF conservados en esta base: no se puede prometer su recorrido. Los bloqueos que requieren información del usuario se documentan una sola vez sin detener el resto del programa.
