
from django.urls import path, include
from . import views

app_name='coffee_pods'

urlpatterns = [
    path('', views.coffee_pod, name='coffee_pod'),
]