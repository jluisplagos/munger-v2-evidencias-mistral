"""Revisor: la huella de entradas (entradas_economicas.instantanea) de cada libro .xlsx de los expedientes, con el código anterior (ebf47fc) y el
actual (fbb146d). Uso: huellas_entradas_revisor.py DIR_SCRIPTS RAIZ_LIBROS SALIDA.json"""
import glob, json, os, sys
sys.path.insert(0, sys.argv[1])
import entradas_economicas as EE
res = {}
for p in sorted(glob.glob(os.path.join(sys.argv[2], "**", "*.xlsx"), recursive=True)):
    if "/pdf/" in p or os.path.basename(p).startswith("~$"):
        continue
    try:
        i = EE.instantanea(p)
        res[os.path.relpath(p, sys.argv[2])] = {"huella": i["huella"], "n": i["n"], "version": i.get("version")}
    except Exception as e:
        res[os.path.relpath(p, sys.argv[2])] = {"error": f"{type(e).__name__}: {e}"[:200]}
json.dump(res, open(sys.argv[3], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(res), "libros")
