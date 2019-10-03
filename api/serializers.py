from .models import Collectable, ProfileUser, BidOrder
from django.contrib.auth.models import User
from rest_framework import serializers



class CollectableSerializer(serializers.ModelSerializer):
	class Meta:
		model = Collectable
		exclude= ['owner']

 