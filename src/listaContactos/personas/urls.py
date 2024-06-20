from django.urls import path
from .views import (
    personaTextView,
    personaCreateView,
    searchForHelp,
    personasAnotherCreateView,
    personasShowObject,
    personasListView,
    personasDeleteView,
    PersonaListView,
)

app_name = 'personas'
urlpatterns = [
    path('', PersonaListView.as_view(), name = 'persona-list'),
    path('search/', searchForHelp, name='buscar'),
    path('persona/', personaTextView, name='otro'),
    path('add/', personaCreateView, name='adding'),
    path('anotherAdd', personasAnotherCreateView, name='OtroAgregarPersonas'),
    path('<int:myID>/', personasShowObject, name = 'browsing'),
    path('', personasListView, name = 'listing'),
    path('<int:myID>/delete/', personasDeleteView, name = 'deleting'),
]