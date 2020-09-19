from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str,smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import *
USER_TYPE=[
    ('MEDICAL STORE','MEDICAL STORE'),
    ('AMBULANCE','AMBULANCE')
]
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model=User
        fields=['email','user_type','password']

    def validate(self,attrs):
        email=attrs.get('email','')
        user_type=attrs.get('user_type','')
        password=attrs.get('password','')
        return attrs
        
    def create(self,validate_data):
        return User.objects.create_user(**validate_data)


# class EmailVerificationSerializer(serializers.ModelSerializer):
#     token=serializers.CharField(max_length=555)

#     class Meta:
#         model=User
#         fields=['email','user_type','token']

class LoginSerializer(serializers.ModelSerializer):
    email=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=68,min_length=8,write_only=True)
    user_type=serializers.ChoiceField(choices=USER_TYPE,read_only=True)
    class Meta:
        model=User
        fields=['email','password','user_type']
    def validate(self,attrs):
        email=attrs.get('email','')
        password=attrs.get('password','')
        user=auth.authenticate(email=email,password=password)
        if not user:
            raise AuthenticationFailed('Invalid credetials,try again')
        if not user.is_active:
            raise AuthenticationFailed('Account diabled,contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')
        
        return{
            'email':user.email,
            'user_type':user.user_type,
        }

        return super().validate(attrs)

class ResetPasswordEmailRequestSerializer(serializers.ModelSerializer):
    email=serializers.CharField(max_length=255)

    class Meta:
        model=User
        fields=['email']

    # def validate(self,attrs):
    #     email=attrs['data'].get('email','')
    #     if User.objects.filter(email=email).exists():
    #         user=User.objects.filter(email=email)
    #         uidb64=urlsafe_base64_encode(user.id)
    #         token=PasswordResetTokenGenerator().make_token(user)
    #         current_site=get_current_site(request=attrs['request'].get('request','')).domain
    #         relativeLink=reverse('password-reset-confirm',kwargs={'uidb64':uidb64,'token':token})
    #         absurl='http://'+current_site+relativeLink
    #         email_body='Hello,\n Use link below to reset your password \n'+ absurl
    #         data={'email_body':email_body,'email_subject':'Reset your Password','to_email':user.email}
    #         Utils.send_email(data)
    #         return attrs
        
        # return super().validate(attrs)

class SetNewPasswordSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68,min_length=8,write_only=True)
    password1=serializers.CharField(max_length=68,min_length=8,write_only=True)

    class Meta:
        model=User
        fields=['password','password1']

    def validate(self,attrs):
        password=attrs.get('password','')
        password1=attrs.get('password1','')
        if password1 ==password:
            return attrs
        else:
            raise AuthenticationFailed('Password does\'nt match')
        return super().validate(attrs)




# class RefreshTokenSerializer(serializers.Serializer):
#     refresh = serializers.CharField()
#     default_error_messages = {
#         'bad_token': 'Token is invalid or expired'
#     }

#     def validate(self, attrs):
#         self.token = attrs['refresh']
#         return attrs

#     def save(self, **kwargs):
#         try:
#             RefreshToken(self.token).blacklist()
#         except TokenError:
#             self.fail('bad_token')