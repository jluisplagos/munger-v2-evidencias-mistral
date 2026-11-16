"""Biblioteca del arnés externo del frente D (Mistral D · aceptación Qwen Q1).

Ejecuta comandos documentados del producto Munger V2 (rama candidata fijada) sobre
copias locales de prueba aisladas. No modifica el producto: solo lee sus scripts y
escribe en expedientes de prueba copiados aparte. Todo comando ejecutado queda
registrado con su código de salida y salida en resultados_qwen/ejecucion_d/evidencias/.
"""
import datetime as dt
import hashlib
import json
import os
import shutil
import subprocess
import sys

AUX = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # resultados_qwen/ejecucion_d
REPO_AUX = os.path.dirname(AUX)
EVIDENCIAS = os.path.join(AUX, "evidencias")

CANDIDATA = os.environ.get("CANDIDATA_DIR", "/workspace/base_414_main")
PERSONAJE = os.path.join(CANDIDATA, "munger_v2_r1", "personaje_v2")
SCRIPTS = os.path.join(PERSONAJE, "scripts")
PLANTILLA_EXP = os.environ.get(
    "PLANTILLA_EXP",
    os.path.join(PERSONAJE, "empresas_v2_correcciones", "2026-11_Vidrala_ensayo_4_13", "viscofan", "Viscofan"),
)
BANCO = os.environ.get("BANCO_DIR", "/workspace/banco_q1_v2/resultados_qwen/q1_v2/banco_revisado")
RUN_DIR = os.environ.get("RUN_DIR", "/workspace/ejecucion_d_run")

HOY = dt.datetime.now().astimezone().date().isoformat()
IGNORAR_COPIA = shutil.ignore_patterns(".lo_perfil", "variantes_v64", "recalc", "prompts_generados", "__pycache__", ".downloads")


def sha256_archivo(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


class Caso:
    def __init__(self, caso_id):
        self.id = caso_id
        self.ev_dir = os.path.join(EVIDENCIAS, caso_id)
        os.makedirs(self.ev_dir, exist_ok=True)
        self.log = os.path.join(self.ev_dir, "ejecucion.log")
        self.resultados = {"caso": caso_id, "pasos": []}

    def _log(self, texto):
        with open(self.log, "a", encoding="utf-8") as f:
            f.write(texto + "\n")

    def ejecutar(self, args, descripcion, cwd=SCRIPTS, guardar=None, exit_esperado=None):
        """Ejecuta un comando real del producto y registra todo."""
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        r = subprocess.run(args, cwd=cwd, env=env, capture_output=True, text=True)
        self._log(f"$ {' '.join(args)}   (cwd={cwd})")
        self._log(f"exit={r.returncode}")
        if r.stdout:
            self._log("--- stdout ---\n" + r.stdout)
        if r.stderr:
            self._log("--- stderr ---\n" + r.stderr)
        paso = {"descripcion": descripcion, "comando": args, "cwd": cwd, "exit": r.returncode,
                "stdout": r.stdout[-20000:], "stderr": r.stderr[-20000:]}
        if guardar:
            with open(os.path.join(self.ev_dir, guardar), "w", encoding="utf-8") as f:
                f.write(r.stdout)
            paso["guardado_en"] = guardar
        if exit_esperado is not None and r.returncode != exit_esperado:
            paso["AVISO"] = f"exit {r.returncode} != esperado {exit_esperado}"
        self.resultados["pasos"].append(paso)
        self._log("")
        return r

    def producto(self, script, args, descripcion, guardar=None, exit_esperado=None):
        return self.ejecutar([sys.executable, "-B", os.path.join(SCRIPTS, script)] + args,
                             descripcion, guardar=guardar, exit_esperado=exit_esperado)

    def guardar_resultados(self):
        with open(os.path.join(self.ev_dir, "resultado_ejecucion.json"), "w", encoding="utf-8") as f:
            json.dump(self.resultados, f, ensure_ascii=False, indent=1)


def nuevo_expediente(caso):
    """Copia limpia del expediente plantilla del producto en un directorio aislado."""
    destino = os.path.join(RUN_DIR, caso.id, "Viscofan")
    shutil.rmtree(os.path.join(RUN_DIR, caso.id), ignore_errors=True)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    shutil.copytree(PLANTILLA_EXP, destino, ignore=IGNORAR_COPIA)
    caso.ejecutar([sys.executable, "-B", os.path.join(SCRIPTS, "verificacion_entradas.py"), "plantilla", destino],
                  "plantilla del registro de entradas (comando documentado del producto)", guardar=None)
    return destino


def materializar_fuente(caso, exp, nombre, texto, con_paginas=True):
    """Guarda una fuente sintética local con marcas [PDF PAGE n] como hace pdf_a_texto.py."""
    d = os.path.join(exp, "fuentes_sinteticas")
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, nombre)
    if con_paginas:
        lineas = texto.splitlines() or [""]
        # las páginas del fixture se separan por líneas en blanco dobles o se numeran en orden
        bloques, actual = [], []
        for ln in lineas:
            if ln.strip() == "" and actual:
                bloques.append("\n".join(actual))
                actual = []
            else:
                actual.append(ln)
        if actual:
            bloques.append("\n".join(actual))
        if len(bloques) <= 1:
            bloques = [texto]
        contenido = "".join(f"[PDF PAGE {i + 1}]\n{b}\n" for i, b in enumerate(bloques))
    else:
        contenido = texto if texto.endswith("\n") else texto + "\n"
    with open(p, "w", encoding="utf-8") as f:
        f.write(contenido)
    return p


def leer_registro(exp):
    p = os.path.join(exp, "verificacion_entradas.json")
    if not os.path.isfile(p):
        plantilla = os.path.join(exp, "verificacion_entradas.plantilla.json")
        shutil.copyfile(plantilla, p)
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def escribir_registro(exp, reg):
    with open(os.path.join(exp, "verificacion_entradas.json"), "w", encoding="utf-8") as f:
        json.dump(reg, f, ensure_ascii=False, indent=1, default=str)


def poner_entrada(exp, celda, clase=None, fuente=None, derivacion=None, hipotesis=None, justificacion=None,
                  comprobacion=None, incidencia=None, material=None, valor_modelo=None):
    reg = leer_registro(exp)
    reg.setdefault("perimetro_del_expediente", "consolidado")
    por = {str(e.get("celda")): e for e in reg["entradas"]}
    e = por.get(celda)
    if e is None:
        raise KeyError(f"celda {celda} no está en el universo de la plantilla")
    if clase is not None:
        e["clase"] = clase
    if fuente is not None:
        e["fuente"] = fuente
    if derivacion is not None:
        e["derivacion"] = derivacion
    if hipotesis is not None:
        e["hipotesis"] = hipotesis
    if justificacion is not None:
        e["justificacion"] = justificacion
    if comprobacion is not None:
        e["comprobacion"] = comprobacion
    if incidencia is not None:
        e["incidencia"] = incidencia
    if material is not None:
        e["material"] = material
    if valor_modelo is not None:
        e["valor_modelo"] = valor_modelo
    escribir_registro(exp, reg)
    return e


def fuente_local(exp, rel_archivo, documento, pagina, concepto, periodo, unidad, escala, signo, valor_fuente, cita,
                 version="sintética v1", ubicacion="tabla sintética", columna=None, perimetro="consolidado",
                 reexpresado="no aplica", tratamiento="ninguno"):
    return {
        "documento": documento,
        "archivo": rel_archivo,
        "sha256": sha256_archivo(os.path.join(exp, rel_archivo)),
        "conservacion": "local",
        "version": version,
        "pagina": str(pagina),
        "ubicacion": ubicacion,
        "concepto": concepto,
        "columna": columna or periodo,
        "periodo": periodo,
        "unidad": unidad,
        "escala": escala,
        "signo": signo,
        "tratamiento": tratamiento,
        "perimetro": perimetro,
        "reexpresado": reexpresado,
        "valor_fuente": valor_fuente,
        "cita": cita,
    }


def comprobacion_verificada(extractor, revisor, fuente_examinada, fecha=None, nota=None):
    return {"extractor": extractor, "revisor": revisor, "fecha": fecha or HOY, "resultado": "verificado",
            "fuente_examinada": fuente_examinada, "nota": nota, "vinculo": None}


def comprobar(caso, exp, guardar):
    return caso.producto("verificacion_entradas.py", ["comprobar", exp, "--json"],
                          "comprobación del registro de entradas (comando documentado del producto)",
                          guardar=guardar)


def leer_comprobacion(ev_dir, nombre):
    with open(os.path.join(ev_dir, nombre), encoding="utf-8") as f:
        return json.load(f)
