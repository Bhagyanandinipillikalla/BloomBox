from django.contrib import admin
from .models import *

# Register your models here.
class PlantAdmin(admin.ModelAdmin):
    model=Plant
    list_display=['name','category','price','image','discount_percent','Choice']


admin.site.register(Plant,PlantAdmin)