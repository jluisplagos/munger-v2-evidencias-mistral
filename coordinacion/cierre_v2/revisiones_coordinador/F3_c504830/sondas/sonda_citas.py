"""Extrae las citas de linea de los textos de F @ c504830 y vuelca las lineas reales del producto.

Uso: python3 -I sonda_citas.py <raiz_alcance_real> <munger_v2_r1_de_la_candidata>
Reconoce: B6:/build_v6.py:, TF:/test_fill.py:, REL:/relacion_entradas_materiales.py:,
P62:/patch_v62_base.py: seguidos de listas 'a-b,c,d-e'. Solo imprime; el juicio es del revisor.
"""
import os
import re
import sys

raiz, prod = sys.argv[1], sys.argv[2]
ARCH = {
    'B6': 'v6/scripts/V6.1/build_v6.py', 'build_v6.py': 'v6/scripts/V6.1/build_v6.py',
    'TF': 'v6/scripts/V6.1/test_fill.py', 'test_fill.py': 'v6/scripts/V6.1/test_fill.py',
    'REL': 'v6/scripts/relacion_entradas_materiales.py',
    'relacion_entradas_materiales.py': 'v6/scripts/relacion_entradas_materiales.py',
    'P62': 'v6/scripts/patch_v62_base.py', 'patch_v62_base.py': 'v6/scripts/patch_v62_base.py',
}
lineas = {k: open(os.path.join(prod, v), encoding='utf-8').read().split('\n') for k, v in ARCH.items()}
TEXTOS = ['preparacion_b3_c1/CONTRATO_C_PROPUESTA.md', 'preparacion_b3_c1/PROTOCOLO_CONGELADO.md',
          'preparacion_b3_c1/MAPA_ENTRADAS.jsonl', 'correccion_f3/RESPUESTA_F3.md',
          'correccion_f3/ENTREGA_F3.json', 'correccion_f2/RESPUESTA_F2.md',
          'correccion_f2/ENTREGA_F2.json', 'COMANDOS.md',
          'correccion_f2/scripts/verificar_contrato_c.py']
pat = re.compile(r'(B6|TF|REL|P62|build_v6\.py|test_fill\.py|relacion_entradas_materiales\.py|patch_v62_base\.py)'
                 r'(?: @ ?957af65)?:(\d+(?:-\d+)?(?:,\d+(?:-\d+)?)*)')
vistas = set()
for t in TEXTOS:
    p = os.path.join(raiz, t)
    for nl, linea in enumerate(open(p, encoding='utf-8'), 1):
        for m in pat.finditer(linea):
            arch, spec = m.group(1), m.group(2)
            for parte in spec.split(','):
                a, _, b = parte.partition('-')
                a, b = int(a), int(b or a)
                clave = (ARCH[arch], a, b)
                print(f'{t}:{nl}  cita {arch}:{parte}')
                if clave in vistas:
                    continue
                vistas.add(clave)
                for k in range(a, b + 1):
                    print(f'      {ARCH[arch].split("/")[-1]}:{k}: {lineas[arch][k-1].strip()[:150]}')
