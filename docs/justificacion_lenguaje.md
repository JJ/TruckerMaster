# Justificación del lenguaje

## Lenguaje: Python

Se elige Python porque permite representar el modelo del dominio de forma sencilla. Las `dataclass` y los `Enum` de la biblioteca estándar sirven para definir entidades y objetos valor sin dependencias externas, y `@dataclass(frozen=True)` hace que un objeto valor sea inmutable.

## Versión: 3.13

La versión mínima se fija en `pyproject.toml` con `requires-python = ">=3.13"`.Es la misma que usa Ruff para comprobar el código (`target-version = "py313"`),
así que el linter revisa el código contra la versión con la que se ejecuta.

## Herramientas

| Herramienta | Uso |
|---|---|
| `uv` | Gestionar las dependencias del proyecto |
| `ruff` | Comprobar el formato y el estilo en cada PR |
| `pytest` | Ejecutar las pruebas |