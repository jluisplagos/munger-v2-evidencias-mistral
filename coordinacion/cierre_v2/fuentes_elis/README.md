# Fuentes oficiales de Elis · preservación (U1)

- `INDICE_11_PDF.csv`: por cada archivo, la URL oficial, los bytes, la SHA-256, las páginas y la fecha de verificación del coordinador.
- `SHA256SUMS`: las huellas, en formato `sha256sum -c`.
- `../../../.github/workflows/preservar_fuentes_elis.yml`: el flujo que, en esta rama, descarga los 11 PDF de sus URL oficiales, exige su huella exacta y crea la Release `fuentes-elis-e-20261117`. Usa solo el `GITHUB_TOKEN` del repositorio: no hay tokens personales ni PDF en Git.
- **Si el flujo no puede crear la Release**, la intervención mínima es una de estas:
  - en *Settings → Actions → General → Workflow permissions*, permitir «Read and write» al `GITHUB_TOKEN`;
  - subir a mano los 11 PDF y el índice a una Release desde la web, comprobándolos después con `sha256sum -c SHA256SUMS`.
