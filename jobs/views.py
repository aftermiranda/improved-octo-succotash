from django.core.exceptions import ValidationError
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .models import Product, Job
from .widgets import DatePickerInput

def job_index(request):
    return render(request, 'job_index.html', {})

def job_list(request):
    newest_jobs = Job.objects.order_by('-create_date')[:20]
    context = {'newest_jobs': newest_jobs}
    return render(request, 'job_list.html', context)

def add_job(request):
    """ View to add new jobs to the job list """
    add_fields = ['job_number', 'product', 'quantity', 'start_date', 'machine_deadline']
    add_labels = {
        'job_number': _('QCD Job Number'),
        'product': _('Product QB Number'),
        'quantity': _('Quantity Required'),
        'start_date': _('Job Start Date'),
        'machine_deadline': _('QCD Machine Shop Deadline'),
    }
    add_widgets = {
        'start_date': DatePickerInput(),
        'machine_deadline': DatePickerInput(),
    }
    add_form_set = modelformset_factory(Job, fields=add_fields, labels=add_labels, widgets=add_widgets)
    if request.method == 'POST':
        formset = add_form_set(request.POST)
        if formset.is_valid():
            formset.save()
            newest_jobs = Job.objects.order_by('-create_date')[:15]
            context = {'newest_jobs': newest_jobs}
            HttpResponseRedirect(reverse('job_list.html', context))
        else:
            raise ValidationError("Oops! Something went wrong!")
    else:
        formset = add_form_set(queryset=Job.objects.none())

    return render(request, 'add_job.html', {'formset': formset})

def job_sheet(request, job_number):
    current_job = Job.objects.get(job_number=job_number)
    context = {'job': current_job}
    return render(request, 'job_sheet.html', context)

def product_list(request):
    list_of_products = Product.objects.order_by('qb_number')
    context = {'product_list': list_of_products}
    return render(request, 'products.html', context)

def add_product(request):
    add_fields = ['qb_number', 'eng_number', 'part_name', 'part_length', 'part_material']
    add_labels = {
        'qb_number': _('Quick Books Number'),
        'eng_number': _('Engineering Number'),
        'part_name': _('Part Name'),
        'part_length': _('Part Length (inches)'),
        'part_material': _('Part Material'),
    }
    add_form_set = modelformset_factory(Product, fields=add_fields, labels=add_labels)
    if request.method == 'POST':
        formset = add_form_set(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('product_list'))
        else:
            raise ValidationError({
                'qb_number': ValidationError(_('Quick Books number must be unique'), code='invalid'),
                'eng_number': ValidationError(_('Engineering number is required'), code='required'),
                'part_name': ValidationError(_('Part name or description is required'), code='required'),
                'part_length': ValidationError(_('Part length must be a numerical value'), code='invalid')
            })
    else:
        formset = add_form_set(queryset=Product.objects.none())

    return render(request, 'add_product.html', {'formset': formset})

def product_detail(request, qb_number):
    product = Product.objects.get(qb_number=qb_number)
    if product.qb_number == qb_number:
        return render(request, 'product_details.html', {'product': product})
    else:
        return render(request, 'products.html', {})