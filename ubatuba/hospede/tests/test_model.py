import pytest
from django.urls import reverse
from model_mommy import mommy

from django_assertions import assert_contains
from ubatuba.hospede.models import Hospede


@pytest.fixture
def hospedes(db):
    hospedes = mommy.make(Hospede, 2)
    return hospedes


@pytest.fixture
def resp(client, hospedes):
    resp = client.get(reverse('hospede:hospede'))
    return resp


def test_hospede_in_page(resp, hospedes):
    for hospede in hospedes:
        assert_contains(resp, hospede.nome)
