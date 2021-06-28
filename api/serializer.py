from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','email','name','password')
        extra_kwargs={
            'password':{
                'write_only': True,
                'style':{'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user=UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user