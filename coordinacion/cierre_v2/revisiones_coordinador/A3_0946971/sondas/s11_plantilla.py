"""Revisor A3: ENTREGA.json de 0946971 frente a coordinacion/cierre_v2/PLANTILLA_ENTREGA.json.
Uso: python3 -I -B s11_plantilla.py PLANTILLA.json ENTREGA.json"""
import json, sys
p, e = (json.load(open(x, encoding='utf-8')) for x in sys.argv[1:3])
print('faltan:', sorted(set(p) - set(e)))
print('sobran:', sorted(set(e) - set(p)))
pp = (p.get('pruebas') or [{}])[0]
for i, x in enumerate(e.get('pruebas', [])):
    print(f'prueba {i}: faltan', sorted(set(pp) - set(x)), 'sobran', sorted(set(x) - set(pp)))
for k in ('es_plantilla', 'commit_entrega', 'base_revisada_sha', 'revision_por_otro_contexto', 'apto_dinero_real', 'integrado_en_producto', 'naturaleza'):
    print(f'{k}: plantilla={json.dumps(p.get(k), ensure_ascii=False)[:110]} | entrega={json.dumps(e.get(k), ensure_ascii=False)[:150]}')
