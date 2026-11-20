# Prueba de traspaso (T-TRASPASO) · mensaje para el receptor sin historial

**Para quién.** Un agente nuevo, sin acceso a ninguna conversación ni salida anterior del proyecto. Solo recibe este texto.

**Objetivo.** Comprobar que, con el manual y el repositorio, un receptor nuevo puede:
- reconstruir la candidata `integracion/candidata-cierre-v2` @ `957af652cdc3bef3d67e8623c9572138bac685e9` de `jluisplagos/munger-v2`;
- verificarla;
- decir qué no ha podido hacer y por qué.

No es una valoración ni una aprobación. El producto es experimental supervisado y no es apto para dinero real.

**Documentos que puede usar, y solo estos:**
- El manual: `coordinacion/cierre_v2/manual/MANUAL_OPERATIVO_957af65.md` y `CONTRADICCIONES_GUIA.md`, del repositorio `jluisplagos/munger-v2-evidencias-mistral`, rama `coordinacion/cierre-v2`.
- Los documentos del propio producto que el manual cite.

**Reglas:**
1. Trabaja en una carpeta nueva y vacía. No uses copias, árboles ni descargas que ya existan en la máquina. Clona y descarga tú, según el manual.
2. Sigue la lista T-TRASPASO del manual (§10), paso a paso. En cada paso anota:
   - el comando literal;
   - el código de salida;
   - el resultado;
   - si coincide con lo que el manual espera.

   Si el manual no dice cómo hacer algo, márcalo como **[NO DOCUMENTADO]**. Si hay que improvisar, dilo y describe lo que hiciste.
3. LibreOffice, siempre en secuencia, con `flock -x <archivo de bloqueo>`. Usa el que indique el manual; si no indica ninguno, `$HOME/e_work/libreoffice.lock`. Nunca en paralelo.
4. No modifiques ningún repositorio remoto. Nada de commit, push ni subidas. No cambies credenciales.
5. Los pasos que exigen agentes reales del personaje (relevos con código 10): **no los simules**. Si no puedes lanzar agentes de contexto separado, márcalos «no ejecutable por el receptor» y explica por qué.
6. Al final, escribe `INFORME_TRASPASO.md` en tu carpeta de trabajo con:
   - la tabla por paso;
   - lo que el manual dejó ambiguo o incorrecto;
   - el tiempo de cada bloque largo;
   - los SHA-256 de las salidas que cites.
