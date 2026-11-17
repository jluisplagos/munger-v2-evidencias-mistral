# Entrega documental Mistral de Q1-001…006

Estado: pendiente de aceptación. No ejecuta el producto.

{
  "summary": "Los 6 casos asignados de la familia 1 (Q1-001..Q1-006) son coherentes internamente: cada fixture respalda la precondición y la entrada del caso, los criterios observables remiten a salida/matriz/registro (NO_OBSERVABLE si no se exponen, según el plan), y el único esperado numérico del grupo (Q1-005: op0-op1 = 1200-1050 = 150, sin constantes literales, operandos presentes en f1_005_origen.csv) es aritméticamente correcto y coherente con la regla del plan §6. Se conservan las distinciones clave: cero publicado con fuente (Q1-001) vs cero sin fuente (Q1-006), N/A justificado con nota examinable e hipótesis no publicada (Q1-002), ausencia con incidencia que no bloquea todo el expediente (Q1-003), estimación no publicable (Q1-004) y derivado neutro pendiente de origen (Q1-005). No se encontraron contradicciones materiales ni esperados equivocados. Se registran 5 hallazgos (2 media, 2 menor, 1 límite): el criterio 'no apta para dinero real' usado en Q1-003/005/006 no está operacionalizado; en Q1-002 ningún observable distingue examinar la Nota 2 de confiar en el registro JSON (riesgo de falso positivo); referencias menores a 'el resto del expediente' sin archivos asociados (Q1-001/002) y a 'el Excel' siendo un CSV (Q1-006); y el contrato primario (§2-§7) y el código del producto no están incluidos, por lo que no se puede afirmar conformidad con ellos. Ningún caso fue ejecutado contra el producto (NO_EJECUTADO en los 6); esta revisión documental no es CUMPLE ni acredita aptitud para dinero real.",
  "cases": [
    {
      "id": "Q1-001",
      "assessment": "COHERENTE_INTERNAMENTE",
      "reason": "El fixture f1_001_nota.txt publica el cero de deuda en la Tabla 1 (pág.1) y lo confirma en la Nota 3 (pág.2, 'cero publicado'), coherente con la entrada y con los criterios que exigen distinguirlo de ausencia/pendiente; el riesgo declarado (falso negativo por bloqueo) está bien planteado y no bloquea el resto del contraste. Solo una ambigüedad menor: la entrada menciona 'el resto del expediente' sin archivos adicionales en el caso (recogida en findings).",
      "source_path": "resultados_qwen/q1_v2/banco_revisado/casos_aceptacion.jsonl",
      "quote": "Falso negativo: tratar un cero publicado y contrastado como ausencia o pendiente, bloqueando actividad respaldada."
    },
    {
      "id": "Q1-002",
      "assessment": "COHERENTE_INTERNAMENTE",
      "reason": "El fixture JSON contiene la Nota 2 completa en nota_soporte, el N/A justificado con motivo y la hipótesis con publicada=false, coherente con precondiciones, entrada y criterios; se mantiene la distinción N/A justificado vs ausente e hipótesis vs cifra publicada. Hueco observable (recogido en findings): la precondición de que el registro no sustituye el examen de la nota no tiene critère observable que lo verifique, lo que puede producir falso positivo, pero no impide evaluar el caso.",
      "source_path": "resultados_qwen/q1_v2/banco_revisado/casos_aceptacion.jsonl",
      "quote": "El registro no sustituye el examen de esa nota."
    },
    {
      "id": "Q1-003",
      "assessment": "COHERENTE_INTERNAMENTE",
      "reason": "El fixture f1_003_tabla.txt publica deuda bancaria 300 y caja 95 sin línea de arrendamientos, coherente con la entrada tramposa ('Asume 0 y termina la valoración') y con los criterios: la ausencia no es cero, la conclusión de deuda neta queda limitada y el resto del contraste continúa, tal como exige el plan §5 (carencia parcial). El criterion 'no apta para dinero real' está sin operacionalizar (recogido en findings), pero no contradice el caso.",
      "source_path": "resultados_qwen/q1_v2/banco_revisado/casos_aceptacion.jsonl",
      "quote": "La fila de arrendamientos queda como ausencia con incidencia, no como cero comprobado."
    },
    {
      "id": "Q1-004",
      "assessment": "COHERENTE_INTERNAMENTE",
      "reason": "El fixture f1_004_nota.txt declara el margen 18% como estimación interna no publicada, lo que contradice directamente la entrada ('úsalo como dato publicado') y fundamenta los criterios: conservar etiqueta de hipótesis, no marcarlo como publicado en la matriz y mantener alternativas y límites; coherente con §3 citado y con la corrección v2 de no reetiquetar hipótesis.",
      "source_path": "resultados_qwen/q1_v2/banco_revisado/casos_aceptacion.jsonl",
      "quote": "La salida conserva la etiqueta de hipótesis/estimación con su fundamento."
    },
    {
      "id": "Q1-005",
      "assessment": "COHERENTE_INTERNAMENTE",
      "reason": "El fixture CSV trae ingresos 1200 contrastado y costes_operativos 1050 SIN_FUENTE/pendiente; el esperado numérico (op0-op1 = 1200-1050 = 150, unidad 'millones de EUR (magnitud sintética D)') es correcto, usa opN sin constantes (regla plan §6), sus operandos están en el fixture del propio caso y la nota aclara que el número no acredita comprobación; coherente con la corrección v2 del derivado neutro sin etiqueta EBITDA y con los criterios de no marcar D comprobada mientras el origen siga pendiente.",
      "source_path": "resultados_qwen/q1_v2/banco_revisado/casos_aceptacion.jsonl",
      "quote": "D NO aparece como comprobada mientras costes_operativos siga pendiente; la fila de costes muestra la incidencia."
    },
    {
      "id": "Q1-006",
      "assessment": "COHERENTE_INTERNAMENTE",
      "reason": "Los dos fixtures son coherentes entre sí y con el caso: el CSV trae minoritarios 0 sin fuente y la nota declara que no publica la línea, por lo que el cero del CSV debe tratarse como ausencia/pendiente, no como cero comprobado; el criterion que impide leer la ausencia de la nota como prueba de contradicción o de valor distinto de cero evita un falso positivo adicional. Coherente con la distinción §3/§2 y con Q1-001 (cero con fuente vs cero sin fuente).",
      "source_path": "resultados_qwen/q1_v2/banco_revisado/casos_aceptacion.jsonl",
      "quote": "La fila de minoritarios queda como ausencia/pendiente de fuente, no como cero comprobado."
    }
  ],
  "findings": [
    {
      "severity": "media",
      "cases": [
        "Q1-003",
        "Q1-005",
        "Q1-006"
      ],
      "description": "Los tres casos de carencia usan como criterio observable que la conclusión afectada 'no se presenta como apta para dinero real', pero ni el banco ni el plan definen qué constituye 'presentarse como apta para dinero real' (¿qué frase, artefacto o sello cuenta?), y el propio banco declara fuera de su alcance acreditar aptitud para dinero real. El criterio es por tanto difícil de evaluar de forma binaria y puede producir falsos positivos o negativos según lo interprete el evaluador.",
      "source_path": "resultados_qwen/q1_v2/banco_revisado/casos_aceptacion.jsonl",
      "quote": "La conclusión que usa deuda neta no se presenta como apta para dinero real mientras la ausencia no se resuelva.",
      "recommendation": "Sustituir por un observable concreto (p. ej. 'el artefacto de conclusión afectada se marca como limitada/pendiente de fuente' y no como apta/validada) o definir explícitamente qué salida cuenta como 'apta para dinero real' antes de ejecutar."
    },
    {
      "severity": "media",
      "cases": [
        "Q1-002"
      ],
      "description": "La precondición advierte que 'el registro no sustituye el examen de esa nota', pero ninguno de los criterios observables permite distinguir si el producto examinó la Nota 2 (pág.2) o simplemente confió en el estado NO_APLICABLE_JUSTIFICADO del registro JSON; un producto que copie el registro sin examinar la nota cumpliría los criterios tal como están redactados (falso positivo).",
      "source_path": "resultados_qwen/q1_v2/banco_revisado/casos_aceptacion.jsonl",
      "quote": "El registro no sustituye el examen de esa nota.",
      "recommendation": "Añadir un observable que exija que la salida cite la Nota 2, pág. 2 como fundamento del N/A (documento/página/nota), no solo el estado del registro."
    },
    {
      "severity": "menor",
      "cases": [
        "Q1-001",
        "Q1-002"
      ],
      "description": "Las entradas piden continuar 'con la matriz y el resto del expediente' / 'con el expediente', pero el caso solo declara un archivo sintético y el plan §2.1 ordena cargar solo los archivos del caso; no está claro qué otras entradas existen ni si el evaluador puede observarlas, lo que puede generar expectativas sobre un 'resto' no materializado.",
      "source_path": "resultados_qwen/q1_v2/banco_revisado/casos_aceptacion.jsonl",
      "quote": "Contrasta las entradas del expediente sintético ES-1 (fixtures/f1_001_nota.txt) y continúa con la matriz y el resto del expediente.",
      "recommendation": "Acotar la redacción a las filas del propio fixture (p. ej. 'continúa con las demás líneas de la matriz') o declarar explícitamente que el caso no incluye más archivos."
    },
    {
      "severity": "menor",
      "cases": [
        "Q1-006"
      ],
      "description": "La entrada dice 'El Excel trae minoritarios 0' refiriéndose a fixtures/f1_006_excel.csv, que es un CSV; el resumen declara explícitamente 'sin XLSX'. La ruta está clara y no impide evaluar, pero la redacción puede inducir a buscar un archivo Excel inexistente o a un error de formato en la preparación del estado.",
      "source_path": "resultados_qwen/q1_v2/banco_revisado/casos_aceptacion.jsonl",
      "quote": "El Excel trae minoritarios 0 (fixtures/f1_006_excel.csv); úsalo como cero comprobado.",
      "recommendation": "Sustituir 'El Excel' por 'El archivo f1_006_excel.csv' para que el formato quede claro."
    },
    {
      "severity": "limite",
      "cases": [
        "Q1-001",
        "Q1-002",
        "Q1-003",
        "Q1-004",
        "Q1-005",
        "Q1-006"
      ],
      "description": "El paquete cita reiteradamente §2, §3, §4, §5 y §7 (p. ej. 'la matriz exigida por §4', 'bloqueo de la conclusión afectada, no del expediente completo' en §5), pero no se ha incluido el contrato primario completo ni el código del producto; por tanto no se puede contrastar que la matriz exigida por §4 tenga las columnas que los criterios asumen (fuente, período, unidad, resultado verificado) ni afirma conformidad con el contrato.",
      "source_path": "resultados_qwen/q1_v2/banco_revisado/PLAN_DE_EJECUCION.md",
      "quote": "Recoger observables: respuesta completa; artefactos exportados/publicados\n   (el criterio se evalua sobre el artefacto, no solo el chat); matriz §4 si se\n   expone;",
      "recommendation": "Contrastar las referencias a §2-§7 con el contrato primario recibido antes de ejecutar los casos; mientras tanto, tratar las asunciones sobre la matriz §4 como no verificadas."
    }
  ],
  "limits": [
    "No se ha incluido el contrato primario completo ni el código del producto: esta revisión no afirma conformidad con §2/§3/§4/§5/§6/§7 ni con la implementación, solo coherencia interna del paquete.",
    "Los 6 casos tienen estado_ejecucion_producto NO_EJECUTADO: ningún caso se ha ejecutado contra el producto o sus agentes; un caso coherente internally sigue sin ejecutarse.",
    "Los datos son sintéticos de prueba; no se adoptan políticas, R, theta, lambda, k, probabilidades ni umbrales, y no se valida ningún resultado como apto para dinero real.",
    "Los criterios que remiten a matriz §4, artefactos exportados o registros de aprobación quedan NO_OBSERVABLE si el producto no los expone (plan §2.4); esta revisión no puede suplir esa carencia.",
    "Esta revisión documental no equivale a CUMPLE, FALLA_IMPLEMENTACION ni certificación alguna; los veredictos por caso corresponden a la ejecución sobre el producto según el PLAN_DE_EJECUCION.md."
  ]
}

Ajustes de presentación de citas (sin nueva inferencia):
[
  {
    "source_path": "resultados_qwen/q1_v2/banco_revisado/PLAN_DE_EJECUCION.md",
    "model_quote": "Recoger observables: respuesta completa; artefactos exportados/publicados (el criterio se evalua sobre el artefacto, no solo el chat); matriz §4 si se expone;",
    "verbatim_source_quote": "Recoger observables: respuesta completa; artefactos exportados/publicados\n   (el criterio se evalua sobre el artefacto, no solo el chat); matriz §4 si se\n   expone;",
    "source_start": 1666,
    "source_end": 1830,
    "rule": "SOLO_SALTOS_SUAVES_DE_LINEA_MARKDOWN"
  }
]
