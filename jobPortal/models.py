from django.conf import settings
from django.db import models

class JobProfile(models.Model):
    job_title = models.CharField(max_length=255)
    segment = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    posted_at = models.CharField(max_length=5)
    monthly_salary_min = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_salary_max = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateTimeField()
    hours = models.CharField(max_length=5)
    job_description = models.TextField()
    key_responsibilities = models.TextField()
    skill_experience = models.TextField()
    type_of_firm = models.CharField(max_length=50, choices=[
        ('private', 'Private'),
        ('public', 'Public')
    ])
    requirement = models.CharField(max_length=50, choices=[
        ('urgent', 'Urgent'),
        ('within_1_month', 'Within 1 Month')
    ])
    job_type = models.CharField(max_length=50, choices=[
        ('full-time', 'Full-Time'),
        ('part-time', 'Part-Time'),
        ('contract', 'Contract'),
        ('temporary', 'Temporary'),
        ('internship', 'Internship')
    ])

    def __str__(self):
        return self.job_title

    def get_key_responsibilities(self):
        return self.key_responsibilities.split('.')

    def get_skill_experience(self):
        return self.skill_experience.split(',')
