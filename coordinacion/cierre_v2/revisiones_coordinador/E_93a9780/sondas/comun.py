"""Utilidades comunes de las sondas del revisor (solo lectura; sin red)."""
import hashlib
import re
import subprocess
import unicodedata


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def pagina(pdf, n, layout=True):
    cmd = ["pdftotext"] + (["-layout"] if layout else []) + ["-f", str(n), "-l", str(n), pdf, "-"]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError(f"pdftotext fallo en p{n}: {r.stderr[:200]}")
    return r.stdout


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("‑", "-"), ("‐", "-"), ("–", "-"), ("—", "-"), ("−", "-"),
                 (" ", " "), (" ", " "), ("’", "'"), ("“", '"'), ("”", '"')]:
        s = s.replace(a, b)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()
