"""Verifica contra el ZIP base-4.14 las huellas PDF de un CSV de fuentes conservadas.

Uso: python3 -I verificar_huellas.py <ruta_al_zip_base_4_14> <fuentes.csv>
El CSV debe tener cabecera con columnas ruta_en_base_4_14,bytes,sha256,es_pdf_candidato,...
(p. ej. FUENTES_CONSERVADAS.csv @ daa7478 de la rama mistral/m2-fundamento-pm1).
Comprueba bytes y SHA-256 de cada fila marcada como PDF candidato. Exit 0 si todas coinciden.
"""
import csv, hashlib, os, sys, zipfile

RAIZ = 'munger_v2_r1/'


def main(zip_path, fuentes_csv):
    zip_path = os.path.abspath(zip_path)
    ok = 0
    bad = []
    with open(fuentes_csv, newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    pdfs = [r for r in rows if r.get('es_pdf_candidato') == 'si']
    with zipfile.ZipFile(zip_path) as z:
        names = set(z.namelist())
        for r in pdfs:
            name = RAIZ + r['ruta_en_base_4_14']
            if name not in names:
                bad.append((r['ruta_en_base_4_14'], 'NO ESTA EN EL ZIP'))
                continue
            info = z.getinfo(name)
            h = hashlib.sha256()
            with z.open(name) as fh:
                for chunk in iter(lambda: fh.read(1 << 20), b''):
                    h.update(chunk)
            if info.file_size == int(r['bytes']) and h.hexdigest() == r['sha256']:
                ok += 1
            else:
                bad.append((r['ruta_en_base_4_14'],
                            f"bytes {info.file_size} vs {r['bytes']}, sha {h.hexdigest()[:12]} vs {r['sha256'][:12]}"))
    print(f'{fuentes_csv}: {ok}/{len(pdfs)} PDF coinciden en bytes y SHA-256 con {os.path.basename(zip_path)}')
    for ruta, why in bad:
        print(f'  FALLO {ruta}: {why}')
    print('RESULTADO:', 'TODO COINCIDE' if not bad else f'{len(bad)} FALLOS')
    sys.exit(0 if not bad else 1)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
