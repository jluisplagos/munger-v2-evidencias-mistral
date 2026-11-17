# Reorientación de Munger V2 hacia el universo real de la persona responsable · 17-nov-2026

**Estado:** notas de una conversación y propuesta del coordinador. Las decisiones que están marcadas como tales son de la persona responsable. El resto **no está adoptado** hasta que ella lo confirme. En concreto, el recorte de alcance y la tasa siguen pendientes.

## 1. Objetivo, en palabras de la persona responsable

- Quiere un personaje de **calidad extraordinaria**, adaptado a su realidad, que analice las empresas de su universo y permita, con su propia investigación, **invertir dinero real en cantidades pequeñas**.
- El personaje mantiene la profundidad de la V2: una hoja resumen arriba y el Excel V6 grande debajo. Toda la maquinaria técnica tiene que estar ahí y verificada, aunque ella no tenga que leerla.
- No quiere consejos sobre ningún portafolio concreto. El informe crítico es material de estudio y la cartera que analiza no es la suya.

## 2. Reglas decididas por la persona responsable

- **R-5:** el personaje analiza sin conocer su opinión y tiene que decir la verdad, aunque duela.
- **R-6:** si el personaje y su investigación no coinciden, **no se invierte**.

## 3. El universo

- El informe crítico tiene 105 empresas con ficha: 5 a fondo (Jumbo, Ahold Delhaize, Zoetis, Elis, Waste Management), 15 en seguimiento, 4 en la cartera estudiada (Hermès, Sika, Aarsleff, Viscofan) y 81 descartadas.
- El universo real ronda las **135–140 empresas** (falta Ferrari, por ejemplo). Hay un Excel de etapa 1 y un resumen `.md` de cada una.
- **Ninguna es financiera.** El motor C sobra para este universo.
- Es un círculo de competencia coherente: negocios simples con demanda duradera (comercio, servicios por rutas, salud, marcas, industria de nicho).

## 4. Opinión del coordinador sobre el embudo del informe (105 → 4)

**Lo bueno:** seis filtros eliminatorios con su pregunta y una regla escrita, y un autor que nunca fue más indulgente que la hoja.

**Lo que cambiaría:**
1. **Filtro 1, «aporte», al final.** Mide el encaje en una cartera concreta, que además no es la suya. Eliminó 42 empresas al principio, algunas excelentes.
2. **Filtro 2, «legible».** Separar «el negocio no se entiende» de «el DCF al 9 % de la plantilla no aplica», que explica 24 de las caídas. Con el motor adecuado a cada tipo de negocio, varias pasarían.
3. **Filtro 4, deuda ≤ 2,5 veces.** Ajustar el límite a la estabilidad del negocio; el propio autor lo admite para Waste Management. La deuda debe contar siempre los arrendamientos, o nunca, en coherencia con F1: Ahold tiene unos 12.000 millones de pasivo por arrendamientos.
4. **Filtro 5, precio.** Mantenerlo, pero con la hoja al día y la tasa elegida por la persona responsable. Zoetis pasó con una hoja anterior a sus resultados.
5. **Orden propuesto:** calidad del negocio → caja → balance → precio → encaje en la cartera. Con los motores del personaje en lugar de la plantilla única. Es probable que, de 135–140, salgan bastantes más de 4 dignas de estudio.

## 5. Las empresas del examen del personaje

Se eligen **para examinar el juicio**, no porque sean compras:

| Empresa | Qué examina |
|---|---|
| Ahold Delhaize | El arrendamiento contado dos veces: el 85 % de sus locales son alquilados y su margen es del 4 %. Motor A frente a B |
| Jumbo | El único caso donde un «Sí» es plausible: comprueba que el personaje sabe decir que sí |
| Zoetis, en dos tiempos | La trampa: parecía barata con la ficha de octubre y el trimestre de noviembre rompió la tesis. Si dice «Sí», suspende |
| Elis | Debe acabar en «faltan datos» (R pendiente) sin inventarse la cifra |
| Vinci | Límite del modelo (concesiones que vencen, suma de partes): debe abstenerse |
| *Waste Management (opcional)* | El error contrario: un negocio excelente y caro debe dar «vigilar», no «no» |

## 6. Después del examen

- Cualquier empresa no financiera del universo puede pasar por el personaje, siguiendo siempre este camino:
  1. el Excel de etapa 1 y el `.md` de la persona responsable;
  2. verificación de cada cifra material contra la fuente oficial (trabajo de Mistral);
  3. `verificacion_entradas` en estado «apto»;
  4. el personaje.
- **Orden sugerido de análisis, que no es una recomendación de compra:**
  - primero, las que el informe sitúa cerca o por debajo de su escenario base: Pandora, FW Thorpe y Arcadis;
  - después, las exigentes, para afinar el modelo: Carriage Services (funeraria con deuda), Lifco y Volution (crecen comprando) y Rational y L'Oréal (muy sensibles a la tasa).
- El «hecho que la reabriría» de cada empresa en seguimiento sirve de disparador: el expediente completo se rehace solo cuando ese hecho ocurre.
- Más adelante, un inventario completo de las 135–140, con nombre, sector y estado.

## 7. Propuesta de recorte (pendiente de decisión)

- **Se queda:**
  - F1 implantado y probado fuera de Elis (Ahold, y una empresa con normas de EE. UU.);
  - verificación de entradas;
  - el personaje completo en los casos del examen;
  - los criterios K1–K12 de la lectura del informe, más: explicación en lenguaje llano en la hoja resumen, sensibilidad a la tasa, repetibilidad y predicciones fechadas.
- **Se aparca, sin borrar:**
  - el motor C y la búsqueda de financieras;
  - la aceptación formal de los 36 casos sintéticos (se usan como control los ~16 útiles);
  - Vidrala;
  - el manual largo (se sustituye por un procedimiento corto);
  - la automatización por API;
  - los contrastes Qwen.
- **Tope:** 4–6 días de trabajo. Si al terminar no se cumplen los criterios, se para.
- **Uso de modelos:**
  - Fable solo en revisiones críticas, entre 4 y 6 sesiones;
  - Mistral, para el volumen: fuentes, datos y código mecánico;
  - el coordinador, para encargos, control y revisiones normales.

## 8. Temas abiertos para conversar

- **Tasa exigida.** La heredada es el 9 %. Cada análisis mostrará su efecto con ±1–2 puntos.
- **Regla de venta.** El informe señala que el método actual no la tiene.
- **Preguntas prácticas:**
  - coste y tiempo por análisis;
  - quién hace la fase 1 de cada empresa nueva;
  - cuándo se repite un análisis (precio o resultados nuevos);
  - divisas, impuestos y comisiones;
  - cambios de versión del modelo de IA;
  - un procedimiento corto para usarlo sin esta conversación;
  - lo que el personaje no hace: la cartera en conjunto, financieras, sumas de partes.
