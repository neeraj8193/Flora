from django.db import models
    

class Contact(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    phone = models.CharField(max_length = 20)
    message =  models.TextField()
    Created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='category')
    description = models.TextField()
    created_at = models.DateTimeField( auto_now_add=True)
    def __str__(self):
        return self.title

class type_of_flower_pots(models.Model):
    title = models.CharField(max_length = 20)
    image = models.ImageField(upload_to='outdoor_plants')
  

    
    

    
    
    
    



