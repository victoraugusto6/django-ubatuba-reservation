from django.forms import ModelForm

from ubatuba.reserva.models import Reserva


class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        exclude = [
            'created_at',
            'updated_at'
        ]
        localized_fields = ['valor_pago_total', 'valor_pago_parcial']

    def clean(self):
        super(ReservaForm, self).clean()

        qtd_pessoas_adulto = self.cleaned_data.get('qtd_pessoas_adulto')
        qtd_pessoas_crianca = self.cleaned_data.get('qtd_pessoas_crianca')

        data_entrada = self.cleaned_data.get('data_entrada')
        data_saida = self.cleaned_data.get('data_saida')

        if qtd_pessoas_adulto + qtd_pessoas_crianca > 7:
            self.add_error('__all__', 'Número de pessoas maior do que permitido (7 pessoas).')

        if data_entrada > data_saida:
            self.add_error('__all__', 'Data de saída é menor que data de entrada.')
