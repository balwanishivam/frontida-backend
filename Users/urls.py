from django.urls import path,include
from .views import *
app_name="Users"

urlpatterns = [
     path('add-details/',UserDetailCreate.as_view(),name="add-details"),
     path('get-details/',UserDetailsGet.as_view(),name="get-details"),
] 