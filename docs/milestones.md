# Milestones

## [M0] Infraestructura y Organización
**Producto:** el modelo del problema en código. Incluye los actores (camionero, oficina y destinatario), sus roles y lo que puede hacer cada uno, las entidades del problema (viaje e historial de viajes y ganancias de cada camionero) y las **interfaces de comunicación** entre el sistema y los actores y entre las partes del propio sistema.

_Las interfaces de comunicación son tan importantes porque nos permiten trabajar en paralelo en módulos distintos._

**Qué lo hace válido:** el código del modelo pasa sin errores la comprobación de sintaxis del lenguaje (que compile o que pase el linter), y esto se comprueba de forma automática en cada PR. Además, el modelo tiene que cubrir lo que piden las historias de usuario.

## [M1] Registro de usuarios
Habilitación de la plataforma de identidad que almacena los diferentes usuarios del servicio, registrando sus particularidades y diferentes perfiles. Esta plataforma actúa como punto de entrada y permite presentar diferentes acciones e interfaces en función del rol. Es válido cuando un usuario puede identificarse y ve opciones distintas dependiendo de si e camionero u otro rol.

[M2] Registro de llegada/disponibilidad
Creación de la lógica de negocio e interfaz que permite a los usuarios camioneros registrar su llegada a base y su disponibilidad para tomar otro trabajo, y a los gestores visualizar los camioneros disponibles. Permite al camionero registrar su llegada y marcarse como disponible, y al gestor ver la lista de camioneros disponibles. Es válido cuando un camionero se marca como disponible y aparece en la lista que ve el gestor.