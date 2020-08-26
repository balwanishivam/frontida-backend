from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from . models import User
USER_CHOICE=[
    ('AMB','Ambulance'),
    ('BLB','Blood-Bank'),
    ('HSP','Hospital'),
    ('MST','Medical-Store'),
]
class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    name = serializers.CharField(required=True)
    user_type = serializers.ChoiceField(required=True,choices=USER_CHOICE)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'name': self.validated_data.get('name', ''),
            'user_type': self.validated_data.get('user_type', ''),
        }

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','name','user_type')
        read_only_fields = ('email',)

class CustomLoginSerializer(serializers.ModelSerializer):
    user_type = serializers.ChoiceField(required=True,choices=USER_CHOICE)
    class Meta:
        model = User
        fields = ('email','password','user_type')