from django.db import models

# Create your models here.

class Registerimg(models.Model):
    email= models.CharField( max_length=50)
    password=models.CharField( max_length=25)
    confirmpassword=models.CharField( max_length=25)
    collegename=models.CharField( max_length=50)
    collegeemail=models.CharField( max_length=50)
    stream=models.CharField( max_length=30)
    year=models.CharField( max_length=30)
    firstname=models.CharField( max_length=50)
    lastname=models.CharField( max_length=50)
    phone=models.CharField( max_length=60)
    address=models.CharField( max_length=60)
    pic=models.ImageField(upload_to='collegeid')


    def __str__(self):
        return self.email
    

