from django.shortcuts import render , redirect ,get_object_or_404
from .models import Contact , Feedback
from django.contrib import messages  
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime
from .forms import AddressForm , ProfileForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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

def selected_flowers_list(request):
    return render(request , 'selected_flowers_list.html' )

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

@login_required
def address_create(request):
    if request.method == 'POST' :
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request,"Address added successfully !")
            return redirect('address_create')
        else:
            messages.error(request,"Please fill all the fields correctly!")
    else:
        form = AddressForm()
    return render(request,'address_create.html',{
        'form':form,
    })

@login_required
def subscription_create(request):
    # check if user has created any address
    if not Address.objects.filter(user=request.user).exists():
        messages.error(request,"Please add address first!")
        return redirect('address_create')
    addressList = Address.objects.filter(user=request.user)
    if request.method == 'POST' :
        sub_type = request.POST.get('sub_type')
        start_date = request.POST.get('date')
        address_id = request.POST.get('address')
        user = request.user

        # check if date is valid or not 
        try:
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            # date is after today
            if start_date.date() >= datetime.datetime.now().date():
                if sub_type == 0:
                    expiry_date = start_date + datetime.timedelta(days=30)
                else:
                    expiry_date = start_date + datetime.timedelta(days=365)
                address = Address.objects.get(id=address_id)
                subscription = Subscription(user=user , start_date=start_date , expiry_date=expiry_date, status=False, address=address, sub_type=sub_type)
                subscription.save()
                # save subscription id in session
                request.session['subscription_id'] = subscription.id
                messages.success(request,"Subscription creation started!")
                return redirect('select_flowers')
            else:
                messages.error(request,"Please enter a valid date!")
                return redirect('subscription_create')
        except:
            messages.error(request,"Please enter a valid date!")
            return redirect('subscription_create')
    return render(request,'subscription_create.html', {
        'addressList':addressList,
    })

@login_required
def select_flowers(request):
    flowers = FlowersOption.objects.all()
    paginator = Paginator(flowers, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    sub_id = request.session.get('subscription_id')
    if request.method == 'POST' :
        flower_ids = request.POST.getlist('flowers')
        for fid in flower_ids:
            flower = FlowersOption.objects.get(id=fid)
            selected_flower = SelectedFlowers(user=request.user, flower=flower, subscription_id=sub_id)
            selected_flower.save()
        messages.success(request,"Flowers added successfully!")
        return redirect('payment_new')
    return render(request,'select_flowers.html',{
        'flowers':page_obj,
    })

@login_required
@csrf_exempt
def sub_new_payment(request):
    sub_id = request.session.get('subscription_id')
    subscription = Subscription.objects.get(id=sub_id)
    added_flowers = SelectedFlowers.objects.filter(subscription_id=sub_id) 
    return render(request,'payment_new.html',{
        'subscription':subscription,
        'selected_flowers':added_flowers,
    })

@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('create_profile')
    return render(request, 'profile.html' , {'profile':profile})

@login_required
def vendorprofile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('create_vendorprofile')
    return render(request, 'vendorprofile.html' , {'profile':profile})

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request,"Profile created successfully!")
            return redirect('profile')
        else:
            messages.error(request,"Please fill all the fields correctly!")
    else:
        form = ProfileForm()
    return render(request,'create_profile.html',{
        'form':form,
    })

def create_vendorprofile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request,"Profile created successfully!")
            return redirect('vendorprofile')
        else:
            messages.error(request,"Please fill all the fields correctly!")
    else:
        form = ProfileForm()
    return render(request,'create_vendorprofile.html',{
        'form':form,
    })

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if profile is None:
        return redirect('create_profile')
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # update
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profile")
    ctx = {
        "form": form,
    }
    return render(request, "edit_profile.html", ctx )


@login_required
def edit_vendorprofile(request):
    profile = Profile.objects.get(user=request.user)
    if profile is None:
        return redirect('create_vendorprofile')
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # update
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("vendorprofile")
    ctx = {
        "form": form,
    }
    return render(request, "edit_vendorprofile.html", ctx )

def add_to_subscription(request , prod):
    flower = FlowersOption.objects.get(prod = prod)
    user = request.user
    cart , _ = Cart.objects.get_or_create(user=user , is_paid = False)
    
    return redirect('select_flowers.html')

def add_to_session_cart(request):
    if request.method == 'POST':
        fid = request.POST.get('flower_id')
        qty = request.POST.get('qty')
        if 'flowers' in request.session:
            request.session['flowers'].append(fid)
        else:
            request.session['flowers'] = [fid]
        return HttpResponse("Added")
    
def remove_from_session_cart(request):
    if request.method == 'POST':
        fid = request.POST.get('flower_id')
        if 'flowers' in request.session:
            request.session['flowers'].remove(fid)
        return HttpResponse("Removed")
    
def clear_session_cart(request):
    if 'flowers' in request.session:
        del request.session['flowers']
    return HttpResponse("Cleared")

