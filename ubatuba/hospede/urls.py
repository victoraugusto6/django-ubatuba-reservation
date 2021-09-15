from django.urls import path
from ubatuba.hospede import views

app_name = 'hospede'
urlpatterns = [
    path('', views.hospedes, name='hospedes'),
    path('cadastrar-hospede', views.create_hospedes, name='create_hospedes'),
    path('atualizar-hospede/<int:pk>/', views.update_hospede, name='update_hospede'),
    path('deletar-hospede/<int:pk>/', views.delete_hospede, name='delete_hospede'),
]
