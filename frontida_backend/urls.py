from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('medical-store/',include('medical_store.urls')),
    path('auth/',include('EmailRegistration.urls')),
    path('users/',include('Users.urls')),
]

