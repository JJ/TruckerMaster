from dataclasses import FrozenInstanceError

import pytest

from camionero import Camionero
from destinatario import Destinatario
from disponibilidad import Disponibilidad
from preferencias import Preferencias
from registro_viajes import RegistroViaje
from viaje import Viaje


def _build_destinatario() -> Destinatario:
    return Destinatario(identificador="D-001", nombre="Ana")


def _build_preferencias() -> Preferencias:
    return Preferencias(distancia_max_km=350.0, acepta_mercancia_especial=True)


def _build_camionero() -> Camionero:
    return Camionero(
        identificador="C-001",
        nombre="Luis",
        preferencias=_build_preferencias(),
        disponibilidad=Disponibilidad.DISPONIBLE_EN_CASA,
    )


def _build_viaje() -> Viaje:
    return Viaje(
        identificador="V-001",
        distancia_km=420.5,
        rentabilidad_euros=1500.0,
        mercancia_especial=True,
        destinatario=_build_destinatario(),
    )


def _build_registro_viaje() -> RegistroViaje:
    return RegistroViaje({"C-001": {1: [_build_viaje()]}})


@pytest.mark.parametrize(
    ("factory", "expected"),
    [
        (_build_destinatario, {"identificador": "D-001", "nombre": "Ana"}),
        (
            _build_preferencias,
            {"distancia_max_km": 350.0, "acepta_mercancia_especial": True},
        ),
        (
            _build_camionero,
            {
                "identificador": "C-001",
                "nombre": "Luis",
                "disponibilidad": Disponibilidad.DISPONIBLE_EN_CASA,
            },
        ),
        (
            _build_viaje,
            {
                "identificador": "V-001",
                "distancia_km": 420.5,
                "rentabilidad_euros": 1500.0,
                "mercancia_especial": True,
                "destinatario": _build_destinatario(),
            },
        ),
        (
            _build_registro_viaje,
            {"viajes_por_camionero": {"C-001": {1: [_build_viaje()]}}},
        ),
    ],
    ids=[
        "destinatario",
        "preferencias",
        "camionero",
        "viaje",
        "registro_viaje",
    ],
)
def test_objetos_se_crean_correctamente(factory, expected):
    objeto = factory()

    for nombre, valor_esperado in expected.items():
        assert getattr(objeto, nombre) == valor_esperado


@pytest.mark.parametrize(
    ("factory", "campo"),
    [
        (_build_destinatario, "nombre"),
        (_build_preferencias, "distancia_max_km"),
        (_build_camionero, "nombre"),
        (_build_viaje, "rentabilidad_euros"),
        (_build_registro_viaje, "viajes_por_camionero"),
    ],
    ids=[
        "destinatario",
        "preferencias",
        "camionero",
        "viaje",
        "registro_viaje",
    ],
)
def test_objetos_son_inmutables(factory, campo):
    objeto = factory()

    with pytest.raises(FrozenInstanceError):
        setattr(objeto, campo, "valor-modificado")


def test_disponibilidad_es_un_enum_inmutable():
    assert Disponibilidad.DISPONIBLE_EN_CASA == Disponibilidad.DISPONIBLE_EN_CASA
    assert Disponibilidad.DISPONIBLE_EN_CASA.name == "DISPONIBLE_EN_CASA"
