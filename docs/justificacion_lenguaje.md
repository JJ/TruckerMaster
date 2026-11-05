# Justificación del lenguaje

## Lenguaje: Python

Se elige Python porque permite resolver el problema, su biblioteca estándar ya trae lo necesario para el modelo, las `dataclass` y los `Enum` sirven para definir entidades y objetos valor sin necesidad de dependencias externas, y `@dataclass(frozen=True)` hace que un objeto valor sea inmutable. El motivo principal escogido es que es multiplataforma, lo que facilita el desarrollo en el que cada uno tiene su propio SO.

## Versión:  3.13

La versión mínima se fija en `pyproject.toml` con `requires-python = ">=3.13"`.Es la misma que usa Ruff para comprobar el código (`target-version = "py313"`),
así que el linter revisa el código contra la versión con la que se ejecuta.
Se elige la 3.13 porque el código no usa nada de versiones posteriores. Por otro lado, las versiones 3.11 y 3.12 tienen menos soporte (aproximadamente hasta 2027), mientras que la versión elegida tiene soporte hasta octubre de 2029.  Además, uv, Ruff, mypy y pytest ya la soportan  y uv descarga su propia versión de Python, así que no depende de los instaladores de python.



## Herramientas

Se ha realizado una búsqueda de las distintas herramientas analizando las caraceterísticas de unas frente a otras. 

| Herramienta | Uso | Alternativas | Por qué se elige esta |
|---|---|---|---|
| `uv` | Gestionar las dependencias del proyecto | pip, Poetry | Sustituye a pip, Poetry y pyenv en una sola herramienta ya que, gestiona dependencias, genera el fichero de bloqueo (`uv.lock`) e instala versiones de Python. Según su documentación es entre 10 y 100 veces más rápido que pip. |
| `ruff` | Comprobar el estilo y los errores del código en cada PR | Flake8 | Las reglas que usamos (`E`, `W`, `F`, `I`, `N`, `B`) en Flake8 necesitan plugins como isort, pep8-naming o flake8-bugbear. Ruff las reimplementa todas y es entre 10 y 100 veces más rápido. No permite reglas propias, pero no las necesitamos. |
| `mypy` | Comprobar los tipos en cada PR | Pyright | En Python los tipos son opcionales y se pueden mezclar funciones anotadas con otras sin anotar (tipado gradual); mypy solo comprueba lo anotado. Como Ruff, con la regla `ANN`, obliga a anotar todo, mypy acaba revisando todo el código. Además se instala con uv como el resto de herramientas. |
| `pytest` | Ejecutar las pruebas | unittest | Las pruebas se escriben con `assert` normal y fixtures, sin clases ni métodos como `self.assertEqual`, y además puede ejecutar pruebas escritas con unittest. |