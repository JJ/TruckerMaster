from dataclasses import dataclass


@dataclass(frozen=True)
class Preferencias:
    distancia_max_km: float
    acepta_mercancia_especial: bool
