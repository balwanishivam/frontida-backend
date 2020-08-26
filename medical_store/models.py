from django.db import models
# from django_google_maps import fields as map_fields
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import User

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
TYPE=[
    ('Sales','Sales'),
    ('Purchase','Purchase')
]


#Medicine Inventory
class MedicineInventory(models.Model):
    medicineid=models.CharField(max_length=5,primary_key=True)
    medicine_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    mfd = models.DateField()
    expiry = models.DateField()
    purchase_price = models.PositiveIntegerField()
    sale_price = models.PositiveIntegerField()
    medicine_quantity = models.PositiveIntegerField()
    account = models.ForeignKey(User,on_delete=models.CASCADE)

#Store Details
class StoreDetails(models.Model):
    store_name = models.CharField(max_length=100, unique=False)
    store_owner = models.CharField(max_length=70)
    address = models.CharField(max_length=500)
    landmark = models.CharField(null=True, max_length=50)
    city = models.CharField(max_length=50,choices=CITY)
    pincode = models.PositiveIntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)]) 
    contact = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    # location = GMaps
    account = models.ForeignKey(User,on_delete=models.CASCADE)


#Billing
class Billing(models.Model):
    medicine_name = models.CharField(max_length=200)
    medicine_id = models.ForeignKey(MedicineInventory,on_delete=models.DO_NOTHING)
    required_quantity = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()
    customer_name = models.CharField(null=True, max_length=50)
    customer_contact = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    account = models.ForeignKey(User,on_delete=models.CASCADE)


class Accounting(models.Model):
    date = models.DateField()
    sale_type=models.CharField(max_length=50,choices=TYPE)
    amount=models.PositiveIntegerField()
    date_time=models.DateTimeField(auto_now_add=False)
    account = models.ForeignKey(User,on_delete=models.CASCADE)

class Delivery(models.Model):
    customer_address = models.CharField(max_length=200)
    customer_contact = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    time_of_order=models.DateTimeField(auto_now_add=False)
    billing=models.ForeignKey(Billing,on_delete=models.CASCADE)
    account = models.ForeignKey(User,on_delete=models.CASCADE)
