import os

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

from .models import Appointment, AppointmentType, WatchModel, WatchType
from .forms import AppointmentForm


@login_required
def services(request):
    if request.method == 'GET':
        appointment_form = AppointmentForm()
    else:
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment_form.save()
            name = appointment_form.cleaned_data['name']
            email = appointment_form.cleaned_data['email']
            appointment_type =  \
                appointment_form.cleaned_data['appointment_type']
            watch_model = appointment_form.cleaned_data['watch_model']
            watch_type = appointment_form.cleaned_data['watch_type']
            date = appointment_form.cleaned_data['date']
            time = appointment_form.cleaned_data['time']
            try:
                template_vars = {
                    'name': request.user.get_full_name(),
                    'email': email,
                    'appointment_type': appointment_type,
                    'watch_model': watch_model,
                    'watch_type': watch_type,
                    'date': date,
                    'time': time,
                }
                cust_email = email
                subject =  \
                    render_to_string('services/confirmation_emails/confirmation_email_subject.txt', template_vars)
                body = render_to_string('services/confirmation_emails/confirmation_email_body.txt', template_vars)

                send_mail(subject, body, settings.DEFAULT_FROM_EMAIL,
                          [cust_email])
            except BadHeaderError:
                messages.error(request, "Please ensure fields "
                                        "are filled out correctly")
            return redirect('services_success')

    context = {
        'form': appointment_form,
    }

    return render(request, "services/services.html", context)


@login_required
def services_success(request):

    return render(request, "services/services_success.html")
