"""Estimación de páginas de un Markdown sencillo (títulos, párrafos, listas y tablas) en A4, márgenes de 2 cm, cuerpo de 10 pt."""
import re, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

src, out = sys.argv[1], sys.argv[2]
cuerpo = float(sys.argv[3]) if len(sys.argv) > 3 else 10.0
margen = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
base = ParagraphStyle("b", fontName="Helvetica", fontSize=cuerpo, leading=cuerpo * 1.25, spaceAfter=4)
h1 = ParagraphStyle("h1", parent=base, fontName="Helvetica-Bold", fontSize=cuerpo + 4, leading=(cuerpo + 4) * 1.2, spaceAfter=6)
h2 = ParagraphStyle("h2", parent=base, fontName="Helvetica-Bold", fontSize=cuerpo + 2, leading=(cuerpo + 2) * 1.2, spaceBefore=6, spaceAfter=4)
li = ParagraphStyle("li", parent=base, leftIndent=12, bulletIndent=2, spaceAfter=2)
celda = ParagraphStyle("c", parent=base, fontSize=cuerpo - 1, leading=(cuerpo - 1) * 1.2, spaceAfter=0)

def fmt(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"`(.+?)`", r"<font face='Courier'>\1</font>", t)
    return t

flow, lines, i = [], open(src, encoding="utf-8").read().split("\n"), 0
ancho = A4[0] - 2 * margen * cm
while i < len(lines):
    l = lines[i]
    if l.startswith("# "):
        flow.append(Paragraph(fmt(l[2:]), h1))
    elif l.startswith("## "):
        flow.append(Paragraph(fmt(l[3:]), h2))
    elif l.startswith("|"):
        filas = []
        while i < len(lines) and lines[i].startswith("|"):
            c = [x.strip() for x in lines[i].strip().strip("|").split("|")]
            if not all(re.fullmatch(r":?-+:?", x) for x in c):
                filas.append([Paragraph(fmt(x), celda) for x in c])
            i += 1
        n = len(filas[0])
        # anchos proporcionales a la longitud máxima del texto de cada columna (acotados)
        lens = [max(len(re.sub(r"<[^>]+>", "", f[k].text)) for f in filas) for k in range(n)]
        lens = [min(max(x, 8), 120) for x in lens]
        tot = sum(lens)
        t = Table(filas, colWidths=[ancho * x / tot for x in lens])
        t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, colors.grey), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                               ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                               ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
        flow += [t, Spacer(1, 5)]
        continue
    elif re.match(r"^(- |\d+\. )", l):
        m = re.match(r"^(- |\d+\. )(.*)", l)
        flow.append(Paragraph(fmt(m.group(2)), li, bulletText="•" if m.group(1) == "- " else m.group(1).strip()))
    elif l.strip():
        flow.append(Paragraph(fmt(l), base))
    i += 1
doc = SimpleDocTemplate(out, pagesize=A4, leftMargin=margen * cm, rightMargin=margen * cm, topMargin=margen * cm, bottomMargin=margen * cm)
doc.build(flow)
from reportlab.pdfgen import canvas  # noqa
import subprocess
print(subprocess.run(["pdfinfo", out], capture_output=True, text=True).stdout.split("Pages:")[1].split()[0], "páginas", f"(cuerpo {cuerpo} pt, márgenes {margen} cm)")
