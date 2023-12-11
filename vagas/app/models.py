from django.db import models
from users.models import CustomUser

class Job(models.Model):
    ED_LEVEL_CHOICES = [
        ('1', 'Ensino Fundamental'),
        ('2', 'Tecnólogo'),
        ('3', 'Ensino Superior'),
        ('4', 'Pós / MBA / Mestrado'),
        ('5', 'Doutorado'),
    ]
    SALARY_CHOICES = [
        ('1', 'Até 1.000'),
        ('2', 'De 1.000 a 2.000'),
        ('3', 'De 2.000 a 3.000'),
        ('4', 'Acima de 3.000'),
    ]
    role = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    ed_level = models.CharField(max_length=1, choices=ED_LEVEL_CHOICES, default='1')
    salary = models.CharField(max_length=1, choices=SALARY_CHOICES, default='1')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role + ' ' + self.owner
    
    def get_applications(self):
        return JobApplication.objects.filter(job_opening=self)
    
class JobApplication(models.Model):
    ED_LEVEL_CHOICES = [
        ('1', 'Ensino Fundamental'),
        ('2', 'Tecnólogo'),
        ('3', 'Ensino Superior'),
        ('4', 'Pós / MBA / Mestrado'),
        ('5', 'Doutorado'),
    ]
    applicant = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    applicant_first_name = models.CharField(max_length=255)
    applicant_email = models.CharField(max_length=255)
    applicant_experience = models.TextField()
    applicant_salary_epec = models.DecimalField(max_digits=10, decimal_places=2)
    applicant_ed_level = models.CharField(max_length=1, choices=ED_LEVEL_CHOICES, default='1')
    appplicant_match = models.IntegerField()
    job_opening = models.ForeignKey(Job,on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.applicant_first_name + ' ' + str(self.application_date)
