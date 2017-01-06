from django.db import models

# Create your models here.


class Goods(models.Model):
    title = models.CharField(max_length=100)
    review = models.TextField()
    special = models.BooleanField(default=False)
    image = models.ImageField()

    def __str__(self):
        return self.title


class News(models.Model):
    nazva = models.CharField(max_length=50)
    telo = models.TextField()