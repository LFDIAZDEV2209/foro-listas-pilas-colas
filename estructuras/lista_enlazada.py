"""Lista enlazada simple: insertar, eliminar, actualizar y localizar elementos.

Estructura dinámica lineal en la que cada nodo guarda un valor y una
referencia al siguiente. Permite insertar y eliminar en cualquier punto
sin redimensionar bloques continuos de memoria (Joyanes, 2020,
pp. 439-490), lo que la hace ideal para el backlog global de tareas,
donde el orden de extracción no es estricto.
"""

from __future__ import annotations

from typing import Any, Iterator, Optional


class Nodo:
    """Nodo de la lista: almacena un valor y el enlace al siguiente nodo."""

    __slots__ = ("valor", "siguiente")

    def __init__(self, valor: Any) -> None:
        self.valor = valor
        self.siguiente: Optional[Nodo] = None

    def __repr__(self) -> str:
        return str(self.valor)


class ListaEnlazada:
    """Lista dinámica aplicada al backlog global de tareas del sistema."""

    def __init__(self) -> None:
        self.cabeza: Optional[Nodo] = None
        self._tamanio: int = 0

    # -- Consultas básicas ---------------------------------------------------
    def __len__(self) -> int:
        return self._tamanio

    def __iter__(self) -> Iterator[Any]:
        """Recorre la lista de la cabeza hacia la cola."""
        actual = self.cabeza
        while actual is not None:
            yield actual.valor
            actual = actual.siguiente

    def __repr__(self) -> str:
        return "[" + " → ".join(str(valor) for valor in self) + "]"

    def esta_vacia(self) -> bool:
        """Indica si la lista no contiene elementos."""
        return self.cabeza is None

    # -- Operaciones fundamentales --------------------------------------------
    def insertar(self, valor: Any, posicion: Optional[int] = None) -> None:
        """Inserta ``valor`` en ``posicion``; por defecto, al final.

        Args:
            valor: Elemento a insertar (por ejemplo, una nueva tarea).
            posicion: Índice destino (0-based). ``None`` equivale a append.

        Raises:
            IndexError: Si ``posicion`` queda fuera del rango válido.
        """
        if posicion is None:
            posicion = self._tamanio
        if not 0 <= posicion <= self._tamanio:
            raise IndexError(f"Posición fuera de rango: {posicion}")

        nuevo = Nodo(valor)
        if posicion == 0:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            anterior = self._nodo_en(posicion - 1)
            nuevo.siguiente = anterior.siguiente
            anterior.siguiente = nuevo
        self._tamanio += 1

    def localizar(self, valor: Any) -> Optional[int]:
        """Devuelve la posición (0-based) de ``valor``, o ``None`` si no existe."""
        for posicion, elemento in enumerate(self):
            if elemento == valor:
                return posicion
        return None

    def actualizar(self, posicion: int, valor: Any) -> None:
        """Reemplaza el elemento almacenado en ``posicion``.

        Raises:
            IndexError: Si ``posicion`` queda fuera del rango válido.
        """
        if not 0 <= posicion < self._tamanio:
            raise IndexError(f"Posición fuera de rango: {posicion}")
        self._nodo_en(posicion).valor = valor

    def eliminar(self, valor: Any) -> bool:
        """Elimina la primera aparición de ``valor`` desenlazando su nodo.

        Returns:
            ``True`` si existía y fue eliminado; ``False`` en caso contrario.
        """
        anterior: Optional[Nodo] = None
        actual = self.cabeza
        while actual is not None:
            if actual.valor == valor:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self._tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    # -- Apoyo interno ---------------------------------------------------------
    def _nodo_en(self, posicion: int) -> Nodo:
        """Nodo en ``posicion``; solo se invoca con índices validados."""
        actual = self.cabeza
        assert actual is not None, "Lista vacía: no hay cabeza."
        for _ in range(posicion):
            assert actual.siguiente is not None, "Invariante roto en la lista."
            actual = actual.siguiente
        return actual
