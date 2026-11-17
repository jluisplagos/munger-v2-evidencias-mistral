import sys, zipfile, re, io
zp = sys.argv[1]
pat = re.compile(rb'ahold|delhaize|koninklijke', re.I)
z = zipfile.ZipFile(zp)
nent = 0; nhit = 0; nested = 0
for info in z.infolist():
    if info.is_dir(): continue
    nent += 1
    data = z.read(info)
    blobs = [(info.filename, data)]
    # nested office/zip containers
    if data[:2] == b'PK':
        try:
            iz = zipfile.ZipFile(io.BytesIO(data))
            for ii in iz.infolist():
                if ii.is_dir(): continue
                blobs.append((info.filename + '!' + ii.filename, iz.read(ii)))
            nested += 1
        except Exception:
            pass
    for name, b in blobs:
        if pat.search(b):
            nhit += 1
            if name.lower().endswith(('.pdf','.png','.jpg','.jpeg')):
                print('BIN\t' + name)
                continue
            try:
                txt = b.decode('utf-8')
            except UnicodeDecodeError:
                txt = b.decode('latin-1')
            for i, line in enumerate(txt.splitlines(), 1):
                if re.search(r'ahold|delhaize|koninklijke', line, re.I):
                    print(f'{name}:{i}:{line[:400]}')
print(f'#entradas={nent} contenedores_anidados={nested} blobs_con_coincidencia={nhit}', file=sys.stderr)
