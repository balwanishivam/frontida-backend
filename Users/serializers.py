from rest_framework.serializers import ModelSerializer
from .models import *


class UserDetailSerializers(ModelSerializer):
    class Meta:
        model=UserDetail
        fields= '__all__'
