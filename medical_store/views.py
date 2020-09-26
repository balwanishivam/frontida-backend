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
from rest_framework.authentication import TokenAuthentication


class MedicineInventoryCreate(APIView):
    authentication_classes = [TokenAuthentication]
    model=MedicineInventory
    serializer_class = MedicineInventory
    def get(self, request):
        print(request.user.id)
        queryset = CompanyDetails.objects.filter(account = request.user)
        return queryset

    # def post(self,request):
    #     serializer=MedicineInventory(data=request.data)
    #     if serializer.is_valid():
    #         serializer.user=self.request.user
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicineInventoryDelete(APIResponse):
    authentication_classes = [TokenAuthentication]
    model=MedicineInventory
    serializer_class = MedicineInventory

    def post(self, request):


class MedicineInventoryUpdate(APIView):
    authentication_classes = [TokenAuthentication]
    model=MedicineInventory
    serializer_class = MedicineInventory

    def post(self, request):


class MedicineInventoryView(APIView):
    authentication_classes = [TokenAuthentication]
    model=MedicineInventory
    serializer_class = MedicineInventory

    def get(self, request):