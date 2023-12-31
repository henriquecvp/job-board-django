# Generated by Django 5.0 on 2023-12-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_job_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_salary_espec', models.DecimalField(decimal_places=2, max_digits=10)),
                ('applicant_ed_level', models.CharField(choices=[('1', 'Ensino Fundamental'), ('2', 'Tecnólogo'), ('3', 'Ensino Superior'), ('4', 'Pós / MBA / Mestrado'), ('5', 'Doutorado')], default='1', max_length=1)),
                ('appplicant_match', models.IntegerField()),
                ('job_opening_id', models.IntegerField()),
            ],
        ),
    ]
