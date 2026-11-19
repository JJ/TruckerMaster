from camionero import Camionero
from disponibilidad import Disponibilidad


def apuntarse_disponible(camioneros: dict[str, Camionero], quien_apunta: str) -> None:
    camioneros[quien_apunta].disponibilidad = Disponibilidad.DISPONIBLE_EN_TERMINAL
