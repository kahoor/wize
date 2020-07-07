from django.urls import path

from .views import (OrganizationView, UpgradeRequestDetailView,
                    UpgradeRequestView)

app_name = 'organization'

urlpatterns = [
	path('', OrganizationView.as_view(), name="organizationapi"),
	path('upgraderequest/', UpgradeRequestView.as_view(), name="upgraderequestapi"),
	path('upgraderequest/<int:pk>/', UpgradeRequestDetailView.as_view(), name="upgraderequestdetailapi")
]
