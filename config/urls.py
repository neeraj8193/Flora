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
from shop.views import contact_details
from shop.views import index
from shop.views import customer_login , customer_register



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', index, name='home'),
    path('contact', contact_details , name='contact'),
    path('Login', customer_login , name='Login'),
    path('SignUp', customer_register , name='SignUp'),

    path('vendor/login', TemplateView.as_view(template_name='vendorLogin.html'), name='vendor_login'),
    path('vendor/register', TemplateView.as_view(template_name='vendorRegister.html'), name='vendor_register'),
    path('listing', TemplateView.as_view(template_name='listing.html'), name='listing'),
    path('feedback', TemplateView.as_view(template_name='feedback.html'), name='feedback'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)