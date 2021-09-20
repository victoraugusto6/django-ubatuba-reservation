import pytest
from django.urls import reverse

from ubatuba.hospede.forms import HospedeForm
from ubatuba.hospede.models import Hospede


@pytest.mark.parametrize(
    'nome, cpf, data_nascimento, telefone,endereco, avaliacao, observacao',
    [('Victor', '654.514.780-31', '1995-12-19', '(11) 12345-1234', 'Rua 1', '', '')])
def test_form_success(db, nome, cpf, data_nascimento, telefone, endereco, avaliacao, observacao):
    form = HospedeForm(data={
        'nome': nome,
        'cpf': cpf,
        'data_nascimento': data_nascimento,
        'telefone': telefone,
        'endereco': endereco,
        'avaliacao': avaliacao,
        'observacao': observacao
    })
    assert form.is_valid()
    assert form.cleaned_data['telefone'] == '11123451234'


@pytest.fixture
def resp_create_hospede(client, db, admin_user):
    client.force_login(admin_user)
    resp_create = client.post(reverse('hospede:create_hospedes'), data={
        'nome': 'Victor',
        'cpf': '654.514.780-31',
        'data_nascimento': '1995-12-19',
        'telefone': '(11) 12345-1234',
        'endereco': 'Rua 1'
    })
    return resp_create


def test_hospede_exists_bd(resp_create_hospede):
    assert Hospede.objects.exists()


@pytest.fixture
def hospede(db):
    return Hospede.objects.create(
        nome='Victor Augusto',
        cpf='654.514.780-31',
        data_nascimento='1995-12-19',
        telefone='(11) 12345-1234',
        endereco='Rua 1'
    )


@pytest.fixture
def resp_update_hospede(client, db, admin_user, hospede):
    client.force_login(admin_user)
    resp_update = client.post(reverse('hospede:update_hospede', kwargs={'pk': hospede.pk}),
                              data={
                                  'nome': 'Victor Augusto',
                                  'cpf': '654.514.780-31',
                                  'data_nascimento': '1995-12-19',
                                  'telefone': '(11) 12345-1234',
                                  'endereco': 'Rua 2'
                              })
    return resp_update


def test_update_hospede(resp_update_hospede):
    assert Hospede.objects.get(nome='Victor Augusto')
    assert Hospede.objects.get(endereco='Rua 2')


@pytest.fixture
def resp_delete_hospede(client, db, admin_user, hospede):
    client.force_login(admin_user)
    resp_delete = client.post(reverse('hospede:delete_hospede', kwargs={'pk': hospede.pk}))
    return resp_delete


def test_delete_hospede(resp_delete_hospede):
    assert not Hospede.objects.exists()
