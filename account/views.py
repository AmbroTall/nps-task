from django.shortcuts import render,redirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import RegisterForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializer import RegistrationSerializer, AccountPropertiesSerializer, ChangePasswordSerializer, AccountProperties
from .models import Account


class LoginViewFront(LoginView):
    fields = '__all__'
    template_name = 'account/login_page.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('nps:admin_page')
        # return reverse_lazy(redirect(f"http://127.0.0.1:8000/nps-scale/NpsScale2022-07-07"))
#
# class RegisterView(FormView):
#     form_class = RegisterForm
#     template_name = 'account/register_page.html'
#     redirect_authenticated_user = True
#     success_url = reverse_lazy('updates:homepage')
#
#
#     def form_valid(self, form):
#         user = form.save()
#         if user is not None:
#             login(self.request, user)
#         return super(RegisterView, self).form_valid(form)
#
#
#     def get(self, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return redirect('nps:homepage')
#         return super(RegisterView,self).get(*args, **kwargs)


@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
def account_info(request):
	try:
		account = request.user
	except Account.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = AccountProperties(account)
		return Response(serializer.data)