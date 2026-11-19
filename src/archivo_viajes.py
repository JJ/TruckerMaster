from dataclasses import dataclass

from registro_viajes import RegistroViaje


@dataclass
class ArchivoViajes:
    historial_viajes: dict[str, list[RegistroViaje]]
