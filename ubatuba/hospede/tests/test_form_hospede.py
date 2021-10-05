import pytest

from ubatuba.hospede.forms import HospedeForm


@pytest.mark.parametrize(
    'nome, cpf, data_nascimento, telefone,endereco, avaliacao, observacao',
    [('Victor', '654.514.780-31', '1995-12-19', '(11) 12345-1234', 'Rua 1', '', ''),
     ('Pedro', '', '1995-12-19', '(11) 12345-9877', 'Rua 2', '', '')])
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


def test_form_telefone_validation(db):
    form = HospedeForm(data={
        'nome': 'Victor',
        'cpf': '397.738.908-48',
        'data_nascimento': '1995-12-19',
        'telefone': '(12) 99207-1544',
        'endereco': 'Rua 1'
    })

    assert form.is_valid()
    assert form.cleaned_data['telefone'] == '12992071544'


def test_form_cpf_validation(db):
    form = HospedeForm(data={
        'nome': 'Victor',
        'cpf': '397.738.908-48',
        'data_nascimento': '1995-12-19',
        'telefone': '(12) 99207-1544',
        'endereco': 'Rua 1'
    })

    assert form.is_valid()
    assert form.cleaned_data['cpf'] == '39773890848'
