import sys, os, json
sys.dont_write_bytecode = True
sys.path.insert(0, sys.argv[1])
import motor_a_f1 as M
raiz = sys.argv[2]
out = {}
for r, ds, fs in os.walk(raiz):
    ds[:] = [d for d in ds if d not in ("__pycache__", ".lo_perfil", "antecedentes", "pdf", "texto", "recalc", "fase1_partes", "prompts_generados")]
    if "estado_pipeline.json" in fs:
        try:
            v = M.vigencia(r)
            out[os.path.relpath(r, raiz)] = {k: v.get(k) for k in ("motor", "exigido", "vigente", "utilizable", "motivo", "exento")}
        except Exception as ex:
            out[os.path.relpath(r, raiz)] = {"excepcion": f"{type(ex).__name__}: {ex}"}
json.dump(out, open(sys.argv[3], "w"), ensure_ascii=False, indent=0, sort_keys=True)
print(len(out), "expedientes")
