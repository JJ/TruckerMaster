from enum import Enum, auto


class Disponibilidad(Enum):
    DISPONIBLE_EN_TERMINAL = auto()
    DISPONIBLE_EN_CASA = auto()
    NO_DISPONIBLE = auto()
