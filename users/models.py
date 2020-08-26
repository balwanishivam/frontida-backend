from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.utils.translation import gettext as _
import datetime
USER_CHOICE=[
    ('AMB','Ambulance'),
    ('BLB','Blood-Bank'),
    ('HSP','Hospital'),
    ('MST','Medical-Store'),
]

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, name, user_type, password=None):
        user = self.model(
            email=self.normalize_email(email),
            user_type=user_type,
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, name, user_type, password):
        user = self.create_user(
            email,
            password=password,
            user_type=user_type,         
            name=name,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = None
    email = models.EmailField(_('email address'),unique=True)
    name = models.CharField(max_length=100)
    user_type=models.CharField(max_length=3,choices=USER_CHOICE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        unique_together=('email','user_type',)

    objects = UserManager()
    def __str__(self):              # __unicode__ on Python 2
        return self.email
    
