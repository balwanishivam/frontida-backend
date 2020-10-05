from rest_framework.routers import SimpleRouter
from . import views
from django.urls import path
app_name="medical_store"

<<<<<<< HEAD
# router = SimpleRouter()
# router.register("medicine-inventory", views.MedicineInventoryViewSets, basename="api-medical-inventory")
# router.register("company_details", views.CompanyDetailsViewSets, basename="api-company-details")
# #router.register("purchase", views.PurchaseViewSets, basename="api-purchase")
# #router.register("purchase-inventory", views.PurchaseInventoryViewSets, basename="api-purchase-inventory")
# #router.register("sales", views.SalesViewSets, basename="api-sales")
# #router.register("sales-inventory", views.SalesInventoryViewSets, basename="api-sales-inventory")

# urlpatterns = router.urls
urlpatterns = [
    
]

=======
router = SimpleRouter()
router.register("medicine-inventory", views.MedicineInventoryViewSets, basename="api-medical-inventory")
router.register("company_details", views.CompanyDetailsViewSets, basename="api-company-details")
router.register("purchase", views.PurchaseViewSets, basename="api-purchase")
#router.register("purchase-inventory", views.PurchaseInventoryViewSets, basename="api-purchase-inventory")
#router.register("sales", views.SalesViewSets, basename="api-sales")
#router.register("sales-inventory", views.SalesInventoryViewSets, basename="api-sales-inventory")

urlpatterns = router.urls

# urlpatterns = router.urls + [path('purchase/',views.PurchaseView.as_view(), name="purchase")]
>>>>>>> 49ea5de539add091ba4f0dfc20f7858c9ac4a9b2
