from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from ubatuba.reserva.forms import ReservaForm
from ubatuba.reserva.models import Reserva


def reservation(request):
    reservas = Reserva.objects.all().order_by('data_entrada')
    context = {
        'reservas': reservas
    }
    return render(request, 'reserva/reservation.html', context)


@login_required
def create_reserva(request):
    reservas = Reserva.objects.all().order_by('data_entrada')
    if request.method == 'POST':
        form = ReservaForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('reserva:reservation'))
    else:
        form = ReservaForm()
    context = {'form': form, 'reservas': reservas}
    return render(request, 'reserva/reservation-form.html', context)


@login_required
def update_reserva(request, pk):
    reserva = Reserva.objects.get(pk=pk)
    form = ReservaForm(instance=reserva)

    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('reserva:reservation'))

    context = {'form': form}
    return render(request, 'reserva/reservation-form-update.html', context)


@login_required
def delete_reserva(request, pk):
    reserva = Reserva.objects.get(pk=pk)
    if request.method == 'POST':
        reserva.delete()
        return HttpResponseRedirect(reverse('reserva:reservation'))
    context = {'reserva': reserva}
    return render(request, 'reserva/reserva-form-delete.html', context)
