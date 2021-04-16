from .models import HFControl

def getData(request):
    hfcontrol = HFControl.objects.latest('id')
    return {'hfcontrol': hfcontrol}