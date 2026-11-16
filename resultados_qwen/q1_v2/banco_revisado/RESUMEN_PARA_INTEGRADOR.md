# RESUMEN PARA INTEGRADOR - Banco Q1 v2 revisado (Munger V2)

Esta copia incorpora cambios del integrador sobre la entrega original de
Qwen, que se conserva por separado. No atribuir esos cambios ni su ejecución
a la sesión de Qwen. La salida real está en resultado_comprobacion.json.

## Alcance
36 casos sinteticos (6 familias x 6; 2 positivos y 4 conflictos/carencias por
familia) para probar despues la entrada por instrucciones y el recorrido de
usuario. No es auditoria financiera, no modifica el producto, no ejecuta
versiones no recibidas. No repite frentes Vidrala/Viscofan, P-M1 ni matematica
de precio/objetivo. Nombres ficticios, numeros simples.

## Correcciones v2 aplicadas (7/7)
1. Q1-010 pasa a POSITIVO (equivalencia 1,5M=1500 miles, sin contradiccion
   inventada); Q1-007 pasa a CONFLICTO con ambiguedad real de escala (tabla sin
   unidad vs nota en millones) para conservar 2/4 en familia 2.
2. Q1-018 limitado a inventario 190 vigente vs 210 antiguo; sin agregado de
   circulante; esperado = impacto de reexpresion 20.
3. Q1-026/027: operando deuda 300 aportado con fuente sintetica propia
   (f5_026_nota.txt, f5_027_excel.csv); operandos de los 17 esperados auditados
   caso a caso (cada caso se ejecuta aislado).
4. Q1-005: derivado neutro magnitud sintetica D (sin etiqueta EBITDA); conserva
   origen pendiente.
5. comprobar_banco.py rechaza operacion que ignora operandos, booleanos como
   numeros y no finitos; AST restringido; 4 controles negativos nuevos (7 tot).
6. Q1-034: rango 0-200 tratado como acotado/delimitado; falta punto justificado
   o tratamiento documentado; se impide punto unico apto, no analisis acotado.
7. Plan/clasificacion: aclaracion de periodo = factual (§2), no politica
   economica; instruccion embebida nunca justifica marcar sin contraste;
   conclusion tras conflicto resuelto+documentado+revisado no es fallo.

## Recuentos v2
- Casos 36 (Q1-001..036); control 12 POSITIVO / 24 CONFLICTO_CARENCIA.
- Naturaleza: 31 CONTRATO_REFERENCIADO / 3 PROPUESTA_ACEPTACION (019,022,029) /
  2 DECISION_PENDIENTE (030,035).
- Esperados numericos: 17, con unidad/operandos/operacion explicitos y
  operandos presentes en los fixtures del propio caso; el comprobador recalcula.
- Fixtures: 50 TXT/CSV/JSON; sin XLSX ni macros ni codigo en fuentes.
- estado_ejecucion_producto: NO_EJECUTADO en los 36.
- Controles negativos del comprobador revisado: 9.

## Pruebas sobre el banco
- Qwen declaró no ejecución de su versión. Su declaración y archivos se
  conservan intactos en recibido/; no se le atribuyen las ejecuciones siguientes.
- El integrador materializó 50 fixtures y ejecutó comprobar_banco.py con
  --autocontroles --resultado --generar-manifiesto: código 0, 36 casos,
  17 esperados y 9 controles negativos detectados. El resultado real y su fecha
  constan en resultado_comprobacion.json.
- Una comprobación independiente con fracciones exactas confirmó los 17
  resultados; las sondas de constante simple, disfrazada y cancelación repetida
  fueron rechazadas. Evidencia en ../revision/VERIFICACION_INTEGRADOR.json
  dentro de la entrega publicada.
- El manifiesto contiene 57 archivos: siete archivos del banco más 50 fixtures.
  Se excluye el propio manifiesto y se conservan huellas calculadas realmente.
- Ningún caso se ha ejecutado contra el personaje: NO_EJECUTADO en los 36.

## Limites
- El integrador añadió el rechazo de constantes disfrazadas y operandos
  repetidos, una nota N/A sintética examinable y precisiones en 8 casos para
  evitar falsos fallos (ausencia frente a contradicción, fuente independiente,
  período documentado y política temporal/motor). Ver la revisión externa.
- Los fixtures representan escenarios; preparar las precondiciones mediante
  las vías soportadas del producto. ADAPTACION_PENDIENTE no es fallo del producto.
- Sin leer la implementacion no se afirma cumplimiento ni que falten
  exactamente estas pruebas; el banco es propuesta, no diagnostico.
- Politicas no fijadas van como DECISION_PENDIENTE/PROPUESTA, nunca obligacion
  inventada. Aclaraciones factuales (§2) se distinguen de politicas economicas.
- No se inventan campos/estados internos; criterios remiten a matriz §4,
  artefactos y registros de aprobacion cuando se expongan; si no, NO_OBSERVABLE.
- Modelo de sesion: Qwen; version/configuracion no expuestas, no inventadas.
  Sin firma humana. SHA-256 del requisito fuente: no verificado en esta sesion.

## Siguientes pasos
1. Comprobar el manifiesto y reproducir los controles estructurales; la copia
   revisada ya dio código 0 en el entorno del integrador.
2. Fijar version y ejecutar los 36 casos segun PLAN_DE_EJECUCION.md recogiendo
   artefactos y registros, no solo texto.
3. Clasificar veredictos; aplicar distinciones de §3 del plan (factual vs
   politica; embebido; conflicto resuelto).
4. Escalar las 2 decisiones pendientes al responsable de politica.
5. Solo entonces valorar cobertura, pendientes e impacto en plazo.

Estado: banco de aceptación propuesto, estructuralmente comprobado y revisado
en el alcance documentado; pendiente de adaptar, ejecutar y revisar sobre el
producto. NO acredita aptitud para decisiones con dinero real.
