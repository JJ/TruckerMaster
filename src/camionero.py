from dataclasses import dataclass

from disponibilidad import Disponibilidad
from preferencias import Preferencias


@dataclass
class Camionero:
    identificador: str
    nombre: str
    preferencias: Preferencias
    disponibilidad: Disponibilidad

    def esta_disponible(self) -> bool:
        return self.disponibilidad != Disponibilidad.NO_DISPONIBLE
