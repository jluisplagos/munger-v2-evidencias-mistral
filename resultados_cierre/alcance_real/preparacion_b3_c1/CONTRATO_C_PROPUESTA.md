# Contrato económico propuesto · primer caso C real (banco o aseguradora) · F-C1

**Estado: PROPUESTA corregida (F2-D3 y F3-R5…R8), alineada con el contrato U3 de la persona
responsable, no ejecutada, no validada.** No se mantienen dos versiones (F3-R12): donde F y U3
disentían, el código da la razón a U3 y aquí se adopta U3. Referencia paralela:
`coordinacion/cierre_v2/u3_motor_c/CONTRATO_C_DESDE_EL_MOTOR.md` (rama `coordinacion/cierre-v2`).
El motor C solo tiene los dos fixtures sintéticos de `v6/pruebas/fixtures/`
(`Fixture_motorC_palancas_A.xlsx`, `Fixture_motorC_original.xlsx`; palancas B14 0,03/0,06/0,08 ·
B15 0,10/0,14/0,16 · B16 vacío · B18 0,10/0,13/0,15; valores esperados B78:D78 en el LEEME.txt).
Ningún recorrido real acreditado.

Todas las citas son de `jluisplagos/munger-v2 @ 957af65` (solo lectura); `build_v6.py` = `B6`,
`test_fill.py` = `TF`, `patch_v62_base.py` = `P62`, `relacion_entradas_materiales.py` = `REL`.
Verificación numérica: `../correccion_f2/scripts/verificar_contrato_c.py` (exit 0; salida en
`../correccion_f3/evidencias/r5_r8_verificar_contrato_c.txt`); citas línea a línea verificadas en
`../correccion_f3/evidencias/r6_citas_reales_957af65.txt`.

## 1. Dónde se elige el motor C (corregido, F3-R5)

- La fase A elige **`Análisis!C62`** (lista en `B6:169-170`): «No · banco o aseguradora» → motor C.
- `Diagnóstico V6!C5` solo traduce C62 (`B6:581-582`); validación V01 (`B6:1102-1103`).
- **`Palancas C6` NO elige el motor**: con C6 = «Financiera (banco o aseguradora)» y motor A o B sale
  REVISAR (`B6:588-590`) y V11 = NOA, modelo no aplicable (`B6:1132-1133`). La nota «Financiera →
  motor C» está en `B6:426`.
- **Contraejemplo:** C6 = Financiera y C62 = «Sí» → motor A bloqueado por V11, **no** motor C.

## 2. Palancas reales del motor C (X = B/C/D = MALO/NORMAL/BUENO)

| Celda | En el motor C es | Cita (verificada) |
|---|---|---|
| `Palancas!X14` | **Crecimiento del patrimonio, años 1–5**; en los años 6–10 g_t baja en **línea recta** hasta g∞ (llega en el año 10) | `B6:444-445,926`; `REL:143-144`; `REF["Motor!Q7"]` |
| `Palancas!X15` | **ROE objetivo, alcanzado en el año 5** (NO es payout; no hay celda de payout: el reparto es un resultado, 1 − g_t/m_t) | `B6:446-449,928`; `REL:145-146`; `REF["Motor!AK7"]` |
| `Palancas!X16` | S2C: **no se usa en C** (el motor pone 1; la gramática exige dejar B16:D16 vacías) | `B6:450-452,971`; `REL:147-148` |
| `Palancas!X17` | No es entrada: copia `Análisis!X68` | `B6:453,479-480` |
| `Palancas!X18` | **ROE a largo plazo (tras el año 10)**, solo entra en el terminal | `B6:454-456,932`; `REL:149-150` |
| `Análisis!X68` | **g∞** | `B6:972`; V15 `B6:1142-1145`; `REL:151-152` |
| `Palancas!C22/C23` | **Probabilidad de quiebra y recuperación** (vacío = 0): `BJ = (1−p)·BI + p·rec` **también aplica en C** | `B6:507-509,936` |

## 3. Historia y ROE de partida

- `Historia!L9` = **beneficio neto atribuible** (después de impuestos y minoritarios) `B6:282`;
  `Historia!L21` = **patrimonio neto atribuible al cierre** `B6:294`;
  `Historia!X34` = ROE del año = X9/X21 (`B6:312,328`; `REF["Historia!L34"]`).
- **ROE de partida = L9/L21 de cierre** (`TF:79`). **No** es BAI ÷ patrimonio medio.
- Matiz (U3 §7.2): el motor aplica m_t al patrimonio de **apertura**, mientras la Historia mide el
  ROE sobre el de **cierre**: en el caso 1000/100/40, 9,434 % (cierre) frente a 10,000 % (apertura).
  Es una convención del producto; cambiarla es propuesta pendiente de decisión.

## 4. Flujo y puente de patrimonio (corregidos)

- `L_t = L(t−1)·(1+g_t)` (`B6:927`); `m_t = ROE0 + (ROE_obj − ROE0)·min(t,5)/5` (`B6:928`, `TF:93`);
  **flujo_t = B(t−1)·ROE_t − ΔB_t** (`B6:929-930`; `TF:94-95`); VP flujos `BE` (`B6:931`).
- **Puente contable (control de datos, fuera de la hoja):** E_t = E(t−1) + beneficio neto atribuible
  + OCI (con su signo) − **dividendos** − recompras + ampliaciones/emisiones ± AT1 ± otros
  movimientos con nombre. **Los dividendos restan.** El residuo no explicado se declara hueco,
  nunca se absorbe en «otros» (tolerancia: propuesta pendiente de decisión, sin número).
- **Excedente limpio:** flujo = reparto (dividendos + recompras − emisiones) **solo si** el
  patrimonio cambia únicamente por beneficio y reparto (OCI = 0 y sin otros movimientos); el motor
  no proyecta OCI. Variante comprobada: E0=1000, BN=100, OCI=−25, div=40, recompras=10 → E1=1025,
  BN−ΔB = 75 pero reparto real = 50; la diferencia 25 = −OCI.

**Ejemplo numérico comprobado** (ilustrativo, no propuesto para ningún caso; exit 0):
E0=1000, BN=100, impuesto=30 (BAI=130), div=40 → **E1 = 1060** (puente viejo 1170, «otros» −110);
ROE cierre **0,094340** vs viejo (BAI/medio) 0,126214; B0=1000, ROE0=10 %, g=3 % → ΔB=30,
flujo=70, dividendo=70. Si `Palancas B15` se rellena con un payout del 40 %, se lee como ROE
objetivo 40 %: con B0=100, ROE0=10 %, g1=3 %, g∞=2 %, ROE_lp=10 %, r=9 % el valor pasa de **115,06**
a **278,45 (×2,42)**. Con quiebra p=10 %, rec=20 (C22/C23): **BJ = 105,55**.

## 5. Terminal, quiebra y valor por acción (completo, F3-R7)

- Flujo año 11: `BF = B10·(ROE_lp − g∞)` (`B6:932`; `TF:99-100`); `BG = BF/(r−g∞)` (`B6:933`);
  `BH = BG/(1+r)^10` (`B6:934`); `BI = BE + BH + 0` (`B6:935`).
- **Quiebra:** `BJ = (1−p)·BI + p·rec` con p = `Palancas!C22`, rec = `Palancas!C23` (`B6:936`).
- **Por acción:** `BK = BJ / Análisis!C55` (`B6:937,964`). El valor por acción es **BJ ÷ nº
  acciones**, no (VP+VT) ÷ acciones sin quiebra.
- En C son fijos τ = 0, f = 0, ajuste = 0 (`B6:960-962`; `TF:86-88`) y r = `Análisis!C56`
  (`B6:963`). Condiciones de cálculo `BS` (`B6:919-922`): r > g∞, ROE_lp > 0 y > g∞, B0 > 0.

## 6. Base de valor y propuestas pendientes de decisión (sin números)

- La base de valor es **la del motor**: VP a r de los flujos B(t−1)·ROE_t − ΔB_t más terminal de
  Gordon sobre B10, con quiebra, dividido entre acciones. **No** es un múltiplo ni un valor
  liquidativo.
- Pendientes de decisión de la persona responsable (alineado con U3 §8, sin números aquí):
  PD-1 guarda de capital regulatorio (aviso, no cálculo de valor); PD-2 base de valor alternativa
  (otro método); PD-3 tratamiento de AT1; PD-4 qué va en «Ventas» (Historia fila 6) en una
  financiera (V02/V03/V04 la exigen aunque no entre en el cálculo C); PD-5 tolerancia del puente;
  PD-6 reexpresiones. E62 (`P62:255-257`): el motor C **NO valida la solvencia ni el capital
  regulatorio** de ningún banco o aseguradora.

## 7. Límites explícitos

- Una plantilla que acepte cifras **no valida ese negocio** ni autoriza tratar igual a todos los
  bancos/aseguradoras: contrato específico por entidad; si el personaje juzga que el motor no
  captura el negocio, la salida es `modelo_no_aplicable` (L2) y se conserva el juicio cualitativo.
- El primer caso C no acredita todos los negocios financieros.

## 8. Bloqueo documental concreto (sin cambios; de la persona responsable)

- Ninguna empresa financiera está conservada (INVENTARIO_Y_HUECOS.csv: 71/71 PDF huella completa,
  todos de Vidrala/Viscofan/Elis). U3 (`u3_motor_c/CANDIDATOS_C.md`) nombra candidatas, pero sus
  descargas están bloqueadas (403 del proxy; FinecoBank denegado por permisos de sesión, Hannover
  Re 403). Hace falta que la persona responsable autorice las descargas o entregue los documentos
  (informe anual y Pilar 3 / SFCR, con bytes y SHA-256). La elección de candidata es suya sobre
  U3; este paquete no nombra candidatas (F3-R12).

## 9. Lo que se entregaría cuando exista la candidata

Recorrido completo en copia aislada con verificación de entradas, fases A/B/C, auditoría
independiente y relevo — por paquetes Git al coordinador (Cola 3), no ejecutado por mí.
