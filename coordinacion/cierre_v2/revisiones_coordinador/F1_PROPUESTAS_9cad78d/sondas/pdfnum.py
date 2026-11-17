"""Utilidad de las sondas del revisor: lee una cifra de una página de un PDF (pdftotext -layout) por rótulo y posición,
y comprueba la huella del PDF. Independiente del código del autor."""
import hashlib
import re
import subprocess
import unicodedata
from fractions import Fraction as Fr
from pathlib import Path

REV = Path(__file__).resolve().parent.parent          # carpeta de la revisión (contiene copia/, release/ y sondas/)
BASE = REV / "copia/munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/elis_decisiones/Elis/fuentes_pdf"
REL = REV / "release/pdf"
DOCS = {
    "URD2021": (BASE / "Elis_URD_2021_EN.pdf", "e2d316b38441a167ee96e413e0c63e39a66f824302d18d5b7c78cc8b8d060537"),
    "URD2022": (BASE / "Elis - 2022 Universal Registration Document.pdf", "98c0012c0ecf7d3cf6f172452764239515126ea1ca37cd7b84c4a9ef249911e3"),
    "URD2023": (BASE / "Elis_Universal Registration Document_2023_EN.pdf", "8aac7004177529bb20d9ca84ce05d747a15d238ffbdc5669e2add9569443bd31"),
    "DEU2024FR": (BASE / "Elis_Document d'enregistrement universel_2024_FR.pdf", "94e994f0de79cc588240f9866d263c4a5ae27fe3ccff83bc0b817eb91633c1e9"),
    "URD2025": (BASE / "Elis - 2025 Universal Registration Document.pdf", "04bfd08724e768804e7110093d3ec2cf017a7e7fe2983bacd75656d3a95cd62e"),
    "REL_FY2024_PRES": (REL / "fy2024_presentacion_en.pdf", "d733b56d6fd25e538d945da6434a0c90a4579fd291550558d2ff786cb2ec4e7d"),
    "REL_FY2025_PRES": (REL / "fy2025_presentacion_en.pdf", "b3642606567cb4d9082e007843670e1fab6d46fab4dd466badfda92648c06786"),
    "REL_H1_2025_COM": (REL / "h1_2025_comunicado_fr.pdf", "1347fc21135ebd6ad5705853f87e489ceee68e864c172b0e2aec4a1a702c9779"),
    "REL_H1_2026_COM": (REL / "h1_2026_comunicado_en.pdf", "5a84458c26fc5b060f5e45e631139436d3a65592e7b676cc29b68ecc44579cb4"),
}
_cache, _huella = {}, {}
NUM = re.compile(r"^\(?[+\-–−]?\d[\d.,  ]*\)?%?$|^[–\-−]$")


def pagina(doc, pag):
    if (doc, pag) not in _cache:
        ruta, sha = DOCS[doc]
        if doc not in _huella:
            _huella[doc] = hashlib.sha256(ruta.read_bytes()).hexdigest() == sha
            assert _huella[doc], f"huella distinta: {doc}"
        out = subprocess.run(["pdftotext", "-layout", "-f", str(pag), "-l", str(pag), str(ruta), "-"], capture_output=True, text=True, check=True).stdout
        _cache[(doc, pag)] = [unicodedata.normalize("NFKC", x).replace("’", "'") for x in out.splitlines()]
    return _cache[(doc, pag)]


def valor(lit, frances=False):
    if lit in ("-", "–", "−"):
        return Fr(0)
    x = lit.strip("()%").replace(" ", "").replace(" ", "")
    x = x.replace(",", ".") if frances else x.replace(",", "")
    return (-1 if lit.startswith("(") else 1) * Fr(x)


def lee(doc, pag, rotulo, pos, ocurrencia=0, desplazamiento=0, regex=False):
    """Celda numérica `pos` de la línea (rótulo + desplazamiento) de la ocurrencia pedida. Devuelve (valor, literal)."""
    ls = pagina(doc, pag)
    hall = []
    for i, ln in enumerate(ls):
        m = re.search(rotulo, ln) if regex else (re.search(re.escape(rotulo), ln))
        if not m:
            continue
        j = i + desplazamiento
        resto = ls[j][m.end():] if desplazamiento == 0 else ls[j]
        cel = [c for c in re.split(r"\s{2,}", resto.strip()) if NUM.match(c)]
        if cel:
            hall.append(cel)
    assert len(hall) > ocurrencia, f"no encontrado: {doc} p.{pag} «{rotulo}» (ocurrencia {ocurrencia})"
    lit = hall[ocurrencia][pos]
    return valor(lit, frances=doc.startswith("DEU") or doc == "REL_H1_2025_COM"), lit


def intervalo(v, decimales=1):
    """Intervalo de redondeo de una cifra impresa con `decimales` decimales."""
    e = Fr(5, 10 ** (decimales + 1))
    return (v - e, v + e)
