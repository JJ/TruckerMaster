# Elección de Herramientas

## Gestor de tareas
 
Un gestor de tareas permite lanzar, como subcomandos de un solo programa, todas las tareas que hay que llevar a cabo en el proyecto definidas en un único fichero. Ahora mismo, para comprobar el código hay que ejecutar a mano `uv run ruff check .`, `uv run mypy` y `uv run pytest`, y el workflow `lint.yml` repite esas órdenes por su cuenta.

Se comparan make, invoke y just. Destacar que uv no permite definir tareas, luego no sirve como gestor de tareas. Los criterios a saber son los siguientes:

- **Estilo de configuración:** declarativa (las tareas se describen en un fichero) o imperativa (se escriben como código).
- **Estándar:** si la herramienta sigue un estándar.
- **Qué hay que instalar:** qué hace falta para usarla.
- **Espacio que ocupa:** lo que ocupa la herramienta una vez instalada.
- **Tiempo en ejecutar `lint`:** lo que tarda en lanzar una tarea `lint` que ejecuta `uv run ruff check .`.

Se adjuntan capturas mostrando las mediciones, para contrastar los datos.

| Herramienta | Estilo de configuración | Estándar | Qué hay que instalar | Espacio que ocupa | Tiempo en ejecutar `lint` |
|---|---|---|---|---|---|
| make | Declarativa | Sí (POSIX) | Nada | 284 KB | 0,060 s |
| just | Declarativa | No | Un único programa | 6,3 MB | 0,022 s |
| invoke | Imperativa | No | Un paquete de Python | 780 KB | 0,247 s |

Mediciones de Make:

![Mediciones de Make](../imgs/medir_make.png)

Mediciones de Just:

![Mediciones de Just](../imgs/medir_just.png)

Mediciones de Invoke:

![Mediciones de Invoke](../imgs/medir_invoke.png)

Se tiene observando la tabla que invoke es el único imperativo, definiendo las tareas en un archivo `.py`. Además se trata de un paquete que hay que instalar y es el que más tarda en ejecutar `lint`. Por otro lado, just es el más rápido, pero la diferencia con make es de unas centésimas de segundo, mientras que make sigue un estándar (POSIX), no hay que instalar nada y ocupa 284 KB frente a los 6,3 MB de just.

Por tanto, se elige make, donde cada objetivo del `Makefile` es una tarea que se lanza con `make <tarea>`.
