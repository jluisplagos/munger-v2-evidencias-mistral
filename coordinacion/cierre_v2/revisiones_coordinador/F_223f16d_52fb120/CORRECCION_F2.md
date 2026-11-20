# Corrección F2 · Mistral C/F · sobre `223f16d` (B-PM1) y `52fb120` (F-B3/F-C1)

- **Para:** Mistral C/F, rama `mistral/f-alcance-real`.
- **De:** el coordinador, según [REVISION_F_223f16d_52fb120.md](REVISION_F_223f16d_52fb120.md) (procedencia en [LEEME.md](LEEME.md)).

## Clasificación

- **B-PM1:** el dato es conforme.
  - El revisor comprobó él mismo, en los PDF y con su huella, las nueve altas de Vidrala.
  - El error antiguo era la nota de intangibles: 156.743 = 3.237 de emisiones + 150.657 de goodwill.
  - El bloqueo P-M1 y θ/λ se conservan.
  - Límite: el contraste de F trabajó sobre textos, sin comprobar páginas ni hacer un control negativo propio.
- **F-B3/F-C1, preparación:** correcciones materiales en D1 y D3.
  - Los bloqueos declarados son reales: no hay Excel de la etapa 1 de Ahold y no se conserva ninguna financiera.
  - Ninguno se resuelve aquí: dependen de datos que solo puede aportar la persona responsable.

## Defectos

| | Defecto | Prueba de cierre |
|---|---|---|
| **F2-D1 (material)** | `scripts/inventario_desde_zip.py` no reproduce `INVENTARIO_Y_HUECOS.csv`: difieren las 7 filas de «correcciones 4.14». En `elis`, lo publicado es 0,0,0,0,105 y lo reproducido, 6,26,46,14,13. ENTREGA declara código 0 para un CSV que el script no produce | El script regenera el CSV byte a byte desde el ZIP (`bb51942c…`), y ENTREGA lo declara con el comando exacto |
| **F2-D2** | El inventario está incompleto sin declararlo:<br>- el filtro deja fuera `elis_decisiones`;<br>- no recorre `contrastes/` ni `…/2026-11_Vidrala_ensayo/fuentes/`, así que da 0 PDF para Vidrala y Viscofan;<br>- 42 de los 71 PDF del ZIP quedan sin huella;<br>- la fila de la Release lleva el SHA truncado | Recorrido completo, o alcance declarado. Huella completa de los 71 PDF y de la Release |
| **F2-D3 (material: corregir antes de usar el contrato C)** | El contrato y el mapa describen mal el motor C del producto:<br>- dicen B14 = g∞ y B15 = payout, cuando en el producto X14 es el crecimiento de los años 1–5, X15 el ROE objetivo en C, X18 la rentabilidad terminal y g∞ está en Análisis B68;<br>- dicen ROE = BAI / patrimonio medio, cuando en el producto es beneficio neto atribuible ÷ patrimonio de cierre;<br>- el puente de patrimonio suma los dividendos (E0 = 1000, beneficio 100, impuesto 30, dividendos 40: el puente da 1170 y lo real es 1060);<br>- rellenar B15 con un payout del 40 % multiplica el valor ilustrativo por 2,42;<br>- propone una «guarda» de capital regulatorio sin definirla y una base de valor (múltiplos o valor liquidativo) que no es la del motor | Contrato y mapa reescritos desde `build_v6.py`, `Palancas` y `test_fill.py`, con cita de línea. Un caso numérico que cuadre el puente. La guarda y la base de valor quedan como **propuesta pendiente de decisión**, sin números |
| **F2-D4** | `PUNTO_DE_RECUPERACION.md` sigue pidiendo el contraste B-PM1, que ya está hecho | Actualizar la siguiente acción |
| **F2-D5** | Sobredeclaración:<br>- «cola C_F completa» y «F-B3/F-C1 HECHOS» se presentan como si fueran del control, cuando son valoración propia;<br>- se dan por cubiertos «principal y reserva por recorrido» y «datos oficiales», que no existen | Distinguir «preparación entregada» de «hecho». El estado lo registra solo el coordinador |
| **F2-D6** | Las horas de `COMANDOS.md` son posteriores a los commits. El protocolo entra en el mismo commit que la selección y no fija criterios de elección para C | Horas reales o ninguna. Protocolo de C con criterios fijados antes de nombrar candidata, sin precios |
| **F2-D7** | Comandos que no se ejecutan tal cual: ruta `/workspace` fija en el extractor | Rutas por argumento |

## Lo que bloquea de verdad (datos de la persona responsable)

- **F-B3:** hace falta una de estas dos cosas:
  - el Excel evaluado de la etapa 1 de Ahold y su respuesta, con sus fuentes (informes 2016–2025 y el folleto de reexpresión NIIF 16 de 2018), en bytes y con SHA-256;
  - otra empresa fuera de muestra designada por la persona. La lista de las 116 no está conservada; Hermès y Aarsleff no sirven porque ya están en la muestra.
- **F-C1:**
  - un banco o una aseguradora concretos, designados por la persona;
  - sus informes oficiales (cuentas, Pilar 3 o SFCR) en bytes y con SHA-256;
  - el Excel de la etapa 1, si existe.

## Entrega

- Un commit con ENTREGA.json y F2-D1…D7, cada uno con su prueba.
- No elegir candidata de C ni sustituto de Ahold sin designación.
- No fijar umbrales ni bases de valor.
