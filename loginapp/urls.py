from . import views
from django.urls import path
from .views import LoginView,RegisterView

urlpatterns = [
     path('', views.Home, name='Home'),
     path('login/', LoginView.as_view(), name='login'),
     path('register/', RegisterView.as_view(), name='register')]