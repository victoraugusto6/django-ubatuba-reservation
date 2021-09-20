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
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})
        self.fields['data_nascimento'].widget.attrs.update({'class': 'mask-data-nascimento'})
        self.fields['observacao'].widget.attrs['rows'] = 3
        self.fields['observacao'].widget.attrs['columns'] = 3

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if telefone:
            telefone = re.sub(r'\D+', '', telefone)
        return telefone
