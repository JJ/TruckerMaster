from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class EstadoDisponibilidad(Enum):
    DISPONIBLE_EN_TERMINAL = "disponible en terminal"
    DISPONIBLE_EN_CASA = "disponible en casa"
    NO_DISPONIBLE = "no disponible"


class DisponibilidadInvalidaError(ValueError):
    pass


@dataclass(frozen=True)
class Disponibilidad:
    camionero: str
    instante: datetime
    estado: EstadoDisponibilidad

    def __post_init__(self) -> None:
        if not self.camionero.strip():
            raise DisponibilidadInvalidaError(
                "La disponibilidad debe indicar qué camionero la declara."
            )
