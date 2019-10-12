
from django.shortcuts import render
from .models import Collectable, ProfileUser, BidOrder
from .serializers import CollectableDetailSerializer,OnGoingBidsSerializer, BidSerializer, CollectableSerializer, UserCreateSerializer
from rest_framework.generics import (RetrieveUpdateAPIView,ListAPIView, RetrieveAPIView,CreateAPIView, DestroyAPIView)
from rest_framework.views import APIView
from rest_framework.filters import (SearchFilter, OrderingFilter,)
from .models import Collectable, ProfileUser, BidOrder
from rest_framework.permissions import (IsAuthenticated, AllowAny, IsAdminUser,)
from rest_framework.response import Response
from django.http import Http404
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import status
from .permissions import IsOwner, IsNotOwner


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
    serializer_class = CollectableDetailSerializer
    permission_classes = [AllowAny]
    lookup_field='id'
    lookup_url_kwarg='collectable_id'


class DeleteCollectable(DestroyAPIView):
    queryset = Collectable.objects.filter(available=False)
    lookup_field = 'id'
    lookup_url_kwarg = 'collectable_id'
    permission_classes = [IsAdminUser, IsOwner]


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


class OnGoingBidsList(ListAPIView):
    queryset = BidOrder.objects.filter(collectable__available=True)
    serializer_class = OnGoingBidsSerializer
    permission_classes = [IsAuthenticated]


class OnGoingBidDetail(RetrieveAPIView):
    queryset = BidOrder.objects.all()
    serializer_class = OnGoingBidsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    lookup_url_kwarg = 'bid_id'


class BidView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, collectable_id):
        collectable = Collectable.objects.get(id=collectable_id)
        highest_bid = BidOrder.objects.filter(
            collectable=collectable, price__gt=request.data['price']
        ).exists()
        if not highest_bid:
            bid, _ = BidOrder.objects.get_or_create(bidder = self.request.user, collectable=collectable)
            bid.price = request.data['price']
            bid.save()   
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
        











