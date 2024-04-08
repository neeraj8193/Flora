from django.shortcuts import render , redirect
from .models import Contact 
from django.contrib import messages 

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
            message.success(request,"Great Your Message has been sent successfully !")
            return redirect('contact')
        else :
            message.error(request,"Please fill all the fields and fill correctly!")
    
    return render(request,'contact.html')

