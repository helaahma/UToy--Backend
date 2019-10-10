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
    image = models.ImageField(null=True, blank=True, upload_to="pics/")
    #condition for box
    conditions= [('new','new'),('used','used')]
    condition = models.CharField(max_length=4, choices=conditions, blank=False, default='new')
    # color=
    special_features = models.CharField(max_length=500, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="collectables")
    desired_price = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.item
    

class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    address = models.TextField(max_length=250, blank=False)  
    def __str__(self):
        return self.user


class BidOrder(models.Model):
    collectable = models.ForeignKey(Collectable,on_delete=models.CASCADE, related_name="bid_order")
    bidder = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user", null=True)
    price = models.IntegerField(null=True)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.collectable)


# 