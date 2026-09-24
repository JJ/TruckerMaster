# Guía de estilo y buenas prácticas

Este documento recoge las normas de código que seguimos en el proyecto para que todo el código tenga un estilo homogéneo.

## Lenguaje y versión
- Lenguaje: python 3.13.

## Nombres
| Elemento             | Convención    | Ejemplo            |
|----------------------|---------------|--------------------|
| Variables            | snake_case    | `ruta_actual`      |
| Funciones y métodos  | snake_case    | `calcular_ruta()`  |
| Clases               | PascalCase    | `CamioneroPremium` |
| Constantes           | UPPER_CASE    | `MAX_HORAS`        |
| Módulos (ficheros)   | snake_case    | `gestor_rutas.py`  |
| Atributos internos   | _snake_case   | `_cache_rutas`     |

- Identificadores en español, sin tildes ni ñ.
- Comentarios y docstrings en español.

## Formato
- 4 espacios por nivel de indentación, nunca tabulaciones.
- Longitud máxima de línea: 88 caracteres.
- Dos líneas en blanco entre funciones y clases de nivel superior;
  una entre métodos de una clase.
- Imports al principio del fichero, agrupados: biblioteca estándar,
  dependencias externas y módulos del proyecto.

## Comentarios y documentación
- Toda clase y función pública lleva docstring en estilo Google:

```python
def calcular_ruta(origen: str, destino: str) -> list[str]:
    """Calcula la ruta más corta entre dos ciudades.

    Args:
        origen: Ciudad de salida.
        destino: Ciudad de llegada.

    Returns:
        Lista de ciudades por las que pasa la ruta.
    """
```

## Estructura del proyecto
```
src/truckermaster/   código fuente
tests/               tests (pytest), un test_<modulo>.py por módulo
docs/                documentación
pyproject.toml       dependencias y configuración de herramientas
```

## Buenas prácticas
- Funciones cortas y con una única responsabilidad.
- Evitar código duplicado.
- Nunca usar `except:` a secas ni silenciar excepciones; capturar
  la excepción concreta.
- No usar valores mutables como argumentos por defecto (`def f(x=[])`).
