# Generated by Django 4.1.1 on 2022-10-10 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyaccount', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SocialProfile',
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='is_activated',
            field=models.BooleanField(default=False),
        ),
    ]
