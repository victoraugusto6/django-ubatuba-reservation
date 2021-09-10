from django.contrib import admin

from ubatuba.hospede.models import Hospede


@admin.register(Hospede)
class HospedeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')
    ordering = ('nome',)
    search_fields = ('nome', 'cpf',)
    list_filter = ('nome', 'cpf',)
