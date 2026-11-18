## 1 bis. Perímetro F1 declarado y vara del foso (P-FOSO (a), 18-nov-2026 (coordinacion/cierre_v2/DECISIONES_PARA_EL_USUARIO.md))

- Perímetro de la reinversión (motor_a_f1.json): **A2_propio** · palancas S2C: A2_propio · ROIC terminal: A2_propio. F1 solo afecta al motor A (motor del libro: A).
- **Qué miden las palancas en este perímetro.** El margen (B15:D15) es el EBIT NIIF 16 (lleva la amortización de los derechos de uso; el resto del alquiler va en f). El S2C (B16:D16) es ventas nuevas ÷ inversión propia, sin derechos de uso. El ROIC terminal (B18:D18) está en las unidades del motor y se compara con r: **r no se traduce a otro perímetro** (ya es el listón del flujo del motor) y un ROIC terminal igual a r no cobra el local dos veces.
- **Regla (vara del foso):** con F1 en A2_propio, el foso (Análisis!C18) se juzga comparando el ROIC del capital propio pagado todo el alquiler, (EBIT − intereses de arrendamiento) × (1 − t) ÷ (capital invertido − arrendamientos), con r (Análisis!C56); Historia!C55 (ROIC de todo el capital) solo frente al sector (Palancas!H18). G4 sigue con r + 0,03. El foso puede seguir en «No» si la ventaja no parece duradera: la cifra no decide la celda.
- Historia!C55 y C54 son de **todo el capital** (con los arrendamientos): C55 = 8.78 %, frente al sector (Palancas!H18) 10.08 %; C54 = 3.185. No se comparan con r.

| Año | EBIT | t | Capital invertido | Arrendamientos | Capital propio | Intereses de arrendamiento | ROIC propio pagado el alquiler | ROIC sin arrendamientos | ROIC todo el capital | Celdas |
|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | 3320 | 0.2108 | 27817 | 11262 | 16555 | 337 (AR2022 p. 251 · «Interest accretion to lease liability») | 14.22 % | 15.83 % | 9.42 % | Historia!H7, H10, H32, H23 |
| 2022 | 3768 | 0.222 | 29963 | 11964 | 17999 | 356 (AR2023 p. 262 · «Interest accretion to lease liability») | 14.75 % | 16.29 % | 9.78 % | Historia!I7, I10, I32, I23 |
| 2023 | 2846 | 0.1983 | 29038 | 11826 | 17212 | 382 (AR2024 p. 321 · «Interest accretion to lease liability») | 11.48 % | 13.26 % | 7.86 % | Historia!J7, J10, J32, J23 |
| 2024 | 2784 | 0.2165 | 29600 | 12253 | 17347 | 422 (AR2025 p. 272 · «Interest accretion to lease liability») | 10.67 % | 12.57 % | 7.37 % | Historia!K7, K10, K32, K23 |
| 2025 | 3542 | 0.2242 | 28993 | 11974 | 17019 | 465 (AR2025 p. 272 · «Interest accretion to lease liability») | 14.03 % | 16.15 % | 9.48 % | Historia!L7, L10, L32, L23 |

- **Media 2021–2025 · ROIC del capital propio pagado todo el alquiler: 13.03 %** frente a r (Análisis!C56) 9.00 %: +4.03 puntos. Fórmula: (EBIT − intereses de arrendamiento) × (1 − t) ÷ (capital invertido − arrendamientos); filas 7, 10, 32 y 23 de la Historia y series.intereses_arrendamiento de motor_a_f1.json; media simple de 5 años.
  - Intereses de arrendamiento: comprobados en su fuente (cifra publicada en la página citada del documento con su huella; condición mínima de F1-SERIES, columna del ejercicio comprobada en 5 años). No es la verificación de entradas: la serie no está en el libro ni en el universo de verificacion_entradas.py.
- **Media 2021–2025 · ROIC sin arrendamientos (NOPAT NIIF 16 ÷ capital propio): 14.82 %** · ancla de G7 y del tope de la referencia mecánica del S2C en el perímetro del S2C: 2 × 14.82 % = 29.64 % (no 2 × C55 = 17.56 %). Fórmula: EBIT × (1 − t) ÷ (capital invertido − arrendamientos) (NOPAT NIIF 16 ÷ capital propio); filas 7, 10, 32 y 23.
- Media 2021–2025 · ROIC de todo el capital: 8.78 % (Historia!C55 = 8.78 %): solo frente al sector.
- S2C del perímetro: ancla Historia!C53 (con D_X del perímetro) = — (vacía: el ancla del perímetro no es calculable; cota A1 de la capa F1 sobre este libro, sin derechos de uso: 5.102) · S2C medio sin arrendamientos 2025 (ventas ÷ capital propio) = 5.426 · C54 (todo el capital) = 3.185.
- ROIC terminal neutro del motor: r × N ÷ (N − f), N = margen objetivo × (1 − Historia!C52), f = Historia!C58 (el ROIC terminal con el que el crecimiento perpetuo ni crea ni destruye valor en el motor A). Con el margen de partida (Historia!C48 = 0.03835) y f = 0.0001397: 9.04 %; con el margen objetivo de cada escenario cambia poco si f es pequeño (la capa F1 lo da por escenario tras la fase B). Un ROIC terminal por encima de él es retorno en exceso sobre el capital nuevo para siempre: es la afirmación sobre el foso que G4 limita a r + 0,03.

