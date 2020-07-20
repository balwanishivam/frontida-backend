# Generated by Django 3.0.8 on 2020-07-20 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medical_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storedetails',
            name='Account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='medicineinventory',
            name='Account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='delivery',
            name='Account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='delivery',
            name='billing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_store.Billing'),
        ),
        migrations.AddField(
            model_name='billing',
            name='Account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='billing',
            name='medicine_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medical_store.MedicineInventory'),
        ),
        migrations.AddField(
            model_name='accounting',
            name='Account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]