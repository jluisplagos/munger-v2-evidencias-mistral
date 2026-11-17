"""Biblioteca del arnés externo del frente D (Mistral D · aceptación Qwen Q1) · v4.

Ejecuta comandos documentados del producto Munger V2 (candidata fijada) sobre copias
locales de prueba aisladas y evalúa aserciones por criterio sobre las salidas reales
del producto. No modifica el producto.

v4 (respuesta D3-R1/R2/R7 a CORRECCION_D3 sobre d032691):
- el id de la spec se valida ANTES de tocar el disco (ruta dentro de EVIDENCIAS);
- TODA ruta (lectura y escritura: aserciones, guardar, escribir_fuente, mutar_fuente,
  copiar_artefacto) se resuelve dentro de las evidencias del caso o de su RUN_DIR;
  se rechazan rutas absolutas y cualquier escape;
- las aserciones solo pueden leer archivos producidos por comandos del producto
  (guardados con `guardar` o copiados con copiar_artefacto): nunca archivos escritos
  por el propio arnés (ejecucion.log, resultado, CAMBIO_*, errores_bloqueo,
  origen_estado) ni `run:` (el RUN_DIR no se publica);
- la candidata "limpia" se comprueba de verdad: además del SHA y de `git status`,
  se detectan skip-worktree/assume-unchanged (`git ls-files -v`) y cualquier archivo
  en disco bajo personaje_v2/scripts/ que no esté rastreado (cubre .git/info/exclude);
- una ejecución = evidencias limpias (salvo ARNES_EVIDENCIAS_LIMPIAS=0, que queda
  registrado); toda comprobación escrita por el arnés lleva _simulada/[SIMULADO],
  también la por defecto de las celdas aux y el --revisor pasado por la spec;
- registra huella del banco y de la spec usada.

v3/v2 (D2) que se conservan: archivo de salidas heredadas, artefactos solo con exit
esperado del productor y huella distinta, propagación de errores, precondiciones
SIMULADAS declaradas, banco y candidata verificados en ejecución.
"""
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True

HARNESS_VERSION = "4.0"
ID_RE = re.compile(r"^Q1-\d{3}$")

AUX = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # resultados_qwen/ejecucion_d
EVIDENCIAS = os.environ.get("EVIDENCIAS_DIR", os.path.join(AUX, "evidencias"))

CANDIDATA = os.environ.get("CANDIDATA_DIR", "/workspace/base_414_main")
SHA_CANDIDATA_ESPERADO = os.environ.get("SHA_CANDIDATA_ESPERADO", "957af652cdc3bef3d67e8623c9572138bac685e9")
PERSONAJE = os.path.join(CANDIDATA, "munger_v2_r1", "personaje_v2")
SCRIPTS = os.path.join(PERSONAJE, "scripts")
PLANTILLA_EXP = os.environ.get(
    "PLANTILLA_EXP",
    os.path.join(PERSONAJE, "empresas_v2_correcciones", "2026-11_Vidrala_ensayo_4_13", "viscofan", "Viscofan"),
)
# BANCO_DIR apunta a la carpeta banco_revisado (la que contiene casos_aceptacion.jsonl)
BANCO = os.environ.get("BANCO_DIR", "/workspace/banco_q1_v2/resultados_qwen/q1_v2/banco_revisado")
RUN_DIR = os.environ.get("RUN_DIR", "/workspace/ejecucion_d_run")

HOY = dt.datetime.now().astimezone().date().isoformat()
IGNORAR_COPIA = shutil.ignore_patterns(".lo_perfil", "variantes_v64", "recalc", "prompts_generados", "__pycache__", ".downloads")

ARTEFACTOS_HEREDADOS = [
    "ficha.json", "ficha_provisional.json", "informe.md", "informe_provisional.md",
    "auditoria.md", "material_auditoria.json", "diagnostico.md", "historial_cierres",
    "publicaciones_resumen.json", "cierre_vigente.json", "auditorias_conocidas.json",
]

PRECONDICION_SIMULADA = ("extractor/revisor escritos por el arnés = precondición SIMULADA de test de componentes; "
                         "no es revisión independiente ejecutada (D-R4/D2-R7/D3-R7)")


def sha256_archivo(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def ruta_dentro(base, rel):
    """D3-R1: resuelve `rel` dentro de `base` y devuelve la ruta absoluta, o None si
    es absoluta, contiene escape o queda fuera de `base`."""
    if not isinstance(rel, str) or not rel or os.path.isabs(rel):
        return None
    base_r = os.path.realpath(base)
    p = os.path.realpath(os.path.join(base_r, rel))
    if p != base_r and not p.startswith(base_r + os.sep):
        return None
    return p


def validar_id(caso_id):
    """D3-R1 invariante 4: el id se valida antes de tocar el disco."""
    if not isinstance(caso_id, str) or not ID_RE.match(caso_id):
        return f"id inválido {caso_id!r}: debe ser Q1-nnn"
    if ruta_dentro(EVIDENCIAS, caso_id) is None:
        return f"id {caso_id!r} queda fuera de EVIDENCIAS={EVIDENCIAS}"
    return None


def verificar_entorno():
    """D3-R1 invariante 5 + D-R5: SHA observado, árbol limpio de verdad (incluye
    skip-worktree/assume-unchanged y archivos no rastreados bajo scripts/, aunque estén
    ocultos por .git/info/exclude) y presencia+huella del banco. Devuelve (problemas, info)."""
    problemas = []
    info = {}
    script = os.path.join(SCRIPTS, "verificacion_entradas.py")
    if not os.path.isfile(script):
        problemas.append(f"falta {script} (CANDIDATA_DIR={CANDIDATA})")
    else:
        r = subprocess.run(["git", "-C", CANDIDATA, "rev-parse", "HEAD"], capture_output=True, text=True)
        sha = r.stdout.strip()
        info["candidata_sha_observado"] = sha
        if r.returncode != 0 or sha != SHA_CANDIDATA_ESPERADO:
            problemas.append(f"SHA candidata observado {sha!r} != esperado {SHA_CANDIDATA_ESPERADO}")
        dif = subprocess.run(["git", "-C", CANDIDATA, "diff", "HEAD", "--name-only"], capture_output=True, text=True).stdout
        con_cambios = [l for l in dif.splitlines() if l.strip()]
        if con_cambios:
            problemas.append(f"cambios sin commit respecto a HEAD: {con_cambios[:5]}")
        lv = subprocess.run(["git", "-C", CANDIDATA, "ls-files", "-v"], capture_output=True, text=True).stdout
        flags = [l for l in lv.splitlines() if l and l[0] in ("h", "S")]
        if flags:
            problemas.append(f"archivos con assume-unchanged/skip-worktree: {[l[2:] for l in flags][:5]}")
        # archivos en disco bajo scripts/ que no estén rastreados (cubre info/exclude)
        tracked = set()
        lf = subprocess.run(["git", "-C", CANDIDATA, "ls-files", "--", "munger_v2_r1/personaje_v2/scripts"],
                            capture_output=True, text=True).stdout.split()
        tracked = set(lf)
        en_disco = []
        for raiz, _, archivos in os.walk(SCRIPTS):
            for a in archivos:
                rel = os.path.relpath(os.path.join(raiz, a), CANDIDATA)
                if rel not in tracked:
                    en_disco.append(rel)
        if en_disco:
            problemas.append(f"archivos no rastreados bajo scripts/ (posible alteración oculta): {en_disco[:5]}")
        st = subprocess.run(["git", "-C", CANDIDATA, "status", "--porcelain"], capture_output=True, text=True).stdout
        lineas = [l for l in st.splitlines() if l.strip()]
        no_rastreadas = [l for l in lineas if l.startswith("??")]
        info["candidata_no_rastreadas"] = len(no_rastreadas)
        residuo = [l for l in no_rastreadas if "pruebas_d" in l]
        if residuo:
            problemas.append(f"la candidata contiene residuo pruebas_d/ del arnés: {residuo[:3]}")
    banco_jsonl = os.path.join(BANCO, "casos_aceptacion.jsonl")
    if not os.path.isfile(banco_jsonl):
        problemas.append(f"BANCO_DIR={BANCO} no contiene casos_aceptacion.jsonl (debe apuntar a .../banco_revisado)")
    else:
        info["banco_casos_sha256"] = sha256_archivo(banco_jsonl)
    return problemas, info


class Caso:
    def __init__(self, caso_id):
        self.id = caso_id
        self.ev_dir = os.path.join(EVIDENCIAS, caso_id)
        self.limpias = os.environ.get("ARNES_EVIDENCIAS_LIMPIAS", "1") == "1"
        if self.limpias and os.path.isdir(self.ev_dir):
            shutil.rmtree(self.ev_dir)  # una ejecución = una carpeta de evidencias limpia
        os.makedirs(self.ev_dir, exist_ok=True)
        self.log = os.path.join(self.ev_dir, "ejecucion.log")
        self.heredados = {}
        self.artefactos = []
        self.archivos_producto = set()  # D3-R1 inv.3: solo estos son legibles por aserciones
        self.errores = []
        self.afirmaciones_fallidas = []
        self.resultados = {"caso": caso_id, "harness_version": HARNESS_VERSION, "fecha": HOY,
                           "precondiciones_simuladas": PRECONDICION_SIMULADA,
                           "evidencias_limpiadas": self.limpias,
                           "candidata_sha": None, "candidata_sha_esperado": SHA_CANDIDATA_ESPERADO,
                           "banco_casos_sha256": None, "spec_sha256": None, "pasos": []}
        if not self.limpias:
            self._log("# AVISO: ARNES_EVIDENCIAS_LIMPIAS=0 -> la evidencia previa NO se ha limpiado; "
                      "este log puede acumular ejecuciones (registrado en el resultado)\n")

    def _log(self, texto):
        with open(self.log, "a", encoding="utf-8") as f:
            f.write(texto + "\n")

    def _guardar(self, guardar, contenido):
        """D3-R1: toda escritura del arnés queda dentro de las evidencias del caso."""
        p = ruta_dentro(self.ev_dir, guardar)
        if p is None:
            self.errores.append(f"ruta de salida fuera de las evidencias del caso: {guardar!r}")
            self._log(f"!! RUTA DE SALIDA RECHAZADA: {guardar!r}\n")
            return False
        with open(p, "w", encoding="utf-8") as f:
            f.write(contenido)
        self.archivos_producto.add(os.path.basename(p))
        return True

    def ejecutar(self, args, descripcion, cwd=SCRIPTS, guardar=None, esperado=(0,), criterio=None):
        """Ejecuta un comando real del producto. exit fuera de `esperado` -> error inesperado."""
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        r = subprocess.run(args, cwd=cwd, env=env, capture_output=True, text=True)
        self._log(f"$ {' '.join(args)}   (cwd={cwd})")
        self._log(f"exit={r.returncode} (esperado {list(esperado)})")
        if r.stdout:
            self._log("--- stdout ---\n" + r.stdout)
        if r.stderr:
            self._log("--- stderr ---\n" + r.stderr)
        paso = {"descripcion": descripcion, "comando": args, "exit": r.returncode,
                "esperado": list(esperado), "criterio": criterio,
                "stdout": r.stdout[-20000:], "stderr": r.stderr[-20000:]}
        if guardar:
            if self._guardar(guardar, r.stdout):
                paso["guardado_en"] = os.path.basename(guardar)
        if r.returncode not in esperado:
            paso["error_inesperado"] = True
            self.errores.append(f"{descripcion}: exit {r.returncode} no está en esperado {list(esperado)}")
            self._log(f"!! ERROR INESPERADO: exit {r.returncode} (esperado {list(esperado)})\n")
        self.resultados["pasos"].append(paso)
        self._log("")
        return r

    def producto(self, script, args, descripcion, guardar=None, esperado=(0,), criterio=None):
        return self.ejecutar([sys.executable, "-B", os.path.join(SCRIPTS, script)] + args,
                             descripcion, guardar=guardar, esperado=esperado, criterio=criterio)

    def copiar_artefacto(self, exp, archivo, guardar, paso_productor):
        """D3-R1: el origen solo puede estar dentro del expediente de prueba del caso."""
        src = ruta_dentro(exp, archivo)
        if src is None:
            self.errores.append(f"copiar_artefacto con ruta fuera del expediente del caso: {archivo!r}")
            self.afirmaciones_fallidas.append(f"copiar_artefacto rechazado (ruta fuera del caso): {archivo!r}")
            self._log(f"!! RUTA DE ARTEFACTO RECHAZADA: {archivo!r}\n")
            return False
        nombre = os.path.basename(archivo)
        if not os.path.isfile(src):
            self.afirmaciones_fallidas.append(f"artefacto {archivo} no existe tras el paso productor")
            return False
        sha = sha256_archivo(src)
        heredado = self.heredados.get(nombre)
        nuevo = heredado is None or sha != heredado
        productor_ok = paso_productor is not None and not paso_productor.get("error_inesperado")
        if not (productor_ok and nuevo):
            self.afirmaciones_fallidas.append(
                f"artefacto {nombre} rechazado: productor_ok={productor_ok}, nuevo={nuevo} (heredado_sha={heredado})")
            self._log(f"!! ARTEFACTO RECHAZADO (heredado o productor fallido): {archivo} sha={sha}\n")
            return False
        if not self._guardar(guardar, open(src, "rb").read().decode("utf-8", errors="replace")):
            return False
        self.artefactos.append({"archivo": nombre, "guardado_en": os.path.basename(guardar), "sha256": sha,
                               "productor": paso_productor.get("descripcion"), "nuevo": True})
        self._log(f"artefacto copiado (nuevo, sha={sha[:16]}…): {guardar}\n")
        return True

    def guardar_resultados(self, estado_caso, criterios):
        self.resultados["estado_caso"] = estado_caso
        self.resultados["criterios"] = criterios
        self.resultados["artefactos"] = self.artefactos
        self.resultados["errores"] = self.errores
        self.resultados["afirmaciones_fallidas"] = self.afirmaciones_fallidas
        self.resultados["archivos_producto"] = sorted(self.archivos_producto)
        with open(os.path.join(self.ev_dir, "resultado_ejecucion.json"), "w", encoding="utf-8") as f:
            json.dump(self.resultados, f, ensure_ascii=False, indent=1)


def nuevo_expediente(caso):
    """Copia limpia del expediente plantilla; archiva las salidas heredadas (D-R2)."""
    destino = os.path.join(RUN_DIR, caso.id, "Viscofan")
    shutil.rmtree(os.path.join(RUN_DIR, caso.id), ignore_errors=True)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    shutil.copytree(PLANTILLA_EXP, destino, ignore=IGNORAR_COPIA)
    arch = os.path.join(RUN_DIR, caso.id, "_heredados")
    os.makedirs(arch, exist_ok=True)
    for nombre in ARTEFACTOS_HEREDADOS:
        p = os.path.join(destino, nombre)
        if os.path.exists(p):
            if os.path.isdir(p):
                shutil.move(p, os.path.join(arch, nombre))
                caso.heredados[nombre] = "dir"
            else:
                shutil.move(p, os.path.join(arch, nombre))
                caso.heredados[nombre] = sha256_archivo(os.path.join(arch, nombre))
    caso._log(f"heredados archivados en {arch}: {sorted(caso.heredados)}\n")
    caso.ejecutar([sys.executable, "-B", os.path.join(SCRIPTS, "verificacion_entradas.py"), "plantilla", destino],
                  "plantilla del registro de entradas (comando documentado del producto)")
    return destino


def materializar_fuente(caso, exp, nombre, texto, con_paginas=True):
    d = os.path.join(exp, "fuentes_sinteticas")
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, nombre)
    if con_paginas:
        bloques, actual = [], []
        for ln in texto.splitlines() or [""]:
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
                  comprobacion=None, incidencia=None, material=None, valor_modelo=None, **extra):
    reg = leer_registro(exp)
    if not (reg.get("perimetro_del_expediente") or "").strip():
        reg["perimetro_del_expediente"] = "consolidado"
    por = {str(e.get("celda")): e for e in reg["entradas"]}
    e = por.get(celda)
    if e is None:
        if not celda.startswith("aux:"):
            raise KeyError(f"celda {celda} no está en el universo de la plantilla")
        e = {"celda": celda, "id": celda, "ambito": "auxiliar", "uso": None, "material": True, "clase": None,
             "valor_modelo": None, "fuente": {}, "derivacion": None, "hipotesis": None, "justificacion": None,
             # D3-R7: la comprobación por defecto que escribe el arnés también es simulada
             "comprobacion": {"extractor": None, "revisor": None, "fecha": None, "resultado": "pendiente",
                              "fuente_examinada": None, "nota": None, "vinculo": None, "_simulada": True},
             "incidencia": None}
        reg["entradas"].append(e)
        por[celda] = e
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
    for k, v in extra.items():
        if v is not None:
            e[k] = v
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
    """D-R4/D2-R7/D3-R7: registro preescrito por el arnés = precondición SIMULADA."""
    return {"extractor": extractor, "revisor": revisor, "fecha": fecha or HOY, "resultado": "verificado",
            "fuente_examinada": fuente_examinada, "nota": nota, "vinculo": None,
            "_simulada": True}


def marcar_simulada(comprobacion):
    """D2-R7a/D3-R7: toda comprobación escrita por el arnés queda marcada como simulada."""
    if not isinstance(comprobacion, dict):
        return comprobacion
    comprobacion["_simulada"] = True
    for campo in ("extractor", "revisor"):
        v = comprobacion.get(campo)
        if isinstance(v, str) and "[SIMULADO]" not in v:
            comprobacion[campo] = v + " [SIMULADO]"
    return comprobacion


def comprobar(caso, exp, guardar, esperado=(0, 1), criterio=None):
    return caso.producto("verificacion_entradas.py", ["comprobar", exp, "--json"],
                         "comprobación del registro de entradas (comando documentado del producto)",
                         guardar=guardar, esperado=esperado, criterio=criterio)


def leer_comprobacion(ev_dir, nombre):
    with open(os.path.join(ev_dir, nombre), encoding="utf-8") as f:
        return json.load(f)
