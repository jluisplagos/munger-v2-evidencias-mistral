# Contrato económico propuesto · primer caso C real (banco o aseguradora) · F-C1

**Estado: PROPUESTA corregida según F2-D3, no ejecutada, no validada.** El motor C solo tiene los
ibraltar dos fixtures sintéticos de `v6/pruebas/fixtures/` (`Fixture_motorC_palancas_A.xlsx`,
`Fixture_motorC_original.xlsx`; palancas B14 0,03/0,06/0,08 · B15 0,10/0,14/0,16 · B16 n/a ·
B18 0,10/0,13/0,15; valores esperados B78:D78 en el LEEME.txt). Ningún recorrido real acreditado.

Todas las citas de celdas y líneas son de `jluisplagos/munger-v2 @ 957af65` (producto de
referencia, solo lectura). Verificación numérica: `../correccion_f2/scripts/verificar_contrato_c.py`
(salida en `../correccion_f2/evidencias/d3_verificar_contrato_c.txt`, exit 0).

## 1. Qué es el motor C (según el producto)

- Selección: `Palancas C6` = caso especial «Financiera» → `Diagnóstico C5` = motor «C»
  (`build_v6.py:146-153`, nota de la fila 6: «Financiera → motor C»).
- E62 (`v6/scripts/patch_v62_base.py:255-257`): «El motor C es un modelo simplificado de
  **patrimonio y ROE**: sirve para ver si el reparto y el crecimiento del patrimonio son
  coherentes, y **NO valida la solvencia ni el capital regulatorio de ningún banco o
  aseguradora**.»

## 2. Palancas reales del motor C (Palancas, por escenario B/C/D = MALO/NORMAL/BUENO)

| Celda | En el motor C es | Fuente en el código |
|---|---|---|
| `Palancas!X14` (B14:D14) | **Crecimiento del patrimonio · años 1–5** | `relacion_entradas_materiales.py:143-144` (id `crec`, motores ABC, «años 1–5»); `build_v6.py:444` |
| `Palancas!X15` (B15:D15) | **ROE objetivo, alcanzado en el año 5** (NO es payout) | `relacion_entradas_materiales.py:145-146` («margen objetivo; ROE objetivo en C»); `build_v6.py:446` |
| `Palancas!X16` (B16:D16) | S2C — **no se usa en el motor C** (el motor fuerza 1) | `relacion_entradas_materiales.py:147-148` (motores «AB»); `build_v6.py:448-449, 970` |
| `Análisis!X68` (B68:D68) | **g∞ (crecimiento terminal del patrimonio)** — no está en Palancas | `relacion_entradas_materiales.py:151-152`; `build_v6.py:453`; validación V15 `build_v6.py:1142-1144` |
| `Palancas!X18` (B18:D18) | **ROE a largo plazo (rentabilidad terminal, año 11 en adelante)** | `relacion_entradas_materiales.py:149-150` («rentabilidad terminal»); `build_v6.py:450-452` |

Validaciones del producto: V12 (crecimiento B14:D14), V13 (margen/ROE objetivo B15:D15), V15 (g∞
Análisis B68:D68), V16 (ROIC/ROE largo plazo B18:D18) — `build_v6.py:1136-1147`.

## 3. ROE y puente de patrimonio (corregidos)

- **ROE de partida** = beneficio neto atribuible (Historia **fila 9**, `build_v6.py:282`)
  ÷ patrimonio neto atribuible de **cierre** (Historia **fila 21**, `build_v6.py:294`);
  fila 34 = «ROE (beneficio ÷ patrimonio)». Réplica: `test_fill.py:79`
  (`ROE0 = rows[2025][9] / rows[2025][21]`). **No** es BAI ÷ patrimonio medio.
- **Puente contable**: B(t) = B(t−1) + beneficio neto atribuible + OCI − **dividendos** −
  recompras + ampliaciones + otros movimientos. **Los dividendos restan.**
- En el motor, ΔB ya incluye el reparto: **flujo_t = B(t−1)·ROE_t − ΔB_t**
  (`build_v6.py:936-937`; `test_fill.py:93-95`), con L_t = L(t−1)·(1+g_t) (`build_v6.py:934`) y
  ROE_t interpolado de ROE0 a ROE objetivo en el año 5 (`build_v6.py:938`, `test_fill.py:84,92`).
  Identidad: dividendo = BN − ΔB; g = ROE − flujo/B(t−1).

**Ejemplo numérico comprobado** (valores ilustrativos del revisor, no propuestos para ningún
caso; `verificar_contrato_c.py`, exit 0):
- E0=1000, beneficio neto=100, impuesto=30 (BAI=130), dividendos=40 → **E1 real = 1060**; el
  puente viejo (sumaba BAI y dividendos) daba 1170 y «otros movimientos» absorbía −110.
- ROE producto = 100/1060 = **0,094340**; ROE del contrato viejo (BAI/patrimonio medio) =
  130/1030 = 0,126214.
- B0=1000, ROE0=10 %, g=3 %: ΔB=30, flujo_t=70, dividendo=100−30=70.
- Si `Palancas B15` se rellena con un payout del 40 %, el motor lo lee como **ROE objetivo del
  40 %**: con B0=100, ROE0=10 %, g1=3 %, g∞=2 %, ROE_lp=10 %, r=9 % el valor pasa de **115,06**
  a **278,45 (×2,42)**.

## 4. Base de valor del motor (la del motor, no otra)

- **Valor por acción** = (VP de flujos años 1–10 + VP del valor terminal) ÷ nº de acciones
  (`build_v6.py:939-945`; nº acciones = `Análisis!C55`; `test_fill.py:99` divide entre acciones).
- **Valor terminal** = B10·(ROE_lp − g∞)/(r − g∞), descontado 10 años (`build_v6.py:940-942`;
  `test_fill.py:97-98`). r = `Análisis!C56` en C (`build_v6.py:968-969`); en C no hay impuesto
  ni f ni ajuste (τ=0, f=0, adj=0: `build_v6.py:966-968`, `test_fill.py:85-87`).
- Es un modelo de **patrimonio y ROE** (E62). **No** es un múltiplo ni un valor liquidativo.
- **Propuesta pendiente de decisión (sin números)**: usar el capital regulatorio (CET1 / ratio de
  solvencia) como «guarda», y cualquier base de valor distinta del motor (múltiplos, valor
  liquidativo en aseguradoras). Requieren decisión explícita de la persona responsable; aquí
  quedan como propuesta sin cuantificar.

## 5. Entradas mínimas por entidad (ver MAPA_ENTRADAS.jsonl, filas C)

Historia filas 9 (beneficio neto atribuible) y 21 (patrimonio neto atribuible de cierre), con
página y cita del informe oficial; fila 34 (ROE) como control; dividendos, recompras,
ampliaciones, OCI y otros movimientos del puente; nº acciones (Análisis C55); r (Análisis C56);
palancas C de la tabla anterior; g∞ en Análisis B68:D68; probabilidades de escenarios
(Análisis B69:D69) como juicio declarado. El capital regulatorio (CET1/Solvency II) entra solo
como **contexto**, nunca como output de valor (E62).

## 6. Límites explícitos del contrato

- Una plantilla que acepte cifras **no valida ese negocio** ni autoriza tratar igual a todos los
  bancos/aseguradoras: hace falta contrato específico por entidad.
- No acredita solvencia ni capital regulatorio (E62).
- El primer caso C no acredita todos los negocios financieros.

## 7. Bloqueo documental concreto (sin cambios)

- Ninguna empresa financiera está conservada (INVENTARIO_Y_HUECOS.csv, ahora con los 71 PDF del
  ZIP huella completa): las 6 de `empresas_v2` + Elis/Vidrala/Viscofan de 4.14 son
  industriales/servicios; del motor C solo hay los 2 fixtures sintéticos.
- Fuente necesaria: informe anual / 20-F / Pilar 3 / SFCR oficial **con bytes y SHA-256**. En
  este entorno solo GitHub es alcanzable de forma autenticada, así que la descarga depende de que
  la persona responsable adjunte la fuente o de un conector con acceso.

## 8. Lo que se entregaría cuando exista la candidata

Recorrido completo en copia aislada con verificación de entradas, fases A/B/C, auditoría
independiente y relevo — por paquetes Git al coordinador (Cola 3), no ejecutado por mí.
