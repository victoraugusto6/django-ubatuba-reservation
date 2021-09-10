from django.contrib import admin

from ubatuba.reserva.models import Reserva


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('data_de', 'data_ate', 'qtd_pessoas_adulto', 'qtd_pessoas_crianca', 'pago', 'valor',)
    ordering = ('data_de',)
