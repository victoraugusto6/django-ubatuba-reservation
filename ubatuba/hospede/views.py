from django.shortcuts import render

from ubatuba.hospede.models import Hospede


def hospede(request):
    hospedes = Hospede.objects.all().order_by('nome')
    context = {
        'hospedes': hospedes
    }
    return render(request, 'hospede/hospede.html', context)
