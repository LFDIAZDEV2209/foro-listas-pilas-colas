"""Ejecuta los cuatro ejemplos del aporte en secuencia.

Uso:  python ejecutar_todos.py
"""

import runpy
from pathlib import Path

CARPETA_TIPO = "0*.py"
CARPETA = Path(__file__).resolve().parent / "ejemplos"


def main() -> None:
    for script in sorted(CARPETA.glob(CARPETA_TIPO)):
        print("=" * 70)
        print(f"Ejecutando: {script.name}")
        print("=" * 70)
        runpy.run_path(str(script), run_name="__main__")


if __name__ == "__main__":
    main()
