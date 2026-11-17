# Lanzadores de comprobaciones · procedimiento (desde el 17-nov-2026)

Sustituye al lanzador ad hoc de C18, cuyo código de salida no reflejaba el resultado (incidencia `../incidencias/COMANDO_FALLIDO_b0vtcdi3x.md`).

## Qué se corrige

| Defecto del lanzador anterior | Corrección |
|---|---|
| Terminaba con un `echo`, así que salía con 0 aunque fallara un paso | `terminar` sale con 0 si todo va bien, con 1 si algún paso es ≠ 0 y con 3 si se ejecutaron menos o más pasos de los declarados |
| `cd X && run …`: si `cd` fallaba, el paso se saltaba sin dejar rastro | `en_dir` anota el `cd` como un paso; si falla, deja el código 125 |
| `run … && cp …`: un `cp` fallido no se anotaba | `copiar` anota la copia como un paso |
| La comprobación posterior usaba `grep`. Su código 1 («sin coincidencias», es decir, sin fallos) se confundía con un error y el 2 («no se puede leer») no se distinguía. `grep … \|\| echo` lo ocultaría todo | `comprobar_registro.py`: **0** si no hay fallos; **1** si hay fallos, listados; **2** si hay un error de lectura o el registro está mal formado (no existe, ilegible, vacío, truncado, sin «fin», un paso sin código o una línea desconocida); **3** si el número de pasos no es el esperado |

## Uso

```bash
source coordinacion/cierre_v2/herramientas/lanzador_comun.sh
iniciar "$REGISTRO" 26
en_dir revisor1 "$F/revision/scripts_revisor"
paso mutantes "$R/salida.txt" python3 -I -B prueba_mutantes.py …
terminar
```

Y para comprobar el registro sin confundir sus resultados:

```bash
bash lanzador.sh; rc_lanzador=$?
python3 -I coordinacion/cierre_v2/herramientas/comprobar_registro.py "$REGISTRO" --esperados 26; rc_registro=$?
[ $rc_lanzador -eq 0 ] && [ $rc_registro -eq 0 ]
```

El resultado es 0 solo si los dos son 0. Cualquier otro código se informa tal cual, con su causa.

## Pruebas

`bash test_herramientas.sh registro_real_C18b.log` da 18 de 18 casos con el código esperado (`test_herramientas.out`). Las pruebas cubren:
- el registro real de C18 (26 pasos, todos con código 0) → 0; con 28 esperados → 3;
- un paso con código 1 → 1;
- registros truncados, sin «fin», con un paso sin código, vacíos, no UTF-8, inexistentes, que son un directorio o con una línea desconocida → 2;
- el lanzador: todo correcto → 0; un paso fallido aunque el último vaya bien → 1; un `cd` o una copia fallidos → 1, con el paso anotado; menos pasos de los declarados → 3.

**Alcance.** Es una herramienta de procedimiento del coordinador. No cambia ninguna prueba del producto ni ningún resultado anterior. Las 26 comprobaciones de C18 no se repiten (contraste de ChatGPT). Su registro real da 0 con el comprobador nuevo.
