from django.urls import path
from ubatuba.hospede import views

app_name = 'hospede'
urlpatterns = [
    path('', views.hospede, name='hospede'),
    path('hospedes', views.create_hospedes, name='hospedes'),
]
