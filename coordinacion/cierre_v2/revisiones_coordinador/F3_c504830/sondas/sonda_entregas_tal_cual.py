"""Ejecuta TAL CUAL (byte a byte) cada 'comando' de las ENTREGA del arbol revisado.

Uso (dentro de un espacio de montaje con /tmp redirigido a una carpeta de la revision):
  unshare -m bash -c 'mount --bind <rev_F3>/sondas/tmp_ns1 /tmp && \
      python3 -I sonda_entregas_tal_cual.py <raiz_worktree> <zip_414> <salida_dir>'

Cada comando se pasa sin modificar a 'bash -c' con cwd = raiz del worktree y ZIP_414 definido.
Las pruebas con resultado NO_EJECUTADO no se ejecutan.
"""
import hashlib
import json
import os
import subprocess
import sys

raiz, zip414, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
base = os.path.join(raiz, 'resultados_cierre/alcance_real')
entregas = ['correccion_f3/ENTREGA_F3.json', 'correccion_f2/ENTREGA_F2.json',
            'preparacion_b3_c1/ENTREGA_B3_C1.json', 'revisiones_b_pm1/ENTREGA_B_PM1.json']
env = dict(os.environ, ZIP_414=zip414)
resumen = []
for e in entregas:
    d = json.load(open(os.path.join(base, e), encoding='utf-8'))
    for i, p in enumerate(d['pruebas']):
        cmd = p['comando']
        if p['resultado'] == 'NO_EJECUTADO':
            resumen.append(f'{e} prueba {i}: NO_EJECUTADO declarado; no se ejecuta')
            continue
        r = subprocess.run(['bash', '-c', cmd], cwd=raiz, env=env,
                           capture_output=True, text=True, timeout=1800)
        tag = f"{e.replace('/', '_')}_p{i}"
        with open(os.path.join(out, tag + '.txt'), 'w', encoding='utf-8') as f:
            f.write(f'COMANDO (sha256 {hashlib.sha256(cmd.encode()).hexdigest()}):\n{cmd}\n\n')
            f.write(f'EXIT: {r.returncode}\n--- STDOUT ---\n{r.stdout}\n--- STDERR ---\n{r.stderr}\n')
        resumen.append(f'{e} prueba {i}: exit observado {r.returncode} '
                       f'(declarado {p["exit_observado"]})')
print('\n'.join(resumen))
