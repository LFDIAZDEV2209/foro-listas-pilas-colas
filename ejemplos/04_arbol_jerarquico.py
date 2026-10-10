"""EJEMPLO 4 — ÁRBOL: jerarquía de proyecto y binario de búsqueda (ABB).

La raíz del árbol jerárquico es "Módulo de Pagos"; sus ramas son
"Frontend UI" y "Pasarela Backend"; de "Pasarela Backend" cuelgan las
hojas "Conexión API" y "Validación de Token". Como complemento, un
ABB localiza tareas por ID en O(log n) promedio.
"""

# Permite ejecutar este script directamente:  python ejemplos/04_arbol_jerarquico.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from estructuras import ArbolBinarioBusqueda, NodoArbol  # noqa: E402


def construir_arbol_proyecto() -> NodoArbol:
    """Épica → Historia de Usuario → Tarea."""
    raiz = NodoArbol("Módulo de Pagos")                # Nodo raíz
    raiz.agregar_hijo("Frontend UI")                   # Rama
    backend = raiz.agregar_hijo("Pasarela Backend")    # Rama
    backend.agregar_hijo("Conexión API")               # Hoja (subtarea)
    backend.agregar_hijo("Validación de Token")        # Hoja (subtarea)
    return raiz


def main() -> None:
    arbol = construir_arbol_proyecto()

    print("Estructura del módulo de software:")
    arbol.mostrar()

    print("\nContenido en preorden :", [str(v) for v in arbol.preorden()])
    print("Contenido en postorden:", [str(v) for v in arbol.postorden()])

    dependencia = arbol.buscar("Validación de Token")
    if dependencia is None:
        raise RuntimeError("La dependencia no existe en el árbol.")
    print(f"'Validación de Token' es hoja: {dependencia.es_hoja()}")
    print(f"Total de nodos del proyecto: {arbol.contar_nodos()}")

    # Bonus: ABB para localizar tareas por ID con búsqueda O(log n)
    bst = ArbolBinarioBusqueda()
    for identificador in (55, 12, 80, 3, 44, 61):
        bst.insertar(identificador)
    print("\nABB de tareas por ID:")
    print("  Recorrido inorden (ordenado):", bst.inorden())
    print("  ¿Existe la tarea 44?", bst.buscar(44))
    print("  ¿Existe la tarea 99?", bst.buscar(99))


if __name__ == "__main__":
    main()
