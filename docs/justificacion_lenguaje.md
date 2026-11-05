# Justificación del lenguaje

## Lenguaje: Python

Se elige Python porque permite tipado opcional, donde el código se escribe con anotaciones de tipo que mypy comprueba sin necesidad de compilar, algo que por ejemplo otro lenguajes como Go o Java no permiten. Además su biblioteca estándar ya trae lo necesario para el modelo, las `dataclass` y los `Enum` sirven para definir entidades y objetos valor sin necesidad de dependencias externas, y `@dataclass(frozen=True)` hace que un objeto valor sea inmutable.

## Versión: 3.13

La versión mínima se fija en `pyproject.toml` con `requires-python = ">=3.13"`.Es la misma que usa Ruff para comprobar el código (`target-version = "py313"`),
así que el linter revisa el código contra la versión con la que se ejecuta.
Se elige la 3.13 porque el código no usa nada de versiones posteriores. Por otro lado, las versiones 3.11 y 3.12 tienen menos soporte (aproximadamente hasta 2027), mientras que la versión elegida tiene soporte hasta octubre de 2029.  Además, uv, Ruff, mypy y pytest ya la soportan  y uv descarga su propia versión de Python, así que no depende de los instaladores de python.



## Herramientas

| Herramienta | Uso |
|---|---|
| `uv` | Gestionar las dependencias del proyecto |
| `ruff` | Comprobar el estilo y los errores del código en cada PR |
| `pytest` | Ejecutar las pruebas |