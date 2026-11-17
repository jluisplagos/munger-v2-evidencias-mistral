#!/usr/bin/env bash
# Sonda 2: respaldo en 957af65 de cada hecho modificado (archivo:línea).
set -u
P="${PRODUCTO:?defina PRODUCTO=<producto>}"
E=munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15
T=munger_v2_r1/personaje_v2/pruebas/test_verificacion_entradas_415.py
g(){ git -C "$P" show "957af65:$1" | sed -n "$2p" | sed "s|^|$1:$2: |" | cut -c1-260; }
echo "== fuentes localizadas"; git -C "$P" ls-tree -r --name-only 957af65 | grep -E 'munger_v2_r1/VERSION$|4_15/HITO_1_4_15.md|hito2/HITO_2_4_15.md|hito2/PUNTO_DE_RECUPERACION.md|pruebas/test_verificacion_entradas_415.py$'
echo "== VERSION (hito 2, aptitud, F1 fuera, C48 108)"; g munger_v2_r1/VERSION 1
echo "== HITO_2: aptitud, alcance";        for l in 8 9 10; do g $E/hito2/HITO_2_4_15.md $l; done
echo "== HITO_2: trabajos anteriores no incorporados"; for l in 20 21; do g $E/hito2/HITO_2_4_15.md $l; done
echo "== HITO_2: I20/I19/H9";              for l in 82 89 92 93; do g $E/hito2/HITO_2_4_15.md $l; done
echo "== HITO_2: 190/190";                 g $E/hito2/HITO_2_4_15.md 99
echo "== HITO_2: pendientes";              for l in 192 193 194 195 196 197 219 220; do g $E/hito2/HITO_2_4_15.md $l; done
echo "== HITO_1: R1 R2 R3 I13 I8/I9 C48";  for l in 16 20 24 27 30 32 42 54 65 72 136 153; do g $E/HITO_1_4_15.md $l; done
echo "== HITO_1: reconstrucción código 1 y expedientes 4.14 no aptos"; for l in 181 205 209 211; do g $E/HITO_1_4_15.md $l; done
echo "== PUNTO_DE_RECUPERACION: pendientes y siguiente paso"; for l in 39 40 51 52 53; do g $E/hito2/PUNTO_DE_RECUPERACION.md $l; done
echo "== test 415: grupos R1–R3 (docstring)"; for l in 8 10 12; do g $T $l; done
echo "== recuento de pruebas 190"
git -C "$P" grep -n -E '^190/190' 957af65 -- $E/hito2/resultados/verificacion_completa_0a0020b.txt
git -C "$P" show 957af65:munger_v2_r1/verificar_paquete.sh | grep -n -- '-ge 190'
echo "== referencias a la candidata o al control en 957af65 (vacío = no respaldado por 957af65)"
git -C "$P" grep -n -e 'candidata-cierre' -e 'evidencias-mistral' -e 'programa de cierre' 957af65 -- . ; echo "rc=$?"
echo "== en 3149128 (G-DOCS)"
git -C "$P" grep -n -e 'candidata-cierre' -e 'evidencias-mistral' 3149128 -- munger_v2_r1/CONTINUIDAD.md | cut -c1-200
echo "== procedimiento de recepción (sin cambios)"; for l in 5 10; do g docs/RECEPCION_ENTREGA_CLAUDE.md $l; done
