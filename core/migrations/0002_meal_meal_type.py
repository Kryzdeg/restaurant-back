# Generated by Django 3.1.5 on 2021-01-27 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='meal_type',
            field=models.CharField(default='dinner', max_length=10),
        ),
    ]
