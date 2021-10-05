import pytest

from ubatuba.hospede.forms import HospedeForm


@pytest.mark.parametrize(
    'nome, cpf, telefone, avaliacao, observacao',
    [('Victor', '654.514.780-31', '(11) 12345-1234', '', ''),
     ('Pedro', '', '(11) 12345-9877', '', '')])
def test_form_success(db, nome, cpf, telefone, avaliacao, observacao):
    form = HospedeForm(data={
        'nome': nome,
        'cpf': cpf,
        'telefone': telefone,
        'avaliacao': avaliacao,
        'observacao': observacao
    })
    assert form.is_valid()


def test_form_telefone_validation(db):
    form = HospedeForm(data={
        'nome': 'Victor',
        'cpf': '397.738.908-48',
        'telefone': '(12) 99207-1544',
    })

    assert form.is_valid()
    assert form.cleaned_data['telefone'] == '12992071544'


def test_form_cpf_validation(db):
    form = HospedeForm(data={
        'nome': 'Victor',
        'cpf': '397.738.908-48',
        'telefone': '(12) 99207-1544',
    })

    assert form.is_valid()
    assert form.cleaned_data['cpf'] == '39773890848'
