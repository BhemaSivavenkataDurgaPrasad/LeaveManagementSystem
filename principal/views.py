from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import principle
from Teachers .models import userprofile , teacher , leave

# Create your views here.
def login(request):
    if request.method == "POST" :
        Name = request.POST['name']
        Password = request.POST['password']
        data = authenticate(request , username = Name , password = Password)
        id = User.objects.get(username = Name)
        data1 = userprofile.objects.get(User = id)
        if data is not None  and data1.role == 'Principal':
            return   phome(request , id)
        else:
            return HttpResponse("<h1> Enter the Correct Details </h1>")
         
    return render(request , 'login.html')

def Register(request) :
    if request.method == "POST" :
        Name = request.POST['name']
        Email = request.POST['email']
        Phone = request.POST['phone']
        Address = request.POST['address']
        Password = request.POST['password']
        RePassword = request.POST['repassword']
        if str(Password) == str(RePassword) : 
            obj = principle(Name = Name , Email = Email , Phone = Phone , Address = Address )
            obj.save()
            myuser = User.objects.create_user(Name , Email , Password)
            myuser.save()
            user = User.objects.get(username = Name)
            obj = userprofile(User = user , role = 'Principal')
            obj.save()
            return redirect('home')

    return render(request , 'register.html')

def home(request) :
    return render(request , 'index.html')

def phome(request , id) :
    emp = teacher.objects.all()
    value = principle.objects.get(Name = id)
    return render(request , 'principal_home.html', { 'emp' : emp , 'id' : value})

def pprofile(request , id):
    obj = principle.objects.get(id = id)
    return render(request , 'principalprofile.html', {'obj' : obj})

def pprofileupdate(request , id):
    obj = principle.objects.get(id = id)
    if request.method == "POST" :
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']

        obj.Name = name
        obj.Email = email
        obj.Phone = phone
        obj.Address = address
        obj.save()
        return pprofile(request , id)
    return render(request , 'pprofileupdate.html', {'obj':obj})


def pregister(request):
    if request.method == "POST":
        Name = request.POST['name']
        Email = request.POST['email']
        Phone = request.POST['phone']
        Address = request.POST['address']
        Password = request.POST['password']
        Repassword = request.POST['repassword']
        obj = teacher()
        obj.Name = Name
        obj.Email = Email
        obj.Phone = Phone
        obj.Address = Address
        obj.save()
        if str(Password) == str(Repassword):
            obj =  User.objects.create_user(Name , Email , Password)
            obj.save()
            return redirect('Principal_login')
        else:
            return HttpResponse('<h1> ones check the two password </h1>')
        
    return render(request , 'pregister.html')


def Thistory(request):
    obj = leave.objects.all()
    return render(request , 'Thistory.html' , {'data' : obj})


def grant(request):
    obj = leave.objects.all()
    return render(request ,'grant.html', {'data' : obj})


def request(request , id) :
    if request.method == "POST" :
        grant = request.POST['grant']
        obj = leave.objects.get(id = id)
        obj.Grant = grant
        obj.save()
    return render(request , 'request.html')

