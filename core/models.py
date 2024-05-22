from django.db import models

# Create your models here.
class UserSession(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    ip = models.CharField(max_length=45)

    def __str__(self):
        return self.username