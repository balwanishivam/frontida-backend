# Generated by Django 3.0.8 on 2020-07-20 16:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('Sales', 'Sales'), ('Purchase', 'Purchase')], max_length=50)),
                ('amount', models.PositiveIntegerField()),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=200)),
                ('required_quantity', models.PositiveIntegerField()),
                ('cost', models.PositiveIntegerField()),
                ('customer_name', models.CharField(max_length=50, null=True)),
                ('customer_contact', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)])),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_address', models.CharField(max_length=200)),
                ('customer_contact', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)])),
                ('time_of_order', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicineInventory',
            fields=[
                ('medicineid', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('medicine_name', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('mfd', models.DateField()),
                ('expiry', models.DateField()),
                ('purchase_price', models.PositiveIntegerField()),
                ('sale_price', models.PositiveIntegerField()),
                ('medicine_quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StoreDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100)),
                ('store_owner', models.CharField(max_length=70)),
                ('address', models.CharField(max_length=500)),
                ('landmark', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(choices=[('Jaipur', 'Jaipur'), ('Kanpur', 'Kanpur'), ('Jabalpur', 'Jabalpur'), ('Indore', 'Indore'), ('Nainital', 'Nainital'), ('Ahmedabad', 'Ahmedabad'), ('Gandinagar', 'Gandhinagar')], max_length=50)),
                ('pincode', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999), django.core.validators.MinValueValidator(100000)])),
                ('contact', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)])),
            ],
        ),
    ]