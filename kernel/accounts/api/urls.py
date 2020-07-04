from django.urls import path
from accounts.api.views import Registeration, UserInfoDetailView

app_name = 'account'

urlpatterns = [
	path('register', Registeration.as_view(), name="register"),
	path('<int:pk>/', UserInfoDetailView.as_view(), name="userinfodetail")
]