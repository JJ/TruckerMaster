from dataclasses import dataclass

from viaje import Viaje


@dataclass
class RegistroViaje:
    viajes_por_camionero: dict[str, dict[int, list[Viaje]]]
