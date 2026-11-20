# El contradictor simétrico · procedimiento y encargo fijo

**Origen:** decisiones D3 a), D5 y D7 de la persona responsable (`../RESUMEN_SESION_20261117_TARDE.md`), 17-nov-2026. Se registra según el §9 de `RUBRICA_EXAMEN.md` (congelada). **No es código del producto:** es un paso de la orquestación, como la auditoría.

## 1. Dónde va en el recorrido

```
… fase C turno 1 → fase C turno 2 (conclusión provisional)
      → CONTRADICTOR (agente nuevo, contexto limpio)
      → RESPUESTA de la fase C (el mismo agente de la fase C, como corrección pedida por el orquestador)
      → el pipeline sigue: verificación, auditoría, cierre
```

- **Modelo:** Opus con esfuerzo alto en cada empresa; Fable con esfuerzo máximo solo para el contradictor del veredicto final (D7).
- **El contradictor no escribe en el expediente.** Su salida va a `contradictor/<empresa>/OBJECIONES.json` en el repositorio auxiliar.
- **La conclusión solo la cambia la fase C**, al responder. Así las salidas cerradas nunca se editan a mano (guía del recorrido, §6) y el cambio queda en el material que audita el agente nuevo.

## 2. Regla de movimiento (D5)

1. **Bidireccional.** Ataca la conclusión que haya, sea cual sea:
   - contra un «Sí» o un `comprar`: por qué es un error comprar;
   - contra un «No», un `descartar` o un «caro»: por qué es un error dejarla pasar;
   - contra un «Vigilar»: en las dos direcciones;
   - contra «Demasiado difícil» o «límite del modelo»: si de verdad no se puede valorar, o si se está escondiendo detrás del límite.
2. **La objeción carga con la prueba.** Solo cuenta si cumple las dos condiciones:
   - nombra un hecho de las fuentes del expediente, con documento y página, o un dato ausente material;
   - dice cuánto mueve el valor, con una cifra o un rango.

   Una duda genérica («la competencia podría apretar», «hay incertidumbre») no cuenta.
3. **Movimiento.** Una objeción válida que la fase C no rebate con un dato mueve la conclusión **un escalón**:
   - si iba contra un «Sí», de «Sí» a «Vigilar»;
   - si iba contra un «No» o un «caro», hacia «Vigilar».

   Si la fase C la rebate, no la mueve. Varias objeciones en el mismo sentido siguen moviendo un solo escalón por ronda.
4. **Una sola ronda** por empresa. No hay réplica a la respuesta.

## 3. Encargo fijo para el contradictor (se copia tal cual; solo cambian las rutas)

> Eres el **contradictor** del personaje Munger V2. Tu único trabajo es intentar demostrar que la conclusión provisional de esta empresa es un error, **en la dirección que corresponda**. Si concluye comprar, busca por qué comprar es un error. Si concluye no comprar o «caro», busca por qué dejarla pasar es un error. Si concluye vigilar, busca en las dos direcciones. Tienes que ser tan duro con un «No» como con un «Sí». Munger temía tanto pagar de más como dejar pasar un gran negocio por exigir un precio imposible.
>
> **Lees solo** la carpeta del expediente `{CARPETA}`: `fase_c.json`, `fase_c.md`, `fase_b.json`, `fase_a.json`, `precio.json`, `resultados.json`, `datos_v63.md`, `extracto_v63.md` y los textos de las fuentes en `texto/` (marcas `[PDF PAGE n]`). No lees nada fuera de esa carpeta: ni el razonamiento del coordinador, ni rúbricas, ni informes de terceros, ni internet. Tampoco usas tu memoria sobre la empresa: si un hecho no está en `texto/`, no existe para ti.
>
> **Cada objeción** tiene que traer las dos cosas:
> (a) un hecho de `texto/`, con archivo, página y cita literal, o un dato que falta y del que depende la conclusión;
> (b) cuánto mueve el valor por acción o el precio de Sí, con una cifra o un rango calculados con lo que hay en la carpeta, enseñando la cuenta.
>
> Una objeción sin (a) o sin (b) no vale; no la escribas. Prefiero dos objeciones sólidas a diez débiles. Si no encuentras ninguna objeción válida, dilo: es un resultado legítimo.
>
> **Escribe** `{SALIDA}/OBJECIONES.json`:
> `{"empresa", "conclusion_atacada": {"estado", "cubo", "accion", "precio_si"}, "objeciones": [{"id", "direccion": "baja" | "sube", "hecho": {"archivo", "pagina", "cita"} | null, "dato_ausente": "…" | null, "cuanto_mueve": {"cifra_o_rango", "cuenta"}, "por_que_cambia_la_conclusion"}], "sin_objeciones_validas": true | false, "nota"}`
>
> y un `OBJECIONES.md` de una página, en español llano. No propones tamaños de posición, no cambias la tasa del 9 % y no escribes en el expediente.

## 4. Lo que recibe la fase C (corrección pedida por el orquestador)

> El contradictor ha presentado las objeciones de `OBJECIONES.json` (adjuntas). Responde **a cada una**:
> - **rebatida**, con el dato que la rebate (celda, archivo y página);
> - **no rebatida**.
>
> Aplica la regla de movimiento: cada objeción válida que no rebatas mueve tu conclusión un escalón en su dirección, y como mucho un escalón por dirección. Actualiza `fase_c.json` y `fase_c.md` como en el turno 2, con todas sus comprobaciones, y añade la sección «Respuesta al contradictor» con la tabla objeción → respuesta → efecto. No cambies nada más.

## 5. Registro

El evaluador rellena la ficha del §9 de la rúbrica con:
- la conclusión antes y después;
- cada objeción, con su dirección, su hecho, su cuantía y su respuesta;
- el movimiento aplicado;
- la comprobación de independencia (el encargo y las rutas leídas);
- en el conjunto del examen, la simetría: tiene que haber al menos un ataque a una conclusión desfavorable.
