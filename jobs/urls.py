from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    # main index at /jobs/
    path("", views.job_index, name="job_index"),
    # job list at /jobs/job_list
    path("job_list/", views.job_list, name="job_list"),
    # new job creator at /jobs/add_job
    path('add_job/', views.add_job, name="add_job"),
    # job sheet at /jobs/<job_number>
    path('<int:job_number>', views.job_sheet, name="job_sheet"),
    # parts list at /jobs/products
    path('products/', views.product_list, name="product_list"),
    # part details at /jobs/products/<qb_number>
    path('products/<str:qb_number>/', views.product_detail, name="product_detail"),
    # new product creator at /jobs/add_product
    path('add_product/', views.add_product, name="add_product"),
]