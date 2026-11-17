#!/usr/bin/env python3
"""Sonda propia del contraste (Mistral R): consistencia de CONTROL.json con los informes
de revisión enlazados en solicitud_revision.informe_revision.

Uso: python3 -I control_consistency.py <ruta a CONTROL.json>
Solo lectura. La clase del veredicto se toma del comienzo del texto: empieza por
"CORRECCIONES" -> CORRECCIONES; contiene "CONFORME CON L"/"CONFORME_CON_LIMITES" ->
CONFORME_CON_LIMITES; empieza por "CUMPLE" -> EXTERNO(CUMPLE); si no, "(sin clase
explícita)" y no se juzga. DISCREPANCIA solo si la clase explícita difiere del campo
`revision` de la tarea.
"""
import json, re, sys

d = json.load(open(sys.argv[1], encoding="utf-8"))
for t in d.get("tareas", []):
    sr = t.get("solicitud_revision")
    if not sr or sr.get("estado") != "RESPONDIDA":
        continue
    inf = sr.get("informe_revision") or {}
    verdict = (inf.get("veredicto") or "")
    campo = t.get("revision")
    vu = verdict.upper()
    if vu.startswith("CORRECCIONES"):
        clase = "CORRECCIONES"
    elif "CONFORME CON L" in vu or "CONFORME_CON_LIMITES" in vu:
        clase = "CONFORME_CON_LIMITES"
    elif vu.startswith("CUMPLE"):
        clase = "EXTERNO(CUMPLE)"
    else:
        clase = "(sin clase explícita)"
    ok = (clase == campo) or clase.startswith("EXTERNO") or clase.startswith("(sin")
    print(f"{t['id']:10s} revision={campo:22s} veredicto~{clase:20s} "
          f"ruta={inf.get('ruta','')} -> {'OK' if ok else 'DISCREPANCIA'}")
    if not ok:
        print(f"    veredicto textual: {verdict[:200]}")
