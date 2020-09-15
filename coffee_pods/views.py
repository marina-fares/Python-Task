from django.shortcuts import render
from .models import Pods
from .filter import PodFilter

# Create your views here.

def coffee_pod(request):
    pods = Pods.objects.all()

    myfilter = PodFilter(request.GET, queryset=pods)
    pod_list = myfilter.qs

    context = {
        'pod_list': pod_list,
        'myfilter': myfilter
    }
    return render(request, 'pod.html', context)