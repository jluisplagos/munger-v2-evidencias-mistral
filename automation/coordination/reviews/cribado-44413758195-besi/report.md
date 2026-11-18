# Cribado · BESI

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-24 |
| Tarea | cribado-44413758195-besi |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 7c5ca2fae19774563808734d52bc12d75bfde32cea785e1b65aa50d2b086cb37 |
| Huella del envío (bundle_sha256) | a96acff04c4fa476575a4b56bcf44df5bb1b6b04853bf5a83bdbe48b0d2fa526 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | fa96c1bde3416c3802368253127b4b00a43e949268de859cdb8d81df3a0f8e21 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 152225 tokens |
| Reserva estimada antes de llamar | USD 1.26426 |
| Uso de tokens | entrada 69236, salida 4941 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.375764; cota 0.375764 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/BESI/BESI_respuesta.md | 69a0ecb0a58ef3c70aeae3c0fe773640438dc83566c48f55db5f0994e986f6ea | 43395 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/BESI/BESI_evaluada.xlsx#Análisis | 131472cfa93aa47f75ad7c5321825e6a03344e7fb5c3bf2cb501fd98f9108d6c | 23910 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/BESI/BESI_evaluada.xlsx#Control maestro | 361258a93ea668d4de83c6beed8261cf65768ebb718c1b1152e9e12fbf40e3d0 | 63880 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = ≈12,2 M€ (pasivo por arrendamientos estimado, incluido en Análisis!C54 = 357.5; fuera del cociente de deuda)


### Tipo de negocio y motor

    Fabricante de equipos de ensamblaje back-end para semiconductores (die attach, advanced packaging, hybrid bonding): industrial tecnológico cíclico, con caja neta.
    Caja libre de ciclo medio (normalizada a lo largo del ciclo de equipos de semiconductores, entre la base de valle de 136,2 M€ y el LTM de 242,6 M€), con contraste de la economía del hybrid bonding.

### calidad

    El negocio se entiende (C11 = Sí) y la ventaja se ve en las cifras: ROIC del 32,3% LTM, media del 21,1% en FY19-25 y margen bruto del 48,8% al 65,2%; pero depende del ciclo, con caídas de ingresos superiores al 30%, y de una transición tecnológica cuyo foso a diez años la etapa 1 no defiende (C18 = No); es una duda de estudio, no un «no se entiende», y por eso discrepo del «demasiado difícil» de la hoja.
    Dato clave: Análisis!C24 = 0.323

### caja

    La caja libre ha sido positiva todos los años de 2018 a 2025 (entre 104,4 y 249,5 M€ antes de SBC), con CFO/beneficio neto de 1,122 (Análisis!C26) y un capex pequeño, aunque no crece de forma sostenida: la de 2025 queda por debajo de la de 2018 (C25 = No).
    Dato clave: Análisis!C52 = 136.2

### balance

    Sin arrendamientos la deuda son 345,3 M€ de bonos al 4,5% con vencimiento en 2031, frente a 371,9 M€ de caja (Análisis!C53) más 220,0 M€ de depósitos, es decir, caja neta de 246,6 M€ y deuda neta/EBITDA de −0,62x (Control maestro!N36), holgado incluso para un negocio cíclico.
    Dato clave: Análisis!C54 = 357.5 (incluye ≈12,2 de arrendamientos); sin arrendamientos: senior notes 345,3 según Control maestro!N51, caja neta 246,6

### precio

    A 145,1 € la cotización supera con creces el valor ponderado de 41,2 €, el escenario bueno de 68,2 € (Análisis!D78) y el caso con r = 7% (65,3 €, Análisis!D90); además, el precio exige un 26% de crecimiento anual de la caja libre (Análisis!C86) y el rendimiento sobre la caja libre LTM de pico es solo del 2,2% (Análisis!C41), así que la conclusión no depende de que la base de 136,2 M€ sea de valle.
    Dato clave: Análisis!C83 = 41.2470793551225 frente a Análisis!C37 = 145.1

### encaje

    El paquete no trae la cartera y la hoja solo aporta contexto de volatilidad (rango de 52 semanas de 120,15-328,40 € en Control maestro!N38), así que este filtro no elimina.
    Dato clave: no consta en la hoja

### Qué lo cambiaría

    - Una cotización por debajo del valor del escenario bueno de la hoja (≈68 €), que acercaría el precio y llevaría el veredicto a estudiar a fondo.
    - Dos o tres ejercicios de caja libre por encima de 250 M€ con el circulante normalizado, que elevarían la base de la valoración.
    - Una caída de la cuota en colocación avanzada o un competidor con un cliente ganado en hybrid bonding, que rebajarían la calidad y llevarían el veredicto a descartar.

### Qué falta

    - Márgenes y economía separados del hybrid bonding frente al negocio mainstream, y mapa competitivo con cuota conciliada entre informes (no se publican).
    - Una caja libre de ciclo medio definida: la base de 136,2 M€ es una media de valle FY23-25 que incluye 10,5 M€ no recurrentes del edificio de Duiven, frente a 242,6 M€ LTM tras SBC.
    - Duda de fuente: Control maestro cita una decisión del inversor del 28-oct-2026 para fijar el periodo de C46-C50, posterior a la fecha de la hoja (24-oct-2026), y la auditoría (filas 88-97) sigue marcada como pendiente.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

