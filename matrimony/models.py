from django.db import models
from django.conf import settings




class UserProfile(models.Model):
    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Divorced', 'Divorced'),
        # Add more options if needed
    ]

    LOCATION_CHOICES = [
        ('Location 1', 'Location 1'),
        ('Location 2', 'Location 2'),
        ('Location 3', 'Location 3'),
        # Add more locations as needed
    ]
    
    EDUCATION_CHOICES = [
        ('High School', 'High School'),
        ("Bachelor's Degree", "Bachelor's Degree"),
        ("Master's Degree", "Master's Degree"),
        ('PhD', 'PhD'),
        # Add more education levels as needed
    ]
    
    DESIGNATION_CHOICES = [
        ('Engineer', 'Engineer'),
        ('Doctor', 'Doctor'),
        ('Teacher', 'Teacher'),
        ('Manager', 'Manager'),
        # Add more designations as needed
    ]
    
    RELIGION_CHOICES = [
        ('Hindu', 'Hindu'),
        ('Christian', 'Christian'),
        ('Muslim', 'Muslim'),
        ('Other', 'Other'),
        # Add more religions as needed
    ]
    
    CASTE_CHOICES = [
        ('Caste 1', 'Caste 1'),
        ('Caste 2', 'Caste 2'),
        ('Caste 3', 'Caste 3'),
        # Add more castes as needed
    ]

    BODY_TYPE_CHOICES = [
        ('average', 'Average'),
        ('athletic', 'Athletic'),
        ('slim', 'Slim'),
        ('heavy', 'Heavy'),
        # Add other body types as needed
    ]

    COMPLEXION_CHOICES = [
        ('fair', 'Fair'),
        ('medium', 'Medium'),
        ('dark', 'Dark'),
        # Add other complexion types as needed
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS_CHOICES, default='Single')
    annual_income = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    family_type = models.CharField(max_length=50, default='Unknown')
    father_name = models.CharField(max_length=100, default='Unknown')
    father_occupation = models.CharField(max_length=100, default='Unknown')
    mother_name = models.CharField(max_length=100, default='Unknown')
    mother_occupation = models.CharField(max_length=100, default='Unknown')
    number_of_siblings = models.IntegerField(default=1)
    number_of_siblings_married = models.IntegerField(default=1)
    sibling_details = models.TextField(default="")
    height = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Set a default value
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    body_type = models.CharField(max_length=50, choices=BODY_TYPE_CHOICES, blank=True, default='average')
    complexion = models.CharField(max_length=50, choices=COMPLEXION_CHOICES, default='medium')
    disabilities = models.CharField(max_length=255, blank=True, default='No disabilities')
    religion = models.CharField(max_length=50, choices=RELIGION_CHOICES, default='Hindu')
    caste = models.CharField(max_length=50, choices=CASTE_CHOICES, default='Caste 1')
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES, default='Location 1')
    education = models.CharField(max_length=100, choices=EDUCATION_CHOICES, default='High School')
    designation = models.CharField(max_length=100, choices=DESIGNATION_CHOICES, default='Engineer')

    def __str__(self):
        return self.user.username


class PartnerExpectations(models.Model):
    CASTE_CHOICES = [
        ('Caste 1', 'Caste 1'),
        ('Caste 2', 'Caste 2'),
        ('Caste 3', 'Caste 3'),
        # Add more castes as needed
    ]
    
    LOCATION_CHOICES = [
        ('Location 1', 'Location 1'),
        ('Location 2', 'Location 2'),
        ('Location 3', 'Location 3'),
        # Add more locations as needed
    ]
    
    EDUCATION_CHOICES = [
        ('High School', 'High School'),
        ('Bachelor\'s Degree', 'Bachelor\'s Degree'),
        ('Master\'s Degree', 'Master\'s Degree'),
        ('PhD', 'PhD'),
        # Add more education levels as needed
    ]
    
    OCCUPATION_CHOICES = [
        ('Engineer', 'Engineer'),
        ('Doctor', 'Doctor'),
        ('Teacher', 'Teacher'),
        ('Manager', 'Manager'),
        # Add more occupations as needed
    ]

    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    age = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    caste = models.CharField(max_length=50, choices=CASTE_CHOICES, default='Caste 1')
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES, default='Location 1')
    education = models.CharField(max_length=100, choices=EDUCATION_CHOICES, default='High School')
    occupation = models.CharField(max_length=100, choices=OCCUPATION_CHOICES, default='Engineer')

    def __str__(self):
        return f"{self.user_profile.user.username}'s Partner Expectations"
