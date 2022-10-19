from django.urls import path
from main_index import views

app_name = 'main_index'
urlpatterns = [
    path('', views.hello_world, name='main_index'),

]