# Selección del caso C tras descartar FinecoBank · U3 / F-C1

- **Autoría:** subagente de fuentes del coordinador, 17-nov-2026, 13:45–13:55 UTC. Hace falta la revisión de un contexto distinto.
- **Estado:** propuesta y registro de acceso. **No es una decisión, una designación ni una aprobación.** La persona responsable elige.
- **Rutas:** `<fuentes_c2>` = `<fuentes_c2>/`; `<u3>` = `<aux>/coordinacion/cierre_v2/u3_motor_c/` (rama `coordinacion/cierre-v2`, `git pull --ff-only` = «Already up to date», HEAD `f2fb3196`, sin cambios locales).
- **Sin precios (C7).** No he consultado precios, cotizaciones ni datos de mercado. No he contactado con nadie. Sin commits ni push.
- **Resultado en una línea:** **ningún candidato es decidible.** Los tres que permite el encargo (Hannover Rück, KBC, Talanx) quedaron sin acceso a su sitio oficial, así que no hay documento descargado, ni verificación de edición, período, perímetro, C1–C7 o R2/R3/R5/R6 con página. No he forzado ninguno.

---

## 1. Reaplicación del protocolo (antes de mirar datos)

### 1.1 Orden y huellas

| Paso | Hora UTC | Huella o evidencia |
|---|---|---|
| Protocolo, sin cambios desde su fijación | comprobado a 13:47:15Z | `PROTOCOLO_SELECCION_C.md` = `3e28d9c0456a9a3197e9a9430e988cde5cbde06b8cfa79e1608f52f836317855`, **igual** que la registrada a las 09:30Z en `CANDIDATOS_C.md` §0 |
| Lista y contrato usados | 13:47:15Z | `CANDIDATOS_C.md` = `296fad5b…d174bd`; `CONTRATO_C_DESDE_EL_MOTOR.md` = `cc9efb21…26bf2ad7` |
| Reaplicación escrita | **13:47:29Z** (mtime) | `<fuentes_c2>/00_REAPLICACION_ANTES_DE_DATOS.txt`, SHA-256 `99a83450e9e1817f42319606cb50c3102f71ede36a4f40b98733634b53ec1e99`. Dentro pone «13:47:30Z»: es la hora que escribí a mano; la del sistema es 13:47:29Z. No lo he editado para no cambiar su huella. |
| Primera petición de red a un candidato | 13:47:37Z | `INDICE.tsv` |
| Última petición | 13:48:06Z | `INDICE.tsv` |

### 1.2 Aplicación de §5 sobre `CANDIDATOS_C.md` §1 sin FinecoBank

Uso las marcas de la lista **tal como están** (todas [a verificar]). No amplío la lista: §1 del protocolo admite que no es exhaustiva, pero no fija cómo ampliarla, y ampliarla justo después de que la primera candidata fallara abre la puerta a elegir a posteriori. Además, con tope de tres candidatos, la lista existente bastaba para llenarlo.

| Paso del protocolo | Bancos | Aseguradoras |
|---|---|---|
| §5.1 familias | se busca un banco (la plaza de Fineco queda vacía) | se busca una aseguradora |
| §5.2 menos R2 | Todos llevan R2 marcado salvo **KBC** («—») → **KBC, 1.er banco** | Sin R2 marcado: **Hannover Rück** y **Talanx** |
| §5.3 menos R3/R5/R6 | KBC lleva R6 (banca-seguros), pero es el único sin R2: el paso 3 no llega a desempatar | Ambas tienen una marca R3. Mantengo el orden heredado: Hannover («a cuantificar») antes que Talanx («material»). *Interpretación heredada, no recuento:* por número de marcas empatan. |
| §5.4–5.6 | no se llegan a aplicar: exigen datos | no se llegan a aplicar |

**Orden de verificación declarado (máximo 3):** 1) Hannover Rück (1.ª aseguradora); 2) KBC Group (1.er banco); 3) Talanx (2.ª aseguradora, porque Hannover no fue accesible).

**Conocimiento previo declarado, sin datos** (escrito en el registro de 13:47:29Z):
- Las sociedades alemanas publican el informe en alemán y en inglés. El problema C3 de Fineco (inglés no fehaciente) **podría repetirse** en Hannover y Talanx. [a verificar]
- La marca «—» de R2 para KBC puede ser incompleta: tengo en mente adquisiciones y ventas en la ventana (Europa central y oriental; Irlanda). [a verificar] Si se confirma, KBC perdería su puesto en §5.2 y el orden de bancos habría que rehacerlo.

---

## 2. Candidato 1 · Hannover Rück SE (aseguradora, reaseguro)

### Acceso

| Petición | Resultado |
|---|---|
| `https://www.hannover-re.com/`, curl por defecto, 13:47:37Z | El proxy **sí** deja pasar (`200 Connection Established`). El sitio contesta **HTTP/2 403**, `server: CloudFront`, `x-cache: Error from cloudfront`, 919 bytes. Es un rechazo del propio sitio. |
| `https://hannover-re.com/`, 13:47:38Z | 302 → `https://www.hannover-re.com:443/` (el host anterior) |
| Reintento con agente de usuario de navegador, el mismo método que usó la verificación de Fineco (`-A 'Mozilla/5.0'`) | **Denegado** por el clasificador de permisos de la sesión («Unauthorized Access»). No lo reintenté ni lo rodeé, y no usé otra herramienta para llegar al mismo sitio. |

### Verificación

- Edición, período, perímetro, correspondencia informe anual–SFCR: **no verificados** (sin documento).
- C1–C7, R2/R3/R5/R6: **no verificados con página.** Solo C6 está comprobado (ver §5).
- C4 sobre los 10 años: **no verificado.**

### Conclusión: **no decidible** (no accesible)

Lo que validaría y lo que no queda como en `CANDIDATOS_C.md` §3, todo [a verificar]. Sigue el riesgo alto de límite del modelo (R7, reaseguro; L2 legítimo).

---

## 3. Candidato 2 · KBC Group NV (banco)

### Acceso

| Petición | Resultado |
|---|---|
| `https://www.kbc.com/`, 13:47:57Z | **CONNECT 403 del proxy.** Estado del proxy: `connect_rejected`, `www.kbc.com:443`, 13:47:58.049Z |
| `https://www.kbc.com/en/investor-relations.html`, 13:47:58Z | **CONNECT 403 del proxy** (13:47:58.295Z) |

Según el encargo, no lo esquivé ni cambié la red, y **detuve el candidato**.

### Verificación

Nada verificado con página. C6 comprobado (ver §5).

### Conclusión: **no decidible** (host bloqueado)

**Qué validaría, si fuera accesible** (conocimiento previo, todo [a verificar]):
- un banco de crédito típico, con provisiones y morosidad, que Fineco no cubría;
- presentación en euros;
- AT1, que habría que localizar en el patrimonio para PD-3.

**Qué no validaría:**
- la solvencia y el capital regulatorio (contrato §7.1);
- el negocio asegurador integrado: KBC es banca-seguros (**R6**, conglomerado), y un único juego de palancas mezclaría negocios;
- si el R2 previsto se confirma, la serie de 10 años del ROE y el CAGR del patrimonio estarían afectados por cambios de perímetro.

---

## 4. Candidato 3 · Talanx AG (aseguradora)

### Acceso

| Petición | Resultado |
|---|---|
| `https://www.talanx.com/`, 13:48:05Z | **CONNECT 403 del proxy.** Estado: `connect_rejected`, `www.talanx.com:443`, 13:48:06.191Z |

Candidato detenido sin esquivar el bloqueo.

### Verificación

Nada verificado con página. C6 comprobado (ver §5).

### Conclusión: **no decidible** (host bloqueado)

**Qué validaría, si fuera accesible** (todo [a verificar]):
- **R3 a fondo.** Talanx consolida Hannover Re sin ser su único dueño, así que los minoritarios son materiales. Serviría para comprobar que L9 y L21 se toman **atribuibles** y que el motor C, que no resta minoritarios, recibe la base correcta.
- El puente de patrimonio con OCI de NIIF 9/17 y la ruptura de serie R1 (PD-6).

**Qué no validaría:**
- la solvencia (ratio de Solvencia II solo como contexto, PD-1);
- el CSM ni las reservas técnicas;
- el riesgo de catástrofes.

Contiene el reaseguro de Hannover, así que hereda parte del riesgo R7.

---

## 5. C6 · fuera de muestra (lo único comprobado)

| Repositorio y referencia | Hannover / Talanx | KBC |
|---|---|---|
| `munger-v2` HEAD (`03e7851`), `git grep -i` | 0 archivos | 6 archivos, **solo** en textos de fuente de Elis (`empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/elis*/Elis/texto/`), donde KBC aparece como contraparte financiera, no como empresa analizada |
| Candidata `957af65` (presente en `munger-v2`), fuera de `/texto/` | 0 | 0 |
| `munger-v2-evidencias-mistral` HEAD y `origin/coordinacion/cierre-v2` | solo documentos de coordinación de U3 (`CANDIDATOS_C.md`, `PROTOCOLO_SELECCION_C.md`, `INDICE_FUENTES.csv`, `LEEME.md`, `CONTROL.json`, `ESTADO.md`, `DECISIONES_PARA_EL_USUARIO.md`) | igual |
| `origin/mistral/f-alcance-real` | `CONTRATO_C_PROPUESTA.md`, `PROTOCOLO_CONGELADO.md` (coordinación) | igual |

**Interpretación:** los tres cumplen C6. La lista de las 116 empresas de la etapa 1 sigue **NO OBSERVABLE**.

---

## 6. Hosts bloqueados y qué haría falta

| Host | Bloqueo | Qué lo resolvería (lo decide la persona responsable) |
|---|---|---|
| `www.kbc.com` | **CONNECT 403 del proxy** (política del entorno) | Añadir el host, y el de sus documentos si es distinto, al entorno; o que la persona descargue los documentos |
| `www.talanx.com` | **CONNECT 403 del proxy** | Igual |
| `www.hannover-re.com` | **No es del proxy:** el sitio (CloudFront) da 403 a curl. El reintento con agente de usuario de navegador lo **denegó el clasificador de permisos**. | Autorización expresa para ese reintento, o que la persona descargue el informe anual 2025 y el SFCR de grupo 2025 desde un navegador y los entregue con su SHA-256 |

Los hosts de Fineco y Hannover que ya estaban en el entorno siguen allí; no he tocado la configuración de red.

---

## 7. Observación para la persona responsable (no es una decisión)

- **C3 estricto.** Si C3 se lee como «versión fehaciente en EN, FR o ES», como sugiere el descarte de Fineco, es previsible [a verificar] que tampoco encajen las sociedades alemanas (Hannover, Talanx) ni, posiblemente, las belgas, cuya versión original sería la neerlandesa.
- **C4 estricto.** Exige 10 informes **consolidados** 2016–2025 y la serie de Pilar 3 o SFCR de grupo desde 2016.
- **Qué queda.** Con las dos lecturas estrictas, en la lista corta quedarían sobre todo las entidades españolas (todas con R2 marcado) y alguna de las nórdicas o neerlandesas. Ninguna está verificada.
- **Qué decidir.** La persona puede ampliar la lista con criterios declarados antes de mirar datos, flexibilizar C3/C4 o abrir el acceso de red a los candidatos detenidos.

---

## 8. Qué validaría del motor C y qué no, en general

- **Validaría**, con un candidato verificado:
  - la Historia (L9 y L21 atribuibles, C5/V02/V04);
  - el puente de patrimonio (contrato §6);
  - PD-3 (AT1) y PD-4 («Ventas»);
  - el flujo frente al reparto real y el terminal;
  - la sensibilidad del producto.
- **No validaría**, con ningún candidato:
  - la **solvencia ni el capital regulatorio**, que quedan fuera del motor (contrato §7.1; `Análisis!E62`). El Pilar 3 o el SFCR sirven solo para comprobar la coherencia documental y como contexto de PD-1.
  - el CSM, las reservas técnicas ni la calidad de la cartera;
  - que el motor sirva para otras entidades.
- **Hoy, con los tres candidatos, nada de lo anterior está verificado.**

*Sin valoración, sin palancas y sin precios. Ninguna cifra de entidad aparece en este documento porque no se ha leído ningún documento de los candidatos.*
