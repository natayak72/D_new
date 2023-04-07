# Create your views here.

from django.views.generic import TemplateView, CreateView
from django.contrib.auth.models import User
from .forms import BaseRegistrationForm


class LoginView(TemplateView):
    template_name = 'sign/login.html'


class BaseRegisterView(CreateView):
    # модель формы, которую реализует данный дженерик;
    model = User
    form_class = BaseRegistrationForm
    success_url = '/news'

