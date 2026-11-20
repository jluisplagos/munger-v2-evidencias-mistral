#!/usr/bin/env bash
# Sonda independiente de F3-R3/R4 (sin el script del autor): .bat, PDF y alcance negativo.
# Uso: bash sonda_r3_r4_alcance.sh <zip_414> <INVENTARIO_Y_HUECOS.csv>
set -u
ZIP="$1"; INV="$2"
L=$(mktemp -p "$(dirname "$0")" zipZ1.XXXX)
unzip -Z1 "$ZIP" > "$L"
echo "== entradas en el ZIP: $(wc -l < "$L"); directorios: $(grep -c '/$' "$L"); archivos: $(grep -vc '/$' "$L")"
echo "== archivos fuera de munger_v2_r1/: $(grep -v '/$' "$L" | grep -vc '^munger_v2_r1/')"
echo "== .bat en todo el ZIP (con SHA-256 por unzip -p):"
grep -i '\.bat$' "$L" | while read -r f; do printf '%s  %s\n' "$(unzip -p "$ZIP" "$f" | sha256sum | cut -c1-64)" "$f"; done
echo "== filas .bat del inventario publicado:"
grep -i '\.bat,' "$INV" | cut -d, -f1,9 | sed 's/conservado en el ZIP; //'
echo "== rutas con 'ahold' (sin distinguir mayúsculas):"
grep -i 'ahold' "$L"
echo "== PDF en el ZIP: $(grep -ic '\.pdf$' "$L")"
echo "== clasificación independiente (awk) dentro / fuera del alcance positivo declarado:"
grep -v '/$' "$L" | grep '^munger_v2_r1/' | sed 's#^munger_v2_r1/##' | awk -F/ '
{
  n=NF; cat="";
  if ($1=="personaje_v2" && $2=="empresas_v2" && n>=3) cat="DENTRO";
  else if ($1=="personaje_v2" && $2=="empresas_v2_correcciones" && n>=4) cat="DENTRO";
  else if ($1=="contrastes" && n>=3) cat="DENTRO";
  else if (n==1) cat="FUERA raiz munger_v2_r1 (sueltos)";
  else if ($1=="personaje_v2" && $2=="empresas_v2_correcciones" && n==3) cat="FUERA empresas_v2_correcciones/ suelto";
  else if ($1=="personaje_v2") cat="FUERA personaje_v2/ (otros)";
  else cat="FUERA " $1 "/";
  c[cat]++; if (cat!="DENTRO" && tolower($0) ~ /\.pdf$/) pdf_fuera++;
  if (cat!="DENTRO" && tolower($0) ~ /\.bat$/) bat_fuera++;
}
END { for (k in c) printf "  %-45s %d\n", k, c[k]; printf "  PDF fuera: %d; .bat fuera: %d\n", pdf_fuera+0, bat_fuera+0 }' | sort
echo "== subdirectorios de primer nivel bajo personaje_v2/ fuera del alcance (recuento):"
grep -v '/$' "$L" | grep '^munger_v2_r1/personaje_v2/' | grep -v -e '^munger_v2_r1/personaje_v2/empresas_v2/' -e '^munger_v2_r1/personaje_v2/empresas_v2_correcciones/' | awk -F/ '{ if (NF==3) k="(archivo suelto en personaje_v2/)"; else k=$3"/"; c[k]++ } END { for (k in c) printf "  %-40s %d\n", k, c[k] }' | sort
echo "== fila ZIP del inventario publicado:"
grep '^ZIP base-4.14' "$INV" | cut -d, -f9-
rm -f "$L"
