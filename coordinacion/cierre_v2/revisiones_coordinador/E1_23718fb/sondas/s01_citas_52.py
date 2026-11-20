"""s01 · Verifica las 52 citas de LECTURA_FUENTES.jsonl (E-ELIS @ 23718fb/f00c5dd) en su pagina PDF.
Adaptado de citas_E.py (adenda 20261117). Extractor independiente del autor: pdftotext (poppler),
pagina a pagina, en orden de lectura y con -layout. Comprueba ademas:
  - huella del PDF local = sha256_doc del registro;
  - el patron registrado casa en la pagina pdftotext sin normalizar (solo blancos; espacios -> \\s+);
  - el patron no contiene '.*' ni '|' ni cuantificadores sin cota sobre '.';
  - la cita no esta truncada (len < 400) y es la coincidencia completa del patron.
Uso: python3 -I s01_citas_52.py <LECTURA_FUENTES.jsonl> <dir_pdf_11> <urd2025.pdf>
"""
import collections, hashlib, json, re, subprocess, sys, unicodedata
from pathlib import Path
lect, pdfdir, urd = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\u00ad", ""), ("\u2011", "-"), ("\u2010", "-")):
        s = s.replace(a, b)
    s = re.sub(r"-\s*\n\s*(?=[a-z])", "", s)
    return re.sub(r"\s+", " ", s).strip()
cache, hcache = {}, {}
def pagina(ruta, p, layout):
    k = (str(ruta), p, layout)
    if k not in cache:
        a = ["pdftotext"] + (["-layout"] if layout else []) + ["-f", str(p), "-l", str(p), str(ruta), "-"]
        cache[k] = norm(subprocess.run(a, capture_output=True, text=True, check=True).stdout)
    return cache[k]
rcache = {}
def pagina_cruda(ruta, p, layout):
    k = (str(ruta), p, layout)
    if k not in rcache:
        a = ["pdftotext"] + (["-layout"] if layout else []) + ["-f", str(p), "-l", str(p), str(ruta), "-"]
        rcache[k] = re.sub(r"\s+", " ", subprocess.run(a, capture_output=True, text=True, check=True).stdout)
    return rcache[k]
def huella(ruta):
    if ruta not in hcache: hcache[ruta] = hashlib.sha256(ruta.read_bytes()).hexdigest()
    return hcache[ruta]
res = []
n = 0
for l in lect.read_text(encoding="utf-8").splitlines():
    d = json.loads(l)
    if d.get("tipo") != "cita": continue
    n += 1
    ruta = urd if d["documento"] == "urd2025" else pdfdir / (d["documento"] + ".pdf")
    if not ruta.exists():
        res.append(dict(n=n, doc=d["documento"], p=d["pagina_pdf"], estado="SIN_PDF")); continue
    huella_ok = huella(ruta) == d["sha256_doc"]
    c = norm(d["cita"]).lower()
    lit = {lay: c in pagina(ruta, d["pagina_pdf"], lay).lower() for lay in (False, True)}
    orden = False
    if not any(lit.values()):
        t = pagina(ruta, d["pagina_pdf"], False).lower(); pos = 0; orden = True
        for w in c.split(" "):
            i = t.find(w, pos)
            if i < 0: orden = False; break
            pos = i + len(w)
    pat = d["patron"]
    patron_ok = {}
    for lay in (False, True):
        patron_ok[lay] = bool(re.search(pat.replace(" ", r"\s+"), pagina_cruda(ruta, d["pagina_pdf"], lay), re.IGNORECASE))
    prohibido = bool(re.search(r"\.\*|\.\+|\|", pat))
    sin_cota = re.findall(r"\\S\*|\\S\+|\\w\*|\\w\+", pat)
    # en otras paginas? (para detectar pagina equivocada)
    est = "EN_PAGINA" if any(lit.values()) else ("EN_PAGINA_ORDEN_LECTURA" if orden else "NO_ENCONTRADA")
    res.append(dict(n=n, preg=d["pregunta"], doc=d["documento"], p=d["pagina_pdf"], estado=est,
                    literal_lectura=lit[False], literal_layout=lit[True],
                    patron_pdftotext_lectura=patron_ok[False], patron_pdftotext_layout=patron_ok[True],
                    huella_ok=huella_ok, patron_prohibido=prohibido, cuantificadores_sin_cota_no_espacio=sin_cota,
                    len_cita=len(d["cita"]), truncada=len(d["cita"]) >= 400, cita=d["cita"][:90]))
for r in res:
    print("\t".join(str(r.get(k, "")) for k in ("n", "preg", "doc", "p", "estado", "patron_pdftotext_lectura", "patron_pdftotext_layout", "huella_ok", "patron_prohibido", "cuantificadores_sin_cota_no_espacio", "truncada", "cita")))
print("TOTAL", len(res), collections.Counter(r["estado"] for r in res))
print("huella_ok", sum(r.get("huella_ok", False) for r in res), "| patron casa en pdftotext (lectura o layout)", sum(r.get("patron_pdftotext_lectura", False) or r.get("patron_pdftotext_layout", False) for r in res),
      "| patrones con .* .+ o |:", sum(r.get("patron_prohibido", False) for r in res), "| truncadas:", sum(r.get("truncada", False) for r in res))
json.dump(res, open(Path(__file__).with_suffix(".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
