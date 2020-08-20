from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import  permission_classes
from rest_framework.response import Response
from rest_framework import status


class StoreDetailsCreate(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]
    model=StoreDetails
    serializer_class = StoreDetailsSerializers
    
    def post(self,request):
        serializer=StoreDetailsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(account=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicineInventoryCreate(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]
    model=StoreDetails
    serializer_class = MedicineSerializers
    def post(self,request):
        serializer=MedicineSerializers(data=request.data)
        if serializer.is_valid():
            serializer.user=self.request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
