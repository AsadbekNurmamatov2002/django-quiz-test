from django.db import models

from quizes.models import Fanmavzusi
from users.models import User

# Create your models here.


class Results(models.Model):
    quiz=models.ForeignKey(Fanmavzusi, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    score=models.FloatField()
    def __str__(self):
        return str(self.pk)