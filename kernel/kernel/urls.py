from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/accounts/', include('accounts.api.urls')),
    path('api/organization/', include('organization.api.urls')),
    path('api/duties/', include('duties.api.urls')),
]
