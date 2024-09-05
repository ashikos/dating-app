from django import forms
from .models import UserProfile, PartnerExpectations
from django.contrib.auth import get_user_model

User = get_user_model()

# forms.py
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password'
    }))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'marital_status', 'annual_income', 'family_type', 'father_name', 'father_occupation',
            'mother_name', 'mother_occupation', 'number_of_siblings', 'number_of_siblings_married', 'sibling_details',
            'height', 'weight', 'body_type', 'complexion', 'disabilities', 'religion', 'caste', 'location', 
            'education', 'designation'
        ]
        widgets = {
            'marital_status': forms.Select(attrs={'class': 'form-control'}),
            'annual_income': forms.NumberInput(attrs={'class': 'form-control'}),
            'family_type': forms.TextInput(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'father_occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_siblings': forms.NumberInput(attrs={'class': 'form-control'}),
            'number_of_siblings_married': forms.NumberInput(attrs={'class': 'form-control'}),
            'sibling_details': forms.Textarea(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'body_type': forms.Select(attrs={'class': 'form-control'}),
            'complexion': forms.Select(attrs={'class': 'form-control'}),
            'disabilities': forms.TextInput(attrs={'class': 'form-control'}),
            'religion': forms.Select(attrs={'class': 'form-control'}),
            'caste': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'education': forms.Select(attrs={'class': 'form-control'}),
            'designation': forms.Select(attrs={'class': 'form-control'}),
        }

class PartnerExpectationsForm(forms.ModelForm):
    class Meta:
        model = PartnerExpectations
        fields = ['age', 'height', 'caste', 'location', 'education', 'occupation']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'detailbox'}),
            'height': forms.NumberInput(attrs={'class': 'detailbox'}),
            'caste': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'education': forms.Select(attrs={'class': 'form-control'}),
            'occupation': forms.Select(attrs={'class': 'form-control'}),
        }
