from rest_framework.serializers import ModelSerializer
from .models import *

class MedicineSerializers(ModelSerializer):
    class Meta:
        model=MedicineInventory
        # exclude=['account',]

# class StoreDetailsSerializers(ModelSerializer):
#     class Meta:
#         model=StoreDetails
#         # exclude=['account',]

class BillingSerializers(ModelSerializer):
    class Meta:
        model=Billing
        # exclude=['account',]

class AccountSerializers(ModelSerializer):
    class Meta:
        model=Accounting
        # exclude=['account',]
    
class DeliverySerializers(ModelSerializer):
    class Meta:
        model=Delivery
        # exclude=['account',]