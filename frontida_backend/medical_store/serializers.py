from rest_framework.serializers import ModelSerializers
from .models import *

class MedicineSerializers(serializers.ModelSerializers):
    class Meta:
        model=MedicineInventory
        fields="__all__"

class StoreDetailsSerializers(ModelSerializers):
    class Meta:
        model=StoreDetails
        fields="__all__"

class BillingSerializers(ModelSerializers):
    class Meta:
        model=Billing
        fields="__all__"

class AccountSerializers(ModelSerializers):
    class Meta:
        model=Account
        fields="__all__"
    
class DeliverySerializers(ModelSerializers):
    class Meta:
        model=Delivery
        fields="__all__"