# from django.db import models
# # from django_google_maps import fields as map_fields
# import datetime
# from django.core.validators import MaxValueValidator, MinValueValidator
# from authentication.models import User


# TYPE=[
#     ('Sales','Sales'),
#     ('Purchase','Purchase')
# ]


# # #Medicine Inventory
# # class MedicineInventory(models.Model):
# #     HSNcode=models.CharField(max_length=6, default='3004', blank=True)
# #     medicineid=models.CharField(max_length=5,primary_key=True)
# #     batch_number=models.CharField(max_length=20,min_length=5)
# #     medicine_name = models.CharField(max_length=200)
# #     company_name = models.ForeignKey(CompanyDetails, max_length=200)
# #     mfd = models.DateField(null=False)
# #     expiry = models.DateField(null=False)
# #     purchase_price = models.PositiveIntegerField()
# #     sale_price = models.PositiveIntegerField()
# #     medicine_quantity = models.PositiveIntegerField()
# #     account = models.ForeignKey(User,on_delete=models.CASCADE)

# # class CompanyDetails(models.Model):
# #     company_name = models.CharField(min_length=1,max_length=200)
# #     company_code = models.CharField(min_length=1,max_length=20)
# #     company_contact = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
# #     agent_name=models.CharField(min_length=1,max_lenght=200)
# #     agent_contact = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
# #     company_address=models.CharField(max_lenght=200)
# #     local_address=models.CharField(min_length=1,max_lenght=200)


# # #Billing
# # class Billing(models.Model):
# #     medicine_name = models.CharField(max_length=200)
# #     medicine_id = models.ForeignKey(MedicineInventory,on_delete=models.DO_NOTHING)
# #     required_quantity = models.PositiveIntegerField()
# #     cost = models.PositiveIntegerField()
# #     customer_name = models.CharField(null=True, max_length=50)
# #     customer_contact = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
# #     account = models.ForeignKey(User,on_delete=models.CASCADE)


# # class Accounting(models.Model):
# #     date = models.DateField()
# #     sale_type=models.CharField(max_length=50,choices=TYPE)
# #     amount=models.PositiveIntegerField()
# #     date_time=models.DateTimeField(auto_now_add=False)
# #     account = models.ForeignKey(User,on_delete=models.CASCADE)

# # # class Delivery(models.Model):
# # #     customer_address = models.CharField(max_length=200)
# # #     customer_contact = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
# # #     time_of_order=models.DateTimeField(auto_now_add=False)
# # #     billing=models.ForeignKey(Billing,on_delete=models.CASCADE)
# # #     account = models.ForeignKey(User,on_delete=models.CASCADE)
