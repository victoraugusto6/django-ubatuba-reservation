from django.urls import path
from ubatuba.base import views

app_name = 'base'
urlpatterns = [
    path('', views.home, name='home'),
]
