from django.contrib import admin
from django.urls import path, include

from Users.views import profile

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("authentication.urls")),
    path("medical-store/", include("medical_store.urls")),
    path("users/", include("Users.urls")),
    path("accounts/profile/", profile, name="profile"),
]
