# Generated by Django 4.1.3 on 2023-01-10 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_flight_company_alter_flight_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='company',
            field=models.CharField(choices=[('SPACEX', 'SPACEX'), ('BLUE ORIGIN', 'BLUE ORIGIN'), ('ROCKET LAB', 'ROCKET LAB'), ('NOT COMPANY', 'NOT COMPANY')], default='NOT COMPANY', max_length=15),
        ),
    ]
