from dataclasses import dataclass

from src.disponibilidad import Disponibilidad

from src.preferencias import Preferencias


@dataclass
class Camionero:
    identificador: str
    nombre: str
    preferencias: Preferencias
    disponibilidad: Disponibilidad
