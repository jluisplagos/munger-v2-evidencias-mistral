#!/usr/bin/env python3
"""Revisión R2 de F1 · US GAAP (revisor, no autor). Ayudas comunes de los casos de la ronda 2.

Carga las ayudas de la batería del autor de la RONDA 2 (libro, decl, serie, expediente, ev_…) ejecutando solo la cabecera de
personaje_v2/pruebas/test_motor_a_f1_usgaap.py (hasta el primer bloque de pruebas) sobre la copia de revisión de bcb6dc3. Los libros
sintéticos, las declaraciones y los expedientes (texto/ + fase1_partes, con la VERDAD separada de lo DECLARADO) son los del autor; lo
único nuevo son los casos. No toca la rama. Los temporales van a la carpeta de trabajo del revisor (TMPDIR), no a /tmp.
"""
import os
import sys
import tempfile

COPIA = os.environ.get("COPIA_REVISION", "/home/user/e_work/revision_usgaap/copia2/munger_v2_r1")   # árbol munger_v2_r1 que se examina (la copia de revisión se borró al acabar: pásese el propio)
PV = os.path.join(COPIA, "personaje_v2")
TMP_R2 = os.environ.get("TMP_R2") or os.path.join(tempfile.gettempdir(), "rev_f1_usgaap_r2")
os.makedirs(TMP_R2, exist_ok=True)
tempfile.tempdir = TMP_R2
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(PV, "scripts"))


def cargar():
    ruta = os.path.join(PV, "pruebas", "test_motor_a_f1_usgaap.py")
    src = open(ruta, encoding="utf-8").read()
    corte = src.index("# ================================================================== N ·")
    cab = src[:corte].replace("AQUI = os.path.dirname(os.path.abspath(__file__))", f"AQUI = {os.path.join(PV, 'pruebas')!r}")
    ns = {"__name__": "ayudas_autor_r2", "__file__": ruta}
    exec(compile(cab, ruta, "exec"), ns)
    return ns


def resumen(r, ns):
    """Una línea con lo esencial de una evaluación: rótulo corto, flujo sin crecimiento, guardas que bloquean, condición y estados del contraste."""
    blo = ns["bloquean"](r)
    f0 = None
    try:
        f0 = ns["F0"](r)
    except Exception:  # noqa: BLE001
        pass
    cond = r.get("condicionada")
    tr = (((r.get("us_gaap") or {}).get("contraste_de_ubicaciones") or {}).get("tramos") or {})
    est = {k: v.get("estado") for k, v in tr.items()}
    return {"utilizable": r.get("utilizable_para_conclusion"), "estado_propuesto": r.get("estado_propuesto"), "F0": None if f0 is None else round(f0, 4),
            "bloquean": blo, "condicionada": (cond or {}).get("hipotesis"), "cota_mm": ((cond or {}).get("cota") or {}).get("resumen", {}).get("flujo_sin_crecimiento_mm") if cond else None,
            "tramos": est, "K3b": (r.get("K3") or {}).get("K3b_alquiler_contado"), "K3b_contrastado": (r.get("K3") or {}).get("K3b_contrastado")}
