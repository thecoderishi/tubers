from django.shortcuts import render

from .models import Slider, Team
from youtubers.models import Youtuber
from django.shortcuts import get_object_or_404
from hfcontrol.models import HFControl


# Create your views here.
def home(request):
    hfcontrol = HFControl.objects.all()
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_youtubers = Youtuber.objects.order_by('-created_date')
    data = {
        'hfcontrol': hfcontrol,
        'sliders': sliders,
        'teams': teams,
        'featured_youtubers': featured_youtubers,
        'all_youtubers':all_youtubers
    }
    return render(request, 'webpages/home.html', data)

def about(request):

    teams = Team.objects.all()

    data = {
        'teams': teams
    }
    return render(request, 'webpages/about.html', data)

def contact(request):
    return render(request, 'webpages/contact.html')

def services(request):
    return render(request, 'webpages/services.html')
