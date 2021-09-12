from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from ubatuba.hospede.forms import HospedeForm
from ubatuba.hospede.models import Hospede


def hospede(request):
    hospedes = Hospede.objects.all().order_by('nome')
    context = {
        'hospedes': hospedes
    }
    return render(request, 'hospede/hospede.html', context)


def hospedes(request):
    return render(request, 'hospede/hospede-form.html')


def create_hospedes(request):
    if request.method == 'POST':
        form = HospedeForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('hospede:hospede'))
    else:
        form = HospedeForm()

    context = {
        'form': form,
    }

    return render(request, 'hospede/hospede-form.html', context)
