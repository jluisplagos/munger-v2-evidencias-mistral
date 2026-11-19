# Cribado · Seche

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-05 |
| Tarea | cribado-44512238939-seche |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | ea01cbc81d2537ed26fd06a5fed1c926b81f39a2875d82958c0ee510bc7094c1 |
| Huella del envío (bundle_sha256) | 8d91211f26d6c9cf98665d8d8e6e25f17b46046a878b2d2ce1603537a4a20be2 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 23f97e4efe1a288ed8cbacd98a05a1c2d3d590c1bca89eff55eab5d259b9c8a9 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 155364 tokens |
| Reserva estimada antes de llamar | USD 1.276816 |
| Uso de tokens | entrada 69734, salida 4116 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.361256; cota 0.361256 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Seche/Seche_respuesta.md | 750e5ca10d7b73a887eafd8cb9f6ee55cbc77e6c0f9120427a43df8d58e4ba70 | 45319 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Seche/Seche_evaluada.xlsx#Análisis | 439834f8bc0e33f24c27a0003929409fa310891bec781c2712ca7df2e376b681 | 24403 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Seche/Seche_evaluada.xlsx#Control maestro | ed3c07e06484cbd0c87f646f07a1461844b1a4490a7687277a9c3fe1d657acef | 64798 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | no_pasa |
| caja | dudoso |
| balance | dudoso |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 92.9 (mm EUR a 30/06/2026; dentro de la deuda bruta de 1267,1 de Análisis!C54)


### Tipo de negocio y motor

    Servicios medioambientales intensivos en capital (tratamiento de residuos peligrosos y no peligrosos, con concesiones DSP y un componente cíclico de precios de energía y química), crecimiento vía adquisiciones con deuda e híbrido
    Caja libre al accionista de ciclo medio que incluya la inversión concesiva IFRIC 12 y el cupón del híbrido, contrastada con una suma de partes Francia/Internacional y con el valor de las DSP hasta su vencimiento.

### calidad

    El negocio se entiende y la demanda regulada parece duradera, pero el ROCE antes de impuestos es del 5,5 % (4,2 % después) frente a un coste propio del 8,15 %, y cae desde el 11,0 % de 2022 con márgenes EBE que bajan del 23,1 % al 19,6 %; la ventaja no aparece en las cifras (coincide con el cubo No de la respuesta, no con el «demasiado difícil» de Análisis!A6)
    Dato clave: Análisis!C24 = 0.055

### caja

    La caja libre al accionista es positiva pero pequeña (31,6 mm frente a una CFO de 204,9 y un capex de 95,5), y en 2025 se apoyó en 30,7 mm de liberación de BFR; además deja fuera unos 110 mm/año de inversión concesiva IFRIC 12, así que su recurrencia no está demostrada
    Dato clave: Análisis!C52 = 31.6

### balance

    Sin arrendamientos, la deuda neta de unos 664,4 mm equivale a 3,29x el EBE pre-NIIF 16 y a unas 21x la caja libre de 31,6 mm, con un híbrido de 300 mm fuera de la cifra (unas 4,8x si se cuenta) y Flamme llevándola hacia unas 4,1x frente a un covenant de 4,0x; la liquidez es holgada (caja 509,7, vencimiento medio 3,5 años), por eso queda en dudoso y no en no_pasa, aunque es alta para un negocio con parte cíclica (el 3,22x de Análisis!C33 incluye arrendamientos y no sirve tal cual)
    Dato clave: Control maestro!N36 = 3.29 (deuda neta sin arrendamientos ≈ 664,4 = financiera 1168,6 + derivados 5,5 − caja 509,7, de Control maestro!M51; sobre EBE pre-NIIF 16 ≈ 202,3)

### precio

    La cotización de 77,6 € supera con claridad el precio de Sí de unos 41,7 € y el ponderado de 64,0 €, y exige un crecimiento del 6,1 %; incluso con r del 7 % el ponderado (88,7 €) la supera, pero el escenario malo no la alcanza, y el DCF de la plantilla es de aplicabilidad dudosa (Análisis!C62 = financiación inestable)
    Dato clave: Análisis!B78 = 41.6521725125968 (precio de Sí) frente a Análisis!C37 = 77.6

### encaje

    El paquete no trae la cartera de la persona responsable; la capitalización de 600 mm solo es contexto, y este filtro no elimina
    Dato clave: Análisis!C41 = 600

### Qué lo cambiaría

    - Un ROCE antes de impuestos por encima del 8–10 % dos años seguidos con el perímetro ya comprado.
    - Un EBE de 2026 dentro de 260–270 mm con una deuda neta sin arrendamientos por debajo de 3x el EBE sin bajar la caja libre.
    - Una cotización por debajo de unos 42 € por acción si la calidad pasara.

### Qué falta

    - Detalle de la inversión concesiva IFRIC 12 (unos 110 mm/año): cuánto se recupera por canon y en cuántos años, porque cambia la caja libre real.
    - Texto del covenant del RCF y calendario de vencimientos por año, incluido el efecto de financiar Flamme (unos 300 mm).
    - ROCE y margen por zona o actividad (Francia frente a Internacional); la cotización procede de una fuente secundaria.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro balance: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

