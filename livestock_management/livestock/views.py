from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .models import Animal, HealthRecord, ProductivityRecord
from .serializers import (
    UserSerializer,
    UserCreateSerializer,
    AnimalSerializer,
    HealthRecordSerializer,
    ProductivityRecordSerializer
)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id, 'username': user.username})
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Animal.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class HealthRecordViewSet(viewsets.ModelViewSet):
    serializer_class = HealthRecordSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return HealthRecord.objects.filter(animal__owner=self.request.user)

    def perform_create(self, serializer):
        animal_rfid = self.request.data.get('animal')
        try:
            animal = Animal.objects.get(rfid=animal_rfid, owner=self.request.user)
            serializer.save(animal=animal)
        except Animal.DoesNotExist:
            raise serializers.ValidationError("Animal with provided RFID does not exist or does not belong to the user.")

class ProductivityRecordViewSet(viewsets.ModelViewSet):
    serializer_class = ProductivityRecordSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ProductivityRecord.objects.filter(animal__owner=self.request.user)

    def perform_create(self, serializer):
        animal_rfid = self.request.data.get('animal')
        try:
            animal = Animal.objects.get(rfid=animal_rfid, owner=self.request.user)
            serializer.save(animal=animal)
        except Animal.DoesNotExist:
            raise serializers.ValidationError("Animal with provided RFID does not exist or does not belong to the user.")