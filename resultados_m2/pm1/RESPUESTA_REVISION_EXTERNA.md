# Respuesta a la revisión externa · frente B (P-M1) · 2026-11-16

Rama mantenida: `mistral/m2-fundamento-pm1` (no se fusionó `revision/chatgpt-m2-20261116`; no se tocaron otros frentes, main, el producto, M1, libros oficiales, configuraciones, decisiones humanas ni auditorías). Revisión leída con `git show` desde el commit `9366bdd563a986cdd6907ba2187f796f96898db6`: `REVISION_CHATGPT_M2.md`, `CORRECCION_B.md`, `SONDA_B_INTANGIBLES.json`, `FUENTES_DESCARGADAS_REVISION.json`. Base revisada: commit congelado `b5a07e007785f0cd194cb6437fcb5cd7029cb79f`. Escritura solo en `resultados_m2/pm1/`.

## B1 · Las nueve altas «PP&E» de Vidrala procedían de la nota Intangible Assets — CORREGIDO

Verificado contra los contraejemplos de la revisión y reconstruido desde la nota correcta (`Property, Plant and Equipment`, fila total de Coste, columna `Additions`), con encabezado de nota, columna y etiqueta de año exigidos en la misma ventana de cita:

| Año | PP&E Additions (k€) | Nota / página PDF / líneas | Intangibles Additions (k€) | de ellos derechos de emisión | de ellos goodwill | Comb. de negocio en PP&E |
|---|---|---|---|---|---|---|
| 2017 | **101.154** | nota 6, p.42, l1829-1848 | 156.743 | 3.237 | **150.657** | 76.170 |
| 2018 | **93.148** | nota 6, p.40, l1834-1854 | 18.623 | 14.645 | 0 | — |
| 2019 | **108.645** | nota 6, p.41, l1782-1802 | 25.694 | 22.147 | 0 | — |
| 2020 | **134.263** | nota 6, p.50, l2475-2494 | 28.666 | 26.558 | 0 | — |
| 2021 | **105.877** | nota 6, p.39, l2248-2268 | 44.810 | 37.359 | 0 | — |
| 2022 | **158.234** | nota 6, p.40, l2335-2355 | 93.759 | 90.780 | 0 | — |
| 2023 | **134.472** | nota 7, p.43, l2272-2294 | 100.655 | 93.306 | 0 | 262.679 |
| 2024 | **171.185** | nota 7, p.47, l2473-2495 | 48.326 | 40.135 | 0 | — |
| 2025 | **177.848** | nota 7, p.43, l2404-2426 | 45.173 | 37.661 | 0 | — |

Contraejemplos confirmados: CF_2025 p.PDF 43 (nota 7) altas PP&E 2025 = **177.848 k€**; **45.173 k€** es la nota 8 (Intangible Assets) p.PDF 46; los **156.743 k€** de 2017 son intangibles e incluyen **150.657 k€ de goodwill** (CF_2017 p.44 l1952). Coinciden con `SONDA_B_INTANGIBLES.json`.

- **Separación (encargo 2):** `VIDRALA_REPOSICION_CAPACIDAD.csv` ahora separa columnas: adiciones PP&E brutas, de ellas combinaciones de negocio; adiciones de intangibles brutas, de ellas derechos de emisión y goodwill; pagos de PP&E y de intangibles (EFE); altas ROU activo/pasivo; amortización ROU. No se fuerza igualdad entre adiciones, pagos de caja y mantenimiento económico.
- **Discrepancias comparativas revisadas (encargo 2):** cada año se contrasta con el comparativo publicado en el CF del ejercicio siguiente (todas las adiciones PP&E coinciden: 2017→CF_2018 l1891, …, 2024→CF_2025 l2476). Las únicas diferencias registradas, sin resolver y sin forzar: CF_2024 reexpresa el comparativo 2023 de la nota PP&E (combinación de negocios 291.821 vs 262.679; cierre de coste 2.131.588 vs 2.102.446; adiciones 134.472 **iguales**) y el de la nota de intangibles (adiciones 102.795 con goodwill 2.170 vs 100.655 en CF_2023). La «discrepancia 2023 = 100.655 vs 102.795» citada antes como PP&E era un artefacto de haber leído la nota de intangibles como PP&E. Conclusiones dependientes corregidas en `DOSSIER_D2.md` §2, `HALLAZGOS.md` (8 y 10) y `PUNTO_DE_RECUPERACION.md` (B5).
- **Verificación reforzada (encargo 3):** `extraer_fila_nota()` exige en la ventana: encabezado de la nota (`N. Property, Plant and Equipment` / `N. Intangible Assets`), columna `Additions`, etiqueta del año y la fila exacta; las PP&E se comprueban además contra el comparativo del año siguiente. **Control negativo:** `control_negativo()` reproduce el error antiguo —las nueve filas «Additions … <total>» usadas antes como PP&E viven en la nota Intangible Assets— y verifica que el extractor de PP&E **rechaza** esas ventanas al no contener el encabezado PP&E. Un regex de números sin contexto de partida ya no acredita la partida. El script falla loudly (AssertionError) si cualquier cita se mueve.

## B2 · θ negativo no identifica θ=0 — CORREGIDO

- Eliminada de `DOSSIER_D2.md` (§3.1, §4, §6), `RESUMEN_PARA_CLAUDE.md`, `HALLAZGOS.md` y `PUNTO_DE_RECUPERACION.md` la inferencia «aceptar el desglose → P-M1 delimitable con θ acotada a 0». Se conserva lo correcto del propio dossier: truncar a 0 no valida θ=0.
- θ negativa (−4,5427 / −2,8442 / −1,5198 sobre el perímetro NIIF16; −2,3649 sobre el total publicado) queda como **diagnóstico condicional fuera de [0,1]**; la sensibilidad de reclasificación (60–100% sobre NIIF16; 70–100% sobre el total publicado) también como diagnóstico condicional. No se elige otro parámetro para cerrar el expediente.
- **Extrapolación de perímetro etiquetada como HIPÓTESIS (encargo 5):** aplicar los porcentajes del total publicado a (capex caja + altas ROU) es un cambio de perímetro; `CALCULOS_PM1.json` lo etiqueta explícitamente (`clasificacion_calculos`, `etiqueta_definicion_M`) y conserva **separados** el cálculo sobre la base correcta (total publicado al que pertenecen los porcentajes: contraste θ=−2,3649; capacidad 158.377 k€; sensibilidad 70,3/76,2/85,1/100%) del de la hipótesis (NIIF16: capacidad 163.595 k€; sensibilidad 60,3/68,3/80,2/100%). Se distinguen datos / transformaciones / extrapolaciones (hipótesis) / política (ninguna adoptada).
- **Conclusión (encargo 5):** **P-M1 no delimitada con la evidencia disponible y bloqueo de la conclusión afectada** (D2 y, de ella, D5/D6, pendientes de la persona responsable). Una política prudencial (p. ej. θ=0) solo puede proponerse como decisión humana con sus límites, no como parámetro identificado. Datos concretos que permitirían avanzar: desglose por tipo 2017 de Viscofan (ausente en bytes); desglose reposición/capacidad de las reconstrucciones de hornos de Vidrala (nº de hornos, calendario, coste, capacidad antes/después); evidencia publicada de qué fracción de la inversión declarada es reposición.

## Estado de preservación de fuentes nuevas (encargo 6)

- Los 4 PDF de `FUENTES_NUEVAS.csv` se re-verificaron en local: SHA-256 y bytes coinciden uno a uno con `FUENTES_DESCARGADAS_REVISION.json` (p. ej. Beat'30 CNMV `8549db83…`, 6.846.066 B; gestión 2024 EN `1dc3ef18…`, 18.489.679 B; ES `195fa418…`, 12.008.408 B; CCAA 2024 `14b61868…`, 1.599.962 B = idéntico al CF_2024.pdf de la base).
- **Bloqueo exacto:** el endpoint de subida de assets de GitHub responde **HTTP 401** en este sandbox (el proxy no inyecta credenciales en `uploads.github.com`). Se reintentó la subida una vez durante esta corrección con `gh release upload` y devolvió `HTTP 401: Bad credentials` sobre la URL de assets de la release 446958355; la Release `fuentes-mistral-m2-20261116` sigue con **assets vacíos** (verificado con `gh release view … --json assets`). No se piden tokens en el chat; los PDF **no** se presentan como preservados en GitHub: permanecen en cobertura PROVISIONAL (URL final + SHA-256 + bytes + páginas en `FUENTES_NUEVAS.csv`, estado actualizado en `scripts/fuentes_csv.py`), fuera de Git. El HTML oficial de la Memoria Anual 2024 y su índice SHA-256 **sí** están conservados en Git (`fuentes_nuevas/`). Si la subida llegara a funcionar, se verificarían primero los assets existentes y se evitarían sobrescrituras.

## Comandos realmente ejecutados y resultados (esta corrección)

```
git fetch origin revision/chatgpt-m2-20261116                       # OK
git show 9366bdd5…:revision_externa/m2/{REVISION_CHATGPT_M2.md,CORRECCION_B.md,SONDA_B_INTANGIBLES.json,FUENTES_DESCARGADAS_REVISION.json}   # leídos
sha256sum .trabajo/fuentes_nuevas/*.pdf                              # 4/4 coinciden con la prueba del revisor
gh release view fuentes-mistral-m2-20261116 --json assets            # assets: [] (vacíos)
gh release upload … viscofan_cuentas_consolidadas_2024_informeanual2024.pdf   # HTTP 401 (reintento)
python3 resultados_m2/pm1/scripts/extraer_pdfs_viscofan.py           # exit 0
python3 resultados_m2/pm1/scripts/tablas_viscofan.py                 # exit 0
python3 resultados_m2/pm1/scripts/tablas_vidrala.py                   # exit 0 (comparativos OK + control negativo superado)
python3 resultados_m2/pm1/scripts/fuentes_csv.py                     # exit 0 (FUENTES_NUEVAS/CONSERVADAS regenerados)
python3 resultados_m2/pm1/scripts/calculos_pm1.py                    # exit 0 (CALCULOS_PM1.json con etiquetas y bloques separados)
```

## Qué cambia y qué no queda identificado

- **Cambia:** clasificación de las inversiones de Vidrala (PP&E reales 101.154…177.848 k€; intangibles/goodwill/derechos de emisión separados); la discrepancia comparativa 2023 queda replanteada (no era de PP&E); la conclusión de D2 pasa a «P-M1 no delimitada + bloqueo de la conclusión afectada» en todos los entregables; la extrapolación de perímetro queda etiquetada como hipótesis con cálculos separados.
- **No cambia:** los datos de Viscofan (desglose 2016–2025, puente capex/D&A/ROU, exceso NIIF16 64.923 k€ / Caja 40.813 k€), los rangos de λ condicionados (C23 [1,3299; 1,3743], C28 [1,2037; 1,2810]), los valores negativos de θ como diagnósticos, y la ausencia de desglose reposición/capacidad de Vidrala.
- **Sigue sin identificarse (límites pendientes):** θ y λ (ningún valor adoptado); estructura de P-M1 y familia Λ; desglose por tipo 2017 de Viscofan; desglose reposición/capacidad de las reconstrucciones de hornos de Vidrala; qué fracción de la inversión declarada es reposición. D2/D5/D6 son decisiones humanas pendientes; este frente no las adopta ni se autoaprueba.
- **Preservación pendiente:** subida de los 4 PDF como assets de la Release auxiliar (bloqueada por el 401 del endpoint de uploads); `www`/`public.viscofan.com` sin TLS verificado en el proxy (bytes no usados); consumo de crédito no visible desde la sesión.

## Entrega

Commit congelado de esta respuesta: HEAD de `mistral/m2-fundamento-pm1` tras el push de esta corrección (SHA reportado en la entrega de la sesión; base revisada `b5a07e0…`). `MANIFIESTO_SHA256.txt` regenerado con todas las salidas. Sin PR, sin fusión, sin ciclos recursivos de revisión, sin recomendaciones de inversión, sin aptitud para dinero real.
