# Generated by Django 5.0.6 on 2024-08-29 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipoApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipo',
            name='listing_date_2',
            field=models.DateField(blank=True, null=True),
        ),
    ]
