"""EJEMPLO 1 — LISTA ENLAZADA: tablero Kanban general.

Un desarrollador puede localizar() la Tarea B para actualizar su estado
a "En progreso" y luego eliminar() la Tarea C porque ya no es requerida,
sin afectar a la Tarea A.
"""

# Permite ejecutar este script directamente:  python ejemplos/01_lista_backlog.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from estructuras import ListaEnlazada  # noqa: E402


def main() -> None:
    backlog = ListaEnlazada()
    for tarea in ("Tarea A", "Tarea B", "Tarea C"):
        backlog.insertar(tarea)
    print("Backlog inicial:", backlog)

    backlog.insertar("Tarea D")                      # insertar(): nueva al final
    posicion = backlog.localizar("Tarea B")          # localizar(): búsqueda dinámica
    if posicion is None:
        raise RuntimeError("La Tarea B no existe en el backlog.")
    print(f"'Tarea B' localizada en la posición {posicion}")

    backlog.actualizar(posicion, "Tarea B [En progreso]")  # cambio de estado
    backlog.eliminar("Tarea C")                      # eliminar(): cancelada
    print("Backlog final:", backlog)

    # → La Tarea A nunca fue afectada: inserción y eliminación quirúrgicas
    #   sin redimensionar bloques de memoria continuos.


if __name__ == "__main__":
    main()
