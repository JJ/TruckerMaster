from viaje import Viaje


def repite_viaje_lejano(
    ultimo_viaje: Viaje, nuevo_viaje: Viaje, distancia_lejana_km: float
) -> bool:
    distancia_mas_corta = min(ultimo_viaje.distancia_km, nuevo_viaje.distancia_km)
    return distancia_mas_corta >= distancia_lejana_km
