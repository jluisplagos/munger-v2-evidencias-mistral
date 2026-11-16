# Dossier D2 · ¿Está delimitada de forma defendible la incertidumbre de P-M1?

Frente B (P-M1) · rama `mistral/m2-fundamento-pm1` · 2026-11-16.
Propuesta de evidencia de Mistral; pendiente de revisión e incorporación por el integrador. No APROBADO. Sin recomendaciones de inversión ni autoaprobación. D2 es decisión de la persona responsable; este dossier presenta lo identificado, lo no identificado, las opciones condicionadas y la evidencia ausente.

D2 (según `DECISIONES_PENDIENTES_4_14.md`): «¿Está delimitada de forma defendible la incertidumbre de P-M1 (estructura, familia y parámetro λ o θ)? ¿Qué protocolo rige?» El encargo §6 fija la regla: sin delimitación defendible, el sistema se abstiene de la conclusión afectada.

Separación exigida: **dato** (publicado, con fuente), **derivación** (cálculo reproducible), **inferencia** (lectura discutible), **hipótesis** (pendiente), **decisión** (de la persona responsable).

---

## 1. Viscofan · lo que queda identificado (datos y derivaciones)

### 1.1 Desglose por tipo de la inversión publicada, 2016–2025

Dato: Viscofan publica cada año un desglose en cuatro tipos (capacidad y maquinaria / proceso / sostenibilidad-EHS / ordinarias). Verificado en bytes conservados para 2016, 2018, 2019, 2020, 2021, 2022, 2023, 2024 y 2025 (`INVERSION_VISCOFAN_2016_2025.csv`, cada fila con documento, página PDF, líneas y cita). 2017: solo el total (107,2 M€, comparativo en IA_2018 p.135) — desglose AUSENTE en bytes conservados.

| Año | Total M€ | Capacidad | Proceso | EHS | Ordinaria |
|---|---|---|---|---|---|
| 2016 | 86,7 | 51% | 22% | 8% | 19% |
| 2017 | 107,2 | — | — | — | — |
| 2018 | 71,6 | 12% | 55% | 8% | 25% |
| 2019 | 62,1 | 23% (€14,3M) | 41% (€25,3M) | 17% (€10,6M) | 19% (€11,9M) |
| 2020 | 56,9 | 27% | 20% | 27% | 26% |
| 2021 | 92,0 | 44% | 18% | 18% | 20% |
| 2022 | 125,6 | 40% | 30% | 16% | 14% |
| 2023 | 77,5 | 16% | 3% | 26% | 55% |
| 2024 | 71,0 | 34% | 14% | 35% | 17% (fuente nueva B4: HTML oficial Memoria Anual 2024, sha256 `bd139bde…`; PDF gestión 2024 p.8 verificado por OCR) |
| 2025 | 84,1 | 37% (€30,9M) | 22% (€19,2M) | 27% (€22,4M) | 14% (€11,6M) |

Dato sobre el significado de las categorías: solo el texto de 2025 dice que la de capacidad iba «aimed at increasing capacity» (AR_2025 PDF p.143 = impresa 123). En 2016–2024 la etiqueta es «capacidad y maquinaria», que puede incluir maquinaria de reposición. No se equipara categoría contable con mantenimiento económico ni con crecimiento.

### 1.2 Conciliación capex / D&A / ROU (derivación, `PUENTE_CAPEX_DA_ROU.csv`, `CALCULOS_PM1.json`)

- Perímetro del modelo 2021–2025 (NIIF 16): Σ capex de caja = 443.945 k€; Σ altas ROU = 24.110 k€; Σ D&A = 403.132 k€; **exceso = 64.923 k€** (perímetro «Caja»: 40.813 k€). Recalculado con `Decimal` desde citas verificadas; coincide con la conciliación de la base.
- Puente 2022 (recomprobado, no igualado por conveniencia): inversión publicada 125,6 M€ vs pagos de inmovilizado 115.566 k€ vs adiciones brutas PP&E 120.362 k€ (+ intangibles y altas ROU 1.633 k€ → devengado ≈ 126 M€). La diferencia publicada−caja (10.034 k€) no se atribuye a una sola causa sin evidencia; se documenta devengado vs caja, bruto vs neto y ROU.
- Puente 2025: la empresa publica dos definiciones de CapEx en el mismo informe — APM Capex (AR_2025 p.146: altas de intangibles + PP&E, **sin** ROU) y taxonomía UE (AR_2025 p.275: **con** ROU, total 90,6 M€ = 84,1 gestión + 6,494 altas ROU). Apoto documental al perímetro NIIF 16 (D4), sin decidirlo.
- Hallazgo de lectura: en CF_2021 p.8 la etiqueta inglesa de la línea de pagos está intercambiada con la de adquisición de dependientes; la columna comparativa de CF_2022 p.25 l.337 fija pagos 2021 = −95.779 y dependientes = 0.

### 1.3 Límite de θ con el desglose por tipo (derivación; `CALCULOS_PM1.json`)

θ = (ΣM − ΣD&A) / exceso, con M estimada aplicando los porcentajes publicados a (capex caja + altas ROU):

| Definición de M | ΣM 2021–25 (k€) | θ |
|---|---|---|
| estrecha (solo ordinarias) | 108.207 | **−4,5427** |
| media (ordinarias + EHS) | 218.478 | **−2,8442** |
| amplia (todo menos capacidad) | 304.460 | **−1,5198** |
| contraste: amplia sobre el total publicado (exceso 47.068) | 291.813 | −2,3649 |

En los cinco años M < D&A bajo las tres definiciones. La inversión declarada de capacidad 2021–2025 suma 163.595 k€. Sensibilidad: para θ=0 haría falta reclasificar como reposición el 60,3% de esa capacidad; θ=0,2 → 68,3%; θ=0,5 → 80,2%; θ=1 → 100%.

Inferencia (discutible): con la clasificación de la propia empresa, el exceso de inversión sobre D&A queda explicado por la inversión de capacidad; lo que no es capacidad ni siquiera cubre la D&A. Una θ negativa se conserva como diagnóstico de definición/identificación — truncarla a cero no valida θ=0, la familia ni el punto actual. El script citado `agentes/B/scripts/theta_desglose_viscofan.py` no está en la base y no se invoca; todo se recalcula en `scripts/calculos_pm1.py`.

## 2. Vidrala · lo que queda identificado

- Vida útil de hornos: «Furnaces, installations and production machinery **8 – 16** años» en la nota de inmovilizado de **todos** los años CF_2017…CF_2025 (y ES_2025 p.14 l.651). Pista contrastada, no distribución adoptada.
- Renovación de hornos: adiciones 2024 «primarily in the renewal of furnaces» en España, Portugal y UK (CF_2024 p.48); 2025 igual (CF_2025 p.44); ES_2024 p.199 «reconstrucción de varios hornos en el Grupo»; ES_2025 p.72 PERTE descarbonización de hornos Crisnova/Castellar (10.298 y 6.316 k€, inversión desde 2026); ES_2025 p.127 «Horno del futuro» (eficiencia, electrificación).
- Adiciones de plantas por país (nota PP&E): 2018 Italia 27.958 k€ / UK 33.733 k€ / Castellar 16.329 k€; 2019 Portugal 20.250 / UK 44.247; 2020 UK 77.801 / Portugal 29.031; 2021 UK 32.597 / Portugal 39.792; 2022 UK 23.479 / Portugal 94.557; 2023 Portugal + contribución por combinaciones de negocio (Nota 5). Se distingue «update/modernización de plantas» de reposición de hornos solo donde el texto lo dice; no se fabrica mezcla reposición/capacidad.
- Adiciones brutas PP&E 2017–2025 (k€): 156.743 / 18.623 / 25.694 / 28.666 / 44.810 / 93.759 / 100.655 / 48.326 / 45.173. Discrepancia registrada sin resolver: comparativo 2023 = 102.795 en CF_2024 vs 100.655 en CF_2023.
- ROU: altas activo/pasivo no idénticas (2022: 2.165 vs 2.133; 2024: 1.485 vs 1.429; 2025: 2.404 ambos, con «otros» 9.595 activo por actualización de precio de «The Park»); 2023: 46.123 k€ por combinación de negocios («The Park», Bristol) + 645/643 ordinarias; amortización ROU 633/4.624/4.768/6.760 (2022–2025); 2021 sin tabla de movimientos (saldo 770). Sale & leaseback 2022 sobre plantas de España. No se supone que activo y pasivo deban coincidir.
- Prueba de deterioro (CF_2019…CF_2023): «recurring capex captured in the valuation models», sin cifra.
- **Capacidad añadida por las reconstrucciones: NO publicada en los bytes conservados.** La afirmación del CFO («more than pure replacement in that CapEx») es de transcripción de terceros sin bytes → queda como cita web provisional, no como documento conservado.

### 2.1 Límite de λ (derivación condicionada; series primarias en `indices/`)

λ ≈ PPI(t) / PPI(t−L), L = vida útil del activo que se repone. Series primarias Eurostat `sts_inpp_a` (PPI industria total, anual, España, I21 base 2021=100, NSA), descargadas de la API con SHA-256 y metadatos (`indices/eurostat_sts_inpp_a_ES_{C23,C28}_I21_NSA.csv`):

- C23 (productos minerales no metálicos, incluye vidrio): λ ∈ **[1,3299 ; 1,3743]** para L ∈ [8,16], t = 2025.
- C28 (maquinaria y equipo): λ ∈ **[1,2037 ; 1,2810]** para L ∈ [8,16], t = 2025.

Límites declarados: miden precios de producción del sector (output), no el precio de un horno (input); no capturan cambio técnico ni cambio de capacidad en la reconstrucción; son de España, anuales, sin ajustar; no representan exactamente activos, tecnología y geografía del grupo. El rango 1,10–1,25 de la crítica de la 4.8 era un rango de crítica, no una medición; estos rangos sí tienen fuente primaria, condicionados a serie y L. **No se adopta λ.**

## 3. Qué NO queda identificado (demostrado como límite)

1. θ para Viscofan: la evidencia no identifica qué fracción de «capacidad y maquinaria» es reposición. El método del desglose delimita θ ≤ 0 (acotado a 0) solo si se acepta la clasificación de la empresa; exige 60–100% de reclasificación para θ ≥ 0. La elección de esa fracción es un juicio económico humano.
2. λ para Vidrala: depende de la estructura de P-M1 (familia Λ) que no está delimitada; y de la vida útil efectiva de los hornos (8–16 es un rango contable, no observado por horno).
3. Vidrala: no hay desglose publicado de reposición vs capacidad añadida en las reconstrucciones de hornos (nº de hornos, calendario, coste, capacidad antes/después) → la incertidumbre de P-M1 de Vidrala **no está delimitada** con lo disponible.
4. Estructura de P-M1 (SR1/SR2/SRF/H/S) no delimitada con el desglose en ninguna empresa; familia Λ no contrastada en Viscofan.
5. Desglose por tipo de 2017 de Viscofan ausente en bytes conservados.

## 4. Opciones defendibles, condicionadas (ninguna adoptada)

- **Viscofan:** (a) aceptar el método replicable del desglose por tipo como juicio económico → P-M1 delimitable con θ acotado a 0 (extremo inferior del dominio), con la sensibilidad expuesta; (b) no aceptarlo → θ sin delimitar y abstención. En ambos casos la estructura y la familia siguen sin delimitar por esta vía.
- **Vidrala:** con lo disponible, la delimitación no es defendible → abstención del objetivo para cualquier uso que no sea el ensayo (coincide con el expediente `vidrala_bloqueo` existente). λ solo tendría sentido condicionado a una estructura aceptada y a serie+vida útil explícitas (rangos en §2.1).
- Protocolo: por empresa (opción 2 de D2 en la base) es la única defendible con esta evidencia; las formas (i) «bloqueo del objetivo» y (ii) «conclusión sin objetivo» son de la base y no se deciden aquí.

## 5. Evidencia ausente (registrada, no inventada)

- Desglose por tipo 2017 de Viscofan (solo total en bytes).
- AR/informe anual completos de Viscofan 2016, 2018, 2021, 2022, 2023 (tenemos extractos IA/AR conservados); notas de resultados trimestrales.
- PDF del informe de gestión 2024 y de la presentación Beat'30 como **assets** de la Release `fuentes-mistral-m2-20261116`: descargados con TLS verificado y con SHA-256 registrados, pero `uploads.github.com` devuelve 401 en este sandbox → **cobertura provisional** declarada en `FUENTES_NUEVAS.csv`; el HTML oficial de la Memoria Anual 2024 y el índice sí están en Git. Pendiente de subida por quien tenga acceso.
- Vidrala: nº de hornos, calendario de reconstrucción, coste y capacidad antes/después (Q-E1–Q-E7 de la 4.8, no enviadas); transcripción/grabación oficial de la presentación de resultados 2024 (la citada es de terceros, roic.ai, sin bytes).
- Series INE específicas de bienes de equipo (se usó Eurostat por acceso API abierto con metadatos; INE requiere clave o scraping de tablas HTML).

## 6. Consecuencias y decisión que corresponde a la persona responsable

- Efectos calculados ya obran en la base (citados como dato de la base, no recalculados aquí): Viscofan precio de Sí θ=0 → 41,8616 €; θ=1 → 38,4664 €; activa (θ=0,5) → 40,1640 €; todas en «caro» con el precio de 54,70 €. Vidrala rango 51,29–65,72 € con precio 90,10 €.
- **Decisión D2 (persona responsable):** si P-M1 está delimitada de forma defendible por empresa y qué protocolo rige. Este frente aporta: Viscofan delimitable solo si se acepta el método del desglose (θ ≤ 0, acotado a 0, con 60–100% de reclasificación para θ ≥ 0); Vidrala no delimitada → abstención del objetivo. D5 (config de Viscofan) y D6 (config de Vidrala) quedan pendientes de D2 y no se tocan.
- Nada de esto es recomendación de inversión ni aptitud para dinero real.
