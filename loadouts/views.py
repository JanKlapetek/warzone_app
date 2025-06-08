from django.shortcuts import render
from .models import Loadout

def loadout_list(request):
    loadouts = Loadout.objects.all()
    return render(request, 'loadouts/index.html', {'loadouts': loadouts})