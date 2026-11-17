"""Sonda s07: tercer extractor independiente (poppler pdftotext; primero sin -layout, después con -layout para filas de tabla) sobre las 68 citas de ea641e7.
Uso: python3 -I s07_citas_pdftotext.py <LECTURA_FUENTES.jsonl> <dir_pdf con <id>.pdf>
Para cada cita: sha256 del PDF == sha256_doc; el patron (espacios -> \\s+) casa en su pagina_pdf.
Normaliza ligaduras fi/fl, NBSP, thin space y guion no separable; colapsa blancos.
Si no casa, informa también si casa quitando el espacio delante de puntuación (artefacto de extractor)."""
import hashlib, json, re, subprocess, sys
from pathlib import Path
LIG = {"ﬁ": "fi", "ﬂ": "fl", "\xa0": " ", "‑": "-", " ": " ", " ": " "}
def norm(s):
    for k, v in LIG.items():
        s = s.replace(k, v)
    return re.sub(r"\s+", " ", s)
lect, d = Path(sys.argv[1]), Path(sys.argv[2])
recs = [json.loads(l) for l in lect.read_text(encoding="utf-8").splitlines()]
citas = [r for r in recs if r["tipo"] == "cita"]
cache, sha = {}, {}
ok = fallos = 0
for i, c in enumerate(citas, 1):
    fid, p = c["documento"], c["pagina_pdf"]
    pdf = d / f"{fid}.pdf"
    if fid not in sha:
        sha[fid] = hashlib.sha256(pdf.read_bytes()).hexdigest()
    if (fid, p) not in cache:
        t = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), str(pdf), "-"], capture_output=True, text=True).stdout
        cache[(fid, p)] = norm(t)
    txt = cache[(fid, p)]
    if (fid, p, "L") not in cache:
        t = subprocess.run(["pdftotext", "-layout", "-f", str(p), "-l", str(p), str(pdf), "-"], capture_output=True, text=True).stdout
        cache[(fid, p, "L")] = norm(t)
    txtL = cache[(fid, p, "L")]
    pat = c["patron"].replace(" ", r"\s+")
    m = re.search(pat, txt, re.IGNORECASE)
    m2 = m or re.search(pat, re.sub(r" ([,.;:)%])", r"\1", re.sub(r" -(\w)", r"-\1", txt)), re.IGNORECASE)
    mL = None if (m or m2) else re.search(pat, txtL, re.IGNORECASE)
    h = sha[fid] == c["sha256_doc"]
    est = "OK" if (m and h) else ("OK_TRAS_NORMALIZAR_ESPACIOS" if (m2 and h) else ("OK_MODO_LAYOUT" if (mL and h) else "FALLO"))
    ok += est != "FALLO"; fallos += est == "FALLO"
    print(f"{i:02d} {c['pregunta']} {fid} p{p} huella={'ok' if h else 'MAL'} {est} :: {c['patron'][:70]}")
print(f"TOTAL {len(citas)} | casan {ok} | fallan {fallos}")
sys.exit(1 if fallos else 0)
