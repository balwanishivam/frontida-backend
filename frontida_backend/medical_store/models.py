from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

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


#Medicine Inventory
class Medicine_Inventory(models.Model):
    medicine_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    mfd = models.DateField()
    expiry = models.DateField()
    purchase_price = models.PositiveIntegerField()
    sale_price = models.PositiveIntegerField()
    medicine_quantity = models.PositiveIntegerField()
    # user = models.ForeignKey(Myuser,on_delete=models.CASCADE)

#Store Details
class Store_Details(models.Model):
    store_name = models.CharField(max_length=100, unique=False)
    store_owner = models.CharField(max_length=70)
    address = models.CharField(max_length=500)
    landmark = models.CharField(null=True, max_length=50)
    city = models.CharField(choices=CITY)
    pincode = models.PositiveIntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])
    contact = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    # location = GMaps
    # user = models.ForeignKey(Myuser,on_delete=models.CASCADE)


#Billing
class Billing(models.Model):
    medicine_name = models.CharField(max_length=200)
    # medicine_id = models.ForeignKey()
    required_quantity = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()
    customer_name = models.CharField(null=True, max_length=50)
    customer_contact = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])

#Accounting
class Accounts(model.Models):
    date = models.DateField()
    sales = models.CharField()
    purchases = models.CharField()


class Delivery(model.Models):
    customer_address = models.CharField(max_length=200)
    customer_contact = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    # isko billing se kaise link karna hai