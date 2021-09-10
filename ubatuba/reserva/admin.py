from django.contrib import admin

from ubatuba.reserva.models import Hospede, Reserva


@admin.register(Hospede)
class HospedeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')
    ordering = ('nome',)
    search_fields = ('nome', 'cpf',)
    list_filter = ('nome', 'cpf',)


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('data_de', 'data_ate', 'qtd_pessoas_adulto', 'qtd_pessoas_crianca', 'pago', 'valor',)
    ordering = ('data_de',)
