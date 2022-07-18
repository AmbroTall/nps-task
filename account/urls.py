from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import(
	registration_view,
	ObtainAuthTokenView,
	account_properties_view,
	update_account_view,
	does_account_exist_view,
	ChangePasswordView,
	UserListView,
	user_api_view_delete,
	account_info,
	LoginViewFront,
	# RegisterView
)
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
	path('check_if_account_exists/', does_account_exist_view, name="check_if_account_exists"),
	path('change_password/', ChangePasswordView.as_view(), name="change_password"),
	path('properties/', account_properties_view, name="properties"),
	path('properties/update/', update_account_view, name="update"),
	path('account/', account_info, name="account_information"),
 	# path('login/', ObtainAuthTokenView.as_view(), name="login"),
 	path('login/', obtain_auth_token, name="login"),
	path('register/', registration_view, name="register"),
	path('all-users/', UserListView.as_view(), name="all_users"),
	path('delete_user/<int:pk>/', user_api_view_delete, name="delete_user"),

	path('nps/login/', LoginViewFront.as_view(), name='loginnps'),
	# path('nps/logout/', LogoutView.as_view(next_page='account:loginnps'), name='logout'),
	# path('nps/register/', RegisterView.as_view(), name='registernpss'),
]