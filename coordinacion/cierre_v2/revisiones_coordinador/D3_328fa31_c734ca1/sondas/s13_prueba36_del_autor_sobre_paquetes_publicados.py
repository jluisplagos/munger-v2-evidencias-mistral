"""D3-R4 · La prueba 36 del propio autor (pruebas_arnes.py:488-505, c734ca1), copiada literalmente,
aplicada a relevo/PAQUETES_RELEVO.json publicado. En el arnés del autor no llega a ejecutarse:
pruebas_arnes.py aborta antes (s03, s04).

Uso: python3 -I -B s13_... <ejecucion_d @c734ca1> <salida.json>
"""
import collections, json, os, sys
D, OUT = [os.path.abspath(x) for x in sys.argv[1:3]]
doc = json.load(open(os.path.join(D, "relevo", "PAQUETES_RELEVO.json"), encoding="utf-8"))
mal = []
for p in doc["paquetes"]:                                    # --- copia literal de la prueba 36 ---
    for clave in ("estado_inicial", "fases", "entrada", "artefacto_por_criterio"):
        if not p.get(clave):
            mal.append(f"{p['caso']} sin {clave}")
    if not p.get("comando_relevo") and not p.get("motivo_sin_comando"):
        mal.append(f"{p['caso']} sin comando_relevo ni motivo")
    for cb in p.get("criterios_banco", []):
        if not cb.get("artefacto"):
            mal.append(f"{p['caso']} criterio {cb.get('indice')} sin artefacto")
ok = not mal                                                 # --- fin de la copia ---
por_tipo = collections.Counter("criterio del banco sin artefacto" if " criterio " in m else " ".join(m.split()[1:3]) for m in mal)
ps = doc["paquetes"]
res = {"prueba_36": "PASA" if ok else "FALLA", "incumplimientos": len(mal), "por_tipo": dict(por_tipo),
       "paquetes": len(ps), "programa_declarado_en_el_paquete": doc["programa"],
       "paquetes_con_las_4_claves": sum(1 for p in ps if all(p.get(k) for k in ("estado_inicial", "fases", "entrada", "artefacto_por_criterio"))),
       "comando_relevo_null": [p["caso"] for p in ps if not p.get("comando_relevo")],
       "comando_relevo_es_el_del_componente": sum(1 for p in ps if (p.get("comando_relevo") or "").startswith("python3 scripts/ejecutar_caso.py")),
       "textos_que_distintos_en_falta_para_caso_completo": len(set(f["qué"] for p in ps for f in p["falta_para_caso_completo"])),
       "paquetes_con_el_mismo_texto_generico_de_agente": sum(1 for p in ps if any(f["qué"].startswith("recorrido del personaje con agente real") for f in p["falta_para_caso_completo"])),
       "Q1-028": {k: next(p for p in ps if p["caso"] == "Q1-028")[k] for k in ("comando_relevo", "motivo_sin_comando", "falta_para_caso_completo")},
       "Q1-032": {k: next(p for p in ps if p["caso"] == "Q1-032")[k] for k in ("comando_relevo", "motivo_sin_comando", "falta_para_caso_completo")}}
open(OUT, "w").write(json.dumps(res, ensure_ascii=False, indent=1)); print(json.dumps(res, ensure_ascii=False, indent=1))
