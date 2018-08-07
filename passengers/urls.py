from django.urls import path
from django.conf.urls import url

from flights import views as core_views

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
	url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		core_views.activate, name='activate'),
]