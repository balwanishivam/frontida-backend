from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
from rest_framework.decorators import  permission_classes
from rest_framework.response import Response
from rest_framework import status


class UserDetailCreate(CreateAPIView):
    permission_classes = [AllowAny]
    model=UserDetail
    serializer_class = UserDetailSerializers

class UserDetailsGet(ListAPIView):
    permission_classes = [IsAuthenticated]
    model=UserDetail
    serializer_class = UserDetailSerializers
    def get_queryset(self):
        user = self.request.user
        return UserDetail.objects.filter(email=user.email)


    


