from django.db import models
from quizes.models import Fanmavzusi
import random
# Create your models here.



class SavolQuerySet(models.QuerySet):
    def Asanroq(self):
        return self.filter(savol_turi="ASN")

    def Ortacha(self):
        return self.filter(savol_turi="ORT")

    
    def Qiyin(self):
        return self.filter(savol_turi="QYN")
    
    
    
class SavolManager(models.Manager):
    def get_queryset(self):
        return SavolQuerySet(self.model, using=self._db)

    def Asanroq(self):
        return self.get_queryset().Asanroq()

    def Ortacha(self):
        return self.get_queryset().Ortacha()
    
    def Qiyin(self):
        return self.get_queryset().Qiyin()

class Savol(models.Model):
    SAVOL_TURI=[
       ("ASN" , "Asonroq Savol"),
       ("ORT" , "O\'rtacha Savol"),
       ("QYN" , "Qiyin Savol"),
    ]
    text=models.CharField(max_length=200)
    fan_yoke_mavzu=models.ForeignKey(Fanmavzusi, on_delete=models.CASCADE)
    savol_turi=models.CharField(max_length=3, choices=SAVOL_TURI, default="ORT")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    objects=SavolManager()
    def __str__(self) -> str:
        return str(self.text)
    def get_answers(self):
        savol=list(self.varyant_set.all())
        random.shuffle(savol)
        return savol
    
    
class Varyant(models.Model):
    text=models.CharField(max_length=250)
    tugri_yoke_natugri=models.BooleanField(default=False, help_text="To\'g\'ri varionad bo\'lsa ptichka qo\'ying!!")
    savol=models.ForeignKey(Savol, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.savol.text} tugri_yoke_natugri:{self.text} xato yoke trug\'risi {self.tugri_yoke_natugri}"
    