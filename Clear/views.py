from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, CreateView
from Clear.forms import RegisterForm
from Clear.models import AppUser, UserInhaler



from django.urls import reverse_lazy

from ClearWeb.settings import AUTH_USER_MODEL


# Create your views here.
class RegisterView(CreateView):
    # Create view for register page
    model = AUTH_USER_MODEL
    form_class = RegisterForm
    template_name = 'clear/registration/register.html'
    success_url = reverse_lazy('login')


# TODO @Libby -  Finish the code for this view section - need to change the tempalte view
class InhalerView(ListView):
    model = UserInhaler
    template_name = 'clear/main/inhaler.html'


# TODO @Cassy + Kareena - Finish the code for this view sectio n- need to change the tempalte view
class PollutionView(TemplateView):
    template_name = 'clear/main/pollution.html'


# TODO @Anna -  Finish the code for this view section - need to change the tempalte view
class SettingsView(TemplateView):
    template_name = 'clear/main/settings.html'



