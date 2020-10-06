import os

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.conf import settings
from .forms import ContactForm
from django.template.loader import render_to_string
from django.contrib import messages

from profiles.models import UserProfile
from profiles.forms import UserProfileForm


def contact(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                contact_form = ContactForm(initial={
                'name': profile.default_full_name,
                'email': profile.user.email,
                })
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(name, message, email, [settings.DEFAULT_FROM_EMAIL])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact_success')

    context = {
        'form': contact_form,
        'api_key': settings.GOOGLE_MAP_API_KEY,
    }

    return render(request, "contact/contact.html", context)


def contact_success(request):

    messages.success(request, f'Email Sent!')
    return render(request, "contact/contact_success.html")
