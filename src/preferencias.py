from dataclasses import dataclass


@dataclass(frozen=True)
class Preferencias:
    distancia_max_m: float
    acepta_mercancia_especial: bool
