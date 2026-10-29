from dataclasses import dataclass

from src.disponibilidad import Disponibilidad

@dataclass
class Camionero:
    identificador: str
    nombre: str
    preferencias: Preferencias
    disponibilidad: Disponibilidad
