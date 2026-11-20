# Encargo para Mistral · M13 · Las 8 finalistas del universo: datos de hoy e historia de diez años

**Para pegar en ventanas nuevas de Mistral, una por bloque (dos empresas por bloque).** Fecha: 20-nov-2026. Encarga: el coordinador Claude. Revisa: un agente Claude distinto. Reglas de `AGENTS.md` (no escribir en `jluisplagos/munger-v2`, no subir PDF/XLSX a Git, no aprobar tu propio trabajo, **no valorar ni recomendar**).

## 1. Para qué sirve

El cribado y el análisis directo con la API han dejado 8 finalistas; dos de ellas salen en «Sí · comprar» en el análisis directo, que solo usó los datos de la etapa 1 de la persona, **sin verificar**. Antes de pensar en dinero real hace falta lo mismo que hiciste con las 16 de calidad: **datos oficiales de hoy** y **una historia de diez años independiente**.

## 2. Qué haces por empresa (las dos partes)

- **Parte A = M8:** lee `coordinacion/cierre_v2/universo_etapa1/m8/ENCARGO_MISTRAL_M8_CALIDAD.md` y haz exactamente su sección 3 (último informe anual e intermedio con URL y SHA-256; ventas, EBIT, CFO, capex, arrendamientos, SBC, caja, deuda y pasivos por arrendamiento del último ejercicio y de los doce últimos meses; acciones en circulación; **precio de cierre del 19-nov-2026** conservado con SHA-256).
- **Parte B = M10:** lee `coordinacion/cierre_v2/universo_etapa1/m10/ENCARGO_MISTRAL_M10_HISTORIAS.md` (que remite a M4) y haz la historia de diez años con el mismo formato (`HISTORIA.csv`). **No abras** la etapa 1 de la persona (`coordinacion/cierre_v2/universo_etapa1/` ni los paquetes de `datos_analisis_directo/`): perderías la independencia.

## 3. Bloques

| Bloque | Empresas | Rama de entrega |
|---|---|---|
| 1 | **FW Thorpe**, **Moury Construct** | `mistral/m13-b1` |
| 2 | Azkoyen, Betsson | `mistral/m13-b2` |
| 3 | Coca-Cola (The Coca-Cola Company), Spie | `mistral/m13-b3` |
| 4 | Strabag, Tüpraş | `mistral/m13-b4` |

Entrega en `resultados_universo/m13_finalistas/<empresa>/` con `DATOS.csv`, `HISTORIA.csv`, `fuentes_mercado/` y `ENTREGA.md` (una página por empresa). Commit y push al terminar cada empresa.

---

### Frase para pegar (cambia solo el número de bloque y la rama)

> Lee `coordinacion/cierre_v2/universo_etapa1/m13/ENCARGO_MISTRAL_M13_FINALISTAS.md` en la rama `coordinacion/cierre-v2` del repositorio `jluisplagos/munger-v2-evidencias-mistral` y haz **el bloque N**. Solo ese bloque. Entrega en la rama `mistral/m13-bN`.
