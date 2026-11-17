#!/usr/bin/env python3
"""Ejecuta una especificación de caso del banco Q1 contra la candidata fijada · v3.

v3 (respuesta D2-R1/R2/R7 a CORRECCION_D2 sobre 1ac661b):
- especificación inválida (pasos o criterios vacíos, o criterio sin aserciones) =>
  ERROR_ESPECIFICACION / FALLA_COMPONENTE, nunca COMPONENTE_OK (D2-R1a/b, D2-R2);
- toda aserción se resuelve dentro de las evidencias del caso o de su RUN_DIR
  (prefijo run:); una ruta fuera de ambos => ERROR (D2-R1c);
- json_lista_no_contiene exige una salida de comprobación real (universo > 0);
  no pasa con salida vacía (D2-R1e);
- nueva aserción json_entrada_campo sobre el registro del expediente de prueba;
- control negativo por aserción: pruebas_arnes.py evalúa cada aserción de cada
  especificación contra un estado previo vacío y exige que falle (D2-R2);
- toda comprobación escrita por el arnés queda marcada [SIMULADO]/_simulada,
  también las dadas como diccionario y el --revisor del sellar (D2-R7a);
- una ejecución = evidencias limpias (un log por ejecución) y el resultado guarda
  el SHA observado de la candidata, el estado del árbol y la huella de la spec (D2-R7b/c);
- Q1-026 (preparar_cambio) trabaja en copias bajo RUN_DIR (nunca escribe en la
  candidata), siempre recrea el origen y separa en errores_bloqueo.json los errores
  de texto PDF faltante (pdftotext) de los demás (ipal, AR_2019, AR_2020) (D2-R3).

v2 (CORRECCION_D D-R1..R5) que se conserva: exits esperados por paso, aserciones por
criterio, propagación de errores, artefactos solo si el productor terminó con exit
esperado y huella distinta de la heredada, precondiciones simuladas declaradas.

Uso: python3 ejecutar_caso.py especificaciones/<dir>/Q1-xxx.json
Exit 0 solo si estado_caso == COMPONENTE_OK.
"""
import json
import os
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib_arnes as L  # noqa: E402

# Los nombres de extractor/revisor son precondiciones SIMULADAS (D-R4/D2-R7a): van
# marcados [SIMULADO] en todo registro escrito por el arnés.
EXTRACTOR = "extractor de prueba D (arnés externo) [SIMULADO]"
REVISOR = "revisor independiente de prueba D (arnés externo) [SIMULADO]"


def _json_ruta(obj, ruta):
    for parte in ruta.split("."):
        if isinstance(obj, list):
            try:
                obj = obj[int(parte)]
            except (ValueError, IndexError):
                return None, False
        elif isinstance(obj, dict) and parte in obj:
            obj = obj[parte]
        else:
            return None, False
    return obj, True


def ruta_permitida(caso, archivo):
    """D2-R1c: la aserción solo puede leer dentro de las evidencias del caso o de su
    RUN_DIR (prefijo run:). Devuelve la ruta absoluta o None si está fuera."""
    if archivo.startswith("run:"):
        base = os.path.realpath(os.path.join(L.RUN_DIR, caso.id))
        p = os.path.realpath(os.path.join(base, archivo[len("run:"):]))
    else:
        base = os.path.realpath(caso.ev_dir)
        p = os.path.realpath(os.path.join(base, archivo))
    if p == base or p.startswith(base + os.sep):
        return p
    return None


def evaluar_afirmacion(caso, a):
    """Evalúa una aserción sobre la evidencia guardada. Devuelve (ok, detalle)."""
    p = ruta_permitida(caso, a["archivo"])
    if p is None:
        caso.errores.append(f"ruta fuera del RUN_DIR/evidencias del caso: {a['archivo']!r}")
        return False, f"RUTA FUERA DEL CASO: {a['archivo']}"
    if not os.path.isfile(p):
        return False, f"falta {a['archivo']}"
    tipo = a["tipo"]
    if tipo in ("json_campo", "json_entrada_campo"):
        try:
            obj = json.load(open(p, encoding="utf-8"))
        except Exception as e:
            return False, f"{a['archivo']} no es JSON: {e}"
        if tipo == "json_entrada_campo":
            entrada = next((e for e in obj.get("entradas", []) if isinstance(e, dict) and e.get("celda") == a["celda"]), None)
            if entrada is None:
                return False, f"{a['archivo']}: no hay entrada {a['celda']!r}"
            obj = entrada
        val, hay = _json_ruta(obj, a["ruta"])
        if not hay:
            return False, f"{a['archivo']}: falta la ruta {a['ruta']}"
        op = a.get("op", "eq")
        if op == "eq":
            ok = val == a["valor"]
        elif op == "ne":
            ok = val != a["valor"]
        elif op == "in":
            ok = val in a["valor"]
        elif op == "contiene":
            ok = isinstance(val, str) and a["valor"] in val
        elif op == "no_vacia":
            ok = isinstance(val, (list, dict, str)) and len(val) > 0
        else:
            ok = False
        return ok, f"{a['archivo']}:{a['ruta']} = {val!r} (op {op} {a['valor']!r}) -> {'OK' if ok else 'FALLA'}"
    if tipo == "json_lista_contiene":
        obj = json.load(open(p, encoding="utf-8"))
        lista = obj.get(a["lista"])
        if not isinstance(lista, list):
            return False, f"{a['archivo']}: falta la lista {a['lista']}"
        ok = any(str(x) == a["elemento"] for x in lista)
        return ok, f"{a['archivo']}:{a['lista']} contiene {a['elemento']!r} -> {'OK' if ok else 'FALLA'}"
    if tipo == "json_lista_contiene_texto":
        obj = json.load(open(p, encoding="utf-8"))
        lista = obj.get(a["lista"])
        if not isinstance(lista, list):
            return False, f"{a['archivo']}: falta la lista {a['lista']}"
        ok = any(str(x).startswith(a["prefijo"]) and a["contiene"] in str(x) for x in lista)
        return ok, f"{a['archivo']}:{a['lista']} con prefijo {a['prefijo']!r} contiene {a['contiene']!r} -> {'OK' if ok else 'FALLA'}"
    if tipo == "json_lista_no_contiene":
        obj = json.load(open(p, encoding="utf-8"))
        # D2-R1e: una salida vacía no acredita nada; se exige una comprobación real
        # (universo positivo) para que el negativo tenga sentido.
        universo = obj.get("universo")
        if not isinstance(universo, int) or universo <= 0:
            return False, f"{a['archivo']}: salida sin universo positivo (vacía); el negativo no acredita"
        lista = obj.get(a["lista"])
        if not isinstance(lista, list):
            return False, f"{a['archivo']}: falta la lista {a['lista']}"
        ok = not any(str(x).startswith(a["prefijo"]) for x in lista)
        return ok, f"{a['archivo']}:{a['lista']} sin prefijo {a['prefijo']!r} (universo={universo}) -> {'OK' if ok else 'FALLA'}"
    if tipo == "texto_contiene":
        txt = open(p, encoding="utf-8").read()
        ok = a["contiene"] in txt
        return ok, f"{a['archivo']} contiene {a['contiene']!r} -> {'OK' if ok else 'FALLA'}"
    if tipo == "texto_contiene_todas":
        txt = open(p, encoding="utf-8").read()
        faltan = [s for s in a["contiene_todas"] if s not in txt]
        return not faltan, f"{a['archivo']} contiene todas {a['contiene_todas']!r} -> {'OK' if not faltan else 'FALLA: falta ' + str(faltan)}"
    if tipo == "archivo_existe":
        return True, f"{a['archivo']} existe"
    return False, f"tipo de aserción desconocido: {tipo}"


def op_escribir_fuente(caso, exp, paso):
    nombre = paso["nombre"]
    d = os.path.join(exp, "fuentes_sinteticas")
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, nombre)
    with open(p, "w", encoding="utf-8") as f:
        for i, b in enumerate(paso["paginas"]):
            f.write(f"[PDF PAGE {i + 1}]\n{b}\n\n")
    caso._log(f"fuente escrita: fuentes_sinteticas/{nombre} ({len(paso['paginas'])} páginas) sha256={L.sha256_archivo(p)}\n")
    return p


def op_entrada(caso, exp, paso):
    fuente = paso.get("fuente")
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
        comp = L.marcar_simulada(comp)  # D2-R7a: también las dadas como diccionario
    extra = {k: v for k, v in paso.items()
             if k not in ("op", "celda", "clase", "fuente", "derivacion", "hipotesis", "justificacion",
                          "comprobacion", "incidencia", "material")}
    L.poner_entrada(exp, paso["celda"], clase=paso.get("clase"), fuente=fuente,
                    derivacion=paso.get("derivacion"), hipotesis=paso.get("hipotesis"),
                    justificacion=paso.get("justificacion"), comprobacion=comp,
                    incidencia=paso.get("incidencia"), material=paso.get("material"), **extra)
    caso._log(f"entrada {paso['celda']}: clase={paso.get('clase')} (comprobación preescrita = SIMULADA, marcada)\n")


def op_mutar_fuente(caso, exp, paso):
    p = os.path.join(exp, paso["archivo"])
    with open(p, "w", encoding="utf-8") as f:
        for i, b in enumerate(paso["paginas"]):
            f.write(f"[PDF PAGE {i + 1}]\n{b}\n\n")
    caso._log(f"fuente mutada: {paso['archivo']} nuevo sha256={L.sha256_archivo(p)}\n")


def op_preparar_cambio(caso, paso, esperado):
    """Q1-026 (D2-R3/R-D10): prepara el CAMBIO en copias bajo RUN_DIR (nunca dentro de
    la candidata), siempre recreando el origen; clasifica el stderr del fallo esperado
    separando los textos PDF faltantes (pdftotext) de los demás errores (ipal, AR_2019,
    AR_2020) y verifica que la candidata queda limpia tras la ejecución."""
    pd = os.path.join(L.RUN_DIR, caso.id, "pruebas_d")
    shutil.rmtree(pd, ignore_errors=True)  # nunca se reutiliza un origen preexistente
    os.makedirs(pd, exist_ok=True)
    origen = os.path.join(pd, caso.id + "_origen")
    shutil.copytree(L.PLANTILLA_EXP, origen, ignore=L.IGNORAR_COPIA)
    tsrc = os.path.join(L.PLANTILLA_EXP, "texto")
    if os.path.isdir(tsrc):
        shutil.copytree(tsrc, os.path.join(origen, "texto"), dirs_exist_ok=True)
    cambio = dict(paso["cambio"])
    cambio["origen"] = origen            # ruta absoluta: cambiar_base.py admite abs
    cambio["destino"] = os.path.join(pd, caso.id + "_copia")
    cpath = os.path.join(pd, f"CAMBIO_{caso.id}.json")
    with open(cpath, "w", encoding="utf-8") as f:
        json.dump(cambio, f, ensure_ascii=False, indent=1)
    shutil.copyfile(cpath, os.path.join(caso.ev_dir, "CAMBIO_" + caso.id + ".json"))
    f1 = os.path.join(origen, "fase1_v63.json")
    sha_antes = L.sha256_archivo(f1)
    r_cambio = caso.producto("cambiar_base.py", ["preparar", cpath],
                             "cambiar_base.py preparar (copia nueva bajo RUN_DIR; nunca sobrescribe)",
                             esperado=esperado or (1,), criterio=paso.get("criterio"))
    with open(os.path.join(caso.ev_dir, paso.get("guardar", "cambiar_base_preparar.txt")), "w", encoding="utf-8") as f:
        f.write("--- stdout ---\n" + r_cambio.stdout + "\n--- stderr ---\n" + r_cambio.stderr)
    # D2-R3: separar en el registro los errores de AR_2019/AR_2020/ipal de los de
    # texto PDF ausente (pdftotext), en vez de una subcadena genérica.
    texto_pdf_faltante, otros_errores = [], []
    for linea in r_cambio.stderr.splitlines():
        if "ausente o inexistente en texto/" in linea:
            texto_pdf_faltante.append(linea.strip())
        elif linea.strip():
            otros_errores.append(linea.strip())
    with open(os.path.join(caso.ev_dir, "errores_bloqueo.json"), "w", encoding="utf-8") as f:
        json.dump({"exit": r_cambio.returncode,
                   "texto_pdf_faltante_pdftotext": texto_pdf_faltante,
                   "otros_errores": otros_errores,
                   "nota": "el bloqueo no se atribuye solo a pdftotext: también hay errores de ipal/AR_2019/AR_2020"},
                  f, ensure_ascii=False, indent=1)
    sha_despues = L.sha256_archivo(f1)
    existe_copia = os.path.isdir(os.path.join(pd, caso.id + "_copia"))
    st = subprocess.run(["git", "-C", L.CANDIDATA, "status", "--porcelain"], capture_output=True, text=True).stdout
    sucias = [l for l in st.splitlines() if l.strip() and not l.startswith("??")]
    with open(os.path.join(caso.ev_dir, "origen_estado.txt"), "w", encoding="utf-8") as f:
        f.write(f"origen={origen}\nsha256_fase1_antes={sha_antes}\nsha256_fase1_despues={sha_despues}\n"
                f"intacto={'true' if sha_antes == sha_despues else 'false'}\n"
                f"destino_existe_tras_fallo={'true' if existe_copia else 'false'}\n"
                f"candidata_escribe_el_arnes={'true' if any('pruebas_d' in l for l in st.splitlines()) else 'false'}\n"
                f"candidata_cambios_sin_commit={sucias[:5]}\n")
    caso._log(f"origen intacto={sha_antes == sha_despues}; destino existe tras fallo={existe_copia}; "
              f"arnés escribe en candidata={'true' if any('pruebas_d' in l for l in st.splitlines()) else 'false'}\n")
    caso._log(f"errores_bloqueo: pdf_faltante={len(texto_pdf_faltante)} otros={len(otros_errores)}\n")


def ejecutar(spec_path):
    spec = json.load(open(spec_path, encoding="utf-8"))
    spec_sha = L.sha256_archivo(spec_path)
    problemas, info = L.verificar_entorno()
    caso = L.Caso(spec["id"])
    caso.resultados["spec_sha256"] = spec_sha
    caso.resultados["spec"] = os.path.relpath(spec_path, os.path.dirname(os.path.dirname(L.AUX)))
    caso.resultados["candidata_sha"] = info.get("candidata_sha_observado")
    caso.resultados["banco_casos_sha256"] = info.get("banco_casos_sha256")
    caso.resultados["candidata_no_rastreadas"] = info.get("candidata_no_rastreadas")
    caso._log(f"# Caso {spec['id']} · {spec.get('descripcion', '')}")
    caso._log(f"# candidato: {L.CANDIDATA} (SHA esperado {L.SHA_CANDIDATA_ESPERADO}, observado {info.get('candidata_sha_observado')}) "
              f"· banco: {L.BANCO} (casos_aceptacion.jsonl sha256 {info.get('banco_casos_sha256')}) · fecha: {L.HOY} · harness {L.HARNESS_VERSION}")
    caso._log(f"# spec: {spec_path} sha256={spec_sha}")
    caso._log(f"# precondiciones: {L.PRECONDICION_SIMULADA}\n")
    # D2-R1a/b: especificación vacía o criterio sin aserciones no puede dar COMPONENTE_OK
    spec_valida = bool(spec.get("pasos")) and bool(spec.get("criterios")) and all(c.get("afirma") for c in spec["criterios"])
    if not spec_valida:
        caso.errores.append("especificación inválida: pasos/criterios vacíos o criterio sin aserciones (D2-R1a/b)")
        caso._log("!! ESPECIFICACIÓN INVÁLIDA: pasos o criterios vacíos, o criterio sin afirma\n")
        caso.guardar_resultados("ERROR_ESPECIFICACION", [])
        print(f"ERROR_ESPECIFICACION {spec['id']}: spec vacía o con criterios sin aserciones")
        return 2
    if problemas:
        caso.errores.extend(problemas)
        caso._log("!! ENTORNO INVALIDO: " + "; ".join(problemas) + "\n")
        caso.guardar_resultados("ERROR_ENTORNO", [])
        print(f"ERROR {spec['id']}: entorno inválido: {problemas}")
        return 2
    exp = None
    abortado = False
    for paso in spec["pasos"]:
        if abortado:
            break
        op = paso["op"]
        esperado = tuple(paso.get("esperado", (0,)))
        if op == "nuevo_expediente":
            exp = L.nuevo_expediente(caso)
        elif op == "escribir_fuente":
            op_escribir_fuente(caso, exp, paso)
        elif op == "entrada":
            op_entrada(caso, exp, paso)
        elif op == "mutar_fuente":
            op_mutar_fuente(caso, exp, paso)
        elif op == "comprobar":
            L.comprobar(caso, exp, paso["guardar"], esperado=esperado or (0, 1), criterio=paso.get("criterio"))
        elif op == "sellar":
            caso.producto("verificacion_entradas.py",
                          ["sellar", exp] + paso["celdas"] + ["--revisor", paso.get("revisor", REVISOR), "--fecha", L.HOY],
                          "sellar (revisor [SIMULADO] vincula la comprobación al fundamento)",
                          guardar=paso.get("guardar"), esperado=esperado, criterio=paso.get("criterio"))
        elif op == "ficha":
            caso.producto("ficha.py", [exp] + paso.get("args", []), "ficha.py (salida del producto)",
                          guardar=paso.get("guardar"), esperado=esperado, criterio=paso.get("criterio"))
        elif op == "informe":
            caso.producto("informe.py", [exp] + paso.get("args", []), "informe.py (artefacto exportable)",
                          guardar=paso.get("guardar"), esperado=esperado, criterio=paso.get("criterio"))
        elif op == "preparar_cambio":
            op_preparar_cambio(caso, paso, esperado)
        elif op == "copiar_artefacto":
            ok = caso.copiar_artefacto(exp, paso["archivo"], paso["guardar"],
                                      caso.resultados["pasos"][-1] if caso.resultados["pasos"] else None)
            if not ok:
                caso.resultados["pasos"].append({"op": "copiar_artefacto", "archivo": paso["archivo"],
                                                 "rechazado": True, "criterio": paso.get("criterio")})
        else:
            caso.errores.append(f"op desconocida: {op}")
        if caso.errores and caso.resultados["pasos"] and caso.resultados["pasos"][-1].get("error_inesperado"):
            abortado = True
            caso._log("!! Caso abortado por error inesperado (se propaga)\n")
    # evaluar criterios sobre la evidencia de ESTA ejecución (D-R1)
    criterios = []
    for c in spec.get("criterios", []):
        detalles, ok_all = [], True
        for a in c.get("afirma", []):
            ok, detalle = evaluar_afirmacion(caso, a)
            detalles.append(detalle)
            ok_all = ok_all and ok
        # D2-R1b: un criterio sin aserciones no puede quedar NO_EVALUADO ni dar OK
        estado = "CUMPLE_COMPONENTE" if ok_all and c.get("afirma") else "FALLA_COMPONENTE"
        if estado == "FALLA_COMPONENTE":
            caso.afirmaciones_fallidas.extend(f"[{c['id']}] {d}" for d in detalles if "FALLA" in d or "FUERA" in d)
            if not c.get("afirma"):
                caso.afirmaciones_fallidas.append(f"[{c['id']}] criterio sin aserciones (D2-R1b)")
        criterios.append({"id": c["id"], "texto": c.get("texto", ""), "estado": estado, "detalle": detalles})
    if caso.errores:
        estado_caso = "ERROR"
    elif caso.afirmaciones_fallidas or any(c["estado"] == "FALLA_COMPONENTE" for c in criterios):
        estado_caso = "COMPONENTE_FALLA"
    else:
        estado_caso = "COMPONENTE_OK"
    caso.guardar_resultados(estado_caso, criterios)
    print(f"{'OK' if estado_caso == 'COMPONENTE_OK' else estado_caso} {spec['id']} · criterios="
          f"{[(c['id'], c['estado']) for c in criterios]} · evidencias en {caso.ev_dir}")
    return 0 if estado_caso == "COMPONENTE_OK" else 1


if __name__ == "__main__":
    sys.exit(ejecutar(sys.argv[1]))
