"""s02 · Comprueba los 32 extractos de extractos/ (E-ELIS @ f00c5dd) contra su PDF local.
Por extracto: huella sha256 y bytes de cabecera = PDF local; pagina dentro del rango; cada ventana
  (a) es subcadena exacta del texto PyMuPDF de esa pagina (mismo extractor que el autor);
  (b) todas sus palabras interiores (>=3 letras; se descartan la primera y la ultima, que la ventana
      puede cortar) estan en el texto pdftotext de esa pagina (extractor independiente; se comparan solo letras,
      para tolerar guiones y cortes de linea);
  El marcador '[PDF PAGE n]' que el autor antepone a cada pagina se retira antes de comparar.
  (c) contiene la cita registrada (normalizando blancos); longitud acotada (<= 800 + coincidencia).
Uso: python3 -I s02_extractos.py <dir_entrega_elis_fuentes> <dir_pdf_11> <urd2025.pdf>   (python con PyMuPDF)
"""
import hashlib, json, re, subprocess, sys, unicodedata
from pathlib import Path
import fitz
ent, pdfdir, urd = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
def ruta(fid): return urd if fid == "urd2025" else pdfdir / f"{fid}.pdf"
def nb(s): return re.sub(r"\s+", " ", s).strip()
def palabras(s, interiores=False):
    s = unicodedata.normalize("NFKC", s).lower()
    if interiores:
        toks = s.split()[1:-1]; s = " ".join(toks)
    return set(re.findall(r"[a-zà-ÿ]{3,}", s))
def pdft(r, p):
    return subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), str(r), "-"], capture_output=True, text=True).stdout
citas = {}
for l in (ent / "LECTURA_FUENTES.jsonl").read_text(encoding="utf-8").splitlines():
    d = json.loads(l)
    if d["tipo"] == "cita": citas.setdefault((d["documento"], d["pagina_pdf"]), []).append(d)
docs, hs, out, malos = {}, {}, [], 0
for f in sorted((ent / "extractos").glob("*.txt")):
    t = f.read_text(encoding="utf-8")
    m = re.search(r"# documento=(\S+) .*\n# pagina_pdf=(\d+) sha256_pdf=([0-9a-f]{64}) bytes_pdf=(\d+)", t)
    fid, p, sha, nbytes = m.group(1), int(m.group(2)), m.group(3), int(m.group(4))
    r = ruta(fid)
    if r not in hs: hs[r] = hashlib.sha256(r.read_bytes()).hexdigest()
    if r not in docs: docs[r] = fitz.open(str(r))
    doc = docs[r]
    huella = hs[r] == sha and r.stat().st_size == nbytes
    pag_fitz = doc[p - 1].get_text()
    ventanas = re.findall(r"---- ventana acotada \(400 caracteres a cada lado\) ----\n(.*?)(?=\n## cita |\Z)", t, re.S)
    ventanas = [re.sub(r"^\[PDF PAGE \d+\]\n", "", v) for v in ventanas]
    a_ok = all(v.rstrip("\n") in pag_fitz for v in ventanas)
    # tolerancia de maquetacion: la palabra puede aparecer partida o unida (guiones, cortes de linea)
    pt = re.sub(r"[^a-zà-ÿ]", "", unicodedata.normalize("NFKC", pdft(r, p)).lower()); faltan = set()
    for v in ventanas:
        faltan |= {w for w in palabras(v, True) if w not in pt}
    b_ok = not faltan
    cs = citas.get((fid, p), [])
    c_ok = all(any(nb(c["cita"]) in nb(v) for v in ventanas) for c in cs) and len(ventanas) == len(cs)
    largo = max(len(v) for v in ventanas)
    ok = huella and a_ok and b_ok and c_ok and largo <= 1200
    malos += not ok
    out.append(dict(extracto=f.name, doc=fid, p=p, huella_ok=huella, ventanas=len(ventanas), citas=len(cs),
                    subcadena_pymupdf=a_ok, palabras_en_pdftotext=b_ok, faltan=sorted(faltan)[:8], contiene_citas=c_ok, max_len_ventana=largo, ok=ok))
for o in out: print("\t".join(str(o[k]) for k in o))
print(f"TOTAL {len(out)} extractos; OK {len(out)-malos}; con defecto {malos}")
json.dump(out, open(Path(__file__).with_suffix(".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
