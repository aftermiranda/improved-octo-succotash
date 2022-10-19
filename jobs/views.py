from django.shortcuts import render

def job_index(request):
    return render(request, 'job_index.html', {})

def job_list(request):
    return render(request, 'job_list.html', {})