from dataclasses import FrozenInstanceError, is_dataclass
from unittest.mock import Mock

import pytest

from camionero import Camionero
from disponibilidad import Disponibilidad
from preferencias import Preferencias


def test_camionero_initialization() -> None:
    preferencias_mock = Mock(spec=Preferencias)
    disponibilidad_mock = Mock(spec=Disponibilidad)

    camionero = Camionero(
        identificador="DRV-001",
        nombre="Ana García",
        preferencias=preferencias_mock,
        disponibilidad=disponibilidad_mock,
    )

    assert is_dataclass(camionero)
    assert camionero.identificador == "DRV-001"
    assert camionero.nombre == "Ana García"
    assert camionero.preferencias is preferencias_mock
    assert camionero.disponibilidad is disponibilidad_mock


def test_camionero_equality() -> None:
    preferencias_mock = Mock(spec=Preferencias)
    disponibilidad_mock = Mock(spec=Disponibilidad)

    c1 = Camionero("DRV-001", "Ana García", preferencias_mock, disponibilidad_mock)
    c2 = Camionero("DRV-001", "Ana García", preferencias_mock, disponibilidad_mock)
    c3 = Camionero("DRV-002", "Luis Pérez", preferencias_mock, disponibilidad_mock)

    assert c1 == c2
    assert c1 != c3
