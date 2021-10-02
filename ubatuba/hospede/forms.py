import re

from django.forms import ModelForm

from ubatuba.hospede.models import Hospede


class HospedeForm(ModelForm):
    class Meta:
        model = Hospede
        fields = [
            'nome',
            'cpf',
            'data_nascimento',
            'telefone',
            'endereco',
            'avaliacao',
            'observacao'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].max_length = 14
        self.fields['telefone'].max_length = 15


    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if telefone:
            telefone = re.sub(r'\D+', '', telefone)
        return telefone

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf:
            cpf = re.sub(r'\D+', '', cpf)
        return cpf
