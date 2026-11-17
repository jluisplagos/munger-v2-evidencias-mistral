# Sondas del informe de revisión A2_8b88fab publicadas como artefacto reproducible (A3-R8)

Fuente (solo lectura, sin fusionar): rama `coordinacion/cierre-v2` @ `57b34a60101d696dc8eca79181fd03c8ab2152eb`,
ruta `coordinacion/cierre_v2/revisiones_coordinador/A2_8b88fab/sondas/`. Recuperadas con:

```bash
git show origin/coordinacion/cierre-v2:coordinacion/cierre_v2/revisiones_coordinador/A2_8b88fab/sondas/<f> > sondas_a3/sondas_informe/<f>
```

Uso (contra el código de esta rama): `python3 -I -B sondas_informe/s02_sondas_revisor_A.py resultados_m2/cobertura_vm/scripts/verificar_contexto.py SALIDA.json`
(s07 igual; s03 igual). En `sondas_a3/out/` quedan las ejecuciones por punto A3-R1…R7
(`R1_s02_sondas_informe.json` … `R7_s07_informe.json`) y las sondas nuevas propias
(`s11_R<n>_sonda_nueva.py`, salidas en `out/R<n>_s11_sonda_nueva.json`).

Las sondas del revisor usan rutas de su entorno (`<rev_A2>`, `<zip>`); aquí se ejecutan
directamente sobre `scripts/` de esta rama con los insumos de `.trabajo/insumos_m2`.
