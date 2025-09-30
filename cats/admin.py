from django.contrib import admin

from .models import Breed, SpyCat, Target, Mission

admin.site.register(Breed)
admin.site.register(SpyCat)
admin.site.register(Target)
admin.site.register(Mission)