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

class Job(models.Model):
    job_number = models.CharField(max_length=10, unique=True)
    create_date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=False)
    quantity = models.CharField(max_length=10)
    start_date = models.DateField()
    machine_deadline = models.DateField()

    class Meta:
        # default sorting order for searches in the job class
        ordering = ['-create_date', '-start_date']