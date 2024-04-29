from django.db import models
import random
# Create your models here.




class FanmavzusiQuerySet(models.QuerySet):
    def Boshlangich(self):
        return self.filter(tur="BOSH")

    def Ortacha(self):
        return self.filter(tur="ORTA")

    
    def Kattalar(self):
        return self.filter(tur="MRAK")
    
    
class FanmavzusiManager(models.Manager):
    def get_queryset(self):
        return FanmavzusiQuerySet(self.model, using=self._db)

    def Boshlangich(self):
        return self.get_queryset().Boshlangich()

    def Ortacha(self):
        return self.get_queryset().Ortacha()
    
    def Kattalar(self):
        return self.get_queryset().Kattalar()

    
class Fanmavzusi(models.Model):
    TUR=(
    ('BOSH','bolshlangich 8 yoshdan 12 atrofdagi bolalarga '),
    ('ORTA','o\'rtacha  13 yoshdan 17 atrofdagi bolalarga '),
    ('MRAK','murakkab  18 yoshdan + atrofdagi bolalarga '),
    )
    name=models.CharField(max_length=200)
    body=models.TextField()
    test_soni=models.IntegerField(help_text="o\'qivchi qancha test yechadi !! masalan: 20 yoki 25 yoki 62 istalgan")
    vaqti=models.IntegerField(help_text="Qancha Minit bo'lishini Kirgazing!! ")
    utish_foizi=models.IntegerField(help_text="o\'tish foizini kiriting!!")
    tur=models.CharField(max_length=20, choices=TUR)
    
    # objects=FanmavzusiManager()
    objects =FanmavzusiQuerySet.as_manager()
    
    def __str__(self) -> str:
        return f"{self.name}-{self.tur}"
    
    def get_savol(self):
        savol=list(self.savol_set.all().Asanroq())+list(self.savol_set.all().Ortacha())+list(self.savol_set.all().Qiyin())
        random.shuffle(savol)
        return savol[:self.test_soni]

        