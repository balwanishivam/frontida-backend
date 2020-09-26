from django.urls import path,include
from .views import *
app_name="medical_store"

urlpatterns = [
    path('company/', MedicineInventoryCreate.as_view(), name='medical_inventory'),
]