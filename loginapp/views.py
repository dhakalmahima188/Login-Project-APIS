from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer


def Home(request):
    return HttpResponse("Hello People, Have a good day !!!")



class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Failed to create user'}, status=status.HTTP_400_BAD_REQUEST)

  
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=username, password=password, email=email)
        if user :
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def get(self,request):
        users = User.objects.all().values('username', 'password', 'email')
        return Response(users)