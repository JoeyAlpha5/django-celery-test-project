from django.db import models
from datetime import date
# Create your models here.
class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    rating_date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.rating_date)