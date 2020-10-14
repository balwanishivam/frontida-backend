<<<<<<< HEAD
# from rest_framework.serializers import ModelSerializer
# from .models import *


# class MedicineInventorySerializers(ModelSerializer):
#     class Meta:
#         model=MedicineInventory
#         fields = ['batch_number', 'medicine_name', 'mfd', 'expiry', 'purchase_price', 'sale_price', 'medicine_quantity', 'company_name']
#         exclude=['account', 'HSNcode']


# class CompanyDetailsSerializers(ModelSerializer):
#     class Meta:
#         model = CompanyDetails
#         fields = ['company_name', 'company_contact', 'company_address', 'company_email', 'gst_number']

# class PurchaseSerializers(ModelSerializer):
#     class Meta:
#         model = Purchase
#         fields = ['distributor_name', 'bill_number', 'bill_date', 'total_amount', 'discount']
#         exclude = ['account', 'company_name']

# class PurchaseInventorySerializers(ModelSerializer):
#     class Meta:
#         model = PurchaseInventory
#         fields = ['medicine_name', 'quantity', 'batch_number', 'price_of_each']
#         exclude = ['purchase_id']

# class SalesSerializers(ModelSerializer):
#     class Meta:
#         model = Sales
#         fields = ['customer_name', 'customer_contact', 'referred_by', 'bill_date', 'total_amount', 'discount']
#         exclude = ['account']

# class SalesInventorySerializers(ModelSerializer):
#     class Meta:
#         model = SalesInventory
#         fields = ['medicine_name', 'quantity', 'batch_number', 'price_of_each']
#         exclude = ['sales_id']

# #class BillingSerializers(ModelSerializer):
# #    class Meta:
# #        model=Billing
# #        # exclude=['account',]

# #class AccountSerializers(ModelSerializer):
# #    class Meta:
# #        model=Accounting
# #        # exclude=['account',]
=======
from rest_framework.serializers import ModelSerializer
from .models import *


class MedicineInventorySerializers(ModelSerializer):
    class Meta:
        model=MedicineInventory
        fields = ['batch_number', 'medicine_name', 'mfd', 'expiry', 'purchase_price', 'sale_price', 'medicine_quantity', 'company_name']
        exclude=['account', 'HSNcode']


class CompanyDetailsSerializers(ModelSerializer):
    class Meta:
        model = CompanyDetails
        fields = ['company_name', 'company_contact', 'company_address', 'company_email', 'gst_number']

class PurchaseInventorySerializers(ModelSerializer):
    class Meta:
        model = PurchaseInventory
        exclude = ['purchase']

class PurchaseSerializers(ModelSerializer):

    purchaseinventory = PurchaseInventorySerializers(many=True)
    class Meta:
        model = Purchase
        fields = ['distributor_name', 'bill_number', 'bill_date', 'total_amount', 'discount', 'purchaseinventory']
    
    def create(self, validated_data):
        purchase_inventory_validated = validated_data.pop('purchaseinventory')
        
        # all_companies = CompanyDetails.objects.all()
        # if company_name not in all_companies
        #     return Response({'error': CompanyDetails.DoesNotExist} ,status=status.HTTP_400_BAD_REQUEST)
        purchase = Purchase.objects.create(**validated_data)
        for entry in purchase_inventory_validated:
            PurchaseInventory.objects.create(purchase=purchase, **entry)
        return purchase

class SalesInventorySerializers(ModelSerializer):
    class Meta:
        model = SalesInventory
        exclude = ['sales_id'] 

class SalesSerializers(ModelSerializer):
    salesinventory = SalesInventorySerializers(many=True)
    class Meta:
        model = Sales
        fields = ['customer_name', 'customer_contact', 'referred_by', 'bill_date', 'total_amount', 'discount', 'salesinventory']
    
    def create(self, validated_data):
        sales_inventory_validated = validated_data.pop('salesinventory')
        sales = Sales.objects.create(**validated_data)
        for entry in sales_inventory_validated:
            SalesInventory.objects.create(sales_id=sales, **entry)
        return sales

#class BillingSerializers(ModelSerializer):
#    class Meta:
#        model=Billing
#        # exclude=['account',]

#class AccountSerializers(ModelSerializer):
#    class Meta:
#        model=Accounting
#        # exclude=['account',]
>>>>>>> 49ea5de539add091ba4f0dfc20f7858c9ac4a9b2
    
# #class DeliverySerializers(ModelSerializer):
# #    class Meta:
# #        model=Delivery
# #        # exclude=['account',]
