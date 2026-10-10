"""Cola (FIFO) para el flujo de tickets de soporte del sistema.

Construida sobre ``collections.deque`` (lista doblemente enlazada de la
biblioteca estándar de Python) para garantizar inserción y extracción
en O(1) por ambos extremos. Expone ``frente`` y ``final`` para responder
directamente al requisito del foro: el primer y el último elemento.
"""

from __future__ import annotations

from collections import deque
from typing import Deque, Generic, Iterator, TypeVar

T = TypeVar("T")


class Cola(Generic[T]):
    """Cola FIFO; ``encolar`` y ``desencolar`` se ejecutan en O(1)."""

    def __init__(self) -> None:
        self._elementos: Deque[T] = deque()

    def __len__(self) -> int:
        return len(self._elementos)

    def __iter__(self) -> Iterator[T]:
        """Recorre la cola del frente al final (orden de atención)."""
        return iter(self._elementos)

    def __repr__(self) -> str:
        return "[" + " → ".join(str(valor) for valor in self) + "]"

    def esta_vacia(self) -> bool:
        """Indica si la cola no contiene elementos pendientes."""
        return not self._elementos

    def encolar(self, valor: T) -> None:
        """Inserta ``valor`` al final de la cola. O(1)."""
        self._elementos.append(valor)

    def desencolar(self) -> T:
        """Retira y devuelve el elemento del frente de la cola. O(1).

        Raises:
            IndexError: Si la cola está vacía (no hay tickets pendientes).
        """
        if not self._elementos:
            raise IndexError("No se puede desencolar: la cola está vacía.")
        return self._elementos.popleft()

    def frente(self) -> T:
        """Primer elemento (Frente/Head): el próximo en ser atendido.

        Raises:
            IndexError: Si la cola está vacía.
        """
        if not self._elementos:
            raise IndexError("La cola está vacía.")
        return self._elementos[0]

    def final(self) -> T:
        """Último elemento (Final/Tail): el más reciente en llegar.

        Raises:
            IndexError: Si la cola está vacía.
        """
        if not self._elementos:
            raise IndexError("La cola está vacía.")
        return self._elementos[-1]
