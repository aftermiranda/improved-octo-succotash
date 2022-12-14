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
    part_raw_mtl_cost = models.FloatField(max_length=10, blank=True, default=0.00,
                                          verbose_name="Part Cost in Raw Material")
    part_vend_name = models.CharField(max_length=500, blank=True,
                                      verbose_name="Vendor Part Name")
    part_vend_cost = models.CharField(max_length=50, blank=True,
                                      verbose_name="Purchase from Vendor Cost")
    part_sale_price = models.CharField(max_length=500, blank=True,
                                       verbose_name="Part Sale Price")
    part_current_rev = models.CharField(max_length=25, blank=True,
                                        verbose_name="Current Revision")
    part_image_file = models.FileField(max_length=50, blank=True,
                                       verbose_name="Image of the Part")
    part_current_drw = models.FileField(max_length=50, blank=True,
                                        verbose_name="Current PDF of Part Drawing")
    part_tool = models.CharField(max_length=150, blank=True,
                                 verbose_name="Tool For Part")
    part_manf_op1 = models.FileField(max_length=50, blank=True,
                                     verbose_name="1st GCode Attachment")
    part_manf_op2 = models.FileField(max_length=50, blank=True,
                                     verbose_name="2nd GCode Attachment")
    part_manf_op3 = models.FileField(max_length=50, blank=True,
                                     verbose_name="3rd GCode Attachment")
    part_manf_op4 = models.FileField(max_length=10, blank=True,
                                     verbose_name="4th GCode Attachment")


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
        ordering = ['-job_number']


#class Assembly(models.Model):
#   qb_assembly_number = models.CharField(max_length=50, unique=True,
#                                        verbose_name="Quick Books Assembly Number")
# eng_assembly_number = models.CharField(max_length=10, unique=True,
#                                       verbose_name="Assembly Engineering Number")

#    def __str__(self):
#        return self.qb_assembly_number

#    class Meta:
        # default sorting order for searches in the job class
#        ordering = ['qb_assembly_number']


#class Asset(models.Model):
#    asset_serial_number = models.CharField(max_length=50, unique=True,
#                                           verbose_name="Asset Serial Number")
#    asset_owner = models.CharField(max_length=10, blank=True,
#                                   verbose_name="Asset Owner")
#    asset_product_name = models.CharField(max_length=100, blank=True,
#                                          verbose_name="Asset Product Name")
#    asset_sale_price = models.CharField(max_length=20, blank=True,
#                                        verbose_name="Sale Price, MSRP")

#    def __str__(self):
#        return self.asset_serial_number

#    class Meta:
#        # default sorting order for searches in the job class
#        ordering = ['asset_serial_number']

