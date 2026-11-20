# Corrección F3 · Mistral C/F · sobre la respuesta a F2 (`195766f` … `98bdf8f`)

- **Para:** Mistral C/F, rama `mistral/f-alcance-real`.
- **De:** el coordinador, según [REVISION_F2_195766f_98bdf8f.md](REVISION_F2_195766f_98bdf8f.md).
- **Comprobado por el coordinador en `build_v6.py` de la candidata:** el motor se elige en `Análisis!C62` (V01, `:1102-1103`; `Diagnóstico V6` A5). `Palancas C6` = «Financiera» solo produce el aviso REVISAR (`:589-590`) y bloquea A y B (V11, `:1133`).

## Clasificación

- **Cerrados:** F2-D1 (el inventario se reproduce byte a byte desde el ZIP) y F2-D4.
- **Cerrados con límites:** D2, D3, D5, D6 (las horas, cerradas), D7 y la ENTREGA.
- **Se conserva:**
  - los 71 PDF con su huella;
  - el puente 1060;
  - X14/X15/X16/X18/B68;
  - el ROE de cierre;
  - el manifiesto de `98bdf8f` (46/46).

## Defectos

| | Defecto | Prueba de cierre |
|---|---|---|
| **F3-R5 (medio)** | El contrato y el criterio 1 del protocolo eligen el motor C con `Palancas C6`. Contraejemplo: C6 = Financiera y C62 = «Sí» sale motor A bloqueado, no C | El motor, en `Análisis!C62`. C6, como aviso y bloqueo de A y B |
| **F3-R3** | El inventario no registra el `.bat` de Ahold (`…/descargas_bat/descargar_fuentes_ahold.bat`, `04feebd4…d53d88`). `README.md:28` y `SELECCION.csv` dicen que no existe | Registrado, con su huella. Textos corregidos |
| **F3-R4** | El alcance se declara solo en positivo: 323 de los 6799 archivos quedan fuera sin aviso | Alcance negativo declarado |
| **F3-R6/R7/R8** | Unas diez citas de línea desplazadas (p. ej. el flujo está en 929-930, no en 936-937). Falta la quiebra, `BJ = (1−p)·BI + p·rec`. «Dividendo = BN − ΔB» se da sin la condición de que no haya OCI. Falta el ROE de cierre frente a apertura | Citas verificadas línea a línea. Fórmulas completas |
| **F3-R9/R11/R14/R15** | Comandos de ENTREGA_B_PM1 y B3_C1 que no se ejecutan tal cual. Textos de antes de F2. RESPUESTA_F2 da por cerrado lo que sigue con límites y dice que el control «no cambia desde 57b34a6». `resultado` compuesto. Variables sin definir. `tareas_control` sin B-PM1. Hora final incorrecta | Corregido |
| **F3-R12** | Hay dos contratos y dos protocolos de C en paralelo: los de U3 (`coordinacion/cierre_v2/u3_motor_c/`, encargo de la persona responsable) y los de F. En las cuatro discrepancias, el código da la razón a U3 | **No se mantienen dos versiones.** El contrato de F se alinea con el de U3, o se retira a favor de él. El protocolo de F no nombra candidatas: la elección es de la persona responsable sobre U3 |
| **F3-R13** | El texto suelto «ibraltar» y los acentos quitados en dos filas B del mapa | Corregido |

**Bloqueos que no son de F:** la etapa 1 de Ahold (U2) y los documentos de los candidatos de C (U3) son de la persona responsable.
