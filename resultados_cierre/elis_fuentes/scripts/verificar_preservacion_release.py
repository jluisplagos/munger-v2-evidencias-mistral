"""E2 (estado de preservacion): verifica que los 11 PDF nuevos de E-ELIS estan preservados en la Release 'fuentes-elis-e-20261117'.

Uso:
  python3 scripts/verificar_preservacion_release.py [--dir DIR]

- Sin --dir descarga los assets con: gh release download fuentes-elis-e-20261117 --repo jluisplagos/munger-v2-evidencias-mistral --dir <tmp>
  (solo lectura; no hay uploads ni tokens).
- Con --dir DIR usa los assets ya descargados en DIR (p. ej. para reproduccion sin red).

Comprueba:
1. sha256sum -c SHA256SUMS dentro del directorio de la Release (11/11 PDF).
2. Cada sha256 de la Release coincide con la fila correspondiente de
   fuentes_descargadas/INDICE_DESCARGAS.csv (11/11; la fila urd2025 se excluye: es base-4.14).
3. La fila urd2025 del indice tiene sha256 04bfd087... (URD 2025 de base-4.14).

Exit 0 si todo OK, exit 1 si falla algo, exit 2 si faltan dependencias (gh o el dir).
"""
import argparse
import csv
import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
SALIDA = RAIZ / "resultados_cierre/elis_fuentes"
REPO = "jluisplagos/munger-v2-evidencias-mistral"
TAG = "fuentes-elis-e-20261117"
SHA_URD2025 = "04bfd08724e768804e7110093d3ec2cf017a7e7fe2983bacd75656d3a95cd62e"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", help="directorio con los assets ya descargados de la Release")
    args = ap.parse_args()
    tmp = None
    if args.dir:
        d = Path(args.dir)
    else:
        if shutil.which("gh") is None:
            print("DEPENDENCIA AUSENTE: gh no disponible y no se paso --dir")
            sys.exit(2)
        tmp = tempfile.mkdtemp(prefix="release_elis_")
        r = subprocess.run(["gh", "release", "download", TAG, "--repo", REPO, "--dir", tmp],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print("FALLO gh release download:", r.stderr[:300])
            sys.exit(2)
        d = Path(tmp)
    sums = d / "SHA256SUMS"
    if not sums.exists():
        print(f"FALLO: no esta {sums}")
        sys.exit(1)
    ok_rel = 0
    n_rel = 0
    release = {}
    for line in sums.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        h, name = line.split(maxsplit=1)
        name = name.strip().lstrip("*")
        n_rel += 1
        f = d / name
        if not f.exists():
            print("FALLO: falta asset", name)
            continue
        if hashlib.sha256(f.read_bytes()).hexdigest() == h:
            ok_rel += 1
        else:
            print("FALLO sha256:", name)
        release[name[:-4] if name.endswith(".pdf") else name] = h
    print(f"Release '{TAG}': {ok_rel}/{n_rel} assets verifican contra SHA256SUMS")

    indice = {r["id"]: r for r in csv.DictReader((SALIDA / "fuentes_descargadas" / "INDICE_DESCARGAS.csv").open(encoding="utf-8"))}
    ok_idx = 0
    n_idx = 0
    for rid, row in indice.items():
        if rid == "urd2025":
            continue
        n_idx += 1
        if release.get(rid) == row["sha256"]:
            ok_idx += 1
        else:
            print("FALLO: indice vs Release difieren en", rid)
    print(f"INDICE_DESCARGAS.csv vs Release: {ok_idx}/{n_idx} PDF nuevos coinciden (11/11 esperado)")
    urd_ok = indice.get("urd2025", {}).get("sha256") == SHA_URD2025
    print(f"urd2025 en indice == base-4.14 (04bfd087...): {urd_ok}")
    if tmp:
        shutil.rmtree(tmp, ignore_errors=True)
    if ok_rel == n_rel and ok_idx == n_idx == 11 and urd_ok:
        print("PRESERVACION VERIFICADA: 11/11 PDF en la Release '" + TAG + "' con sha256 iguales al indice de descarga")
        sys.exit(0)
    sys.exit(1)


if __name__ == "__main__":
    main()
