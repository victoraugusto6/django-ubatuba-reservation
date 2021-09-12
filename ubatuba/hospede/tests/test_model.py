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
def hospede(db):
    hospede = Hospede.objects.create(
        nome='Victor',
        cpf='397.738.908-48',
        data_nascimento='1995-12-19',
        telefone='(12) 99207-1544',
        endereco='Rua 1'
    )
    return hospede


@pytest.fixture
def resp(client, hospedes):
    resp = client.get(reverse('hospede:hospedes'))
    return resp


def test_hospede_in_page(resp, hospedes):
    for hospede in hospedes:
        assert_contains(resp, hospede.nome)


def test_hospede_normalize_fields(db, hospede):
    assert Hospede.objects.exists()
