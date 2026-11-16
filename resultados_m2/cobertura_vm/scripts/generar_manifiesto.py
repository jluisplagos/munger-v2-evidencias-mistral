"""Genera MANIFIESTO_SHA256.txt con la huella de cada archivo del frente."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun as C


def main():
    lineas = []
    for p in sorted(C.OUT.rglob('*')):
        if p.is_file() and p.name != 'MANIFIESTO_SHA256.txt' and '__pycache__' not in p.parts:
            rel = p.relative_to(C.OUT).as_posix()
            lineas.append(f'{C.sha256_file(p)}  {rel}')
    (C.OUT / 'MANIFIESTO_SHA256.txt').write_text('\n'.join(lineas) + '\n', encoding='utf-8')
    print(f'{len(lineas)} archivos con huella en MANIFIESTO_SHA256.txt')


if __name__ == '__main__':
    main()
