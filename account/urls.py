from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import(
	account_info,
	Login,
	# RegisterView
)
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
	path('account/', account_info, name="account_information"),

	path('nps-admin/', Login, name='loginnps'),
	# path('nps/logout/', LogoutView.as_view(next_page='account:loginnps'), name='logout'),
	# path('nps/register/', RegisterView.as_view(), name='registernpss'),
]