from dataclasses import dataclass

from viaje import Viaje


@dataclass
class RegistroViaje:
    historial_viajes: dict[str, list[Viaje]]
