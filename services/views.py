import os

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

from .models import (
    Appointment, AppointmentType, WatchModel, WatchType,
    AppointmentTime, UserProfile
)
from .forms import AppointmentForm


@login_required
def services(request):
    # Appointment booking form
    if request.method == 'GET':
        # Registered user's detail prefilled for 'Name' and 'Email'
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                appointment_form = AppointmentForm(initial={
                    'name': profile.default_full_name,
                    'email': profile.user.email,
                })
            except UserProfile.DoesNotExist:
                appointment_form = AppointmentForm()
        else:
            appointment_form = AppointmentForm()
    else:
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            user_profile = get_object_or_404(UserProfile, user=request.user)
            appointment_form = appointment_form.save(commit=False)
            appointment_form.user_profile = user_profile
            appointment_form.save()
            name = request.POST.get('name')
            email = request.POST.get('email')
            appointment_type = get_object_or_404(AppointmentType,
                                                 pk=request.POST.get('appointment_type'))
            watch_model = get_object_or_404(WatchModel,
                                            pk=request.POST.get('watch_model'))
            watch_type = get_object_or_404(WatchType,
                                           pk=request.POST.get('watch_type'))
            date = request.POST.get('date')
            time = get_object_or_404(AppointmentTime,
                                     pk=request.POST.get('time'))
            # Variables to be used in email
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
                # Email content
                subject =  \
                    render_to_string('services/confirmation_emails/confirmation_email_subject.txt',
                                     template_vars)
                body = render_to_string('services/confirmation_emails/confirmation_email_body.txt',
                                        template_vars)
                # Send email
                send_mail(subject, body, settings.DEFAULT_FROM_EMAIL,
                          [cust_email])
            except BadHeaderError:
                messages.error(request, "Please ensure fields "
                                        "are filled out correctly")
            # Appointment Success confirmation page rendered
            return redirect('appointment_success')

    context = {
        'form': appointment_form,
    }

    return render(request, "services/services.html", context)


@login_required
def appointment_success(request):
    # Appointment success
    # Message for success of booking
    messages.success(request, f'Appointment Confirmed!')
    return render(request, "services/appointment_success.html")


@login_required
def edit_appointment(request, appointment_id):
    # Edit appointment
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'GET':
        appointment_form = AppointmentForm(initial={
            'name': appointment.name,
            'email': appointment.email,
            'appointment_type': appointment.appointment_type,
            'watch_model': appointment.watch_model,
            'watch_type': appointment.watch_type,
            'date': appointment.date,
            'time': appointment.time,
            })
    else:
        appointment_form = AppointmentForm(request.POST, instance=appointment)
        # Prefilling of existing booking info
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
            # Variables to be used in email
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
                # Email content
                subject = render_to_string('services/confirmation_emails/confirmation_email_subject_edit.txt',
                                           template_vars)
                body = render_to_string('services/confirmation_emails/confirmation_email_body_edit.txt',
                                        template_vars)
                # Send email
                send_mail(subject, body, settings.DEFAULT_FROM_EMAIL,
                          [cust_email])
            except BadHeaderError:
                messages.error(request, "Please ensure fields "
                               "are filled out correctly")
            return redirect('edit_appointment_success')

    # Message to inform users of past booking being modified
    messages.info(request, f'You are editing an appointment for a Pocket \
                  Watch {appointment.appointment_type.name} booked for \
                  {appointment.date} at {appointment.time}')

    template = 'services/edit_appointment.html'
    context = {
        'form': appointment_form,
    }

    return render(request, template, context)


@login_required
def edit_appointment_success(request):
    # Message for success of modified booking
    messages.success(request, f'{"Updated Appointment Confirmed!"}')
    return render(request, "services/edit_appointment_success.html")
