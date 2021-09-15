# @pytest.mark.parametrize(
#     'nome, cpf, data_nascimento, telefone,endereco, avaliacao, observacao',
#     [('Victor', '654.514.780-31', '1995-12-19', '(11) 12345-1234', 'Rua 1', '', '')])
# def test_form_success(db, nome, cpf, data_nascimento, telefone, endereco, avaliacao, observacao):
#     form = HospedeForm(data={
#         'nome': nome,
#         'cpf': cpf,
#         'data_nascimento': data_nascimento,
#         'telefone': telefone,
#         'endereco': endereco,
#         'avaliacao': avaliacao,
#         'observacao': observacao
#     })
#     assert form.is_valid()


# @pytest.fixture
# def resp(client, db):
#     resp = client.post(reverse('hospede:create_hospedes'), data={
#         'nome': 'Victor',
#         'cpf': '654.514.780-31',
#         'data_nascimento': '1995-12-19',
#         'telefone': '(11) 12345-1234',
#         'endereco': 'Rua 1'
#     })
#     print(resp.status_code)
#     return resp
#
#
# def test_hospede_exists_bd(resp):
#     assert Hospede.objects.exists()
