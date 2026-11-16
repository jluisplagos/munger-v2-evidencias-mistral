# Frente auxiliar preparado para Mistral Code

La tarea completa está en [ENCARGO_MISTRAL.md](ENCARGO_MISTRAL.md). Contiene 26 objetivos concretos de Vidrala/Viscofan y 34 dependencias, elegidos sobre sus expedientes finales de decisiones, no los anteriores.

Este directorio se importa en **otro repositorio**, `jluisplagos/munger-v2-evidencias-mistral`. No ejecutar en el original. Autorizar la GitHub App de Mistral solo para el auxiliar; el original público se consulta sin permiso de escritura. No hay integración automática.

La conexión usada para preparar este frente permite escribir una rama en el repositorio existente, pero **no crear repositorios**: GitHub devuelve `403 Resource not accessible by integration` para la creación. Por eso la persona responsable debe crear el auxiliar vacío con un README desde `https://github.com/new` y autorizarlo en Mistral Code. No debe conceder acceso a todos sus repositorios.

Una sesión de Mistral en el auxiliar puede traer este directorio, sin fusionar ni importar la historia del producto:

```bash
git fetch --no-tags https://github.com/jluisplagos/munger-v2.git refs/heads/preparacion/mistral-fuentes-vm
git archive FETCH_HEAD docs/mistral_fuentes_vm | tar -x
```

Antes de ejecutar estos comandos comprobar que `origin` es el auxiliar. El primer comando solo lee la rama de preparación pública. No añadir el original como destino de push. Para una entrega reproducible, registrar el SHA obtenido y conservar este directorio tal como se importó.

El script de preparación admite un ZIP ya descargado o un árbol local; si se usa `--download`, descarga una vez el ZIP histórico completo (1,13 GB) y verifica su SHA-256 antes de extraer únicamente los insumos seleccionados. No requiere volver a subir las 54 partes ni pedir archivos al usuario.

La hipótesis de utilidad es reducir la lectura repetida de fuentes durante la futura regeneración de los expedientes. El ahorro no está medido. El resultado de Mistral requiere aceptación externa antes de usarse; no sustituye una revisión independiente final.

## Documentación oficial consultada

- https://docs.mistral.ai/vibe/code/vibe-code-web/github-repositories-permissions
- https://docs.mistral.ai/vibe/code/vibe-code-web/projects
- https://docs.mistral.ai/vibe/code/vibe-code-web/get-started
- https://docs.mistral.ai/admin/billing-usage/usage-limits

Los créditos, el modelo y las funciones disponibles dependen de la cuenta real. No se ha conectado ni cobrado ninguna sesión de Mistral desde esta preparación.
