# Generated by Django 4.1.1 on 2022-10-14 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0007_alter_experience_candidate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='job_status',
            field=models.CharField(default='applied', max_length=20),
        ),
    ]
