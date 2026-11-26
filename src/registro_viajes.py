from dataclasses import dataclass
from types import MappingProxyType

from viaje import Viaje


@dataclass(frozen=True)
class RegistroViaje:
    viajes_por_camionero: dict[str, dict[int, list[Viaje]]]

    def __post_init__(self) -> None:
        viajes_por_camionero = {
            camionero: {
                dia: tuple(viajes)
                for dia, viajes in viajes_por_dia.items()
            }
            for camionero, viajes_por_dia in self.viajes_por_camionero.items()
        }
        object.__setattr__(
            self,
            "viajes_por_camionero",
            MappingProxyType(
                {
                    camionero: MappingProxyType(viajes_por_dia)
                    for camionero, viajes_por_dia in viajes_por_camionero.items()
                }
            ),
        )
