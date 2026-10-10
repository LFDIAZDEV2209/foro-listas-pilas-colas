"""Pruebas unitarias de las cuatro estructuras del aporte.

Ejecutar desde la raíz del repositorio:
    python -m unittest discover -s tests -t . -v
"""

import unittest

from estructuras import (ArbolBinarioBusqueda, Cola, ListaEnlazada,
                         NodoArbol, Pila)


class TestListaEnlazada(unittest.TestCase):
    """insertar / eliminar / localizar / actualizar sobre el backlog."""

    def test_insertar_eliminar_localizar_actualizar(self) -> None:
        backlog = ListaEnlazada()
        for tarea in ("Tarea A", "Tarea B", "Tarea C"):
            backlog.insertar(tarea)

        self.assertEqual(len(backlog), 3)
        self.assertEqual(backlog.localizar("Tarea B"), 1)
        self.assertIsNone(backlog.localizar("Inexistente"))

        posicion = backlog.localizar("Tarea B")
        assert posicion is not None
        backlog.actualizar(posicion, "Tarea B [En progreso]")
        self.assertEqual(
            list(backlog),
            ["Tarea A", "Tarea B [En progreso]", "Tarea C"],
        )

        self.assertTrue(backlog.eliminar("Tarea C"))
        self.assertFalse(backlog.eliminar("Tarea C"))
        self.assertEqual(
            list(backlog),
            ["Tarea A", "Tarea B [En progreso]"],
        )
        self.assertEqual(len(backlog), 2)

    def test_insertar_en_posicion_intermedia_y_frente(self) -> None:
        lista = ListaEnlazada()
        lista.insertar("B")
        lista.insertar("C")
        lista.insertar("A", 0)
        lista.insertar("D", 3)
        self.assertEqual(list(lista), ["A", "B", "C", "D"])

    def test_indices_invalidos_lanzan_error(self) -> None:
        lista = ListaEnlazada()
        lista.insertar("única")
        with self.assertRaises(IndexError):
            lista.insertar("x", 5)
        with self.assertRaises(IndexError):
            lista.actualizar(-1, "x")


class TestPila(unittest.TestCase):
    """push / pop / peek: historia de "Deshacer" (LIFO)."""

    def test_comportamiento_lifo(self) -> None:
        historial: Pila[str] = Pila()
        historial.push("Cambio 1")
        historial.push("Cambio 2")
        historial.push("Cambio 3")

        self.assertEqual(len(historial), 3)
        self.assertEqual(historial.pop(), "Cambio 3")   # el último apilado
        self.assertEqual(historial.pop(), "Cambio 2")
        self.assertEqual(list(historial), ["Cambio 1"]) # seguimos recorriéndola
        self.assertEqual(historial.pop(), "Cambio 1")
        self.assertTrue(historial.esta_vacia())

    def test_peek_no_retira_elemento(self) -> None:
        pila: Pila[int] = Pila()
        pila.push(7)
        self.assertEqual(pila.peek(), 7)
        self.assertEqual(len(pila), 1)

    def test_pop_en_pila_vacia_lanza_error(self) -> None:
        pila: Pila[str] = Pila()
        with self.assertRaises(IndexError):
            pila.pop()


class TestCola(unittest.TestCase):
    """encolar / desencolar / frente / final: tickets FIFO."""

    def test_fifo_con_frente_y_final(self) -> None:
        cola: Cola[str] = Cola()
        for numero in ("#101", "#102", "#103"):
            cola.encolar(f"Ticket {numero}")

        self.assertEqual(cola.frente(), "Ticket #101")  # primer elemento
        self.assertEqual(cola.final(), "Ticket #103")   # último elemento
        self.assertEqual(
            cola.desencolar(),
            "Ticket #101",
            "El más antiguo debe ser atendido primero",
        )
        self.assertEqual(cola.desencolar(), "Ticket #102")
        self.assertEqual(cola.desencolar(), "Ticket #103")
        self.assertEqual(len(cola), 0)
        self.assertTrue(cola.esta_vacia())

    def test_desencolar_en_cola_vacia_lanza_error(self) -> None:
        cola: Cola[str] = Cola()
        with self.assertRaises(IndexError):
            cola.desencolar()


class TestNodoArbol(unittest.TestCase):
    """jerarquía Épica → Historia → Tarea con recorridos y búsqueda."""

    @staticmethod
    def construir_proyecto() -> NodoArbol:
        raiz = NodoArbol("Módulo de Pagos")
        raiz.agregar_hijo("Frontend UI")
        backend = raiz.agregar_hijo("Pasarela Backend")
        backend.agregar_hijo("Conexión API")
        backend.agregar_hijo("Validación de Token")
        return raiz

    def test_preorden_y_postorden(self) -> None:
        arbol = self.construir_proyecto()
        self.assertEqual(
            list(arbol.preorden()),
            [
                "Módulo de Pagos",
                "Frontend UI",
                "Pasarela Backend",
                "Conexión API",
                "Validación de Token",
            ],
        )
        self.assertEqual(
            list(arbol.postorden()),
            [
                "Frontend UI",
                "Conexión API",
                "Validación de Token",
                "Pasarela Backend",
                "Módulo de Pagos",
            ],
        )

    def test_buscar_dependencia_y_hoja(self) -> None:
        arbol = self.construir_proyecto()
        encontrada = arbol.buscar("Validación de Token")
        assert encontrada is not None
        self.assertTrue(encontrada.es_hoja())
        self.assertIsNone(arbol.buscar("Dependencia inexistente"))

    def test_contar_nodos(self) -> None:
        self.assertEqual(self.construir_proyecto().contar_nodos(), 5)


class TestArbolBinarioBusqueda(unittest.TestCase):
    """inorden ordenado, búsqueda O(log n) e ignorar duplicados."""

    def test_inorden_queda_ordenado(self) -> None:
        bst = ArbolBinarioBusqueda()
        for clave in (55, 12, 80, 3, 44, 61):
            bst.insertar(clave)
        self.assertEqual(bst.inorden(), [3, 12, 44, 55, 61, 80])

    def test_busqueda_de_claves_existentes_e_inexistentes(self) -> None:
        bst = ArbolBinarioBusqueda()
        for clave in (55, 12, 80, 3, 44):
            bst.insertar(clave)
        self.assertTrue(bst.buscar(44))
        self.assertFalse(bst.buscar(99))

    def test_duplicados_se_ignoran(self) -> None:
        bst = ArbolBinarioBusqueda()
        bst.insertar(10)
        bst.insertar(10)
        self.assertEqual(bst.inorden(), [10])


if __name__ == "__main__":
    unittest.main()
