from dataclasses import dataclass

from disponibilidad import Disponibilidad
from preferencias import Preferencias


@dataclass
class Camionero:
    preferencias: Preferencias
    disponibilidad: Disponibilidad
