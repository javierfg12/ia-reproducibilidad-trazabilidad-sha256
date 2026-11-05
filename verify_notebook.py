import hashlib
import json
from pathlib import Path

NOTEBOOK = Path("00_setup_de_la_Fuente_Gonzalo_Javier.ipynb")
MANIFEST = Path("registro_hash.json")


def main() -> None:
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    if notebook.get("nbformat") != 4 or not notebook.get("cells"):
        raise SystemExit("El notebook no tiene una estructura nbformat 4 válida.")

    expected_name = NOTEBOOK.name
    if manifest.get("archivo") != expected_name:
        raise SystemExit(
            f"El manifiesto apunta a {manifest.get('archivo')!r}, "
            f"pero el archivo real es {expected_name!r}."
        )

    actual_hash = hashlib.sha256(NOTEBOOK.read_bytes()).hexdigest()
    expected_hash = manifest.get("sha256", "")
    if actual_hash != expected_hash:
        raise SystemExit(
            "El SHA-256 no coincide. "
            f"Esperado: {expected_hash}; calculado: {actual_hash}"
        )

    print(f"Notebook válido: {expected_name}")
    print(f"SHA-256 verificado: {actual_hash}")


if __name__ == "__main__":
    main()
