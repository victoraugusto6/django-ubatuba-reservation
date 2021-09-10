from django.core.exceptions import ValidationError
from django.db import models


class Hospede(models.Model):
    nome = models.CharField(max_length=120, verbose_name='Nome')
    cpf = models.CharField(max_length=120, verbose_name='CPF')
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    endereco = models.CharField(max_length=120, verbose_name='Endereço')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Hóspedes'
        verbose_name = 'Hóspede'


STATUS_PAY = (
    ('false', 'Não'),
    ('true', 'Sim'),
    ('partial', 'Parcial'),
)


class Reserva(models.Model):
    hospede = models.ManyToManyField(Hospede)
    data_de = models.DateField(verbose_name='Data - Entrada')
    data_ate = models.DateField(verbose_name='Data - Saída')
    qtd_pessoas_adulto = models.IntegerField(verbose_name='Qtd. Adultos')
    qtd_pessoas_crianca = models.IntegerField(verbose_name='Qtd. Crianças')
    pago = models.CharField(max_length=10, choices=STATUS_PAY)
    valor = models.FloatField()

    def save(self, *args, **kwargs):
        if self.data_de > self.data_ate:
            raise ValidationError('Data de saída é menor que data de entrada.')
        elif self.qtd_pessoas_adulto + self.qtd_pessoas_crianca > 7:
            raise ValidationError('Número de pessoas maior do que permitido (7 pessoas).')
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.data_de)
