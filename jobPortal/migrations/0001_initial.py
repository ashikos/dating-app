# Generated by Django 4.1.5 on 2024-08-31 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('segment', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('posted_at', models.CharField(max_length=5)),
                ('monthly_salary_min', models.DecimalField(decimal_places=2, max_digits=10)),
                ('monthly_salary_max', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expiration_date', models.DateField()),
                ('hours', models.CharField(max_length=5)),
                ('job_description', models.TextField()),
                ('key_responsibilities', models.TextField()),
                ('skill_experience', models.TextField()),
                ('type_of_firm', models.CharField(choices=[('private', 'Private'), ('public', 'Public')], max_length=50)),
                ('requirement', models.CharField(choices=[('urgent', 'Urgent'), ('within_1_month', 'Within 1 Month')], max_length=50)),
                ('job_type', models.CharField(choices=[('full-time', 'Full-Time'), ('part-time', 'Part-Time'), ('contract', 'Contract'), ('temporary', 'Temporary'), ('internship', 'Internship')], max_length=50)),
            ],
        ),
    ]
