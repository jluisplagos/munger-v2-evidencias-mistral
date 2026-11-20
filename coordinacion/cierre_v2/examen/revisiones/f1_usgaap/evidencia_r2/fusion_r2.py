#!/usr/bin/env python3
"""Revisión R2 (revisor) · árbol FUSIONADO en una carpeta temporal: motor_a_f1.py de f1/usgaap @ bcb6dc3 fusionado a tres bandas (git merge-file, sin
conflictos) con el de f1/series-escala @ b3998a8 (base común 1694f08). No se escribe nada en el repositorio.

  M1 · Zoetis real (examen): el principal de 2023, impreso «—», ¿se puede declarar ya?
  M2 · el camino del «importe cero» con las vías nuevas de la otra rama: un tramo contrastado dentro de la fila 14 (línea propia sumada, 10 al año)
       declarado con importe 0 por «cero_comprobado» (una frase cualquiera de la página, de 8 palabras o más) → ¿concluye sin condición?
Uso: COPIA_REVISION=<árbol fusionado> python3 -B fusion_r2.py [SALIDA.txt]
"""
import copy
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ayudas2  # noqa: E402

A = ayudas2.cargar()
M, libro, libro_v631, decl, serie, expediente = A["M"], A["libro"], A["libro_v631"], A["decl"], A["serie"], A["expediente"]
DOC, ANIOS = A["DOC"], A["ANIOS"]
SAL, TMP = [], []


def p(*a):
    t = " ".join(str(x) for x in a)
    SAL.append(t)
    print(t, flush=True)


p(f"motor_a_f1.py evaluado: {M.__file__}")
p(f"¿lleva las dos ramas?: D-US2 bis {'sí' if 'D-US2 bis' in M.DECISIONES_US else 'no'} · ceros sin dígitos {'sí' if hasattr(M, 'CEROS_IMPRESOS') else 'no'}")

# ---- M1 · Zoetis real
import importlib.util  # noqa: E402
spec = importlib.util.spec_from_file_location("zr", os.path.join(os.path.dirname(os.path.abspath(__file__)), "zoetis_real_r2.py"))
zr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(zr)
Lz = M.leer_libro(os.path.join(zr.Z, "recalc", "Zoetis_v63_datos.xlsx"))
cz = zr.carpeta()
try:
    r = M.evaluar(Lz, zr.declaracion(), carpeta=cz, motor_libro="A")
    fs = r.get("F1_SERIES") or {}
    bl = sorted({x["id"] for x in r["guardas"] if x["salta"] and x["severidad"] == "BLOQUEA"})
    p(f"\n== M1 · Zoetis real, principal de 2023 declarado «—» (fila «Financing cash flows – finance leases», página 89)")
    p(f"   F1-SERIES · inválidas: {fs.get('invalidas')} · incompletas: {fs.get('incompletas')} · columna pendiente: {len(fs.get('columna_pendiente') or [])}")
    p(f"   pendientes que nombran el cero: {[x[:200] for x in (fs.get('columna_pendiente') or []) if 'cero' in x or '—' in x]}")
    p(f"   bloquean: {bl} (F1-K3a: fila 17 de 2025 vacía en la fase 1 real; F1-LIBRO: el libro aún no lleva la declaración) · condicionada: {(r.get('condicionada') or {}).get('hipotesis')}")
finally:
    shutil.rmtree(os.path.dirname(cz), ignore_errors=True)

# ---- M2 · importe cero por «cero_comprobado»
L = libro_v631(libro(da=20.0, dwc=10.0, palancas=False), "A2_propio", 0.0)
FRASE = "The Company leases office space under non-cancellable operating lease agreements"
d = decl("A2_propio", ub_pas="fila_14", ajuste=None)
d["series"]["circulante_arr_operativo"] = {str(y): {"valor_fuente": 0, "signo": 1, "tratamiento": "ninguno", "documento": DOC, "pagina": 1,
                                                    "cero_comprobado": {"motivo": "sin importe dentro de la fila 14", "cita": FRASE}} for y in range(2021, 2026)}
c = expediente(d, verdad=("fuera", "fila_14"), notas=(FRASE,))
TMP.append(c)
try:
    r = M.evaluar(L, d, carpeta=c)
    bl = sorted({x["id"] for x in r["guardas"] if x["salta"] and x["severidad"] == "BLOQUEA"})
    cd = r.get("calculo_perimetro_declarado") or {}
    tr = (((r.get("us_gaap") or {}).get("contraste_de_ubicaciones") or {}).get("tramos") or {})
    fs = r.get("F1_SERIES") or {}
    p("\n== M2 · «Operating lease liabilities» (10 al año) sumada en la fila 14 y contrastada; importe declarado 0 con «cero_comprobado» (frase de las notas)")
    p(f"   utilizable: {r['utilizable_para_conclusion']} · condicionada: {(r.get('condicionada') or {}).get('hipotesis')} · bloquean: {bl} · flujo {cd.get('flujo_sin_crecimiento')} (correcto 68) · "
      f"contraste { {k: v.get('estado') for k, v in tr.items()} } · K3b {(r.get('K3') or {}).get('K3b_alquiler_contado')} (contrastado: {(r.get('K3') or {}).get('K3b_contrastado')})")
    p(f"   F1-SERIES · inválidas: {fs.get('invalidas')} · incompletas: {fs.get('incompletas')} · pendientes: {[x[:150] for x in (fs.get('columna_pendiente') or [])][:2]}")
    p(f"   rótulo: {str(r.get('rotulo'))[:200]}")
finally:
    for t in TMP:
        shutil.rmtree(t, ignore_errors=True)
if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8").write("\n".join(SAL) + "\n")
