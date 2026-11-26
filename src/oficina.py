from dataclasses import dataclass

from camionero import Camionero
from registro_viajes import RegistroViaje


@dataclass
class Oficina:
    camioneros: dict[str, Camionero]
    registro_viajes: RegistroViaje
