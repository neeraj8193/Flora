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
from .forms import AddressForm , ProfileForm , VendorProfileForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import dotenv
import stripe
import os
from django.conf import settings
from django.core.mail import send_mail


def index(request):
    return render(request,'index.html')

def gallery_details(request):
    return render(request,'gallery.html')

def about_details(request):
    return render(request,'about.html')

def maintenance(request):
    return render(request,'maintenanceform.html')

def menu_details(request):
    return render(request,'menu.html', {
        'flowers':FlowersOption.objects.all(),
    })

def selected_flowers_list(request):
    return render(request , 'selected_flowers_list.html' )

def contact_details(request):
    if request.method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if len(name)>0 and len(email)>0 and len(phone)>=10 and len(message)>10 :
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


def subscription_details(request):
    return render(request,'subscription_list.html')

def subscription_item_details(request):
    return render(request,'subscription_list_items.html')


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
    stripe_public_key = settings.STRIPE_PK
    sub_id = request.session.get('subscription_id')
    subscription = Subscription.objects.get(id=sub_id)
    today = datetime.datetime.now().date()
    added_flowers = SelectedFlowers.objects.filter(subscription_id=sub_id)
    checkout_id = create_checkout_session(request)
    print(checkout_id)
    return render(request,'payment_new.html',{
        'subscription':subscription,
        'selected_flowers':added_flowers,
        'checkout_id':checkout_id,
        'spk':stripe_public_key,
    })

@csrf_exempt
def create_checkout_session(request):
    base_url = request.build_absolute_uri('/')[:-1]
    stripe.api_key = settings.STRIPE_SK
    print(stripe.api_key)
    sub_id = request.session.get('subscription_id')
    subscription = Subscription.objects.get(id=sub_id)
    added_flowers = SelectedFlowers.objects.filter(subscription_id=sub_id)
    user = request.user
    currency = 'inr'
    print('info')
    print(f'sub_id: {sub_id}')
    print(f'subscription: {subscription}')
    print(f'added_flowers: {added_flowers}')
    print(f'user: {user}')
    print(f'currency: {currency}')


    total_price = 0
    for flower in added_flowers:
        price = flower.flower.price
        qty  = flower.quantity
        total_price += price * qty

    print(f'total_price: {total_price}')
               
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        mode='payment',
        success_url=f'{base_url}/success/',
        cancel_url=f'{base_url}/cancel/',
        # customer name and info
        line_items=[
            {
                'price_data': {
                    'currency': currency,
                    'product_data': {
                        'name': 'Flora Subscription',
                    },
                    'unit_amount': int(total_price*100),
                },
                'quantity': 1,
                
            },
        ],
        customer_email=user.email,
        billing_address_collection='required',
    )
    return checkout_session.id

def success(request):
    sub_id = request.session.get('subscription_id')
    subscription = Subscription.objects.get(id=sub_id)
    subscription.is_payment_done = True
    subscription.save()
    # clear selected flowers
    SelectedFlowers.objects.filter(subscription_id=sub_id).delete()
    # clear subscription id from session
    del request.session['subscription_id']
    messages.success(request,"Payment successful!")
    return render(request,'success.html', {
        'subscription':subscription,
    })


def cancel(request):
    messages.error(request,"Payment failed!")
    return request('cancel.html')

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
        profile = VendorProfile.objects.get(user=request.user)
    except VendorProfile.DoesNotExist:
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
        form = VendorProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request,"Profile created successfully!")
            return redirect('vendorprofile')
        else:
            messages.error(request,"Please fill all the fields correctly!")
    else:
        form = VendorProfileForm()
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
    profile = VendorProfile.objects.get(user=request.user)
    if profile is None:
        return redirect('create_vendorprofile')
    form = VendorProfileForm(instance=profile)
    if request.method == "POST":
        form = VendorProfileForm(request.POST, request.FILES, instance=profile)
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

