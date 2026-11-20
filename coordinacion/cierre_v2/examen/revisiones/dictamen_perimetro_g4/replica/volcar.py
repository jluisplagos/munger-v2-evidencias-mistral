"""Vuelca celdas (fórmula y valor en caché) de un libro. Solo lectura. Uso: volcar.py LIBRO HOJA FILA0 FILA1 [COLUMNAS]"""
import sys, openpyxl
path, sheet, r0, r1 = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
cols = sys.argv[5] if len(sys.argv) > 5 else 'ABCDEFGHIJKLM'
wf = openpyxl.load_workbook(path, data_only=False, read_only=False)
wv = openpyxl.load_workbook(path, data_only=True, read_only=False)
sf, sv = wf[sheet], wv[sheet]
for r in range(r0, r1 + 1):
    for c in cols:
        f = sf[f'{c}{r}'].value
        v = sv[f'{c}{r}'].value
        if f is None and v is None:
            continue
        fs = str(f)
        if fs.startswith('='):
            print(f'{sheet}!{c}{r}: F[{fs[:600]}] => {v!r}')
        else:
            print(f'{sheet}!{c}{r}: {str(v)[:600]!r}')
