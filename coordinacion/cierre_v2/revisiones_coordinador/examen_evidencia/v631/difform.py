import openpyxl, sys
a = openpyxl.load_workbook(sys.argv[1]); b = openpyxl.load_workbook(sys.argv[2])
print("hojas", a.sheetnames == b.sheetnames)
for ws in a.sheetnames:
    A, B = a[ws], b[ws]
    cells = set()
    for W in (A, B):
        for row in W.iter_rows():
            for c in row:
                if c.value is not None: cells.add(c.coordinate)
    for co in sorted(cells, key=lambda x:(openpyxl.utils.cell.coordinate_from_string(x)[1], x)):
        va, vb = A[co].value, B[co].value
        if va != vb:
            print(f"{ws}!{co}\n  V63 : {str(va)[:600]}\n  V631: {str(vb)[:1500]}")
