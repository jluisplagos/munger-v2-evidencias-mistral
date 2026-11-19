import sys, openpyxl, json, os, glob
for ruta in sys.argv[1:]:
    try:
        wb = openpyxl.load_workbook(ruta, data_only=True, read_only=True)
        p = wb["Palancas"]; d = wb["Diagnóstico V6"]; h = wb["Historia"]
        c8 = p["C8"].value; c10 = d["C10"].value; c5 = d["C5"].value; c48 = h["C48"].value; c49 = h["C49"].value; l4 = wb["Control maestro"]["L4"].value
        print(f"{ruta.split('empresas_v2_correcciones/')[-1]} | motor {c5} | C8 {c8!r} | C10 {c10} | C48 {c48} | C49 {c49} | L4 {l4!r}")
        wb.close()
    except Exception as e:
        print(ruta, "ERROR", type(e).__name__, e)
