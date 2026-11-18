#!/usr/bin/env python3
"""Revisión R2 de F1 · US GAAP (revisor, no autor) · casos propios de EXTREMO A EXTREMO en el pipeline (LibreOffice).

Uso: flock /home/user/e_work/libreoffice.lock python3 -B pipeline_r2.py [SALIDA.txt] [caso …]
Reutiliza el montaje del autor de la ronda 2 (f1_usgaap/scripts/prueba_pipeline_usgaap.py: empresa sintética US GAAP, agentes simulados, plantilla
V6.3.1 F1, fuente en texto/ y fase1_partes) sobre la copia de revisión de bcb6dc3; directorio temporal propio. Lo nuevo son las declaraciones.
En la empresa sintética el alquiler es pequeño (pagos ≈ 3,2 al año frente a un flujo ≈ 148): los porcentajes son pequeños y proporcionales a su peso.

  Y0  control: los dos tramos son líneas propias NO sumadas y se declaran «fuera» citándolas → concluido sin condición.
  ALTAS de la ronda 1, repetidas tal como las ejecuté entonces:
  Y1  (R1-3 i · X1) la variación del pasivo (2,5 al año) está dentro de la fila 14; se declara «fuera» con cita real de una nota; sin fase1_partes.
  Y2  (R1-3 ii · X2) «fila_8» falsa: da_rou_operativo = 3,0 con la cita genérica «Depreciation and amortization».
  Y3  (R1-3 iii) solo el pasivo está dentro de la fila 14 y se declaran los dos «fila_14».
  Y8  (R1-1 · XB3) motor B, libro US GAAP y sin declaración F1.
  Caminos nuevos de esta ronda:
  Y4  línea señuelo: el pasivo (2,5) va dentro de «Accrued and other liabilities» (fila 14); el estado de flujos lleva «Loss on lease termination»
      (no sumada) y los dos tramos se declaran «fuera» citándola.
  Y4h lo mismo con la declaración VERAZ («no_publicada» los dos).
  Y5  importe cero: la línea propia «Operating lease liabilities» (2,5 al año) está sumada en la fila 14, se declara «fila_14» (contrastada) con
      importe 0; la amortización, «fuera» con su línea propia.
  Decisiones:
  Y7  D-WM: financieros «no_publicado» (como deuda), con caja pagada y gasto total → ¿concluido CONDICIONADA y la diferencia estimada en la ficha y el informe?
  Y9  motor B con «Otro» en la norma de la fase 1 (límite nuevo: no concluye).
  Y10 control NIIF con el motor B (no debe exigirse F1 ni cambiar nada).
"""
import json
import os
import shutil
import sys
import tempfile

COPIA = os.environ.get("COPIA_REVISION", "/home/user/e_work/revision_usgaap/copia2/munger_v2_r1")
PV = os.path.join(COPIA, "personaje_v2")
TMP_R2 = os.environ.get("TMP_R2") or os.path.join(tempfile.gettempdir(), "rev_f1_usgaap_r2")
os.makedirs(TMP_R2, exist_ok=True)
tempfile.tempdir = TMP_R2
os.environ["TMPDIR"] = TMP_R2
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(PV, "empresas_v2_correcciones", "2026-11_Vidrala_ensayo_4_15", "f1_usgaap", "scripts"))
import prueba_pipeline_usgaap as PU  # noqa: E402
TS, PF, DOC = PU.TS, PU.PF, PU.DOC
sys.path.insert(0, os.path.join(PV, "scripts"))
import motor_a_f1 as M  # noqa: E402
import cierre_v2 as CIE  # noqa: E402

SAL = []
L_AM, L_PAS, SEN = "Non-cash lease expense", "Operating lease liabilities", "Loss on lease termination"


def p(*a):
    t = " ".join(str(x) for x in a)
    SAL.append(t)
    print(t, flush=True)


def ub(u, cita, pagina=2):
    return {"ubicacion": u, "documento": DOC, "pagina": pagina, "cita": cita}


FUERA = "fuera_de_las_filas_8_y_14"


def informe_de(c, nombre):
    st, r, fi = TS.estado(c), PU.leer(c, "motor_a_f1_resultado.json"), PU.leer(c, "ficha.json")
    pr, dg = PU.leer(c, "precio.json"), PU.leer(c, "diagnostico.json")
    cd = r.get("calculo_perimetro_declarado") or {}
    cond = r.get("condicionada") or {}
    tr = (((r.get("us_gaap") or {}).get("contraste_de_ubicaciones") or {}).get("tramos") or {})
    p(f"\n== {nombre}")
    p(f"   estado final: {st.get('estado_analisis')} · paso {st.get('paso')} · motor {st.get('motor')} · F1 en el paso {(st.get('motor_a_f1') or {}).get('paso')} · bloquean {PU.bloquean(r)}")
    if st.get("estado_analisis") != "concluido":
        p(f"   causa: {str((dg.get('causa') or {}).get('tipo'))} · {str((dg.get('causa') or {}).get('detalle'))[:330]}")
    p(f"   rótulo F1: {str(r.get('rotulo'))[:260]}")
    p(f"   flujo sin crecimiento {cd.get('flujo_sin_crecimiento')} · condicionada: {cond.get('hipotesis') if cond else 'no'} · contraste "
      f"{ {k: v.get('estado') for k, v in tr.items()} } · K3b: {(r.get('K3') or {}).get('K3b_alquiler_contado')} (contrastado: {(r.get('K3') or {}).get('K3b_contrastado')})")
    if cond:
        p(f"   cota: {((cond.get('cota') or {}).get('resumen') or {}).get('texto')}")
    claves = {k: pr.get(k) for k in ("precio_de_si", "ponderado", "valor_ponderado", "sin_lectura") if k in pr}
    p(f"   precio.json: {json.dumps(claves, ensure_ascii=False)[:300]} · ficha: estado {fi.get('estado_analisis')} · precio de Sí {fi.get('precio_de_si')}")
    lin = PU.linea_f1(c)
    if lin:
        p(f"   informe.md, línea F1: {lin[:700]}")
    return st, r, fi, pr


def main():
    args = sys.argv[1:]
    salida = args[0] if args and args[0].endswith(".txt") else None
    casos = [a for a in args if not a.endswith(".txt")] or ["Y0", "Y1", "Y2", "Y3", "Y4", "Y4h", "Y5", "Y7", "Y8", "Y9", "Y10"]
    base0, TS.BASE = TS.BASE, tempfile.mkdtemp(prefix="rev2_usgaap_pipe_")
    ref = {}
    try:
        for caso in casos:
            if caso == "Y0":
                d = PU.declaracion()
                op = d["arrendamientos_us_gaap"]["operativos"]
                op["amortizacion_rou"], op["variacion_pasivo"] = ub(FUERA, L_AM), ub(FUERA, L_PAS)
                c = PU.preparar("EmpresaX_Y0", d, fuera=(L_AM, L_PAS), partes=True)
                PU.correr(c)
                ref[caso] = informe_de(c, "Y0 · control: los dos tramos son líneas propias no sumadas, declarados «fuera» citándolas")
            elif caso == "Y1":
                d = PU.declaracion()
                op = d["arrendamientos_us_gaap"]["operativos"]
                op["amortizacion_rou"], op["variacion_pasivo"] = ub(FUERA, "Operating lease cost", 1), ub(FUERA, L_PAS, 1)
                c = PU.preparar("EmpresaX_Y1", d, circulante_extra=2.5, notas=(L_PAS,))
                PU.correr(c)
                ref[caso] = informe_de(c, "Y1 · (R1-3 i · X1 de la ronda 1) pasivo 2,5 al año dentro de la fila 14, declarado «fuera» con cita real de una nota; sin fase1_partes")
            elif caso == "Y2":
                d = PU.declaracion()
                op = d["arrendamientos_us_gaap"]["operativos"]
                op["amortizacion_rou"] = ub("fila_8", "Depreciation and amortization")
                op["variacion_pasivo"] = ub(FUERA, L_PAS)
                d["series"]["da_rou_operativo"] = PU.serie({y: 3.0 for y in range(2016, 2026)})
                c = PU.preparar("EmpresaX_Y2", d, fuera=(L_PAS,), partes=True)
                PU.correr(c)
                ref[caso] = informe_de(c, "Y2 · (R1-3 ii · X2 de la ronda 1) «fila_8» falsa: 3,0 al año con la cita genérica «Depreciation and amortization»")
            elif caso == "Y3":
                d = PU.declaracion()
                op = d["arrendamientos_us_gaap"]["operativos"]
                op["amortizacion_rou"], op["variacion_pasivo"] = ub("fila_14", L_PAS), ub("fila_14", L_PAS)
                c = PU.preparar("EmpresaX_Y3", d, circulante_extra=2.5, wc=PU.WC + (L_PAS,), partes=True)
                PU.correr(c)
                ref[caso] = informe_de(c, "Y3 · (R1-3 iii) solo el pasivo dentro de la fila 14; declarados los dos «fila_14» (la amortización, con la cita de la línea del pasivo)")
            elif caso in ("Y4", "Y4h"):
                d = PU.declaracion()
                op = d["arrendamientos_us_gaap"]["operativos"]
                if caso == "Y4":
                    op["amortizacion_rou"], op["variacion_pasivo"] = ub(FUERA, SEN), ub(FUERA, SEN)
                c = PU.preparar("EmpresaX_" + caso, d, circulante_extra=2.5, wc=PU.WC + ("Accrued and other liabilities",), fuera=(SEN,), partes=True)
                PU.correr(c)
                ref[caso] = informe_de(c, ("Y4 · línea señuelo: pasivo 2,5 al año dentro de «Accrued and other liabilities» (fila 14); los dos tramos «fuera» citando «Loss on lease termination»"
                                           if caso == "Y4" else "Y4h · lo mismo con la declaración VERAZ: los dos tramos «no_publicada»"))
            elif caso == "Y5":
                d = PU.declaracion(ub_pas="fila_14", ajuste=0)
                d["arrendamientos_us_gaap"]["operativos"]["amortizacion_rou"] = ub(FUERA, L_AM)
                c = PU.preparar("EmpresaX_Y5", d, circulante_extra=2.5, wc=PU.WC + (L_PAS,), fuera=(L_AM,), partes=True)
                PU.correr(c)
                ref[caso] = informe_de(c, "Y5 · importe cero: «Operating lease liabilities» (2,5 al año) sumada en la fila 14, declarada «fila_14» (contrastada) con importe 0")
            elif caso == "Y7":
                d = PU.declaracion(financieros=True)
                fin = d["arrendamientos_us_gaap"]["financieros"]
                fin.update({"cita": "Finance lease cost", "desglose": "no_publicado"})
                d["series"]["caja_pagada_arr_financiero"] = PU.serie({2023: 0.6, 2024: 0.9, 2025: 1.01})
                d["series"]["gasto_arr_financiero"] = PU.serie({2023: 0.58, 2024: 0.73, 2025: 0.96})
                c = PU.preparar("EmpresaX_Y7", d, notas=("Finance lease cost",))
                PU.correr(c)
                st, r, fi, pr = ref[caso] = informe_de(c, "Y7 · D-WM: financieros «no_publicado» (como deuda), caja pagada 0,60/0,90/1,01 y gasto total 0,58/0,73/0,96")
                f1b = fi.get("motor_a_f1") or {}
                de = (((f1b.get("us_gaap") or {}).get("D_WM") or {}).get("diferencia_estimada") or {})
                p(f"   ficha.motor_a_f1.us_gaap.D_WM.diferencia_estimada: caja − gasto = {de.get('caja_pagada_menos_gasto_total_medio_mm')} · % de CFO − capex: {de.get('%_de_CFO_menos_capex_medio (Análisis C46 − C47)')}")
                p(f"   ¿la línea F1 del informe nombra D-WM y la diferencia estimada?: D-WM {'sí' if 'D-WM' in PU.linea_f1(c) else 'NO'} · «diferencia estimada» {'sí' if 'diferencia estimada' in PU.linea_f1(c) else 'NO'}")
            elif caso == "Y8":
                c = PU.preparar("EmpresaX_Y8", PU.declaracion(), sin_decl=True)
                PU.correr(c, motor="B")
                st, r, fi, pr = ref[caso] = informe_de(c, "Y8 · (R1-1 · XB3 de la ronda 1) motor B, libro US GAAP y SIN declaración F1")
                v = M.vigencia(c, motor="B")
                p(f"   vigencia(motor B): exigido {v.get('exigido')} · vigente {v.get('vigente')} · utilizable {v.get('utilizable')} · {v.get('motivo')}")
                p(f"   objeción F1 del cierre a un «concluido»: {str(CIE.motivo_f1(c, dict(st, estado_analisis='concluido')))[:220]}")
                p(f"   ¿existe motor_a_f1_resultado.json?: {os.path.exists(os.path.join(c, 'motor_a_f1_resultado.json'))} · ¿fase_b.json?: {os.path.exists(os.path.join(c, 'fase_b.json'))}")
            elif caso == "Y9":
                d = PU.declaracion()
                c = PU.preparar("EmpresaX_Y9", d, norma="Otro", sin_decl=True)
                PU.correr(c, motor="B")
                ref[caso] = informe_de(c, "Y9 · motor B con «Otro» en la norma de la fase 1, expediente 4.15, sin declaración F1 (límite nuevo)")
            elif caso == "Y10":
                c = TS.preparar("EmpresaX_Y10")
                json.dump({"modo": "registrada", "motivo": "control NIIF de la revisión R2"}, open(os.path.join(c, "entrada_efectiva.json"), "w", encoding="utf-8"))
                os.environ["MUNGER_CONFIG"] = PU.CFG631
                try:
                    TS.correr(c, PU.reaccion_motor("B"))
                finally:
                    os.environ.pop("MUNGER_CONFIG", None)
                st = TS.estado(c)
                p("\n== Y10 · control NIIF con el motor B, expediente 4.15 (la empresa sintética tal cual, norma IFRS)")
                p(f"   estado final: {st.get('estado_analisis')} · paso {st.get('paso')} · motor {st.get('motor')} · registro F1 en el estado: {st.get('motor_a_f1')} · "
                  f"¿motor_a_f1_resultado.json?: {os.path.exists(os.path.join(c, 'motor_a_f1_resultado.json'))}")
                v = M.vigencia(c, motor="B")
                p(f"   vigencia(motor B): exigido {v.get('exigido')} · {v.get('motivo')}")
        if "Y0" in ref:
            p("\n== comparación de valor con el control Y0 (mismo FCF base y mismas palancas simuladas)")
            f0 = (ref["Y0"][1].get("calculo_perimetro_declarado") or {}).get("flujo_sin_crecimiento")
            for k in ("Y0", "Y1", "Y4", "Y4h", "Y5"):
                if k in ref:
                    st, r, fi, pr = ref[k]
                    cd = r.get("calculo_perimetro_declarado") or {}
                    fk = cd.get("flujo_sin_crecimiento")
                    p(f"   {k}: estado {st.get('estado_analisis')} · condicionada {'sí' if r.get('condicionada') else 'no'} · flujo sin crecimiento {fk}"
                      + (f" ({fk - f0:+.3f} frente a Y0)" if (fk is not None and f0 is not None) else "") + f" · precio de Sí (ficha) {fi.get('precio_de_si')} · "
                      f"precio.json {json.dumps({q: pr.get(q) for q in ('precio_de_si', 'ponderado', 'valor_ponderado') if q in pr}, ensure_ascii=False)[:160]}")
    finally:
        shutil.rmtree(TS.BASE, ignore_errors=True)
        TS.BASE = base0
    if salida:
        open(salida, "a", encoding="utf-8").write("\n".join(SAL) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
