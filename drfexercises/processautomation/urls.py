from django.urls import path

from processautomation import views

urlpatterns = [
    path('valves', views.ValvesListView.as_view(), name='valves-list'),
    path('pumps', views.PumpsListView.as_view(), name='pumps-list')
]
