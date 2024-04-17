from django.shortcuts import render , redirect 
from .models import Contact 
from django.contrib import messages 
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate , login


def index(request):
    return render(request,'index.html')


def contact_details(request):
    if request.method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if len(name)>0 and len(email)>0 and len(phone)>10 and len(message)>10 :
            contact = Contact(name=name , email=email , phone=phone , message=message)
            contact.save()
            messages.success(request,"Great Your Message has been sent successfully !")
            return redirect('contact')
        else :
            messages.error(request,"Please fill all the fields and fill correctly!")
    
    return render(request,'contact.html')


def customer_register(request):
    if request.method == 'POST' :
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')

        if password1 != password2 :
            messages.error(request,"Password and Confirm Password are not same! ")
        else :
            user = User.objects.create_user(
                fname,lname,email
            )
            user.set_password(password1)
            user.save()
            return redirect('Login')

    return render(request ,'customerRegister.html')


def customer_login(request):

    if request.method == 'POST' :
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request ,email=email, password=password)

        if user is not None :
            login(request,user)
            return redirect('home')
        
        else:
            messages.error(request,"Bad Credentials")

    return render(request , 'customerLogin.html') 