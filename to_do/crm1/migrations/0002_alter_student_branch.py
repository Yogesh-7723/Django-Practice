# Generated by Django 5.0.2 on 2024-02-19 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(max_length=50),
        ),
    ]