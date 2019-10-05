from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


# Create your models here.
class Collectable(models.Model):
	
	item = models.CharField(max_length=60, blank=False)
	group = models.CharField(max_length=70, blank=False)
	description = models.TextField(max_length=500, blank=False)
	image = models.ImageField(null=False, blank=False)
	#condition for box
	condition = models.CharField(max_length=70, blank=True)
	# color=
	special_features = models.CharField(max_length=500, blank=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="collectables")
	desired_price = models.IntegerField(default=1)

	def __str__(self):
		return self.name
	

class ProfileUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
	address = models.TextField(max_length=250, blank=False)  
	# Each bid has many users
	# bid_order = models.Forginkey(BidOrder,on_delete=models.CASCADE, related_name="profiles")
	def __str__(self):
		return self.name

class BidOrder(models.Model):
	bid_item = models.OneToOneField(User,on_delete=models.CASCADE, related_name="bid_order")
	bidder = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user")
	filled_price = models.IntegerField()
	time = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)
	def __str__(self):
		return self.name


