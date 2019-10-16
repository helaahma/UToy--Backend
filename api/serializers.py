from .models import Collectable, ProfileUser, BidOrder
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Collectable, ProfileUser, BidOrder

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    first_name = serializers.CharField(max_length=10, min_length=None, allow_blank=False)
    last_name = serializers.CharField(max_length=10, min_length=None, allow_blank=False)
    address = serializers.CharField(max_length=250)
    
    class Meta:
        model = User
        fields = ['username', 'password','email', 'first_name','last_name','address']

    def create(self, validated_data):

        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        new_user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        new_user.set_password(password)
        new_user.save()
        address = validated_data['address']
        ProfileUser.objects.create(user=new_user, address=address)
        return validated_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email', 'first_name','last_name','last_login','date_joined']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # we did use the ProfileUser Model as we are required to refer to the specific fields within that assigned model. 
    # Therefore, we utilized the above (UserSerializer) because of the existence of the needed fields
    class Meta:
        model = ProfileUser
        fields = ['user','address']


class ProfileUpdateSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()
    class Meta:
        model = ProfileUser
        fields = ['address','user','email']


class CollectableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collectable
        exclude = ['owner']


class OnGoingBidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidOrder
        fields= ['id','collectable', 'price', 'time']


class CollectableDetailSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    bid_order= serializers.SerializerMethodField()
    class Meta:
        model = Collectable
        fields=['id', 'bid_order','item', 'group', 'description', 'image', 'condition', 'special_features', 'desired_price', 'available','owner']
    def get_bid_order(self, obj):
        bid_order= BidOrder.objects.filter(collectable=obj)
        return OnGoingBidsSerializer(bid_order, many=True).data


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidOrder
        fields= ['price']

    




