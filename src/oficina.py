from dataclasses import dataclass
from datetime import date

from camionero import Camionero
from disponibilidad import Disponibilidad
from viaje import Viaje


@dataclass
class Oficina:
    camioneros_por_identificador: dict[str, Camionero]
    viajes_por_camionero: dict[str, dict[date, Viaje]]

    def asignar(self, identificador: str, fecha: date, viaje: Viaje) -> None:
        camionero = self.camioneros_por_identificador[identificador]
        if camionero.disponibilidad == Disponibilidad.NO_DISPONIBLE:
            raise ValueError("El camionero no está disponible")
        viajes = self.viajes_por_camionero.setdefault(identificador, {})
        viajes[fecha] = viaje

