from camionero import Camionero
from disponibilidad import Disponibilidad


def camioneros_disponibles(camioneros: dict[str, Camionero]) -> list[str]:
    return [
        identificador
        for identificador, camionero in camioneros.items()
        if camionero.disponibilidad is not Disponibilidad.NO_DISPONIBLE
    ]
