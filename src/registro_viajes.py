from dataclasses import dataclass

from camionero import Camionero
from disponibilidad import Disponibilidad
from viaje import Viaje


@dataclass
class RegistroViaje:
    viajes_por_camionero: dict[str, dict[int, list[Viaje]]]

    def asignar(self, camionero: Camionero, mes: int, viaje: Viaje) -> None:
        if camionero.disponibilidad == Disponibilidad.NO_DISPONIBLE:
            raise ValueError("El camionero no está disponible")
        viajes = self.viajes_por_camionero.setdefault(camionero.identificador, {})
        viajes.setdefault(mes, []).append(viaje)
