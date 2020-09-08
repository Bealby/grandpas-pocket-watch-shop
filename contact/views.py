from django.shortcuts import render

# Create your views here.

def view_contact(request):
# A view to render contact page

    return render(request, 'contact/contact.html')
