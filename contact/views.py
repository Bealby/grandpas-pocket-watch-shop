import os

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm


def contact(request):
    if request.method == 'GET':
        contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            from_email = contact_form.cleaned_data['from_email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['grandpas-pocket-watch-shop@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    context = {
        'form': contact_form,
        'api_key': settings.GOOGLE_MAP_API_KEY,
    }

    return render(request, "contact.html", context)


def success(request):
    return HttpResponse('Success! Thank you for your message.')