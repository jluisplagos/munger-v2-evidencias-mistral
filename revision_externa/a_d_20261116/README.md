# Reproducción y alcance

Lee REVISION_A_D.md. CORRECCION_A.md y CORRECCION_D.md son encargos preparados para las sesiones autoras; no han sido enviados.

## Sondas pequeñas sin descargar la base

En copias aisladas de los commits fijados A y D:

```bash
python3 -B sondas_revision.py --a /ruta/worktree_A --d /ruta/worktree_D --salida sondas_locales.json
```

El repositorio auxiliar debe tener disponible el commit del banco `4745f38` para `git show`. Las sondas importan el módulo A, ejecutan el generador D sin evidencias y el arnés con un directorio deliberadamente carente de scripts del producto. Esta última es una prueba del arnés, no del producto. No requieren agente, LibreOffice, proveedores de IA ni instalación de dependencias financieras. La sonda no genera veredictos económicos. Verifica el manifiesto en los worktrees **antes** de regenerar salidas.

## Regeneración de A

Usar otra copia A @0224b71, conservando la entrega original en su worktree. Recuperar el ZIP público de la Release `jluisplagos/munger-v2`, tag `base-4.14`, asset `munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip` y comprobar su SHA indicado en el informe.

```bash
python3 docs/programa_mistral_m2/herramientas/preparar_insumos.py --zip /ruta/base414.zip
python3 -B resultados_m2/cobertura_vm/scripts/verificar_contexto.py
python3 -B resultados_m2/cobertura_vm/scripts/derivaciones.py
python3 -B resultados_m2/cobertura_vm/scripts/construir_cobertura.py
python3 -B resultados_m2/cobertura_vm/scripts/control_negativo.py
python3 -B resultados_m2/cobertura_vm/scripts/control_cobertura.py
```

La última orden terminó exit 1 en esta revisión. Las cinco anteriores se completaron. A_REPRODUCCION.json conserva los estados, los 20 cambios de reexpresión y las huellas de las salidas originales/regeneradas. Los cuatro logs adjuntos son de esa ejecución. No presentar esos conflictos automáticos como 20 errores financieros primarios.

## Componentes D

Copiar `resultados_qwen/ejecucion_d/` a una carpeta de revisión aislada. CANDIDATA_DIR debe ser el código real @957af65. BANCO_DIR para **el ejecutor** apunta a la carpeta `resultados_qwen/q1_v2/banco_revisado` de @4745f38, no a su raíz de repositorio. RUN_DIR debe ser un directorio nuevo de prueba.

Los binarios requeridos se recuperan del ZIP y se verifican contra el índice 4.14: expediente plantilla `personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_13/viscofan/Viscofan/`, `v6/v641_experimental/entregables/Plantilla_V6.4.1_experimental.xlsx` y `v6/entregables/Ejemplo_V6.3_EmpresaX.xlsx`. Conservar los archivos versionados de la candidata; no reemplazarlos por el código 4.14. Esta preparación es parcial y suficiente para los comandos ensayados; no acredita base completa ni todos los componentes.

```bash
export CANDIDATA_DIR=/ruta/copia_prueba_candidata
export BANCO_DIR=/ruta/banco/resultados_qwen/q1_v2/banco_revisado
export RUN_DIR=/ruta/nueva/ejecucion_de_prueba
bash /ruta/copia_arnes/scripts/ejecutar_todo.sh
```

El shell del autor oculta fallos: revisar los resultado_ejecucion.json y no aceptar su exit 0 como veredicto. D_REPRODUCCION.json conserva por caso las secuencias de códigos comparadas y por archivo los campos JSON contrastados. La reproducción inicial necesitó añadir las dos plantillas XLSX antes de repetir Q1-036; después coinciden 27/27 secuencias y 48/48 JSON en esos campos.

Para repetir la sonda D_SALIDA_OBSOLETA.json: en una **copia de prueba** con esos binarios ya disponibles, retirar temporalmente solo la plantilla V6.4.1 experimental, ejecutar Q1-036 desde estado limpio y restaurarla al terminar. La copia del expediente histórico contiene ficha_provisional.json e informe_provisional.md preexistentes. Comprobar que los comandos provisionales salen 2 por dependencia ausente, pero el arnés sale 0 y copia esos archivos idénticos a los históricos. Esa fue la sonda realizada; los binarios se restauraron. No ensayar retirando dependencias de una instalación utilizada por otra persona.

No se ha ejecutado el personaje completo ni Q1-026 de extremo a extremo. No se han revisado aquí las correcciones de Claude F1. No se ha integrado nada en main.
