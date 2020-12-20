from rest_framework import serializers
from rest_framework.response import Response
from authentication.models import User,UserDetails


class SearchMedicineSerializer(serializers.Serializer):
    medicine = serializers.CharField(max_length=255)
    latitude = serializers.DecimalField(max_digits=16, decimal_places=6, default=0.0)
    longitude = serializers.DecimalField(max_digits=16,decimal_places=6,default=0.0)

    class Meta:
        fields = ['medicine', 'latitude', 'longitude']


    def validate(self, attrs):
        medicine = attrs.get('medicine')
        latitude = attrs.get('latitude')
        longitude = attrs.get('longitude')

        if not medicine:
            raise TypeError('Medicine name can not be none')
        if not latitude or not longitude:
            raise TypeError('Location fields can not be empty')
        return super().validate(attrs)


# class SearchResultsSerializer(serializers.Serializer):
#     store_name = serializers.CharField(max_length=255)
#     latitude = serializers.DecimalField(max_digits=16, decimal_places=6)
#     longitude = serializers.DecimalField(max_digits=16, decimal_places=6)
#
#     class Meta:
#         fields = ['store_name', 'latitude', 'longitude']
#
