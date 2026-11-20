import copy, hashlib, json, os, sys, tempfile
W = "/tmp/claude-0/revision_v631/r2/munger_v2_r1"; PV = f"{W}/personaje_v2"
sys.path.insert(0, f"{PV}/scripts"); sys.path.insert(0, f"{PV}/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/f1_impl/scripts")
import motor_a_f1 as M, regresion_elis_f1 as RE
ELIS = f"{PV}/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/elis_decisiones/Elis"
cif = json.load(open(f"{PV}/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/f1_impl/datos/elis_cifras_f1.json"))
TEXTOS = {"URD2022": "Elis - 2022 Universal Registration Document.txt", "URD2023": "Elis_Universal Registration Document_2023_EN.txt",
          "DEU2024FR": "Elis_Document d'enregistrement universel_2024_FR.txt", "URD2025": "Elis - 2025 Universal Registration Document.txt"}
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
def decl(fila=True):
    d = RE.declaracion(cif, True, False); d["perimetro_reinversion"] = {"valor": "A1_sin_ROU", "registro": {"fecha": "2026-11-18", "persona": "revisor", "motivo": "prueba"}}
    for n in ("da_rou", "da_ppa"):
        for y, e in d["series"][n].items():
            if fila: e["fila"] = cif["series"][n][y]["etiqueta"]
    d["fuentes_series"] = {doc: {"archivo": os.path.join("texto", n), "sha256": sha(os.path.join(ELIS, "texto", n))} for doc, n in TEXTOS.items()}
    return d
def fs(d, carpeta=ELIS):
    G = M.Guardas(); res = {}; M._guarda_fuentes_series(G, d, carpeta, list(range(2016, 2026)), res); x = G.lista[-1]; r = res["F1_SERIES"]
    return f"{'SALTA ' + x['efecto'] if x['salta'] else 'no salta'} · columna ok {r['columna_comprobada']} · pendiente {len(r['columna_pendiente'])} · " + \
           "; ".join(r["invalidas"] + r["incompletas"] + r["columna_pendiente"])[:260]
out = []
def caso(k, v): out.append(f"{k}: {v}"); print(out[-1], flush=True)
caso("L0 Elis legítima con fila", fs(decl()))
caso("L1 Elis legítima sin fila", fs(decl(False)))
d = decl(); d["series"]["da_rou"]["2025"].update(valor_fuente=-132.2, literal="(132.2)"); caso("E1a 2025 con la cifra de 2024, con fila", fs(d))
d = decl(); d["series"]["da_rou"]["2025"].update(valor_fuente=-132.2, literal="(132.2)"); d["series"]["da_rou"]["2025"].pop("fila"); caso("E1b lo mismo SIN fila", fs(d))
d = decl(); d["series"]["da_rou"]["2025"].update(valor_fuente=-132.2, literal="(132.2)", fila="assets"); caso("E1c lo mismo con una fila ambigua («assets»)", fs(d))
d = decl(); d["series"]["da_rou"]["2025"].update(valor_fuente=149.5, signo=1, tratamiento="ninguno", literal="149.5"); caso("S1 «149.5» sin paréntesis (T9)", fs(d))
d = decl(); d["series"]["da_rou"]["2025"].update(valor_fuente=-49.5, literal="(49.5)"); caso("S2 «(49.5)» (parte de «(149.5)»)", fs(d))
# expediente sintético
t = tempfile.mkdtemp(prefix="exp_", dir="/tmp/claude-0/revision_v631"); os.makedirs(f"{t}/texto")
pag = ("[PDF PAGE 1]\nNote 9 Right-of-use assets\n                                        2025        2024\n"
       "Depreciation right-of-use               (999.9)     (132.2)\nBig items                             (1 019,4)   (1 019,4)\nOther (1,019.4) total\n[PDF PAGE 2]\nx\n")
open(f"{t}/texto/inventada.txt", "w").write(pag)
def dsint(lit, vf, fila, arch="texto/inventada.txt", sh=None, doc="X", extra=None):
    e = {"valor_fuente": vf, "signo": -1, "tratamiento": "importe publicado entre paréntesis", "documento": doc, "pagina": 1, "literal": lit, "fila": fila}
    if extra: e.update(extra)
    return {"series": {"da_rou": {"2025": e}}, "fuentes_series": {doc: {"archivo": arch, "sha256": sh if sh is not None else (sha(os.path.join(t, arch)) if os.path.isfile(os.path.join(t, arch)) else "0")}}}
caso("S4 fuente inventada dentro del expediente, con su sha256", fs(dsint("(999.9)", -999.9, "Depreciation right-of-use"), t))
caso("S8 sha256 distinto", fs(dsint("(999.9)", -999.9, "Depreciation right-of-use", sh="ab" * 32), t))
rel = os.path.relpath(os.path.join(ELIS, "texto", TEXTOS["URD2025"]), t)
caso("S5 fuente de otro expediente (../)", fs(dsint("(149.5)", -149.5, "Right-of-use assets", arch=rel, sh=sha(os.path.join(ELIS, "texto", TEXTOS["URD2025"])), extra={"pagina": 350}), t))
os.symlink(os.path.join(ELIS, "texto", TEXTOS["URD2025"]), f"{t}/texto/enlace.txt")
caso("S5b enlace simbólico dentro del expediente a otro expediente", fs(dsint("(149.5)", -149.5, "Right-of-use assets", arch="texto/enlace.txt", sh=sha(os.path.join(ELIS, "texto", TEXTOS["URD2025"])), extra={"pagina": 350}), t))
os.link(os.path.join(ELIS, "texto", TEXTOS["URD2025"]), f"{t}/texto/duro.txt") if os.stat(ELIS).st_dev == os.stat(t).st_dev else None
if os.path.exists(f"{t}/texto/duro.txt"):
    caso("S5c enlace duro (copia) del texto de otro expediente", fs(dsint("(149.5)", -149.5, "Right-of-use assets", arch="texto/duro.txt", extra={"pagina": 350}), t))
caso("S6 «archivo» de la entrada distinto del registrado", fs(dsint("(999.9)", -999.9, "Depreciation right-of-use", extra={"archivo": "texto/otro.txt"}), t))
caso("F1 legítima con espacio de miles «(1 019,4)» (columna 2025)", fs(dsint("(1 019,4)", -1019.4, "Big items"), t))
caso("F2 legítima con espacio duro «(1 019,4)» (columna 2024 → se declara 2025 aquí, debería decir columna 2024)", fs(dsint("(1 019,4)", -1019.4, "Big items"), t))
caso("F3 legítima con coma de miles «(1,019.4)» sin encabezado alineado", fs(dsint("(1,019.4)", -1019.4, "Other"), t))
open("/tmp/claude-0/revision_v631/s2/series2_salida.txt", "w").write("\n".join(out) + "\n")
