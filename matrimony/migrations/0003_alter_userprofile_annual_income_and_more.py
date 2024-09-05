# Generated by Django 5.0 on 2024-09-02 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0002_alter_partnerexpectations_caste_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='annual_income',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='body_type',
            field=models.CharField(blank=True, choices=[('average', 'Average'), ('athletic', 'Athletic'), ('slim', 'Slim'), ('heavy', 'Heavy')], default='average', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='complexion',
            field=models.CharField(choices=[('fair', 'Fair'), ('medium', 'Medium'), ('dark', 'Dark')], default='medium', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='disabilities',
            field=models.CharField(blank=True, default='No disabilities', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='family_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='family_type',
            field=models.CharField(default='Unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='father_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='father_occupation',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mother_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mother_occupation',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='number_of_siblings',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='number_of_siblings_married',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sibling_details',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]