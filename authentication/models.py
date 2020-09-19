from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
 

USER_TYPE=[
    ('MEDICAL STORE','MEDICAL STORE'),
    ('AMBULANCE','AMBULANCE')
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
    is_verified=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)





@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)



        

