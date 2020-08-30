# Generated by Django 3.1 on 2020-08-30 11:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100)),
                ('store_owner', models.CharField(max_length=70)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(choices=[('Jaipur', 'Jaipur'), ('Kanpur', 'Kanpur'), ('Jabalpur', 'Jabalpur'), ('Indore', 'Indore'), ('Nainital', 'Nainital'), ('Ahmedabad', 'Ahmedabad'), ('Gandinagar', 'Gandhinagar')], max_length=50)),
                ('pincode', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999), django.core.validators.MinValueValidator(100000)])),
                ('contact', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('website', models.URLField(blank=True)),
            ],
        ),
    ]
