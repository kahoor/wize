from django.urls import path
from accounts.api.views import Registeration

app_name = 'account'

urlpatterns = [
	path('register', Registeration.as_view(), name="register"),
]