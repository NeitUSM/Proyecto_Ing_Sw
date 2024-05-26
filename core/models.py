from django.db import models
from django.utils import timezone

# Create your models here.
class UserSession(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    ip = models.CharField(max_length=45)
    timestamp = models.DateTimeField(default=timezone.now)
    success = models.BooleanField(default=False)
    def __str__(self):
        return self.username