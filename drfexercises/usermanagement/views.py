from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
# Create your views here.


class RegisterFormView(FormView):
    template_name = 'usermanagement/register.html'
    form_class = UserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = form.save()
            login(request, user)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
