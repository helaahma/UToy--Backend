from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


# 