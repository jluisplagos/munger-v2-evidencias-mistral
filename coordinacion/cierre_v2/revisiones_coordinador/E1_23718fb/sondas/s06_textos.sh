#!/usr/bin/env bash
# s06 · E-R1 (retirada de la afirmacion), E-R7 (frases absolutas), E-R8 (textos desfasados), cobertura hallazgo/cita,
#       y comprobacion de la cobertura en la base 4.14 de cifras rotuladas «nuevo».
# Uso: bash s06_textos.sh <dir_entrega_elis_fuentes> <pdf_semestral_2026_EN_de_la_base> <dir_pdf_11>
set -u
E="$1"; S1="$2"; P="$3"; cd "$E"
X="--exclude-dir=extractos --exclude=VERIFICACION_SEGUNDO_EXTRACTOR.json"
echo "== E-R1: afirmaciones positivas de 'concepto monetario'/'flujo operativo' para el +25,7 (solo deben quedar menciones de retirada)"
grep -rnoiE ".{0,60}(concepto monetario|flujo (de caja )?operativo|caja operativa).{0,40}" $X . | cut -c1-200
echo "== E-R7: frases absolutas (grep del autor y grep ampliado)"
echo "-- grep del autor (no publicad|sin publicar) fuera de scripts:"; grep -rnoiE ".{0,40}(no publicad|sin publicar|sigue sin publicarse).{0,40}" $X --exclude-dir=scripts . | cut -c1-160
echo "-- ampliado (ningun[ao]? .* publicad|sin cifra publicada|No publica):"; grep -rnoiE ".{0,60}(ningun[ao]? (tasa|importe|cifra)[^,;.]{0,30}publicad[oa]|sin cifra publicada|No publica la).{0,40}" $X --exclude-dir=scripts . | cut -c1-200
echo "== E-R8: 'este commit' en f00c5dd (ambiguo: 23718fb o f00c5dd)"
grep -rnoE ".{0,60}este commit.{0,30}" $X --exclude-dir=scripts . | cut -c1-160
echo "-- ENTREGA.json menciona f00c5dd / CHECKPOINT_RELEVO: $(grep -cE 'f00c5dd|CHECKPOINT_RELEVO' ENTREGA.json)"
echo "-- menciones a la Release fuentes-elis-e-20261117: $(grep -rl 'fuentes-elis-e-20261117' . | wc -l); archivos con PROVISIONAL: $(grep -rl PROVISIONAL . | wc -l)"
echo "-- erratas de nombre: $(grep -rhoE 'W[aä]rts ?cherei' $X . | sort | uniq -c | tr '\n' ' ')"
echo "== E-R5: afirmaciones de hallazgo fuera de la cita registrada (presentes en la pagina/extracto, no en la cita)"
python3 -I - <<'PY'
import json
chk = {3: "lino", 4: "FCF 358,6", 20: "37%", 23: "disciplina de precios", 24: "efecto divisa"}
n = 0
for l in open("LECTURA_FUENTES.jsonl", encoding="utf-8"):
    d = json.loads(l)
    if d["tipo"] != "cita": continue
    n += 1
    if n in chk: print(f"[{n}] {d['documento']} p{d['pagina_pdf']}: hallazgo dice «{chk[n]}» -> en hallazgo: {chk[n] in d['hallazgo']}; cita registrada: «{d['cita'][:70]}»")
PY
for spec in "fy2025_comunicado_en 6 linen.investment fy2025_comunicado_en_p6" "fy2025_presentacion_en 29 358.6 fy2025_presentacion_en_p29" "factsheet2026 1 37% factsheet2026_p1" "q3_2026_revenue 3 pricing.discipline q3_2026_revenue_p3"; do
  set -- $spec; a=$(pdftotext -f $2 -l $2 "$P/$1.pdf" - 2>/dev/null | tr '\n' ' ' | grep -ciE "$3"); b=$(tr '\n' ' ' < "extractos/$4.txt" | grep -ciE "$3"); echo "  $1 p$2 «$3»: en pagina=$a en extracto=$b"; done
echo "== E-R4: H1-2026 19,5% rotulado «nuevo»; ¿esta en la base 4.14?"
grep -rnoE ".{0,30}H1-2026 19,5% nuevo.{0,10}" $X --exclude-dir=scripts . | cut -c1-120
echo "huella del informe semestral 2026 EN de la base: $(sha256sum "$S1" | cut -c1-16)…"
pdftotext -f 10 -l 10 "$S1" - 2>/dev/null | tr '\n' ' ' | grep -oE "ratio stood at 19\.5% in H1 2026 \(versus 18\.4% in H1 2025\)[^.]{0,80}" | sed 's/^/  base p.10: /'
