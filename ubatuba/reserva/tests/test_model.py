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
def resp(client, reservas):
    resp = client.get(reverse('reserva:reservation'))
    return resp


def test_reserva_in_page(resp, reservas):
    for reserva in reservas:
        for hospede in reserva.hospede.all():
            assert_contains(resp, hospede)
