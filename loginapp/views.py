from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer
from django.contrib.auth import update_session_auth_hash
from rest_framework.permissions import IsAuthenticated


def Home(request):
    return HttpResponse("Hello People, Have a good day !!!")


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # Check if the user already exists
        existing_user = User.objects.filter(username=username).first()
        if existing_user:
            return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)

        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Failed to create user'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        users = User.objects.all().values('username', 'password', 'email')
        return Response(users)


class EditProfileView(APIView):
    permission_classes = [IsAuthenticated]  # Add permission class to ensure the user is authenticated

    def post(self, request):
        user = request.user  # Access the logged-in user directly

        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        print(username,email,password)
        print(user.username,user.email,user.password)

        if password:
            # Check if the provided password is valid
            if not user.check_password(password):
                update_session_auth_hash(request, user)
                return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)

        if username:
            user.username = username
        if email:
            user.email = email
        if password:
            user.set_password(password)

        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
