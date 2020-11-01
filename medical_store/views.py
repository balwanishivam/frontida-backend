from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from medical_store.models import MedicineInventory, CompanyDetails, Purchase, PurchaseInventory, Sales, SalesInventory
from medical_store.serializers import MedicineInventorySerializers, CompanyDetailsSerializers, PurchaseSerializers, PurchaseInventorySerializers, SalesSerializers, SalesInventorySerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
import datetime
from collections import Counter

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

            if not serializer.is_valid():
                error_values = list(serializer.errors.values())
                error_keys = list(serializer.errors.keys())
                if len(error_keys) > 0 and len(error_values) > 0:
                    return Response({f'{error_keys[0]}': f'{error_values[0][0]}'})

            serializer.save()
            return Response({'Comanay Details': serializer.data}, status=status.HTTP_200_OK)
            
    def retrieve(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            company = CompanyDetails.objects.get(pk=pk)
        except ComapnyDetails.DoesNotExist as exp:
            return Response({'error': 'Company with given pk not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(company)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        if request.user.is_superuser:
            instance = self.get_object()
            serializer = self.serializer_class(data=request.data)
            
            if not serializer.is_valid():
                error_values = list(serializer.errors.values())
                error_keys = list(serializer.errors.keys())
                if len(error_keys) > 0 and len(error_values) > 0:
                    return Response({f'{error_keys[0]}': f'{error_values[0][0]}'})

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
            
            if not serializer.is_valid():
                error_values = list(serializer.errors.values())
                error_keys = list(serializer.errors.keys())
                if len(error_keys) > 0 and len(error_values) > 0:
                    return Response({f'{error_keys[0]}': f'{error_values[0][0]}'})
            
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



# # class MedicineInventoryCreate(APIView):
# #     authentication_classes = [authentication.TokenAuthentication]
# #     permission_classes = [IsAuthenticated]
# #     model=StoreDetails
# #     serializer_class = MedicineInventorySerializers
# #     # def get(self,request):

# #     def post(self,request):
# #         serializer=MedicineInventorySerializers(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data,status=status.HTTP_201_CREATED)
# #         else:
# #             return Response({'error': 'permission denied'}, status=status.HTTP_401_UNAUTHORIZED)

class MedicineInventoryViewSets(viewsets.ViewSet):
    queryset = MedicineInventory.objects.all()
    serializer_class = MedicineInventorySerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        medicine_inventory=MedicineInventory.objects.filter(account=request.user)
        serializer = MedicineInventorySerializers(medicine_inventory, many=True)
        medicine_intventory=serializer.data
        return Response({'medicine_inventory':medicine_intventory},status=status.HTTP_200_OK)

    
#     def create(self, request):
#         print(request.user)
#         if not request.user.is_authenticated:
#             return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
#         if request.user.is_superuser:
#             serializer = self.serializer_class(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save(account=request.user)
#             return Response({'Comanay Details': serializer.data}, status=status.HTTP_200_OK)
            
#     def retrieve(self, request, pk=None):
#         if not request.user.is_authenticated:
#             return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
#         try:
#             inventory = MedicineInventory.objects.get(medicine_name)
#         except:
#             return Response({'error': 'Medicine with given name not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = self.serializer_class(medicine)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, pk=None):
#         if not request.user.is_authenticated:
#             return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
#         if request.user.is_superuser:
#             instance = self.get_object()
#             serializer = self.serializer_class(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             instance.batch_number = serializer.data['batch_number']
#             instance.medicine_name = serializer.data['medicine_name'] 
#             # instance.company_name = serializer.data['company_name']
#             instance.mfd = serializer.data['mfd']
#             instance.expiry = serializer.data['expiry']
#             instance.purchase_price = serializer.data['purchase_price']
#             instance.sale_price = serializer.data['sale_price']
#             instance.medicine_quantity = serializer.data['medicine_quantity']
#             instance.save(account=request.user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'permission denied'}, status=status.HTTP_401_UNAUTHORIZED)
    
#     def create(self, request):
#         print(request.user)
#         if not request.user.is_authenticated:
#             return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
#         if request.user.is_superuser:
#             serializer = self.serializer_class(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save(account=request.user)
#             return Response({'Comanay Details': serializer.data}, status=status.HTTP_200_OK)
            
#     def retrieve(self, request, pk=None):
#         if not request.user.is_authenticated:
#             return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
#         try:
#             inventory = MedicineInventory.objects.get(medicine_name)
#         except:
#             return Response({'error': 'Medicine with given name not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = self.serializer_class(medicine)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, pk=None):
#         if not request.user.is_authenticated:
#             return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
#         if request.user.is_superuser:
#             instance = self.get_object()
#             serializer = self.serializer_class(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             instance.batch_number = serializer.data['batch_number']
#             instance.medicine_name = serializer.data['medicine_name'] 
#             # instance.company_name = serializer.data['company_name']
#             instance.mfd = serializer.data['mfd']
#             instance.expiry = serializer.data['expiry']
#             instance.purchase_price = serializer.data['purchase_price']
#             instance.sale_price = serializer.data['sale_price']
#             instance.medicine_quantity = serializer.data['medicine_quantity']
#             instance.save(account=request.user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'permission denied'}, status=status.HTTP_401_UNAUTHORIZED)
    
#     def partial_update(self, request, pk=None):
#         if not request.user.is_authenticated:
#             return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
#         if request.user.is_superuser:
#             instance = self.get_object()
#             serializer = self.serializer_class(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             instance.batch_number = serializer.data['batch_number']
#             instance.medicine_name = serializer.data['medicine_name'] 
#             # instance.company_name = serializer.data['company_name']
#             instance.mfd = serializer.data['mfd']
#             instance.expiry = serializer.data['expiry']
#             instance.purchase_price = serializer.data['purchase_price']
#             instance.sale_price = serializer.data['sale_price']
#             instance.medicine_quantity = serializer.data['medicine_quantity']
#             instance.save(account=request.user)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#     def destroy(self, request, pk=None):
#         if not request.user.is_authenticated:
#             return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
#         if request.user.is_superuser:
#             instance = self.get_object()
#             serializer = self.serializer_class(data=instance)
#             serializer.is_valid(raise_exception=True)
#             instance.delete()
#             return Response(serializer.data, status=status.HTTP_200_OK)

class PurchaseViewSets(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    def list(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        purchases = Purchase.objects.filter(account = request.user)
        company_name=[company.company_name for company in CompanyDetails.objects.all()]
        serializer = self.serializer_class(purchases, many=True)
        responsedata = {'previousbills': serializer.data, 
                        'companynames': company_name}
        return Response(responsedata, status=status.HTTP_200_OK)

    def create(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            error_values = list(serializer.errors.values())
            error_keys = list(serializer.errors.keys())
            if len(error_keys) > 0 and len(error_values) > 0:
                return Response({f'{error_keys[0]}': f'{error_values[0][0]}'})
        try:
            company = CompanyDetails.objects.get(company_name=serializer.validated_data.get('company_name'))
        except CompanyDetails.DoesNotExist as exp:
            return Response({'error': 'Invalid company name'}, status=status.HTTP_200_OK)
        purchase = serializer.save(account=request.user, company_name=company)
        purchase_inventory = purchase.purchaseinventory.all()
        for entry in purchase_inventory:
            try:
                med_inventory = MedicineInventory.objects.get(medicine_name=entry.medicine_name, batch_number=entry.batch_number)
                med_inventory.medicine_quantity += entry.quantity
                med_inventory.save()
            except MedicineInventory.DoesNotExist as identifier:
                med_inventory = MedicineInventory(medicine_name=entry.medicine_name, batch_number=entry.batch_number, company_name=company,
                                                  mfd=entry.mfd, expiry=entry.expiry ,purchase_price=entry.price_of_each, sale_price=entry.mrp,
                                                  medicine_quantity=entry.quantity, account=request.user)
                med_inventory.save()
        serializer = PurchaseSerializers(instance = purchase)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    def retrieve(self, request, pk=None):
        try:
            purchase = Purchase.objects.get(pk=pk)
            serializer = self.serializer_class(purchase)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Purchase.DoesNotExist as exp:
            return Response({'doesNotExist':'does not exist in database'}, status=status.HTTP_404_NOT_FOUND)
    
class SalesViewSets(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def list(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged in'}, status=status.HTTP_401_UNAUTHORIZED)

        sales = Sales.objects.filter(account=request.user)
        medicine_name = [medicine.medicine_name for medicine in MedicineInventory.objects.filter(account=request.user)]
        medicine_name = list(set(medicine_name))
        if len(sales) == 0:
            return Response({'empty': 'no records as of now'}, status=status.HTTP_200_OK)
            
        serializer = self.serializer_class(sales, many=True)
        responsedata = {'previoussales': serializer.data,
                        'medicine_name': medicine_name }
        return Response(responsedata, status=status.HTTP_200_OK)
            
    def create(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged in'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            error_values = list(serializer.errors.values())
            error_keys = list(serializer.errors.keys())
            if len(error_keys) > 0 and len(error_values) > 0:
                return Response({f'{error_keys[0]}': f'{error_values[0][0]}'})         

        for entry in serializer.validated_data.get('salesinventory'):
            medicine_name = entry.get('medicine_name')
            required_quantity = entry.get('quantity')
            med_inventory = list(MedicineInventory.objects.filter(medicine_name=medicine_name).order_by('sale_price'))
            if len(med_inventory) == 0:
                return Response({'medicine': 'not found'}, status=status.HTTP_400_BAD_REQUEST)
            available_stock = 0
            for medicine in med_inventory:
                if (medicine.expiry - datetime.date.today()) < datetime.timedelta(days=90):
                    medicine.isexpired = True
                    med_inventory.remove(medicine)
                    medicine.save()
                else:
                    available_stock += medicine.medicine_quantity

            if required_quantity > available_stock:
                return Response({'medicine': 'not enough stock'}, status=status.HTTP_400_BAD_REQUEST)

            for medicine in med_inventory:
                if required_quantity <= medicine.medicine_quantity:
                    medicine.medicine_quantity -= required_quantity
                    medicine.save()
                    break
                else:
                    required_quantity -= medicine.medicine_quantity
                    medicine.delete()
        
        sales = serializer.save(account=request.user)
        serializer = SalesSerializers(instance=sales)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            sales = Sales.objects.get(pk=pk)
            serializer = self.serializer_class(sales)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Sales.DoesNotExist as exp:
            return Response({'doesNotExist':'does not exist in database'}, status=status.HTTP_404_NOT_FOUND)
                


        
        
    
#     def retrieve(self, request, pk=None):
#         try:
#             purchase = Purchase.objects.get(pk=pk)
#             serializer = self.serializer_class(purchase)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Purchase.DoesNotExist as exp:
#             return Response(exp, status=status.HTTP_400_BAD_REQUEST)


#Count of purchases, count of sales and count of total medicines
class CountAPI(APIView):
    queryset = Purchase.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    #class RegisterView(generics.GenericAPIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'Authentication failed': 'User not authenticated'}, status=status.HTTP_200_OK)

        medicine_names=[medicine.medicine_name for medicine in MedicineInventory.objects.filter(account=request.user)]
        sales_names=[sales.id for sales in Sales.objects.filter(account=request.user)]
        purchase_names=[purchase.id for purchase in Purchase.objects.filter(account=request.user)]


        medicine_count = len(Counter(medicine_names).keys())
        sales_count = len(Counter(sales_names).keys())
        purchase_count = len(Counter(purchase_names).keys())

        return Response({'medicine_count': medicine_count, 'sales_count': sales_count, 'purchase_count': purchase_count}, status=status.HTTP_200_OK)

class ExpiryAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'Authentication failed': 'User not authenticated'}, status=status.HTTP_200_OK)

        medicine_names=[medicine.medicine_name for medicine in MedicineInventory.objects.filter(account=request.user, isexpired=True)]
        return Response({'medicine_names': medicine_names}, status=status.HTTP_200_OK)

class StockAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'Authentication failed': 'User not authenticated'}, status=status.HTTP_200_OK)
        medicine_names = [medicine.medicine_name for medicine in MedicineInventory.objects.filter(account=request.user)]
        medicine_names = list(set(medicine_names))
        low_stock = {}
        for medicine_name in medicine_names:
            medicines = MedicineInventory.objects.filter(medicine_name=medicine_name)
            count = 0
            for medicine in medicines:
                print(medicine)
                count += medicine.medicine_quantity
            if count < 10:
                low_stock[medicine_name] = count 
        return Response({'medicine_details':low_stock}, status=status.HTTP_200_OK)