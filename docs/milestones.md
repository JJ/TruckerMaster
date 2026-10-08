# Milestones

## [M0] Infraestructura y Organización
**Producto:** el modelo del problema en código. Incluye los actores (camionero, oficina y destinatario), sus roles y lo que puede hacer cada uno, las entidades del problema (viaje e historial de viajes y ganancias de cada camionero) y las **interfaces de comunicación** entre el sistema y los actores y entre las partes del propio sistema.

_Las interfaces de comunicación son tan importantes porque nos permiten trabajar en paralelo en módulos distintos._

**Qué lo hace válido:** el código del modelo pasa sin errores la comprobación de sintaxis del lenguaje (que compile o que pase el linter), y esto se comprueba de forma automática en cada PR. Además, el modelo tiene que cubrir lo que piden las historias de usuario.