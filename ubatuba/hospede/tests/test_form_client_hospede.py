import pytest
from django.urls import reverse

from ubatuba.hospede.models import Hospede


@pytest.fixture
def hospede(db):
    return Hospede.objects.create(
        nome='Victor Augusto',
        cpf='65451478031',
        telefone='11123451234',
    )


@pytest.fixture
def resp_create_hospede(client, db, admin_user):
    client.force_login(admin_user)
    resp_create = client.post(reverse('hospede:create_hospedes'), data={
        'nome': 'Victor',
        'cpf': '65451478031',
        'telefone': '11123451234',
    })
    return resp_create


def test_hospede_exists_bd(resp_create_hospede):
    assert Hospede.objects.exists()


@pytest.fixture
def resp_update_hospede(client, db, admin_user, hospede):
    client.force_login(admin_user)
    resp_update = client.post(reverse('hospede:update_hospede', kwargs={'pk': hospede.pk}),
                              data={
                                  'nome': 'Victor Augusto',
                                  'cpf': '65451478031',
                                  'telefone': '11123451234',
                              })
    return resp_update


def test_update_hospede(resp_update_hospede):
    assert Hospede.objects.get(nome='Victor Augusto')


@pytest.fixture
def resp_delete_hospede(client, db, admin_user, hospede):
    client.force_login(admin_user)
    resp_delete = client.post(reverse('hospede:delete_hospede', kwargs={'pk': hospede.pk}))
    return resp_delete


def test_delete_hospede(resp_delete_hospede):
    assert not Hospede.objects.exists()
