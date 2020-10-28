from django.shortcuts import render
from rest_framework import generics,status,views
from rest_framework.response import Response
from .serializers import *
from .models import User,Token,UserDetails
from rest_framework.authtoken.models import Token
from .utils import Utils
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.shortcuts import redirect
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

def UserVerification(request, uidb64, token):
    if request.method == 'GET':        
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)
        except DjangoUnicodeDecodeError as exp:
            raise AuthenticationFailed('Not a valid account verification link', 401)    
        if token != Token.objects.get(user=user).key:
            raise AuthenticationFailed('Not a valid account verification link', 401)
        else:
            if not user.is_verified:
                user.is_verified=True
                user.save()
            user.auth_token.delete()
            Token.objects.create(user = request.user)
            frontend_login_url = "http://localhost:3000/signin"
            return redirect(frontend_login_url)


class RegisterView(generics.GenericAPIView):
    serializer_class=RegisterSerializer
    permission_classes = [AllowAny]
    def post(self,request):
        user=request.data
        serializer=self.serializer_class(data=user)
        
        if not serializer.is_valid():
            error_values = list(serializer.errors.values())
            error_keys = list(serializer.errors.keys())
            print(error_keys)
            print(error_values)
            if len(error_keys) > 0 and len(error_values) > 0:
                return Response({f'{error_keys[0]}': f'{error_values[0][0]}'})
        
        serializer.save()
        user_data=serializer.data
        user=User.objects.get(email=user_data['email'])
        uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
        token = Token.objects.get(user=user).key

        user_verification_link = reverse('user_verification', kwargs={'uidb64': uidb64, 'token': token})
        current_site = get_current_site(request).domain
        # current_site = 'http://127.0.0.1:8000'
        absurl = current_site + user_verification_link
        subject = 'Account verification for ' + str(user.email)
        message = 'Hello, \n Thankyou for joining us, please login to complete your details and registration process. \n' + absurl  
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        email = EmailMessage(subject, message, from_email, recipient_list,)
        email.send()
        return Response(user_data,status=status.HTTP_201_CREATED)
        # else:
        #     error_values = list(serializer.errors.values())
        #     error_keys = list(serializer.errors.keys())
        #     if len(error_keys) > 0 and len(error_values) > 0:
        #         return Response({f'{error_keys[0]}': f'{error_values[0][0]}'})
        #     if User.objects.filter(email=serializer.data['email']).exists():
        #         print(serializer.errors)
        #         return Response({'Duplicate User':'User Email already used'},status=status.HTTP_200_OK)
        #     else:
        #         return Response({'Empty Fields':'Fields can not be empty'},status=status.HTTP_200_OK)
       


class LoginAPI(generics.GenericAPIView):
    serializer_class=LoginSerializer
    permission_classes = [AllowAny]
    def get(self, request):
        print(request.user)
        return Response({'yup': 'Lets try this'}, status=status.HTTP_200_OK)
    def post(self,request):
        serializer =self.serializer_class(data=request.data)
        
        if not serializer.is_valid():
            error_values = list(serializer.errors.values())
            error_keys = list(serializer.errors.keys())
            if len(error_keys) > 0 and len(error_values) > 0:
                return Response({f'{error_keys[0]}': f'{error_values[0][0]}'})
        
        user_data=serializer.data
        user=auth.authenticate(email=user_data['email'],password=user_data['password'])
        #print(user.is_verified)
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_200_OK)
        if not user.is_verified:
            return Response({'error': 'User not verified'}, status=status.HTTP_200_OK)
        auth.login(request,user)
        user=User.objects.get(email=user_data['email'])
        user_type=user.user_type
        token = Token.objects.get(user=user).key
        try:
            user_details = UserDetailsSerializers(instance = UserDetails.objects.get(account=user)) 
        except UserDetails.DoesNotExist as exp:
            return Response({'NoUserDetails':'User details not provided','token':token}, status=status.HTTP_200_OK)
        response_data = {'email': user_data['email'],'user_type':user.user_type,'token': token, 'user_details': user_details.data}

        return Response(response_data,status=status.HTTP_200_OK)
        
            # if User.objects.filter(email=serializer.data['email']).exists():
            #     print(serializer.errors)
            #     return Response({'Duplicate User':'User Email already used'},status=status.HTTP_200_OK)
            # else:
            #     return Response({'Empty Fields':'Fields can not be empty'},status=status.HTTP_200_OK)

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
            raise AuthenticationFailed(exp, 200)
        logout(request)
        return Response({"success": "Successfully logged out."},
                        status=status.HTTP_200_OK)


class UserDetailsCreate(APIView):
    authentication_classes = [TokenAuthentication]
    model=UserDetails
    serializer_class = UserDetailsSerializers
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            user_details = UserDetails.objects.get(account=request.user)
            serializer = self.serializer_class(user_details, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserDetails.DoesNotExist as exp:
            return Response({'error': 'User details not provided'}, status=status.HTTP_200_OK)
            
        

    def post(self, request):
        serializer=UserDetailsSerializers(data=request.data)
        if not request.user.is_authenticated:
            return Response({'error': 'User not logged  in'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not serializer.is_valid():    
            error_values = list(serializer.errors.values())
            error_keys = list(serializer.errors.keys())
            if len(error_keys) > 0 and len(error_values) > 0:
                return Response({f'{error_keys[0]}': f'{error_values[0][0]}'})
        
        serializer.save(account=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
            
                # if User.objects.filter(email=serializer.data['email']).exists():
                #     print(serializer.errors)
                #     return Response({'Duplicate User':'User Email already used'},status=status.HTTP_200_OK)
                # else:
                #     return Response({'Empty Fields':'Fields can not be empty'},status=status.HTTP_200_OK)

class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = PasswordResetEmailRequestSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if not serializer.is_valid():
            error_values = list(serializer.errors.values())
            error_keys = list(serializer.errors.keys())
            if len(error_keys) > 0 and len(error_values) > 0:
                return Response({f'{error_keys[0]}': f'{error_values[0][0]}'})

        email = serializer.data['email']

        try:
            user = User.objects.get(email = email)            
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token=Token.objects.get(user=user).key
            password_reset_link = reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            current_site = get_current_site(request).domain
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
            return Response(status=status.HTTP_200_OK)
        

class PasswordResetConfirm(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)
            if token != Token.objects.get(user=user).key:
                raise AuthenticationFailed('Not a valid reset link', 200)
            else:
                return Response({'success':'Token authenticated'})
        except DjangoUnicodeDecodeError as identifier:
            raise AuthenticationFailed('Not a valid reset link', 200)

    def patch(self, request, uidb64, token):
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)
            if token != Token.objects.get(user=user).key:
                raise AuthenticationFailed('Not a valid reset link', 200)
            else:
                serializer = self.serializer_class(data=request.data)
                
                if not serializer.is_valid():
                    error_values = list(serializer.errors.values())
                    error_keys = list(serializer.errors.keys())
                    if len(error_keys) > 0 and len(error_values) > 0:
                        return Response({f'{error_keys[0]}': f'{error_values[0][0]}'})

                password1 = serializer.data['password1']
                user.set_password(password1)
                user.save()
                return Response({'success': 'Password reset successfull'}, status= status.HTTP_200_OK)
        except DjangoUnicodeDecodeError as identifier:
            raise AuthenticationFailed('Not a valid user', 200)