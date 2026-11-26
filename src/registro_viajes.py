from collections.abc import Mapping
from dataclasses import dataclass

from viaje import Viaje


@dataclass(frozen=True)
class RegistroViaje:
    viajes_por_camionero: Mapping[str, Mapping[int, tuple[Viaje, ...]]]
