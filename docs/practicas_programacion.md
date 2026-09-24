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

- No se usan tildes ni ñ (se comprobará con el linter)
- Identificadores en español (esto es una convención que se revisa manualmente)

## Formato
Estas normas de formato se comprobarán automáticamente con el linter:
- 4 espacios por nivel de indentación, nunca tabulaciones.
- Longitud máxima de línea: 88 caracteres.


## Comentarios y documentación
- NO SE PONEN COMENTARIOS EN EL CODIGO, las explicaciones van en los mensajes de commit.

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
