from django.shortcuts import render
from django.contrib.auth import login, get_user_model

from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .forms import MyUserCreationForm


# Create your views here.


class DashboardView(TemplateView):
    template_name = "usermanagement/dashboard.html"


class RegisterFormView(FormView):
    template_name = 'usermanagement/register.html'
    form_class = MyUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = form.save()
            login(request, user)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
