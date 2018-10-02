# Generated by Django 2.0.2 on 2018-10-02 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_taken_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_ShortName',
            field=models.CharField(blank=True, help_text='Your short name', max_length=20),
        ),
    ]
