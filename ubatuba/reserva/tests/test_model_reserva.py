import pytest
from django.urls import reverse
from model_mommy import mommy

from django_assertions import assert_contains
from ubatuba.reserva.models import Reserva


@pytest.fixture
def reservas(db):
    reservas = mommy.make(Reserva, 2, qtd_pessoas_adulto=6, qtd_pessoas_crianca=1)
    return reservas


@pytest.fixture
def reserva(db):
    return mommy.make(Reserva, 1, qtd_pessoas_adulto=5, qtd_pessoas_crianca=1)


@pytest.fixture
def resp(client, reservas):
    resp = client.get(reverse('reserva:reservation'))
    return resp


def test_reserva_in_page(resp, reservas):
    for reserva in reservas:
        assert_contains(resp, reserva.hospede)


def test_reserva_normalize_fields(db, reserva):
    assert Reserva.objects.exists()
