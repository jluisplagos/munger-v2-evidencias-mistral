# Encargo para Mistral · M8 · Datos verificados de las empresas de calidad del cribado

**Para pegar en una ventana nueva de Mistral** (o en dos: bloque A en una y bloque B en otra). Fecha: 19-nov-2026. Encarga: el coordinador Claude. Revisa: un agente Claude distinto. Reglas de `AGENTS.md`: no escribir en `jluisplagos/munger-v2`, no subir PDF/XLSX a Git, no aprobar tu propio trabajo y **no valorar ni recomendar** (nada de «barata», «cara», «comprar»: solo datos con su fuente).

## 1. Para qué sirve

El cribado del universo con la API (rama `automatizacion/claude-api-piloto-registro`, `automation/coordination/reviews/cribado-*/report.json`) marca 16 empresas que **pasan en calidad, caja y balance**, aunque casi todas fallan en precio. La persona responsable quiere tenerlas vigiladas con **datos oficiales actualizados**, no con los de su etapa 1. Tu trabajo es reunir esos datos, cada uno con su documento, su página y su huella.

## 2. Empresas

- **Bloque A:** ABB, ASML, Andina, Bioventix, FW_Thorpe, Ferrari, Hermes, Inditex.
- **Bloque B:** Intuitive, LOreal, LVMH, Lifco, London_Security, Moncler, Puigbrands, Rational.

(El nombre es el de la carpeta del universo: `coordinacion/cierre_v2/universo_etapa1/INDICE.tsv` dice la empresa, la bolsa y la moneda.)

## 3. Qué reúnes por empresa

De la **fuente oficial** (informe anual o semestral más reciente publicado hasta hoy, en la web de inversores de la empresa o del regulador; y la bolsa o la web de inversores para el precio):
1. Último informe anual y último informe intermedio: título, fecha de publicación, URL y SHA-256 del PDF (no lo subas a Git).
2. Del último ejercicio completo y de los doce últimos meses si hay intermedio: ventas, resultado de explotación (EBIT), flujo de caja de las operaciones, inversiones en inmovilizado (capex), pagos de principal de arrendamientos, compensación en acciones si se publica, caja, deuda financiera (sin arrendamientos) y pasivos por arrendamiento, cada uno con página y cita literal.
3. Acciones en circulación (sin autocartera) en la fecha más reciente publicada, con página.
4. Precio de cierre de **18-nov-2026** (o el último día hábil anterior) de la bolsa principal, conservado como texto o CSV con SHA-256 en `fuentes_mercado/`.
5. Cifras tal como están impresas (número, signo, unidad y moneda). Si algo no lo encuentras, `no_encontrado` con el motivo; nunca un cero sin prueba.

## 4. Qué entregas

Rama nueva **`mistral/m8-calidad`**, carpeta `resultados_universo/m8_calidad/`: `DATOS.csv` (`empresa, partida, periodo, valor_impreso, unidad, moneda, archivo, url, sha256, pagina, cita_literal, estado, nota`), `fuentes_mercado/` con `HUELLAS.txt`, y `ENTREGA.md` (una página: qué encontraste, qué no y por qué, modelo y herramientas reales). Commit y push por empresa.

---

### Frases para pegar

> Lee `coordinacion/cierre_v2/universo_etapa1/m8/ENCARGO_MISTRAL_M8_CALIDAD.md` en la rama `coordinacion/cierre-v2` del repositorio `jluisplagos/munger-v2-evidencias-mistral` y haz **el bloque A**. Entrega en la rama `mistral/m8-calidad`.

> Lee `coordinacion/cierre_v2/universo_etapa1/m8/ENCARGO_MISTRAL_M8_CALIDAD.md` en la rama `coordinacion/cierre-v2` del repositorio `jluisplagos/munger-v2-evidencias-mistral` y haz **el bloque B**. Entrega en la rama `mistral/m8-calidad-b`.
