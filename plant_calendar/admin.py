from django.contrib import admin
from .models import PlantCalendar, Plant

# Register your models here.
admin.site.register(PlantCalendar)
admin.site.register(Plant)