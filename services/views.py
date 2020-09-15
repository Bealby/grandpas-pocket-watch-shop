from django.shortcuts import render

# Create your views here.

def services(request):
# A view to return the index page

    return render(request, 'services/services.html')

def success(request):
    return HttpResponse('Success! Thank you for your message.')