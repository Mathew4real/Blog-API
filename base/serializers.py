from rest_framework import serializers
from django.contrib.auth import get_user_model
from . models import *

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["email","username","first_name","last_name","last_name","password"]
        extra_kwargs = {
            "password" : {"write_only" : True,
            'min_length': 6
            }
        }
    
    def create(self, validated_data):
        email = validated_data["email"]
        username = validated_data["username"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        password = validated_data["password"]
        
        user = get_user_model()
        new_user = user.objects.create(first_name=first_name,last_name=last_name,username=username,email=email)

        new_user.set_password(password)
        new_user.save()
        return new_user
class BlogSerializer (serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        