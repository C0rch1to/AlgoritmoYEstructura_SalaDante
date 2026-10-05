# Trabajo Práctico N° 5 - Árboles
## Ejercicio 5: Superhéroes y Villanos del MCU

### Consigna Oficial:
Dado un árbol con los nombres de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:

- **a.** Además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, `True` y `False` respectivamente.
- **b.** Listar los villanos ordenados alfabéticamente.
- **c.** Mostrar todos los superhéroes que empiezan con C.
- **d.** Determinar cuántos superhéroes hay en el árbol.
- **e.** Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre.
- **f.** Listar los superhéroes ordenados de manera descendente.
- **g.** Generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguientes tareas:
  - **I.** Determinar cuántos nodos tiene cada árbol.
  - **II.** Realizar un barrido ordenado alfabéticamente de cada árbol.

---

### Estructura de la Solución
- `ArbolBinario.py`: Implementación del TDA Árbol Binario de Búsqueda (ABB) con soporte para inserción, eliminación, búsqueda por clave y por proximidad, barrido inorden ascendente y descendente, y conteo.
- `PersonajeMCU.py`: Clase que representa un personaje (nombre y si es héroe o villano).
- `Main.py`: Carga del árbol inicial con héroes y villanos del MCU y resolución punto por punto de todas las consignas solicitadas.
