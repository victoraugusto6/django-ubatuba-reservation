from django.urls import path
from ubatuba.hospede import views

app_name = 'hospede'
urlpatterns = [
    path('', views.hospedes, name='hospedes'),
    path('hospedes', views.create_hospedes, name='create_hospedes'),
]
