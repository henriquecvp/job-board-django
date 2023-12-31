# Generated by Django 5.0 on 2023-12-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_jobapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='aplplication_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='applicant_email',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='applicant_experience',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='applicant_first_name',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='applicant_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
