from django import forms
from .models import Job, JobApplication

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role', 'ed_level', 'salary']
        labels = {
            'role': 'Cargo',
            'ed_level': 'Escolaridade',
            'salary': 'Faixa Salarial',
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['applicant_experience', 'applicant_ed_level', 'applicant_salary_expec']
        labels = {
            'applicant_experience': 'Experiência',
            'applicant_ed_level': 'Escolaridade',
            'applicant_salary_expec': 'Pretensão Salarial',
        }