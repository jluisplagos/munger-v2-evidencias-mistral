# Seguimiento dirigido del frente C · 16-nov-2026

Commit revisado: `ba46ea51a33a87dc8f2a03668b0e44dd79735d09`.

**C1 aritmético e interpretación de D7: resueltos.** Se verificó el manifiesto de 22 entradas y se ejecutaron de nuevo el autotest y los seis scripts: 57 casos, diez propiedades globales conformes, residuo máximo frente al producto 2,842e-14, 192 puntos de sensibilidad y 24/24 correspondencias de cobertura. La tabla Caja da +1,538645906781241 €, como D7. No se adoptan políticas ni se modifica el producto.

**C2 pendiente: la guarda declarada no compara los extremos.** En `codigo/efectos_probabilidades.py`, las filas llevan un texto `misma_pregunta = OK` escrito directamente. La variable `mal` busca `PREGUNTA_DISTINTA` en ese texto, sin comparar los atributos de los extremos. Por tanto, se comprueba una etiqueta que el mismo generador acaba de asignar.

Sonda ejecutada sobre copia aislada: cambiar `perimetros.H6` de Caja a NIIF 16, dejando H5 en Caja. Resultado: código 0, guarda OK y fila con «Caja → NIIF 16» que todavía afirma «mismo perímetro Caja en ambos extremos». Detalle en `SONDA_C_GUARDA_ba46ea5.json`. Se restauró la copia y se regeneró la salida original. Esto no demuestra un importe real incorrecto; demuestra que la protección anunciada no funciona.

Corrección acotada solicitada:

1. Representar cada extremo con identidad de caso, empresa y perímetro canónicos, vinculados al mismo vector y fuente. Las descripciones de fecha/variante no se comparan como si fueran el perímetro.
2. Hacer que una función compare realmente `(empresa, perímetro)` de ambos extremos. Derivar de ella la etiqueta: misma empresa y perímetro admite comparación entre años; mezclar cualquiera de ambos se rechaza como equivalente o se marca `PREGUNTA_DISTINTA`.
3. Hacer que la generación use esa función, también para comprobar los cambios totales. No basta con añadir una función solo llamada desde un test. Incluir pruebas positivas Caja/Caja y NIIF16/NIIF16 entre años, y negativas Caja/NIIF16 y empresas distintas, además de la sonda descrita arriba. Los controles negativos esperados no son fallo del banco; una mezcla inesperada no puede terminar como OK.
4. Regenerar lo afectado, actualizar respuesta, declaraciones y manifiesto, publicar commit y terminar. No abrir revisión general, decisiones D1/D7/D11, valoración, cambios del oráculo o cambios del producto.

La siguiente comprobación se limita a esta guarda y sus salidas; la aritmética e interpretación de D7 ya reproducidas se conservan.
