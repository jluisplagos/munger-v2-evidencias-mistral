# Comandos exactos para reproducir el frente C (M2)

Desde la raíz del auxiliar `jluisplagos/munger-v2-evidencias-mistral`, rama `mistral/m2-matematica-b`:

```bash
# 0. Verificar origen y rama, y traer la rama publicada
git remote get-url origin            # https://github.com/jluisplagos/munger-v2-evidencias-mistral.git
git fetch origin mistral/m2-matematica-b
git checkout mistral/m2-matematica-b

# 1. Insumos (selección parcial verificada; ZIP de la Release base-4.14 de jluisplagos/munger-v2)
gh release download base-4.14 --repo jluisplagos/munger-v2 --dir .trabajo \
  --pattern 'munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip'
mv .trabajo/munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip .trabajo/base414.zip
sha256sum .trabajo/base414.zip      # bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e
python3 docs/programa_mistral_m2/herramientas/preparar_insumos.py --zip .trabajo/base414.zip
# -> {"seleccion_conforme": 251, ... "producto_completo_verificado": false}

# 2. Casos fijados (lee solo .trabajo/insumos_m2/, escribe casos_fijados.json)
cd resultados_m2/matematica_b
python3 codigo/oraculo_precio_si.py --selftest      # -> PASA
python3 codigo/generar_casos_fijados.py              # -> 57 casos con provenance y sha256 (H6 = Viscofan 4.13 Caja, tras C1)

# 3. Oráculo sobre los 57 casos + propiedades (escribe resultados_casos.json)
python3 codigo/ejecutar_casos.py                     # -> 10/10 propiedades true

# 4. Comparación con el producto (esperado = oráculo; producto en columnas aparte)
python3 codigo/comparar_producto.py                  # -> COMPARACION_IMPLEMENTACION.csv, residuo máx 2,8e-14

# 5. Efectos de probabilidades (D7) y sensibilidad finita preanunciada
python3 codigo/efectos_probabilidades.py              # -> EFECTOS_PROBABILIDADES.csv
python3 codigo/sensibilidad_finita.py                # -> SENSIBILIDAD_FINITA.csv (192 filas)

# 6. Protocolos de cobertura y ejemplos sintéticos
python3 codigo/protocolos_cobertura.py               # -> PROTOCOLOS_COBERTURA.csv (cobertura coincide 24/24)

# 7. Manifiesto
cd resultados_m2/matematica_b
find . -type f ! -name MANIFIESTO_SHA256.txt | sort | xargs sha256sum > MANIFIESTO_SHA256.txt
```

No se ejecuta LibreOffice, ni el pipeline, ni macros; no se abren XLSX; no se modifica el producto. Los scripts solo leen `.trabajo/insumos_m2/` y escriben dentro de `resultados_m2/matematica_b/`.
