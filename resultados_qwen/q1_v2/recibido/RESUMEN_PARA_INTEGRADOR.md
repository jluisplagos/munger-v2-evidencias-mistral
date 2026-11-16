# RESUMEN PARA INTEGRADOR - Banco Q1 v2 (Munger V2)

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
- Controles negativos del comprobador: 7.

## Pruebas sobre el banco
- En esta sesion: NINGUNA ejecutada (sin entorno). Declarado en
  resultado_comprobacion.json (ejecutado=false, version v2). La ejecucion previa
  del integrador fue sobre v1.
- Esperados calculados a mano con operandos explicitos; verificacion aritmetica
  real la hace comprobar_banco.py al ejecutarse.
- Controles negativos separados del banco valido (copias en memoria): ausencia
  de caso, esperado+1, id duplicado, operacion constante que ignora operandos,
  resultado booleano, calculo no finito, operando booleano. Pendientes de
  ejecutar con --autocontroles.
- MANIFIESTO_SHA256.txt: no entregado con huellas inventadas; se genera con
  --generar-manifiesto tras codigo 0.

## Limites
- Sin leer la implementacion no se afirma cumplimiento ni que falten
  exactamente estas pruebas; el banco es propuesta, no diagnostico.
- Politicas no fijadas van como DECISION_PENDIENTE/PROPUESTA, nunca obligacion
  inventada. Aclaraciones factuales (§2) se distinguen de politicas economicas.
- No se inventan campos/estados internos; criterios remiten a matriz §4,
  artefactos y registros de aprobacion cuando se expongan; si no, NO_OBSERVABLE.
- Modelo de sesion: Qwen; version/configuracion no expuestas, no inventadas.
  Sin firma humana. SHA-256 del requisito fuente: no verificado en esta sesion.

## Siguientes pasos
1. Materializar fixtures y ejecutar comprobar_banco.py con --autocontroles
   --resultado --generar-manifiesto; exigir codigo 0.
2. Fijar version y ejecutar los 36 casos segun PLAN_DE_EJECUCION.md recogiendo
   artefactos y registros, no solo texto.
3. Clasificar veredictos; aplicar distinciones de §3 del plan (factual vs
   politica; embebido; conflicto resuelto).
4. Escalar las 2 decisiones pendientes al responsable de politica.
5. Solo entonces valorar cobertura, pendientes e impacto en plazo.

Estado: banco de aceptacion propuesto (v2); comprobacion estructural pendiente
de ejecutar en el entorno del integrador; pendiente de ejecutar y revisar sobre
el producto. NO acredita aptitud para decisiones con dinero real.