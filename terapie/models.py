from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Therapy(models.Model):
    name  = models.CharField(max_length=50)
    rozpoznanie = ArrayField(models.CharField(max_length=50),blank=False)
    mutacja_aktywujaca_EFGR = models.BooleanField(null=True)
    zaawansowanie = ArrayField(models.CharField(max_length=50),blank=True,null=True)
    zmiany_mierzalne = models.BooleanField(null=True)
    brak_przerzutow_OUN = models.BooleanField(null=True)
    stopien_sprawnosci = ArrayField(models.CharField(max_length=10),blank=True,null=True)
    wczesniejsze_leczenie_systemowe_zp_raka_pluca = models.BooleanField(null=True)
    wczesniejsze_leczenie_systemowe_zp_raka_pluca_incl_anty_ALK = models.BooleanField(null=True)
    wykluczenie_przeciwwskazan = models.BooleanField(null=True)
    progresja_po_leczeniu_innym_inhibitorem_EFGR = models.BooleanField(null=True)
    mutacja_T790_w_genie_EGFR = models.BooleanField(null=True)
    Obecnosc_rearanzacji_w_genie_ALK_lub_ROS1 = models.BooleanField(null=True)
    wczesniejsze_leczenie_systemowe_kryzotynibem = models.BooleanField(null=True)


    
