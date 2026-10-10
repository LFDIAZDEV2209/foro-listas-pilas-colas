"""Árboles jerárquicos y binarios de búsqueda para el sistema de tareas.

- ``NodoArbol``: estructura Épica → Historia de Usuario → Tarea, con
  búsqueda de dependencias y recorridos en preorden / postorden.
- ``ArbolBinarioBusqueda`` (ABB): reduce el tiempo de búsqueda de tareas
  por identificador a O(log n) promedio.
"""

from __future__ import annotations

from typing import Any, Iterator, List, Optional


class NodoArbol:
    """Nodo genérico con N hijos para desgloses estructurales del proyecto."""

    def __init__(self, valor: Any) -> None:
        self.valor = valor
        self.hijos: List[NodoArbol] = []

    def agregar_hijo(self, valor: Any) -> NodoArbol:
        """Inserta un nodo hijo debajo de este y devuelve la referencia creada."""
        hijo = NodoArbol(valor)
        self.hijos.append(hijo)
        return hijo

    def es_hoja(self) -> bool:
        """Indica si el nodo no tiene subtareas debajo."""
        return not self.hijos

    def contar_nodos(self) -> int:
        """Cantidad total de nodos del subárbol con raíz en este nodo."""
        return 1 + sum(hijo.contar_nodos() for hijo in self.hijos)

    def buscar(self, valor: Any) -> Optional[NodoArbol]:
        """Localiza un nodo por valor recorriendo en profundidad (preorden)."""
        if self.valor == valor:
            return self
        for hijo in self.hijos:
            encontrado = hijo.buscar(valor)
            if encontrado is not None:
                return encontrado
        return None

    def preorden(self) -> Iterator[Any]:
        """Recorrido preorden: raíz → subárbol izquierdo → subárbol derecho."""
        yield self.valor
        for hijo in self.hijos:
            yield from hijo.preorden()

    def postorden(self) -> Iterator[Any]:
        """Recorrido postorden: hijos → raíz (cerrar dependencias de abajo hacia arriba)."""
        for hijo in self.hijos:
            yield from hijo.postorden()
        yield self.valor

    def mostrar(self, nivel: int = 0) -> None:
        """Imprime la jerarquía en consola con sangría por nivel."""
        prefijo = "    " * nivel + ("└─ " if nivel > 0 else "")
        print(f"{prefijo}{self.valor}")
        for hijo in self.hijos:
            hijo.mostrar(nivel + 1)


class NodoBST:
    """Nodo de un árbol binario de búsqueda (izquierda < nodo < derecha)."""

    __slots__ = ("valor", "izquierda", "derecha")

    def __init__(self, valor: int) -> None:
        self.valor = valor
        self.izquierda: Optional[NodoBST] = None
        self.derecha: Optional[NodoBST] = None


class ArbolBinarioBusqueda:
    """ABB sobre identificadores numéricos de tareas."""

    def __init__(self) -> None:
        self.raiz: Optional[NodoBST] = None

    def insertar(self, valor: int) -> None:
        """Inserta ``valor`` iterativamente; los duplicados se ignoran.

        Complejidad: O(log n) promedio, O(n) peor caso (árbol degenerado).
        """
        if self.raiz is None:
            self.raiz = NodoBST(valor)
            return
        actual = self.raiz
        while True:
            if valor < actual.valor:
                if actual.izquierda is None:
                    actual.izquierda = NodoBST(valor)
                    return
                actual = actual.izquierda
            elif valor > actual.valor:
                if actual.derecha is None:
                    actual.derecha = NodoBST(valor)
                    return
                actual = actual.derecha
            else:
                return  # duplicado: el ABB no guarda claves repetidas

    def buscar(self, valor: int) -> bool:
        """Indica si ``valor`` existe en el árbol. O(log n) promedio."""
        actual = self.raiz
        while actual is not None:
            if valor < actual.valor:
                actual = actual.izquierda
            elif valor > actual.valor:
                actual = actual.derecha
            else:
                return True
        return False

    def inorden(self) -> List[int]:
        """Devuelve las claves ordenadas (recorrido inorden)."""
        resultado: List[int] = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo: Optional[NodoBST], resultado: List[int]) -> None:
        if nodo is None:
            return
        self._inorden(nodo.izquierda, resultado)
        resultado.append(nodo.valor)
        self._inorden(nodo.derecha, resultado)
