from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    myContext = {
        'mytext' : 'Esto es sobre nosotros',
        'myNumber' : 123,
        'myList' : [33, 44, 55]
    }
    return render(request, "home.html", myContext)

def anotherView(*args, **kwargs):
    return HttpResponse('<h1>Sólo es otra página</h1>')