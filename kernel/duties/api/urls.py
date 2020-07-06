from django.urls import path
from .views import DutyView, DutyDetailView

app_name = 'duties'

urlpatterns = [
	path('', DutyView.as_view(), name="dutyapi"),
	path('<int:pk>/', DutyDetailView.as_view(), name="dutydetailapi")
]