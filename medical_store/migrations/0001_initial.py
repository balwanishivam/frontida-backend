# Generated by Django 3.1 on 2020-08-30 13:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


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
                ('sale_type', models.CharField(choices=[('Sales', 'Sales'), ('Purchase', 'Purchase')], max_length=50)),
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
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_address', models.CharField(max_length=200)),
                ('customer_contact', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)])),
                ('time_of_order', models.DateTimeField()),
                ('billing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_store.billing')),
            ],
        ),
        migrations.AddField(
            model_name='billing',
            name='medicine_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_store.medicineinventory'),
        ),
    ]
