from django.urls import path,include
from .views import *
app_name="medical_store"

urlpatterns = [
    path('add-details/',StoreDetailsCreate.as_view(),name="create-store"),
]