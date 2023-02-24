from django.contrib import admin
from .models import Pets


@admin.register(Pets)
class PetsAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'year_of_birth')
