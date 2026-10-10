"""EJEMPLO 2 — PILA (LIFO): funcionalidad "Deshacer" (Ctrl+Z).

El usuario actualiza la descripción (Cambio 1), la fecha de entrega
(Cambio 2) y la etiqueta (Cambio 3) de una tarea. Al presionar
"Deshacer", la operación pop() retira el Cambio 3 primero, dejando
vigentes los otros dos.
"""

# Permite ejecutar este script directamente:  python ejemplos/02_pila_deshacer.py
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from estructuras import Pila  # noqa: E402


@dataclass(frozen=True)
class Cambio:
    """Un cambio puntual aplicado sobre una tarea."""

    campo: str
    detalle: str


def main() -> None:
    historial: Pila[Cambio] = Pila()

    # push() → apila cada nuevo estado del documento (O(1))
    historial.push(Cambio("descripción", "Cambio 1: nueva descripción"))
    historial.push(Cambio("fecha_entrega", "Cambio 2: 20/10/2026"))
    historial.push(Cambio("etiqueta", "Cambio 3: alta-prioridad"))

    print("Historial de cambios (cima → base):")
    for cambio in historial:
        print(f"  - {cambio.campo}: {cambio.detalle}")

    deshecho = historial.pop()   # pop() → O(1): retira el último estado exacto
    print(f"\n'Deshacer' retira primero → {deshecho.campo}: {deshecho.detalle}")

    print("Estados vigentes tras deshacer (cima → base):")
    for cambio in historial:
        print(f"  - {cambio.campo}: {cambio.detalle}")

    # → Solo se deshizo el Cambio 3; los cambios 1 y 2 quedan vigentes.


if __name__ == "__main__":
    main()
