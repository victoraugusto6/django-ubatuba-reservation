from django.forms import ModelForm

from ubatuba.reserva.models import Reserva


class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        exclude = [
            'created_at',
            'updated_at'
        ]
