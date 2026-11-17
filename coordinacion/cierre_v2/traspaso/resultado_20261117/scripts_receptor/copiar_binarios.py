"""Copia improvisada por el receptor (paso 5 de T-TRASPASO; procedimiento no documentado).

Copia los archivos con storage == "release_asset" de baselines/4.14.json desde la base
materializada (clon de main) a la candidata, sin sobrescribir nunca. Comprueba la huella
del origen antes de copiar y la del destino después. Escribe un informe JSON.

Uso: python3 -I copiar_binarios.py <raiz_main> <raiz_candidata> <informe.json>
"""
import hashlib
import json
import shutil
import sys
from pathlib import Path


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main():
    src_root, dst_root, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    idx = json.loads((src_root / "baselines/4.14.json").read_text())
    pref = idx["archive_prefix"]
    res = {"copiados": [], "existentes_iguales": [], "distintos": [], "fallos": []}
    for e in idx["files"]:
        if e["storage"] != "release_asset":
            continue
        rel = pref + e["path"]
        s, d = src_root / rel, dst_root / rel
        try:
            if s.is_symlink() or not s.is_file() or sha(s) != e["sha256"]:
                res["fallos"].append({"ruta": rel, "motivo": "origen ausente o con huella distinta"})
                continue
            if d.exists() or d.is_symlink():
                (res["existentes_iguales"] if d.is_file() and sha(d) == e["sha256"] else res["distintos"]).append(rel)
                continue
            d.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(s, d)
            if sha(d) != e["sha256"]:
                res["fallos"].append({"ruta": rel, "motivo": "huella distinta tras copiar"})
            else:
                res["copiados"].append(rel)
        except OSError as ex:
            res["fallos"].append({"ruta": rel, "motivo": str(ex)})
    resumen = {k: len(v) for k, v in res.items()}
    out.write_text(json.dumps({"resumen": resumen, **res}, ensure_ascii=False, indent=1))
    print(json.dumps(resumen))
    return 0 if resumen["fallos"] == 0 and resumen["distintos"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
