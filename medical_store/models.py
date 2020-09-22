
from django.db import models
# from django_google_maps import fields as map_fields
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from authentication.models import User



#Medicine Inventory
class MedicineInventory(models.Model):
    HSNcode=models.CharField(max_length=6, default='3004', blank=True)
    batch_number=models.CharField(max_length=20,min_length=5)
    medicine_name = models.CharField(max_length=200)
    company_name = models.ForeignKey('CompanyDetails', max_length=200)
    mfd = models.DateField(null=False)
    expiry = models.DateField(null=False)
    purchase_price = models.PositiveIntegerField()
    sale_price = models.PositiveIntegerField()
    medicine_quantity = models.PositiveIntegerField()
    account = models.ForeignKey(User,on_delete=models.CASCADE)

#     #create_buy and update_buy

class CompanyDetails(models.Model):
    company_name = models.CharField(min_length=1,max_length=200)
    company_contact = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    company_address=models.CharField(max_lenght=200)
    company_email = models.EmailField()
    gst_number = models.CharField(max_length=15)
    account = models.ForeignKey('User',on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name


class Purchase(models.Model):
    distributor_name = models.CharField(max_length=50)
    company_name = models.ForeignKey('CompanyDetails', max_length=200)
    bill_number= models.CharField()
    bill_date= models.DateTimeField()
    total_amount= models.DecimalField(decimal_places=2)
    discount = models.DecimalField(decimal_places=2, max_length=4)
    account = models.ForeignKey('User',on_delete=models.CASCADE)

    def __str__(self):
        return  self.id


class PurchaseInventory(models.Model):
    medicine_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    batch_number = models.CharField(max_length=20,min_length=5)
    price_of_each= models.PositiveIntegerField()
    purchase_id= models.ForeignKey('Purchase', on_delete=models.DO_NOTHING)

class Sales(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_contact = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    referred_by = models.CharField(max_length=50)
    bill_date= models.DateTimeField()
    total_amount= models.DecimalField(decimal_places=2)
    discount = models.DecimalField(decimal_places=2, max_length=4)
    account = models.ForeignKey('User',on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class SalesInventory(models.Model):
    medicine_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    #prescription = models.CharField(max_length=)
    batch_number = models.CharField(max_length=20,min_length=5)
    price_of_each= models.PositiveIntegerField()
    sales_id = models.ForeignKey('Sales', on_delete=models.DO_NOTHING)





# class Delivery(models.Model):
#     customer_address = models.CharField(max_length=200)
#     customer_contact = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
#     time_of_order=models.DateTimeField(auto_now_add=False)
#     billing=models.ForeignKey(Billing,on_delete=models.CASCADE)
#     account = models.ForeignKey(User,on_delete=models.CASCADE)


