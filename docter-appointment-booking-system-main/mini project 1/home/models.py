from django.db import models

# Create your models here.
#class Signup(models.Model):
   # FirstName=models.CharField(max_length=122)
   # LastName=models.CharField(max_length=122)
    #Email=models.EmailField(max_length=122)
   # reemail=models.EmailField(max_length=122)
   # mobileno=models.CharField(max_length=10)
   # city=models.CharField(max_length=20)
   # password=models.CharField(max_length=20)
   # repassword=models.CharField(max_length=20)

class Sign(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    Email = models.EmailField(max_length=122, unique=True)
    reemail=models.EmailField(max_length=122)
    mobileno=models.CharField(max_length=10)
    city=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    repassword=models.CharField(max_length=20)
    def __str__(self):
        return self.firstname+self.lastname

#class Login(models.Model):
 #   username=models.EmailField(max_length=122)
  #  password=models.CharField(max_length=122)

class Appointment(models.Model):
    username=models.CharField(max_length=122)
    doctername=models.CharField(max_length=122)
    timeslot=models.CharField(max_length=122)
    def __str__(self):
        return self.username
