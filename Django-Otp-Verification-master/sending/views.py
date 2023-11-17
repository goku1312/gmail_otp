import random
from django.http import HttpResponse
from rest_framework import generics
from .models import FieldsToBeSent 
from django.shortcuts import render,redirect
from .serializers import FieldsToBeSentSerializers
from django.core.mail import send_mail,EmailMessage
from .forms import UserRegistrationForm,OtpForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            msg=EmailMessage('otp code',f'<p>Your code is { number }</p>','emailfield',[email])
            msg.content_subtype="html"                                        
            msg.send()                                                        
            print('the number generated is =====>>>',number)                  
            return redirect('otpform')
    else:
        form = UserRegistrationForm()
    return render(request, 'sending/register.html', {'form': form})

number=random.randrange(1000,9999)


def otp_form(request):
    if request.method=='POST':
        form=OtpForm(request.POST)
        if form.is_valid():
            token_number=form.cleaned_data.get('token_number')
            if token_number==number:
                FieldsToBeSent.objects.create(number=number)
                return HttpResponse('you entered the correct otp!')
            else:
                return HttpResponse('incorrect otp')
    else:
        form=OtpForm()
    return render(request,'sending/otp.html',{'form':form})



class FieldsToBeSentViews (generics.ListCreateAPIView):
    queryset=FieldsToBeSent.objects.all()
    serializer_class=FieldsToBeSentSerializers
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)


