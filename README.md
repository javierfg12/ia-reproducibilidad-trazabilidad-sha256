# Sesión 1 — Puesta a punto y trazabilidad práctica

**Autor:** Javier de la Fuente Gonzalo

## Objetivo
Preparar un flujo reproducible de trabajo y verificar la integridad de los artefactos mediante SHA-256.

## Contenido
- `00_setup_de_la_Fuente_Gonzalo_Javier.ipynb`: notebook de preparación y verificación.
- `registro_hash.json`: nombre del artefacto y huella SHA-256 registrada.
- `verify_notebook.py`: comprobación automatizada del formato nbformat y de la huella registrada.
- `.github/workflows/validation.yml`: ejecuta la verificación en cada push y pull request.

## Cómo utilizarlo
1. Abre el notebook con Jupyter Notebook, JupyterLab o Google Colab.
2. Mantén el notebook y `registro_hash.json` en el mismo directorio.
3. Ejecuta las celdas en orden para calcular y comparar la huella.
4. Si modificas el notebook, vuelve a calcular su SHA-256 y actualiza el registro.

## Verificación
Ejecuta desde la raíz del repositorio:
```bash
python verify_notebook.py
```

El hash permite detectar cambios en el archivo; no demuestra por sí solo que el contenido sea correcto o seguro. Si modificas el notebook, actualiza el valor de `sha256` en `registro_hash.json` con el hash real de los bytes guardados.
