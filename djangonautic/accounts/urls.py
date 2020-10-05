from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomAuthForm

app_name = 'accounts'

urlpatterns = [
 path('signup',views.signup_view,name="signup"),
 path('login/',views.login_view,name="login"),
 path('logout',views.logout_view,name="logout"),
 path('',views.login_view,name="login"),


]
