"""D3-R2 · control negativo contra el ESTADO PREVIO, hecho de verdad, sobre la evidencia publicada.

Uso: python3 -I -B s09_control_estado_previo.py <ejecucion_d @c734ca1> <estado_previo.json> <salida.json>

<estado_previo.json> es la salida REAL de `verificacion_entradas.py comprobar --json` (candidata
957af65) sobre el expediente recién copiado de la plantilla, sin ninguna entrada del caso
(s09_estado_previo_plantilla_957af65.json). No ejecuta el producto: reevalúa las aserciones con el
`evaluar_afirmacion` del propio arnés v4.

Para cada aserción que lee una salida de `comprobar`:
  BASE = la misma aserción evaluada sobre el estado previo común (antes de cualquier paso del caso);
  PREV = la misma aserción evaluada sobre la salida de `comprobar` inmediatamente anterior del mismo caso.
Una aserción que pasa en BASE o en PREV no distingue «el caso hizo algo» de «el caso no hizo nada».
El estado previo DE REFERENCIA de una aserción es PREV si existe y BASE si no (primera comprobación del caso).
Un CRITERIO es no discriminante si TODAS sus aserciones leen salidas de `comprobar` y TODAS pasan en su estado
previo de referencia: daría CUMPLE aunque el paso que debe producir el efecto no hubiera ocurrido.
(Un criterio de persistencia, como Q1-025 C1 «sigue comprobada», pasa en PREV por diseño en su segunda aserción;
no se señala porque su primera aserción sí discrimina frente a BASE.)

Compara con la prueba 34 del autor (pruebas_arnes.py:427-464), que quita el archivo leído y por eso
no puede fallar.
"""
import glob, json, os, shutil, sys, tempfile

D, BASE, OUT = [os.path.abspath(x) for x in sys.argv[1:4]]
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(D, "scripts"))
import lib_arnes as L  # noqa: E402
import ejecutar_caso as EC  # noqa: E402

res = {"objeto": "c734ca1: especificaciones + evidencia publicada", "estado_previo": os.path.basename(BASE),
       "aserciones": 0, "aserciones_sobre_comprobar": 0, "detalle": {}}
no_disc_criterios, pasan_base, pasan_prev = [], [], []


def evaluar(tmp, archivo, contenido_de, a):
    d = tempfile.mkdtemp(dir=tmp)
    shutil.copy(contenido_de, os.path.join(d, archivo))
    c = L.Caso.__new__(L.Caso)
    c.id = "X"; c.ev_dir = d; c.errores = []; c.archivos_producto = {archivo}
    return EC.evaluar_afirmacion(c, a)[0]


os.makedirs(os.environ.get("TMPDIR", tempfile.gettempdir()), exist_ok=True)
with tempfile.TemporaryDirectory() as tmp:
    for sp in sorted(glob.glob(os.path.join(D, "scripts", "especificaciones", "*", "Q1-*.json"))):
        s = json.load(open(sp, encoding="utf-8"))
        cid = s["id"]
        ev = os.path.join(D, "evidencias", cid)
        prod = {}      # archivo -> (indice de paso, op)
        for i, p in enumerate(s["pasos"]):
            if p.get("guardar"):
                prod[p["guardar"]] = (i, p["op"])
        comprobar_en_orden = [g for g, (i, op) in sorted(prod.items(), key=lambda x: x[1][0]) if op == "comprobar"]
        for cr in s["criterios"]:
            filas = []
            for k, a in enumerate(cr["afirma"]):
                res["aserciones"] += 1
                arch = a["archivo"]
                i, op = prod.get(arch, (None, None))
                pub = evaluar(tmp, arch, os.path.join(ev, arch), a) if os.path.isfile(os.path.join(ev, arch)) else None
                base = prev = None
                if op == "comprobar":
                    res["aserciones_sobre_comprobar"] += 1
                    base = evaluar(tmp, arch, BASE, a)
                    j = comprobar_en_orden.index(arch)
                    if j > 0:
                        prev = evaluar(tmp, arch, os.path.join(ev, comprobar_en_orden[j - 1]), a)
                filas.append({"n": k, "tipo": a["tipo"], "archivo": arch, "op": op, "publicada": pub, "BASE": base, "PREV": prev})
                if base:
                    pasan_base.append(f"{cid} {cr['id']}.{k} {a['tipo']} {arch}")
                if prev:
                    pasan_prev.append(f"{cid} {cr['id']}.{k} {a['tipo']} {arch}")
            solo_comprobar = all(f["op"] == "comprobar" for f in filas)
            for f in filas:
                f["REF"] = None if f["op"] != "comprobar" else (f["PREV"] if f["PREV"] is not None else f["BASE"])
            todo_ref = solo_comprobar and all(f["REF"] for f in filas)
            marcado = bool(cr.get("no_discriminante"))
            if todo_ref:
                no_disc_criterios.append({"caso": cid, "criterio": cr["id"], "texto": cr.get("texto", "")[:150],
                                          "pasa_integro_en": ["su estado previo de referencia: " + ", ".join(
                                              f"{f['n']}→{'PREV' if f['PREV'] is not None else 'BASE'}" for f in filas)],
                                          "marcado_no_discriminante": marcado,
                                          "cuenta_para_COMPONENTE_OK": not marcado})
            res["detalle"][f"{cid} {cr['id']}"] = {"no_discriminante_declarado": marcado, "aserciones": filas}

res["aserciones_que_pasan_en_BASE"] = pasan_base
res["aserciones_que_pasan_en_PREV"] = pasan_prev
res["CRITERIOS_que_pasan_integros_en_el_estado_previo"] = no_disc_criterios
res["CRITERIOS_no_discriminantes_SIN_MARCA_que_cuentan_como_CUMPLE"] = [
    f"{x['caso']} {x['criterio']} (pasa íntegro en {x['pasa_integro_en'][0]})" for x in no_disc_criterios if x["cuenta_para_COMPONENTE_OK"]]
res["prueba_34_del_autor"] = ("copia a `prev` solo los archivos de pasos ANTERIORES al que produce el archivo leído "
                              "(pruebas_arnes.py:449-456), así que el archivo leído nunca está y toda aserción falla por "
                              "'RUTA NO PERMITIDA': mal == [] siempre. Ver s05 (mutante B: Q1-027 C4 sin marca -> PASA igual).")
detalle = res.pop("detalle")
res["detalle"] = detalle
txt = json.dumps(res, ensure_ascii=False, indent=1)
open(OUT, "w").write(txt)
print(json.dumps({k: v for k, v in res.items() if k != "detalle"}, ensure_ascii=False, indent=1))
