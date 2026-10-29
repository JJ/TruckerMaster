from dataclasses import dataclass

from destinatario import Destinatario


@dataclass
class Viaje:
    identificador: str
    distancia_km: float
    rentabilidad_euros: float
    mercancia_especial: bool
    destinatario: Destinatario
