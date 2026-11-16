#!/usr/bin/env python3
"""Ejecuta una especificación de caso del banco Q1 contra la candidata fijada del producto.

Uso: python3 ejecutar_caso.py especificaciones/piloto/Q1-001.json
Cada paso invoca comandos documentados del producto sobre una copia aislada del
expediente plantilla; todo queda en evidencias/<caso>/.
"""
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib_arnes as L  # noqa: E402

EXTRACTOR = "extractor de prueba D (arnés externo)"
REVISOR = "revisor independiente de prueba D (arnés externo)"


def op_escribir_fuente(caso, exp, paso):
    nombre = paso["nombre"]
    paginas = paso["paginas"]
    d = os.path.join(exp, "fuentes_sinteticas")
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, nombre)
    with open(p, "w", encoding="utf-8") as f:
        for i, b in enumerate(paginas):
            f.write(f"[PDF PAGE {i + 1}]\n{b}\n\n")
    caso._log(f"fuente escrita: fuentes_sinteticas/{nombre} ({len(paginas)} páginas) sha256={L.sha256_archivo(p)}")
    return p


def op_entrada(caso, exp, paso):
    fuente = paso.get("fuente")
    if fuente and fuente.get("archivo") and fuente.get("sha256") is None and os.path.isfile(os.path.join(exp, fuente["archivo"])):
        rel = fuente["archivo"]
        fuente = dict(fuente)
        fuente["sha256"] = L.sha256_archivo(os.path.join(exp, rel))
    if fuente:
        fuente = dict(fuente)
        fuente.setdefault("columna", fuente.get("periodo"))
        fuente.setdefault("tratamiento", "ninguno")
        fuente.setdefault("perimetro", "consolidado")
        fuente.setdefault("reexpresado", "no aplica")
        fuente.setdefault("conservacion", "local" if fuente.get("archivo") else "externa")
        if fuente.get("archivo") and fuente.get("sha256") is None and os.path.isfile(os.path.join(exp, fuente["archivo"])):
            fuente["sha256"] = L.sha256_archivo(os.path.join(exp, fuente["archivo"]))
    comp = paso.get("comprobacion")
    if comp == "verificada":
        rel = (fuente or {}).get("archivo", "")
        comp = L.comprobacion_verificada(EXTRACTOR, REVISOR, f"{rel} (página {paso.get('fuente', {}).get('pagina', '?')})")
    elif isinstance(comp, dict):
        comp = {k: (L.HOY if v == "HOY" else v) for k, v in comp.items()}
    extra = {k: v for k, v in paso.items()
             if k not in ("op", "celda", "clase", "fuente", "derivacion", "hipotesis", "justificacion",
                          "comprobacion", "incidencia", "material")}
    L.poner_entrada(exp, paso["celda"], clase=paso.get("clase"), fuente=fuente,
                    derivacion=paso.get("derivacion"), hipotesis=paso.get("hipotesis"),
                    justificacion=paso.get("justificacion"), comprobacion=comp,
                    incidencia=paso.get("incidencia"), material=paso.get("material"), **extra)
    caso._log(f"entrada {paso['celda']}: clase={paso.get('clase')}")


def op_mutar_fuente(caso, exp, paso):
    p = os.path.join(exp, paso["archivo"])
    with open(p, "w", encoding="utf-8") as f:
        for i, b in enumerate(paso["paginas"]):
            f.write(f"[PDF PAGE {i + 1}]\n{b}\n\n")
    caso._log(f"fuente mutada: {paso['archivo']} nuevo sha256={L.sha256_archivo(p)}")


def ejecutar(spec_path):
    spec = json.load(open(spec_path, encoding="utf-8"))
    caso = L.Caso(spec["id"])
    caso._log(f"# Caso {spec['id']} · {spec.get('descripcion', '')}")
    caso._log(f"# candidato: {L.CANDIDATA} · banco: {L.BANCO} · fecha: {L.HOY}\n")
    exp = None
    for paso in spec["pasos"]:
        op = paso["op"]
        if op == "nuevo_expediente":
            exp = L.nuevo_expediente(caso)
        elif op == "escribir_fuente":
            op_escribir_fuente(caso, exp, paso)
        elif op == "entrada":
            op_entrada(caso, exp, paso)
        elif op == "mutar_fuente":
            op_mutar_fuente(caso, exp, paso)
        elif op == "comprobar":
            L.comprobar(caso, exp, paso["guardar"])
        elif op == "sellar":
            caso.producto("verificacion_entradas.py",
                          ["sellar", exp] + paso["celdas"] + ["--revisor", paso.get("revisor", REVISOR), "--fecha", L.HOY],
                          "sellar (revisor vincula la comprobación al fundamento)", guardar=paso.get("guardar"))
        elif op == "ficha":
            caso.producto("ficha.py", [exp] + paso.get("args", []), "ficha.py (salida del producto)",
                          guardar=paso.get("guardar"))
        elif op == "informe":
            caso.producto("informe.py", [exp] + paso.get("args", []), "informe.py (artefacto exportable)",
                          guardar=paso.get("guardar"))
        elif op == "copiar_artefacto":
            src = os.path.join(exp, paso["archivo"])
            if os.path.isfile(src):
                shutil.copyfile(src, os.path.join(caso.ev_dir, paso["guardar"]))
                caso._log(f"artefacto copiado a evidencias: {paso['guardar']}")
        else:
            raise ValueError(f"op desconocida: {op}")
    caso.guardar_resultados()
    print(f"OK {spec['id']} · pasos={len(spec['pasos'])} · evidencias en {caso.ev_dir}")


if __name__ == "__main__":
    ejecutar(sys.argv[1])
