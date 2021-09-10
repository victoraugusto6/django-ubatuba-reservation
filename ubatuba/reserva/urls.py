from django.urls import path
from ubatuba.reserva import views

app_name = 'reserva'
urlpatterns = [
    path('', views.reservation, name='reservation'),
]
