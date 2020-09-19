from django.shortcuts import render
from rest_framework import generics,status,views
from rest_framework.response import Response
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User,Token
from rest_framework.authtoken.models import Token
from .utils import Utils
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from .renderers import UserRenderer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str,smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from rest_framework.permissions import IsAuthenticated,AllowAny

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
        current_site=get_current_site(request).domain
        absurl='http://'+current_site
        email_body='Hi'+user.email+'Welcome to Frontida \n'+ absurl
        data={'email_body':email_body,'email_subject':'Welcome to frontida family','to_email':user.email}
        Utils.send_email(data)
        return Response(user_data,status=status.HTTP_201_CREATED)

# class VerifyEmail(views.APIView):
#     permission_classes = [AllowAny]
#     def get(self,request,id):
#         user=User.objects.get(id=id)
#         print(user.id)
#         token=Token.objects.get(user=user).key 
#         try:
#             if not user.is_verified:
#                 user.is_verified=True
#                 user.save()
#             return Response({'email':user.email,'user_type':user.user_type,'Email':'Is Verified','token:':token},status=status.HTTP_200_OK)
#         except jwt.ExpiredSignatureError as identifier:
#             return Response({'error':'Activation Expired'},status=status.HTTP_400_BAD_REQUEST)
#         except jwt.exceptions.DecodeError as identifier:
#             return Response({'error':'Invalid Token'},status=status.HTTP_400_BAD_REQUEST)
        
class LoginAPI(generics.GenericAPIView):
    serializer_class=LoginSerializer
    permission_classes = [AllowAny]
    def post(self,request):
        serializer =self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data=serializer.data
        user=User.objects.get(email=user_data['email'])
        token=Token.objects.get(user=user).key
        response_data = {'details': serializer.data,'token': token}
        return Response(response_data,status=status.HTTP_200_OK)

# class RequestPasswordResetEmail(generics.GenericAPIView):
#     serializer_class=ResetPasswordEmailRequestSerializer
#     permission_classes = [AllowAny]
#     def post(self,request):
#         # data={'request':request,'data':request.data}
#         serializer=self.serializer_class(data=request.data)
#         email=request.data['email']
#         if User.objects.filter(email=email).exists():
#             user=User.objects.get(email=email)
#             # print(user.id)
#             # uidb64=urlsafe_base64_encode(smart_bytes(user.id))
#             token=Token.objects.get(user=user).key
#             current_site=get_current_site(request=request).domain
#             # absurl='http://'+current_site+relativeLink
#             # email_body='Hello,\n Use link below to reset your password \n'+ absurl
#             # data={'email_body':email_body,'email_subject':'Reset your Password','to_email':user.email}
#             # Utils.send_email(data)
            
#             return Response({'Success':'We have sent you a link to reset your password'},status=status.HTTP_200_OK)
#         else:
#             return Response({'Email':'Email Not Found'},status=status.HTTP_400_BAD_REQUEST)



# class SetNewPasswordAPI(generics.GenericAPIView):
#     serializer_class=SetNewPasswordSerializer
#     permission_classes = [AllowAny]
#     def post(self,request,uidb64,token):
#         try:
#             serializer=self.serializer_class(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             id=smart_str(urlsafe_base64_decode(uidb64))
#             user=User.objects.get(id=id)
#             token_user=Token.objects.get(user=user).key
#             if token!=token_user:
#                 return Response({'error':'Token is not valid.Please request for a new one'},status=status.HTTP_401_UNAUTHORIZED)
#             user.set_password(password)
#             user.save()
#             return Response({'sucess':True,'message':'Credentials Valid','uidb64':uidb64,'token':token},status=status.HTTP_200_OK)
#         except DjangoUnicodeDecodeError as identifier:
#              return Response({'error':'Token is not valid.Please request for a new one'},status=status.HTTP_401_UNAUTHORIZED)

# class SetNewPasswordAPI(generics.GenericAPIView):
    # serializer_class=SetNewPasswordSerializer
    # permission_classes = [AllowAny]
    # def post(self,request):
    #     serializer=self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     return Response({'sucess':True,'message':'Password reset success'},status=status.HTTP_200_OK)

# class LogoutView(generics.GenericAPIView):
#     serializer_class = RefreshTokenSerializer
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args):
#         sz = self.get_serializer(data=request.data)
#         sz.is_valid(raise_exception=True)
#         sz.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)