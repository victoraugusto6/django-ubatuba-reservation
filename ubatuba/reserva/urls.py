from django.urls import path
from ubatuba.reserva import views

app_name = 'reserva'
urlpatterns = [
    path('', views.reservation, name='reservation'),
    path('cadastrar-reserva', views.create_reserva, name='create_reserva'),
    path('atualizar-reserva/<int:pk>/', views.update_reserva, name='update_reserva'),
    path('deletar-reserva/<int:pk>/', views.delete_reserva, name='delete_reserva'),
]
