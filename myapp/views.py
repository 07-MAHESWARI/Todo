from django.shortcuts import render, redirect   # redirect

from django.views.generic import View

from myapp.forms import UserRegForm, LoginForm, TaskForm, ForgotPassForm

from myapp.models import User, TaskModel, OTPModel

from django.contrib.auth import authenticate, login, logout    # settings--> installed app --> contrib.auth

from django.core.mail import send_mail  # for mail

import random


# Create your views here.





class UserRegistrationView(View):

    def get(self,request):

        form = UserRegForm

        return render(request,"register.html", {"form":form})

    def post(self,request):      # storing data to db --> POST

        form = UserRegForm(request.POST)   

        if form.is_valid():   #  checking constraints

            print(form.cleaned_data) 

            username = form.cleaned_data.get("username")   

            password= form.cleaned_data.get("password")
            
            email = form.cleaned_data.get("email")

            first_name = form.cleaned_data.get("first_name")

            User.objects.create_user(username=username,email=email,password=password, first_name = first_name)
            #create_user --> password encryption . django only allows user to login only if the pass is encrypted

        form = UserRegForm

        # return render(request, "register.html",{"form":form})

        return redirect("login")    # user registration sucess aayi kazinj login pageil pokum
    

# loginView --> GET & POST

class LoginView(View):

    def get(self,request):

        form = LoginForm

        return render(request, "login.html",{"form":form})
    
    def post(self, request):

        form = LoginForm(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user_obj = authenticate(request, username=username, password=password)

            if user_obj:

                login(request,user_obj)

                return render(request,"index.html")
            
            else:

                form = LoginForm
            
                return render(request,"register.html",{"form":form})
            
# logout --> methods(GET)
class LogoutView(View):

    def get(self,request):

        logout(request)

        return redirect("login")    # whenever user logout it redirects to login page
    
# CRUD

#taskview --> method-GET and POST

class TaskView(View):

    def get(self, request):

        form = TaskForm

        return render(request,"task.html",{"form":form})    

    def post(self,request):

        form = TaskForm(request.POST)   

        # print(form.cleaned_data)

        if form.is_valid():

            TaskModel.objects.create(user_id=request.user, **form.cleaned_data)

            # request.user is an obj that keeps the LAST LOGIN as user
            # user_id is a foregn key that's why we give like this  or we get error
            return render(request,"taskresult.html")
        
        form = TaskForm

        return render(request,"task.html",{"form":form})   


# read view 
# url : localhost/task/read
# method - GET 

class TaskReadView(View):

    def get(self,request):

        data = TaskModel.objects.all()   # collections

        return render(request,"tasklist.html",{"items":data})
    
#update view
# GET method --> 

class TaskUpdateView(View):

    def get(self, request, **kwargs):   # id pass cheyanm

        id = kwargs.get("pk")


        data = TaskModel.objects.get(id = id)   # get the obj with the id from model table

        form = TaskForm(instance= data)   # data should be passed as intsnace

        return render(request,"update.html",{"form":form})
    
    def post(self, request, **kwargs):   # kwargs  {"pk":1}

        id = kwargs.get("pk")

        data = TaskModel.objects.get(id = id)

        form = TaskForm(request.POST,instance=data)

        if form.is_valid():

            form.save()

        form = TaskForm

        return render(request,"update.html",{"form":form})
    

# delete --> methods : GET

class TaskDeleteView(View):

    def get(self,request, **kwargs):

        id = kwargs.get("pk")

        TaskModel.objects.get(id = id).delete()

        # data.delete()

        return redirect("tasklist")   # redirect to list page
    
    
# details --> GET

#to get detials of specific task

class TaskDetailView(View):

    def get(self, request, **kwargs):

        id = kwargs.get("pk")

        data = TaskModel.objects.get(id = id)

        return render(request, "detail.html",{"data":data})
    
#complted status = True
# localhost:task/task_edit/1
# method : GET 
# 
class TaskStatusEdit(View):

    def get(self, request, **kwargs):

        id = kwargs.get("pk")

        data = TaskModel.objects.get(id = id)

        print(data)

        data.complete_status = 1   # doubt(23/04)

        data.save()

        return redirect("tasklist")


# 24/04
"""
Forgot password view
==================
get > form :: email
post > m@gmail.com

opt view
======
get: form :: otp
post : entered_otp == otp

redirect

reset password view
================
get : form password confirm password
post :: sdet_password()

return redirect


email and otp--> 
host mail, key, smtp authentication etc 
"""
class ForgotPassView(View):

    def get(self, request):

        form = ForgotPassForm

        return render(request, "forgot.html",{"form":form})

    def post(self, request):

        form = ForgotPassForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data.get("email")

            user_id = User.objects.get(email = email)   # get the email from User table that matching the email that we typed

            otp = random.randint(1000,9999)
            
            OTPModel.objects.create(user_id = user_id, otp=otp)

            # SMTP GATEWAY --->  
            # send_mail is imported and we should provide the details as per the class like subject, msg etc
            send_mail(subject="otp for pwd reset",message=str(otp), from_email="maheswariammu101010@gmail.com",
                      recipient_list=[email])
            
            return redirect("forgot")
            

            
# pzeu tptl ncpr bspy









"""
#Note 
===============

login
logout

user_id=request.user

instance
save
"""