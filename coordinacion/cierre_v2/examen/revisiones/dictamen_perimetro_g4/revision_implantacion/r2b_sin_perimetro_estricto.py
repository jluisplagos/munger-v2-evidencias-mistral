"""Revisión de la implantación de P-FOSO · R2b: «sin perímetro nada cambia», variante ESTRICTA de r2_sin_perimetro.py.
Diferencia con R2: antes de ejecutar, se BORRAN de las dos copias las salidas que el expediente ya traía (datos_v63.*, referencias_mecanicas.json,
gramatica.*, motor_a_f1_resultado.*), de modo que solo se comparan archivos que cada versión ha vuelto a ESCRIBIR; y se anota qué pasos
terminan sin escribir su salida. Así una copia heredada del expediente no puede contar como «idéntica».
Scripts ANTERIORES (ab40e80) frente a NUEVOS (688df46). Nada se escribe en los repositorios.
Uso: r2b_sin_perimetro_estricto.py PV_NUEVO PV_ANTERIOR RAIZ_EXPEDIENTES CARPETA_TRABAJO"""
import concurrent.futures as cf, glob, json, os, shutil, subprocess, sys

PV_N, PV_A, RAIZ, TRAB = (os.path.abspath(x) for x in sys.argv[1:5])
PY = sys.executable
HEREDADAS = ("datos_v63.md", "datos_v63.json", "referencias_mecanicas.json", "gramatica.json", "gramatica.md", "motor_a_f1_resultado.json", "motor_a_f1_resultado.md")
PASOS = {"volcar": ("datos_v63.md", "datos_v63.json", "referencias_mecanicas.json"), "gram_antes": ("gramatica.json", "gramatica.md"),
         "gram_tras": ("gramatica.json", "gramatica.md"), "f1": ("motor_a_f1_resultado.json", "motor_a_f1_resultado.md")}


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
        if os.path.isfile(p) and not n.endswith(".xlsx") and n not in HEREDADAS:
            shutil.copy(p, os.path.join(dst, n))
    for sub in ("etapa1",) + (("texto",) if con_texto else ()):
        if os.path.isdir(os.path.join(src, sub)):
            shutil.copytree(os.path.join(src, sub), os.path.join(dst, sub), ignore=shutil.ignore_patterns("*.xlsx", "*.pdf"))


def correr(pv, carpeta, libro, cfg):
    reg, escritos = {}, {}

    def run(nombre, args):
        for a in PASOS[nombre]:
            if os.path.exists(os.path.join(carpeta, a)):
                os.remove(os.path.join(carpeta, a))
        r = subprocess.run([PY, "-B"] + args, capture_output=True, text=True, env=dict(os.environ, MUNGER_CONFIG=cfg))
        reg[nombre] = r.returncode
        for a in PASOS[nombre]:
            if os.path.exists(os.path.join(carpeta, a)):
                b = f"R2B_{nombre}_{a}"
                shutil.copy(os.path.join(carpeta, a), os.path.join(carpeta, b))
                escritos[b] = True
        reg[nombre + "_salida"] = (r.stdout + r.stderr).replace(carpeta, "<CARPETA>").replace(pv, "<PV>")
    s = os.path.join(pv, "scripts")
    run("volcar", [os.path.join(s, "volcar_datos_v63.py"), libro, carpeta, "--referencias-mecanicas", "--config", cfg])
    if os.path.exists(os.path.join(carpeta, "fase_b.json")):
        run("gram_antes", [os.path.join(s, "comprobar_gramatica.py"), carpeta, "--antes-de-recalculo", "--config", cfg])
        if os.path.exists(os.path.join(carpeta, "resultados.json")):
            run("gram_tras", [os.path.join(s, "comprobar_gramatica.py"), carpeta, "--tras-recalculo", "--config", cfg]
                + (["--con-fase-c"] if os.path.exists(os.path.join(carpeta, "fase_c.json")) else []))
    if os.path.exists(os.path.join(carpeta, "motor_a_f1.json")):
        run("f1", [os.path.join(s, "motor_a_f1.py"), "evaluar", carpeta, "--libro", libro])
    # el volcado se guarda al final para comparar el que deja el paso «volcar» (los pasos siguientes no lo reescriben)
    return reg, sorted(escritos)


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
        regs[etiqueta] = (d,) + correr(pv, d, libro, os.path.join(pv, cfg_n))
    (da, ra, ea), (dn, rn, en) = regs["anterior"], regs["nuevo"]
    out["codigos"] = {"anterior": {k: v for k, v in ra.items() if not k.endswith("_salida")}, "nuevo": {k: v for k, v in rn.items() if not k.endswith("_salida")}}
    out["consola_distinta"] = [k[:-7] for k in ra if k.endswith("_salida") and ra[k] != rn.get(k)]
    dif = []
    for n in sorted(set(ea) | set(en)):
        a, b = os.path.join(da, n), os.path.join(dn, n)
        if os.path.exists(a) != os.path.exists(b):
            dif.append(n + " (solo en una)")
        elif open(a, encoding="utf-8").read().replace(da, "<CARPETA>") != open(b, encoding="utf-8").read().replace(dn, "<CARPETA>"):
            dif.append(n)
    out["distintas"], out["reescritas"] = dif, ea
    out["pasos_sin_salida"] = [k for k in PASOS if k in out["codigos"]["anterior"] and not any(x.startswith(f"R2B_{k}_") for x in ea)]
    return out


libros = sorted(glob.glob(os.path.join(RAIZ, "**", "recalc", "*_v63_evaluada.xlsx"), recursive=True))
libros = [x for x in libros if os.sep + "antecedentes" + os.sep not in x]
if os.path.exists(TRAB):
    shutil.rmtree(TRAB)
with cf.ThreadPoolExecutor(max_workers=6) as ex:
    res = list(ex.map(uno, enumerate(libros)))
propio = lambda r: r["perimetro"] in ("A1_sin_ROU", "A2_propio")  # noqa: E731
sin = [r for r in res if not propio(r)]
print(f"{len(res)} expedientes con libro recalculado · {len(sin)} sin perímetro F1 propio")
tot = {}
for r in res:
    print(f"[{'PERÍMETRO' if propio(r) else 'sin':<9}] {r['expediente']:<93} F1 {str(r['perimetro']):<12} reescritas {len(r['reescritas'])} · distintas {r['distintas']} · "
          f"códigos {r['codigos']['nuevo']}" + ("" if r["codigos"]["anterior"] == r["codigos"]["nuevo"] else f" ≠ anterior {r['codigos']['anterior']}")
          + (f" · consola distinta en {r['consola_distinta']}" if r["consola_distinta"] else "") + (f" · pasos sin salida {r['pasos_sin_salida']}" if r["pasos_sin_salida"] else ""))
    if not propio(r):
        for k in r["codigos"]["nuevo"]:
            tot.setdefault(k, [0, 0]); tot[k][0] += 1
            tot[k][1] += sum(1 for x in r["reescritas"] if x.startswith(f"R2B_{k}_"))
print(f"\nSIN PERÍMETRO · archivos reescritos por las dos versiones y comparados: {sum(len(r['reescritas']) for r in sin)} · distintos: "
      f"{sum(len(r['distintas']) for r in sin)} {[(r['expediente'].split('/')[-2], r['distintas']) for r in sin if r['distintas']]}")
print("   por paso (expedientes que lo ejecutan, archivos reescritos):", {k: tuple(v) for k, v in tot.items()})
print("   códigos de salida distintos entre versiones:", [r["expediente"] for r in sin if r["codigos"]["anterior"] != r["codigos"]["nuevo"]])
print("   consola distinta entre versiones:", [(r["expediente"].split("/")[-2], r["consola_distinta"]) for r in sin if r["consola_distinta"]])
print("   pasos que no escriben su salida (en las dos versiones):", [(r["expediente"].split("/")[-2], r["pasos_sin_salida"]) for r in sin if r["pasos_sin_salida"]])
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "salidas", "r2b_sin_perimetro_estricto.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
