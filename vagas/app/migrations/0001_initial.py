# Generated by Django 5.0 on 2023-12-10 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('ed_level', models.CharField(choices=[('1', 'Ensino fundamental'), ('2', 'Tecnólogo'), ('3', 'Ensino Superior'), ('4', 'Pós / MBA / Mestrado'), ('5', 'Doutorado')], default='1', max_length=1)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]