from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    # main index at /jobs/
    path("", views.job_index, name="job_index"),
    # job list at /jobs/job_list
    path("job_list/", views.job_list, name="job_list")
]