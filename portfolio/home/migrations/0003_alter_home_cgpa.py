# Generated by Django 4.2.2 on 2023-06-08 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_home_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='cgpa',
            field=models.FloatField(),
        ),
    ]
