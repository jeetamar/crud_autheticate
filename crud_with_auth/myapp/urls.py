from django.urls import path
# from .views import index,CustomerRegisView
from .views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordChangeForm
urlpatterns = [
    path('',index , name='home'),
    path('register/', CustomerRegisView.as_view(), name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=LoginForm),
         name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),

]