from django.forms import ModelForm

from ubatuba.hospede.models import Hospede


class HospedeForm(ModelForm):
    class Meta:
        model = Hospede
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})
        self.fields['data_nascimento'].widget.attrs.update({'class': 'mask-data-nascimento'})
