from django.shortcuts import render
from .models import HFControl

# Create your views here.

def control(request, slug):
    hfcontrol = HFControl.objects.all().order_by('-id')
    data = {
        'hfcontrol': hfcontrol,
    }
    return render(request, 'base.html', data)