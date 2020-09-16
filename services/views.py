import os

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages

from .models import Appointment, AppointmentType, WatchModel, WatchType
from .forms import AppointmentForm


def services(request):
    if request.method == 'GET':
        appointment_form = AppointmentForm()
    else:
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment_form.save()
            name = appointment_form.cleaned_data['name']
            email = appointment_form.cleaned_data['email']
            appointment_type = appointment_form.cleaned_data['appointment_type']
            watch_model = appointment_form.cleaned_data['watch_model']
            watch_type = appointment_form.cleaned_data['watch_type']
            date = appointment_form.cleaned_data['date']
            try:
                send_mail(name, email, appointment_type, watch_model, watch_type, date, ['grandpas-pocket-watch-shop@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    context = {
        'form': appointment_form,
    }

    return render(request, "services/services.html", context)


def success(request):
    return HttpResponse('Success! Thank you for your message.')