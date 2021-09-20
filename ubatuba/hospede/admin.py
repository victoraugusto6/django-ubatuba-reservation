from django.contrib import admin

from ubatuba.hospede.models import Hospede


@admin.register(Hospede)
class HospedeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'avaliacao', 'created_at', 'updated_at')
    ordering = ('nome',)
    search_fields = ('nome', 'cpf',)
    list_filter = ('avaliacao',)
