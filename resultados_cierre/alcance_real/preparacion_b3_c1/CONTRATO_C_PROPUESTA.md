# Contrato económico propuesto · primer caso C real (banco o aseguradora) · F-C1

**Estado: PROPUESTA, no ejecutada, no validado.** El motor C solo tiene los dos fixtures
sintéticos de `v6/pruebas/fixtures/` (LEEME.txt: `Fixture_motorC_palancas_A.xlsx`,
`Fixture_motorC_original.xlsx`; palancas B14 0,03/0,06/0,08 · B15 0,10/0,14/0,16 · B16 n/a ·
B18 0,10/0,13/0,15). Ningún recorrido real acreditado (MATRIZ_ALCANCE_4_14 §1: «solo los dos
fixtures sintéticos del motor C»).

## 1. Qué es el motor C (según el producto, no según yo)

- Plantilla V6.3 con reglas propias en `B16:D16`; palancas propias del motor C (fixtures anteriores).
- E62 (patch_v62_base.py @ base F1): «El motor C es un modelo simplificado de **patrimonio y ROE**:
  sirve para ver si el reparto y el crecimiento del patrimonio son coherentes, y **NO valida la
  solvencia ni el capital regulatorio de ningún banco o aseguradora**.»

## 2. Contrato económico específico propuesto (por entidad, no generalizable)

1. **Unidad de cuenta**: patrimonio neto contable por acción (o valor liquidativo en aseguradoras),
   no FCF. El valor por acción se deriva de patrimonio × múltiplos coherentes con ROE y reparto.
2. **Puentes contables obligatorios** (entrada desde el informe oficial, con página y cita):
   - patrimonio inicio → fin: BAI + OCI + dividendos − recompras + ampliaciones + otros movimientos;
   - ROE = BAI / patrimonio medio; cohérence con el reparto (payout) declarado;
   - crecimiento del patrimonio = (1 − payout) × ROE (modelo simplificado del motor C).
3. **Hipótesis declaradas** (cada una con clase: hecho/fundamentada/convención/técnica):
   - ROE terminal por escenario (B18 en los fixtures), g∞ del patrimonio (B14), payout (B15);
   - capital regulatorio (CET1 / ratio de solvencia) **solo como contexto y guarda**, nunca como
     output de valor (E62).
4. **Límites explícitos del contrato**:
   - una plantilla que acepte cifras **no valida ese negocio** ni autoriza tratar todos los
     bancos/aseguradoras igual: hace falta contrato específico por entidad (distribución, vida,
     reaseguro, banca retail vs inversión…);
   - no acredita solvencia ni capital regulatorio;
   - el primer caso C no acredita todos los negocios financieros.

## 3. Bloqueo documental concreto

- Ninguna empresa financiera está conservada (INVENTARIO_Y_HUECOS.csv): las 6 de `empresas_v2` +
  Elis/Vidrala/Viscofan de 4.14 son industriales/servicios.
- Fuente necesaria: informe anual / 20-F / SFCR oficial **con SHA-256 y bytes**. En este entorno
  solo GitHub es alcanzable de forma autenticada (el frente B documentó HTTP 401 en
  `uploads.github.com` y TLS no verificado en el proxy para `www`), así que la descarga de la
  fuente oficial depende de que la persona responsable la adjunte o de un conector con acceso.
- Mientras tanto: paquete listo (SELECCION.csv, PROTOCOLO_CONGELADO.md, MAPA_ENTRADAS.jsonl,
  fuentes/huellas), contrato propuesto, huecos como huecos.

## 4. Lo que se entregará cuando exista la candidata

Recorrido completo en copia aislada con verificación de entradas, fases A/B/C, auditoría
independiente y relevo — por paquetes Git al coordinador (Cola 3), no ejecutado por mí.
