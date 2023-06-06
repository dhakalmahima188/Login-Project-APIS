from . import views
from django.urls import path
from .views import LoginView,RegisterView,EditProfileView
from rest_framework_simplejwt.views import TokenObtainPairView
   


urlpatterns = [
     path('', views.Home, name='Home'),
     path('api/login/', LoginView.as_view(), name='login'),
     path('api/register/', RegisterView.as_view(), name='register'),
     path('api/editprofile/', EditProfileView.as_view(), name='register'),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     ]