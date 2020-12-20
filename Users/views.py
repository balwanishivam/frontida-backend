from rest_framework.response import Response
from rest_framework import status
from medical_store.models import *
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from .serializers import *
from authentication.models import UserDetails
from authentication.serializers import UserDetailsSerializers
from django.contrib.gis.measure import D
from django.contrib.gis.geos import GEOSGeometry
from medical_store.models import MedicineInventory


class SearchMedicineAPI(GenericAPIView):
    serializer_class = SearchMedicineSerializer
    queryset = UserDetails

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            error_values = list(serializer.errors.values())
            error_keys = list(serializer.errors.keys())
            if len(error_values) > 0 and len(error_keys) > 0:
                return Response(f'{error_keys[0]}: {error_values[0][0]}', status.HTTP_200_OK)

        user_data = serializer.data
        medicine_name = user_data['medicine']
        latitude = float(user_data['latitude'])
        longitude = float(user_data['longitude'])
        location = GEOSGeometry(f'POINT({longitude} {latitude})', srid=4326)
        available_store = []
        store_within_radius = UserDetails.objects.filter(point__distance_lte = (location, D(km=5)))
        for store in store_within_radius:
            user = store.account
            med_inventory = MedicineInventory.objects.filter(account=user, medicine_name=medicine_name)
            if len(med_inventory) > 0:
                available_store.append(store)

        serializer = UserDetailsSerializers(available_store, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
