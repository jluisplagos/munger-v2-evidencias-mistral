"""Comprueba cada cita de LECTURA_FUENTES.jsonl (E-ELIS @ 93a9780) en su página PDF: huella, texto normalizado de una página (pdftotext, con y sin -layout)."""
import hashlib, json, re, subprocess, sys, unicodedata
from pathlib import Path
lect, pdfdir, urd = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
def norm(s):
    s = unicodedata.normalize("NFKC", s).replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("­", "")
    s = re.sub(r"-\s*\n\s*", "", s)
    return re.sub(r"\s+", " ", s).strip().lower()
cache = {}
def pagina(ruta, p, layout):
    k = (str(ruta), p, layout)
    if k not in cache:
        a = ["pdftotext"] + (["-layout"] if layout else []) + ["-f", str(p), "-l", str(p), str(ruta), "-"]
        cache[k] = norm(subprocess.run(a, capture_output=True, text=True).stdout)
    return cache[k]
res = []
for l in lect.read_text(encoding="utf-8").splitlines():
    d = json.loads(l)
    if d.get("tipo") != "cita": continue
    ruta = urd if d["documento"] == "urd2025" else pdfdir / (d["documento"] + ".pdf")
    if not ruta.exists():
        res.append((d["documento"], d["pagina_pdf"], "SIN_PDF", d["cita"][:70])); continue
    h = hashlib.sha256(ruta.read_bytes()).hexdigest()
    c = norm(d["cita"])
    ok = any(c in pagina(ruta, d["pagina_pdf"], lay) for lay in (False, True))
    # tolerancia de maquetación: todas las palabras de la cita, en orden, en la página sin -layout
    orden = False
    if not ok:
        t = pagina(ruta, d["pagina_pdf"], False); pos = 0; orden = True
        for w in c.split(" "):
            i = t.find(w, pos)
            if i < 0: orden = False; break
            pos = i + len(w)
    est = "EN_PAGINA" if ok else ("EN_PAGINA_ORDEN_LECTURA" if orden else "NO_ENCONTRADA")
    res.append((d["documento"], d["pagina_pdf"], est + ("" if h == d.get("sha256_doc", h) else " HUELLA_DISTINTA"), d["cita"][:70]))
for r in res: print("\t".join(map(str, r)))
import collections; print(collections.Counter(r[2] for r in res))
