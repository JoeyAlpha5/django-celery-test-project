from django.db import models

# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key=True)
    user_firebase_id = models.CharField(max_length=250)

    def __str__(self):
        return self.user_firebase_id

