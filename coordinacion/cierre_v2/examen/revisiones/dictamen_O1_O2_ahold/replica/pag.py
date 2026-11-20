import re, sys
t = open(sys.argv[1], encoding='utf-8', errors='replace').read()
P = {int(m.group(1)): m.group(2) for m in re.finditer(r"\[PDF PAGE (\d+)\]\n(.*?)(?=\[PDF PAGE \d+\]|\Z)", t, re.S)}
for p in sys.argv[2:]:
    print(f'=========== PDF PAGE {p}')
    print(P[int(p)])
