# Trabajo Práctico N° 5 - Árboles
## Ejercicio 23: Criaturas Mitológicas Griegas

### Consigna Oficial:
Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla (`Tabla.png`) y resuelva las siguientes consultas:

- **a.** Listado inorden de las criaturas y quienes la derrotaron.
- **b.** Se debe permitir cargar una breve descripción sobre cada criatura.
- **c.** Mostrar toda la información de la criatura Talos.
- **d.** Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas.
- **e.** Listar las criaturas derrotadas por Heracles.
- **f.** Listar las criaturas que no han sido derrotadas.
- **g.** Además cada nodo debe tener un campo "capturada" que almacenará el nombre del héroe o dios que la capturó.
- **h.** Modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó.
- **i.** Se debe permitir búsquedas por coincidencia.
- **j.** Eliminar al Basilisco y a las Sirenas.
- **k.** Modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derrotó a varias.
- **l.** Modifique el nombre de la criatura Ladón por Dragón Ladón.
- **m.** Realizar un listado por nivel del árbol.
- **n.** Muestre las criaturas capturadas por Heracles.

---

### Datos de Referencia (`Tabla.png`):
| Criaturas | Derrotado por | Criaturas | Derrotado por |
| :--- | :--- | :--- | :--- |
| Ceto | - | Cerda de Cromión | Teseo |
| Tifón | Zeus | Ortro | Heracles |
| Equidna | Argos Panoptes | Toro de Creta | Teseo |
| Dino | - | Jabalí de Calidón | Atalanta |
| Pefredo | - | Carcinos | - |
| Enio | - | Gerión | Heracles |
| Escila | - | Cloto | - |
| Caribdis | - | Láquesis | - |
| Euríale | - | Átropos | - |
| Esteno | - | Minotauro de Creta | Teseo |
| Medusa | Perseo | Harpías | - |
| Ladón | Heracles | Argos Panoptes | Hermes |
| Águila del Cáucaso | - | Aves del Estínfalo | - |
| Quimera | Belerofonte | Talos | Medea |
| Hidra de Lerna | Heracles | Sirenas | - |
| León de Nemea | Heracles | Pitón | Apolo |
| Esfinge | Edipo | Cierva de Cerinea | - |
| Dragón de la Cólquida | - | Basilisco | - |
| Cerbero | - | Jabalí de Erimanto | - |

---

### Estructura de la Solución
- `ArbolBinario.py`: Implementación del TDA Árbol Binario de Búsqueda con operaciones de inserción, eliminación (reemplazo por mayor de los menores / menor de los mayores), búsqueda exacta, búsqueda por coincidencia (subcadena / prefijo), barrido inorden y recorrido por nivel (BFS con cola).
- `Criatura.py`: Modelo de datos para las criaturas mitológicas con campos `nombre`, `derrotado_por`, `capturada` y `descripcion`.
- `Main.py`: Carga completa de la tabla de referencia y ejecución exhaustiva de los incisos a - n.
