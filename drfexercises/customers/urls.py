from django.urls import path

from customers import views

urlpatterns = [
    path('', views.GenerateCustomerView.as_view(), name='customer'),
]