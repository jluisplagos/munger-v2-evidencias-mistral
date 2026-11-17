#!/usr/bin/env bash
# Sonda 1: diff completo de G-RAIZ y lista de líneas suprimidas/añadidas por archivo.
# Uso: PRODUCTO=<producto> bash 01_diff_y_supresiones.sh
set -u
P="${PRODUCTO:?defina PRODUCTO=<producto>}"
git -C "$P" rev-parse origin/integracion/hechos-raiz-957af65
git -C "$P" diff --stat 957af65 3d66437
echo "== líneas suprimidas (-) y añadidas (+)"
git -C "$P" diff -U0 957af65 3d66437 | grep -E '^(\+\+\+|[-+][^-+])'
