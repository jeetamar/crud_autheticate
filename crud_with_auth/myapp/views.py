from django.shortcuts import render
from django.views import View
from .models import *
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from crud_with_auth.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import random


# Create your views here.

def index(request):
    return render(request,'index.html')


class CustomerRegisView(View):

    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'accounts/register.html',{'form':form})

    def post(self,request):
        form =CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations !! Registered Successfully !')
            # form.save()
            print("User Created")
            email=request.POST.get('email')
            username=request.POST.get('username')
            password=request.POST.get('password1')
            # print(email,password)
            # send_mail("User Data: ", f"New User Created", EMAIL_HOST_USER,
            #       [email], fail_silently=True)
            subject = " Welcome to the Dajngo Crud Function"
            message = " Hii.. \nYour Username is :-" + username + " \nPassword is :- " + password + "\nThank u for visiting our website .\n\nThanking You !"
            from_email = EMAIL_HOST_USER
            to_list = [email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        return render(request,'accounts/register.html',{'form':form})


class ProfileView(View):

    def get(self,request):
        form=CustomerProfileForm()
        return render(request,'accounts/profile.html',{'form':form,'active':'btn-primary'})
