from django.db import models
from django.contrib.auth.models import User 
    
    
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE , null = True , blank = True)
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    phone = models.CharField(max_length = 20)
    message =  models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
 
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
        ('All','All'),
    )

    maintainance_type = (
        ('low','low'),
        ('medium','medium'),
        ('high','high'),
    )

    name = models.CharField(max_length = 20)
    image = models.ImageField(upload_to='flowers/')
    description = models.TextField()
    season_type= models.CharField(max_length=20,choices=season_type)
    maintainance_type = models.CharField(max_length=20,choices=maintainance_type)
    price = models.FloatField()
    
    def __str__(self):
        return self.name

class Address(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE , null = True , blank = True)
    address_line_1 = models.CharField(max_length = 225)
    address_line_2 = models.CharField(max_length = 255, blank = True, null = True)
    landmark = models.CharField(max_length = 20, blank = True, null = True)
    city = models.CharField(max_length = 20)
    state = models.CharField(max_length = 20)
    pincode = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"""{self.address_line_1},\n
        {self.address_line_2}\n
        {self.landmark},\n
        {self.city},\n
        {self.state},\n
        {self.pincode}\n
        """


class Subscription(models.Model):
    sub_type_choices = (
        (0,'monthly'),
        (1,'yearly'),
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE , null = True , blank = True)
    start_date = models.DateField(auto_now_add = True)
    expiry_date = models.DateField()
    price = models.FloatField(blank=True,null=True)
    sub_type = models.IntegerField(choices=sub_type_choices)
    is_payment_done = models.BooleanField(default=False)
    address = models.ForeignKey(Address, on_delete = models.CASCADE , null = True , blank = True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    transaction_id = models.CharField(max_length = 255, blank = True, null = True)

    def __str__(self):
        return self.user.username

class SelectedFlowers(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE , null = True , blank = True)
    flower = models.ForeignKey(FlowersOption, on_delete = models.CASCADE , null = True , blank = True)
    subscription = models.ForeignKey(Subscription, on_delete = models.CASCADE , null = True , blank = True)
    quantity = models.IntegerField(default=1)    
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.user.username

class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE , null = True , blank = True)
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    phone = models.CharField(max_length = 20)
    address = models.ForeignKey(Address, on_delete = models.CASCADE , null = True , blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length = 150)
    about = models.TextField(max_length=100 , null = True)
    image = models.ImageField(default='media/profile_imagedefault.png' , upload_to='profile_image', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class VendorProfile(models.Model):
    email = models.EmailField()
    phone = models.CharField( max_length=10)
    address = models.CharField(max_length = 150)
    about = models.TextField(max_length=100 , null = True)
    image = models.ImageField(default='media/default.jpg' , upload_to='profile_image', null=True, blank=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE , null = True , blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.user.username


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='carts')
    is_paid = models.BooleanField(default=False)

class CartItems(models.Model):
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE , related_name='cart_items')
    product = models.ForeignKey(FlowersOption , on_delete = models.SET_NULL , null = True , blank=True)
    def get_price(self):
        price=[self.product.price]
        return sum(price)