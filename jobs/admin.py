from django.contrib import admin
from jobs.models import Job, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


