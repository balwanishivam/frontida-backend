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



class MedicineInventoryCreate(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]
    model=StoreDetails
    serializer_class = MedicineInventorySerializers
    # def get(self,request):

    def post(self,request):
        serializer=MedicineInventorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.user=self.request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
