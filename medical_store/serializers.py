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

class PurchaseSerializers(ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['distributor_name', 'bill_number', 'bill_date', 'total_amount', 'discount']
        exclude = ['account', 'company_name']

class PurchaseInventorySerializers(ModelSerializer):
    class Meta:
        model = PurchaseInventory
        fields = ['medicine_name', 'quantity', 'batch_number', 'price_of_each']
        exclude = ['purchase_id']

class SalesSerializers(ModelSerializer):
    class Meta:
        model = Sales
        fields = ['customer_name', 'customer_contact', 'referred_by', 'bill_date', 'total_amount', 'discount']
        exclude = ['account']

class SalesInventorySerializers(ModelSerializer):
    class Meta:
        model = SalesInventory
        fields = ['medicine_name', 'quantity', 'batch_number', 'price_of_each']
        exclude = ['sales_id']

#class BillingSerializers(ModelSerializer):
#    class Meta:
#        model=Billing
#        # exclude=['account',]

#class AccountSerializers(ModelSerializer):
#    class Meta:
#        model=Accounting
#        # exclude=['account',]
    
#class DeliverySerializers(ModelSerializer):
#    class Meta:
#        model=Delivery
#        # exclude=['account',]
