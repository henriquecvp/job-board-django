# Generated by Django 5.0 on 2023-12-11 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_rename_applicant_id_jobapplication_applicant_and_more'),
    ]

    operations = [
    migrations.RenameField(
        model_name='jobapplication',
        old_name='applicant_salary_espec',
        new_name='applicant_salary_expec',
    ),
]
