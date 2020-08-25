from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse


# Create your views here.
def emailConsole(request):
    send_mail('Subject', 'Hello world...', 'teacherinwhitehat@gmail.com', ['diksha.verm139@gmail.com'],
              fail_silently=False)
    return HttpResponse("successfully sent mail")
