from camionero import Camionero
from disponibilidad import Disponibilidad


def apuntar_disponible(camioneros: dict[str, Camionero], id_camionero: str) -> None:
    camioneros[id_camionero].disponibilidad = Disponibilidad.DISPONIBLE_EN_TERMINAL
