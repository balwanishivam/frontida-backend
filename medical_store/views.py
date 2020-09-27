from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from medical_store.models import MedicineInventory, CompanyDetails, Purchase, PurchaseInventory, Sales, SalesInventory
from medical_store.serializers import MedicineInventorySerializers, CompanyDetailsSerializers, PurchaseSerializers, PurchaseInventorySerializers, SalesSerializers, SalesInventorySerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

class MedicineInventoryViewSets(ModelViewSet):
    serializer_class = MedicineInventorySerializers
    queryset = MedicineInventory.objects.all()

class CompanyDetailsViewSets(ModelViewSet):
    serializer_class = CompanyDetailsSerializers
    queryset = CompanyDetails.objects.all()

    def list(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes(IsAuthenticated)
    def create(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        if request.user.is_superuser:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'permission denied'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def retrieve(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            company = CompanyDetails.objects.get(pk=pk)
        except:
            return Response({'error': 'Company with given pk not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(company)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        if request.user.is_superuser:
            instance = self.get_object()
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            instance.company_name = serializer.data['company_name']
            instance.company_contact = serializer.data['company_contact'] 
            instance.company_address = serializer.data['company_address']
            instance.company_email = serializer.data['company_email']
            instance.gst_number = serializer.data['gst_number']
            instance.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'permission denied'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def partial_update(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        if request.user.is_superuser:
            instance = self.get_object()
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            instance.company_name = serializer.data['company_name']
            instance.company_contact = serializer.data['company_contact'] 
            instance.company_address = serializer.data['company_address']
            instance.company_email = serializer.data['company_email']
            instance.gst_number = serializer.data['gst_number']
            instance.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        if request.user.is_superuser:
            instance = self.get_object()
            serializer = self.serializer_class(data=instance)
            serializer.is_valid(raise_exception=True)
            instance.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)

