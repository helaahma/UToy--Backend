
from django.shortcuts import render
from .models import Collectable, ProfileUser, BidOrder
from .serializers import OnGoingBidsSerializer, BidSerializer, BidUpdateSerializer, CollectableSerializer, UserCreateSerializer
from rest_framework.generics import (RetrieveUpdateAPIView,ListAPIView, RetrieveAPIView,CreateAPIView, DestroyAPIView)
from rest_framework.views import APIView
from rest_framework.filters import (SearchFilter, OrderingFilter,)
from .models import Collectable, ProfileUser, BidOrder
from rest_framework.permissions import (IsAuthenticated, AllowAny, IsAdminUser,)
from rest_framework.response import Response
from django.http import Http404
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import status
from .permissions import IsOwner


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class CollectableList(ListAPIView):
    queryset= Collectable.objects.filter(available=True)
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


class DeleteCollectable(DestroyAPIView):
    queryset= Collectable.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'collectable_id'
    permission_classes = [IsAdminUser]


class CreateSellRequest(CreateAPIView):
    serializer_class = CollectableSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RequestUpdateView(RetrieveUpdateAPIView):
    queryset = Collectable.objects.all()
    serializer_class = CollectableSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'sellrequest_id'


class DeleteSellRequest(DestroyAPIView):
    queryset = Collectable.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'watch_id'
    permission_classes = [IsAdminUser]


class OnGoingBidsList(ListAPIView):
    queryset = BidOrder.objects.filter(status=True)
    serializer_class = OnGoingBidsSerializer
    permission_classes = [IsAuthenticated]


class OnGoingBidDetail(RetrieveAPIView):
    queryset = BidOrder.objects.all()
    serializer_class = OnGoingBidsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'bid_id'


class BidCreateView(CreateAPIView):
    serializer_class = BidSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        bid=serializer.save(bid_item=Collectable.objects.get(id=self.kwargs['collectable_id']))
        bid.save()
        print(bid)
        
        
class BidUpdateView(RetrieveUpdateAPIView):
    queryset = BidOrder.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'bid_id'
    serializer_class = BidUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwner]



