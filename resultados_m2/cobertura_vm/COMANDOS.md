# Comandos realmente ejecutados · Frente A M2 (cobertura VM)

Entorno declarado: **Python 3.12.15** (stdlib), **openpyxl 3.1.5**, **pypdf 7.1.0** en `.trabajo/pylibs` (XLSX/PDF solo lectura), git/gh, sha256. Sin LibreOffice, pipeline ni macros. `asociacion_pdf.py` declara y exige pypdf >= 6.0 (probado con 7.1.0) y falla con mensaje claro si no basta.

Todos los comandos se ejecutan desde la raíz del auxiliar `jluisplagos/munger-v2-evidencias-mistral` con `PYTHONPATH=$PWD/.trabajo/pylibs` y `python3 -B` (sin bytecode):

```bash
# Lectura de revisiones/control (sin fusionar; solo fetch + show)
git fetch origin coordinacion/cierre-v2
git show FETCH_HEAD:coordinacion/cierre_v2/revisiones_coordinador/A_2c41d68/CORRECCION_A2.md
git show FETCH_HEAD:coordinacion/cierre_v2/revisiones_coordinador/A_2c41d68/REVISION_A_2c41d68.md

# Pipeline completo (orden fijo), cobertura v4.0 (corrección A2-R1..R5)
PYTHONPATH=$PWD/.trabajo/pylibs python3 -B resultados_m2/cobertura_vm/scripts/inventario.py
PYTHONPATH=$PWD/.trabajo/pylibs python3 -B resultados_m2/cobertura_vm/scripts/verificar_fuentes.py
PYTHONPATH=$PWD/.trabajo/pylibs python3 -B resultados_m2/cobertura_vm/scripts/verificar_contexto.py
PYTHONPATH=$PWD/.trabajo/pylibs python3 -B resultados_m2/cobertura_vm/scripts/derivaciones.py
PYTHONPATH=$PWD/.trabajo/pylibs python3 -B resultados_m2/cobertura_vm/scripts/construir_cobertura.py
PYTHONPATH=$PWD/.trabajo/pylibs python3 -B resultados_m2/cobertura_vm/scripts/control_negativo.py        # exit 0; sondas revisor 5/5 CONFLICTO; bilaterales 15/15
PYTHONPATH=$PWD/.trabajo/pylibs python3 -B resultados_m2/cobertura_vm/scripts/control_cobertura.py       # exit 0 = PASS
PYTHONPATH=$PWD/.trabajo/pylibs python3 -B resultados_m2/cobertura_vm/scripts/cola_pendientes.py
PYTHONPATH=$PWD/.trabajo/pylibs python3 -B resultados_m2/cobertura_vm/scripts/resolver_bloque2.py
for L in L00 L01 L02 L03 L04 L05 L06 L07 L08 L09 L10 L11 L12 L13 L14 L15 L16 L17 L18 L19 L20 L21; do
  PYTHONPATH=$PWD/.trabajo/pylibs python3 -B resultados_m2/cobertura_vm/scripts/revisar_lote.py $L
done
PYTHONPATH=$PWD/.trabajo/pylibs python3 -B resultados_m2/cobertura_vm/scripts/control_cobertura.py       # re-ejecucion final: PASS exit 0
PYTHONPATH=$PWD/.trabajo/pylibs python3 -B resultados_m2/cobertura_vm/scripts/asociacion_pdf.py          # texto<->PDF por muestra (pypdf >= 6.0 declarado)

# Recuentos vigentes generados (A2-R5: no escritos a mano) y diff de estados entre commits
PYTHONPATH=$PWD/.trabajo/pylibs python3 -B resultados_m2/cobertura_vm/scripts/generar_recuentos_doc.py
python3 -B resultados_m2/cobertura_vm/scripts/generar_cambios_estado.py 9d676cefdfeb3771a43414fcb93f430e9340fae0 a2_v4

# Manifiesto (sin __pycache__) y publicacion
rm -rf resultados_m2/cobertura_vm/scripts/__pycache__
PYTHONPATH=$PWD/.trabajo/pylibs python3 -B resultados_m2/cobertura_vm/scripts/generar_manifiesto.py
git add resultados_m2/cobertura_vm
git commit -m "Frente A M2 (correccion A2-R1..R5, v4.0): ..."
git push -u origin mistral/m2-cobertura-vm
git ls-remote origin mistral/m2-cobertura-vm    # comprobar que el SHA remoto == HEAD local
```

Versiones: `python3 --version` → Python 3.12.15; `openpyxl.__version__` → 3.1.5; `pypdf.__version__` → 7.1.0 (comprobado con `PYTHONPATH=.trabajo/pylibs python3 -c "import openpyxl, pypdf, sys; print(sys.version.split()[0], openpyxl.__version__, pypdf.__version__)"`).

## Bloque A3 (corrección A3-R1…R8, control @ 57b34a60)

Tras el pipeline anterior, con el código A3 definitivo:

```bash
# sondas del informe (publicadas en sondas_a3/sondas_informe/) y sondas nuevas propias
python3 -I -B resultados_m2/cobertura_vm/sondas_a3/sondas_informe/s02_sondas_revisor_A.py resultados_m2/cobertura_vm/scripts/verificar_contexto.py /tmp/s02.json
python3 -I -B resultados_m2/cobertura_vm/sondas_a3/sondas_informe/s03_sondas_d375d80_A.py resultados_m2/cobertura_vm/scripts/verificar_contexto.py /tmp/s03.json
python3 -I -B resultados_m2/cobertura_vm/sondas_a3/sondas_informe/s07_sondas_nuevas_A2.py resultados_m2/cobertura_vm/scripts/verificar_contexto.py /tmp/s07.json
python3 -I -B resultados_m2/cobertura_vm/sondas_a3/s11_R1_sonda_nueva.py resultados_m2/cobertura_vm/scripts/verificar_contexto.py /tmp/r1.json   # idem R2..R6
python3 -I -B resultados_m2/cobertura_vm/sondas_a3/s11_R7_sonda_nueva.py resultados_m2/cobertura_vm/scripts /tmp/r7.json

# A3-R8: huellas/recuentos de ENTREGA.json y textos desde las salidas (generados, no a mano)
python3 -B resultados_m2/cobertura_vm/scripts/generar_entrega_json.py
python3 -B resultados_m2/cobertura_vm/scripts/actualizar_textos_resumen.py

# diff de estados vs la base revisada y por punto
python3 -B resultados_m2/cobertura_vm/scripts/generar_cambios_estado.py 8b88fab28261506c60bc7631fd24894e225099d2 a3

# nota: cola_pendientes.py y resolver_bloque2.py ya funcionan con python3 -I -B (A3-R8);
# asociacion_pdf.py con pypdf 6.x sale con mensaje claro (exit 1); con 7.1.0 exit 0
```
