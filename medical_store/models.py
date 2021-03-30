from django.db import models

# from django_google_maps import fields as map_fields
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from authentication.models import User
from hashid_field import HashidField

# Medicine Inventory
class MedicineInventory(models.Model):
    HSNcode = models.CharField(max_length=6, default="3004", blank=True)
    batch_number = models.CharField(max_length=20)
    medicine_name = models.CharField(max_length=200)
    company_name = models.ForeignKey(
        "CompanyDetails", max_length=200, on_delete=models.DO_NOTHING
    )
    mfd = models.DateField(null=False)
    expiry = models.DateField(null=False)
    purchase_price = models.PositiveIntegerField()
    sale_price = models.PositiveIntegerField()
    medicine_quantity = models.PositiveIntegerField()
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    isexpired = models.BooleanField(default=False)

    def __str__(self):
        return self.medicine_name


class CompanyDetails(models.Model):
    company_name = models.CharField(max_length=200)
    company_contact = models.BigIntegerField(
        validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)]
    )
    company_address = models.CharField(max_length=200)
    company_email = models.EmailField()
    gst_number = models.CharField(max_length=15)

    def __str__(self):
        return self.company_name


class Purchase(models.Model):
    distributor_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=200)
    bill_number = models.CharField(max_length=10)
    bill_date = models.DateField(null=True)
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)
    discount = models.DecimalField(decimal_places=2, max_digits=4)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    hash_val = HashidField(null=True,blank=True)

    def __str__(self):
        return self.distributor_name


class PurchaseInventory(models.Model):
    medicine_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    batch_number = models.CharField(max_length=20)
    price_of_each = models.PositiveIntegerField()
    mrp = models.PositiveIntegerField()
    mfd = models.DateField(null=False)
    expiry = models.DateField(null=False)
    purchase = models.ForeignKey(
        Purchase, on_delete=models.DO_NOTHING, related_name="purchaseinventory"
    )
    isexpired = models.BooleanField(default=False)

    def __str__(self):
        return self.medicine_name


class Sales(models.Model):
    bill_number = models.CharField(max_length=10)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.BigIntegerField()
    referred_by = models.CharField(max_length=50)
    bill_date = models.DateField()
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)
    discount = models.DecimalField(decimal_places=2, max_digits=4)
    account = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_name


class SalesInventory(models.Model):
    medicine_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    # prescription = models.CharField(max_length=)
    batch_number = models.CharField(max_length=20)
    price_of_each = models.PositiveIntegerField()
    sales_id = models.ForeignKey(
        Sales, on_delete=models.DO_NOTHING, related_name="salesinventory"
    )
    isexpired = models.BooleanField(default=False)

    def __str__(self):
        return self.medicine_name


# class Delivery(models.Model):
#     customer_address = models.CharField(max_length=200)
#     customer_contact = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
#     time_of_order=models.DateTimeField(auto_now_add=False)
#     billing=models.ForeignKey(Billing,on_delete=models.CASCADE)
#     account = models.ForeignKey(User,on_delete=models.CASCADE)