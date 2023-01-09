"""ClearWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .forms import LoginForm

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('password_reset', auth_views.PasswordChangeView.as_view(), name='password_reset'),

    path('inhalers/', views.UserInhalerView.as_view(), name='inhalers'),
    path('inhaler/log_puff/<int:user_inhaler_id>', views.logInhalerPuff, name='inhaler_log_puff'),
    path('pollution/', views.PollutionView.as_view(), name='pollution'),

    # TODO FIX
    path('pollution/set_current_location/<int:app_user_id>', views.logCurrentLocation, name='pollution_log_location'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('add_inhaler/', views.add_inhaler, name='add_inhaler'),
    path('delete_inhaler/<int:id>/',views.delete_inhaler,name="delete_inhaler")
    # TODO Everyone add their views like above
    # https://docs.djangoproject.com/en/4.1/topics/class-based-views/intro/
]
