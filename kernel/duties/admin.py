from django.contrib import admin
from .models import Duty

@admin.register(Duty)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    