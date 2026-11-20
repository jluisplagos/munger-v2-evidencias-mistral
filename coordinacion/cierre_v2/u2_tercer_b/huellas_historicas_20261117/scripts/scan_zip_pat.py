import sys, zipfile, io
z = zipfile.ZipFile(sys.argv[1]); pats=[l.strip().lower().encode() for l in open(sys.argv[2]) if l.strip()]
for info in z.infolist():
    if info.is_dir(): continue
    d=z.read(info); bl=[(info.filename,d)]
    if d[:2]==b'PK':
        try:
            iz=zipfile.ZipFile(io.BytesIO(d)); bl+= [(info.filename+'!'+i.filename, iz.read(i)) for i in iz.infolist() if not i.is_dir()]
        except Exception: pass
    for n,b in bl:
        lb=b.lower()
        for p in pats:
            if p in lb:
                for k,line in enumerate(lb.split(b'\n'),1):
                    if p in line: print(f'{n}:{k}:{p.decode()}:{line[:300].decode("utf-8","replace")}')
