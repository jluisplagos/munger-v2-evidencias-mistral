#!/bin/bash
# Biblioteca para lanzadores de comprobaciones en secuencia (programa de cierre v2). Uso: `source lanzador_comun.sh` y después:
#   iniciar REGISTRO N_ESPERADOS        crea el registro (lo vacía) y fija cuántos pasos deben ejecutarse
#   paso NOMBRE SALIDA comando args…    ejecuta el comando, guarda su salida en SALIDA y anota «código N» en el registro
#   en_dir NOMBRE DIRECTORIO            cd; si falla, lo anota como paso fallido (código 125) y los pasos siguientes siguen anotándose
#   copiar NOMBRE ORIGEN DESTINO        cp; un fallo se anota como paso fallido
#   terminar                            escribe el resumen y SALE con 0 (todo bien), 1 (algún paso ≠ 0) o 3 (pasos ejecutados ≠ esperados)
# El código de salida del lanzador es el resultado de las comprobaciones; no depende de la última orden ni de grep.
set -u
_REG=""; _ESPERADOS=0; _EJECUTADOS=0; _FALLIDOS=0
iniciar() { _REG=$1; _ESPERADOS=$2; : > "$_REG" || { echo "no se puede escribir el registro $_REG" >&2; exit 2; }
            echo "# lanzador · inicio $(date -u +%FT%TZ) · esperados $_ESPERADOS" >> "$_REG"; }
_anotar() { _EJECUTADOS=$((_EJECUTADOS+1)); [ "$2" -ne 0 ] && _FALLIDOS=$((_FALLIDOS+1)); printf '== %s %s\n   código %s\n' "$1" "$(date -u +%H:%M:%S)" "$2" >> "$_REG"; }
paso() { local n=$1 s=$2; shift 2; "$@" > "$s" 2>&1; _anotar "$n" $?; }
en_dir() { cd "$2" 2>/dev/null; local c=$?; [ $c -ne 0 ] && c=125; _anotar "$1" $c; }
copiar() { cp "$2" "$3"; _anotar "$1" $?; }
terminar() {
  local r=0; [ $_FALLIDOS -gt 0 ] && r=1; [ $r -eq 0 ] && [ $_EJECUTADOS -ne $_ESPERADOS ] && r=3
  echo "fin $(date -u +%H:%M:%S) · ejecutados $_EJECUTADOS · esperados $_ESPERADOS · fallidos $_FALLIDOS · resultado $r" >> "$_REG"
  exit $r; }
