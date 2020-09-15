from django.shortcuts import render
from .models import Machine
from .filters import MachineFilter

def home(request):
    machines = Machine.objects.all()

    myfilter = MachineFilter(request.GET, queryset=machines)
    machine_list = myfilter.qs

    context = {
        'machines':myfilter,
        'machine_list':machine_list
    }
    return render(request, 'home.html', context)