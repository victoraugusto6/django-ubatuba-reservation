from django.forms import ModelForm

from ubatuba.reserva.models import Reserva


class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        exclude = [
            'created_at',
            'updated_at'
        ]

    def clean(self):
        super(ReservaForm, self).clean()

        qtd_pessoas_adulto = self.cleaned_data.get('qtd_pessoas_adulto')
        qtd_pessoas_crianca = self.cleaned_data.get('qtd_pessoas_crianca')

        data_entrada = self.cleaned_data.get('data_entrada')
        data_saida = self.cleaned_data.get('data_saida')

        if qtd_pessoas_adulto + qtd_pessoas_crianca > 7:
            self._errors['qtd_pessoas_adulto'] = self.error_class([
                'Número de pessoas maior do que permitido (7 pessoas).'])
        elif data_entrada > data_saida:
            self._errors['data_entrada'] = self.error_class([
                'Data de saída é menor que data de entrada.'])
