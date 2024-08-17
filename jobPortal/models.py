from django.conf import settings
from django.db import models

class JobProfile(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    monthly_salary_min = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_salary_max = models.DecimalField(max_digits=10, decimal_places=2)
    skills = models.TextField()
    benefits = models.TextField()
    job_description = models.TextField()
    job_requirements = models.TextField()
    about_company = models.TextField()
    hr_email = models.EmailField()
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    posted_time = models.DateTimeField(auto_now_add=True)
    experience_level = models.CharField(max_length=50, choices=[
        ('entry', 'Entry Level'),
        ('mid', 'Mid Level'),
        ('senior', 'Senior Level'),
        ('lead', 'Lead Level')
    ])
    job_type = models.CharField(max_length=50, choices=[
        ('full-time', 'Full-Time'),
        ('part-time', 'Part-Time'),
        ('contract', 'Contract'),
        ('temporary', 'Temporary'),
        ('internship', 'Internship')
    ])
    category = models.ForeignKey('JobCategory', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.job_title

    def split_skills(self):
        return self.skills.split(',')

    def split_benefits(self):
        return self.benefits.split(',')

    def split_job_description(self):
        return self.job_description.split(',')

    def split_job_requirements(self):
        return self.job_requirements.split(',')

class JobCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
