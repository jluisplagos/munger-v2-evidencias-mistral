# Registro de uso de Fable en el examen (tope: 6 sesiones; D7)

| N.º | Fecha (UTC) | Para qué | Material | Esfuerzo | Resultado |
|---|---|---|---|---|---|
| 1 | 2026-11-17, noche | Revisión crítica independiente de F1-IMPL (implantación de las decisiones F1 en el motor A), incluida la recomendación sobre el límite F1-LIBRO para Ahold | `jluisplagos/munger-v2`, rama `f1/implantacion` @ 2e9442f (código probado: eb193f8) | máximo | CORRECCIONES: cifras reproducidas; 5 hallazgos materiales (cierre sin F1, F1 no exigido, F1-LIBRO con términos explícitos, V-F1m simétrica, K3 identidad); recomienda plantilla V6.3.1 mínima. Segunda ronda (misma sesión, sobre 24e9a30): CONFORME CON LÍMITES; `verificar_paquete.sh completa` PASA reproducido; abierto R2-1 (`--reiniciar --desde 13`). `revisiones/f1_impl/` |
| 2 | 2026-11-18, tarde | C4: autor de F1 con US GAAP (decisión de la persona, PLAN §5) | `munger-v2`, rama `f1/usgaap` | máximo | en curso |
| 3 | 2026-11-18, tarde | C5: revisión crítica de la hoja resumen (agente distinto del autor) | `munger-v2`, rama `examen/hoja-resumen` @ ef93699 | máximo | CORRECCIONES: 4 altas (precio de Sí sin conclusión oficial, vigencia, aptitud, escribe aunque falle), 5 medias, 5 bajas. `revisiones/hoja_ef93699/` |
| 4 | 2026-11-18, tarde | C1: contradictor de Ahold (CONTRADICTOR.md §3, contexto limpio) sobre la fase C turno 2 (descartar, cubo No, precio de Sí 27,74) | `munger-v2`, rama `examen/ahold-f1` @ a7b9357, carpeta `ahold_f1/Ahold` | máximo | 4 objeciones, todas al alza (flujo del accionista sin cobros financieros +3,00 €; acciones 865 M +1,0–1,2 €; listón del ROIC con arrendamientos No→Vigilar; margen NORMAL +0,4–0,7 €). `contradictor/ahold/` |

Reparto acordado (D7): Fable solo para F1-IMPL y para el contradictor del veredicto final; el contradictor de cada empresa usa Opus con esfuerzo alto.


Cambio de reparto (18-nov-2026, PLAN_TRES_FRENTES.md §3 y §5, con uso de Fable sin tope el 18 y el 19-nov por decisión de la persona responsable): Fable también para C4, revisiones críticas, el contradictor y la auditoría de cada empresa del examen. El tope de 6 sesiones de D7 queda sustituido para esos dos días.
