from dataclasses import dataclass

@dataclass
class Asignacion:
    viaje: Viaje
    destino: Destinatario
    camionero_asignado: Camionero