# Generated by Django 3.0.8 on 2020-08-01 21:51

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terapie', '0002_therapy_mutacja_aktywujaca_efgr'),
    ]

    operations = [
        migrations.AddField(
            model_name='therapy',
            name='Obecnosc_rearanzacji_w_genie_ALK_lub_ROS1',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='therapy',
            name='brak_przerzutow_OUN',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='therapy',
            name='mutacja_T790_w_genie_EGFR',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='therapy',
            name='progresja_po_leczeniu_innym_inhibitorem_EFGR',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='therapy',
            name='stopien_sprawnosci',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)]),
        ),
        migrations.AddField(
            model_name='therapy',
            name='wczesniejsze_leczenie_systemowe_kryzotynibem',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='therapy',
            name='wczesniejsze_leczenie_systemowe_zp_raka_pluca',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='therapy',
            name='wczesniejsze_leczenie_systemowe_zp_raka_pluca_incl_anty_ALK',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='therapy',
            name='wykluczenie_przeciwwskazan',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='therapy',
            name='zaawansowanie',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), null=True, size=None),
        ),
        migrations.AddField(
            model_name='therapy',
            name='zmiany_mierzalne',
            field=models.BooleanField(null=True),
        ),
    ]