from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    checkbox1 = models.BooleanField(default=False)
    checkbox2 = models.BooleanField(default=False)
    checkbox3 = models.BooleanField(default=False)
    checkbox4 = models.BooleanField(default=False)
    class Meta:
        app_label = 'usermanagement'
