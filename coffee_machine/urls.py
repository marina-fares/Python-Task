from django.urls import path, include
from . import views

app_name='coffee_machine'

urlpatterns = [
    path('', views.home, name='home'),
]