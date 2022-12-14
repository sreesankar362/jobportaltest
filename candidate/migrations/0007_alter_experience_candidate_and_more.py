# Generated by Django 4.1.1 on 2022-10-14 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0006_candidateprofile_total_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='candidate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exp', to='candidate.candidateprofile'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='job_status',
            field=models.CharField(default='Applied', max_length=20),
        ),
    ]
