from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm

# Create your views here.
def personaTextView(request):
    obj = Persona.objects.get(id = 1)
    context = {
        'objeto' : obj,
    }
    return render(request, 'personas/descripcion.html', context)

def personaCreateView(request):
    print('GET: ', request.GET)
    print('POST: ', request.POST)

def searchForHelp(request):
    return render(request, 'personas/search.html', {})