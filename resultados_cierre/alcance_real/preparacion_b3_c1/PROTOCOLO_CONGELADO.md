# Protocolo congelado · F-B3 / F-C1 (preparación de casos reales) · 2026-11-16

Fijado **antes de cualquier cálculo** (encargo Cola 2, paso 3). Nada de esto usa precios de
valoración ni resultados para seleccionar.

## 1. Criterios de elegibilidad (en este orden)

1. **Documental**: fuente oficial con huella (SHA-256 + bytes) o Excel de etapa 1 ya verificado;
   procedencia y vigencia comprobadas; los análisis previos NO se toman como datos verificados.
2. **Negocio**: el caso debe casar con el método por su economía, no por conveniencia.
   - Motor B (V6.4): financiación cambiante (recompras, deuda a corto, filial con financiación propia).
   - Motor C: banco o aseguradora, con contrato económico específico (ver CONTRATO_C_PROPUESTA.md).
3. **Método posible**: la plantilla lo soporta sin forzar (la fase A real valida el método; si no
   elige B, se documenta y no se fuerza — precedente Elis 4.14: `no_entregable · límite del modelo`).

## 2. Reglas de selección

- Hasta **3 candidatas por recorrido**, con carencias declaradas.
- **No se usa la valoración/precio resultante para seleccionar** (prohibido por el encargo).
- Se propone **principal y reserva por recorrido**, conservando exclusiones y motivos (SELECCION.csv).
- Es una selección de **ensayo**, no una elección de motor por conveniencia.
- Huecos como huecos, nunca ceros.

## 3. Protocolo de ejecución (cuando exista candidata con insumos)

1. Materializar copia aislada desde el ZIP base-4.14 (SHA-256 `bb51942c…`, 6798/6798 verificados);
   nunca sobre el producto ni main.
2. Etapa 1 con fuente+página por cifra; verificación completa de entradas (`verificacion_entradas.py`,
   puerta del pipeline; hito 2 reforzó el signo — R415-SIGNO).
3. Configuración propia **congelada antes de evaluar** (precedente: `hito1/SELECCION_TERCERA_EMPRESA.md`
   se justificó antes de conocer el resultado).
4. Fases A/B/C con agentes reales y regla de rama; auditoría independiente (paso 13) por un contexto
   distinto del extractor (límite I18/I20 de la matriz vieja: no restaurar como vigentes los límites
   superados; la frase de doble PPA más fuerte que F1 no se restaura — F1 es la vigente).
5. Relevo documentado (CONTINUIDAD.md / PROMPT_NUEVA_VENTANA.md) y paquete de relevo.
6. Entrega por paquetes Git al coordinador; nada integrado por mí.

## 4. Lo que NO se hará

- No se ejecuta LibreOffice ni el pipeline en mi sesión (prohibido por el encargo F); la ejecución
  corresponde a Cola 3 con agentes/pipeline, en copias aisladas.
- No se declara validado un caso C por el mero hecho de que la plantilla acepte cifras.
- No se fuerza Ahold (reserva sin insumos) ni ningún caso fuera de muestra sin fuente oficial.
- No se cambia ningún parámetro económico para producir resultados favorables.

## 5. Estado actual de las candidatas (SELECCION.csv)

- **B**: principal condicionada = Ahold Delhaize (bloqueada por insumo); reservas técnicas dentro
  de muestra (Hermès, Aarsleff) solo como control de variabilidad; Elis excluida (no forzar motor).
- **C**: principal propuesta = banco/aseguradora europea con fuente oficial pendiente (bloqueo
  documental concreto: en este entorno solo GitHub es alcanzable); fixture sintético excluido como
  caso real.
