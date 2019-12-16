from django.db import models


class User(models.Model):
    phone = models.CharField(max_length=11)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name
