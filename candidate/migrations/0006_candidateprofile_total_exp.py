# Generated by Django 4.1.1 on 2022-10-14 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0005_jobapplication_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateprofile',
            name='total_exp',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
