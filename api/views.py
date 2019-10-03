from django.shortcuts import render
from .models import Collectable, ProfileUser, BidOrder
from .serializers import CollectableSerializer
from rest_framework.generics import (RetrieveUpdateAPIView,ListAPIView, RetrieveAPIView,CreateAPIView, DestroyAPIView)
from rest_framework.views import APIView
from rest_framework.filters import (SearchFilter, OrderingFilter,)
from .models import Collectable, ProfileUser, BidOrder
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

# Create your views here.
class CollectableList(ListAPIView):
    queryset= Collectable.objects.all()
    serializer_class = CollectableSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['item', 'group', 'desired_price', 'special_features', 'condition', 'owner']


class CollectableDetails(RetrieveAPIView):
    queryset= Collectable.objects.all()
    serializer_class = CollectableSerializer
    permission_classes = [AllowAny]
    lookup_field='id'
    lookup_url_kwarg='collectable_id'






