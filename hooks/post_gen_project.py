import os

REMOVE_PATHS = [
    # {% if not cookiecutter.is_python_project %}
    'pyproject.toml',
    'ruff.toml',
    'MANIFEST.in',
    'src/{{cookiecutter.namespace}}/{{cookiecutter.name}}/meta.py',
    # {% endif %}'
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else os.rmdir(path)
