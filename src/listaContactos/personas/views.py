from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona
from .forms import PersonaForm, rawPersonaForm

# Create your views here.
def personasAnotherCreateView(request):
    form = rawPersonaForm()
    if request.method == "POST":
        form = rawPersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Persona.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        'form' : form,
    }
    return render(request, 'personas/personasCreate.html', context)


def personaTextView(request):
    obj = Persona.objects.get(id = 1)
    context = {
        'objeto' : obj,
    }
    return render(request, 'personas/descripcion.html', context)

def personaCreateView(request):
    initialValues = {
        'nombres' : 'Sin Nombre'
    }
    form = PersonaForm(request.POST or None, initial = initialValues)
    if form.is_valid():
        form.save()
        form = PersonaForm()

    context = {
            'form' : form 
        }
    return render(request, 'personas/personasCreate.html', context)

def searchForHelp(request):
    return render(request, 'personas/search.html', {})

def personasShowObject(request, myID):
    obj = get_object_or_404(Persona, id = myID)
    context = {
        'objeto' : obj
    }
    return render(request, 'personas/descripcion.html', context)

def personasListView(request):
    queryset = Persona.objects.all()
    context = {
        'objectList' : queryset,
    }
    return render(request, 'personas/personasList.html', context)

def personasDeleteView(request, myID):
    obj = get_object_or_404(Persona, id = myID)
    if request.method == 'POST':
        print('LO BORRO')
        obj.delete()
        return redirect('../')
    context ={
        'objeto' : obj,
    }
    return render(request, 'personas/personasBorrar.html', context)