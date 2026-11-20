# Protocolo de selección del primer caso C real · U3 / F-C1

- **Estado:** fijado **antes** de nombrar candidatos. Su SHA-256 y su hora se registran en `CANDIDATOS_C.md` §0, antes de la primera descarga.
- **Qué hace:** propone; no decide. La persona responsable elige.
- **Qué no se hace:**
  - no se usan precios, múltiplos, rentabilidades bursátiles, consenso ni ningún dato de mercado;
  - no se valora;
  - no se contacta con nadie;
  - no se fijan R, ROE objetivo, g, probabilidades, umbrales ni base de valor.
- **Contrato que debe poder alimentar la candidata:** [CONTRATO_C_DESDE_EL_MOTOR.md](CONTRATO_C_DESDE_EL_MOTOR.md).

## 0. Declaración previa (límite)

- Antes de escribir este protocolo comprobé la conectividad de red con tres sitios: `finecobank.com`, `www.hannover-re.com` y `www.bankinter.com`.
- Los tres dieron 403 del proxy: no leí ningún dato.
- Es decir, al escribir el protocolo ya tenía esos nombres en mente. Los criterios de abajo son verificables y se aplican a una lista corta publicada, para que otro agente pueda repetir o discutir la elección.

## 1. Universo

- **Lista corta declarada** en `CANDIDATOS_C.md` §1. La construí desde conocimiento general sobre entidades financieras europeas cotizadas: **no es exhaustiva**.
- Otro agente podría construir otra lista. Por eso se publican cada entidad y el motivo de cada descarte.
- La lista de las 116 empresas de la etapa 1 no está conservada. No se puede comprobar si alguna era financiera: es un hueco (**NO OBSERVABLE**).

## 2. Criterios de admisión (todos verificables sin precios)

| Id | Criterio | Cómo se verifica |
|---|---|---|
| C1 | **Tipo:** banco (entidad de crédito) o aseguradora/reaseguradora | Informe anual: descripción de la actividad y supervisor |
| C2 | **Cotizada** en un mercado regulado europeo (EEE, Suiza o Reino Unido) | Informe anual: sección de la acción o portada |
| C3 | **Idioma:** informe anual consolidado oficial en inglés, francés o español | Documento descargado del sitio oficial |
| C4 | **Disponibilidad a 10 años:** 10 informes anuales consolidados (2016–2025) y la serie de Pilar 3 (bancos) o SFCR de grupo (aseguradoras; el SFCR existe desde el ejercicio 2016), en el sitio oficial de la entidad | Para los finalistas: el **último** informe anual y el **último** Pilar 3 o SFCR se descargan con URL, fecha, HTTP, bytes, SHA-256 y páginas. Del resto se muestra que existe (URL o listado oficial), sin descargarlo. |
| C5 | **Datos que necesita el motor C:**<br>- beneficio neto atribuible a la dominante;<br>- patrimonio atribuible al cierre;<br>- estado de cambios en el patrimonio con dividendos, recompras, emisiones, OCI y, si existen, instrumentos AT1;<br>- acciones (nota del BPA).<br>Además se identifica, sin decidirla, la línea que podría ir en la fila 6 de «Ventas» (contrato §7.1, PD-4). | Páginas de los estados en el último informe anual |
| C6 | **Fuera de muestra.** No está en:<br>- `personaje_v2/empresas_v2`: Aarsleff, Hermès, Nike, Rational, Vidrala, Viscofan;<br>- los expedientes de `empresas_v2_correcciones` y `contrastes`: Vidrala, Viscofan y Elis;<br>- los ejemplos del producto: ABB, Empresa X;<br>- el frente B3: Ahold Delhaize. | `ls` y `grep` de nombres de entidades financieras en la candidata `957af65` y en las ramas `origin/coordinacion/cierre-v2` y `origin/mistral/f-alcance-real` (resultado en `CANDIDATOS_C.md` §1) |
| C7 | **Sin precios:** ninguna columna, nota ni razonamiento usa la cotización ni un dato de mercado | Revisión del propio documento |

## 3. Exclusión automática (solo si el motor no puede leer la entidad)

| Id | Exclusión | Motivo en el motor |
|---|---|---|
| X1 | Sin informe anual consolidado oficial del último ejercicio en EN, FR o ES | No hay fuente para L9 ni para L21 |
| X2 | Patrimonio atribuible ≤ 0 en el último ejercicio | V32: «el motor C no puede partir de ahí» (`build_v6.py:1187-1189`) |
| X3 | No publica por separado el beneficio y el patrimonio atribuibles a la dominante | B0 y ROE0 no se pueden documentar (`build_v6.py:282,294`) |
| X4 | Menos de 5 ejercicios consecutivos con estados consolidados | V02 y V04 (`build_v6.py:1104-1111`) |

## 4. Riesgos: se declaran y no excluyen por sí solos

| Id | Riesgo | Por qué importa en el motor C |
|---|---|---|
| R1 | **NIIF 17 / NIIF 9** (aseguradoras, 2023, con 2022 reexpresado): ruptura de serie y CSM fuera del patrimonio | Afecta a la serie de ROE (fila 34, C56) y a la referencia mecánica del crecimiento. B0 y ROE0 del último año sí son homogéneos. El CSM es beneficio futuro que no está en B. |
| R2 | **Perímetro:** fusiones, escisiones, actividades interrumpidas, reexpresiones | Rompe el CAGR del patrimonio y la media del ROE |
| R3 | **Minoritarios** materiales | El motor C no resta minoritarios (ajuste 0): B y beneficio tienen que ser atribuibles, y su coherencia hay que comprobarla |
| R4 | **AT1 dentro del patrimonio atribuible** (NIC 32) y cupones fuera de la cuenta de resultados | Cambia B0 y ROE0 según PD-3 |
| R5 | **Moneda** distinta del euro o hiperinflación | La hoja no convierte divisas |
| R6 | **Grupo mixto** banca-seguros (conglomerado) | Un juego de palancas mezcla negocios (aviso de conglomerado) |
| R7 | **Límite del modelo** (L2): negocio que el motor C no captura (reaseguro, vida con garantías, banca de inversión) | El personaje puede concluir `modelo_no_aplicable` |
| R8 | Cambio de fecha de cierre o de norma (de GAAP local a NIIF) en la ventana | Años no comparables (V04) |

## 5. Regla de elección entre candidatas admitidas

Orden lexicográfico fijo, sin umbrales numéricos. Cada paso solo desempata el anterior.

1. **Familias:** se propone, si es posible, **un banco y una aseguradora**, para que la persona elija qué rama del motor C valida primero. Si solo una familia tiene candidatas admitidas, se propone solo esa.
2. Dentro de cada familia, la que tenga **menos riesgos R2** (perímetro) en la ventana 2016–2025, según declare la propia entidad.
3. Después, **menos riesgos entre R3, R5 y R6**.
4. Después, **AT1 identificable por separado** (dentro o fuera del patrimonio), porque permite aplicar cualquiera de las dos opciones de PD-3.
5. Después, **moneda de presentación euro**.
6. Por último, idioma: español, luego inglés, luego francés.

- R1 no desempata: afecta a todas las aseguradoras por igual.
- R7 se declara siempre y no ordena.

## 6. Qué se entrega por candidata

- Criterios C1–C7 con su evidencia (documento y página) o con «no verificado» y su motivo.
- Riesgos R1–R8 aplicables.
- Qué permitiría validar del motor C (ROE de la Historia, puente, flujo, terminal, sensibilidad) y qué no.
- Si podría acabar en el límite del modelo.
- Ningún número de valoración ni de palanca.

*Protocolo de propuesta. No es una decisión ni una política. La elección y cualquier umbral corresponden a la persona responsable.*
