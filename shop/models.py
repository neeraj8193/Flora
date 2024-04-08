from django.db import models
    

class Contact(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    phone = models.CharField(max_length = 20)
    message =  models.TextField()
    Created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    
    