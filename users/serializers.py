from rest_framework import serializers
from django.db import models
from models import CustomUser

class UserSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = '__all__'




