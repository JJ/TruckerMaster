from dataclasses import dataclass

from disponibilidad import Disponibilidad
from preferencias import Preferencias


@dataclass
class Camionero:
    identificador: str
    nombre: str
    preferencias: Preferencias
    disponibilidad: Disponibilidad
