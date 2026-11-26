from dataclasses import dataclass

from camionero import Camionero
from registro_viajes import RegistroViaje


@dataclass
class Oficina:
    camioneros_por_identificador: dict[str, Camionero]
    registro_viajes: RegistroViaje
