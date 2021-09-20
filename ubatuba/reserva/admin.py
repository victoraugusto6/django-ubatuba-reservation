from django.contrib import admin

from ubatuba.reserva.models import Reserva


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = (
        'data_entrada',
        'data_saida',
        'qtd_pessoas_adulto',
        'qtd_pessoas_crianca',
        'pago',
        'valor_pago_total',
        'valor_pago_parcial',
        'pagara_limpeza',
        'created_at',
        'updated_at',
    )
    ordering = ('data_entrada',)
    search_fields = ('data_entrada', 'data_saida',)
    list_filter = ('pago',)
