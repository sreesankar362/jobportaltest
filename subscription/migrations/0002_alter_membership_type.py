# Generated by Django 4.1.1 on 2022-10-07 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='type',
            field=models.CharField(choices=[('Free', 'free'), ('Paid', 'paid')], default='paid', max_length=20),
        ),
    ]
