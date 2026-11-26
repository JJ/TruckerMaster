from dataclasses import dataclass

from camionero import Camionero
from viaje import Viaje


@dataclass
class Oficina:
    camioneros_por_identificador: dict[str, Camionero]
    viajes_por_camionero: dict[str, dict[int, list[Viaje]]]
