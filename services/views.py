from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Appointment, AppointmentType
from .forms import AppointmentForm


def view_services(request):
    form = AppointmentForm()
    template = 'services/services.html'
    context = {
        'form': form,
    }

    return render(request, template, context)