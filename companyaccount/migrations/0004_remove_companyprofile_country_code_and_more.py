# Generated by Django 4.1.1 on 2022-10-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyaccount', '0003_alter_companyprofile_company_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyprofile',
            name='country_code',
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='company_address',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
