import sys
sys.path.insert(0, sys.argv[1])
import fase1_historia as F
casos = [
 ("Zoetis exacto, unidades", {"valor": 424.927535, "impreso": "424.927.535", "unidad": "unidades"}),
 ("coma de miles", {"valor": 424.927535, "impreso": "424,927,535"}),
 ("unidad de Ahold «millones de acciones» con impreso", {"valor": 886.877259, "impreso": "886,877,259", "unidad": "millones de acciones"}),
 ("unidad sin impreso (Ahold hoy)", {"valor": 886.877259, "unidad": "millones de acciones"}),
 ("millones con 3 decimales «424.928»", {"valor": 424.928, "impreso": "424.928", "unidad": "millones"}),
 ("millones con 1 decimal «424,9»", {"valor": 424.9, "impreso": "424,9", "unidad": "millones"}),
 ("miles «886,877» (AR Ahold)", {"valor": 886.877, "impreso": "886,877", "unidad": "miles"}),
 ("con dilución sumada (outstanding + 4 M)", {"valor": 428.927535, "impreso": "424.927.535"}),
 ("valor texto", {"valor": "424.927535", "impreso": "424.927.535"}),
 ("valor entero 905 con impreso 905 millones", {"valor": 905, "impreso": "905", "unidad": "millones"}),
 ("impreso vacío", {"valor": 1, "impreso": ""}),
 ("impreso negativo", {"valor": -1, "impreso": "(1)", "unidad": "millones"}),
 ("unidad None explícita", {"valor": 424.927535, "impreso": "424.927.535", "unidad": None}),
]
for n, ac in casos:
    print(f"{n}: {F.defecto_acciones_meta(ac) or 'sin defecto'}")
