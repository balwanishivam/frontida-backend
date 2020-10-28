from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
USER_TYPE=[
    ('MEDICAL STORE','MEDICAL STORE'),
    ('AMBULANCE','AMBULANCE')
]

CITY=[
    ('Jaipur','Jaipur'),
    ('Kanpur','Kanpur'),
    ('Jabalpur','Jabalpur'),
    ('Indore','Indore'),
    ('Nainital','Nainital'),
    ('Ahmedabad','Ahmedabad'),
    ('Gandinagar','Gandhinagar')
]


class UserManager(BaseUserManager):
    def create_user(self,email,user_type,password=None):
        if email is None:
            raise TypeError('User should have a email')
        
        user=self.model(email=self.normalize_email(email),user_type=user_type)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=None):
        if email is None:
            raise TypeError('User should have a email')
        if password is None:
            raise TypeError('Password should not be none')
        user=self.create_user(email,"ADMIN",password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
    
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

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)


#User Details
class UserDetails(models.Model):
    store_name = models.CharField(max_length=100, unique=False)
    store_owner = models.CharField(max_length=70)
    address = models.CharField(max_length=500)
    landmark = models.CharField(null=True, max_length=50)
    city = models.CharField(max_length=50,choices=CITY)
    pincode = models.PositiveIntegerField() 
    contact = models.BigIntegerField()
    # location = GMaps
    account = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.account.email



