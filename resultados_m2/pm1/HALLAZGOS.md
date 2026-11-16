# Hallazgos · frente B (P-M1) · 2026-11-16

Corregido según la revisión externa de 2026-11-16 (commit `9366bdd5…`, rama `revision/chatgpt-m2-20261116`): B1 y B2; ver `RESPUESTA_REVISION_EXTERNA.md`.

Propuesta de evidencia de Mistral; pendiente de revisión e incorporación por el integrador. Clases: DATO (publicado, con fuente), DERIVACIÓN (script reproducible), INFERENCIA (discutible), AUSENTE (no está en bytes conservados), PROVISIONAL (web/bytes sin preservar como asset).

## Viscofan

1. DATO — Viscofan publica desglose por tipo de la inversión cada año; verificado en bytes para 2016, 2018–2025 (2017 solo total 107,2 M€). Ver `INVERSION_VISCOFAN_2016_2025.csv` (cita + página PDF + líneas por fila). Solo 2025 etiqueta la capacidad como «aimed at increasing capacity».
2. DATO — El desglose de 2024 (34/14/35/17 sobre €71,0M) ya está en bytes conservados: página HTML oficial de la Memoria Anual 2024 (sha256 `bd139bde…`), en `fuentes_nuevas/`; el PDF de gestión 2024 (EN p.8) se verificó por OCR porque su capa de texto (Workiva) tiene el mapa de caracteres roto.
3. DERIVACIÓN — Perímetro 2021–2025 recalculado: capex caja 443.945 k€, altas ROU 24.110, D&A 403.132, amort ROU 27.051, **exceso NIIF 16 = 64.923 k€**, exceso «Caja» = 40.813 k€ (`PUENTE_CAPEX_DA_ROU.csv`, `puente_resumen.json`). Coincide con la conciliación de la base.
4. DATO — Puente 2022: publicada 125,6 M€ vs pagos 115.566 k€ vs adiciones PP&E brutas 120.362 k€; no se igualan por conveniencia. Puente 2025: dos definiciones de CapEx en el mismo informe (APM sin ROU, p.146; taxonomía con ROU, p.275, total 90,6 = 84,1 + 6,494 ROU). En CF_2021 p.8 la etiqueta de la línea de pagos está intercambiada con la de dependientes (la comparatif de CF_2022 lo deshace).
5. DERIVACIÓN — θ con el desglose por tipo 2021–2025: −4,5427 (estrecha) / −2,8442 (media) / −1,5198 (amplia) sobre el perímetro NIIF16 (capex caja + altas ROU), etiquetado como **hipótesis de extrapolación de perímetro**; sobre el total publicado (base correcta, cálculo separado) el contraste da −2,3649. M < D&A en los cinco años; θ≥0 exige reclasificar 60–100% de la «capacidad» sobre el perímetro NIIF16 (70–100% sobre el total publicado) (`CALCULOS_PM1.json`, dos bloques separados). θ negativa (fuera de [0,1]) se conserva como diagnóstico condicional; no identifica θ=0 ni otro valor; no se trunca ni se adopta.
6. DATO/PROVISIONAL — Beat'30 (CNMV, 27-feb-2026, sha256 `8549db83…`, 58 págs.): capex 2026–2030 €600M, ~50% recurrente / €300M crecimiento (p.27/31/35/53; excluye €12M biomasa y €9M terrenos por no ser salida de caja). Resuelve la discrepancia de fuentes secundarias. Bytes en cobertura provisional (uploads 401), SHA registrada.
7. AUSENTE — Desglose por tipo 2017; AR completos 2016/2018/2021/2022/2023; notas trimestrales.

## Vidrala

8. DATO — Vida útil hornos 8–16 años en todos los años CF_2017…CF_2025. Renovación de hornos 2024–2025 (ES/PT/UK); modernización de plantas UK/PT 2018–2022 con importes por país. Adiciones brutas PP&E 2017–2025 (nota *Property, Plant and Equipment*, corregidas tras B1): 101.154 / 93.148 / 108.645 / 134.263 / 105.877 / 158.234 / 134.472 / 171.185 / 177.848 k€, separadas de intangibles (156.743 … 45.173 k€, con goodwill 150.657 en 2017 y derechos de emisión aparte), combinaciones de negocio, ROU y pagos de caja en `VIDRALA_REPOSICION_CAPACIDAD.csv`.
9. DATO — ROU: altas activo/pasivo difieren (2.165/2.133 en 2022; 1.485/1.429 en 2024); 46.123 k€ por «The Park» (2023) como combinación de negocios; amortización ROU 633→6.760 (2022–2025); 2021 sin movimientos publicados. No se igualan activo y pasivo.
10. AUSENTE — Vidrala no publica desglose reposición/capacidad de las reconstrucciones (nº hornos, calendario, coste, capacidad antes/después); la cita «more than pure replacement» es de terceros sin bytes. Discrepancias comparativas 2023 registradas sin resolver (CF_2024): nota PP&E, combinación de negocios reexpresada 291.821 vs 262.679 y cierre de coste 2.131.588 vs 2.102.446 (adiciones 134.472 iguales en ambos); nota de intangibles, adiciones 102.795 (goodwill 2.170) vs 100.655 en CF_2023. La discrepancia antigua «100.655 vs 102.795 como PP&E» era artefacto de leer la nota de intangibles como PP&E (error B1, corregido).
11. DERIVACIÓN — λ condicionado a series primarias Eurostat (ES, PPI anual, 2021=100, NSA, con SHA-256 en `indices/`): C23 λ∈[1,3299; 1,3743]; C28 λ∈[1,2037; 1,2810] para L∈[8,16], t=2025. Mide inflación de precios de sector, no cambio técnico ni capacidad; no se adopta.

## Protocolo y límites

12. PROVISIONAL — Release auxiliar `fuentes-mistral-m2-20261116` creada; los PDF nuevos no pudieron subirse como assets (uploads.github.com → 401 en el sandbox): quedan con URL final + SHA-256 + bytes + páginas en `FUENTES_NUEVAS.csv` y pendientes de subida. El HTML oficial 2024 y el índice sí están en Git. Nada de PDF/XLSX/ZIP en el historial Git.
13. LÍMITE — www/public.viscofan.com no verifican TLS en el proxy del sandbox; no se usaron sus bytes. CNMV, BOE, informeanual*.viscofan.com y ec.europa.eu sí verifican.
14. NO ADOPTADO — θ, λ, k, probabilidades, políticas, estructura de P-M1; no se convierte categoría contable en mantenimiento económico; sin recomendaciones de inversión; D2/D5/D6 quedan para la persona responsable.
