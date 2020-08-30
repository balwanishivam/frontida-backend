from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str,smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import *
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
USER_TYPE=[
    ('ADMIN','ADMIN'),
    ('MEDICAL STORE','MEDICAL STORE')
]
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=60,min_length=8,write_only=True)

    class Meta:
        model=User
        fields=['email','user_type','password']

    def validate(self,attrs):
        email=attrs.get('email','')
        user_type=attrs.get('user_type','')
        return attrs
        
    def create(self,validate_data):
        return User.objects.create_user(**validate_data)

class EmailVerificationSerializer(serializers.ModelSerializer):
    token=serializers.CharField(max_length=555)

    class Meta:
        model=User
        fields=['email','user_type','token']

class LoginSerializer(serializers.ModelSerializer):
    email=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=68,min_length=8,write_only=True)
    tokens=serializers.CharField(max_length=555,read_only=True)
    user_type=serializers.ChoiceField(choices=USER_TYPE,read_only=True)
    class Meta:
        model=User
        fields=['email','password','user_type','tokens']
    def validate(self,attrs):
        email=attrs.get('email','')
        password=attrs.get('password','')
        user=auth.authenticate(email=email,password=password)
        print("123")
        if not user:
            raise AuthenticationFailed('Invalid credetials,try again')
        if not user.is_active:
            raise AuthenticationFailed('Account diabled,contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')
        
        return{
            'email':user.email,
            'user_type':user.user_type,
            'tokens':user.tokens()
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
    token=serializers.CharField(min_length=1,write_only=True)
    uidb64=serializers.CharField(min_length=1,write_only=True)

    class Meta:
        model=User
        fields=['password','token','uidb64']

        def validate(self,attrs):
            try:
                password = attrs.get('password','')
                token=attrs.get('token','')
                uidb64=attrs.get('uidb64','')
                id=froce_str(urlsafe_base64_decode(uidb64))
                user=user.objects.get(id=id)
                if not PasswordResetTokenGenerator().check_token(user,token):
                    raise AuthenticationFailed('The reset is invalid',401)
                user.set_password(password)
                user.save()
                return user
            except Exception as e:
                raise AuthenticationFailed('The reset is invalid',401)
            return super().validate(attrs)


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': 'Token is invalid or expired'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')