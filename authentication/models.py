from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.contrib.auth.models import User

USER_TYPE=[
    ('ADMIN','ADMIN'),
    ('MEDICAL STORE','MEDICAL STORE')
]
class UserManager(BaseUserManager):
    def create_user(self,email,user_type,password=None):
        if email is None:
            raise TypeError('User should have a email')
        
        user=self.model(email=self.normalize_email(email),user_type=user_type)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password=None):
        if email is None:
            raise TypeError('User should have a email')
        if password is None:
            raise TypeError('Password should not be none')
        user=self.create_user(email,"ADMIN",password)
        user.is_staff=True
        user.is_superuser=True
        user.save()
    
class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=255,blank=True)
    email=models.EmailField(max_length=255,unique=True,db_index=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    user_type=models.CharField(max_length=15,choices=USER_TYPE,blank=False)

    USERNAME_FIELD='email'

    REQUIRED_FIELDS=[]

    objects=UserManager()
    class Meta:
        unique_together=(('email','user_type'),)
    def __str__(self):
        return self.email

    def tokens(self):
        token=RefreshToken.for_user(self)
        return {
            'refresh':str(token),
            'access':str(token.access_token)
        }

# Create your models here.
