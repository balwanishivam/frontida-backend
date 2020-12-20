from django.urls import path
from .views import SearchMedicineAPI

urlpatterns = [
    path('medicine_search/', SearchMedicineAPI.as_view(), name='medicine_search')
]