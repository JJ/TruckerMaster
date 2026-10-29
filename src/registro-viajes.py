from dataclasses import dataclass
import datetime


@dataclass
class RegistroViaje:
    id_caminionero: str
    id_viaje: str
    fecha_inicio: datetime.datetime
    fecha_fin: datetime.datetime
