# Encargo para Mistral · M10 · Historia de diez años de las empresas de calidad del cribado

**Para pegar en ventanas nuevas de Mistral, una por bloque (dos empresas por bloque).** Fecha: 19-nov-2026. Encarga: el coordinador Claude. Revisa: un agente Claude distinto. Reglas de `AGENTS.md` (no escribir en `jluisplagos/munger-v2`, no subir PDF/XLSX a Git, no aprobar tu propio trabajo, **no valorar ni recomendar**).

## 1. Qué es

Es **el mismo trabajo que M4** (`coordinacion/cierre_v2/examen/ENCARGO_MISTRAL_M4_HISTORIAS.md`, rama `coordinacion/cierre-v2`): léelo entero y sigue sus definiciones, reglas y formato (`HISTORIA.csv`, cifra más reciente publicada, tal como está impresa, cero con evidencia o `no_encontrado`, página del visor, cita literal). Cambian solo las empresas y las fuentes: aquí descargas tú los informes anuales oficiales de los diez últimos ejercicios (2016–2025, o los diez últimos cerrados si el ejercicio no es natural) de la web de inversores de cada empresa o de su regulador, y anotas URL, fecha y SHA-256 de cada PDF (no lo subas a Git). Si un año no está disponible en la web oficial, dilo.

Sirve para la segunda vuelta del universo: el coordinador contrastará tu Historia con los datos de la etapa 1 de la persona responsable (`coordinacion/cierre_v2/universo_etapa1/`), **que no debes abrir** para no perder la independencia.

## 2. Bloques (dos empresas por ventana)

| Bloque | Empresas | Rama de entrega |
|---|---|---|
| 1 | ABB, ASML | `mistral/m10-b1` |
| 2 | Andina (Embotelladora Andina), Bioventix | `mistral/m10-b2` |
| 3 | FW Thorpe, Ferrari | `mistral/m10-b3` |
| 4 | Hermès, Inditex | `mistral/m10-b4` |
| 5 | Intuitive Surgical, L'Oréal | `mistral/m10-b5` |
| 6 | LVMH, Lifco | `mistral/m10-b6` |
| 7 | London Security, Moncler | `mistral/m10-b7` |
| 8 | Puig Brands, Rational | `mistral/m10-b8` |

Entrega en `resultados_universo/historia_independiente/<empresa>/HISTORIA.csv` y `ENTREGA.md` (una página por empresa), con commit y push al terminar cada empresa.

---

### Frase para pegar (cambia solo el número de bloque y la rama)

> Lee `coordinacion/cierre_v2/universo_etapa1/m10/ENCARGO_MISTRAL_M10_HISTORIAS.md` en la rama `coordinacion/cierre-v2` del repositorio `jluisplagos/munger-v2-evidencias-mistral` y haz **el bloque N**. Solo ese bloque. Entrega en la rama `mistral/m10-bN`.
