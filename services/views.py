import os

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

from .models import Appointment, AppointmentType, WatchModel, WatchType, AppointmentTime, UserProfile
from .forms import AppointmentForm


@login_required
def services(request):
    if request.method == 'GET':
        form = AppointmentForm()
    else:
        form = AppointmentForm(request.POST)
        if form.is_valid():
            user_profile = get_object_or_404(UserProfile, user=request.user)
            form=form.save(commit=False)
            form.user_profile=user_profile
            form.save()
            name = request.POST.get('name')
            email = request.POST.get('email')
            appointment_type = get_object_or_404(AppointmentType, pk=request.POST.get('appointment_type'))
            watch_model = get_object_or_404(WatchModel, pk=request.POST.get('watch_model'))
            watch_type = get_object_or_404(WatchType, pk=request.POST.get('watch_type'))
            date = request.POST.get('date')
            time = get_object_or_404(AppointmentTime, pk=request.POST.get('time'))
            try:
                template_vars = {
                    'name': name,
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
            return redirect('appointment_success')

    context = {
        'form': form,
    }

    return render(request, "services/services.html", context)


@login_required
def appointment_success(request):

    return render(request, "services/appointment_success.html")


def edit_appointment(request, appointment_id):
    # Edit appointment
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'GET':
        form = AppointmentForm(initial={
            'name': appointment.name,
            'email': appointment.email,
            'appointment_type': appointment.appointment_type,
            'watch_model': appointment.watch_model,
            'watch_type': appointment.watch_type,
            'date': appointment.date,
            'time': appointment.time,
            })
    else:
        form = AppointmentForm(request.POST, instance=appointment)
        if  form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            appointment_type =  \
                form.cleaned_data['appointment_type']
            watch_model = form.cleaned_data['watch_model']
            watch_type = form.cleaned_data['watch_type']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
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
                    render_to_string('services/confirmation_emails/confirmation_email_subject_edit.txt', template_vars)
                body = render_to_string('services/confirmation_emails/confirmation_email_body_edit.txt', template_vars)

                send_mail(subject, body, settings.DEFAULT_FROM_EMAIL,
                          [cust_email])
            except BadHeaderError:
                messages.error(request, "Please ensure fields "
                                        "are filled out correctly")
            return redirect('edit_appointment_success')
    

    template = 'services/edit_appointment.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_appointment_success(request):

    return render(request, "services/edit_appointment_success.html")