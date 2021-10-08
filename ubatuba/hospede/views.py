from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from ubatuba.hospede.forms import HospedeForm
from ubatuba.hospede.models import Hospede


@login_required
def hospedes(request):
    hospedes = Hospede.objects.all().order_by('nome')
    context = {'hospedes': hospedes}
    return render(request, 'hospede/hospede.html', context)


@login_required
def create_hospedes(request):
    if request.method == 'POST':
        form = HospedeForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('hospede:hospedes'))
    else:
        form = HospedeForm()
    context = {'form': form}
    return render(request, 'hospede/hospede-form.html', context)


@login_required
def update_hospede(request, pk):
    hospede = Hospede.objects.get(pk=pk)
    form = HospedeForm(instance=hospede)

    if request.method == 'POST':
        form = HospedeForm(request.POST, instance=hospede)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('hospede:hospedes'))

    context = {'form': form}
    return render(request, 'hospede/hospede-form-update.html', context)


@login_required
def delete_hospede(request, pk):
    hospede = Hospede.objects.get(pk=pk)
    if request.method == 'POST':
        try:
            hospede.delete()
            return HttpResponseRedirect(reverse('hospede:hospedes'))
        except ProtectedError:
            hospede = Hospede.objects.get(pk=pk)
            hospedes = Hospede.objects.all().order_by('nome')
            context = {'hospedes': hospedes,
                       'error': f'Não é possível deletar: {hospede} - Contém reservas cadastradas'}
            return render(request, 'hospede/hospede.html', context)
    context = {'hospede': hospede}
    return render(request, 'hospede/hospede-form-delete.html', context)
