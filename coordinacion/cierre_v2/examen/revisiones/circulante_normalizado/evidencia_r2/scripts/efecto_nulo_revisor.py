#!/usr/bin/env python3
"""(V-CIRC) Efecto nulo del cambio en los expedientes en curso, SIN la declaración de la normalización del circulante: la evaluación F1 completa
(motor_a_f1.evaluar, salvo «version» y «fecha»), su informe .md, lo que la aplicación de la declaración escribe en un libro V6.3.1 F1
(f1_libro_v631.celdas), la huella de entradas de los libros (entradas_economicas.instantanea) y la vigencia F1 (motor_a_f1.vigencia), con el
código ANTERIOR (git, por omisión ebf47fc, el de partida de la rama) y con el del árbol actual, sobre COPIAS de los expedientes (sin pdf/).

Uso (desde munger_v2_r1/): python3 -I …/f1_circulante/scripts/comprobar_efecto_nulo.py EXAMEN DESTINO [--commit ebf47fc] [--json SALIDA.json]
  EXAMEN: carpeta 2026-11_examen_universo de un árbol con los expedientes y sus binarios (solo se lee); DESTINO: carpeta nueva (se borra al final).
Expedientes: ahold_f3/Ahold, jumbo_g/Jumbo, zoetis_t1c/Zoetis (los tres en curso con la V6.3.1 F1) y vinci/Vinci (sin la declaración nueva).
Código 0 si todo es idéntico.
"""
import json
import os
import shutil
import subprocess
import sys

RAIZ = "/dev/shm/r2/nuevo/munger_v2_r1"
REPO = "/home/user/e_work/wt_circulante"
EXPEDIENTES = ("ahold_f3/Ahold", "ahold_f4/Ahold", "jumbo_g/Jumbo", "zoetis_t1c/Zoetis", "zoetis_t1d/Zoetis", "vinci/Vinci")
TRABAJADOR = r'''
import json, os, sys
scripts, c, libro, datos, motor = sys.argv[1:6]
sys.path.insert(0, scripts)
import motor_a_f1 as M
import f1_libro_v631 as V
import entradas_economicas as EE
L = M.leer_libro(libro)
d = json.load(open(os.path.join(c, "motor_a_f1.json"), encoding="utf-8"))
r = M.evaluar(L, d, motor_libro=motor or None, carpeta=c)
md = M.informe_md(dict(r, version="(versión)", fecha="(fecha)"))
anios = [int(L[f"Historia!{x}5"]) for x in "CDEFGHIJKL"]
out = {"evaluacion": {k: v for k, v in r.items() if k not in ("version", "fecha")}, "informe_md": md, "celdas_v631": V.celdas(d, anios),
       "huella_libro_evaluado": EE.instantanea(libro)["huella"], "huella_libro_datos": EE.instantanea(datos)["huella"] if datos else None,
       "vigencia": M.vigencia(c), "version": r.get("version")}
print("@@" + json.dumps(out, ensure_ascii=False, default=str, sort_keys=True))
'''


def correr(scripts, c, libro, datos, motor):
    t = os.path.join(os.path.dirname(c), "_trabajador.py")
    open(t, "w", encoding="utf-8").write(TRABAJADOR)
    r = subprocess.run([sys.executable, "-I", t, scripts, c, libro, datos or "", motor or ""], capture_output=True, text=True)
    lin = [x for x in r.stdout.splitlines() if x.startswith("@@")]
    if not lin:
        raise SystemExit(f"el trabajador falló con {scripts} en {c}: {r.stderr[-600:]}")
    return json.loads(lin[-1][2:])


def main():
    a = sys.argv[1:]
    if len(a) < 2:
        print(__doc__)
        return 2
    examen, destino = a[0], a[1]
    commit = a[a.index("--commit") + 1] if "--commit" in a else "ebf47fc"
    salida = a[a.index("--json") + 1] if "--json" in a else None
    if os.path.exists(destino):
        raise SystemExit(f"{destino} ya existe")
    os.makedirs(destino)
    try:
        viejo = os.path.join(destino, "anterior")
        os.makedirs(viejo)
        arch = subprocess.run(["git", "-C", REPO, "archive", commit, "munger_v2_r1/personaje_v2/scripts", "munger_v2_r1/personaje_v2/esquema",
                               "munger_v2_r1/personaje_v2/config_v2.json", "munger_v2_r1/v6/scripts"], capture_output=True, check=True).stdout
        subprocess.run(["tar", "-x", "-C", viejo], input=arch, check=True)
        s_viejo = os.path.join(viejo, "munger_v2_r1", "personaje_v2", "scripts")
        s_nuevo = os.path.join(RAIZ, "personaje_v2", "scripts")
        filas, todo_igual = [], True
        for e in EXPEDIENTES:
            orig = os.path.join(examen, e)
            c = os.path.join(destino, "copias", e)
            shutil.copytree(orig, c, ignore=shutil.ignore_patterns("pdf", ".lo_perfil", "__pycache__"))
            emp = os.path.basename(e)
            rec = os.path.join(c, "recalc")
            libro = next((os.path.join(rec, n) for n in (f"{emp}_v63_evaluada.xlsx", f"{emp}_v63_datos.xlsx") if os.path.isfile(os.path.join(rec, n))), None)
            datos = os.path.join(c, f"{emp}_v63_datos.xlsx") if os.path.isfile(os.path.join(c, f"{emp}_v63_datos.xlsx")) else None
            st = json.load(open(os.path.join(c, "estado_pipeline.json"), encoding="utf-8"))
            motor = st.get("motor")
            v, n = correr(s_viejo, c, libro, datos, motor), correr(s_nuevo, c, libro, datos, motor)
            dif = sorted(k for k in set(v) | set(n) if k != "version" and v.get(k) != n.get(k))
            if "evaluacion" in dif:
                ev_, en_ = v["evaluacion"], n["evaluacion"]
                dif.remove("evaluacion")
                dif += [f"evaluacion.{k}" for k in sorted(set(ev_) | set(en_)) if ev_.get(k) != en_.get(k)]
            todo_igual &= not dif
            r = n["evaluacion"]
            cd = r.get("calculo_perimetro_declarado") or {}
            filas.append({"expediente": e, "libro": os.path.relpath(libro, c), "motor": motor, "paso": st.get("paso"),
                          "utilizable": r.get("utilizable_para_conclusion"), "bloquean": sorted({g["id"] for g in r.get("guardas") or [] if g.get("salta") and g.get("severidad") == "BLOQUEA"}),
                          "f": cd.get("f"), "flujo_sin_crecimiento": cd.get("flujo_sin_crecimiento"), "ancla_s2c_E4": cd.get("ancla_s2c_E4"),
                          "normalizacion_en_el_resultado": "normalizacion_circulante" in r, "guarda_F1_CIRC": any(g.get("id") == "F1-CIRC" for g in r.get("guardas") or []),
                          "vigencia": {k: n["vigencia"].get(k) for k in ("exigido", "vigente", "utilizable")},
                          "diferencias_salvo_version_y_fecha": dif, "version_anterior": v["version"], "version_nueva": n["version"]})
            print(f"{e}: {'IDÉNTICO' if not dif else 'DISTINTO ' + str(dif)} (salvo versión y fecha) · utilizable {r.get('utilizable_para_conclusion')} · bloquean "
                  f"{filas[-1]['bloquean']} · f {cd.get('f')} · flujo sin crecimiento {cd.get('flujo_sin_crecimiento')} · vigencia {filas[-1]['vigencia']}")
        res = {"commit_anterior": commit, "expedientes": filas, "todo_identico": todo_igual,
               "comparado": "evaluación F1 completa salvo versión y fecha, informe .md, celdas que f1_libro_v631 escribe en el libro V6.3.1, huella de entradas "
                            "del libro evaluado y del de datos, y vigencia F1"}
        if salida:
            json.dump(res, open(salida, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
        print(f"{'todo idéntico' if todo_igual else 'HAY DIFERENCIAS'} en {len(filas)} expedientes (código anterior {commit} frente al actual)")
        return 0 if todo_igual else 1
    finally:
        shutil.rmtree(destino, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
