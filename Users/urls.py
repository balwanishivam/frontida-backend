from django.urls import path, include
from .views import SearchMedicineAPI, logout

# app_name = "Users"

urlpatterns = [
    path("medicine_search/", SearchMedicineAPI.as_view(), name="medicine_search"),
    # path("accounts/", include("allauth.urls")),
    path("auth/", include("rest_framework_social_oauth2.urls")),
    path("logout/", logout, name="logout"),
]