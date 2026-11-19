#!/bin/bash
# Revisor: verificar_paquete.sh rapida sobre una copia limpia de fbb146d (git archive + los 1060 binarios del manifiesto, copiados solo si su huella coincide)
set -u
S=/tmp/claude-0/-home-user/b9d62468-c45b-5fe5-8762-d58eebe9c95a/scratchpad/rev/r4
C=/dev/shm/rev4/limpia
rm -rf $C && mkdir -p $C
cd /home/user/e_work/wt_circulante && git archive fbb146d | tar -x -C $C
cd $C/munger_v2_r1 && python3 -I - <<'PY'
import hashlib, os, shutil, subprocess
raiz = os.getcwd()
srcs = ["/home/user/e_work/wt_circulante/munger_v2_r1", "/home/user/e_work/wt_expedientes/munger_v2_r1"]
man = [l.split("  ", 1) for l in open("MANIFIESTO_SHA256.txt", encoding="utf-8").read().splitlines() if l.strip() and not l.startswith("#")]
def h(p):
    s = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): s.update(b)
    return s.hexdigest()
falta, copiados = [], 0
for hu, ruta in man:
    if os.path.exists(ruta):
        continue
    for s in srcs:
        p = os.path.join(s, ruta)
        if os.path.isfile(p) and h(p) == hu:
            os.makedirs(os.path.dirname(ruta) or ".", exist_ok=True); shutil.copy2(p, ruta); copiados += 1; break
    else:
        falta.append(ruta)
print("binarios copiados", copiados, "· sin copia con su huella", len(falta), falta[:5])
PY
export TMPDIR=/dev/shm/rev4/tmp
s=$(date +%s)
( cd $C/munger_v2_r1 && flock /home/user/e_work/libreoffice.lock timeout 3600 bash verificar_paquete.sh rapida ) > $S/rapida_fbb146d.txt 2>&1
echo "rc=$? · $(( $(date +%s) - s )) s" >> $S/rapida_fbb146d.txt
echo FIN > $S/rapida_FIN
