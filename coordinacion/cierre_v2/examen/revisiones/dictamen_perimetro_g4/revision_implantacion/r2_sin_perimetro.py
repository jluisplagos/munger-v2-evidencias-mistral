"""Revisión de la implantación de P-FOSO · R2: «sin perímetro nada cambia». Para cada expediente con libro recalculado, ejecuta los scripts
ANTERIORES (ab40e80) y los NUEVOS (688df46) sobre dos copias iguales y compara las salidas byte a byte:
  volcar_datos_v63.py --referencias-mecanicas → datos_v63.md, datos_v63.json, referencias_mecanicas.json
  comprobar_gramatica.py --antes-de-recalculo / --tras-recalculo → gramatica.json, gramatica.md (si hay fase_b.json / resultados.json)
  motor_a_f1.py evaluar → motor_a_f1_resultado.json, .md (si hay motor_a_f1.json)
Nada se escribe en los repositorios: las copias van a una carpeta temporal.
Uso: r2_sin_perimetro.py PV_NUEVO PV_ANTERIOR RAIZ_EXPEDIENTES CARPETA_TRABAJO"""
import concurrent.futures as cf, glob, json, os, shutil, subprocess, sys

PV_N, PV_A, RAIZ, TRAB = (os.path.abspath(x) for x in sys.argv[1:5])
PY = sys.executable


def perimetro(carpeta):
    p = os.path.join(carpeta, "motor_a_f1.json")
    if not os.path.exists(p):
        return None
    try:
        return ((json.load(open(p, encoding="utf-8")).get("perimetro_reinversion") or {}).get("valor")) or "sin declarar"
    except Exception as e:  # noqa
        return f"ilegible ({type(e).__name__})"


def copia(src, dst, con_texto):
    os.makedirs(dst)
    for n in os.listdir(src):
        p = os.path.join(src, n)
        if os.path.isfile(p) and not n.endswith(".xlsx"):
            shutil.copy(p, os.path.join(dst, n))
    for sub in ("etapa1",) + (("texto",) if con_texto else ()):
        if os.path.isdir(os.path.join(src, sub)):
            shutil.copytree(os.path.join(src, sub), os.path.join(dst, sub), ignore=shutil.ignore_patterns("*.xlsx", "*.pdf"))


def correr(pv, carpeta, libro, cfg):
    reg = {}

    def run(nombre, args, guardar=()):
        r = subprocess.run([PY, "-B"] + args, capture_output=True, text=True, env=dict(os.environ, MUNGER_CONFIG=cfg))
        reg[nombre] = r.returncode
        for a, b in guardar:
            if os.path.exists(os.path.join(carpeta, a)):
                shutil.copy(os.path.join(carpeta, a), os.path.join(carpeta, b))
    s = os.path.join(pv, "scripts")
    run("volcar", [os.path.join(s, "volcar_datos_v63.py"), libro, carpeta, "--referencias-mecanicas", "--config", cfg])
    if os.path.exists(os.path.join(carpeta, "fase_b.json")):
        run("gram_antes", [os.path.join(s, "comprobar_gramatica.py"), carpeta, "--antes-de-recalculo", "--config", cfg],
            (("gramatica.json", "R2_gram_antes.json"), ("gramatica.md", "R2_gram_antes.md")))
        if os.path.exists(os.path.join(carpeta, "resultados.json")):
            run("gram_tras", [os.path.join(s, "comprobar_gramatica.py"), carpeta, "--tras-recalculo", "--config", cfg]
                + (["--con-fase-c"] if os.path.exists(os.path.join(carpeta, "fase_c.json")) else []),
                (("gramatica.json", "R2_gram_tras.json"), ("gramatica.md", "R2_gram_tras.md")))
    if os.path.exists(os.path.join(carpeta, "motor_a_f1.json")):
        run("f1", [os.path.join(s, "motor_a_f1.py"), "evaluar", carpeta, "--libro", libro])
    return reg


SALIDAS = ("datos_v63.md", "datos_v63.json", "referencias_mecanicas.json", "R2_gram_antes.json", "R2_gram_antes.md", "R2_gram_tras.json",
           "R2_gram_tras.md", "motor_a_f1_resultado.json", "motor_a_f1_resultado.md")


def uno(i_libro):
    i, libro = i_libro
    src = os.path.dirname(os.path.dirname(libro))
    rel = os.path.relpath(src, RAIZ)
    per = perimetro(src)
    pa = os.path.join(src, "plantilla_activa.json")
    cfg_n = (json.load(open(pa, encoding="utf-8")).get("config") if os.path.exists(pa) else None) or "config_v2.json"
    out = {"expediente": rel, "perimetro": per, "config": cfg_n}
    regs = {}
    for etiqueta, pv in (("anterior", PV_A), ("nuevo", PV_N)):
        d = os.path.join(TRAB, f"{i:02d}", etiqueta, os.path.basename(src))
        copia(src, d, con_texto=per in ("A1_sin_ROU", "A2_propio"))
        cfg = os.path.join(pv, cfg_n)
        if not os.path.exists(cfg):
            out["error"] = f"falta {cfg_n} en {etiqueta}"
            return out
        regs[etiqueta] = (d, correr(pv, d, libro, cfg))
    (da, ra), (dn, rn) = regs["anterior"], regs["nuevo"]
    out["codigos"] = {"anterior": ra, "nuevo": rn}
    dif = []
    for n in SALIDAS:
        a, b = os.path.join(da, n), os.path.join(dn, n)
        if os.path.exists(a) != os.path.exists(b):
            dif.append(n + " (solo en una)")
        elif os.path.exists(a):
            ta = open(a, encoding="utf-8").read().replace(da, "<CARPETA>")
            tb = open(b, encoding="utf-8").read().replace(dn, "<CARPETA>")
            if ta != tb:
                dif.append(n)
    out["distintas"] = dif
    out["comparadas"] = [n for n in SALIDAS if os.path.exists(os.path.join(da, n))]
    return out


libros = sorted(glob.glob(os.path.join(RAIZ, "**", "recalc", "*_v63_evaluada.xlsx"), recursive=True))
libros = [x for x in libros if os.sep + "antecedentes" + os.sep not in x]
if os.path.exists(TRAB):
    shutil.rmtree(TRAB)
with cf.ThreadPoolExecutor(max_workers=6) as ex:
    res = list(ex.map(uno, enumerate(libros)))
n_sin = sum(1 for r in res if r["perimetro"] not in ("A1_sin_ROU", "A2_propio"))
print(f"{len(res)} expedientes con libro recalculado · {n_sin} sin perímetro F1 propio (sin declaración, A0, A3 o sin declarar)")
for r in res:
    marca = "PERÍMETRO" if r["perimetro"] in ("A1_sin_ROU", "A2_propio") else "sin"
    print(f"[{marca:<9}] {r['expediente']:<95} F1 {str(r['perimetro']):<14} comparadas {len(r.get('comparadas', []))} · distintas: {r.get('distintas')}"
          + (f" · ERROR {r['error']}" if r.get("error") else "") + (f" · códigos distintos {r['codigos']}" if r.get("codigos") and r["codigos"]["anterior"] != r["codigos"]["nuevo"] else ""))
malos = [r for r in res if r["perimetro"] not in ("A1_sin_ROU", "A2_propio") and (r.get("distintas") or r.get("error"))]
print(f"\nSIN PERÍMETRO con alguna salida distinta: {len(malos)}" + ("" if not malos else ": " + "; ".join(f"{r['expediente']} {r.get('distintas')}" for r in malos)))
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "salidas", "r2_sin_perimetro.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
