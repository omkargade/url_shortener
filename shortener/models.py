from django.db import models

# Create your models here.


class Shorted(models.Model):
    url = models.TextField()
    short_url = models.TextField(unique=True)

    def __str__(self):
        return self.url
