#!/usr/bin/env python3
"""Ejecuta una especificación de caso del banco Q1 contra la candidata fijada · v4.

v4 (respuesta D3-R1/R2/R7 a CORRECCION_D3 sobre d032691):
- el id se valida (Q1-nnn, dentro de EVIDENCIAS) ANTES de tocar el disco;
- toda ruta — aserciones, `guardar`, `escribir_fuente.nombre`, `mutar_fuente.archivo`,
  `copiar_artefacto.archivo` — se resuelve dentro de las evidencias del caso o de su
  RUN_DIR; se rechazan rutas absolutas y escapes (variantes P3va/P3vb/N1a/N1b);
- las aserciones solo leen archivos producidos por comandos del producto (guardados
  con `guardar` o copiados con copiar_artefacto); nunca archivos del propio arnés
  ni `run:` (P1v, N3);
- nueva aserción `stderr_lineas_eq` (líneas exactas del stderr de un paso del producto);
- un criterio marcado `no_discriminante` se evalúa pero queda OBSERVACION y fuera del
  cómputo de COMPONENTE_OK (Q1-027 C4);
- Q1-026: el CAMBIO se valida contra el banco (cifras 95→90, deuda 300, deuda neta 210)
  y C1 se ancla a las líneas exactas del stderr real; origen intacto y candidata limpia
  son comprobaciones duras del arnés, no aserciones;
- sellar: el --revisor siempre queda marcado [SIMULADO];
- spec vacía / sin aserciones → ERROR_ESPECIFICACION (D2-R1, conservado).

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
    """D3-R1: la aserción solo puede leer dentro de las evidencias del caso, y solo
    archivos producidos por el producto. Devuelve la ruta o None."""
    if archivo.startswith("run:"):
        caso.errores.append("aserción con prefijo run: no soportada (D3-R1 inv.3: solo salidas del producto en evidencias)")
        return None
    p = L.ruta_dentro(caso.ev_dir, archivo)
    if p is None:
        caso.errores.append(f"ruta fuera de las evidencias del caso: {archivo!r}")
        return None
    ap = getattr(caso, "archivos_producto", None)
    if ap is not None and os.path.basename(p) not in ap:
        caso.errores.append(f"aserción sobre archivo no producido por el producto: {archivo!r}")
        return None
    return p


def evaluar_afirmacion(caso, a):
    """Evalúa una aserción sobre la evidencia del producto guardada. Devuelve (ok, detalle)."""
    p = ruta_permitida(caso, a["archivo"])
    if p is None:
        return False, f"RUTA NO PERMITIDA: {a['archivo']}"
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
        return not faltan, f"{a['archivo']} contiene todas -> {'OK' if not faltan else 'FALLA: falta ' + str(faltan[:2])}"
    if tipo == "stderr_lineas_eq":
        # D3-R2: ancla al mensaje real y completo del stderr de un paso del producto
        txt = open(p, encoding="utf-8").read()
        sec = txt.split("--- stderr ---", 1)[1] if "--- stderr ---" in txt else ""
        lineas = [l.rstrip() for l in sec.splitlines() if l.strip()]
        esperadas = [s.rstrip() for s in a["lineas_stderr"]]
        ok = lineas == esperadas
        return ok, (f"{a['archivo']}: stderr con {len(lineas)} líneas == {len(esperadas)} esperadas -> "
                    + ("OK" if ok else f"FALLA (diferencia en {[l for l in lineas if l not in esperadas][:1]})"))
    if tipo == "archivo_existe":
        return True, f"{a['archivo']} existe"
    return False, f"tipo de aserción desconocido: {tipo}"


def op_escribir_fuente(caso, exp, paso):
    nombre = paso["nombre"]
    if L.ruta_dentro(os.path.join(exp, "fuentes_sinteticas"), nombre) is None or os.path.basename(nombre) != nombre:
        caso.errores.append(f"escribir_fuente con nombre fuera de fuentes_sinteticas del caso: {nombre!r}")
        caso._log(f"!! NOMBRE DE FUENTE RECHAZADO: {nombre!r}\n")
        return None
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
        comp = L.marcar_simulada(comp)
    extra = {k: v for k, v in paso.items()
             if k not in ("op", "celda", "clase", "fuente", "derivacion", "hipotesis", "justificacion",
                          "comprobacion", "incidencia", "material")}
    L.poner_entrada(exp, paso["celda"], clase=paso.get("clase"), fuente=fuente,
                    derivacion=paso.get("derivacion"), hipotesis=paso.get("hipotesis"),
                    justificacion=paso.get("justificacion"), comprobacion=comp,
                    incidencia=paso.get("incidencia"), material=paso.get("material"), **extra)
    caso._log(f"entrada {paso['celda']}: clase={paso.get('clase')} (comprobación preescrita = SIMULADA, marcada)\n")


def op_mutar_fuente(caso, exp, paso):
    p = L.ruta_dentro(exp, paso["archivo"])
    if p is None:
        caso.errores.append(f"mutar_fuente con ruta fuera del expediente del caso: {paso['archivo']!r}")
        caso._log(f"!! RUTA DE MUTACIÓN RECHAZADA: {paso['archivo']!r}\n")
        return
    with open(p, "w", encoding="utf-8") as f:
        for i, b in enumerate(paso["paginas"]):
            f.write(f"[PDF PAGE {i + 1}]\n{b}\n\n")
    caso._log(f"fuente mutada: {paso['archivo']} nuevo sha256={L.sha256_archivo(p)}\n")


def validar_cambio_contra_banco(caso, spec):
    """D3-R3: el CAMBIO de Q1-026 se valida contra el banco (cifras y cálculo de la
    deuda neta), no contra texto suelto. Lee el banco (fuente normativa, de solo lectura)."""
    cid = spec["id"]
    casos = [json.loads(l) for l in open(os.path.join(L.BANCO, "casos_aceptacion.jsonl"), encoding="utf-8") if l.strip()]
    banco = next(c for c in casos if c["id"] == cid)
    esperado = banco.get("esperado_numerico") or {}
    for paso in spec.get("pasos", []):
        if paso.get("op") != "preparar_cambio":
            continue
        cambio = paso.get("cambio") or {}
        c24 = (cambio.get("analisis") or {}).get("C24") or {}
        errores = []
        if c24.get("valor") != 90.0:
            errores.append(f"analisis.C24.valor={c24.get('valor')!r} != 90 (banco: caja 95->90)")
        fuente_txt = c24.get("fuente") or ""
        fixture = os.path.join(L.BANCO, "fixtures", "f5_026_nota.txt")
        linea_fixture = open(fixture, encoding="utf-8").read().strip() if os.path.isfile(fixture) else ""
        if linea_fixture and linea_fixture not in fuente_txt:
            errores.append("la cita de C24.fuente no contiene la línea literal del fixture f5_026_nota.txt")
        if not (cambio.get("evidencia")):
            errores.append("falta el bloque evidencia del CAMBIO")
        dn = (cambio.get("derivados_esperados") or {}).get("deuda_neta") or {}
        if dn.get("resultado") != esperado.get("resultado") or dn.get("operandos") != esperado.get("operandos"):
            errores.append(f"derivados_esperados.deuda_neta={dn!r} != esperado del banco {esperado!r}")
        for e in errores:
            caso.errores.append(f"CAMBIO no coherente con el banco: {e}")
        caso._log(f"validación del CAMBIO contra el banco {cid}: {'OK' if not errores else 'FALLA: ' + '; '.join(errores)}\n")


def op_preparar_cambio(caso, paso, esperado):
    """Q1-026 (D3-R1/R3): copias bajo RUN_DIR (nunca en la candidata), origen siempre
    recreado; origen intacto y candidata limpia son comprobaciones DURAS del arnés."""
    pd = os.path.join(L.RUN_DIR, caso.id, "pruebas_d")
    shutil.rmtree(pd, ignore_errors=True)
    os.makedirs(pd, exist_ok=True)
    origen = os.path.join(pd, caso.id + "_origen")
    shutil.copytree(L.PLANTILLA_EXP, origen, ignore=L.IGNORAR_COPIA)
    tsrc = os.path.join(L.PLANTILLA_EXP, "texto")
    if os.path.isdir(tsrc):
        shutil.copytree(tsrc, os.path.join(origen, "texto"), dirs_exist_ok=True)
    cambio = dict(paso["cambio"])
    cambio["origen"] = origen
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
    caso._guardar(paso.get("guardar", "cambiar_base_preparar.txt"),
                 "--- stdout ---\n" + r_cambio.stdout + "\n--- stderr ---\n" + r_cambio.stderr)
    # diagnóstico del arnés (NO asertable: no es salida del producto)
    texto_pdf, otros = [], []
    for linea in r_cambio.stderr.splitlines():
        if "ausente o inexistente en texto/" in linea:
            texto_pdf.append(linea.strip())
        elif linea.strip():
            otros.append(linea.strip())
    with open(os.path.join(caso.ev_dir, "errores_bloqueo.json"), "w", encoding="utf-8") as f:
        json.dump({"exit": r_cambio.returncode, "texto_pdf_faltante_pdftotext": texto_pdf,
                   "otros_errores": otros,
                   "nota": "diagnostico del arnes; las aserciones solo leen salidas del producto (cambiar_base_preparar.txt)"},
                  f, ensure_ascii=False, indent=1)
    sha_despues = L.sha256_archivo(f1)
    if sha_antes != sha_despues:
        caso.errores.append("Q1-026: el origen cambió (sha256 distinto) — el producto debe no sobrescribir")
    st = subprocess.run(["git", "-C", L.CANDIDATA, "status", "--porcelain"], capture_output=True, text=True).stdout
    if any("pruebas_d" in l for l in st.splitlines()):
        caso.errores.append("Q1-026: el arnés escribió dentro de la candidata (pruebas_d/)")
    with open(os.path.join(caso.ev_dir, "origen_estado.txt"), "w", encoding="utf-8") as f:
        f.write(f"origen={origen}\nsha256_fase1_antes={sha_antes}\nsha256_fase1_despues={sha_despues}\n"
                f"intacto={'true' if sha_antes == sha_despues else 'false'}\n")
    caso._log(f"origen intacto={sha_antes == sha_despues} (comprobación dura del arnés)\n")


def ejecutar(spec_path):
    spec = json.load(open(spec_path, encoding="utf-8"))
    # D3-R1 inv.4: validar el id ANTES de tocar el disco
    err_id = L.validar_id(spec.get("id"))
    if err_id:
        print(f"ERROR_ID {spec.get('id')!r}: {err_id}")
        return 2
    spec_sha = L.sha256_archivo(spec_path)
    problemas, info = L.verificar_entorno()
    caso = L.Caso(spec["id"])
    caso.resultados["spec_sha256"] = spec_sha
    caso.resultados["spec"] = os.path.relpath(os.path.abspath(spec_path), os.path.dirname(os.path.dirname(L.AUX)))
    caso.resultados["candidata_sha"] = info.get("candidata_sha_observado")
    caso.resultados["banco_casos_sha256"] = info.get("banco_casos_sha256")
    caso.resultados["candidata_no_rastreadas"] = info.get("candidata_no_rastreadas")
    caso._log(f"# Caso {spec['id']} · {spec.get('descripcion', '')}")
    caso._log(f"# candidato: {L.CANDIDATA} (SHA esperado {L.SHA_CANDIDATA_ESPERADO}, observado {info.get('candidata_sha_observado')}) "
              f"· banco: {L.BANCO} (casos sha256 {info.get('banco_casos_sha256')}) · fecha: {L.HOY} · harness {L.HARNESS_VERSION}")
    caso._log(f"# spec: {spec_path} sha256={spec_sha}")
    caso._log(f"# precondiciones: {L.PRECONDICION_SIMULADA}\n")
    spec_valida = bool(spec.get("pasos")) and bool(spec.get("criterios")) and all(c.get("afirma") for c in spec["criterios"])
    if not spec_valida:
        caso.errores.append("especificación inválida: pasos/criterios vacíos o criterio sin aserciones (D2-R1a/b)")
        caso._log("!! ESPECIFICACIÓN INVÁLIDA\n")
        caso.guardar_resultados("ERROR_ESPECIFICACION", [])
        print(f"ERROR_ESPECIFICACION {spec['id']}: spec vacía o con criterios sin aserciones")
        return 2
    if problemas:
        caso.errores.extend(problemas)
        caso._log("!! ENTORNO INVALIDO: " + "; ".join(problemas) + "\n")
        caso.guardar_resultados("ERROR_ENTORNO", [])
        print(f"ERROR {spec['id']}: entorno inválido: {problemas}")
        return 2
    validar_cambio_contra_banco(caso, spec)
    if caso.errores:
        caso.guardar_resultados("ERROR_ESPECIFICACION", [])
        print(f"ERROR_ESPECIFICACION {spec['id']}: {caso.errores}")
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
            revisor = paso.get("revisor", REVISOR)
            if "[SIMULADO]" not in revisor:
                revisor = revisor + " [SIMULADO]"  # D3-R7: siempre marcado
            caso.producto("verificacion_entradas.py",
                          ["sellar", exp] + paso["celdas"] + ["--revisor", revisor, "--fecha", L.HOY],
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
    if caso.errores and any("RUTA" in e or "fuera" in e or "no producido" in e for e in caso.errores):
        abortado = True
    criterios = []
    for c in spec.get("criterios", []):
        detalles, ok_all = [], True
        for a in c.get("afirma", []):
            ok, detalle = evaluar_afirmacion(caso, a)
            detalles.append(detalle)
            ok_all = ok_all and ok
        if not c.get("afirma"):
            ok_all = False
        if c.get("no_discriminante"):
            estado = "OBSERVACION_NO_DISCRIMINANTE" if ok_all else "FALLA_COMPONENTE"
        else:
            estado = "CUMPLE_COMPONENTE" if ok_all else "FALLA_COMPONENTE"
        if estado == "FALLA_COMPONENTE":
            caso.afirmaciones_fallidas.extend(f"[{c['id']}] {d}" for d in detalles if "FALLA" in d or "NO PERMITIDA" in d)
        criterios.append({"id": c["id"], "texto": c.get("texto", ""), "estado": estado,
                          "no_discriminante": bool(c.get("no_discriminante")), "detalle": detalles})
    if caso.errores:
        estado_caso = "ERROR"
    elif caso.afirmaciones_fallidas or any(c["estado"] == "FALLA_COMPONENTE" for c in criterios):
        estado_caso = "COMPONENTE_FALLA"
    elif all(c["estado"] == "CUMPLE_COMPONENTE" for c in criterios if not c["no_discriminante"]) and any(
            c["estado"] == "CUMPLE_COMPONENTE" for c in criterios):
        estado_caso = "COMPONENTE_OK"
    else:
        estado_caso = "COMPONENTE_FALLA"
    caso.guardar_resultados(estado_caso, criterios)
    print(f"{'OK' if estado_caso == 'COMPONENTE_OK' else estado_caso} {spec['id']} · criterios="
          f"{[(c['id'], c['estado']) for c in criterios]} · evidencias en {caso.ev_dir}")
    return 0 if estado_caso == "COMPONENTE_OK" else 1


if __name__ == "__main__":
    sys.exit(ejecutar(sys.argv[1]))
