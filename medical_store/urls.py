from rest_framework.routers import SimpleRouter
from . import views
from django.urls import path
app_name="medical_store"

# router = SimpleRouter()
# router.register("medicine-inventory", views.MedicineInventoryViewSets, basename="api-medical-inventory")
# router.register("company_details", views.CompanyDetailsViewSets, basename="api-company-details")
# #router.register("purchase", views.PurchaseViewSets, basename="api-purchase")
# #router.register("purchase-inventory", views.PurchaseInventoryViewSets, basename="api-purchase-inventory")
# #router.register("sales", views.SalesViewSets, basename="api-sales")
# #router.register("sales-inventory", views.SalesInventoryViewSets, basename="api-sales-inventory")

# urlpatterns = router.urls
urlpatterns = [
    path('count/', views.CountAPI.as_view(), name='count-API'),
    path('expiry/', views.ExpiryAPI.as_view(), name='expiry-API'),
    path('stock/', views.StockAPI.as_view(), name='stock-API'),
    
]

router = SimpleRouter()
router.register("medicine-inventory", views.MedicineInventoryViewSets, basename="api-medical-inventory")
router.register("company_details", views.CompanyDetailsViewSets, basename="api-company-details")
router.register("purchase", views.PurchaseViewSets, basename="api-purchase")
#router.register("purchase-inventory", views.PurchaseInventoryViewSets, basename="api-purchase-inventory")
router.register("sales", views.SalesViewSets, basename="api-sales")
#router.register("sales-inventory", views.SalesInventoryViewSets, basename="api-sales-inventory")

urlpatterns = urlpatterns + router.urls