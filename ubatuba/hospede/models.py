from django.db import models


class Hospede(models.Model):
    nome = models.CharField(max_length=120, verbose_name='Nome')
    cpf = models.CharField(unique=True, max_length=14, verbose_name='CPF')
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=120, verbose_name='Endereço')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Hóspedes'
        verbose_name = 'Hóspede'
