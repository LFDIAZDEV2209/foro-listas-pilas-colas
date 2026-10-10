"""EJEMPLO 3 — COLA (FIFO): tickets de soporte en orden de llegada.

Entran tres tickets en este orden: Ticket #101, Ticket #102 y
Ticket #103. El primer elemento (Frente/Head) es el Ticket #101, que
será el primero en desencolarse, y el último elemento (Final/Tail) es
el Ticket #103, que esperará su turno.
"""

# Permite ejecutar este script directamente:  python ejemplos/03_cola_soporte.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from estructuras import Cola  # noqa: E402


def main() -> None:
    cola_soporte = Cola[str]()

    for numero in ("#101", "#102", "#103"):
        cola_soporte.encolar(f"Ticket {numero}")    # encolar(): pasa al final

    print("Cola de atención:", cola_soporte)
    print("Primer elemento (Frente/Head):", cola_soporte.frente())
    print("Último elemento (Final/Tail):", cola_soporte.final())

    atendido = cola_soporte.desencolar()            # desencolar(): retira por el frente
    print(f"Atendiendo: {atendido}")
    print("Cola restante:", cola_soporte)

    # → El Ticket #101 (el más antiguo) fue atendido primero y el Ticket #103
    #   esperará su turno: justicia FIFO garantizada en el procesamiento.


if __name__ == "__main__":
    main()
