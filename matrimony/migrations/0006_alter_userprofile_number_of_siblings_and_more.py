# Generated by Django 5.0 on 2024-09-03 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0005_alter_userprofile_annual_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='number_of_siblings',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='number_of_siblings_married',
            field=models.IntegerField(default=1),
        ),
    ]