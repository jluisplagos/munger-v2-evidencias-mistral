import sys, re, openpyxl
path, pat = sys.argv[1], sys.argv[2]
sheets = sys.argv[3].split(',') if len(sys.argv) > 3 else None
wf = openpyxl.load_workbook(path, data_only=False)
wv = openpyxl.load_workbook(path, data_only=True)
rx = re.compile(pat, re.I)
for ws in wf.worksheets:
    if sheets and ws.title not in sheets:
        continue
    sv = wv[ws.title]
    for row in ws.iter_rows():
        for c in row:
            if c.value is None:
                continue
            s = str(c.value)
            if rx.search(s):
                v = sv[c.coordinate].value
                if s.startswith('='):
                    print(f'{ws.title}!{c.coordinate}: F[{s[:1200]}] => {str(v)[:300]!r}')
                else:
                    print(f'{ws.title}!{c.coordinate}: {s[:1200]!r}')
