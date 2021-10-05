import pytest
from django.urls import reverse

from ubatuba.hospede.models import Hospede
from ubatuba.reserva.models import Reserva


@pytest.fixture
def hospede(db):
    return Hospede.objects.create(
        nome='Victor Augusto',
        cpf='65451478031',
        telefone='11123451234',
    )


@pytest.fixture
def reserva(db, hospede):
    return Reserva.objects.create(
        hospede=hospede,
        data_entrada='2021-09-28 12:40:00',
        data_saida='2021-09-28 12:41:00',
        qtd_pessoas_adulto=1,
        qtd_pessoas_crianca=1,
        pago='true',
        valor_pago_total=100,
        valor_pago_parcial=0,
        pagara_limpeza=True,
        observacao=''
    )


@pytest.fixture
def resp_create_reserva(client, db, admin_user, hospede):
    client.force_login(admin_user)
    resp_create = client.post(reverse('reserva:create_reserva'), data={
        'hospede': hospede.pk,
        'data_entrada': '2021-09-28 12:40:00',
        'data_saida': '2021-09-29 12:40:00',
        'qtd_pessoas_adulto': 1,
        'qtd_pessoas_crianca': 1,
        'pago': 'true',
        'valor_pago_total': 100,
        'valor_pago_parcial': 0,
        'pagara_limpeza': True,
        'observacao': ''
    })
    return resp_create


def test_reserva_exists_bd(resp_create_reserva):
    assert Reserva.objects.exists()


@pytest.fixture
def resp_update_reserva(client, db, admin_user, hospede, reserva):
    client.force_login(admin_user)
    resp_update = client.post(reverse('reserva:update_reserva', kwargs={'pk': reserva.pk}), data={
        'hospede': hospede.pk,
        'data_entrada': '2021-09-28 12:40:00',
        'data_saida': '2021-09-29 12:40:00',
        'qtd_pessoas_adulto': 3,
        'qtd_pessoas_crianca': 3,
        'pago': 'true',
        'valor_pago_total': 100,
        'valor_pago_parcial': 0,
        'pagara_limpeza': True,
        'observacao': ''
    })
    return resp_update


def test_update_reserva(resp_update_reserva):
    assert Reserva.objects.get(
        qtd_pessoas_adulto=3,
        qtd_pessoas_crianca=3
    )


@pytest.fixture
def resp_delete_reserva(client, db, admin_user, reserva):
    client.force_login(admin_user)
    resp_delete = client.post(reverse('reserva:delete_reserva', kwargs={'pk': reserva.pk}))
    return resp_delete


def test_delete_hospede(resp_delete_reserva):
    assert not Reserva.objects.exists()
