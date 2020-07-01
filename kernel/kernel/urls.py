from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/accounts/', include('accounts.api.urls')),
    path('api/organization/', include('organization.api.urls')),
]
