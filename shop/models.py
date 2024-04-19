from django.db import models
from django.contrib.auth.models import User 
    

class Contact(models.Model):

    user = models.ForeignKey(User, on_delete = models.SET_NULL , null = True , blank = True)
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    phone = models.CharField(max_length = 20)
    message =  models.TextField()
    Created_at = models.DateTimeField(auto_now_add = True)
 



    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    message =  models.TextField()
    rating= models.IntegerField()

    def __str__(self):
        return self.name
    
    
class FlowersOption(models.Model):
    season_type = (
        ('summer','summer'),
        ('winter','winter'),
        ('spring','spring'),
        ('autumn','autumn'),
    )
    maintainance_type = (
        ('low','low'),
        ('medium','medium'),
        ('high','high'),
    )
    name = models.CharField(max_length = 20)
    price = models.FloatField()
    image = models.ImageField(upload_to='flowers/')
    description = models.TextField()
    season_type= models.CharField(max_length=20,choices=season_type)
    maintainance_type = models.CharField(max_length=20,choices=maintainance_type)
    
    
    def __str__(self):
        return self.name


class Subscription(models.Model):
    user= models.ForeignKey(User, on_delete = models.SET_NULL , null = True , blank = True)
    price = models.FloatField()
    start_date = models.DateField()
    paymeent_type = models.CharField(max_length=20)
    is_payment_done = models.BooleanField(default=False)
    vendor = models.CharField(max_length=20)
    subscription_type = models.CharField(max_length=20)
    next_payment_date = models.DateField()
    def __str__(self):
        return self.user.username
    
class SelectedFlowers(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL , null = True , blank = True)
    quantity = models.IntegerField()
    price = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_payment_done = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
