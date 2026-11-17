# Candidatos para el primer caso C real · U3 / F-C1

- **Estado:** propuesta. La persona responsable elige; nada queda designado.
- **Se aplica:** [PROTOCOLO_SELECCION_C.md](PROTOCOLO_SELECCION_C.md) sobre el contrato [CONTRATO_C_DESDE_EL_MOTOR.md](CONTRATO_C_DESDE_EL_MOTOR.md).
- **Sin precios:** ningún dato de mercado interviene.
- **Límite principal:** **no he podido descargar ni leer ningún documento oficial de los candidatos**, así que la prueba documental de C4 y C5 queda **NO VERIFICADA** (ver §4 e `INDICE_FUENTES.csv`). Lo que digo de cada entidad es **conocimiento previo, pendiente de verificar en su fuente**, y lo marco **[a verificar]**.

## 0. Orden (protocolo antes de candidatos)

| Paso | Hora UTC | Huella |
|---|---|---|
| Contrato y protocolo escritos | 2026-11-17T09:30:00Z | `PROTOCOLO_SELECCION_C.md` en ese momento: `3e28d9c0456a9a3197e9a9430e988cde5cbde06b8cfa79e1608f52f836317855`<br>`CONTRATO_C_DESDE_EL_MOTOR.md`: `4d4798b6…3995d` (después solo cambié la ruta del script de réplica por su ruta absoluta; su huella final está en el resumen de entrega) |
| Primera petición a un sitio de candidato tras el protocolo | 09:31Z | `INDICE_FUENTES.csv` |
| Antes del protocolo | < 09:30Z | Prueba de conectividad a tres sitios, sin datos. Declarada en el protocolo, §0. |

## 1. Lista corta (universo declarado, no exhaustivo) y criterio C6

**C6, fuera de muestra:**
- en la candidata `957af65` no hay ninguna entidad financiera entre las empresas de `empresas_v2` ni en los expedientes;
- ninguno de los nombres de abajo aparece salvo como prestamista citado en los textos de Vidrala y Viscofan (`grep` sobre `personaje_v2/` y `contrastes/`);
- tampoco aparecen en `origin/coordinacion/cierre-v2` ni en `origin/mistral/f-alcance-real` (`git grep`);
- la lista de las 116 empresas no está conservada: **NO OBSERVABLE**.

Las marcas de riesgo siguen el protocolo, §4. Todas son **[a verificar]**.

| Entidad | Familia | C3 idioma | R2 perímetro 2016–2025 | R3, R5, R6 | Resultado en el protocolo |
|---|---|---|---|---|---|
| FinecoBank (IT) | banco | EN | sin operación societaria relevante conocida | sin minoritarios conocidos; EUR; no mixto | **1.º banco** |
| Bankinter (ES) | banco | ES/EN | escisión y reparto de Línea Directa (2021) | mixto banca-seguros hasta 2021 (R6) | descartado en el paso 2 |
| CaixaBank (ES) | banco | ES/EN | fusión con Bankia (2021) | VidaCaixa consolidada (R6) | descartado en el paso 2 |
| Banco Sabadell (ES) | banco | ES/EN | venta de TSB (anunciada en 2025) | GBP (R5) | descartado en el paso 2 |
| Unicaja (ES) | banco | ES | fusión con Liberbank (2021) | — | descartado en el paso 2 |
| Santander, BBVA (ES) | banco | ES/EN | varias | minoritarios materiales, varias monedas, hiperinflación (R3, R5) | descartados en los pasos 2 y 3 |
| Handelsbanken (SE) | banco | EN | salidas de Dinamarca, Finlandia y Países Bajos | SEK (R5) | descartado en el paso 2 |
| Nordea (FI) | banco | EN | traslado de sede (2018) y ventas en los países bálticos | — | descartado en el paso 2 |
| KBC (BE) | banco | EN | — | banca-seguros (R6) | descartado en el paso 3 |
| Hannover Rück (DE) | aseguradora (reaseguro) | EN | sin operación societaria relevante conocida | minoritarios por filiales no participadas al 100 % (R3, a cuantificar); EUR | **1.ª aseguradora** |
| Mapfre (ES) | aseguradora | ES/EN | varias (Brasil) | minoritarios materiales, hiperinflación (R3, R5) | descartada en el paso 3 |
| Talanx (DE) | aseguradora | EN | — | minoritarios materiales (Hannover Re) (R3) | descartada en el paso 3 |
| Sampo (FI), Tryg (DK) | aseguradora | EN | escisión de Mandatum y Topdanmark; adquisición de RSA Escandinavia | DKK en Tryg | descartadas en el paso 2 |
| NN Group (NL) | aseguradora | EN | Delta Lloyd (2017) | — | descartada en el paso 2 |

El paso 1 (un banco y una aseguradora) sale de la regla del protocolo, §5.1, no de una preferencia sobre los resultados.

---

## 2. Candidato 1 · FinecoBank S.p.A. (banco)

### Fuentes

**Existencia del sitio:** comprobada solo por cabecera (`finecobank.com` → 302 → `it.finecobank.com`).

**Pendiente de localizar y descargar** (bloqueado; ver §4):
- *Annual Report / Bilancio consolidato* 2025, y la serie desde 2016;
- *Pillar III Disclosure* al 31-12-2025 y su serie.

**C1–C5:** [a verificar]. Banco cotizado en Borsa Italiana con informes en inglés. Grupo de perímetro estrecho (la filial irlandesa de gestión de activos).

### Qué permitiría validar del motor C

- **ROE de la Historia** (L9/L21):
  - con un perímetro estable, la serie de 10 años del beneficio atribuible y del patrimonio atribuible debería ser homogénea, salvo la transición a NIIF 9 en 2018 [a verificar];
  - permite comprobar L34, C56 y la referencia mecánica del CAGR del patrimonio sin ruido de fusiones.
- **Puente de patrimonio:**
  - prueba el puente completo con partidas reales: dividendos, reservas de valoración (OCI de la cartera de renta fija y actuariales), autocartera para planes de incentivos y, si existen, instrumentos AT1 y sus cupones dentro del patrimonio [a verificar];
  - es un caso útil para PD-3.
- **Flujo:** en los años con restricciones supervisoras al dividendo (2020) [a verificar], el reparto real se separa de beneficio − ΔB. Así se ve en un caso real qué significa el excedente limpio (contrato §3 y §6).
- **Terminal y sensibilidad:** el tornado y las tablas r × g∞ del producto se ejercitan con un ROE de partida alto. Así se comprueban las condiciones `BS` (ROE_lp > g∞, r > g∞) y los semáforos de ROE frente al sector, que saltarían como desviación justificable, no como error.

### Qué no valida

- El capital regulatorio: el Pilar 3 da contexto (PD-1) y la hoja no lo lee.
- La calidad del negocio de comisiones y corretaje.
- Un banco de crédito típico: Fineco tiene poco riesgo de crédito, así que no cubre provisiones ni morosidad.
- Que el motor sirva para otros bancos.

### Riesgos

| Riesgo | Situación |
|---|---|
| R4 · AT1 | Si hay AT1 dentro del patrimonio atribuible [a verificar], hace falta decidir PD-3 antes de rellenar L9 y L21 |
| R8 · NIIF 9 (2018) y NIIF 16 (2019) | Cambios de norma en la ventana: ajustes de primera aplicación en el patrimonio de apertura |
| R2 · perímetro | Bajo [a verificar]. La salida de UniCredit (2019) es un cambio de accionista, no de perímetro, pero cambió la cartera de inversiones. |
| R3 · minoritarios | Previsiblemente ninguno [a verificar] |
| PD-4 · «Ventas» | Habría que decidir la línea: margen de intermediación o ingresos totales |

**¿Límite del modelo?** Posible, no probable.
- El valor de Fineco depende más de los ingresos por comisiones que del patrimonio contable.
- El personaje podría juzgar (L2) que una base de patrimonio y ROE no lo captura.
- No hay motivo mecánico: el motor puede calcularlo.

---

## 3. Candidato 2 · Hannover Rück SE (aseguradora, reaseguro)

### Fuentes

- **Sitio oficial:** `www.hannover-re.com` contesta **403 de CloudFront** a curl. Es un rechazo del propio sitio, no del proxy.
- No cambié el agente de usuario para sortearlo.
- **Pendiente:** *Annual Report* 2025 y *Solvency and Financial Condition Report (Group)* 2025, y sus series desde 2016 (el SFCR existe desde el ejercicio 2016).

**C1–C5:** [a verificar]. Reaseguradora cotizada en Fráncfort, con informes en inglés y presentación en euros. Su matriz, Talanx, tiene la mayoría: es accionista, no perímetro.

### Qué permitiría validar del motor C

- **Puente de patrimonio con OCI material:**
  - con NIIF 9 y NIIF 17, los movimientos de tipos de interés pasan por el OCI;
  - es el caso que más directamente pone a prueba el excedente limpio: la diferencia entre beneficio − ΔB y el dividendo real (contrato §6, variante con OCI).
- **ROE de la Historia con ruptura de serie (R1):**
  - comprueba cómo trata el contrato la reexpresión de 2022 bajo NIIF 17 (PD-6);
  - L9/L21 del último año son homogéneos;
  - C56 y la referencia mecánica mezclarían normas si no se decide.
- **Flujo y terminal:** dividendo ordinario más extraordinario, sin recompras relevantes [a verificar]. Esto pone a prueba el reparto implícito 1 − g/ROE frente al real.
- **Minoritarios (R3):**
  - comprueba que L9 y L21 se toman como atribuibles;
  - el motor C no resta minoritarios.

### Qué no valida

- La solvencia: el SFCR da el ratio de Solvencia II solo como contexto (PD-1).
- Las reservas técnicas y el CSM. Bajo NIIF 17, el CSM es beneficio futuro que no está en el patrimonio, y el motor no lo ve.
- El riesgo de catástrofes.
- Que el motor sirva para aseguradoras directas de vida o no vida.

### Riesgos

| Riesgo | Situación |
|---|---|
| R1 · NIIF 17/9 | Desde 2023 con 2022 reexpresado: ruptura de serie y CSM fuera del patrimonio. Es un riesgo, no una exclusión: el motor lee el último año. |
| R3 · minoritarios | Hay filiales con socios externos [a verificar]. Su peso hay que cuantificarlo en el balance. |
| R4 · AT1 | Su capital híbrido sería deuda subordinada fuera del patrimonio [a verificar]. Si es así, PD-3 no cambia B0. |
| R7 · reaseguro | Riesgo alto de límite del modelo (§3, más abajo) |
| PD-4 · «Ventas» | Primas brutas o ingresos de seguros (NIIF 17): hay que decidirlo |

**¿Límite del modelo?** **Probable que se discuta.**
- La gramática prevé L2 para «seguros» o «capital regulatorio» que el motor C no capture (`ANEXO_B_gramatica_damodaran.md:112`).
- En el reaseguro, el resultado depende de la siniestralidad catastrófica y de la liberación de reservas.
- Bajo NIIF 17 parte del valor está en el CSM, fuera de B.
- Si se elige, la conclusión `modelo_no_aplicable` es legítima y también informa: valida que el sistema llega al límite correctamente.

---

## 4. Qué bloqueó la verificación y qué hace falta

| Bloqueo | Detalle | Lo que lo resolvería |
|---|---|---|
| Red del entorno | Al empezar, el proxy rechazaba todos los sitios oficiales (403). Añadí al entorno personal, con aprobación, cinco hosts: `finecobank.com`, `www.finecobank.com`, `www.hannover-re.com`, `hannover-re.com` e `it.finecobank.com`. **Esos hosts siguen en el entorno**: quitarlos, si se desea, es una decisión de la persona. | — |
| Permisos de la sesión | Con el host ya permitido, el clasificador de permisos **denegó** las descargas desde `it.finecobank.com` («Unauthorized Access»). No lo rodeé. | Que la persona autorice esas descargas (regla de permiso para curl a esos hosts) o descargue ella los documentos |
| Sitio de Hannover Re | CloudFront contesta 403 a curl | Que la persona descargue el informe anual 2025 y el SFCR 2025 desde un navegador y los entregue con su SHA-256 |

**Con los dos documentos clave de cada candidato en `<e_work>/u3_c/pdf/`**, la comprobación pendiente es:
- C4: la serie existe, con un listado de URL de 2016–2025;
- C5: páginas de la cuenta de resultados, el balance y el estado de cambios en el patrimonio;
- R3/R4: el peso de los minoritarios y de los AT1;
- `INDICE_FUENTES.csv` completo (URL, fecha, HTTP, bytes, SHA-256, páginas).

*Ninguna entidad queda designada. No se fija ningún parámetro, umbral ni base de valor. No hubo contacto con personas ni empresas; las únicas peticiones fueron las cabeceras HTTP del índice.*
