from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from medical_store.models import MedicineInventory, CompanyDetails, Purchase, PurchaseInventory, Sales, SalesInventory
from medical_store.serializers import MedicineInventorySerializers, CompanyDetailsSerializers, PurchaseSerializers, PurchaseInventorySerializers, SalesSerializers, SalesInventorySerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action

class CompanyDetailsViewSets(ModelViewSet):
    serializer_class = CompanyDetailsSerializers
    queryset = CompanyDetails.objects.all()
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]


    def list(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# def list(self, request):
#         queryset = CompanyDetails.objects.all()
#         serializer = CompanyDetailsSerializers(queryset, many=True)
#         user_data=serializer.data
#         company_name=user_data['company_name']
#         return Response({'company_name':company_name},status=status.HTTP_200_OK)
    
    def create(self, request):
        print(request.user)
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        if request.user.is_superuser:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'Comanay Details': serializer.data}, status=status.HTTP_200_OK)
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
        else:
            return Response({'error': 'permission denied'}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        if request.user.is_superuser:
            instance = self.get_object()
            serializer = self.serializer_class(data=instance)
            serializer.is_valid(raise_exception=True)
            instance.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)



# class MedicineInventoryCreate(APIView):
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     model=StoreDetails
#     serializer_class = MedicineInventorySerializers
#     # def get(self,request):

#     def post(self,request):
#         serializer=MedicineInventorySerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response({'error': 'permission denied'}, status=status.HTTP_401_UNAUTHORIZED)

class MedicineInventoryViewSets(viewsets.ViewSet):
    queryset = MedicineInventory.objects.all()
    serializer_class = MedicineInventorySerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = CompanyDetails.objects.all()
        serializer = CompanyDetailsSerializers(queryset, many=True)
        user_data=serializer.data
        company_name=user_data['company_name']
        return Response({'company_name':company_name},status=status.HTTP_200_OK)

    
    def create(self, request):
        print(request.user)
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        if request.user.is_superuser:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(account=request.user)
            return Response({'Comanay Details': serializer.data}, status=status.HTTP_200_OK)
            
    def retrieve(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            inventory = MedicineInventory.objects.get(medicine_name)
        except:
            return Response({'error': 'Medicine with given name not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(medicine)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        if request.user.is_superuser:
            instance = self.get_object()
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            instance.batch_number = serializer.data['batch_number']
            instance.medicine_name = serializer.data['medicine_name'] 
            # instance.company_name = serializer.data['company_name']
            instance.mfd = serializer.data['mfd']
            instance.expiry = serializer.data['expiry']
            instance.purchase_price = serializer.data['purchase_price']
            instance.sale_price = serializer.data['sale_price']
            instance.medicine_quantity = serializer.data['medicine_quantity']
            instance.save(account=request.user)
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
            instance.batch_number = serializer.data['batch_number']
            instance.medicine_name = serializer.data['medicine_name'] 
            # instance.company_name = serializer.data['company_name']
            instance.mfd = serializer.data['mfd']
            instance.expiry = serializer.data['expiry']
            instance.purchase_price = serializer.data['purchase_price']
            instance.sale_price = serializer.data['sale_price']
            instance.medicine_quantity = serializer.data['medicine_quantity']
            instance.save(account=request.user)
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

class PurchaseView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PurchaseSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        company = CompanyDetails.objects.get(company_name = "Sun Pharma")
        purchase = serializer.save(account = request.user, company_name = company)
        # serializer = PurchaseSerializers(purchase)
        return Response({'success: created'}, status=status.HTTP_201_CREATED)