# Generated by Django 3.0.8 on 2020-08-01 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terapie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='therapy',
            name='mutacja_aktywujaca_EFGR',
            field=models.BooleanField(null=True),
        ),
    ]
