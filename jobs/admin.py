from django.contrib import admin
from jobs.models import Job, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('qb_number', 'eng_number', 'part_name')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


