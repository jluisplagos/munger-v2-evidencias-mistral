import ast, subprocess, re, sys
import os; C=os.environ['CAND']
def show(rev,p): return subprocess.run(['git','-C',C,'show',f'{rev}:{p}'],capture_output=True).stdout.decode('utf-8')
files=subprocess.run(['git','-C',C,'ls-tree','-r','--name-only','3149128'],capture_output=True,text=True).stdout.split('\n')
pat=re.compile(r'^munger_v2_r1/(personaje_v2/empresas_v2_correcciones/[^/]+/scripts/|personaje_v2/pruebas/|contrastes/[^/]+/scripts/).*\.py$')
sel=[f for f in files if pat.match(f)]
lits=set()
for f in sel:
    try: t=ast.parse(show('3149128',f))
    except Exception as e: print('no parse',f,e); continue
    for n in ast.walk(t):
        if isinstance(n,ast.Constant) and isinstance(n.value,str) and n.value: lits.add(n.value)
old=show('3149128','munger_v2_r1/CONTINUIDAD.md'); o957=show('957af65','munger_v2_r1/CONTINUIDAD.md')
s1a="Si falta espacio, terminada la verificación se pueden borrar los `*.xlsx` y `vigencia/` de `personaje_v2/pruebas/_v64/` (los controles no recorren `_v64/`), registrando las rutas (regla 11.10)."
s1b="Si falta espacio, terminada la verificación se pueden borrar los `*.xlsx` y `vigencia/` de `personaje_v2/pruebas/_v64/`, registrando las rutas (regla 11.10). Hay que hacerlo antes del control de la 4.8.1: ese control copia `personaje_v2/` con `pruebas/_v64/` en temporales de `/tmp` (`comprobar_entrega_4_8_1.py`, función `arbol`), aunque no evalúa su contenido."
s2a="Conviene tener al menos 7 GB libres después de descomprimir."
s2b="Conviene tener al menos 7 GB libres después de descomprimir. En la prueba de traspaso de la 4.15 (vía del repositorio, 17-nov-2026), unos 8,4 GB libres al empezar los controles no bastaron para el de la 4.8.1; tras la limpieza que sigue, con unos 13 GB, terminó con el mismo resultado que en el árbol 4.14 (25 de 30)."
s2c="Conviene tener al menos 7 GB libres después de descomprimir. En la prueba de traspaso de la 4.15 (vía del repositorio) esa cantidad no bastó para el control de la 4.8.1, que terminó después de la limpieza que sigue."
print('scripts analizados',len(sel),'literales',len(lits))
print('frase1 actual aparece exactamente', old.count(s1a),'vez/veces')
print('frase2 actual aparece exactamente', old.count(s2a),'vez/veces')
new=old.replace(s1a,s1b,1).replace(s2a,s2b,1); new2=old.replace(s1a,s1b,1).replace(s2a,s2c,1)
for nombre,nv in (('cambios 1+2',new),('cambio 1 + variante 2',new2)):
    d=[l for l in lits if (l in old)!=(l in nv)]
    print(nombre,': literales que aparecen o desaparecen =',len(d), d[:10])
d=[l for l in lits if (l in o957)!=(l in old)]
print('957af65 -> 3149128 (CONTINUIDAD): literales que aparecen o desaparecen =',len(d), d[:10])
# literales que aparecen en CONTINUIDAD (dependencias reales)
print('literales presentes en CONTINUIDAD 3149128:',sum(1 for l in lits if l in old and len(l)>3))
