from django.urls import path

from links import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]