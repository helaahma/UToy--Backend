from .models import Collectable, ProfileUser, BidOrder
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Collectable, ProfileUser, BidOrder

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    first_name = serializers.CharField(max_length=10, min_length=None, allow_blank=False)
    last_name = serializers.CharField(max_length=10, min_length=None, allow_blank=False)
    class Meta:
        model = User
        fields = ['username', 'password','email', 'first_name','last_name']

    def create(self, validated_data):

        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        new_user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class CollectableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collectable
        exclude= ['owner']


# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         exclude= ['user']
    





