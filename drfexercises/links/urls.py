from django.urls import path

from links import views

urlpatterns = [
    path('', views.FavouriteLinksView.as_view(), name='favourite'),
    path('function_based', views.favourite_links_view, name='favourite_function')
]