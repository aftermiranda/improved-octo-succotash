from django.db import models

class Product(models.Model):
    qb_number = models.CharField(max_length=20, unique=True)
    eng_number = models.CharField(max_length=20)
    part_name = models.CharField(max_length=200)
    part_length = models.FloatField(max_length=10, blank=True)
    part_material = models.CharField(max_length=20, blank=True)
    image = models.FilePathField(path="/img")

    class Meta:
        # default sorting order for searches in the product class
        ordering = ['qb_number']