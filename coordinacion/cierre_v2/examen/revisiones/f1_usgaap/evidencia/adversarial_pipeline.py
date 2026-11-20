#!/usr/bin/env python3
"""Revisión R1 de F1 · US GAAP (revisor, no autor) · casos adversariales de EXTREMO A EXTREMO en el pipeline (LibreOffice).

Uso: flock /home/user/e_work/libreoffice.lock python3 -B adversarial_pipeline.py [SALIDA.txt] [caso …]
Reutiliza el montaje del autor (f1_usgaap/scripts/prueba_pipeline_usgaap.py: empresa sintética US GAAP, agentes simulados, plantilla
V6.3.1 F1) sobre la copia de revisión; directorio temporal. Lo nuevo son las declaraciones y lo que se mide:
  X0  control: tramos «fuera de las filas» (verdad), fila 14 sin partidas del arrendamiento.
  X1  (riesgo b) la variación del pasivo (2,5 al año) está dentro de la fila 14 y la declaración dice «fuera», con cita real.
  X2  «fila_8» falsa: se declara la amortización operativa (3,0 al año) dentro de la D&A, que no la lleva; A2 la excluye de D_X.
  X3  D-US1 («no_publicada»): cómo se presenta la cota en la ficha y en el informe.
  XB1 motor B con US GAAP, 50 de pasivo operativo en la fila 23 declarado: ¿termina en límite del modelo en el paso 7?
  XB2 motor B con US GAAP y la fila 23 a cero (pasivo operativo 0 declarado): ¿llega al final con F1 evaluado en los pasos 7 y 12?
  XB3 motor B con US GAAP y sin declaración F1: ¿pendiente_de_datos?
"""
import copy
import json
import os
import shutil
import sys
import tempfile

COPIA = os.environ.get("COPIA_REVISION", "/home/user/e_work/revision_usgaap/copia/munger_v2_r1")
PV = os.path.join(COPIA, "personaje_v2")
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(PV, "empresas_v2_correcciones", "2026-11_Vidrala_ensayo_4_15", "f1_usgaap", "scripts"))
import prueba_pipeline_usgaap as PU  # noqa: E402
TS, PF = PU.TS, PU.PF
import agentes_sinteticos as AG  # noqa: E402

SAL = []


def p(*a):
    t = " ".join(str(x) for x in a)
    SAL.append(t)
    print(t, flush=True)


def decl_fuera(per="A2_propio"):
    d = PU.declaracion()
    ev = {"documento": PU.DOC, "pagina": 1}
    d["arrendamientos_us_gaap"]["operativos"]["amortizacion_rou"] = dict(ev, cita="Operating lease cost", ubicacion="fuera_de_las_filas_8_y_14")
    d["arrendamientos_us_gaap"]["operativos"]["variacion_pasivo"] = dict(ev, cita="Operating lease liabilities", ubicacion="fuera_de_las_filas_8_y_14")
    return d


def decl_fila8(importe=3.0):
    d = decl_fuera()
    d["arrendamientos_us_gaap"]["operativos"]["amortizacion_rou"] = {"documento": PU.DOC, "pagina": 2, "cita": "Depreciation and amortization", "ubicacion": "fila_8"}
    d["series"]["da_rou_operativo"] = PU.serie({y: importe for y in range(2021, 2026)})
    return d


def reaccion_motor(motor):
    base = TS.reaccion_normal()

    def r(c, nombre):
        if nombre == "fase_a":
            AG.fase_a(c, motor=motor)
        else:
            base(c, nombre)
    return r


def preparar(nombre, d, circulante_extra=0.0, fila23=None, sin_decl=False):
    c = PU.preparar(nombre, d, circulante_extra=circulante_extra)
    if fila23 is not None:
        pth = os.path.join(c, "fase1_v63.json")
        f1 = json.load(open(pth, encoding="utf-8"))
        f1["historia"]["partidas"]["arrendamientos"]["valores"] = [fila23] * 10
        json.dump(f1, open(pth, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if sin_decl:
        os.remove(os.path.join(c, "motor_a_f1.json"))
    return c


def correr(c, motor="A", cfg=PU.CFG631):
    os.environ["MUNGER_CONFIG"] = cfg
    try:
        return TS.correr(c, reaccion_motor(motor))
    finally:
        os.environ.pop("MUNGER_CONFIG", None)


def informe_de(c, nombre):
    st, r, fi = TS.estado(c), PU.leer(c, "motor_a_f1_resultado.json"), PU.leer(c, "ficha.json")
    pr, res = PU.leer(c, "precio.json"), PU.leer(c, "resultados.json")
    cd = r.get("calculo_perimetro_declarado") or {}
    p(f"\n== {nombre}")
    p(f"   estado final: {st.get('estado_analisis')} · paso {st.get('paso')} · motor {st.get('motor')} · F1 en el paso {(st.get('motor_a_f1') or {}).get('paso')} · bloquean {PU.bloquean(r)}")
    p(f"   rótulo F1: {str(r.get('rotulo'))[:240]}")
    p(f"   f declarada {cd.get('f')} · flujo sin crecimiento {cd.get('flujo_sin_crecimiento')} · condicionada: {'sí' if r.get('condicionada') else 'no'} · K3b: {(r.get('K3') or {}).get('K3b_alquiler_contado')}")
    for gid in ("F1-US-FILAS", "F1-US-PUENTE", "F1-US-DESGLOSE", "F1-SERIES", "F1-LIBRO"):
        for x in r.get("guardas") or []:
            if x["id"] == gid and (x["salta"] or gid == "F1-US-FILAS"):
                p(f"   {gid} · salta {x['salta']} · {x.get('severidad')} · {str(x['detalle'])[:230]}")
    claves = {k: pr.get(k) for k in ("precio_de_si", "ponderado", "valor_ponderado", "escenarios", "sin_lectura") if k in pr}
    p(f"   precio.json: {json.dumps(claves, ensure_ascii=False)[:420]}")
    p(f"   ficha: estado {fi.get('estado_analisis')} · cubo {fi.get('cubo')} · precio de Sí {fi.get('precio_de_si')}")
    return st, r, fi, pr


def main():
    args = sys.argv[1:]
    salida = args[0] if args and args[0].endswith(".txt") else None
    casos = set(a for a in args if not a.endswith(".txt")) or {"X0", "X1", "X2", "X3", "XB1", "XB2", "XB3"}
    base0, TS.BASE = TS.BASE, tempfile.mkdtemp(prefix="rev_usgaap_pipe_")
    guardar = os.environ.get("GUARDAR_EN")
    try:
        ref = {}
        if "X0" in casos:
            c = preparar("EmpresaX_X0", decl_fuera())
            rc, out = correr(c)
            ref["X0"] = informe_de(c, "X0 · control: tramos «fuera» (verdad); fila 14 sin partidas del arrendamiento")
        if "X1" in casos:
            c = preparar("EmpresaX_X1", decl_fuera(), circulante_extra=2.5)
            rc, out = correr(c)
            ref["X1"] = informe_de(c, "X1 · (b) la variación del pasivo (2,5 al año) está dentro de la fila 14 y se declara «fuera» con cita real; sin fase1_partes")
        if "X2" in casos:
            c = preparar("EmpresaX_X2", decl_fila8(3.0))
            rc, out = correr(c)
            ref["X2"] = informe_de(c, "X2 · «fila_8» falsa: da_rou_operativo = 3,0 declarado dentro de una D&A que no lo lleva (cita «Depreciation and amortization»)")
        if "X3" in casos:
            c = preparar("EmpresaX_X3", PU.declaracion())
            rc, out = correr(c)
            st, r, fi, pr = informe_de(c, "X3 · D-US1 («no_publicada»): presentación de la cota")
            f1b = fi.get("motor_a_f1") or {}
            cota = (f1b.get("condicionada") or {}).get("cota") or {}
            p(f"   ficha.motor_a_f1.condicionada.cota: {json.dumps(cota, ensure_ascii=False)[:900]}")
            inf = open(os.path.join(c, "informe.md"), encoding="utf-8").read() if os.path.exists(os.path.join(c, "informe.md")) else ""
            linea = next((x for x in inf.splitlines() if "· F1:" in x), "")
            p(f"   informe.md, línea F1: {linea[:900]}")
            p(f"   ¿el informe lleva alguna cifra de la cota («mm» o «%» junto a la hipótesis)?: {'sí' if ('Cota' in inf or 'cota' in inf) else 'no'} · menciones de «cota» en informe.md: {inf.lower().count('cota')}")
            if guardar:
                os.makedirs(guardar, exist_ok=True)
                for n in ("informe.md", "ficha.json", "motor_a_f1_resultado.md", "motor_a_f1_resultado.json"):
                    if os.path.exists(os.path.join(c, n)):
                        shutil.copy(os.path.join(c, n), os.path.join(guardar, "X3_" + n))
        if {"X0", "X1"} <= set(ref) or {"X0", "X2"} <= set(ref):
            p("\n== comparación de valor (mismo FCF base, mismas palancas simuladas)")
            for k in ("X0", "X1", "X2"):
                if k in ref:
                    st, r, fi, pr = ref[k]
                    cd = r.get("calculo_perimetro_declarado") or {}
                    p(f"   {k}: estado {st.get('estado_analisis')} · f {cd.get('f')} · flujo sin crecimiento {cd.get('flujo_sin_crecimiento')} · precio de Sí (ficha) {fi.get('precio_de_si')} · precio.json {pr.get('precio_de_si')}")
        if "XB1" in casos:
            d = PU.declaracion()
            c = preparar("EmpresaX_XB1", d)
            rc, out = correr(c, motor="B")
            informe_de(c, "XB1 · motor B con US GAAP y 50 de pasivo operativo en la fila 23 (declarado)")
        if "XB2" in casos:
            d = PU.declaracion()
            d["series"]["pasivo_arr_operativo"] = PU.serie({2025: 0})
            c = preparar("EmpresaX_XB2", d, fila23=0)
            rc, out = correr(c, motor="B")
            st, r, fi, pr = informe_de(c, "XB2 · motor B con US GAAP, fila 23 a cero y pasivo operativo 0 declarado")
            p(f"   código {rc} · detalle: {str(out)[-300:]}")
            inf = open(os.path.join(c, "informe.md"), encoding="utf-8").read() if os.path.exists(os.path.join(c, "informe.md")) else ""
            p(f"   informe.md, línea F1: {next((x for x in inf.splitlines() if '· F1:' in x), '')[:500]}")
            v = PU.leer(c, "ficha.json").get("motor_a_f1") or {}
            p(f"   ficha.motor_a_f1.vigencia: {json.dumps(v.get('vigencia'), ensure_ascii=False)}")
        if "XB3" in casos:
            c = preparar("EmpresaX_XB3", PU.declaracion(), sin_decl=True)
            rc, out = correr(c, motor="B")
            informe_de(c, "XB3 · motor B con US GAAP y sin declaración F1")
    finally:
        shutil.rmtree(TS.BASE, ignore_errors=True)
        TS.BASE = base0
    if salida:
        open(salida, "a", encoding="utf-8").write("\n".join(SAL) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
