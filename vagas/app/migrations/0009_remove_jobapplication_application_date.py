# Generated by Django 5.0 on 2023-12-11 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_aplplication_date_jobapplication_application_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='application_date',
        ),
    ]