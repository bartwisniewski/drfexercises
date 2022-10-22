from datetime import datetime
from django.contrib.auth import login, get_user_model

from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .forms import MyUserCreationForm
from .models import LoginHistory

# Create your views here.

User = get_user_model()


def get_last_login(user: User) -> datetime:
    try:
        return LoginHistory.objects.filter(user=user, successful=False).order_by('-timestamp')[0].timestamp
    except IndexError:
        return None


class DashboardView(TemplateView):
    template_name = "usermanagement/dashboard.html"

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        context['joined'] = request.user.date_joined.strftime('%m/%d/%Y')
        context['last_failed_login'] = get_last_login(request.user).strftime('%m/%d/%Y, %H:%M:%S')

        return self.render_to_response(context)


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
