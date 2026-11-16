# Frente C · matemática independiente del precio y del objetivo del motor B

Leer PROGRAMA.md. Rama `mistral/m2-matematica-b`; escribir solo en `resultados_m2/matematica_b/`. Código propio de investigación; no editar ni importar como oráculo las funciones del producto. La comparación con el producto se hace después de derivar y fijar los casos de referencia.

## Material de partida

- `personaje_v2/ANEXO_C_precio_de_si.md`.
- `personaje_v2/scripts/precio_de_si.py`.
- `personaje_v2/scripts/configuracion_economica.py`.
- `personaje_v2/scripts/objetivo_v64.py`.
- `..._4_14/documentacion_cierre_4_14/DECISIONES_PENDIENTES_4_14.md`: D1, D2, D7 y D11.
- Fases A/B/C y configuraciones de los expedientes finales de Vidrala y Viscofan, y antecedentes concretos de 4.13 incluidos en el índice.

## 1. Definición y oráculo independiente

Reconstruir desde las ecuaciones, no copiando el algoritmo:

`G(P)=Σ p_i max(V_i−P,0)`; `L(P)=Σ p_i max(P−V_i,0)`; precio límite por `G(P*)=k·L(P*)`; salida de precio de Sí según el contrato que añade el límite del escenario normal.

Derivar una solución por tramos y otra numérica independiente (por ejemplo bisección), explicitando dominio, existencia/unicidad y degeneraciones. Contrastar ambas con los cinco casos del Anexo C y casos sintéticos propios. No convertir un caso del código en la definición del caso esperado.

Comprobar escala monetaria, traslación, permutación de escenarios, monotonicidad en k, masas/probabilidades cero, valores iguales/negativos, extremos, probabilidades inválidas y tolerancias justificadas. Para el precio de Sí con límite normal, distinguir las propiedades del P* de las de la salida recortada.

Investigar con bibliografía primaria la relación con expectiles, si corresponde, derivándola y contrastando su convención. No confundir expectil con percentil ni con nivel de confianza. Una identidad matemática no valida k=3 como política inversora ni demuestra un límite de pérdidas.

## 2. Probabilidades y efectos separados

Reproducir en los casos históricos preservados el contraste entre probabilidades de referencia y las alternativas que realmente figuran, incluido el cambio 0,20/0,60/0,20 frente a 0,25/0,60/0,15 cuando corresponda. Fijar primero qué versión, valores, fecha, acciones y perímetro usa cada comparación.

Separar el efecto puro de probabilidades del cambio total entre entregas, manteniendo lo demás fijo; documentar discrepancias y límites. No emparejar archivos por nombre parecido ni asumir que un resultado de 4.13 sea el de 4.14. No elegir el vector que produzca el mayor valor.

Generar una sensibilidad **finita y anunciada antes de ver resultados** de k y probabilidades, con motivos y dominio. No simular distribuciones nuevas como si estuvieran empíricamente calibradas. Usar importes históricos solo para contraste, nunca como objetivo vigente de inversión.

## 3. Protocolos y evidencia de cobertura

Revisar el contrato de `objetivo_v64.py`: cobertura aislada, conjunta necesaria, conjunta y sin cobertura; diferencia entre materialidad para acción y para objetivo. Identificar condiciones necesarias y suficientes de lo que realmente se calcula.

Construir ejemplos sintéticos donde:
- la acción se conserva y el objetivo cambia materialmente;
- las variaciones aisladas parecen inocuas y la conjunta importa;
- faltan dominios o hipótesis materiales;
- la sensibilidad calculada no identifica el dominio económico real.

Las variantes se proponen, no se adoptan. «Conclusión sin objetivo» no se presenta como un tercer protocolo ya implementado si requiere una extensión de software. No resolver D1 sin la evidencia económica de D2.

## Salidas específicas

- `DEFINICIONES_Y_DEMOSTRACIONES.md`, bibliografía con enlaces verificables y límites de acceso.
- Oráculo propio, casos fijados, comandos y resultados, sin depender del código del producto para el esperado.
- `COMPARACION_IMPLEMENTACION.csv`, con valores esperados, obtenidos, residuos y versión exacta comparada. No ejecutar LibreOffice ni pipeline.
- `EFECTOS_PROBABILIDADES.csv` y `SENSIBILIDAD_FINITA.csv`, generados por script con hipótesis explícitas.
- `DOSSIER_D1_D7_D11.md`: datos/derivaciones/políticas, qué garantiza la regla y qué no, alternativas y decisiones pendientes. Vincular con D2 sin invadir el frente B.

No recomendar k, probabilidades o protocolo como óptimos sin evidencia pertinente. No afirmar que más tests, un expectil o una réplica prueban capacidad predictiva. Si el problema está en el producto, entregar contraejemplo mínimo y propuesta separada; no corregirlo aquí.
