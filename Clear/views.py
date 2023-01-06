
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, CreateView
from Clear.forms import RegisterForm, SettingsForm
from Clear.models import AppUser, UserInhaler ,Inhaler
from django.shortcuts import get_object_or_404
# from django.views import View
from django.views.generic import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.contrib import messages

from ClearWeb.settings import AUTH_USER_MODEL

# Create your views here.
class RegisterView(CreateView):
    # Create view for register page
    model = AUTH_USER_MODEL
    form_class = RegisterForm
    template_name = 'clear/registration/register.html'
    success_url = reverse_lazy('login')


# TODO @Libby -  Finish the code for this view section - need to change the tempalte view
class UserInhalerView(ListView):
    model = UserInhaler
    template_name = 'clear/main/inhaler.html'


# TODO @Cassy + Kareena - Finish the code for this view section- need to change the tempalte view
class PollutionView(TemplateView):
    template_name = 'clear/main/pollution.html'


# TODO @Anna -  Finish the code for this view section - need to change the tempalte view
class SettingsView(LoginRequiredMixin, UpdateView):
    template_name = 'clear/main/settings.html'
    user_form = SettingsForm

    def get(self, request):
        user = get_object_or_404(AppUser, id = request.user.id)
        inhalers = UserInhaler.objects.filter(user = request.user)
        user_form = self.user_form(instance = user)
        return render(request, self.template_name, context= {"form":user_form,"inhalers":inhalers})

    def post(self,request):
        user = get_object_or_404(AppUser, id = request.user.id)
        form_class = SettingsForm(request.POST,instance = user)
        if form_class.is_valid():
            form_class.save()
            inhaler_id = request.POST.getlist('inhaler_id')
            inhaler_type = request.POST.getlist('inhaler_type')
            puff_remaining = request.POST.getlist('puff_remaining')
            puffs = request.POST.getlist('puffs')
            per_day = request.POST.getlist('per_day')
            if inhaler_type and puff_remaining and puffs and per_day:
                all_user_inhalers=[ {'inahler_id':inahler_id,"type":type,"puff_remaining":puff_remaining,"puffs":puffs,"per_day":per_day} for inahler_id,type,puff_remaining,puffs,per_day in zip(inhaler_id,inhaler_type,puff_remaining,puffs,per_day)]
                for i in all_user_inhalers:
                    obj = get_object_or_404(UserInhaler,id = i['inhaler_id'])
                    obj.inhaler_type    = i['type']
                    obj.per_Day         = i['per_day']
                    obj.puffs_remaining = i['puff_remaining']
                    obj.puffs           = i['puffs']
                    obj.save()
                messages.warning(request,'User settings has been updated successfully')
                return redirect('settings')

        else:
            messages.error(request,'Please fill in all required fields')
            return redirect('settings')


def add_inhaler(request):
    user = request.user
    inhaler_type = request.POST.get('inhaler_type')
    puff_remaining = request.POST.get('puff_remaining')
    puffs = request.POST.get('puffs')
    per_day = request.POST.get('per_day')
    if inhaler_type and puff_remaining and puffs and per_day:
        obj = UserInhaler.objects.create(
            user = user,
            inhaler_type = inhaler_type,
            puffs_remaining = puff_remaining,
            puffs = puffs,
            per_Day = per_day
        )
        obj.save()
        messages.success(request,'Inahler has been added successfully')
        return redirect('settings')
    else:
        messages.error(request,'Please fill in all required fields')
        return redirect('settings')

def logInhalerPuff(request, user_inhaler_id):
    # you should update you model field here
    UserInhaler.log_puff(user_inhaler_id)
    return redirect(reverse_lazy('inhalers'))

# TODO FIX
def logCurrentLocation(request, app_user_id):
    # you should update you model field here
    AppUser.set_new_current_location(app_user_id)
    return redirect(reverse_lazy('pollution'))