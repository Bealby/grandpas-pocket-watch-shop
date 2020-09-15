import os

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages

from .models import Appointment, AppointmentType, WatchModel, WatchType
from .forms import AppointmentForm


def services(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('services'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = AppointmentForm()
        
    template = 'services/services.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def success(request):
    
    return HttpResponse('Success! Thank you for your message.')