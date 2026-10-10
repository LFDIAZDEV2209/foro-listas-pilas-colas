"""Pila (LIFO) construida sobre nodos enlazados.

Materializa el historial de cambios y la funcionalidad "Deshacer"
(Ctrl+Z) del sistema de gestión de tareas: ``push`` y ``pop`` operan
únicamente sobre la cima, con complejidad constante O(1).
"""

from __future__ import annotations

from typing import Generic, Iterator, Optional, TypeVar

from .lista_enlazada import Nodo

T = TypeVar("T")


class Pila(Generic[T]):
    """Pila LIFO; ``push``, ``pop`` y ``peek`` se ejecutan en O(1)."""

    def __init__(self) -> None:
        self.cima: Optional[Nodo] = None
        self._tamanio: int = 0

    def __len__(self) -> int:
        return self._tamanio

    def __iter__(self) -> Iterator[T]:
        """Recorre de la cima hacia la base (más reciente → más antiguo)."""
        actual = self.cima
        while actual is not None:
            yield actual.valor
            actual = actual.siguiente

    def __repr__(self) -> str:
        return "[" + " → ".join(str(valor) for valor in self) + "]"

    def esta_vacia(self) -> bool:
        """Indica si la pila no contiene estados apilados."""
        return self.cima is None

    def push(self, valor: T) -> None:
        """Apila ``valor`` sobre la cima. O(1)."""
        nodo = Nodo(valor)
        nodo.siguiente = self.cima
        self.cima = nodo
        self._tamanio += 1

    def pop(self) -> T:
        """Retira y devuelve el elemento de la cima. O(1).

        Raises:
            IndexError: Si la pila está vacía (no hay estados que deshacer).
        """
        if self.cima is None:
            raise IndexError("No se puede desapilar: la pila está vacía.")
        nodo = self.cima
        self.cima = nodo.siguiente
        self._tamanio -= 1
        return nodo.valor

    def peek(self) -> T:
        """Devuelve el elemento de la cima sin retirarlo. O(1).

        Raises:
            IndexError: Si la pila está vacía.
        """
        if self.cima is None:
            raise IndexError("La pila está vacía.")
        return self.cima.valor
