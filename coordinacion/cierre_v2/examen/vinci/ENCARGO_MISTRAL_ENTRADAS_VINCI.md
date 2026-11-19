# Encargo para Mistral · Registro de entradas de VINCI SA (examen del personaje)

**Para pegar en una ventana nueva de Mistral.** Fecha: 19-nov-2026. Encarga: el coordinador Claude. Revisa: un agente Claude distinto, que es quien sella. **Tú no sellas ni marcas nada como «verificado».**

Es el mismo trabajo que hiciste con Ahold, Jumbo y Zoetis. **Lee primero el encargo de Ahold** (`coordinacion/cierre_v2/examen/ahold/ENCARGO_MISTRAL_ENTRADAS_AHOLD.md`, rama `coordinacion/cierre-v2`) y su corrección (`…/ahold/CORRECCION_MISTRAL_ENTRADAS_AHOLD_R1.md`): las reglas, las clases, el formato y la forma de aceptación son **idénticos**. Aprende también de lo que corrigieron los revisores en tus registros anteriores: `coordinacion/cierre_v2/examen/{jumbo,zoetis,ahold}/revision_registro/REVISION.md` y `REVISION_SELLADO.md`. Los fallos que más se repitieron: **ceros con una cita que no prueba el cero** (la cita tiene que mostrar que la partida no existe o vale cero en esa columna, o la clase es otra), **años y periodos** mal citados, **folios** (página del visor PDF, no la impresa) y **signos** de gastos impresos en positivo.

## 1. Dónde está todo (Vinci)

- **Expediente (solo lectura):** repo `jluisplagos/munger-v2`, rama **`examen/expedientes-f1`**, carpeta `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_examen_universo/vinci/Vinci/`:
  - `texto/*.txt`: informes anuales 2016–2019, URD 2020–2025, semestral a 30-jun-2026 y estados intermedios de julio de 2026, con marcas `[PDF PAGE n]`. **Los URD 2021–2023 son PDF a doble página:** el texto de cada marca va por mitades (izquierda y luego derecha); la página es la del visor;
  - `fase1_partes/AR_AAAA.json` (lo que extrajeron los extractores, con `impreso`, `pagina` y `linea` literal), `fase1_v63.json`, `fase1_metadatos.json`, `historia_revision.md`, `motor_a_f1.json`, y la configuración del cambio en `../../configuracion/cambio_vinci.json` (cálculos declarados de C46–C50: regístralos como `derivado`).
- **PDF oficiales:** Release `fuentes-examen-20261118` del auxiliar, con huellas en `coordinacion/cierre_v2/examen/RELEASE_FUENTES_EXAMEN_SHA256SUMS`. **Nada publicado después del 10-oct-2026** (la información de 9M 2026 del 22-oct queda fuera).
- **Plantilla del registro:** `coordinacion/cierre_v2/examen/vinci/verificacion_entradas.plantilla.json` (**315 entradas**; `valor_modelo` es el valor del libro). Lista resumida: `vinci/LISTA_ENTRADAS.csv`.

## 2. Alcance

Las **285 entradas** con `en_este_encargo` = «sí». Las 30 hipótesis las escriben las fases del personaje: no las toques.

## 3. Lo que tienes que vigilar especialmente en Vinci

- **Unidades:** millones de euros en las cuentas consolidadas. `escala` y `unidad` tienen que decirlo.
- **EBIT derivado:** la cuenta de resultados de VINCI no imprime el resultado antes de impuestos como en otras empresas; mira cómo lo construye `fase1_partes` y registra cada componente con su signo tal como está impreso.
- **Deuda:** deuda financiera bruta **sin** NIIF 16; los arrendamientos van aparte. Distingue lo que es de concesiones y lo de contratación solo si el libro lo usa.
- **Capex:** compras de inmovilizado material e intangible **más** inversiones en concesiones (dos líneas).
- **Acciones (C55):** 555.967.094 en circulación al 31-dic-2025 (URD 2025 PDF p. 346), sin dilución (decisión P-O2: acciones al cierre). Registra la cifra impresa exacta.
- **Ceros 2016–2018** de arrendamientos e intereses de arrendamientos: antes de la NIIF 16; si no hay una cita que pruebe el cero, la clase probablemente sea `no_aplicable` (norma anterior), con su motivo.
- **Precio (C37) 107,05 € (9-oct-2026) y Bund a 10 años (C57) 3,486 %:** de la etapa 1, sin fuente oficial guardada. Intenta conservar el histórico oficial de Euronext Paris de esa sesión y el Bund del Bundesbank o del BCE de ese día como texto con SHA-256 en `fuentes_mercado/`; si no puedes, dilo. No pongas otra fuente sin avisar.

## 4. Qué entregas

Rama nueva **`mistral/examen-vinci-entradas`**, carpeta `resultados_examen/vinci/`: `verificacion_entradas.json` (las 315 entradas, las 30 hipótesis sin tocar), `fuentes_mercado/` con `HUELLAS.txt`, `DESCARGAS.tsv` y `ENTREGA.md` (máximo una página). Commit y push al terminar cada bloque grande.

---

### Frase para pegar en la ventana nueva

> Lee `coordinacion/cierre_v2/examen/vinci/ENCARGO_MISTRAL_ENTRADAS_VINCI.md` en la rama `coordinacion/cierre-v2` del repositorio `jluisplagos/munger-v2-evidencias-mistral` y hazlo entero. Entrega en la rama `mistral/examen-vinci-entradas`.
