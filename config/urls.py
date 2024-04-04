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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('vendor/login', TemplateView.as_view(template_name='vendorLogin.html'), name='vendor_login'),
    path('vendor/register', TemplateView.as_view(template_name='vendorRegister.html'), name='vendor_register'),
    path('listing', TemplateView.as_view(template_name='listing.html'), name='listing'),
    path('customer/login', TemplateView.as_view(template_name='customerLogin.html'), name='customer_login'),
    path('customer/register', TemplateView.as_view(template_name='customerRegister.html'), name='customer_register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)