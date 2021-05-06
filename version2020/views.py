from django.shortcuts import render,HttpResponse
from datetime import datetime
from version2020.models import Registerimg
from django.contrib.messages import constants as messages

def index(request):
      return render(request,'home.html')

def hometest(request):
      return render(request,'home.html')



def teams(request):
    return render(request,'teeam.html')

def contact(request):
    return render(request,'rrcontact.html')

def events(request):
    return render(request,'events.html')

def gallery(request):
    return render(request,'gallery.html')

def testkp(request):
    return render(request,'testkp.html')

def aboutus(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'rrcontact.html')

def register(request):
    return render(request,'register.html')

def new(request):
      return render(request,'new.html')

def registerwithimg(request):
    if request.method =="POST":
        email = request.POST.get('email')
        password= request.POST.get('password')
        confirmpassword= request.POST.get('confirmpassword')
        collegename= request.POST.get('collegename')
        collegeemail= request.POST.get('collegeemail')
        stream = request.POST.get('stream')
        year = request.POST.get('year')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        p = request.FILES['image'];

        kp = Registerimg(email = email, password= password,
        confirmpassword= confirmpassword,
        collegename= collegename,
        collegeemail= collegeemail,
        stream = stream,
        year = year,
        firstname = firstname,
        lastname = lastname,
        phone = phone,
        address = address,
        pic=p)
        kp.save()

    return HttpResponse("this is homepage")
