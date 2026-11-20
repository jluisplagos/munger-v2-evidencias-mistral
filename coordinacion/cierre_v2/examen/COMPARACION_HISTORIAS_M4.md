# Contraste de la Historia de diez años: Claude (fase 1) frente a Mistral (M4, a ciegas) · 18-nov-2026

| Empresa | Resultado | Diferencias y explicación |
|---|---|---|
| Ahold (ventana 5, contraste de las 210 cifras de `ahold_f1`) | 199 coinciden en la página citada; 1 «no»; 10 «no se encuentra» | El «no» es EBIT 2019 = 2.663 (derivado BAI − resultado financiero) frente al «Operating income» impreso 2.662: redondeo explicado. Los 10 «no se encuentra» son I+D (`null`, no publicado). |
| Jumbo (`jumbo_d` frente a la ventana 1) | ventas, EBIT, beneficio, CFO, capex, patrimonio, caja, acciones y D&A coinciden en 2016–2018 y 2020–2025 | **2019:** Claude toma el año natural 2019 (columna comparativa del informe 2020, 12 meses); Mistral el periodo de transición de 6 meses. Ninguno inventa cifras; la decisión J-T presuponía el de 6 meses. Pendiente de confirmar con la persona (recomendación del coordinador: año natural 2019, con el solape de 6 meses con 2018/19 anotado). |
| Zoetis (`zoetis_t1b` frente a la ventana 2) | ventas, beneficio, CFO, capex, patrimonio, caja y D&A coinciden en los diez años (incluidos 2020–2024, de OCR) | Deuda 2023 y 2024: 8–12 mm de diferencia = arrendamientos financieros, que Claude incluye en la deuda (US GAAP). SBC y acciones no se compararon por rótulos distintos. |

Además, Mistral entregó una segunda lectura OCR independiente de los 10-K 2020–2024 de Zoetis (rama `mistral/zoetis-texto-ocr`, Mistral OCR, estados financieros verificados contra la imagen, 0 inconsistencias aritméticas).
