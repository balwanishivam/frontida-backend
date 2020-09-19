from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# from django.dispatch import receiver
# from django.urls import reverse
# from django_rest_passwordreset.signals import reset_password_token_created
# from django.core.mail import send_mail 

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


# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

#     email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

#     send_mail(
#         # title:
#         "Password Reset for {title}".format(title="frontida"),
#         # message:
#         email_plaintext_message,
#         # from:
#         "healthcare.frontida@gmail.com",
#         # to:
#         [reset_password_token.user.email]
#     )