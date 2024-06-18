from django.urls import path
from personas.views import (
    personaTextView,
    personaCreateView,
    searchForHelp,
    personasAnotherCreateView,
    personasShowObject,
    personasListView,
    personasDeleteView
)

app_name = 'personas'
urlpatterns = [
    path('search/', searchForHelp, name='buscar'),
    path('persona/', personaTextView, name='otro'),
    path('add/', personaCreateView, name='adding'),
    path('anotherAdd', personasAnotherCreateView, name='OtroAgregarPersonas'),
    path('<int:myID>/', personasShowObject, name = 'browsing'),
    path('', personasListView, name = 'listing'),
    path('<int:myID>/delete/', personasDeleteView, name = 'deleting'),
]