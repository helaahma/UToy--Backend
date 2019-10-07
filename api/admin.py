from django.contrib import admin
from django.contrib import admin
from .models import  Collectable, ProfileUser, BidOrder

admin.site.register(Collectable)
admin.site.register(ProfileUser)
admin.site.register(BidOrder)
