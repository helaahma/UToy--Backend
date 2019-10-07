
from django.shortcuts import render
from .models import Collectable, ProfileUser, BidOrder
from .serializers import CollectableSerializer, UserCreateSerializer
from rest_framework.generics import (RetrieveUpdateAPIView,ListAPIView, RetrieveAPIView,CreateAPIView, DestroyAPIView)
from rest_framework.views import APIView
from rest_framework.filters import (SearchFilter, OrderingFilter,)
from .models import Collectable, ProfileUser, BidOrder
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.http import Http404
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import status


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


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


class CreateSellRequest(CreateAPIView):
    serializer_class = CollectableSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user).data


class RequestUpdateView(RetrieveUpdateAPIView):
    queryset = Collectable.objects.all()
    serializer_class = CollectableSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'sellrequest_id'



#CART
# class Cart(RetrieveAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CollectableSerializer
#     #should it be IsOwner
#     permission_classes = [IsAuthenticated]
#     lookup_field='id'
#     lookup_url_kwarg='cart_id'

#     def get_queryset(self):
#         return Cart.objects.filter(user=self.request.user)


# class CreateCart(APIView):
#     serializer_class = CartSerializer
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         collectable = Collectable.objects.get(id=kwargs.get('collectable_id'))

#         if (self.request.user.carts.filter(status=False)):
#             cart = Cart.objects.get(user=self.request.user, status= False)
#             if not cart.collectable.get(id=cart.id):
#                 cart.collectable.push(cart)
#                 cart.save()
#         else:
#             cart = Cart(user=self.request.user)
#             cart.save()
#             cart.carts.push(cart)
#             cart.save()
#         response = CartSerializer(CollectableSerializer).data
#         response['collectable'] = CollectableSerializer(cart).data
#         return Response(response)


# class CartUpdate(RetrieveUpdateAPIView):
#     queryset = Cart.objects.all() 
#     serializer_class = CartSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'cart_id'
#     permission_classes = [IsAuthenticated]


# class CartItemDelete(DestroyAPIView):
#     queryset = Cart.objects.all()
#     lookup_field = 'id'
#     lookup_url_kwarg = 'cart_id'
#     permission_classes = [IsAuthenticated, IsCartOwner]

#     def delete(self, request, *args, **kwargs):
#         cart = self.get_object()
#         cart = Cart.objects.filter(user=self.request.user, status=True)
#         cart[0].cart.remove(cart)
#         return Response({"status" : 200})


# class Checkout (APIView):
#     serializer_class= CartSerializer
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         cart = Cart.objects.get(user=self.request.user, status=False)
#         serializer = CheckoutSerializer(cart)
#         for collectable in cart.cart.all():
#                 collectable.availability = False
#                 collectable.user=self.request.user
#                 collectable.save()
#         cart.status=True
#         cart.save()
#         return Response(serializer.data)



