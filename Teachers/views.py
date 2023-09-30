from django.shortcuts import render , HttpResponse , redirect
from django.http import HttpResponse
from .models import teacher
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from Teachers.models import userprofile , leave
from django.contrib.auth.decorators import login_required
 


def login(request):
    if request.method == "POST" :
        Name = request.POST['name']
        Password = request.POST['password']
        data = authenticate(request , username = Name , password = Password)
        id = User.objects.get(username = Name)
        user_id = userprofile.objects.get(User = id)
        value = teacher.objects.get(Name = id)
        emp = teacher.objects.all()
        if data is not None  and user_id.role == 'Teachers':
            return  render(request , 'teacher/Teacher_Home.html' , {'id' : value , 'emp' : emp} )
        else:
            return HttpResponse("<h1> Enter the Correct Details </h1>")
         
    return render(request , 'teacher/login.html')


def Register(request) :
    if request.method == "POST" :
        Name = request.POST['name']
        Email = request.POST['email']
        Phone = request.POST['phone']
        Address = request.POST['address']
        Password = request.POST['password']
        RePassword = request.POST['repassword']
        if str(Password) == str(RePassword) :
            obj = teacher(Name = Name , Email = Email , Phone = Phone , Address = Address )
            obj.save()
            myuser = User.objects.create_user(Name , Email , Password)
            myuser.save()
            user = User.objects.get(username = Name)
           # print(user.password)
            obj = userprofile(User = user, role = 'Teachers')
            obj.save()
            return redirect('home')
        else:
            return HttpResponse("<h1> Re-Password was Wrong</h1>")
    return render(request , 'teacher/register.html')



 
def Teacher_Home(request):
    return render(request , 'teacher/Teacher_Home.html')


def Tprofile(request , id):
    data = teacher.objects.get(id = id)
    return render(request , 'teacher/Tprofile.html' , {'data' : data})


 
def profileupdate(requset , id):
    obj = teacher.objects.get(id = id)
    if requset.method == "POST" :
        name = requset.POST['name']
        email = requset.POST['email']
        phone = requset.POST['phone']
        address = requset.POST['address']

        obj.Name = name
        obj.Email = email
        obj.Phone = phone
        obj.Address = address
        obj.save()
    return render(requset, "teacher/Tprofile_update.html" , {'obj' : obj})



def LeaveFrom(request , id):
    obj = teacher.objects.get(id= id)
    if request.method == "POST" :
        Fdate = request.POST['Fdate']
        Tdate = request.POST['Tdate']
        Reasion = request.POST['reasion']

        obj1 = leave()
        obj1.Name = obj.Name
        obj1.Fdate = Fdate
        obj1.Tdata = Tdate
        obj1.Reasion = Reasion
        obj1.save()
    return render(request , 'teacher/Leave.html' , {'data' : obj})
         
 
def ResetPassword(request , id) :
    obj = teacher.objects.get(id= id)
    id = User.objects.get(username = obj.Name)
    if request.method == "POST" :
        newpassword = request.POST['newpassword']
        repassword = request.POST['repassword']
        if str(newpassword) == str(repassword) :
            id.set_password(newpassword)
            id.save()

            
    return render(request , 'teacher/Repassword.html' , {'data' : obj})


 
def History(request , id):
    obj = teacher.objects.get(id = id)
    data = leave.objects.all()
    print(obj.Name)
    return render(request , 'teacher/History.html' , {'data' : data , 'obj' : obj})