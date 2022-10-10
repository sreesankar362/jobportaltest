# Generated by Django 4.1.1 on 2022-10-09 13:19

import autoslug.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_field', models.CharField(blank=True, max_length=255, null=True)),
                ('job_position', models.CharField(blank=True, max_length=50, null=True)),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('experience_describe', models.TextField(blank=True, max_length=300, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('exp_duration', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='LatEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(blank=True, max_length=255, null=True)),
                ('institute', models.CharField(blank=True, max_length=50, null=True)),
                ('university', models.CharField(blank=True, max_length=50, null=True)),
                ('percent', models.IntegerField(validators=[django.core.validators.MinValueValidator(25), django.core.validators.MaxValueValidator(100)])),
                ('passed_year', models.IntegerField(blank=True)),
                ('study_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavedJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_job', to='home.jobmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dob', models.DateField(blank=True, max_length=8, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes')),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='user', unique=True)),
                ('experience', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='candidate.experience')),
                ('latest_edu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='candidate.lateducation')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_job', to='home.jobmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
