from django.db import models

# Create your models here.
class Fragrance(models.Model):
    name = models.CharField(max_length=200)
    house = models.CharField(max_length=200)
    perfumer = models.CharField(max_length=200)
    size = models.FloatField()

    def __str__(self):
        return self.name

class Top_Note(models.Model):
    fragrance = models.ForeignKey(Fragrance, on_delete=models.CASCADE)
    note = models.CharField(max_length=200)

class Base_Note(models.Model):
    fragrance = models.ForeignKey(Fragrance, on_delete=models.CASCADE)
    note = models.CharField(max_length=200)

class Heart_Note(models.Model):
    fragrance = models.ForeignKey(Fragrance, on_delete=models.CASCADE)
    note = models.CharField(max_length=200)
