import pytest
from django.db.models import ProtectedError
from django.urls import reverse
from model_bakery import baker

from django_assertions import assert_contains
from ubatuba.hospede.models import Hospede
from ubatuba.reserva.models import Reserva


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


def test_delete_hospede_with_reserva_error(db):
    hospede = Hospede.objects.create(
        nome='Victor',
        cpf='654.514.780-31',
        telefone='(11) 12345-1234',
    )
    Reserva.objects.create(
        hospede=hospede,
        data_entrada='2021-09-28 12:40:00',
        data_saida='2021-09-28 12:41:00',
        qtd_pessoas_adulto=3,
        qtd_pessoas_crianca=3,
        pago=True,
        valor_pago_total=100,
        valor_pago_parcial=0,
        pagara_limpeza=True,
        observacao=''
    )
    Reserva.objects.get(data_entrada='2021-09-28 12:40:00').delete()
    assert pytest.raises(ProtectedError)
