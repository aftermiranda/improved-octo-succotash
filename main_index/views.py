from django.shortcuts import render
from jobs.models import Product

def hello_world(request):
    return render(request, 'main_index.html', {})

