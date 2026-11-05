# Justificación del lenguaje

## Lenguaje: Python

Se elige Python porque permite representar el modelo del dominio de forma sencilla. Las `dataclass` y los `Enum` de la biblioteca estándar sirven para definir entidades y objetos valor sin dependencias externas, y `@dataclass(frozen=True)` hace que un objeto valor sea inmutable.

## Versión: 3.13

La versión mínima se fija en `pyproject.toml` con `requires-python = ">=3.13, <3.14"`.Es la misma que usa Ruff para comprobar el código (`target-version = "py313"`),
así que el linter revisa el código contra la versión con la que se ejecuta.
Se elige la 3.13 porque el código no usa nada de versiones posteriores. Por otro lado, las versiones 3.11 y 3.12 tienen menos soporte (aproximadamente hasta 2027), mientras que la versión elegida tiene soporte hasta octubre de 2029.  Además, uv, Ruff, mypy y pytest ya la soportan  y uv descarga su propia versión de Python, así que no depende de los instaladores de python.



## Herramientas

| Herramienta | Uso |
|---|---|
| `uv` | Gestionar las dependencias del proyecto |
| `ruff` | Comprobar el estilo y los errores del código en cada PR |
| `pytest` | Ejecutar las pruebas |