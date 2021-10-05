import pytest
from django.urls import reverse
from model_bakery import baker

from django_assertions import assert_contains
from ubatuba.hospede.models import Hospede


@pytest.fixture
def hospedes(db):
    hospedes = baker.make('Hospede', 2)
    return hospedes


@pytest.fixture
def hospede(db):
    hospede = Hospede.objects.create(
        nome='Victor',
        cpf='654.514.780-31',
        telefone='(11) 12345-1234',
    )
    return hospede


@pytest.fixture
def resp(client, admin_user, hospedes):
    client.force_login(admin_user)
    resp = client.get(reverse('hospede:hospedes'))
    return resp


def test_hospede_in_page(resp, hospedes):
    for hospede in hospedes:
        assert_contains(resp, hospede.nome)


def test_hospede_normalize_fields(db, hospede):
    assert Hospede.objects.exists()
