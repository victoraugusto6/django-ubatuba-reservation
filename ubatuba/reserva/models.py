from decimal import Decimal

from decouple import config
from django.core.exceptions import ValidationError
from django.db import models

from ubatuba.hospede.models import Hospede

STATUS_PAY = (
    ('false', 'Não'),
    ('true', 'Sim'),
    ('partial', 'Parcial'),
)

YES_OR_NO = (
    (True, 'Sim'),
    (False, 'Não'),
)


class Reserva(models.Model):
    hospede = models.ForeignKey(Hospede, on_delete=models.PROTECT, verbose_name='Hóspede')
    data_entrada = models.DateTimeField(verbose_name='Data - Entrada')
    data_saida = models.DateTimeField(verbose_name='Data - Saída')
    qtd_pessoas_adulto = models.PositiveIntegerField(verbose_name='Qtd. Adultos')
    qtd_pessoas_crianca = models.PositiveIntegerField(verbose_name='Qtd. Crianças')
    pago = models.CharField(max_length=10, choices=STATUS_PAY)
    valor_pago_total = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor total')
    valor_pago_parcial = models.DecimalField(decimal_places=2, max_digits=6, default=0, verbose_name='Valor adiantado')
    pagara_limpeza = models.BooleanField(choices=YES_OR_NO, default=True, verbose_name='Incluir limpeza?')
    payed_limpeza = models.BooleanField(default=False, editable=False)
    observacao = models.TextField(verbose_name='Observações', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.data_entrada > self.data_saida:
            raise ValidationError('Data de saída é menor que data de entrada.')
        elif self.qtd_pessoas_adulto + self.qtd_pessoas_crianca > 7:
            raise ValidationError('Número de pessoas maior do que permitido (7 pessoas).')
        elif self.pagara_limpeza and self.payed_limpeza is False:
            self.valor_pago_total += Decimal(config('VALOR_LIMPEZA'))
            self.payed_limpeza = True
        elif self.pagara_limpeza is False and self.payed_limpeza:
            self.payed_limpeza = False
            self.valor_pago_total -= Decimal(config('VALOR_LIMPEZA'))
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.data_entrada)
