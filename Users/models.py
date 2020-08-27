from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
#
# Create your models here.
CITY=[
    ('Jaipur','Jaipur'),
    ('Kanpur','Kanpur'),
    ('Jabalpur','Jabalpur'),
    ('Indore','Indore'),
    ('Nainital','Nainital'),
    ('Ahmedabad','Ahmedabad'),
    ('Gandinagar','Gandhinagar')
]

# Store Details
class UserDetail(models.Model):
    store_name = models.CharField(max_length=100, unique=False)
    store_owner = models.CharField(max_length=70)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50,choices=CITY)
    pincode = models.PositiveIntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)]) 
    contact = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    # location = GMaps
    email = models.EmailField(required=True)
    website = models.URLField(required=False)