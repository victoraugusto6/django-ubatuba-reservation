import pytest
from django.urls import reverse
from model_bakery import baker

from django_assertions import assert_contains
from ubatuba.hospede.models import Hospede
from ubatuba.reserva.models import Reserva


@pytest.fixture
def reservas(db):
    reservas = baker.make('Reserva', 2, qtd_pessoas_adulto=6, qtd_pessoas_crianca=1)
    return reservas


@pytest.fixture
def reserva(db):
    return baker.make('Reserva', 1, qtd_pessoas_adulto=5, qtd_pessoas_crianca=1)


@pytest.fixture
def hospede(db):
    return Hospede.objects.create(
        nome='Victor Augusto',
        cpf='65451478031',
        telefone='11123451234',
    )


@pytest.fixture
def resp(client, admin_user, reservas):
    client.force_login(admin_user)
    resp = client.get(reverse('reserva:reservation'))
    return resp


def test_reserva_in_page(resp, reservas):
    for reserva in reservas:
        assert_contains(resp, reserva.hospede)


def test_reserva_normalize_fields(db, reserva):
    assert Reserva.objects.exists()


@pytest.fixture
def reserva_test_limpeza_pago(db, hospede):
    return Reserva.objects.create(
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


def test_exists_banco(reserva_test_limpeza_pago):
    assert Reserva.objects.exists()


def test_valor_limpeza_aplicado(reserva_test_limpeza_pago):
    assert Reserva.objects.get(
        valor_pago_total=190
    )


def test_valor_limpeza_removido(reserva_test_limpeza_pago):
    assert Reserva.objects.get(
        valor_pago_total=190
    )
    reserva = Reserva.objects.get(data_entrada='2021-09-28 12:40:00')
    reserva.pagara_limpeza = False
    reserva.save()
    assert reserva.valor_pago_total == 100
