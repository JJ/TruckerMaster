from dataclasses import dataclass


@dataclass
class Viaje:
    distancia_km: float
    rentabilidad_euros: float
    mercancia_especial: bool
