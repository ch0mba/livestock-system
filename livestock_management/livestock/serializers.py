from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Animal, HealthRecord, ProductivityRecord

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password') # Explicitly include only username and password
        write_only_fields = ('password',)

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        user.first_name = validated_data.get('first_name', '')
        user.last_name = validated_data.get('last_name', '')
        user.save()
        return user

class AnimalSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Animal
        fields = '__all__'
        read_only_fields = ('registration_date',)

class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = '__all__'
        read_only_fields = ('record_date',)

class ProductivityRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductivityRecord
        fields = '__all__'