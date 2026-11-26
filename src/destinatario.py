from dataclasses import dataclass


@dataclass(frozen=True)
class Destinatario:
    identificador: str
    nombre: str
