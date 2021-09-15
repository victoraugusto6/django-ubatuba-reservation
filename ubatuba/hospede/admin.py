from django.contrib import admin

from ubatuba.hospede.models import Hospede


@admin.register(Hospede)
class HospedeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'avaliacao', 'criado_em', 'atualizado_em')
    ordering = ('nome',)
    search_fields = ('nome', 'cpf',)
    list_filter = ('avaliacao',)
