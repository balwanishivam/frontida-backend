from django.shortcuts import render
from rest_framework import generics,status,views
from rest_framework.response import Response
from .serializers import *
from .models import User,Token,UserDetails
from rest_framework.authtoken.models import Token
from .utils import Utils
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
from .renderers import UserRenderer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str,smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import  permission_classes
from django.core.exceptions import ObjectDoesNotExist

class RegisterView(generics.GenericAPIView):
    serializer_class=RegisterSerializer
    permission_classes = [AllowAny]
    def post(self,request):
        user=request.data
        serializer=self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data=serializer.data
        user=User.objects.get(email=user_data['email'])
        uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
        token = Token.objects.get(user=user).key
        enter_details_link = reverse('user_details', kwargs={'uidb64': uidb64, 'token': token})

        current_site = get_current_site(request)
        absurl = 'http://'+ current_site + enter_details_link
        subject = 'Account verification for ' + str(user.email)
        message = 'Hello, \n Thankyou for joining us, please follow the link to verify your account and complete your registration. \n' + absurl
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]

        email = EmailMessage(subject, message, from_email, recipient_list,)
        email.send()

        return Response(user_data,status=status.HTTP_201_CREATED)


class LoginAPI(generics.GenericAPIView):
    serializer_class=LoginSerializer
    permission_classes = [AllowAny]
    def get(self, request):
        print(request.user)
        return Response({'yup': 'Lets try this'}, status=status.HTTP_200_OK)
    def post(self,request):
        serializer =self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data=serializer.data
        user=auth.authenticate(email=user_data['email'],password=user_data['password'])
        if not user:
            return Response({'detail': 'Invalid Credentials or activate account'}, status=status.HTTP_404_NOT_FOUND)
        auth.login(request,user)
        user=User.objects.get(email=user_data['email'])
        token = Token.objects.get(user=user).key
        # token, _ = Token.objects.get_or_create(user = user)
        response_data = {'email': user_data['email'],'token': token}
        return Response(response_data,status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return self.logout(request)
    def logout(self, request):
        try:
            # print(request.user)
            request.user.auth_token.delete()
            token = Token.objects.create(user = request.user)
            # print(token)
        except Exception as exp:
            raise AuthenticationFailed(exp, 401)

        logout(request)
        return Response({"success": "Successfully logged out."},
                        status=status.HTTP_200_OK)


class UserDetailsCreate(APIView):
    authentication_classes = [TokenAuthentication]
    model=UserDetails
    serializer_class = UserDetailsSerializers
    def get(self, request, uidb64, token):
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)

            if token != Token.objects.get(user=user).key:
                raise AuthenticationFailed('Not a valid account verification link', 401)
            else:
                return Response({'success': 'Token authenticated'}, status=status.HTTP_200_OK)
        except DjangoUnicodeDecodeError as identifier:
            raise AuthenticationFailed('Not a valid reset link', 401)


    def post(self, request, uidb64, token):
        serializer=UserDetailsSerializers(data=request.data)
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)
            print(user)
            print('\n \n')
            if token != Token.objects.get(user=user).key:
                raise AuthenticationFailed('Not a valid account verification link', 401)
            if serializer.is_valid():
                if not user.is_verified:
                    user.is_verified=True
                    user.save()
                serializer.save(account=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DjangoUnicodeDecodeError as identifier:
            raise AuthenticationFailed(identifier, 401)

class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = PasswordResetEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']

        try:
            user = User.objects.get(email = email)            
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token=Token.objects.get(user=user).key
            password_reset_link = reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            current_site = get_current_site(request)
            absurl = 'http://'+ current_site + password_reset_link
            subject = 'Password reset link for ' + str(user.email)
            message = 'Hello, \n Below is the link to reset your password \n' + absurl
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]

            email = EmailMessage(
                subject,
                message,
                from_email,
                recipient_list,
            )

            email.send()

            return Response({'success': 'Password reset link sent, check your inbox'}, status=status.HTTP_200_OK)         
        except Exception as exp:
            print('Here')
            return Response(status=status.HTTP_404_NOT_FOUND)

class PasswordResetConfirm(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)
            if token != Token.objects.get(user=user).key:
                raise AuthenticationFailed('Not a valid reset link', 401)
            else:
                return Response({'success':'Token authenticated'})
        except DjangoUnicodeDecodeError as identifier:
            raise AuthenticationFailed('Not a valid reset link', 401)

    def patch(self, request, uidb64, token):
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)
            if token != Token.objects.get(user=user).key:
                raise AuthenticationFailed('Not a valid reset link', 401)
            else:
                serializer = self.serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                password1 = serializer.data['password1']
                user.set_password(password1)
                user.save()
                return Response({'success': 'Password reset successfull'}, status= status.HTTP_200_OK)
        except DjangoUnicodeDecodeError as identifier:
            raise AuthenticationFailed('Not a valid user', 401)