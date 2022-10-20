from django.urls import path
from django.urls import include

from usermanagement import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('dashboard', views.DashboardView.as_view(), name="dashboard"),
    path('register', views.RegisterFormView.as_view(), name="register")
]