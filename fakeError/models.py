from django.db import models

# Create your models here.
class Credentials(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.email