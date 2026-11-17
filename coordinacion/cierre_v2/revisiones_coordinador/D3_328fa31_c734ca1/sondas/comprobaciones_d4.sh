#!/usr/bin/env bash
# Comprobaciones del revisor sobre mistral/d-qwen-aceptacion @ c734ca1 (bloques A 328fa31 y B c734ca1).
# Uso: bash comprobaciones_d4.sh <aux> <rev_D3> <cand957> [<candidata>]
#   <aux>       clon de jluisplagos/munger-v2-evidencias-mistral (solo lectura; ya con `git fetch` de las ramas)
#   <rev_D3>    carpeta de esta revisión; contiene wt/ (git worktree add --detach <rev_D3>/wt c734ca1), banco/
#               (git archive 4745f38 resultados_qwen/q1_v2/banco_revisado), previas/ (sondas de las revisiones
#               anteriores, extraídas de coordinacion/cierre-v2) y sondas/ (este directorio)
#   <cand957>   copia PROPIA del producto en 957af65 con la base materializada (aquí: clon local + los 1008
#               binarios; su MANIFIESTO_SHA256.txt da 7762/7762). El arnés ejecuta sus scripts con -B y no escribe en ella.
#   <candidata> opcional: la candidata compartida, solo para comprobar el comando con SHA_CANDIDATA_ESPERADO
# No usa red. No ejecuta LibreOffice ni agentes: los comandos del producto que lanza el arnés (verificacion_entradas.py,
# ficha.py, informe.py, cambiar_base.py preparar, fase1_historia.py construir) no lo invocan. Todo se escribe bajo <rev_D3>.
set -u
AUX=$1; REV=$2; CAND=$3; COMP=${4:-}
WT=$REV/wt; E=$WT/resultados_qwen/ejecucion_d; B=$REV/banco/resultados_qwen/q1_v2/banco_revisado; T=$REV/trabajo; S=$REV/sondas
export TMPDIR=$T/tmp BANCO_DIR=$B GIT_OPTIONAL_LOCKS=0 LC_ALL=C.UTF-8; mkdir -p "$TMPDIR"
san() { sed -e "s#$REV#<rev_D3>#g" -e "s#$AUX#<aux>#g" ${COMP:+-e "s#$COMP#<candidata>#g"}; }
copia() { rm -rf "$T/$1"; mkdir -p "$T/$1/resultados_qwen"; cp -a "$E" "$T/$1/resultados_qwen/"; echo "$T/$1/resultados_qwen/ejecucion_d"; }
h() { echo; echo "=== $*"; }

h "0 · objeto"
echo "worktree: $(git -C "$WT" rev-parse HEAD) · limpio: $(git -C "$WT" status --porcelain | wc -l) cambios"
git -C "$WT" log --format='%h %ad %s' --date=format:'%H:%M:%S' d032691..c734ca1 | cut -c1-110
echo "banco: sha256sum -c exit $(cd "$B" && sha256sum -c --quiet MANIFIESTO_SHA256.txt >/dev/null 2>&1; echo $?) · casos $(sha256sum < "$B/casos_aceptacion.jsonl" | cut -c1-16)…"
echo "cand957: HEAD $(git -C "$CAND" rev-parse --short HEAD) · manifiesto del producto exit $(cd "$CAND/munger_v2_r1" && sha256sum -c --quiet MANIFIESTO_SHA256.txt >/dev/null 2>&1; echo $?)"
echo "herramientas en este entorno: pdftotext=$(command -v pdftotext || echo no) soffice=$(command -v soffice || echo no) python=$(python3 --version 2>&1)"

h "1 · D3-R6 manifiesto (cd resultados_qwen/ejecucion_d && sha256sum -c MANIFIESTO_SHA256.txt)"
(cd "$E" && sha256sum -c MANIFIESTO_SHA256.txt > "$TMPDIR/manif.out" 2>&1; echo "exit $? · OK $(grep -c ': OK$' "$TMPDIR/manif.out") · FAILED $(grep -c ': FAILED$' "$TMPDIR/manif.out") · entradas $(grep -c . MANIFIESTO_SHA256.txt) · archivos $(find . -type f ! -name MANIFIESTO_SHA256.txt | wc -l)")

h "2 · D3-R8/R3 último commit que toca cada documento de entrega"
for f in ENTREGA.json RESPUESTA_D2.md PUNTO_DE_RECUPERACION.md README.md HALLAZGOS.md RESUMEN_PARA_INTEGRADOR.md RELEVO_SUPERVISADO.md CONFIGURACION.json MANIFIESTO_SHA256.txt evidencias/pruebas_arnes.log scripts/generar_relevo.py scripts/preparar_entorno.sh scripts/lib_arnes.py scripts/generar_matriz.py; do
  printf '%-34s %s\n' "$f" "$(git -C "$WT" log -1 --format='%h %ad' --date=format:'%H:%M:%S' -- "resultados_qwen/ejecucion_d/$f")"; done
echo "especificaciones en disco: $(ls "$E"/scripts/especificaciones/*/Q1-*.json | wc -l) · resultados: $(ls "$E"/evidencias/Q1-*/resultado_ejecucion.json | wc -l) · documentos que dicen «28 esp…»: $(grep -l -E '28 (specs|especificaciones|casos)' "$E"/*.md "$E"/*.json | wc -l)"
echo "textos caducados frente a c734ca1: CONFIGURACION.harness_version=$(python3 -I -c "import json;print(json.load(open('$E/CONFIGURACION.json'))['harness_version'][:3])") (el arnés es $(grep -o 'HARNESS_VERSION = "[0-9.]*"' "$E/scripts/lib_arnes.py")) · «59 con aserción» en $(grep -l '59 con aserci' "$E"/*.md "$E"/*.json | wc -l) documentos (el MAPA dice 54) · «16/16» en $(grep -l '16/16' "$E"/*.md "$E"/*.json | wc -l) documentos (pruebas_arnes.py declara 36 pruebas)"
echo "RESPUESTA_D3*: $(ls "$E" | grep -c -i 'RESPUESTA_D3') archivos · base_revisada_sha de ENTREGA.json: $(python3 -I -c "import json;print(json.load(open('$E/ENTREGA.json'))['base_revisada_sha'][:7])")"

h "3 · D3-R3 regeneración desde la evidencia publicada (cmp con lo publicado)"
C=$(copia regen); (cd "$C" && for s in generar_matriz.py generar_correspondencia.py generar_relevo.py; do python3 -I -B scripts/$s >/dev/null 2>&1; echo "$s exit $?"; done
 for f in MATRIZ_EJECUCION.csv MAPA_CRITERIOS_BANCO.csv relevo/PAQUETES_RELEVO.json evidencias/recuentos.json; do cmp -s "$f" "$E/$f"; echo "cmp $f = $?"; done
 python3 -I -c "import json;r=json.load(open('evidencias/recuentos.json'));print(r['estado_ejecucion'],r['veredicto_componente'],r['veredicto_caso'],r['criterios_banco'])")

h "4 · sondas de las revisiones anteriores, SIN CAMBIOS, sobre c734ca1 (stubs)"
C=$(copia sondas_copia)
python3 -I -B "$REV/previas/D_d032691/sondas/sondas_arnes_d3.py" "$C" "$B" "$S/s01_sondas_arnes_d3_original_sobre_c734ca1.json" > "$S/s01_sondas_arnes_d3_original_sobre_c734ca1.stdout" 2>&1; echo "sondas_arnes_d3.py exit $?"
python3 -I -B "$REV/previas/D2_3934bc9_5f4b2a2/sondas/sondas_arnes_d2.py" "$C" "$C" "$B" "$S/s01b_sondas_arnes_d2_original_sobre_c734ca1.json" > "$S/s01b_sondas_arnes_d2_original_sobre_c734ca1.stdout" 2>&1; echo "sondas_arnes_d2.py exit $?"
C2=$(copia sondas_autor); (cd "$C2" && python3 -I sondas/sondas_d2.py . "$B" sondas/sondas_d2.json > "$TMPDIR/sa.out" 2>&1; echo "sondas/sondas_d2.py DEL AUTOR exit $? · veredictos: $(grep -o '"veredicto": "[A-Z]*' "$TMPDIR/sa.out" | sort | uniq -c | tr -s ' ' | tr '\n' ';')"); san < "$TMPDIR/sa.out" > "$S/s11_sondas_d2_del_autor_sobre_c734ca1.out"
python3 -I - "$S/s01_sondas_arnes_d3_original_sobre_c734ca1.json" <<'EOF'
import json, sys
d = json.load(open(sys.argv[1]))
for k, v in d["R1_arnes"].items(): print(f"  {k}: exit {v.get('exit')} estado {v.get('estado','-')} → {v['veredicto']}")
for k, v in d["R1_matriz"].items():
    if isinstance(v, dict) and "estado_ejecucion" in v: print(f"  {k}: {v['estado_ejecucion']} / {v['veredicto_componente'] or '-'}")
for k in ("P7c_stderr_real", "P7v_ajeno_con_lineas_antiguas", "P7v2_CAMBIO_invalido_mas_lineas_reales (nueva)", "Q1-034_con_producto_de_eco"):
    print(f"  {k}: exit {d['R2'][k]['exit']} {d['R2'][k]['estado']}")
print("  R4: Q1-005→COMPONENTE_FALLA deja solo:", [f["qué"] for f in d["R4_relevo"]["Q1-005_tras_pasar_a_COMPONENTE_FALLA"]["falta"]], "· Q1-028/Q1-032:", d["R4_relevo"]["publicado_Q1-028_Q1-032"])
EOF

h "5 · sondas NUEVAS (stubs): s02"
python3 -I -B "$S/s02_sondas_arnes_d4.py" "$C" "$B" "$S/s02_sondas_arnes_d4.json" > "$S/s02_sondas_arnes_d4.stdout" 2>&1; echo "s02 exit $?"
python3 -I - "$S/s02_sondas_arnes_d4.json" <<'EOF'
import json, sys
d = json.load(open(sys.argv[1]))
for g in ("INV3_aserciones_sobre_archivos_del_arnes", "INV1_rutas", "INV4_id", "INV5_candidata_limpia"):
    for k, v in d[g].items():
        if "veredicto" in v: print(f"  {k}: exit {v.get('exit')} estado {v.get('estado','-')} matriz {v.get('matriz','-')} → {v['veredicto'][:95]}")
m = d["INV2_R3_matriz"]
print("  E1:", m["E1_M3b_Q1-026_resultado_de_un_campo_ERROR_ENTORNO"]["estado_ejecucion"], "| E2:", m["E2_M3c_Q1-026_ejecutado_con_candidata_sucia"]["estado"], "→", m["E2_M3c_Q1-026_ejecutado_con_candidata_sucia"]["matriz"]["estado_ejecucion"], "·", m["E2_M3c_Q1-026_ejecutado_con_candidata_sucia"]["matriz"]["veredicto_caso"][:70])
e3 = m["E3_M7_generar_matriz_ignora_EVIDENCIAS_DIR"]
print("  E3: ejecutar_caso con EVIDENCIAS_DIR propio →", e3["ejecutar_caso_con_EVIDENCIAS_DIR_propio"]["estado"], "| generar_matriz con el mismo EVIDENCIAS_DIR →", e3["generar_matriz_con_el_mismo_EVIDENCIAS_DIR"]["veredicto_componente"])
EOF

h "5b · A1 y A2 repetidas con el PRODUCTO REAL 957af65 (s16)"
export CANDIDATA_DIR=$CAND
mkdir -p "$T/s16"; rm -rf "$T/s16/ev"
for v in A1 A2; do (cd "$T/s16" && RUN_DIR=$T/run_s16 EVIDENCIAS_DIR=$T/s16/ev python3 -I -B "$E/scripts/ejecutar_caso.py" "$S/s16_${v}_producto_real.json" 2>&1 | san | cut -c1-100; echo "  exit ${PIPESTATUS[0]}"); done
python3 -I -c "
import json
for cid in ('Q1-031','Q1-033'):
    r=json.load(open('$T/s16/ev/'+cid+'/resultado_ejecucion.json'))
    print('  ',cid, r['estado_caso'], '· comandos del producto ejecutados:', [(p['descripcion'][:22], p['exit']) for p in r['pasos'] if p.get('comando')], '· archivos «del producto» según el arnés:', r['archivos_producto'], '· origen real:', [a['archivo'] for a in r['artefactos']])"

h "6 · pruebas del autor (python3 -B scripts/pruebas_arnes.py) contra el producto real 957af65"
C=$(copia pruebas_autor); (cd "$C" && RUN_DIR=$T/run_pruebas_autor python3 -B scripts/pruebas_arnes.py > "$TMPDIR/pa.out" 2>&1; echo "exit $?" >> "$TMPDIR/pa.out"); san < "$TMPDIR/pa.out" > "$S/s03_pruebas_arnes_autor_tal_cual.out"
echo "tal cual: $(grep -c '^PASA' "$TMPDIR/pa.out") PASA · $(grep -c '^FALLA' "$TMPDIR/pa.out") FALLA · $(grep -E '^[A-Za-z]+Error' "$TMPDIR/pa.out" | san | cut -c1-150) · $(tail -1 "$TMPDIR/pa.out")"
C=$(copia pruebas_autor_parche); (cd "$C" && patch -s -p0 scripts/pruebas_arnes.py < "$S/s04_parches_del_revisor_a_pruebas_arnes.diff" && RUN_DIR=$T/run_pruebas_autor_parche python3 -B scripts/pruebas_arnes.py > "$TMPDIR/pp.out" 2>&1; echo "exit $?" >> "$TMPDIR/pp.out"); san < "$TMPDIR/pp.out" > "$S/s04_pruebas_arnes_autor_con_parches.out"
echo "con 4 parches mínimos del revisor (s04_parches…diff): $(grep -c '^PASA' "$TMPDIR/pp.out") PASA · FALLA: [$(grep '^FALLA' "$TMPDIR/pp.out" | cut -c9-130)] · $(grep -E '^[A-Za-z]+Error' "$TMPDIR/pp.out" | san | cut -c1-150) · $(tail -1 "$TMPDIR/pp.out")"
rm -rf "$T/pruebas_autor_mutante"; cp -a "$T/pruebas_autor_parche" "$T/pruebas_autor_mutante"; C=$T/pruebas_autor_mutante/resultados_qwen/ejecucion_d
(cd "$C" && python3 -I - <<'EOF'
import json
p = "scripts/lib_arnes.py"; s = open(p, encoding="utf-8").read()
a = s[s.index("    if not isinstance(rel, str) or not rel or os.path.isabs(rel):"):s.index("def validar_id")]
s = s.replace(a, "    return os.path.realpath(os.path.join(os.path.realpath(base), rel))  # MUTANTE A DEL REVISOR: sin contención de rutas\n\n\n")
open(p, "w", encoding="utf-8").write(s)
p = "scripts/especificaciones/piloto/Q1-027.json"; d = json.load(open(p, encoding="utf-8"))
assert [c for c in d["criterios"] if c["id"] == "C4"][0].pop("no_discriminante") is True      # MUTANTE B: C4 sin la marca
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
EOF
 RUN_DIR=$T/run_pruebas_autor_mutante python3 -B scripts/pruebas_arnes.py > "$TMPDIR/pm.out" 2>&1; echo "exit $?" >> "$TMPDIR/pm.out"); san < "$TMPDIR/pm.out" > "$S/s05_pruebas_arnes_autor_sobre_mutantes.out"
echo "sobre el arnés MUTADO (A: ruta_dentro sin contención; B: Q1-027 C4 sin marca no_discriminante):"
grep -E '^(PASA|FALLA) · (10|17|18|19|20|34) ' "$TMPDIR/pm.out" | cut -c1-120 | sed 's/^/  /'

h "7 · D3-R3 reejecución REAL de las 30 especificaciones (bash scripts/ejecutar_todo.sh) y comparación byte a byte"
mkdir -p "$T/bin_sin_pdf"; if [ -z "$(ls -A "$T/bin_sin_pdf")" ]; then IFS=:; for d in $PATH; do [ -d "$d" ] || continue; for f in "$d"/*; do n=$(basename "$f"); case "$n" in pdf*|soffice|libreoffice|lo*|unopkg|sbase|scalc|sdraw|simpress|smath|swriter) continue;; esac; [ -x "$f" ] && [ ! -e "$T/bin_sin_pdf/$n" ] && ln -s "$f" "$T/bin_sin_pdf/$n"; done; done; unset IFS; fi
for modo in sin_pdf con_pdf; do
  C=$(copia real_$modo); rm -rf "$T/run_real_$modo"
  if [ $modo = sin_pdf ]; then P=$T/bin_sin_pdf; else P=$PATH; fi
  (cd "$C" && RUN_DIR=$T/run_real_$modo PATH=$P bash scripts/ejecutar_todo.sh > "$TMPDIR/et_$modo.out" 2>&1; echo "exit $?" >> "$TMPDIR/et_$modo.out"); san < "$TMPDIR/et_$modo.out" > "$S/s06_ejecutar_todo_957af65_$modo.out"
  echo "[$modo: pdftotext $( [ $modo = sin_pdf ] && echo ausente || echo presente )] $(grep -c '^OK ' "$TMPDIR/et_$modo.out") OK · $(tail -1 "$TMPDIR/et_$modo.out") · $(grep 'estados:' "$TMPDIR/et_$modo.out")"
  (cd "$C" && for f in MATRIZ_EJECUCION.csv MAPA_CRITERIOS_BANCO.csv relevo/PAQUETES_RELEVO.json evidencias/recuentos.json; do cmp -s "$f" "$E/$f"; echo -n "cmp $f=$? · "; done; echo)
  python3 -I - "$E" "$C" <<'EOF'
import os, sys
A, B = sys.argv[1:3]; tot = 0; dif = []
for cid in sorted(os.listdir(os.path.join(A, "evidencias"))):
    da, db = os.path.join(A, "evidencias", cid), os.path.join(B, "evidencias", cid)
    if not os.path.isdir(da): continue
    for f in sorted(os.listdir(da)):
        if f in ("ejecucion.log", "resultado_ejecucion.json"): continue
        tot += 1
        if not os.path.isfile(os.path.join(db, f)) or open(os.path.join(da, f), "rb").read() != open(os.path.join(db, f), "rb").read(): dif.append(f"{cid}/{f}")
print(f"  salidas del producto publicadas vs reejecutadas: {tot - len(dif)}/{tot} idénticas; distintas (solo cambia RUN_DIR): {dif}")
EOF
done
cmp "$E/evidencias/Q1-026/cambiar_base_preparar.txt" "$T/real_con_pdf/resultados_qwen/ejecucion_d/evidencias/Q1-026/cambiar_base_preparar.txt" && echo "Q1-026: con pdftotext y soffice en el PATH, cambiar_base_preparar.txt es IDÉNTICO al publicado (las mismas 9 líneas)"

h "8 · Q1-026: de dónde salen las 9 líneas, y qué pasa con otro expediente base"
rm -rf "$T/q026_construir"; mkdir -p "$T/q026_construir"; cp -a "$T/run_real_con_pdf/Q1-026/pruebas_d/Q1-026_origen" "$T/q026_construir/Viscofan"
(cd "$CAND/munger_v2_r1/personaje_v2/scripts" && python3 -B fase1_historia.py construir "$T/q026_construir/Viscofan" > "$TMPDIR/c.out" 2>&1; echo "exit $?" >> "$TMPDIR/c.out"); san < "$TMPDIR/c.out" > "$S/s08_q026_fase1_historia_construir_completo.out"
echo "fase1_historia.py construir sobre el origen (plantilla 4.13 Viscofan): $(grep -vc '^exit' "$TMPDIR/c.out") líneas de error ($(grep -c 'ausente o inexistente' "$TMPDIR/c.out") textos ausentes, $(grep -c 'sin «cita»' "$TMPDIR/c.out") ceros sin cita) · $(tail -1 "$TMPDIR/c.out") · bytes $(grep -v '^exit' "$TMPDIR/c.out" | wc -c) (cambiar_base.py:300 publica solo los últimos 600 caracteres)"
echo "texto/ de la plantilla: $(ls "$CAND/munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_13/viscofan/Viscofan/texto" | tr '\n' ' ')"
echo "PDF o texto AR_2021..AR_2024 de Viscofan en toda la candidata: $(find "$CAND" -path "$CAND/.git" -prune -o -ipath '*viscofan*' \( -name 'AR_2021.*' -o -name 'AR_2022.*' -o -name 'AR_2023.*' -o -name 'AR_2024.*' \) ! -path '*fase1_partes*' -print | wc -l)"
mkdir -p "$T/construir_alt"; for e in 2026-11_Vidrala_ensayo_4_14/viscofan/Viscofan 2026-11_Vidrala_ensayo_4_14/viscofan_decisiones/Viscofan 2026-11_Vidrala_ensayo_4_14/vidrala_decisiones/Vidrala 2026-11_Vidrala_ensayo_4_14/elis_decisiones/Elis; do n=$(echo $e | tr '/' '_'); rm -rf "$T/construir_alt/$n"; cp -a "$CAND/munger_v2_r1/personaje_v2/empresas_v2_correcciones/$e" "$T/construir_alt/$n"; (cd "$CAND/munger_v2_r1/personaje_v2/scripts" && python3 -B fase1_historia.py construir "$T/construir_alt/$n" > "$TMPDIR/ca.out" 2>&1; echo "  construir sobre $e: exit $? · $(head -1 "$TMPDIR/ca.out" | cut -c1-60)"); done
C=$(copia q026_base414); rm -rf "$T/run_q026_base414"
(cd "$C" && RUN_DIR=$T/run_q026_base414 PLANTILLA_EXP=$CAND/munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/viscofan/Viscofan python3 -B scripts/ejecutar_caso.py scripts/especificaciones/bloque2/Q1-026.json > "$TMPDIR/q26.out" 2>&1; echo "arnés (misma spec, PLANTILLA_EXP = Viscofan 4.14): exit $? · $(cut -c1-70 "$TMPDIR/q26.out" | head -1)"
 python3 -I -c "
import json; r=json.load(open('evidencias/Q1-026/resultado_ejecucion.json')); p=[x for x in r['pasos'] if 'cambiar_base' in ' '.join(x['comando'])][0]
print('  cambiar_base.py preparar: exit', p['exit'], '(la spec espera', p['esperado'], ') · stderr vacío:', p['stderr']=='', '·', [l for l in p['stdout'].splitlines() if 'Entradas sustituidas' in l or 'Origen' in l][-1][:70])")
san < "$C/evidencias/Q1-026/cambiar_base_preparar.txt" > "$S/s08b_q026_preparar_con_base_viscofan_4_14.out"

h "9 · D3-R2 control REAL contra el estado previo (s09) y Q1-017 sin los pasos del caso (s09b)"
mkdir -p "$T/base"; (cd "$T/base" && RUN_DIR=$T/run_base EVIDENCIAS_DIR=$T/base/evidencias python3 -I -B "$E/scripts/ejecutar_caso.py" "$S/s09_spec_estado_previo.json" >/dev/null 2>&1; cmp -s evidencias/Q1-031/00_estado_previo.json "$S/s09_estado_previo_plantilla_957af65.json"; echo "estado previo regenerado == s09_estado_previo_plantilla_957af65.json: cmp $?")
python3 -I -B "$S/s09_control_estado_previo.py" "$T/sondas_copia/resultados_qwen/ejecucion_d" "$S/s09_estado_previo_plantilla_957af65.json" "$S/s09_control_estado_previo.json" > "$S/s09_control_estado_previo.stdout" 2>&1
python3 -I -c "import json;d=json.load(open('$S/s09_control_estado_previo.json'));print('  aserciones',d['aserciones'],'· sobre comprobar',d['aserciones_sobre_comprobar']);print('  criterios íntegros sobre su estado previo:',[(x['caso'],x['criterio'],'marcado' if x['marcado_no_discriminante'] else 'SIN MARCA: cuenta como CUMPLE') for x in d['CRITERIOS_que_pasan_integros_en_el_estado_previo']])"
mkdir -p "$T/q017"; (cd "$T/q017" && RUN_DIR=$T/run_q017 EVIDENCIAS_DIR=$T/q017/evidencias python3 -I -B "$E/scripts/ejecutar_caso.py" "$S/s09b_q017_sin_pasos_del_caso.json" 2>&1 | san | cut -c1-90; echo "  exit ${PIPESTATUS[0]}")

h "10 · N1c con el producto real, D3-R7 y candidata compartida"
mkdir -p "$T/n1c"; rm -rf "$T/run_n1c"; mkdir -p "$T/run_n1c/Q1-036/Viscofan/fuentes_sinteticas"; printf '[PDF PAGE 1]\nExtracto sintetico del caso Q1-036.\n\n[PDF PAGE 2]\nTabla 4 pag.2: caja = 95 millones EUR.\n\n' > "$T/run_n1c/Q1-036/Viscofan/fuentes_sinteticas/ajena.txt"
(cd "$T/n1c" && RUN_DIR=$T/run_n1c EVIDENCIAS_DIR=$T/n1c/ev python3 -I -B "$E/scripts/ejecutar_caso.py" "$S/s14_n1c_fuente_en_otro_caso.json" 2>&1 | san | cut -c1-70; echo "  N1c (fuente.archivo=../../Q1-036/…): $(sed -n '2p' ev/Q1-031/01_sellar.txt | cut -c1-170)")
mkdir -p "$T/r7"; (cd "$T/r7" && rm -rf ev && RUN_DIR=$T/run_r7 EVIDENCIAS_DIR=$T/r7/ev python3 -I -B "$E/scripts/ejecutar_caso.py" "$S/s15_r7.json" >/dev/null 2>&1; for i in 1 2; do ARNES_EVIDENCIAS_LIMPIAS=0 RUN_DIR=$T/run_r7 EVIDENCIAS_DIR=$T/r7/ev python3 -I -B "$E/scripts/ejecutar_caso.py" "$S/s15_r7.json" >/dev/null 2>&1; done
 python3 -I -c "
import json
r=json.load(open('ev/Q1-033/resultado_ejecucion.json')); l=open('ev/Q1-033/ejecucion.log').read(); reg=json.load(open('$T/run_r7/Q1-033/Viscofan/verificacion_entradas.json'))
p=[x for x in r['pasos'] if 'sellar' in x['comando']][0]; print('  R7a --revisor:', p['comando'][p['comando'].index('--revisor')+1])
print('  R7b auxiliar sin comprobación:', [e['comprobacion'].get('_simulada') for e in reg['entradas'] if e['celda']=='aux:sin_comprobacion'])
print('  R7c ARNES_EVIDENCIAS_LIMPIAS=0: evidencias_limpiadas', r['evidencias_limpiadas'], '· cabeceras en el log', l.count('# Caso '), '· avisos', l.count('# AVISO: ARNES_EVIDENCIAS_LIMPIAS=0'))")
echo "  R7d preparar_entorno.sh:33 lee r['good'] → $(grep -c "r\['good'\]" "$E/scripts/preparar_entorno.sh") aparición; tools/base_414.py escribe: $(grep -o '"verified"\|"good"' "$CAND/tools/base_414.py" | sort -u | tr '\n' ' ')"
if [ -n "$COMP" ]; then SHA=$(git -C "$COMP" rev-parse HEAD); touch "$T/marca"; mkdir -p "$T/cand_compartida"
  (cd "$T/cand_compartida" && export RUN_DIR=$T/run_cand_compartida EVIDENCIAS_DIR=$T/cand_compartida/ev
   echo "  candidata compartida HEAD $(echo $SHA | cut -c1-7) · diff de personaje_v2/scripts frente a 957af65: $(git -C "$COMP" diff --name-only 957af65 HEAD -- munger_v2_r1/personaje_v2/scripts | wc -l) archivos"
   CANDIDATA_DIR=$COMP python3 -I -B "$E/scripts/ejecutar_caso.py" "$E/scripts/especificaciones/piloto/Q1-001.json" 2>&1 | san | cut -c1-150 | sed 's/^/  sin SHA_CANDIDATA_ESPERADO: /'
   CANDIDATA_DIR=$COMP SHA_CANDIDATA_ESPERADO=$SHA python3 -I -B "$E/scripts/ejecutar_caso.py" "$E/scripts/especificaciones/piloto/Q1-001.json" 2>&1 | san | cut -c1-90 | sed 's/^/  con SHA_CANDIDATA_ESPERADO=HEAD: /'
   echo "  candidata compartida tras la prueba: $(git -C "$COMP" status --porcelain | wc -l) cambios · $(find "$COMP" -newer "$T/marca" -not -path '*/.git/*' | wc -l) archivos nuevos"); fi

h "11 · D3-R5 (s10, s12) y D3-R4 (s13)"
python3 -I -B "$S/s10_auditoria_mapa_54_filas.py" "$T/sondas_copia/resultados_qwen/ejecucion_d" "$S/s10_auditoria_mapa_54_filas.csv" "$S/s10_auditoria_mapa_54_filas.json" | python3 -I -c "import json,sys;d=json.load(sys.stdin);print('  ',d['clasificacion_del_revisor'],'· NO_OBSERVA:',d['NO_OBSERVA'])"
python3 -I -B "$S/s12_cambio_q026_y_mapa_declarado.py" "$T/sondas_copia/resultados_qwen/ejecucion_d" "$B" "$S/s12_cambio_q026_y_mapa_declarado.json" | python3 -I -c "import json,sys;d=json.load(sys.stdin);a=d['a_validacion_del_CAMBIO'];print('  CAMBIO:',{k[:2]:(v['exit'],v['producto_llamado']) for k,v in a.items() if isinstance(v,dict)});b=d['b_MAPA_declarado'];print('  MAPA con aserción:',b['con_asercion_publicado'],'→',b['con_asercion_tras_declarar_dos_filas'],'tras declarar dos filas sin respaldo')"
python3 -I -B "$S/s13_prueba36_del_autor_sobre_paquetes_publicados.py" "$T/sondas_copia/resultados_qwen/ejecucion_d" "$S/s13_prueba36_del_autor_sobre_paquetes_publicados.json" | python3 -I -c "import json,sys;d=json.load(sys.stdin);print('  prueba 36 del autor:',d['prueba_36'],'·',d['incumplimientos'],'incumplimientos',d['por_tipo'],'· comando_relevo null:',d['comando_relevo_null'],'· mismo texto genérico en',d['paquetes_con_el_mismo_texto_generico_de_agente'],'paquetes')"
python3 -I - "$WT" <<'EOF'
import csv, io, json, subprocess, sys
def paq(c):
    t = subprocess.run(["git", "-C", sys.argv[1], "show", f"{c}:resultados_qwen/ejecucion_d/relevo/PAQUETES_RELEVO.json"], capture_output=True, text=True).stdout
    return {p["caso"]: p for p in json.loads(t)["paquetes"]}
pa, pc = paq("d032691"), paq("c734ca1")
print("  paquetes de relevo que cambian d032691→c734ca1:", [k for k in pa if pa[k] != pc[k]], "· Q1-028 y Q1-032 idénticos:", pa["Q1-028"] == pc["Q1-028"] and pa["Q1-032"] == pc["Q1-032"])
def mapa(c):
    t = subprocess.run(["git", "-C", sys.argv[1], "show", f"{c}:resultados_qwen/ejecucion_d/MAPA_CRITERIOS_BANCO.csv"], capture_output=True, text=True).stdout
    return {(r["caso"], r["criterio_indice"]): r for r in csv.DictReader(io.StringIO(t))}
a, c = mapa("d032691"), mapa("c734ca1")
print("  filas del MAPA que cambian de aserción d032691→c734ca1:", [f"{k[0]}#{k[1]}" for k in sorted(a) if (a[k]["asercion_arnes"], a[k]["cobertura"]) != (c[k]["asercion_arnes"], c[k]["cobertura"])])
EOF

h "12 · bloque A (328fa31) por separado: ¿su MATRIZ sale de su evidencia?"
rm -rf "$T/regen_328fa31"; mkdir -p "$T/regen_328fa31"; git -C "$WT" archive 328fa31 resultados_qwen/ejecucion_d | tar -x -C "$T/regen_328fa31"
(cd "$T/regen_328fa31/resultados_qwen/ejecucion_d" && cp MATRIZ_EJECUCION.csv "$TMPDIR/m328.csv" && python3 -I -B scripts/generar_matriz.py | grep 'estados:' ; cmp -s MATRIZ_EJECUCION.csv "$TMPDIR/m328.csv"; echo "  cmp MATRIZ regenerada vs publicada en 328fa31 = $? · candidata_sha de Q1-001 en 328fa31: $(grep -o '"candidata_sha": "[0-9a-f]\{10\}' evidencias/Q1-001/resultado_ejecucion.json) · $(sed -n '2p' evidencias/Q1-001/ejecucion.log | cut -c1-70)")

h "13 · higiene"
echo "rutas fuera de resultados_qwen/ejecucion_d en d032691..c734ca1: $(git -C "$WT" diff --name-only d032691 c734ca1 | grep -vc '^resultados_qwen/ejecucion_d/') · binarios: $(git -C "$WT" diff --numstat d032691 c734ca1 | awk '$1=="-"' | wc -l) · pyc rastreados: $(git -C "$WT" ls-files | grep -c -E '__pycache__|\.pyc$')"
echo "rutas absolutas en especificaciones: $(grep -rlE '"/(workspace|tmp|home|root)/' "$E/scripts/especificaciones" | wc -l) archivos · en el CAMBIO publicado: $(grep -cE '"(origen|destino)": "/workspace/' "$E/evidencias/Q1-026/CAMBIO_Q1-026.json") (origen y destino)"
echo "worktree de revisión sigue limpio: $(git -C "$WT" status --porcelain | wc -l) cambios · cand957: $(git -C "$CAND" diff --stat HEAD | wc -l) cambios rastreados, $(find "$CAND/munger_v2_r1/personaje_v2/scripts" -name __pycache__ | wc -l) __pycache__"
