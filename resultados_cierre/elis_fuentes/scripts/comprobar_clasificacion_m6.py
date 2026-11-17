"""E2-D1: prueba de cierre de la clasificacion por sociedad de las adquisiciones (URD 2025, base-4.14).

Lee el URD 2025 de .trabajo/elis_fuentes/pdf/urd2025.pdf (sha256 04bfd087..., base-4.14) con
PyMuPDF y Decimal, y comprueba:
1. p.306: la lista de 'major acquisitions' de 2025 contiene a Acquaflash y NO a Lavartex.
2. p.341: las seis importantes de 2025 tienen columna propia y su fila NET CASH FLOW suma
   8,9+13,2+10,2+7,0+11,8+9,7 = 60,8; Lavartex tiene '-' en desembolsos y (19,7) en earnouts;
   'Other acquisitions' (37,3) incluye (3,6) de earnouts; la suma de columnas 117,8 frente al
   total impreso (117,6) -> diferencia de redondeo 0,2.
3. p.341 (ejercicio anterior) y p.342: Carsan (9,7 M EUR de ingresos 2024) y Ernst
   (19,0 M EUR) son adquisiciones importantes de 2024 con columna propia en la tabla de 2024.

Exit 0 si todo se cumple, exit 1 si falla alguna comprobacion, exit 3 si falta PyMuPDF.
"""
import hashlib
import re
import sys
from decimal import Decimal
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
TRABAJO = RAIZ / ".trabajo/elis_fuentes"
SHA_URD2025 = "04bfd08724e768804e7110093d3ec2cf017a7e7fe2983bacd75656d3a95cd62e"


def main():
    try:
        import fitz
    except ImportError:
        print("DEPENDENCIA AUSENTE: PyMuPDF (fitz). pip install -r scripts/requirements.txt")
        sys.exit(3)
    ruta = TRABAJO / "pdf" / "urd2025.pdf"
    sha = hashlib.sha256(ruta.read_bytes()).hexdigest()
    assert sha == SHA_URD2025, f"urd2025 sha256 {sha[:16]} != base-4.14"
    doc = fitz.open(str(ruta))

    def pag(n):
        return re.sub(r"\s+", " ", doc[n - 1].get_text())

    p306 = pag(306)
    assert "Acquaflash in Brazil" in p306.replace("\ufb02", "fl"), "p.306: falta Acquaflash"
    assert "Lavartex" not in p306, "p.306: Lavartex no debe estar en la lista de importantes 2025"
    for nombre in ["Wäscherei Bodensee", "Bugadería Neutral", "Larosé", "JP Muller", "Adrett"]:
        assert nombre.replace("ä", "ä") in p306.replace("\ufb02", "fl") or nombre in p306, f"p.306: falta {nombre}"
    print("p.306 OK: seis importantes 2025 = Bodensee, Bugadería Neutral, Larosé, Acquaflash, JP Muller, Adrett; sin Lavartex")

    p341 = pag(341)
    m = re.search(r"NET CASH FLOW \(117\.6\) \(8\.9\) \(13\.2\) \(10\.2\) \(7\.0\) \(11\.8\) \(9\.7\) \(19\.7\) \(37\.3\)", p341)
    assert m, "p.341: fila NET CASH FLOW no encontrada"
    vals = [Decimal(v) for v in ["8.9", "13.2", "10.2", "7.0", "11.8", "9.7"]]
    seis = sum(vals)
    assert seis == Decimal("60.8"), f"suma seis importantes {seis} != 60,8"
    total_cols = seis + Decimal("19.7") + Decimal("37.3")
    assert total_cols == Decimal("117.8"), f"suma columnas {total_cols} != 117,8"
    assert (total_cols - Decimal("117.6")) == Decimal("0.2"), "redondeo esperado 0,2"
    m_out = re.search(r"Cash outflows for the acquisition \(112\.6\) \(9\.3\) \(16\.6\) \(13\.2\) \(7\.1\) \(15\.1\) \(12\.7\) - \(38\.5\)", p341.replace("\ufb02", "fl"))
    assert m_out, "p.341: fila Cash outflows (Lavartex '-') no encontrada"
    m_earn = re.search(r"Earnouts and deferred consideration \(23\.3\) 0\.0 0\.0 0\.0 0\.0 0\.0 0\.0 \(19\.7\) \(3\.6\)", p341)
    assert m_earn, "p.341: fila Earnouts (19,7 Lavartex / 3,6 Other) no encontrada"
    print(f"p.341 OK: seis importantes suman {seis} (60,8); Lavartex solo earnout (19,7) y '-' en desembolsos; Other (37,3) con (3,6) earnouts; columnas 117,8 vs impreso 117,6 (redondeo 0,2)")

    assert "Acquisitions during the previous financial year" in p341
    assert re.search(r"acquisition of 100%\s*of Carsan Renting", p341), "p.341: falta adquisicion Carsan (2024)"
    assert re.search(r"Carsan, which had €9\.7 million in revenue in 2024", p341), "p.341: falta ingreso Carsan 9,7"
    assert re.search(r"acquisition of 100%\s*of Wäscherei Ernst GmbH", p341.replace("\ufb02", "fl")), "p.341: falta adquisicion Ernst (2024)"
    assert re.search(r"Ernst, which had €19\.0 million in revenue in 2024", p341), "p.341: falta ingreso Ernst 19,0"
    p342 = pag(342)
    assert re.search(r"Moderna Wasned Wonway Carsan Ernst Other acquisitions", p342), "p.342: faltan columnas Carsan/Ernst en tabla 2024"
    print("p.341/p.342 OK: Carsan (9,7 M EUR) y Ernst (19,0 M EUR) son importantes de 2024 con columna propia en la tabla de 2024")

    print("E2-D1 CUMPLE: clasificacion por sociedad con pagina verificada con Decimal sobre URD 2025 (base-4.14)")
    sys.exit(0)


if __name__ == "__main__":
    main()
