from django.contrib import admin

from .models import PersonalComputer


@admin.register(PersonalComputer)
class PersonalComputerAdmin(admin.ModelAdmin):
    list_display = ('id', 'gpu',)
