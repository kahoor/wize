from django.contrib import admin

from .models import Organization, UpgradeRequest

# Register your models here.

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(UpgradeRequest)
class UpgradeReauestAdmin(admin.ModelAdmin):
    list_display =  ('user', 'current_role', 'dream_role', 'organization', 'status')
