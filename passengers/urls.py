from django.urls import path
from django.conf.urls import url

from passengers import views as core_views

from .views import (
	PassengerList,
	PassengerDetailView,
	PassengerCreateView,
	PassengerDeleteView,
	PassengerUpdateView,
	signup_view,
)

urlpatterns = [
	path('list/', PassengerList.as_view(), name="passenger-list"),
	path('<int:pk>/detail/', PassengerDetailView.as_view(), name="passenger-detail"),
	path('create/', PassengerCreateView.as_view(), name="passenger-create"),
	path('delete/<int:pk>', PassengerDeleteView.as_view(), name="passenger-delete"),
	path('<int:pk>/update/', PassengerUpdateView.as_view(), name="passenger-update"),
]

urlpatterns += [
	path('signup/', signup_view, name="signup"),
]

urlpatterns += [
	path('account/activation/sent/', core_views.account_activation_sent, name="account_activation_sent"),
	path('accounts/activation/<uidb64>/<token>/', core_views.activate, name="activate"),
]