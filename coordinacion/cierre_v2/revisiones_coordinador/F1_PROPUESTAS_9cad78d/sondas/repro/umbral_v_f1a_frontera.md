# Umbral de V-F1a · casos de frontera (importes ficticios)

Generado por `scripts/umbral_v_f1a_frontera.py`. **No adopta ningún umbral.** X = D&A ROU media de la ventana; B = cota de redondeo del FCF base; e = X ÷ FCF base; ρ = X ÷ ventas medias.

Casos: 30, con su estado esperado: 30. Comprobaciones directas: 14 de 14.

| Caso | Descripción | X | B | e (%) | ρ (%) | Sin umbral | Propuesta: 0,1 % FCF base | Resolución | 1 % FCF base | 5 % FCF base | 0,5 % ventas (v1) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F01 | sin arrendamientos (los dos a cero) | 0.0 | 0.25 | 0.0 | 0.0 | admisible | admisible | admisible | admisible | admisible | admisible |
| F02 | solo C49 positivo | 0.0 | 0.25 | 0.0 | 0.0 | V-F1m | V-F1m | V-F1m | V-F1m | V-F1m | V-F1m |
| F03 | solo D&A ROU positiva | 0.3 | 0.25 | 0.3 | 0.03 | V-F1m | V-F1m | V-F1m | V-F1m | V-F1m | V-F1m |
| F04 | fila de D&A ROU vacía en un año, con C49 positivo | None | 0.25 | None | None | V-F1b | V-F1b | V-F1b | V-F1b | V-F1b | V-F1b |
| F05 | D&A ROU negativa en un año | 0.166667 | 0.25 | 0.1667 | 0.0167 | V-F1e | V-F1e | V-F1e | V-F1e | V-F1e | V-F1e |
| F06 | arrendamientos grandes con el perímetro A1_sin_ROU | 50.0 | 0.25 | 50.0 | 5.0 | no aplica | no aplica | no aplica | no aplica | no aplica | no aplica |
| F07 | frontera del uno por mil, igualdad: X = 0,3 y FCF base 300 | 0.3 | 0.25 | 0.1 | 0.01 | BLOQUEA | AVISO | BLOQUEA | AVISO | AVISO | AVISO |
| F08 | justo por encima del uno por mil: e = 0,1111 % | 0.333333 | 0.25 | 0.1111 | 0.0111 | BLOQUEA | BLOQUEA | BLOQUEA | AVISO | AVISO | AVISO |
| F09 | justo por debajo del uno por mil: e = 0,0889 % | 0.266667 | 0.25 | 0.0889 | 0.0089 | BLOQUEA | AVISO | BLOQUEA | AVISO | AVISO | AVISO |
| F10 | uno por mil, igualdad exacta que la coma flotante no ve: 0,1 + 0,2 + 0,3 y FCF base 200 | 0.2 | 0.025 | 0.1 | 0.01 | BLOQUEA | AVISO | BLOQUEA | AVISO | AVISO | AVISO |
| F11 | resolución, por debajo: X = 0,2333 < B = 0,25 (e = 0,2333 %) | 0.233333 | 0.25 | 0.2333 | 0.0233 | BLOQUEA | BLOQUEA | AVISO | AVISO | AVISO | AVISO |
| F12 | resolución, igualdad: X = B = 0,25 (ventana de dos años) | 0.25 | 0.25 | 0.25 | 0.025 | BLOQUEA | BLOQUEA | AVISO | AVISO | AVISO | AVISO |
| F13 | resolución, justo por encima: X = 0,2667 > B = 0,25 | 0.266667 | 0.25 | 0.2667 | 0.0267 | BLOQUEA | BLOQUEA | BLOQUEA | AVISO | AVISO | AVISO |
| F14 | frontera del 1 %, igualdad | 1.0 | 0.25 | 1.0 | 0.1 | BLOQUEA | BLOQUEA | BLOQUEA | AVISO | AVISO | AVISO |
| F15 | justo por encima del 1 %: e = 1,001 % | 1.001 | 0.25 | 1.001 | 0.1001 | BLOQUEA | BLOQUEA | BLOQUEA | BLOQUEA | AVISO | AVISO |
| F16 | frontera del 5 % del FCF base y del 0,5 % de las ventas a la vez (igualdad en las dos) | 5.0 | 0.25 | 5.0 | 0.5 | BLOQUEA | BLOQUEA | BLOQUEA | BLOQUEA | AVISO | BLOQUEA |
| F17 | margen estrecho: ρ = 0,4 % de las ventas y e = 20 % del FCF base | 4.0 | 0.25 | 20.0 | 0.4 | BLOQUEA | BLOQUEA | BLOQUEA | BLOQUEA | BLOQUEA | AVISO |
| F18 | margen ancho: ρ = 0,6 % de las ventas y e = 2 % del FCF base | 6.0 | 0.25 | 2.0 | 0.6 | BLOQUEA | BLOQUEA | BLOQUEA | BLOQUEA | AVISO | BLOQUEA |
| F19 | FCF base cero con arrendamiento al nivel del redondeo | 0.2 | 0.25 | None | 0.02 | BLOQUEA | BLOQUEA | AVISO | BLOQUEA | BLOQUEA | AVISO |
| F20 | FCF base negativo con ρ = 0,2 % de las ventas | 2.0 | 0.25 | None | 0.2 | BLOQUEA | BLOQUEA | BLOQUEA | BLOQUEA | BLOQUEA | AVISO |
| F21 | el caso F07 en miles, con la misma precisión impresa (centenas de millar): mismo resultado | 300.0 | 250.0 | 0.1 | 0.01 | BLOQUEA | AVISO | BLOQUEA | AVISO | AVISO | AVISO |
| F22 | el caso F11 en miles, con la misma precisión impresa: mismo resultado | 233.333333 | 250.0 | 0.2333 | 0.0233 | BLOQUEA | BLOQUEA | AVISO | AVISO | AVISO | AVISO |
| F23 | los importes de F22 con el millar impreso: la resolución depende de la precisión de la fuente; el porcentaje, no | 233.333333 | 2.5 | 0.2333 | 0.0233 | BLOQUEA | BLOQUEA | BLOQUEA | AVISO | AVISO | AVISO |
| F24 | coeficientes que se anulan: el principal entra y sale y no cuenta en la cota (B = 0,25, no 0,35) | 0.3 | 0.25 | 0.3 | 0.03 | BLOQUEA | BLOQUEA | BLOQUEA | AVISO | AVISO | AVISO |
| F25 | un año de la ventana con D&A ROU cero y media positiva (e = 0,0667 %) | 0.2 | 0.25 | 0.0667 | 0.0067 | BLOQUEA | AVISO | AVISO | AVISO | AVISO | AVISO |
| F26 | baja precisión de la fuente: FCF base 3,0 y D&A ROU 0,2 (dos unidades de la última cifra; e = 6,67 %) | 0.2 | 0.25 | 6.6667 | 0.6667 | BLOQUEA | BLOQUEA | AVISO | BLOQUEA | BLOQUEA | BLOQUEA |
| F27 | caso T5 de la especificación (arrendamiento material): ROU 10, FCF verdadero 68 | 10.0 | 0.25 | 14.7059 | 2.5 | BLOQUEA | BLOQUEA | BLOQUEA | BLOQUEA | BLOQUEA | BLOQUEA |
| F28 | caso T5 con arrendamiento mínimo: ROU 0,2, FCF verdadero 79,76 (e = 0,2508 %) | 0.2 | 0.25 | 0.2508 | 0.05 | BLOQUEA | BLOQUEA | AVISO | AVISO | AVISO | AVISO |
| F29 | caso T5 con arrendamiento ínfimo: ROU 0,05, FCF verdadero 79,94 (e = 0,0625 %) | 0.05 | 0.025 | 0.0625 | 0.0125 | BLOQUEA | AVISO | BLOQUEA | AVISO | AVISO | AVISO |
| F30 | motor B | None | 0.25 | None | None | no aplica | no aplica | no aplica | no aplica | no aplica | no aplica |

## El 0,5 % de las ventas, expresado sobre el flujo

| FCF base ÷ ventas | 0,5 % de las ventas = … del FCF base | 0,1 % del FCF base = … de las ventas |
|---|---|---|
| 2 % | 25.0 % | 0.002 % |
| 5 % | 10.0 % | 0.005 % |
| 10 % | 5.0 % | 0.01 % |
| 20 % | 2.5 % | 0.02 % |
| 30 % | 1.67 % | 0.03 % |

## Comprobaciones directas

- OK · cota con cinco cifras de un decimal = 0,25
- OK · cota con una cifra que entra y sale (coeficiente neto cero) = 0,25
- OK · cota en miles con precisión de centenas de millar = 250
- OK · coma flotante: (0.1 + 0.2 + 0.3) / 3 / 200 > 0.001 (por eso la comparación es exacta)
- OK · exacto: (0,1 + 0,2 + 0,3) / 3 / 200 = 0,1 %
- OK · T5: FCF verdadero 68, A1 = 68, A0 = 58; el exceso es la D&A ROU
- OK · T5: f_A0 − f_A1 = ρ = D&A ROU ÷ ventas
- OK · T5 con arrendamiento mínimo: FCF verdadero 79,76; A0 da 79,56 (0,2 de menos)
- OK · T5 con arrendamiento ínfimo: FCF verdadero 79,94; A0 da 79,89 (0,05 de menos, lo que el AVISO de la propuesta toleraría)
- OK · FCF base cero o negativo: el motivo mostrado es que la medida no está definida
- OK · vigente (sin umbral), D&A ROU positiva y C49 positivo: V-F1a BLOQUEA
- OK · vigente (sin umbral), D&A ROU cero y C49 cero: A0 admisible
- OK · vigente (sin umbral), D&A ROU positiva y C49 cero: V-F1m BLOQUEA
- OK · vigente (sin umbral), D&A ROU cero y C49 positivo: V-F1m BLOQUEA

## Reglas erróneas que los casos detectan

- frontera estricta en el umbral sobre el FCF base: detectada (F07, F10, F14, F16, F21; 0 comprobaciones directas)
- frontera estricta en la resolución: detectada (F12; 0 comprobaciones directas)
- frontera de la versión 1 al revés: detectada (F16; 0 comprobaciones directas)
- sin la guarda del FCF base no positivo: detectada (ningún caso; 1 comprobaciones directas)
- coeficientes sin compensar: detectada (F24; 1 comprobaciones directas)
- dominio de A0 con «y» en lugar de «o»: detectada (F02, F03; 2 comprobaciones directas)

## Elis (solo información; no es criterio)

- nota: solo información, con cifras verificadas; no es criterio para elegir ningún umbral. Por la decisión (1a), Elis no usa A0_total
- X_D&A_ROU_media_2023_25: 132.5
- FCF_base_registrado: 307.933
- e_sobre_el_FCF_base_pct: 43.03
- rho_sobre_las_ventas_pct: 2.9057
- B_cota_de_redondeo_del_FCF_base: 0.25
- X_sobre_B: 530.0
- estado_con_A0_total: U0: V-F1a BLOQUEA; UP01: V-F1a BLOQUEA; UR: V-F1a BLOQUEA; UP1: V-F1a BLOQUEA; UP5: V-F1a BLOQUEA; UV1: V-F1a BLOQUEA
- estado_con_el_perimetro_de_(1a): no aplica
- referencias_de_tamaño:
  - cota_de_redondeo_del_FCF_base_pct: 0.081
  - residuo_del_interes_de_arrendamiento_en_C48 (informe §5.4): importe: 0.133; pct_del_FCF_base: 0.043
  - alcance_de_N1_en_2022_25 (opción B del alcance): importe: -0.302; pct_del_FCF_base: 0.098
  - alcance_de_N1_en_2021_25_sin_efecto_fiscal (opción A del alcance): importe: 0.416; pct_del_FCF_base: 0.135
  - actualizacion_del_earnout: importe: -0.79; pct_del_FCF_base: 0.257
