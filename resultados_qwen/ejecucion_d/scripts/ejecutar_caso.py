#!/usr/bin/env python3
"""Ejecuta una especificación de caso del banco Q1 contra la candidata fijada · v2.

v2 (CORRECCION_D D-R1..R5):
- cada paso declara `esperado` (exits válidos; los negativos reales como sellar
  rechazado exit 1 o ficha oficial exit 3 se declaran y no son fallo);
- cada caso declara `criterios` con `afirma`: aserciones sobre los JSON/artefactos
  producidos (campos, listas, textos). Se evalúan sobre la evidencia actual;
- un exit inesperado o una aserción fallida marcan el caso ERROR / COMPONENTE_FALLA
  y se propagan al exit del comando (D-R1);
- los artefactos solo se copian si el comando productor terminó con exit esperado y
  la huella difiere de la heredada (D-R2);
- las precondiciones de extractor/revisor quedan marcadas como simuladas (D-R4).

Uso: python3 ejecutar_caso.py especificaciones/<dir>/Q1-xxx.json
Exit 0 solo si estado_caso == COMPONENTE_OK.
"""
import json
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib_arnes as L  # noqa: E402

# Los nombres de extractor/revisor son precondiciones SIMULADAS (D-R4): el resultado
# lo declara en `precondiciones_simuladas` y cada comprobación lleva "_simulada": true.
EXTRACTOR = "extractor de prueba D (arnés externo)"
REVISOR = "revisor independiente de prueba D (arnés externo)"


def _json_ruta(obj, ruta):
    for parte in ruta.split("."):
        if not isinstance(obj, dict) or parte not in obj:
            return None, False
        obj = obj[parte]
    return obj, True


def evaluar_afirmacion(caso, a):
    """Evalúa una aserción sobre la evidencia guardada. Devuelve (ok, detalle)."""
    p = os.path.join(caso.ev_dir, a["archivo"])
    if not os.path.isfile(p):
        return False, f"falta {a['archivo']}"
    tipo = a["tipo"]
    if tipo in ("json_campo",):
        try:
            obj = json.load(open(p, encoding="utf-8"))
        except Exception as e:
            return False, f"{a['archivo']} no es JSON: {e}"
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
        else:
            ok = False
        return ok, f"{a['archivo']}:{a['ruta']} = {val!r} (op {op} {a['valor']!r}) -> {'OK' if ok else 'FALLA'}"
    if tipo == "json_lista_contiene":
        obj = json.load(open(p, encoding="utf-8"))
        lista = obj.get(a["lista"]) or []
        ok = any(str(x) == a["elemento"] for x in lista)
        return ok, f"{a['archivo']}:{a['lista']} contiene {a['elemento']!r} -> {'OK' if ok else 'FALLA'}"
    if tipo == "json_lista_contiene_texto":
        obj = json.load(open(p, encoding="utf-8"))
        lista = obj.get(a["lista"]) or []
        ok = any(str(x).startswith(a["prefijo"]) and a["contiene"] in str(x) for x in lista)
        return ok, f"{a['archivo']}:{a['lista']} con prefijo {a['prefijo']!r} contiene {a['contiene']!r} -> {'OK' if ok else 'FALLA'}"
    if tipo == "json_lista_no_contiene":
        obj = json.load(open(p, encoding="utf-8"))
        lista = obj.get(a["lista"]) or []
        ok = not any(str(x).startswith(a["prefijo"]) for x in lista)
        return ok, f"{a['archivo']}:{a['lista']} sin prefijo {a['prefijo']!r} -> {'OK' if ok else 'FALLA'}"
    if tipo == "texto_contiene":
        txt = open(p, encoding="utf-8").read()
        ok = a["contiene"] in txt
        return ok, f"{a['archivo']} contiene {a['contiene']!r} -> {'OK' if ok else 'FALLA'}"
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
    extra = {k: v for k, v in paso.items()
             if k not in ("op", "celda", "clase", "fuente", "derivacion", "hipotesis", "justificacion",
                          "comprobacion", "incidencia", "material")}
    L.poner_entrada(exp, paso["celda"], clase=paso.get("clase"), fuente=fuente,
                    derivacion=paso.get("derivacion"), hipotesis=paso.get("hipotesis"),
                    justificacion=paso.get("justificacion"), comprobacion=comp,
                    incidencia=paso.get("incidencia"), material=paso.get("material"), **extra)
    caso._log(f"entrada {paso['celda']}: clase={paso.get('clase')} (comprobación preescrita = simulada)\n")


def op_mutar_fuente(caso, exp, paso):
    p = os.path.join(exp, paso["archivo"])
    with open(p, "w", encoding="utf-8") as f:
        for i, b in enumerate(paso["paginas"]):
            f.write(f"[PDF PAGE {i + 1}]\n{b}\n\n")
    caso._log(f"fuente mutada: {paso['archivo']} nuevo sha256={L.sha256_archivo(p)}\n")


def ejecutar(spec_path):
    spec = json.load(open(spec_path, encoding="utf-8"))
    problemas = L.verificar_entorno()
    caso = L.Caso(spec["id"])
    caso._log(f"# Caso {spec['id']} · {spec.get('descripcion', '')}")
    caso._log(f"# candidato: {L.CANDIDATA} (SHA esperado {L.SHA_CANDIDATA_ESPERADO}) · banco: {L.BANCO} · fecha: {L.HOY}")
    caso._log(f"# precondiciones: {L.PRECONDICION_SIMULADA}\n")
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
                          "sellar (revisor vincula la comprobación al fundamento)",
                          guardar=paso.get("guardar"), esperado=esperado, criterio=paso.get("criterio"))
        elif op == "ficha":
            caso.producto("ficha.py", [exp] + paso.get("args", []), "ficha.py (salida del producto)",
                          guardar=paso.get("guardar"), esperado=esperado, criterio=paso.get("criterio"))
        elif op == "informe":
            caso.producto("informe.py", [exp] + paso.get("args", []), "informe.py (artefacto exportable)",
                          guardar=paso.get("guardar"), esperado=esperado, criterio=paso.get("criterio"))
        elif op == "preparar_cambio":
            # Q1-026: prepara el CAMBIO en una copia de prueba DENTRO de la copia local de la
            # candidata (pruebas_d/, no commiteada) y ejecuta cambiar_base.py preparar.
            # Escribe en evidencias el CAMBIO y el estado del origen (intacto o no).
            import shutil as _sh
            pd = os.path.join(L.CANDIDATA, "munger_v2_r1", "pruebas_d")
            os.makedirs(pd, exist_ok=True)
            origen = os.path.join(pd, caso.id + "_origen")
            if not os.path.isdir(origen):
                _sh.copytree(L.PLANTILLA_EXP, origen, ignore=L.IGNORAR_COPIA)
                # los textos de los PDF faltan sin pdftotext: se copia lo disponible
                tsrc = os.path.join(L.PLANTILLA_EXP, "texto")
                if os.path.isdir(tsrc):
                    _sh.copytree(tsrc, os.path.join(origen, "texto"), dirs_exist_ok=True)
            cambio = dict(paso["cambio"])
            cambio["origen"] = f"pruebas_d/{caso.id}_origen"
            cambio["destino"] = f"pruebas_d/{caso.id}_copia"
            _sh.rmtree(os.path.join(pd, caso.id + "_copia"), ignore_errors=True)
            cpath = os.path.join(pd, f"CAMBIO_{caso.id}.json")
            with open(cpath, "w", encoding="utf-8") as f:
                json.dump(cambio, f, ensure_ascii=False, indent=1)
            _sh.copyfile(cpath, os.path.join(caso.ev_dir, "CAMBIO_" + caso.id + ".json"))
            f1 = os.path.join(origen, "fase1_v63.json")
            sha_antes = L.sha256_archivo(f1)
            r_cambio = caso.producto("cambiar_base.py", ["preparar", cpath],
                                     "cambiar_base.py preparar (copia nueva; nunca sobrescribe)",
                                     esperado=esperado or (1,), criterio=paso.get("criterio"))
            with open(os.path.join(caso.ev_dir, paso.get("guardar", "cambiar_base_preparar.txt")), "w", encoding="utf-8") as f:
                f.write("--- stdout ---\n" + r_cambio.stdout + "\n--- stderr ---\n" + r_cambio.stderr)
            sha_despues = L.sha256_archivo(f1)
            existe_copia = os.path.isdir(os.path.join(pd, caso.id + "_copia"))
            with open(os.path.join(caso.ev_dir, "origen_estado.txt"), "w", encoding="utf-8") as f:
                f.write(f"origen={cambio['origen']}\nsha256_fase1_antes={sha_antes}\nsha256_fase1_despues={sha_despues}\n"
                        f"intacto={'true' if sha_antes == sha_despues else 'false'}\n"
                        f"destino_existe_tras_fallo={'true' if existe_copia else 'false'}\n")
            caso._log(f"origen intacto={sha_antes == sha_despues}; destino existe tras fallo={existe_copia}\n")
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
    # evaluar criterios sobre la evidencia actual (D-R1)
    criterios = []
    for c in spec.get("criterios", []):
        detalles, ok_all = [], True
        for a in c.get("afirma", []):
            ok, detalle = evaluar_afirmacion(caso, a)
            detalles.append(detalle)
            ok_all = ok_all and ok
        if not c.get("afirma"):
            ok_all = None
        estado = "CUMPLE_COMPONENTE" if ok_all else ("FALLA_COMPONENTE" if ok_all is False else "NO_EVALUADO")
        if estado == "FALLA_COMPONENTE":
            caso.afirmaciones_fallidas.extend(f"[{c['id']}] {d}" for d in detalles if "FALLA" in d)
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
