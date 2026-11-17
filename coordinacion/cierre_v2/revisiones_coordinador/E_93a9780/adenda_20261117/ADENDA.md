# Adenda a la revisión de E-ELIS @ 93a9780 · verificación de los 11 PDF provisionales y de las 28 citas (coordinador, 17-nov-2026)

**Por qué ahora.** La reanudación (`c241a59`) aclara que «no contactar con terceros» no prohíbe descargar documentos de URL públicas oficiales para revisar. Con esa aclaración, el coordinador descargó los 11 PDF de sus URL declaradas, en una carpeta nueva fuera de Git.

## Resultado

- **11 de 11 PDF:** HTTP 200 y la URL final declarada. Bytes y SHA-256 **idénticos** a los de `FUENTES_Y_BUSQUEDA.csv`; las páginas, las declaradas (`descargas_verificacion.tsv` y `paginas.tsv`).
- **28 de 28 citas en su página declarada** (`citas_E.py`, `citas_E.out`), con dos notas:
  - 26 están literalmente en la página;
  - la de la factsheet, p.1, está en orden de lectura (maquetación a columnas);
  - la de la presentación FY2025, p.29, tiene impreso el marcador de nota «5» entre el rótulo y la cifra: `Acquisitions of subsidiaries, net of cash acquired 5 (117.6) (183.3)`. La cita registrada lo omite. **Es una precisión de la cita, no un cambio de cifra.**

## Lo que no cambia

- **La preservación duradera sigue pendiente.** La copia del coordinador está en un sandbox efímero. Los 11 PDF siguen siendo PROVISIONALES (U1).
- **Las correcciones E-R1…E-R9 siguen vigentes.** Que una cita esté en su página no corrige su interpretación: N2 y M6 (E-R1 y E-R2). La revisión anterior marcó NO OBSERVABLES 21 citas; ahora son observables, y su verificación sale bien.
- **Elis sigue `pendiente_de_datos`.** Nada desbloquea R, θ ni λ.
