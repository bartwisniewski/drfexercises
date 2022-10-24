from django.urls import path
from .views import ValvesListCreate, PumpsListCreate, ValvesRetrieveUpdateDestroy, PumpsRetrieveUpdateDestroy, DbFillView

urlpatterns = [
    path('db/', DbFillView.as_view(), name='api-db-fill'),
    path('valves/', ValvesListCreate.as_view(), name='api-valves'),
    path('valves/<int:pk>/', ValvesRetrieveUpdateDestroy.as_view(), name='api-valve'),
    path('pumps/', PumpsListCreate.as_view(), name='api-pumps'),
    path('pumps/<int:pk>/', PumpsRetrieveUpdateDestroy.as_view(), name='api-pump'),
]
