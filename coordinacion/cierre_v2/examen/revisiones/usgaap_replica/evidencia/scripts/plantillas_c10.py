import sys, openpyxl
for ruta in sys.argv[1:]:
    try:
        wb = openpyxl.load_workbook(ruta, data_only=False)
    except Exception as e:
        print(ruta, "ERROR", e); continue
    if "Diagnóstico V6" not in wb.sheetnames:
        print(ruta, "sin Diagnóstico V6"); continue
    d = wb["Diagnóstico V6"]; p = wb["Palancas"]; m = wb["Motor"] if "Motor" in wb.sheetnames else None
    lb = wb.defined_names.get("Lista_Base")
    vals = None
    if lb is not None:
        for hoja, rng in lb.destinations:
            vals = [c.value for row in wb[hoja][rng] for c in row]
    dvs = [(str(dv.sqref), dv.formula1) for dv in p.data_validations.dataValidation if "C8" in str(dv.sqref).split()]
    print(ruta.split("/")[-1], "| C10:", d["C10"].value, "| C8:", repr(p["C8"].value), "| Lista_Base:", vals, "| DV:", dvs,
          "| D6:", m["D6"].value if m else None, "| H.C49:", wb["Historia"]["C49"].value)
