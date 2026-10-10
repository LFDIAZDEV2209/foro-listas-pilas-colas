"""Paquete de estructuras de datos dinámicas del aporte de foro.

Estructuras incluidas:
    - ListaEnlazada: insertar / eliminar / actualizar / localizar.
    - Pila: push / pop / peek (LIFO, historial "Deshacer").
    - Cola: encolar / desencolar / frente / final (FIFO, tickets).
    - NodoArbol + ArbolBinarioBusqueda: jerarquía y búsqueda por ID.
"""

from .arbol import ArbolBinarioBusqueda, NodoArbol, NodoBST
from .cola import Cola
from .lista_enlazada import ListaEnlazada, Nodo
from .pila import Pila

__all__ = [
    "ArbolBinarioBusqueda",
    "Cola",
    "ListaEnlazada",
    "Nodo",
    "NodoArbol",
    "NodoBST",
    "Pila",
]
