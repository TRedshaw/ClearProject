from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(UserLocations)
admin.site.register(Location)
admin.site.register(Inhaler)
admin.site.register(UserInhaler)
admin.site.register(PollutionLevels)
admin.site.register(PollutionLevelInfo)


# Register your models here.
