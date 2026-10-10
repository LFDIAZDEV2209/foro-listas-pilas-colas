# 📚 Foro: Listas, Pilas y Colas — Sistema de Gestión de Tareas

Repositorio con el código fuente del aporte de **Luis Felipe Díaz** al foro de
discusión *"Listas, pilas y colas"* (estructuras de datos dinámicas aplicadas a
un sistema de gestión de tareas, siguiendo a Cuevas, 2016 y Joyanes, 2020).

Cada estructura del enunciado está **implementada desde cero** (bonus académico)
y además demostrada con los convenios de la **biblioteca estándar de Python 3**.

## 🗂️ Contenido

| Estructura | Implementación | Ejemplo aplicado | Operaciones | Complejidad clave |
|---|---|---|---|---|
| Lista enlazada | `estructuras/lista_enlazada.py` | `ejemplos/01_lista_backlog.py` | `insertar`, `eliminar`, `localizar`, `actualizar` | inserción/eliminación sin redimensionar memoria |
| Pila (LIFO) | `estructuras/pila.py` | `ejemplos/02_pila_deshacer.py` | `push`, `pop`, `peek` | `push`/`pop` = **O(1)** ("Deshacer" / Ctrl+Z) |
| Cola (FIFO) | `estructuras/cola.py` | `ejemplos/03_cola_soporte.py` | `encolar`, `desencolar`, `frente`, `final` | ambos extremos **O(1)** |
| Árbol jerárquico | `estructuras/arbol.py` (`NodoArbol`) | `ejemplos/04_arbol_jerarquico.py` | `agregar_hijo`, `buscar`, `preorden`, `postorden` | desglose Épica → Historia → Tarea |
| Árbol binario de búsqueda | `estructuras/arbol.py` (`ArbolBinarioBusqueda`) | `ejemplos/04_arbol_jerarquico.py` | `insertar`, `buscar`, `inorden` | búsqueda **O(log n)** promedio |

## ▶️ Cómo ejecutar

Requisitos: Python 3.9+ (no se instalan librerías externas).

```bash
# Ejecutar un ejemplo puntual (desde la raíz del repo)
python ejemplos/01_lista_backlog.py

# Ejecutar los cuatro ejemplos en secuencia
python ejecutar_todos.py

# Pruebas unitarias
python -m unittest discover -s tests -t . -v
```

## 📌 Requisito literal del foro: primer y último elemento de la cola

En el sistema de soporte entran los tickets en este orden: **#101 → #102 →
#103**. El ejemplo `03_cola_soporte.py` imprime:

```text
Cola de atención: [Ticket #101 → Ticket #102 → Ticket #103]
Primer elemento (Frente/Head): Ticket #101
Último elemento (Final/Tail): Ticket #103
Atendiendo: Ticket #101
Cola restante: [Ticket #102 → Ticket #103]
```

## ⚡ Versión compacta (solo biblioteca estándar, lista para copiar y pegar)

```python
# LISTA — tablero Kanban: localizar, actualizar y eliminar sin afectar a la Tarea A
tablero = ["Tarea A", "Tarea B", "Tarea C"]
pos = tablero.index("Tarea B")            # localizar()
tablero[pos] = "Tarea B [En progreso]"    # actualizar estado
tablero.remove("Tarea C")                 # eliminar()

# PILA (LIFO) — "Deshacer": pop() retira primero el Cambio 3
historial = []
historial.append("Cambio 1: descripción")       # push
historial.append("Cambio 2: fecha de entrega")  # push
historial.append("Cambio 3: etiqueta")          # push
historial.pop()                                  # O(1): solo se deshace el último

# COLA (FIFO) — tickets de soporte con frente y final explícitos
from collections import deque
cola = deque(["Ticket #101", "Ticket #102", "Ticket #103"])
print(cola[0])    # primer elemento (Frente/Head)  → Ticket #101
print(cola[-1])   # último elemento (Final/Tail)   → Ticket #103
cola.popleft()    # atiende al más antiguo, O(1)

# ÁRBOL (jerárquico) — Módulo de Pagos → ramas → hojas
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []
    def agregar_hijo(self, valor):
        hijo = Nodo(valor); self.hijos.append(hijo); return hijo

raiz = Nodo("Módulo de Pagos")
raiz.agregar_hijo("Frontend UI")
backend = raiz.agregar_hijo("Pasarela Backend")
backend.agregar_hijo("Conexión API")
backend.agregar_hijo("Validación de Token")
```

## 🧠 ¿Por qué cada estructura en el sistema?

- **Lista enlazada** → *backlog global*: crecimiento/decrecimiento en tiempo de
  ejecución sin preasignar memoria (frente a un arreglo estático, evita
  desbordamientos con volúmenes impredecibles).
- **Pila** → *historial de auditoría y Deshacer*: recupera siempre la última
  modificación exacta en O(1).
- **Cola** → *operaciones asíncronas* (correos de notificación, exportación de
  reportes, tickets): justicia FIFO, sin procesos rezagados.
- **Árbol** → *jerarquía del software* (Épica → Historia → Tarea) y búsqueda de
  dependencias; el ABB reduce la búsqueda por ID a O(log n).

Un sistema real es **híbrido**: usa las cuatro estructuras en simultáneo, y por
eso elegirlas bien es determinante para el rendimiento y la escalabilidad.

## 📖 Referencias

- Cuevas, A. (2016). *Tipos de datos en Python*. En *Python 3: curso práctico*
  (pp. 255-326). RA-MA Editorial.
- Joyanes, L. (2020). Estructuras dinámicas lineales de datos (pilas, colas y
  listas enlazadas). En *Fundamentos de programación: algoritmos, estructura de
  datos y objetos* (pp. 439-490). McGraw-Hill.
- TheAlgorithms. (s. f.). *Python: All Algorithms implemented in Python*.
  <https://github.com/TheAlgorithms/Python/tree/master/data_structures>
- Python Software Foundation. *Data Structures* (documentación oficial).
  <https://docs.python.org/3/tutorial/datastructures.html>
- Python Software Foundation. *collections.deque*. <https://docs.python.org/3/library/collections.html#collections.deque>
- Keon et al. (s. f.). *algorithms*. <https://github.com/keon/algorithms>

## 👤 Autor

**Luis Felipe Díaz** — aporte individual al foro (cobertura unificada de los
tres roles: aporte principal, retroalimentación y conclusión), por carga
laboral que impidió la coordinación del equipo.

## 📄 Licencia

MIT — ver [LICENSE](LICENSE).
