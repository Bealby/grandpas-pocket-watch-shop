import os
from django.shortcuts import render
from django.conf import settings

# Create your views here.


def view_contact(request):
# A view to render contact page
    context = {
            'api_key': settings.GOOGLE_MAP_API_KEY,
    }

    return render(request, 'contact/contact.html')
