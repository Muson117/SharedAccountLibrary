# Generated by Django 2.0.2 on 2018-07-29 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180728_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={},
        ),
        migrations.RemoveField(
            model_name='account',
            name='account_free',
        ),
        migrations.AddField(
            model_name='account',
            name='account_status',
            field=models.CharField(blank=True, choices=[('t', 'Taken'), ('a', 'Available'), ('m', 'Maintenance')], default='m', help_text='Account availability', max_length=1),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_FirstName',
            field=models.CharField(max_length=100, verbose_name='FirstName'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_LastName',
            field=models.CharField(max_length=100, verbose_name='LastName'),
        ),
    ]
