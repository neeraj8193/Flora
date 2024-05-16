"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from shop.views import *
from accounts.views import *
from django.contrib.auth import views as auth_view 



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', index, name='home'),
    path('contact', contact_details , name='contact'),
    path('maintenance/Form', maintenance , name='maintenance'),
    path('gallery', gallery_details , name='gallery'),

    path('menu', menu_details , name='menu'),
    path('about', about_details , name='about'),
    path('profile/view', profile , name='profile'),
    path('profile/edit', edit_profile , name='editprofile'),
    path('profile/create', create_profile , name='create_profile'),

    path('vendorprofile/view', vendorprofile , name='vendorprofile'),
    path('vendorprofile/edit', edit_vendorprofile , name='editvendorprofile'),
    path('vendorprofile/create', create_vendorprofile , name='create_vendorprofile'),
    # vendor add., edit, delete flowers
    path('flowers/add', add_flowers , name='add_flowers'),
    path('flowers/<int:id>/edit', edit_flowers , name='edit_flowers'),
    path('flowers/<int:id>/delete', delete_flowers , name='delete_flowers'),


    path('login/customer', customer_login_view, name='clogin'),
    path('register/customer', customer_register_view, name='cregister'),
    path('logout/', logout_view, name='logout'),

    path('vendor/login', vendor_login_view, name='vlogin'),
    path('vendor/register', vendor_register_view, name='vregister'),


    path('reset_password' , auth_view.PasswordResetView.as_view(template_name='password_reset.html' , email_template_name='password_reset_email.html',success_url='reset_password/sent') , name='password_reset' ),
    path('reset_password/sent' , auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html') , name='password_reset_done' ),
    path('reset/<uidb64>/<token>' , auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',
        success_url='reset_password/done') , name='password_reset_confirm' ),
    path('reset_password/done' , auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html') , name='password_reset_complete' ),



    path('subscription/taken',subscription_details, name='subscription_taken'),
    path('subscription/<int:id>/detail',subscription_item_details, name='subscription_details'),
    path('subscription/create',subscription_create, name='subscription_create'),
    path('select/flowers',select_flowers, name='select_flowers'),
    path('subscription/payment',sub_new_payment, name='payment_new'),
    path('checkout/session/create',create_checkout_session, name='checkout_session_create'),
    path('address/create',address_create, name='address_create'),
    path('address/<int:id>/edit',address_edit, name='address_edit'),
    path('address/<int:id>/delete', address_delete, name="address_delete"),
    path('feedback', feedback_details, name='feedback'),

    # success url
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
