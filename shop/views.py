from django.shortcuts import render , redirect 
from .models import Contact , Feedback
from django.contrib import messages  
from .models import *

def index(request):
    return render(request,'index.html')

def about_details(request):
    return render(request,'about.html')

def menu_details(request):
    return render(request,'menu.html', {
        'flowers':FlowersOption.objects.all(),
    })

def subscription_details(request):
    return render(request,'subscription.html')

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

def feedback_details(request):
    if request.method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        rating = request.POST.get('star')

        if len(name)>0  and len(email)>6 and len(message)>10 :
            feedback = Feedback(name=name , email=email , message=message , rating=rating)
            feedback.save()
            messages.success(request,"Your Feedback has been sent successfully !")
            return redirect('feedback')
        else :
            messages.error(request,"Please fill all the fields correctly!")
    return render(request,'feedback.html')

