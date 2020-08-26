from django.urls import path,include
from .views import *
app_name="medical_store"

urlpatterns = [
    path('add-details/',StoreDetailsCreate.as_view(),name="create-store"),
    # path('store-details/create-store/',StoreDetailsCreate.as_view(),name="create-store"),
    # path('store-details/<int:pk>/',StoreDetailsUpdate.as_view(),name="update-store"),
    # path('store-details/<int:pk>/leave-store/',StoreDetailsLeave.as_view(),name="leave-store"),
    # path('inventory/add-inventory/',InventoryAdd.as_view(),name="add-inventory"),
    # path('inventory/<int:pk>/delete-inventory', InventoryDelete.as_view(), name="delete-inventory"),
    # path('billing/add-billing/', BillingAdd.as_view(), name="add-billing"),
    # path('billing/<int:pk>/delete-billing/', BillingDelete.as_view(), name="delete-billing"),
    # path('accounting/add-accounting/', AccountingAdd.as_view(), name="add-accounting"),
    # path('accounting/<int:pk>/', AccountingUpdate.as_view(), name="update-accounting"),
    # path('delivery/add-delivery/', DeliveryAdd.as_view(), name="add-delivery"),
    # path('delivery/<int:pk>/', DeliveryUpdate.as_view(), name="update-delivery"),
    # path('delivery/<int:pk>/cancel-delivery/', DeliveryCancel.as_view(), name="cancel-delivery"),
]