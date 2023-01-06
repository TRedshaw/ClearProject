from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(AppUser, UserAdmin)
admin.site.register(UserLocations)
admin.site.register(Location)
admin.site.register(Inhaler)
admin.site.register(UserInhaler)
admin.site.register(PollutionLevels)
admin.site.register(PollutionLevelInfo)
admin.site.register(Inhalers)

# Register your models here.
