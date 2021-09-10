from django.shortcuts import render

from ubatuba.reserva.models import Reserva


def reservation(request):
    reservas = Reserva.objects.all().order_by('data_de')
    context = {
        'reservas': reservas
    }
    return render(request, 'reserva/reservation.html', context)
