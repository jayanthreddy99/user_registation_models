from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

def registration(request):
    USFO = UserForm()
    PFO = ProfileForm()
    d = {'USFO':USFO,'PFO':PFO}
    if request.method == 'POST' and request.FILES :
        USFD = UserForm(request.POST)
        PFD = ProfileForm(request.POST,request.FILES)
        if USFD.is_valid() and PFD.is_valid():
            NSUFO = USFD.save(commit=False)
            SPW = USFD.cleaned_data['password']
            NSUFO.set_password(SPW)
            NSUFO.save()
            NSPFO = PFD.save(commit=False)
            NSPFO.username = NSUFO
            NSPFO.save()

            send_mail('Registration',
                    'Ur Registration is Successfull',
                      'jayanthreddyvannappagari@gmail.com',
                      [NSUFO.email],
                      fail_silently=False
                          )

        return HttpResponse('data submitted sucessfully chack in admin ')
    return render(request,'registration.html',d)