from django.db import models

class Product(models.Model):
    qb_number = models.CharField(max_length=50, unique=True,
                                 verbose_name="Quick Books Number")
    eng_number = models.CharField(max_length=50,
                                  verbose_name="Engineering Number")
    part_name = models.CharField(max_length=200,
                                 verbose_name="Part Name")
    part_length = models.FloatField(max_length=10, blank=True,
                                    verbose_name="Part Length (inches)")
    part_material = models.CharField(max_length=20, blank=True,
                                     verbose_name="Part Material")

    def __str__(self):
        return self.qb_number

    class Meta:
        # default sorting order for searches in the product class
        ordering = ['qb_number']

class Job(models.Model):
    job_number = models.CharField(max_length=10, unique=True)
    create_date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=False,
                                verbose_name="Quick Books Number for Product")
    quantity = models.CharField(max_length=10)
    start_date = models.DateField()
    machine_deadline = models.DateField()

    def __str__(self):
        return self.job_number

    class Meta:
        # default sorting order for searches in the job class
        ordering = ['-create_date', '-start_date']