from . import views
from django.urls import path
from .views import LoginView,RegisterView,EditProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
     path('', views.Home, name='Home'),
     path('api/login/', LoginView.as_view(), name='login'),
     path('api/register/', RegisterView.as_view(), name='register'),
     path('api/editprofile/', EditProfileView.as_view(), name='register'),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
    
     
     ]