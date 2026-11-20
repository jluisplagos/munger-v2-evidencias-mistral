# Análisis directo · VINCI SA, ejercicio 2025 y primer semestre de 2026

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | vinci |
| Fecha de corte | 2026-10-10 |
| Tasa | 9 % |
| Tarea | analisis-directo-vinci-44719920278 |
| SHA del código | 779b55abd380e8427650233fcb8a9c9fa74472f4 |
| Huella del paquete (package_sha256) | 681b69cab6bdba6620bb6ccfe030c9c787f7a87246eaa09dc8e454bb7bd069ef |
| Huella del envío (bundle_sha256) | 7ed5bb74769dd05d72a6db14dca620570591df5b4c0149171129538fcb394055 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | medium |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 955096 tokens |
| Reserva estimada antes de llamar | USD 4.475744 (máximo de la ejecución USD 4.5) |
| Reserva registrada | USD 4.475744 |
| Uso de tokens | entrada 391893, salida 18309 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 1.933752; cota 1.933752 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| datos_v63_md | datos_analisis_directo/vinci/datos_v63.md | 779b55abd380 | 6d36d27cc745ffeb96f7b52eebfa287a1067953679bfd8c32881afdd89534ed4 | 94173 |
| extracto_v63_md | datos_analisis_directo/vinci/extracto_v63.md | 779b55abd380 | d076d0c11dc0cc1755f1cbac59286afcf757f651a2759cd22eb105d3f9fd649a | 20364 |
| fase1_v63_json | datos_analisis_directo/vinci/fase1_v63.json | 779b55abd380 | 4adeb78d8c27738f2ec90bdb0a849bbf6b7e551849a2b3701441f94ef815a212 | 73769 |
| etapa1_vinci_analisis_csv | datos_analisis_directo/vinci/etapa1/Vinci_evaluada__Análisis.csv | 779b55abd380 | fbfca000e72248fb1fc219336a703d6f7a1e955285021dbd9e714108ea96c48c | 22795 |
| etapa1_vinci_control_maestro_csv | datos_analisis_directo/vinci/etapa1/Vinci_evaluada__Control_maestro.csv | 779b55abd380 | 586f8f22c41973277faaac8a07bd87d458792c14399d851a9e2a767006d3f14c | 61550 |
| etapa1_vinci_guia_sws_csv | datos_analisis_directo/vinci/etapa1/Vinci_evaluada__Guía_Simply_Wall_St.csv | 779b55abd380 | e3cabea03c1a776ed1203ce43f216ec3b29760e8c866e2b925b8990e31152651 | 7660 |
| etapa1_vinci_opciones_csv | datos_analisis_directo/vinci/etapa1/Vinci_evaluada__Opciones.csv | 779b55abd380 | 56246fb2e5ca7ca826b3c07c4786422bb1cf9c5a3a0d110abc53919735356a4d | 1486 |
| etapa1_vinci_respuesta_md | datos_analisis_directo/vinci/etapa1/Vinci_respuesta.md | 779b55abd380 | 63411305c449466d47e60a360db4c1292490912fc8b17c2641337a00b67307af | 33150 |
| fuentes_urd_2025_seleccion | datos_analisis_directo/vinci/fuentes/vinci-urd-2025.seleccion.compacto.txt | 779b55abd380 | c82d6e4111c908f622345890cef2c995bfcd95334c06dfe36e323c4017254d76 | 394367 |
| fuentes_semestral_2026_seleccion | datos_analisis_directo/vinci/fuentes/vinci-hy-report-2026.seleccion.compacto.txt | 779b55abd380 | 719bfff7ae4dcef015e1d01c42ce603f1407f2e08dd9c5bfd58ffec21c1d6c32 | 192408 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `caro`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 63.9 | 0.2 |
| normal | 102.6 | 0.6 |
| bueno | 141.3 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 107.05 | |
| Precio del escenario malo | 63.9 | 63.9 |
| P* | 91.54 | 91.5429 |
| Precio de Sí = mín(P*, V_normal) | 91.54 | 91.5429 |
| Ponderado | 102.6 | 102.6 |
| Crecimiento implícito al precio actual / del normal (%) | 4.3 / 3.5 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 138.81 | 156.18 | cumple_regla_k |
| 8 % | 110.8 | 124.24 | cumple_regla_k |
| 9 % | 91.54 | 102.6 | caro |
| 10 % | 77.41 | 86.86 | caro |
| 11 % | 66.39 | 74.66 | caro |

### Resumen

    VINCI combina autopistas francesas que vuelven al Estado sin compensación entre 2032 y 2036 con negocios más duraderos: aeropuertos, VINCI Energies, Cobra IS y construcción. Para no tratar como perpetuo un flujo que caduca, la valoro por suma de partes al 9 %. Las autopistas se valoran solo hasta su vencimiento y el resto como perpetuidades. Después resto la deuda neta, el valor de los minoritarios de Gatwick, Edimburgo y OMA, la SBC capitalizada y el déficit de pensiones. Salen unos 64 € en el escenario malo, 103 € en el normal y 141 € en el bueno. El ponderado es 102,6 € y el precio de Sí con k = 3 es 91,5 €. A 107,05 € la acción está en zona cara al 9 % y no deja margen. El resultado es muy sensible a la tasa: al 8 % cumpliría la regla k y al 10 % quedaría claramente cara. Cubo Vigilar, acción esperar.


### Moneda

    EUR


### Justificación

    Estado: concluido. Con la suma de partes puedo acotar el valor por escenarios aunque falten flujos y deuda concesión por concesión.
    Cubo: Vigilar. El negocio se entiende, tiene activos de calidad (Energies con un rendimiento de alrededor del 39 % sobre el capital empleado, aeropuertos en propiedad plena) y un balance A−. Pero a 107,05 € el precio está por encima del ponderado (102,6 €) y del precio de Sí (91,5 €). Además, el escenario malo implica perder cerca del 40 %.
    Acción: esperar. Volvería a mirarla por debajo de unos 91 €, con los hechos intactos.


### Probabilidades

    Mantengo 0,2 / 0,6 / 0,2. El riesgo fiscal y el del vencimiento ya están dentro de las cifras de cada escenario, y el paquete no da información sobre negociaciones de prórroga que justifique mover las probabilidades.


### Fórmula aplicada

    Para P entre 63,9 y 102,6:
    G(P) = 0,6·(102,6−P) + 0,2·(141,3−P) = 89,82 − 0,8P
    L(P) = 0,2·(P − 63,9)
    G ≥ 3L ⇔ 89,82 − 0,8P ≥ 0,6P − 38,34 ⇔ P ≤ 128,16 / 1,4 = 91,54
    Precio de Sí = mín(91,54; 102,6) = 91,54
    Ponderado = 0,2·63,9 + 0,6·102,6 + 0,2·141,3 = 102,6
    El precio de 107,05 es mayor que 102,6, así que la zona es caro.


### Crecimiento implícito

    Es una aproximación, porque el modelo es una suma de partes y no se construye sobre ventas.
    - El normal supone un crecimiento de ventas del grupo de alrededor del 3,5 % anual a cinco años: Energy Solutions al 5-6 %, construcción plana, aeropuertos al 2-3 % y autopistas planas.
    - Para llegar a 107,05 € faltan 4,45 € por acción, unos 2.470 M.
    - Un punto adicional de crecimiento anual en los negocios que crecen (unos 69.000 M de valor) añade cerca de 3.000 M neto de reinversión.
    - Por tanto, el precio descuenta unos 0,8 puntos más, es decir, alrededor del 4,3 % anual.

### Escenario malo

    Suma de partes al 9 %, en millones de euros.
    - Autopistas: 15.000, sin prórroga, con la carga fiscal extra de forma permanente y tráfico débil (-2,9 % en el primer semestre de 2026).
    - Airports: FCF normalizado de 1.450 con g del 1,5 %, 19.620.
    - VINCI Energies: 1.000 con g del 2,5 %, 15.770.
    - Cobra IS: 5.000 (EPC y renovables decepcionan).
    - Construcción: 700 con g del 1 %, 8.840.
    - Otras concesiones: 1.500. Immobilier: 500.
    Total operativo: 66.230.
    Ajustes: -6.000 de SBC capitalizada, +3.156 de puestas en equivalencia (2.051) e instrumentos de patrimonio (1.105), -22.450 de deuda neta a 30-jun-2026, -900 de pensiones y -4.500 de minoritarios.
    Resultado: 35.536 / 555,967 M acciones = 63,9 €.

### Escenario normal

    Suma de partes al 9 %, en millones de euros.
    - Autopistas: FCF sin apalancar de unos 3.000 al año. Parto de un Ebitda de 4.784, resto una inversión de 588 y un impuesto de unos 1.200, y lo ajusto al alza porque la contribución excepcional no se repite siempre. Se descuenta como anualidad hasta el vencimiento de ASF (2036), Cofiroute (2034) y Escota (2032): 18.500.
    - Airports: Ebitda 3.042, FCF normalizado de unos 1.600 al 100 %, g del 2,5 %: 25.000.
    - VINCI Energies: Ebit 1.606, FCF normalizado de 1.150, g del 3,5 %: 21.000.
    - Cobra IS: Ebit 644, incluye Zero.e: 7.500.
    - Construcción: Ebit 1.353, FCF normalizado de 878, g del 2 %: 12.000.
    - Otras concesiones: 2.500. Immobilier: 700.
    Total operativo: 87.200.
    Ajustes: -6.000 de SBC (422 no caja capitalizados), +3.156 de participaciones, -21.000 de deuda neta (media entre 19.075 en diciembre y 22.450 en junio, por la estacionalidad del circulante), -900 de pensiones y -5.400 de minoritarios (unos 338 de resultado a unas 16 veces).
    Resultado: 57.056 / 555,967 = 102,6 €.

### Escenario bueno

    Suma de partes al 9 %, en millones de euros.
    - Autopistas: 22.000, con prórroga parcial o compensación por las inversiones nuevas.
    - Airports: FCF de 1.800 con g del 3 %, 30.900 (pista norte de Gatwick y plan de OMA a inflación +6,9 %).
    - VINCI Energies: 1.250 con g del 4 %, 26.000.
    - Cobra IS y Zero.e: 10.000 (Ebitda de Zero.e por encima de 400 en 2030).
    - Construcción: 950 con g del 2,5 %, 14.980.
    - Otras concesiones: 3.500. Immobilier: 900.
    Total operativo: 108.280.
    Ajustes: -6.000 de SBC, +3.156 de participaciones, -20.000 de deuda neta, -900 de pensiones y -6.000 de minoritarios.
    Resultado: 78.536 / 555,967 = 141,3 €.

### Sensibilidad (comentarios)

    7 %: Malo 95,4 / normal 155,9 / bueno 217,8. Las perpetuidades de aeropuertos y Energies dominan el valor. Solo informativo.
    8 %: Malo 77,2 / normal 124,2 / bueno 171,4. Con un punto menos de tasa, el precio actual ya cumpliría la regla k, lo que muestra que la conclusión es frágil ante la tasa.
    9 %: Malo 63,9 / normal 102,6 / bueno 141,3. Es la tasa de conclusión y coincide con la escalera.
    10 %: Malo 53,8 / normal 86,9 / bueno 119,8.
    11 %: Malo 45,7 / normal 74,7 / bueno 103,5.

### Qué haría falsa la conclusión

    - Una prórroga o compensación contractual de ASF, Escota o Cofiroute que alargue los flujos de las autopistas más allá de 2032-2036 (subiría el malo y el normal y acercaría el cubo a Sí).
    - Que la acción cotice por debajo de unos 91 € sin deterioro de los hechos (pasaría a Sí).
    - Un nuevo gravamen francés permanente sobre las concesiones, o un cambio unilateral de tarifas o contratos, más allá de la contribución excepcional prorrogada en 2026 (empeoraría el normal: No).
    - Deterioros en Cobra IS (goodwill de 4.156) o en los aeropuertos, o que Zero.e no alcance el Ebitda de más de 400 previsto para 2030 (empeoraría la valoración).
    - Que el FCF publicado de 2026 quede muy por debajo de la guía de unos 6.000 M sin una causa puntual, o que se revierta la entrada de circulante de 2.496 M de 2025.
    - Que el margen de VINCI Energies siga subiendo y su crecimiento orgánico se mantenga por encima del 5 % varios años, lo que acercaría el bueno.

### Lo que no sabe

    - Deuda, flujos y obligaciones de fin de contrato concesión por concesión: solo tengo VINCI Autoroutes agregado, con deuda neta de 14.677 y FCF de 2.639. El reparto entre ASF, Cofiroute y Escota lo aproximo por ingresos.
    - Los FCF por segmento ajustados a una normalidad sin circulante son estimaciones mías a partir de Ebit, D&A, inversiones y arrendamientos por segmento. La asignación del impuesto por segmento y del FCF a minoritarios es aproximada (resultado de minoritarios de 144 + 143 + 51 y dividendos de 805).
    - El precio de 107,05 € del 9-oct-2026 viene de proveedores secundarios y está pendiente de verificación en una fuente oficial. Incluye el dividendo a cuenta de 1,10 € (fecha ex 13-oct-2026).
    - Uso 555,967 M de acciones a 31-dic-2025. A 30-jun-2026 había 585.891.697 emitidas y 31.748.863 en autocartera (unos 554,1 M netas). La cifra de 551,55 M a 30-sep-2026 no está entre las fuentes primarias del paquete.
    - El paquete incluye decisiones metodológicas fechadas después del corte (23-oct-2026, 18-nov-2026 y 19-nov-2026). Uso sus cifras solo como datos contables de fuentes anteriores al corte, no como hechos posteriores. La información de los nueve meses de 2026 no está en el paquete ni la uso.
    - No conozco los múltiplos ni el retorno sobre el precio pagado en las compras (Gatwick, Edimburgo, OMA, Northwest Parkway, Cobra IS), ni las subidas anuales de peaje de ASF y Escota.
    - La valoración de minoritarios, SBC y Cobra IS / Zero.e es una estimación con incertidumbre alta. La sensibilidad a la tasa es muy grande: entre el 8 % y el 10 % la zona cambia de cumplir la regla k a cara.
    - La hoja indica que la r mínima calculada (9,1 %) es algo superior al 9 % usado. Concluyo al 9 % como se pide.

### Citas

    [datos_v63_md] «último cierre en Euronext Paris del 9-oct-2026, 107,05 €» → Precio actual y fecha.
    [datos_v63_md] «555.967.094 = derechos de voto netos» → Acciones en circulación usadas para el valor por acción.
    [datos_v63_md] «FCF base (C52, fórmula): 4419.33» → FCF normalizado del grupo, como contraste de la suma de partes.
    [fuentes_urd_2025_seleccion] «Free cash flow 2,639 1,245 5 3,890 1,568 (365) 1,204 1,397 313 1,710» → FCF de 2025 por línea de negocio (Autoroutes, Airports, Energies, Cobra IS, Construction).
    [fuentes_urd_2025_seleccion] «4,784 3,042 344 8,169 2,019 786 2,805 2,133 61 2,194» → Ebitda de 2025 por línea de negocio, base de los FCF normalizados.
    [fuentes_urd_2025_seleccion] «VINCI Energies 1,606 7.4% 1,474 7.2% +132 +9.0%» → Ebit y margen de VINCI Energies.
    [fuentes_urd_2025_seleccion] «Cobra IS 644 8.0% 553 7.8% +91 +16.4%» → Ebit de Cobra IS.
    [fuentes_urd_2025_seleccion] «VINCI Construction 1,353 4.2% 1,304 4.1% +49 +3.7%» → Ebit de VINCI Construction.
    [fuentes_urd_2025_seleccion] «ASF network (excl. Puymorens Tunnel) 2,731 km France 100% 2036» → Vencimiento de ASF.
    [fuentes_urd_2025_seleccion] «Cofiroute network (excl. A86 Duplex tunnel) 1,100 km France 100% 2034» → Vencimiento de Cofiroute.
    [fuentes_urd_2025_seleccion] «Escota network 471 km France 99.5% 2032» → Vencimiento de Escota.
    [fuentes_urd_2025_seleccion] «the concession infrastructure is returned to the grantor for no consideration» → Las autopistas se valoran solo hasta el vencimiento.
    [fuentes_semestral_2026_seleccion] «Net financial debt (22,450) (23,336) +886 (19,075)» → Deuda neta a 30-jun-2026 y a 31-dic-2025.
    [fuentes_semestral_2026_seleccion] «VINCI Autoroutes (14,677) (10,504) 3x» → Deuda neta de las autopistas que debe devolverse antes del vencimiento.
    [fuentes_urd_2025_seleccion] «of which attributable to non-controlling interests 144 143 51» → Resultado de minoritarios de Gatwick, OMA y Edimburgo, base de su valor restado.
    [fuentes_urd_2025_seleccion] «– to non-controlling interests 23.5 (805) (902)» → Dividendos pagados a minoritarios.
    [fuentes_urd_2025_seleccion] «Share-based payments (IFRS 2) - - - 422 - - - 422 - 422» → SBC no caja de 2025 capitalizada y restada.
    [fuentes_semestral_2026_seleccion] «Investments in companies accounted for under the equity method 10 2,051 2,111 1,995» → Valor de las puestas en equivalencia sumado.
    [fuentes_semestral_2026_seleccion] «Equity instruments 1,105 1,146» → Instrumentos de patrimonio (incluido el 8 % de ADP) sumados.
    [fuentes_urd_2025_seleccion] «Deficit (or surplus) I − II 892 965» → Déficit de pensiones restado.
    [fuentes_urd_2025_seleccion] «anticipates a charge in 2026 of the same magnitude as that recorded in 2025» → Persistencia de la contribución fiscal excepcional.
    [fuentes_semestral_2026_seleccion] «VINCI Autoroutes’ traffic levels fell by 2.9% in the first half.» → Debilidad del tráfico en 2026.
    [fuentes_semestral_2026_seleccion] «free cash flow could reach €6 billion» → Guía de FCF de 2026 confirmada.
    [fuentes_urd_2025_seleccion] «Changes in operating working capital requirement and current provisions 19.1 2,496 2,311» → Entrada de circulante excluida del FCF normalizado.
    [fuentes_urd_2025_seleccion] «Capital employed at 31/12/2025 16,647 24,102 5,590 46,339 4,122 5,340 9,462 783 1,108 1,892» → Capital empleado por negocio, para juzgar la rentabilidad de cada parte.
    [fuentes_urd_2025_seleccion] «of which €852 million related» → Inversión en renovables de Cobra IS que hace negativo su FCF.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 91.54285714285713,
          "precio_si": 91.54285714285713,
          "ponderado": 102.6,
          "precio_escenario_malo": 63.9
        },
        "citas_total": 26,
        "citas_literales": 26,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

