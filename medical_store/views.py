from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from medical_store.models import MedicineInventory, CompanyDetails, Purchase, PurchaseInventory, Sales, SalesInventory
from medical_store.serializers import MedicineInventorySerializers, CompanyDetailsSerializers, PurchaseSerializers, PurchaseInventorySerializers, SalesSerializers, SalesInventorySerializers

class MedicineInventoryViewSets(ModelViewSet):
    serializer_class = MedicineInventorySerializers
    queryset = MedicineInventory.objects.all()

class CompanyDetailsViewSets(ModelViewSet):
    serializer_class = CompanyDetailsSerializers
    queryset = CompanyDetails.objects.all()

    def list(self, request):
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        if request.user.is_superuser:
            super().update(self, request, pk=None)
        else:
            return Response({'error': 'permission denied'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def retrieve(self, request, pk=None):
        queryset = CompanyDetails.objects.filter(pk=pk)
        serializer = serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        if request.user.is_superuser:
            super().update(self, request, pk=None)
        else:
            return Response({'error': 'permission denied'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def partial_update(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        if request.user.is_superuser:
            super().partial_update(self, request, pk=None)

    def destroy(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        if request.user.is_superuser:
            super().destroy(self, request, pk=None)

