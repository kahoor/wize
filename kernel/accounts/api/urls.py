from django.urls import path

from accounts.api.views import (Registeration, UserInfoDetailView,
                                UserInfoListView)

app_name = 'account'

urlpatterns = [
	path('register', Registeration.as_view(), name="register"),
	path('usersinfo', UserInfoListView.as_view(), name="userinfolist"),
	path('<int:pk>/', UserInfoDetailView.as_view(), name="userinfodetail"),
	
]
